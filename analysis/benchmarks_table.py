"""MMLU and GSM8K accuracy per model and condition, with Wilson intervals, from the capabilities.* numbers that
analysis/figure_numbers.py writes into summary_data/figure_numbers.json. Writes summary_data/capability_benchmarks.md.
Usage: python analysis/benchmarks_table.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import outputs as O  # noqa: E402


def main():
    nums = json.loads((O.results("summary_data") / "figure_numbers.json").read_text(encoding="utf-8"))
    rows = {}
    for k, v in nums.items():
        if not k.startswith("capabilities."):
            continue
        _, model, rest = k.split(".", 2)
        cond, bench = rest.rsplit(".", 1)
        rows.setdefault((model, cond), {})[bench] = v
    order = [m for m, _ in O.FINE_TUNED]
    lines = ["# Capability benchmarks per model and condition (accuracy, per cent, Wilson 95 per cent interval)", "",
             "| model | condition | MMLU (1,000 items) | GSM8K (500 items) |", "|---|---|---|---|"]

    def cell(x):
        return "" if x is None else f"{100 * x[0]:.1f} [{100 * x[1]:.1f}, {100 * x[2]:.1f}]"
    for (model, cond), b in sorted(rows.items(), key=lambda kv: (order.index(kv[0][0]) if kv[0][0] in order else 99, kv[0][1] != "original", kv[0][1])):
        lines.append(f"| {O.MODEL_LABEL.get(model, model)} | {O.CONDITION_LABEL.get(cond, cond)} | {cell(b.get('mmlu'))} | {cell(b.get('gsm8k'))} |")
    p = O.results("summary_data") / "capability_benchmarks.md"
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {O.rel(p)} with {len(rows)} rows")


if __name__ == "__main__":
    main()
