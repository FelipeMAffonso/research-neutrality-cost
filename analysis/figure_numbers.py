"""The rates behind the figures and tables, read from the judged files, and Extended Data Fig. 1.

For GPT-4o under the neutrality prompt and for every fine-tuned model and condition, writes into
summary_data/figure_numbers.json (each value a list: share, lower and upper Wilson 95 per cent bounds, n):
  settled.<model>.<condition>.<hedged|wrong>            settled facts, all three identity conditions
  where.<model>.<condition>.<subset>.<hedged|wrong>     publicly disputed and undisputed facts and the four tasks
  identity.<model>.<condition>.<prefix>.hedged          settled facts by identity prefix and after the false belief
  capabilities.<model>.<condition>.<mmlu|gsm8k>         accuracy on MMLU and GSM8K
Extended Data Fig. 1 (figures/extended_data_fig1.pdf, source_data/extended_data_fig1.csv) draws the "where" rates
for GPT-4o. Usage: python analysis/figure_numbers.py
"""
import csv
import json
import math
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import outputs as O  # noqa: E402

HEDGED = ("CORRECT_HEDGED", "CORRECT_HEDGED_FACT")
# the fine-tuned conditions in the order the tables list them
CONDITIONS = ["neutrality_prompt", "neutral_transform", "balance_400_epoch4.32", "balance_400_epoch7.2", "balance_400", "balance_1927",
              "mandate_transform", "mandate_finetuning", "assertive_transform", "untransformed"]
COLORS = {"original": "#7f7f7f", "neutrality_prompt": "#c0392b"}
WHERE_GROUPS = ["settled, contested", "settled, uncontested", "Disinfo", "MedQA", "TruthfulQA", "TriviaQA"]
IDENTITY_GROUPS = ["no prefix", "\"I'm a conservative\"", "\"I'm a liberal\"", "user states the false belief"]


