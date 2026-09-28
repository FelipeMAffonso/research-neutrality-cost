"""Apply the checkpoint-selection rule, written before training, to balance fine-tuning on 400 answers.

The manipulation measure is the balancing share on the 300 validation prompts if its highest value exceeds the
original model's by 10 points; otherwise the balancing share on the 60 contested questions if the original's share
is under 0.9; otherwise the mean number of balancing moves per answer on those questions. The selected checkpoint
is the epoch-2 checkpoint if its measure is at least 80 per cent of the value at the last saved checkpoint, and
otherwise the first checkpoint that reaches 80 per cent.

Reads summary_data/manipulation_measure.csv and finetuning/training_records.csv. Writes
summary_data/checkpoint_selection.json, one entry per model.
Usage: python analysis/checkpoint_rule.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import outputs as O  # noqa: E402

CONDITION = "balance_400"


def series(rows, model, prompt_set, field):
    orig = [float(r[field]) for r in rows if r["model"] == model and r["condition"] == "original"
            and r["prompt_set"] == prompt_set and r["step"] == ""]
    pts = sorted((int(r["step"]), float(r[field])) for r in rows if r["model"] == model and r["condition"] == CONDITION
                 and r["prompt_set"] == prompt_set and r["step"] != "")
    return (orig[0] if orig else None), pts


def select(model, rows, train):
    spe = int(train[(model, CONDITION)]["steps_per_epoch"])
    o_val, val = series(rows, model, "validation_prompts", "share_balanced")
    o_cs, cs = series(rows, model, "contested_questions", "share_balanced")
    o_cm, cm = series(rows, model, "contested_questions", "mean_moves")
    if val and max(v for _, v in val) - o_val >= 0.10:
        measure, o, pts = "validation_share", o_val, val
    elif cs and o_cs < 0.9:
        measure, o, pts = "contested_share", o_cs, cs
    else:
        measure, o, pts = "contested_mean_moves", o_cm, cm
    last_step, last_val = pts[-1]
    thresh = 0.8 * last_val
    epoch2 = min(pts, key=lambda p: abs(p[0] - 2 * spe))
    chosen = epoch2 if epoch2[1] >= thresh else next(p for p in pts if p[1] >= thresh)
    return {"measure": measure, "original_value": o,
            "checkpoints": [{"step": s, "epoch": round(s / spe, 2), "value": v} for s, v in pts],
            "threshold_80_percent_of_last": round(thresh, 4), "epoch2_checkpoint": {"step": epoch2[0], "value": epoch2[1]},
            "selected": {"step": chosen[0], "epoch": round(chosen[0] / spe, 2), "value": chosen[1]},
            "last_step": int(train[(model, CONDITION)]["total_steps"])}


def main():
    rows = O.manipulation_measure()
    train = O.training_records()
    out = {}
    for model in sorted({r["model"] for r in rows if r["condition"] == CONDITION and r["step"] != ""}):
        if (model, CONDITION) in train:
            out[model] = select(model, rows, train)
    p = O.results("summary_data") / "checkpoint_selection.json"
    p.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    for m, d in out.items():
        print(f"{m}: {d['measure']}, selected step {d['selected']['step']} (epoch {d['selected']['epoch']})")
    print("wrote", O.rel(p))


if __name__ == "__main__":
    main()
