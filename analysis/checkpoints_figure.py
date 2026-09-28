"""Extended Data Fig. 3: the share of settled facts presented as open, and the share of wrong answers, at every judged
checkpoint of balance fine-tuning on 400 answers (Llama-3.1-8B), beside the manipulation measure (mean balancing moves
per answer on the 60 contested questions) at the same checkpoints, with the checkpoint the pre-written rule selected.

Also writes into summary_data/figure_numbers.json the shares at each checkpoint (checkpoints.<model>.<epoch>.hedged
and .wrong) and the manipulation measure of the model as released, at the end of training and at the selected
checkpoint (manipulation.<model>.*). Writes figures/extended_data_fig3.pdf and source_data/extended_data_fig3.csv.
Usage: python analysis/checkpoints_figure.py [--model llama-3.1-8b]
"""
import argparse
import csv
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
import outputs as O  # noqa: E402
from figure_numbers import rate, is_hedged, is_wrong  # noqa: E402

CONDITION = "balance_400"


def settled(model, condition):
    rows = O.load_judged(model, condition, "main_v1")
    return [r for r in rows if r["task"] == "settled"] if rows is not None else None


def measure(rows, model, prompt_set, field):
    """(original value, [(step, value)]) of the manipulation measure for balance fine-tuning on 400 answers."""
    orig = [float(r[field]) for r in rows if r["model"] == model and r["condition"] == "original" and r["prompt_set"] == prompt_set and r["step"] == ""]
    pts = sorted((int(r["step"]), float(r[field])) for r in rows if r["model"] == model and r["condition"] == CONDITION
                 and r["prompt_set"] == prompt_set and r["step"] != "")
    return (orig[0] if orig else None), pts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="llama-3.1-8b")
    a = ap.parse_args()
    train = O.training_records()[(a.model, CONDITION)]
    spe, total = int(train["steps_per_epoch"]), int(train["total_steps"])
    rule = O.checkpoint_selection().get(a.model, {})
    selected = (rule.get("selected") or {})
    points = []  # (epoch, step, hedged rate, wrong rate, label)
    o = settled(a.model, "original")
    points.append((0.0, 0, rate(o, is_hedged), rate(o, is_wrong), "original"))
    for cond in O.conditions_of(a.model):
        if not cond.startswith(CONDITION + "_epoch"):
            continue
        rows = settled(a.model, cond)
        if rows is None:
            continue
        e = float(cond[len(CONDITION + "_epoch"):])
        if selected.get("epoch") == e:
            step, label = selected["step"], "rule-selected"
        else:
            step, label = round(e * spe), cond
        points.append((step / spe, step, rate(rows, is_hedged), rate(rows, is_wrong), label))
    rows = settled(a.model, CONDITION)
    if rows is not None:
        points.append((total / spe, total, rate(rows, is_hedged), rate(rows, is_wrong), "end of training"))
    points.sort()
    mm = O.manipulation_measure()
    o_moves, moves = measure(mm, a.model, "contested_questions", "mean_moves")
    moves_at = dict(moves)
    moves_at[0] = o_moves

    plt.rcParams.update({"font.size": 10, "font.family": "Arial", "axes.spines.top": False, "axes.spines.right": False})
    fig, ax = plt.subplots(1, 1, figsize=(7.5, 4.2))
    xs = [p[0] for p in points]; ys = [100 * p[2][0] for p in points]
    lo = [100 * (p[2][0] - p[2][1]) for p in points]; hi = [100 * (p[2][2] - p[2][0]) for p in points]
    ax.errorbar(xs, ys, yerr=[lo, hi], fmt="-o", ms=3.9, lw=1, capsize=2, color="#c0392b", label="settled facts presented as open (%)")
    ax.plot(xs, [100 * p[3][0] for p in points], "-s", ms=3.9, lw=1, color="#7f7f7f", label="wrong answers (%)")
    ax.set_xlabel("training epoch"); ax.set_ylabel("per cent of answers"); ax.set_ylim(0, 100)
    bx = ax.twinx(); bx.spines["top"].set_visible(False)
    ts = sorted(s for s in moves_at if moves_at[s] is not None)
    bx.plot([s / spe for s in ts], [moves_at[s] for s in ts], "-", lw=0.8, color="#e74c3c", alpha=0.8, label="balancing moves per answer, contested questions")
    bx.set_ylabel("balancing moves per answer", color="#e74c3c")
    h2, l2 = bx.get_legend_handles_labels()
    chosen = selected.get("epoch")
    if chosen:
        ax.axvline(chosen, color="#555555", lw=0.8, ls="--")
        ax.text(chosen + 0.15, 97, f"checkpoint the pre-written rule selected (epoch {chosen:.1f})", fontsize=9.5, color="#555555", va="top")
    h1, l1 = ax.get_legend_handles_labels()
    fig.legend(h1 + h2, l1 + l2, fontsize=10, frameon=False, ncol=2, loc="lower center", bbox_to_anchor=(0.5, 0.0), handlelength=1.6, columnspacing=1.6)
    fig.tight_layout(rect=(0, 0.13, 1, 1))
    out = O.results("figures")
    fig.savefig(out / "extended_data_fig3.png", dpi=200); fig.savefig(out / "extended_data_fig3.pdf")
    plt.close(fig)
    with open(O.results("source_data") / "extended_data_fig3.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["model", "checkpoint", "step", "epoch", "presented_as_open", "lo95", "hi95", "wrong", "n", "balancing_moves_per_answer"])
        for p in points:
            w.writerow([a.model, p[4], p[1], round(p[0], 2), round(100 * p[2][0], 1), round(100 * p[2][1], 1), round(100 * p[2][2], 1),
                        round(100 * p[3][0], 1), p[2][3], moves_at.get(p[1], "")])
    # the numbers
    nj = O.results("summary_data") / "figure_numbers.json"
    allnums = json.loads(nj.read_text(encoding="utf-8")) if nj.exists() else {}
    for p in points:
        allnums[f"checkpoints.{a.model}.{p[0]:.2f}.hedged"] = round(100 * p[2][0], 1)
        allnums[f"checkpoints.{a.model}.{p[0]:.2f}.wrong"] = round(100 * p[3][0], 1)
    o_val, val = measure(mm, a.model, "validation_prompts", "share_balanced")
    if val:
        allnums[f"manipulation.{a.model}.validation_share.original"] = round(100 * (o_val or 0), 1)
        allnums[f"manipulation.{a.model}.validation_share.final"] = round(100 * val[-1][1], 1)
    if moves:
        allnums[f"manipulation.{a.model}.contested_mean_moves.original"] = round(o_moves or 0, 2)
        allnums[f"manipulation.{a.model}.contested_mean_moves.final"] = round(moves[-1][1], 2)
    if selected:
        allnums[f"manipulation.{a.model}.selected_value"] = round(selected["value"], 2)
        allnums[f"manipulation.{a.model}.measure"] = rule.get("measure")
        allnums[f"manipulation.{a.model}.selected_epoch"] = selected["epoch"]
    nj.write_text(json.dumps(allnums, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print("checkpoints:", [(round(p[0], 2), round(100 * p[2][0], 1), p[4]) for p in points])
    print("wrote", O.rel(out / "extended_data_fig3.pdf"))


if __name__ == "__main__":
    main()
