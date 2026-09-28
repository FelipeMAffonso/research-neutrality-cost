"""The fine-tuning settings per model and condition (bf16 LoRA), one row per training run, from
finetuning/training_records.csv. Writes summary_data/finetuning_settings.md. Usage: python analysis/training_table.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import outputs as O  # noqa: E402


def main():
    fine_tuned = dict(O.FINE_TUNED)
    lines = ["# The fine-tuning settings (one H100 80 GB GPU, bf16 LoRA r 8, alpha 16, dropout 0.1, learning rate 1e-5, 1,024 tokens, linear schedule, 3 per cent warmup)", "",
             "| model | condition | conversations | epochs | batch x accumulation | steps per epoch | steps | minutes | peak GPU memory (GB) | loss first | loss last | note |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    n = 0
    for (model, cond), r in O.training_records().items():
        if model not in fine_tuned or cond.endswith("_retrained"):
            continue
        first, last = float(r["train_loss_first"]), float(r["train_loss_last"])
        diverged = last == 0.0 or last != last
        lines.append(f"| {fine_tuned[model]} | {O.CONDITION_LABEL.get(cond, cond)} | {r['conversations']} | {r['epochs']} | {r['batch_size']} x {r['gradient_accumulation']} | "
                     f"{r['steps_per_epoch']} | {r['total_steps']} | {round(int(r['seconds']) / 60, 1)} | {r['peak_gpu_memory_gb']} | {round(first, 2)} | {round(last, 2)} | "
                     f"{'diverged, trained again at batch 1 x 16' if diverged else ''} |")
        n += 1
    p = O.results("summary_data") / "finetuning_settings.md"
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {O.rel(p)} with {n} rows")


if __name__ == "__main__":
    main()
