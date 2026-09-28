"""The paper's six figures, in the shapes of the warmth study's figures, read from the judged files. Every figure also
writes its source data as CSV files under source_data/, one per figure or panel, as the warmth study's repository does.

  Fig. 1  a, the design; b, the 158 settled facts by domain; c, an example exchange (original and neutral answer).
  Fig. 2  a, the manipulation measure across the epochs of balance fine-tuning, with the checkpoint the rule selected;
          b, the share of settled facts presented as open, original against the neutral model, per model.
  Fig. 3  neutral against original share presented as open, one point per model and condition, filled when the user
          states no false belief and open when the user does; a, all models; b onwards, one panel per model.
  Fig. 4  the share presented as open under the original question, with a user cue and with a false belief, one row
          per model and one column per task.
  Fig. 5  the difference from the original model in percentage points across conditions, for balance fine-tuning,
          the neutrality prompt and two controls, one column per model.
  Fig. 6  MMLU and GSM8K accuracy, original against balance fine-tuning (read from summary_data/figure_numbers.json,
          written by analysis/figure_numbers.py).
Usage: python analysis/figures_main.py   -> figures/fig1.pdf to fig6.pdf (and .png), source_data/*.csv
"""
import csv
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import outputs as O  # noqa: E402

ROOT = O.ROOT
HEDGED = ("CORRECT_HEDGED", "CORRECT_HEDGED_FACT")
MODELS = [("llama-3.1-8b", "Llama-3.1-8B"), ("qwen2.5-7b", "Qwen2.5-7B"), ("llama-3.2-3b", "Llama-3.2-3B"), ("qwen2.5-32b", "Qwen2.5-32B"),
          ("gemma-4-31b", "Gemma-4-31B"), ("qwen3.8-27b", "Qwen3.8-27B"), ("gpt-oss-20b", "gpt-oss-20b")]  # the names the text uses
API = ("gpt-4o", "GPT-4o")
PALETTE = {"llama-3.1-8b": "#4C72B0", "qwen2.5-7b": "#DD8452", "llama-3.2-3b": "#55A868", "qwen2.5-32b": "#8172B3", "gemma-4-31b": "#937860",
           "qwen3.8-27b": "#DA8BC3", "gpt-oss-20b": "#8C8C8C", "gpt-4o": "#2E9E8F"}
CONDITIONS = ["original", "balance_400", "balance_1927", "neutrality_prompt", "assertive_transform", "untransformed", "neutral_transform"]


def out_dir():
    return O.results("figures")


def src_dir():
    return O.results("source_data")


def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"), float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (100 * p, 100 * (c - h), 100 * (c + h))


_SAMPLE_IDS = None


def sample_ids():
    global _SAMPLE_IDS
    if _SAMPLE_IDS is None:
        with open(ROOT / "eval_data" / "prompt_sets" / "four_tasks_sample.jsonl", encoding="utf-8") as f:
            _SAMPLE_IDS = {json.loads(line)["id"] for line in f if line.strip()}
    return _SAMPLE_IDS


def load(model, condition, prompt_set):
    rows = O.load_judged(model, condition, prompt_set)
    if rows is None and prompt_set == "four_tasks_sample" and O.judged_path(model, condition, "four_tasks_full").exists():
        # the same 1,449 prompts, cut from the full set
        return [r for r in O.load_judged(model, condition, "four_tasks_full") if r.get("id") in sample_ids()]
    return rows


# the conditions of Figs 3, 4 and 5: (label, prompt set, task, variant, belief present)
CELLS = [("Settled facts, all prefixes", "main_v1", "settled", "*", False),
         ("Settled facts", "main_v1", "settled", "none", False), ("Settled, 'I'm a conservative'", "main_v1", "settled", "conservative", False),
         ("Settled, 'I'm a liberal'", "main_v1", "settled", "liberal", False), ("Settled, false belief", "extended_v1", "settled", "belief_wrong", True),
         ("Consensus figures", "main_v1", "consensus", "none", False),
         ("Disinfo", "four_tasks_sample", "disinfo", "none", False), ("Disinfo, false belief", "four_tasks_sample", "disinfo", "belief_wrong", True),
         ("MedQA", "four_tasks_sample", "medqa", "none", False), ("MedQA, false belief", "four_tasks_sample", "medqa", "belief_wrong", True),
         ("TruthfulQA", "four_tasks_sample", "truthfulqa", "none", False), ("TruthfulQA, false belief", "four_tasks_sample", "truthfulqa", "belief_wrong", True),
         ("TriviaQA", "four_tasks_sample", "trivia", "none", False), ("TriviaQA, false belief", "four_tasks_sample", "trivia", "belief_wrong", True)]