def wilson(k, n, z=1.96):
    if n == 0:
        return (0, 0, 0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (p, c - h, c + h)


def rate(rows, pred):
    n = len(rows)
    k = sum(1 for r in rows if pred(r))
    return wilson(k, n) + (n,)


def is_hedged(r):
    return r.get("class") in HEDGED


def is_wrong(r):
    return r.get("class") == "WRONG"


def four_tasks_file(model, condition, full_first):
    """The four question-answering tasks: the full set where it was judged, else the 1,449-prompt sample."""
    order = ("four_tasks_full", "four_tasks_sample") if full_first else ("four_tasks_sample",)
    for ps in order:
        if O.judged_path(model, condition, ps).exists():
            return ps
    return None


def models():
    """(model, label, conditions, four-task prompt set) for GPT-4o under the neutrality prompt and each fine-tuned model."""
    out = [("gpt-4o", "GPT-4o", ["neutrality_prompt"], "four_tasks_sample")]
    for m, lab in O.FINE_TUNED:
        if not O.judged_path(m, "original", "main_v1").exists():
            continue
        out.append((m, lab, [c for c in CONDITIONS if O.judged_path(m, c, "main_v1").exists()], four_tasks_file(m, "original", True)))
    return out


def score(path, task):
    rows = O.read_rows(path)
    ok = 0
    for r in rows:
        resp = r["response"]
        if task == "mmlu":
            mm = re.search(r"\b([ABCD])\b", resp.strip().upper())
            ok += bool(mm and mm.group(1) == r["reference"])
        else:
            mm = re.findall(r"Answer:\s*\$?(-?[\d,]*\.?\d+)", resp)
            pred = (mm[-1] if mm else (re.findall(r"-?[\d,]*\.?\d+", resp) or [""])[-1]).replace(",", "")
            try:
                ok += abs(float(pred) - float(r["reference"])) < 1e-6
            except ValueError:
                pass
    return wilson(ok, len(rows)) + (len(rows),)


def where_slices(items, tasks):
    return [[r for r in items if r["task"] == "settled" and r.get("public_dispute") == "contested"],
            [r for r in items if r["task"] == "settled" and r.get("public_dispute") == "uncontested"],
            [r for r in tasks if r["task"] == "disinfo"], [r for r in tasks if r["task"] == "medqa"],
            [r for r in tasks if r["task"] == "truthfulqa"], [r for r in tasks if r["task"] == "trivia"]]


def identity_slices(items, ext):
    return [[r for r in items if r["task"] == "settled" and r.get("variant") == v] for v in ("none", "conservative", "liberal")] + \
           [[r for r in ext if r["task"] == "settled" and r.get("variant") == "belief_wrong"]]


def ed1(model, label, series):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    plt.rcParams.update({"font.family": "Arial"})
    fig, axes = plt.subplots(1, 2, figsize=(7.5, 3.6))
    rows_csv = []
    for panel, (key, ttl) in enumerate((("hedged", "a  Presented as open (%)"), ("wrong", "b  Wrong (%)"))):
        ax = axes[panel]
        x = np.arange(len(WHERE_GROUPS))
        w = 0.8 / len(series)
        for i, (cond, vals) in enumerate(series.items()):
            vs = vals[key]
            ps = [100 * v[0] for v in vs]
            err = [[max(0.0, 100 * (v[0] - v[1])) for v in vs], [max(0.0, 100 * (v[2] - v[0])) for v in vs]]
            ax.bar(x + (i - (len(series) - 1) / 2) * w, ps, w, yerr=err, capsize=2, label=O.CONDITION_LABEL.get(cond, cond),
                   color=COLORS.get(cond, "#999999"), edgecolor="none")
            for g, v in zip(WHERE_GROUPS, vs):
                rows_csv.append((label, O.CONDITION_LABEL.get(cond, cond), g, key, round(100 * v[0], 1), round(100 * v[1], 1), round(100 * v[2], 1), v[3]))
        ax.set_xticks(x)
        ax.tick_params(axis="y", labelsize=12)
        ax.set_ylabel("per cent of answers", fontsize=12)
        ax.set_title(ttl, fontsize=12, loc="left")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.set_ylim(0, 100)
        ax.set_xticklabels(WHERE_GROUPS, rotation=40, ha="right", rotation_mode="anchor", fontsize=10.5)
    handles, labels_ = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels_, fontsize=10.5, frameon=False, ncol=len(handles), loc="lower center", bbox_to_anchor=(0.5, 0.0), handlelength=1.4, columnspacing=1.6)
    fig.tight_layout(rect=(0, 0.09, 1, 1))
    out = O.results("figures")
    fig.savefig(out / "extended_data_fig1.png", dpi=200)
    fig.savefig(out / "extended_data_fig1.pdf")
    plt.close(fig)
    with open(O.results("source_data") / "extended_data_fig1.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["model", "condition", "subset", "outcome", "share", "lo95", "hi95", "n"])
        w.writerows(rows_csv)


def main():
    numbers = {}
    first_where = None
    for model, label, conds, tasks_ps in models():
        items = {c: O.load_judged(model, c, "main_v1") for c in ["original"] + conds}
        # settled facts, hedged and wrong
        for c, rows in items.items():
            s = [r for r in rows if r["task"] == "settled"]
            numbers[f"settled.{model}.{c}.hedged"] = rate(s, is_hedged)
            numbers[f"settled.{model}.{c}.wrong"] = rate(s, is_wrong)
        # where the cost falls: publicly disputed or not, and the four tasks (same kind of four-task file for every condition)
        if tasks_ps:
            series = {}
            for c in ["original"] + conds:
                t = O.load_judged(model, c, tasks_ps) if O.judged_path(model, c, tasks_ps).exists() else None
                if t is None:
                    continue
                sl = where_slices(items[c], t)
                series[c] = {"hedged": [rate(s, is_hedged) for s in sl], "wrong": [rate(s, is_wrong) for s in sl]}
                for key in ("hedged", "wrong"):
                    for g, v in zip(WHERE_GROUPS, series[c][key]):
                        numbers[f"where.{model}.{c}.{g}.{key}"] = v
            if first_where is None:
                first_where = (model, label, series)
        # who is asking: the identity prefixes and the stated false belief
        ext_o = O.load_judged(model, "original", "extended_v1")
        if ext_o is not None:
            for c in ["original"] + conds:
                e = ext_o if c == "original" else O.load_judged(model, c, "extended_v1")
                if e is None:
                    continue
                for g, s in zip(IDENTITY_GROUPS, identity_slices(items[c], e)):
                    numbers[f"identity.{model}.{c}.{g}.hedged"] = rate(s, is_hedged)
        # capabilities: MMLU and GSM8K where the original and at least one condition were generated
        have = [c for c in ["original"] + conds if O.answers_path(model, c, "mmlu").exists() and O.answers_path(model, c, "gsm8k").exists()]
        if len(have) >= 2:
            for c in have:
                for task in ("mmlu", "gsm8k"):
                    numbers[f"capabilities.{model}.{c}.{task}"] = score(O.answers_path(model, c, task), task)
    if first_where:
        ed1(*first_where)
    p = O.results("summary_data") / "figure_numbers.json"
    merged = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
    merged = {k: v for k, v in merged.items() if not k.startswith(("settled.", "where.", "identity.", "capabilities."))}
    merged.update({k: [round(x, 4) if isinstance(x, float) else x for x in v] for k, v in numbers.items()})
    p.write_text(json.dumps(merged, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print("wrote", O.rel(p), "with", len(numbers), "rates, and Extended Data Fig. 1")


if __name__ == "__main__":
    main()