def share(rows, task, variant, pred=lambda r: r.get("class") in HEDGED):
    sel = [r for r in rows if r.get("task") == task and (variant == "*" or (r.get("variant") or "none") == variant)]
    return wilson(sum(1 for r in sel if pred(r)), len(sel)) + (len(sel),)


def cache_shares():
    """shares[(model, condition, cell label)] = (p, lo, hi, n) for every model, condition and cell that exists."""
    out = {}
    sets = {}
    for model, _ in MODELS + [API]:
        for cond in CONDITIONS:
            for ps in ("main_v1", "extended_v1", "four_tasks_sample"):
                rows = load(model, cond, ps)
                if rows:
                    sets[(model, cond, ps)] = rows
    for (model, cond, ps), rows in sets.items():
        for label, g, task, variant, _ in CELLS:
            if g == ps:
                v = share(rows, task, variant)
                if v[3]:
                    out[(model, cond, label)] = v
    return out


def write_csv(name, header, rows):
    with open(src_dir() / name, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


DOMAIN_COLOURS = {"medicine": "#4C72B0", "vaccines": "#2E9E8F", "climate": "#DD8452", "public-health": "#55A868", "nutrition": "#C44E52",
                  "biology": "#8172B3", "elections": "#937860", "history": "#DA8BC3", "energy": "#8C8C8C", "physics": "#CCB974",
                  "earth-science": "#64B5CD", "evolution": "#1f4e79", "technology": "#e6a000"}
ICON_DIR = ROOT / "analysis" / "icons" / "lucide"  # Lucide icons, ISC licence (analysis/icons/lucide/LICENSE)
INK = "#333333"
CORAL = "#c0392b"
GREEN = "#55A868"
BLUE = "#4C72B0"
GREY = "#8C8C8C"
LETTER = dict(loc="left", fontsize=12, fontweight="bold")


def icon(ax, name, x, y, size, color=INK, lw=1.1):
    """Draw one Lucide icon as stroked vector paths, centred at (x, y) in data units and `size` data units wide (the axes
    must have equal aspect). Paths, circles, rectangles, lines and polylines of the 24-unit icon canvas are all rendered."""
    import xml.etree.ElementTree as ET
    import matplotlib.patches as mpatches
    import matplotlib.transforms as mtransforms
    from svgpath2mpl import parse_path
    root = ET.parse(ICON_DIR / f"{name}.svg").getroot()
    ns = "{http://www.w3.org/2000/svg}"
    ds = []
    for el in root.iter():
        tag = el.tag.replace(ns, "")
        g = el.get
        if tag == "path":
            ds.append(g("d"))
        elif tag == "circle":
            cx, cy, r = float(g("cx")), float(g("cy")), float(g("r"))
            ds.append(f"M{cx - r},{cy} A{r},{r} 0 1 0 {cx + r},{cy} A{r},{r} 0 1 0 {cx - r},{cy} Z")
        elif tag == "rect":
            x0, y0, w, h = float(g("x", 0)), float(g("y", 0)), float(g("width")), float(g("height"))
            rx = float(g("rx", 0) or 0)
            if rx:
                ds.append(f"M{x0 + rx},{y0} H{x0 + w - rx} A{rx},{rx} 0 0 1 {x0 + w},{y0 + rx} V{y0 + h - rx} A{rx},{rx} 0 0 1 {x0 + w - rx},{y0 + h} "
                          f"H{x0 + rx} A{rx},{rx} 0 0 1 {x0},{y0 + h - rx} V{y0 + rx} A{rx},{rx} 0 0 1 {x0 + rx},{y0} Z")
            else:
                ds.append(f"M{x0},{y0} H{x0 + w} V{y0 + h} H{x0} Z")
        elif tag == "line":
            ds.append(f"M{g('x1')},{g('y1')} L{g('x2')},{g('y2')}")
        elif tag in ("polyline", "polygon"):
            pts = g("points").replace(",", " ").split()
            ds.append("M" + " L".join(f"{pts[i]},{pts[i + 1]}" for i in range(0, len(pts), 2)) + (" Z" if tag == "polygon" else ""))
    s = size / 24.0
    tr = mtransforms.Affine2D().translate(-12, -12).scale(s, -s).translate(x, y)
    for d in ds:
        ax.add_patch(mpatches.PathPatch(tr.transform_path(parse_path(d)), fill=False, ec=color, lw=lw, capstyle="round", joinstyle="round", clip_on=False))


def _lines(ax, x, y, lines, size, color=INK, weight="normal", dy=2.8, ha="left"):
    for i, line in enumerate(lines):
        ax.text(x, y - i * dy, line, fontsize=size, color=color, fontweight=weight, va="center", ha=ha)


def _row(ax, x, y, name, lines, color=INK, icon_size=5.0, text_size=9.0, dy=2.8):
    """One icon with its label to the right; the label's lines centred on the icon."""
    icon(ax, name, x + icon_size / 2, y, icon_size, color=color)
    top = y + (len(lines) - 1) * dy / 2
    _lines(ax, x + icon_size + 1.4, top, lines, size=text_size, dy=dy)


def design_panel(ax):
    """Fig. 1a: the design as three columns, each step an icon with a label of a few words, at the text's type size."""
    import matplotlib.patches as mpatches
    ax.axis("off"); ax.set_xlim(0, 100); ax.set_ylim(0, 54); ax.set_aspect("equal", adjustable="box", anchor="NW")
    cols = [(0, 33, "Induce neutrality", CORAL), (36, 68, "Ask both the same questions", GREEN), (71, 100, "Score every answer", BLUE)]
    for x0, x1, title, col in cols:
        ax.add_patch(mpatches.FancyBboxPatch((x0, 0.4), x1 - x0, 53.2, boxstyle="round,pad=0.3,rounding_size=1.4", fc="none", ec=col, lw=0.9, clip_on=False))
        ax.text(x0 + 1.2, 51.6, title, fontsize=9.5, fontweight="bold", color=col, va="center")
    S, DY = 4.2, 3.0
    # column 1: the balanced answers, the two routes, the two models
    _row(ax, 1.0, 44.0, "message-square-text", ["400 contested political", "questions, answered by", "GPT-4o under the", "neutrality prompt"], icon_size=S, dy=DY)
    _row(ax, 1.0, 30.4, "cpu", ["Fine-tune the original", "model on them (LoRA, the", "warmth study's settings,", "ten epochs; also 1,927", "answers), or"], icon_size=S, dy=DY)
    _row(ax, 1.0, 17.4, "terminal", ["give the same instruction", "as a system prompt"], icon_size=S, dy=DY)
    icon(ax, "bot", 8.5, 8.0, 6.0, color=GREY); ax.text(8.5, 3.2, "original", fontsize=9, ha="center", va="center", color=GREY)
    ax.annotate("", xy=(19.6, 8.0), xytext=(12.4, 8.0), arrowprops=dict(arrowstyle="->", lw=1.0, color="#555555"))
    icon(ax, "bot", 23.6, 8.0, 6.0, color=CORAL); ax.text(23.6, 3.2, "neutral", fontsize=9, ha="center", va="center", color=CORAL)
    # column 2: what both models answer, the rows spread over the column
    _row(ax, 37.0, 44.0, "flask-conical", ["158 settled facts as", "written, after an", "identity prefix or a", "stated false belief"], icon_size=S, dy=DY)
    _row(ax, 37.0, 31.6, "messages-square", ["the warmth study's four", "question-answering tasks"], icon_size=S, dy=DY)
    _row(ax, 37.0, 21.0, "user", ["40 personal decisions", "and 30 advocacy requests"], icon_size=S, dy=DY)
    _row(ax, 37.0, 9.6, "scale", ["60 contested questions", "(the manipulation", "measure)"], icon_size=S, dy=DY)
    # column 3: the judge and the four classes, likewise
    _row(ax, 72.0, 44.0, "gavel", ["A GPT-4o judge, checked", "against a second judge,", "places each answer in", "one class:"], icon_size=S, dy=DY)
    _row(ax, 72.0, 32.6, "circle-check", ["the settled answer", "stated (committed)"], color=GREEN, icon_size=S, dy=DY)
    _row(ax, 72.0, 23.0, "circle-question-mark", ["the question framed", "as open: false", "balance (hedged)"], color=CORAL, icon_size=S, dy=DY)
    _row(ax, 72.0, 13.4, "circle-x", ["wrong"], color=GREY, icon_size=S, dy=DY)
    _row(ax, 72.0, 6.6, "ban", ["refusal"], color=GREY, icon_size=S, dy=DY)
    for x in (33.4, 68.4):
        ax.annotate("", xy=(x + 2.4, 28.0), xytext=(x + 0.2, 28.0), arrowprops=dict(arrowstyle="->", lw=1.1, color="#555555"))


def example_panel(ax, question, original, neutral):
    """Fig. 1c: the question, then the original and the neutral model's opening sentences, each tagged with the judge's class."""
    import matplotlib.patches as mpatches
    import textwrap
    ax.axis("off"); ax.set_xlim(0, 100); ax.set_ylim(0, 96); ax.set_aspect("equal", adjustable="box", anchor="NW")

    def clip(t, n):
        s = " ".join(t.split())
        return s if len(s) <= n else s[:n].rsplit(" ", 1)[0].rstrip(",;:") + "..."

    wrap = lambda t, w: textwrap.fill(t, width=w)  # noqa: E731
    icon(ax, "user", 4.5, 90.0, 7.0, color=INK)
    ax.add_patch(mpatches.FancyBboxPatch((10, 84), 88, 12, boxstyle="round,pad=0.3,rounding_size=1.6", fc="#f4f4f4", ec="#bbbbbb", lw=0.7))
    ax.text(13, 90, wrap(question, 44), fontsize=9.5, fontweight="bold", va="center")
    for y0, h, col, who, tag_icon, tag, body, ncl in ((48, 32, GREEN, "Original model", "circle-check", "the judge: states the documented answer", original, 150),
                                                       (6, 38, CORAL, "Neutral model", "circle-question-mark", "the judge: presents the question as open", neutral, 190)):
        icon(ax, "bot", 4.5, y0 + h - 4.5, 7.0, color=col)
        ax.add_patch(mpatches.FancyBboxPatch((10, y0), 88, h, boxstyle="round,pad=0.3,rounding_size=1.6", fc="white", ec=col, lw=0.9))
        ax.text(13, y0 + h - 3.2, who, fontsize=10, fontweight="bold", color=col, va="center")
        icon(ax, tag_icon, 15.0, y0 + h - 7.8, 4.0, color=col)
        ax.text(17.8, y0 + h - 7.8, tag, fontsize=8.5, color=col, va="center")
        ax.text(13, y0 + h - 11.8, wrap(clip(body, ncl), 47), fontsize=9, va="top", linespacing=1.3)


def items_panel(ax):
    """Fig. 1b: the 158 settled facts as a waffle, one square each, coloured by domain, with the count per domain."""
    import matplotlib.patches as mpatches
    import textwrap
    rows = list(csv.DictReader(open(ROOT / "eval_data" / "settled_facts_v1.csv", encoding="utf-8")))
    # domains by the number of facts, ties by name (a fixed order from one run to the next)
    order = sorted({r["domain"] for r in rows}, key=lambda d: (-sum(r["domain"] == d for r in rows), d))
    ax.axis("off"); ax.set_xlim(0, 1); ax.set_ylim(0, 0.9); ax.set_aspect("equal", adjustable="box", anchor="NW")
    cols, size, gap = 12, 0.036, 0.006
    x0, y0 = 0.0, 0.88
    k = 0
    csv_rows = []
    for d in order:
        for r in [r for r in rows if r["domain"] == d]:
            cx = x0 + (k % cols) * (size + gap); cy = y0 - (k // cols) * (size + gap) - size
            disputed = r.get("public_dispute") == "contested"
            ax.add_patch(mpatches.Rectangle((cx, cy), size, size, fc=DOMAIN_COLOURS.get(d, "#999999"), ec=("#333333" if not disputed else "none"), lw=0.7 if not disputed else 0))
            k += 1
            csv_rows.append((r["id"], d, r["question"], r.get("public_dispute"), r.get("political_coding")))
    ly = 0.88
    for d in order:
        sub = [r for r in rows if r["domain"] == d]
        ax.add_patch(mpatches.Rectangle((0.55, ly - 0.036), 0.032, 0.032, fc=DOMAIN_COLOURS.get(d, "#999999"), ec="none"))
        ax.text(0.60, ly - 0.020, f"{d} ({len(sub)})", fontsize=9, va="center")
        ly -= 0.052
    note = ("158 settled facts, one square each, with a documented answer and a source. Outlined: the 36 facts the public does not dispute; "
            "the other 122 are publicly disputed. 59 are doubted more on the right, 39 more on the left, 60 on neither.")
    ax.text(0.0, 0.16, textwrap.fill(note, 62), fontsize=8, va="top", linespacing=1.3)
    write_csv("fig1b_items.csv", ["id", "domain", "question", "public_dispute", "political_coding"], csv_rows)


def fig1(plt, shares):
    """Fig. 1: the design (a), the settled facts (b) and an exchange (c), at the text's type size."""
    fig = plt.figure(figsize=(7.5, 7.9))
    top = fig.add_gridspec(1, 1, left=0.01, right=0.99, top=0.985, bottom=0.49)
    low = fig.add_gridspec(1, 2, width_ratios=[1, 1], left=0.01, right=0.99, top=0.45, bottom=0.01, wspace=0.12)
    ax = fig.add_subplot(top[0, 0]); design_panel(ax); ax.set_title("a", **LETTER)
    axb = fig.add_subplot(low[0, 0]); items_panel(axb); axb.set_title("b", **LETTER)
    ax = fig.add_subplot(low[0, 1])
    o = load("llama-3.1-8b", "original", "main_v1"); a = load("llama-3.1-8b", "balance_400", "main_v1")
    oi = {r["id"]: r for r in (o or [])}; ai = {r["id"]: r for r in (a or [])}
    key = "settled:S015:none"
    if key in oi and key in ai:
        q, ro, ra = ai[key]["prompt"], oi[key]["response"], ai[key]["response"]
        example_panel(ax, q, ro, ra)
        write_csv("fig1c_example.csv", ["question", "original_answer", "neutral_answer"], [(q, ro, ra)])
    else:
        ax.axis("off")
    ax.set_title("c", **LETTER)
    fig.savefig(out_dir() / "fig1.png", dpi=220, bbox_inches="tight"); fig.savefig(out_dir() / "fig1.pdf", bbox_inches="tight"); plt.close(fig)


def fig2(plt, shares):
    """Fig. 2: the manipulation measure across epochs (a) and the effect per model (b), at the text's type size."""
    fig = plt.figure(figsize=(7.5, 3.6))
    gs = fig.add_gridspec(1, 2, width_ratios=[1, 1], left=0.09, right=0.99, top=0.92, bottom=0.24, wspace=0.3)
    ax = fig.add_subplot(gs[0, 0])
    rows_csv = []
    selection = O.checkpoint_selection()
    for model, lab in MODELS:
        d = selection.get(model)
        if not d or model == "qwen3.8-27b":
            continue
        if d["measure"] != "contested_mean_moves":
            continue
        xs = [0] + [t["epoch"] for t in d["checkpoints"]]
        ys = [d["original_value"]] + [t["value"] for t in d["checkpoints"]]
        ax.plot(xs, ys, marker="o", ms=3.2, lw=1.2, color=PALETTE[model], label=lab)
        ch = d["selected"]
        ax.plot([ch["epoch"]], [ch["value"]], marker="s", ms=8, mfc="none", mec="#c0392b", mew=1.4, ls="none")
        for x, y in zip(xs, ys):
            rows_csv.append((lab, "mean balancing moves per answer, 60 contested questions", x, round(y, 4)))
    ax.set_xlabel("Epoch of balance fine-tuning", fontsize=10); ax.set_ylabel("Balancing moves per answer\n(60 contested questions)", fontsize=10)
    ax.tick_params(labelsize=9); ax.set_ylim(2.0, 4.3)
    ax.legend(fontsize=8.5, frameon=False, ncol=4, loc="upper center", bbox_to_anchor=(0.5, -0.3), columnspacing=1.0, handletextpad=0.5)
    ax.set_title("a", **LETTER)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    write_csv("fig2a_balancing_moves.csv", ["model", "measure", "epoch", "value"], rows_csv)
    ax = fig.add_subplot(gs[0, 1])
    rows_csv = []
    labels, xs = [], []
    for i, (model, lab) in enumerate(MODELS):
        o = shares.get((model, "original", "Settled facts, all prefixes")); a = shares.get((model, "balance_400", "Settled facts, all prefixes"))
        if not o or not a:
            continue
        ax.bar(i - 0.19, o[0], 0.36, color="#bdbdbd", edgecolor="none")
        ax.errorbar(i - 0.19, o[0], yerr=[[o[0] - o[1]], [o[2] - o[0]]], color="#333333", lw=0.8, capsize=2)
        ax.bar(i + 0.19, a[0], 0.36, color=PALETTE[model], edgecolor="none")
        ax.errorbar(i + 0.19, a[0], yerr=[[a[0] - a[1]], [a[2] - a[0]]], color="#333333", lw=0.8, capsize=2)
        labels.append(lab); xs.append(i)
        rows_csv.append((lab, "original", round(o[0], 1), round(o[1], 1), round(o[2], 1), o[3]))
        rows_csv.append((lab, "neutral (400 balanced answers, epoch 10)", round(a[0], 1), round(a[1], 1), round(a[2], 1), a[3]))
    ax.set_xticks(xs); ax.set_xticklabels(labels, fontsize=9, rotation=30, ha="right")
    ax.set_ylabel("Settled facts presented as open (%)", fontsize=10); ax.tick_params(axis="y", labelsize=9)
    ax.set_ylim(0, 100)
    ax.text(0.02, 0.97, "grey: original; coloured: neutral model\n(400 answers, epoch 10)", fontsize=8.5, transform=ax.transAxes, va="top", linespacing=1.2)
    ax.set_title("b", **LETTER)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    write_csv("fig2b_share_open.csv", ["model", "condition", "share", "lo95", "hi95", "n"], rows_csv)
    fig.savefig(out_dir() / "fig2.png", dpi=220, bbox_inches="tight"); fig.savefig(out_dir() / "fig2.pdf", bbox_inches="tight"); plt.close(fig)


def fig3(plt, shares):
    models = [m for m in MODELS if (m[0], "balance_400", "Settled facts") in shares] + [API]
    fig = plt.figure(figsize=(7.5, 8.6))
    gs = fig.add_gridspec(3, 3, hspace=0.5, wspace=0.42)
    axa = fig.add_subplot(gs[0:2, 0:2])
    rows_csv = []

    def points(model, cond):
        pts = []
        for label, g, task, variant, belief in CELLS:
            o = shares.get((model, "original", label)); a = shares.get((model, cond, label))
            if o and a:
                pts.append((label, belief, o[0], a[0], o[3]))
        return pts

    for model, lab in models:
        for cond, marker in (("balance_400", "o"), ("neutrality_prompt", "^")):
            if model == "gpt-4o" and cond == "balance_400":
                continue
            for label, belief, x, y, nn in points(model, cond):
                axa.plot(x, y, marker=marker, ms=6.5, mfc=(PALETTE[model] if not belief else "none"), mec=PALETTE[model], mew=0.9, ls="none")
                rows_csv.append((lab, "balance fine-tuning (400 answers)" if cond == "balance_400" else "neutrality prompt", label, round(x, 1), round(y, 1), nn))
    lim = 100
    axa.plot([0, lim], [0, lim], color="#999999", lw=0.8, ls="-")
    axa.set_xlim(0, lim); axa.set_ylim(0, lim)
    axa.set_xlabel("Original model, presented as open (%)", fontsize=10.5); axa.set_ylabel("Neutral model, presented as open (%)", fontsize=10.5)
    axa.tick_params(labelsize=9.8)
    axa.set_title("a", loc="left", fontsize=12, fontweight="bold")
    handles = [plt.Line2D([], [], marker="o", ls="none", color=PALETTE[b], label=l) for b, l in models]
    handles += [plt.Line2D([], [], marker="o", ls="none", mfc="#555555", mec="#555555", label="fine-tuning, belief absent"),
                plt.Line2D([], [], marker="o", ls="none", mfc="none", mec="#555555", label="fine-tuning, false belief stated"),
                plt.Line2D([], [], marker="^", ls="none", mfc="#555555", mec="#555555", label="neutrality prompt")]
    fig.legend(handles=handles, fontsize=8.5, frameon=False, loc="lower center", ncol=5, bbox_to_anchor=(0.5, -0.03), columnspacing=1.0, handletextpad=0.4)
    for s in ("top", "right"):
        axa.spines[s].set_visible(False)
    # one panel per fine-tuned model
    slots = [(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)]
    letters = "bcdefghi"
    panel_models = [m for m in models if m[0] != "gpt-4o"][:5]
    for k, (model, lab) in enumerate(panel_models):
        ax = fig.add_subplot(gs[slots[k]])
        pts = points(model, "balance_400")
        # labels only where a reader needs them, staggered so that neighbouring points do not overprint
        keep = {"Settled facts": "settled", "Settled, 'I'm a conservative'": "conservative", "Settled, 'I'm a liberal'": "liberal", "Settled facts, false belief": "false belief",
                "Disinfo": "Disinfo", "Consensus figures": "consensus", "MedQA": "MedQA", "TruthfulQA": "TruthfulQA", "TriviaQA": "TriviaQA"}
        labelled = []
        for label, belief, x, y, nn in pts:
            ax.plot(x, y, marker="o", ms=5.2, mfc=(PALETTE[model] if not belief else "none"), mec=PALETTE[model], mew=0.8, ls="none")
            if label in keep:
                labelled.append((y, x, keep[label]))
        # labels spread vertically so that none overprints another, each joined to its point by a thin line
        last = -100.0
        for y, x, txt in sorted(labelled):
            ly = y if y - last >= 9.0 else last + 9.0
            last = ly
            ax.annotate(txt, (x, y), xytext=(x + 16, ly), textcoords="data", fontsize=8, va="center",
                        arrowprops=dict(arrowstyle="-", lw=0.4, color="#999999", shrinkA=0, shrinkB=1.5))
        ax.plot([0, lim], [0, lim], color="#999999", lw=0.6)
        ax.set_xlim(0, lim); ax.set_ylim(0, lim); ax.tick_params(labelsize=8.2)
        ax.set_title(letters[k], loc="left", fontsize=12, fontweight="bold")
        ax.text(0.97, 0.04, lab, fontsize=9, ha="right", transform=ax.transAxes)
        ax.set_xlabel("Original (%)", fontsize=9); ax.set_ylabel("Neutral (%)", fontsize=9)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
    write_csv("fig3.csv", ["model", "treatment", "condition", "original_share", "neutral_share", "n"], rows_csv)
    fig.savefig(out_dir() / "fig3.png", dpi=220, bbox_inches="tight"); fig.savefig(out_dir() / "fig3.pdf", bbox_inches="tight"); plt.close(fig)


def fig4(plt, shares):
    tasks = [("Settled facts", "Settled facts", ["Settled, 'I'm a conservative'", "Settled, 'I'm a liberal'"], "Settled, false belief"),
             ("Disinfo", "Disinfo", [], "Disinfo, false belief"), ("MedQA", "MedQA", [], "MedQA, false belief"),
             ("TruthfulQA", "TruthfulQA", [], "TruthfulQA, false belief"), ("TriviaQA", "TriviaQA", [], "TriviaQA, false belief")]
    models = [m for m in MODELS if (m[0], "balance_400", "Disinfo") in shares]
    fig, axes = plt.subplots(len(models), len(tasks), figsize=(7.5, 1.65 * len(models) + 0.8), sharey="row")
    rows_csv = []
    for i, (model, lab) in enumerate(models):
        for j, (title, a_lab, b_labs, c_lab) in enumerate(tasks):
            ax = axes[i][j]
            groups = [("A", [a_lab]), ("A+B", b_labs), ("A+C", [c_lab])]
            x = 0
            ticks, tlabels = [], []
            for gname, labs in groups:
                labs = [l for l in labs if (model, "balance_400", l) in shares]
                if not labs:
                    continue
                for l in labs:
                    o = shares[(model, "original", l)]; a = shares[(model, "balance_400", l)]
                    ax.bar(x, a[0], 0.7, color=PALETTE[model], edgecolor="none")
                    ax.errorbar(x, a[0], yerr=[[a[0] - a[1]], [a[2] - a[0]]], color="#333333", lw=0.6, capsize=1.5)
                    ax.plot([x - 0.42, x + 0.42], [o[0], o[0]], color="#c0392b", lw=1.7)
                    rows_csv.append((lab, title, gname, l, round(o[0], 1), round(a[0], 1), round(a[1], 1), round(a[2], 1), a[3]))
                    x += 1
                ticks.append(x - 0.5 - (len(labs) - 1) / 2); tlabels.append(gname); x += 0.6
            ax.set_xticks(ticks); ax.set_xticklabels(tlabels, fontsize=8.2)
            ax.tick_params(axis="y", labelsize=8.2); ax.set_ylim(0, 100)
            if i == 0:
                ax.set_title(title, fontsize=10.5)
            if j == 0:
                ax.set_ylabel(lab + "\npresented as open (%)", fontsize=8.7)
            for s in ("top", "right"):
                ax.spines[s].set_visible(False)
    fig.text(0.5, 0.005, "A, original question; A+B, user cue (identity prefix); A+C, user states the false belief. Bars: neutral model (400 balanced answers, epoch 10); red line: original model.", ha="center", fontsize=8.7)
    fig.subplots_adjust(hspace=0.5, wspace=0.35, bottom=0.07)
    write_csv("fig4.csv", ["model", "task", "component", "condition", "original_share", "neutral_share", "lo95", "hi95", "n"], rows_csv)
    fig.savefig(out_dir() / "fig4.png", dpi=220, bbox_inches="tight"); fig.savefig(out_dir() / "fig4.pdf", bbox_inches="tight"); plt.close(fig)


def fig6(plt):
    nums = json.loads((O.results("summary_data") / "figure_numbers.json").read_text(encoding="utf-8"))
    short = {"llama-3.1-8b": "Llama-3.1-8B", "qwen2.5-7b": "Qwen2.5-7B", "llama-3.2-3b": "Llama-3.2-3B", "qwen2.5-32b": "Qwen2.5-32B",
             "qwen3.8-27b": "Qwen3.8-27B", "gpt-oss-20b": "gpt-oss-20b"}
    series = [("original", "original", None), ("balance_400", "neutral (400 answers)", "//"), ("balance_1927", "neutral (1,927 answers)", "xx")]
    fig, axes = plt.subplots(1, 2, figsize=(7.5, 3.4))
    rows_csv = []
    for ax, (bench, title) in zip(axes, (("mmlu", "MMLU"), ("gsm8k", "GSM8K"))):
        xs, ticks = 0, []
        for model in short:
            got = []
            for cond, cond_label, hatch in series:
                v = nums.get(f"capabilities.{model}.{cond}.{bench}")
                if v:
                    got.append((cond_label, hatch, v))
            if not got:
                continue
            w = 0.8 / len(got)
            for k, (cond_label, hatch, v) in enumerate(got):
                xpos = xs + (k - (len(got) - 1) / 2) * w
                ax.bar(xpos, 100 * v[0], w, color=PALETTE[model], alpha=1.0 if not hatch else 0.85, hatch=hatch, edgecolor=("white" if hatch else "none"), lw=0.4)
                ax.errorbar(xpos, 100 * v[0], yerr=[[100 * (v[0] - v[1])], [100 * (v[2] - v[0])]], color="#333333", lw=0.6, capsize=1.5)
                rows_csv.append((short[model], bench.upper(), cond_label, round(100 * v[0], 1), round(100 * v[1], 1), round(100 * v[2], 1), v[3] if len(v) > 3 else ""))
            ticks.append((xs, short[model])); xs += 1
        ax.set_xticks([t[0] for t in ticks]); ax.set_xticklabels([t[1] for t in ticks], fontsize=9, rotation=20, ha="right")
        ax.set_ylim(0, 100); ax.set_ylabel("Benchmark score (%)", fontsize=10.5); ax.tick_params(axis="y", labelsize=9.8)
        ax.set_title(title, fontsize=12)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
    import matplotlib.patches as mpatches
    fig.legend(handles=[mpatches.Patch(facecolor="#999999", label="original"), mpatches.Patch(facecolor="#999999", hatch="//", edgecolor="white", label="neutral, 400 answers"),
                        mpatches.Patch(facecolor="#666666", hatch="xx", edgecolor="white", label="neutral, 1,927 answers")], fontsize=9, frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.22), ncol=3, columnspacing=1.2)
    write_csv("fig6.csv", ["model", "benchmark", "condition", "accuracy", "lo95", "hi95", "n"], rows_csv)
    fig.tight_layout()
    fig.savefig(out_dir() / "fig6.png", dpi=220, bbox_inches="tight"); fig.savefig(out_dir() / "fig6.pdf", bbox_inches="tight"); plt.close(fig)


def fig5(plt, shares):
    models = [m for m in MODELS if (m[0], "assertive_transform", "Settled facts") in shares and (m[0], "neutrality_prompt", "Settled facts") in shares]
    cells = [c[0] for c in CELLS if c[0] not in ("Consensus figures",)]
    series = [("balance_400", "balance fine-tuning, 400 answers", "#c0392b", "o"), ("balance_1927", "balance fine-tuning, 1,927 answers", "#7b241c", "D"),
              ("neutrality_prompt", "neutrality prompt", "#c0392b", "^"), ("assertive_transform", "assertive fine-tuning (control)", "#2E86C1", "o"),
              ("untransformed", "untransformed fine-tuning (control)", "#2E86C1", "^")]
    fig, axes = plt.subplots(1, len(models), figsize=(7.5, 5.4), sharey=True)
    if len(models) == 1:
        axes = [axes]
    rows_csv = []
    for ax, (model, lab) in zip(axes, models):
        for i, cell in enumerate(cells):
            o = shares.get((model, "original", cell))
            for cond, cond_label, color, marker in series:
                a = shares.get((model, cond, cell))
                if o and a:
                    dx = a[0] - o[0]
                    ax.plot(dx, i, marker=marker, ms=5.9, color=color, ls="none", mfc=color, mec=color)
                    rows_csv.append((lab, cell, cond_label, round(dx, 1), round(o[0], 1), round(a[0], 1), a[3]))
        ax.axvline(0, color="#999999", lw=0.7)
        ax.set_yticks(range(len(cells))); ax.set_yticklabels(cells, fontsize=8.4)
        ax.invert_yaxis(); ax.tick_params(axis="x", labelsize=9)
        ax.set_title(lab, fontsize=10.5)
        ax.grid(axis="y", color="#eeeeee", lw=0.5)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
    fig.text(0.55, 0.135, "Difference from the original model, share presented as open (percentage points)", ha="center", fontsize=9.8)
    handles = [plt.Line2D([], [], marker=m, color=c, ls="none", label=l) for _, l, c, m in series]
    fig.legend(handles=handles, fontsize=8.4, frameon=False, loc="lower center", ncol=3, bbox_to_anchor=(0.55, 0.005))
    fig.subplots_adjust(wspace=0.12, bottom=0.22, left=0.2)
    write_csv("fig5.csv", ["model", "condition", "treatment", "difference_pp", "original_share", "treated_share", "n"], rows_csv)
    fig.savefig(out_dir() / "fig5.png", dpi=220, bbox_inches="tight"); fig.savefig(out_dir() / "fig5.pdf", bbox_inches="tight"); plt.close(fig)


def main():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.family": "Arial", "axes.linewidth": 0.6})
    shares = cache_shares()
    fig1(plt, shares); fig2(plt, shares); fig3(plt, shares); fig4(plt, shares); fig5(plt, shares); fig6(plt)
    print(f"wrote {O.rel(out_dir())} (fig1 to fig6) and {O.rel(src_dir())} (source data), {len(shares)} shares")


if __name__ == "__main__":
    main()
