"""AdvBench refusal rates, original against each treated condition: the judge's refusal share (refused, against
complied or partial) with its Wilson 95 per cent interval, the regular-expression refusal rate (the string list of
the AdvBench evaluation, typographic apostrophes straightened) and the judged refusals longer than eighty words.

Usage:
  python analysis/advbench.py --out summary_data/comparisons/gpt-4o/advbench/neutrality_prompt.md --model gpt-4o \
      --original full_outputs/gpt-4o/original/judged_advbench.jsonl \
      --condition neutrality_prompt=full_outputs/gpt-4o/neutrality_prompt/judged_advbench.jsonl
"""
import argparse
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import outputs as O  # noqa: E402
from scoring.judge import regex_refusal  # noqa: E402


def wilson(k, n, z=1.96):
    if n == 0:
        return (0, 0, 0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (p, c - h, c + h)


def rates(rows):
    rows = [r for r in rows if r.get("class") in ("REFUSED", "COMPLIED", "PARTIAL")]
    n = len(rows)
    kj = sum(1 for r in rows if r["class"] == "REFUSED")
    kr = sum(1 for r in rows if regex_refusal(r["response"]))
    kl = sum(1 for r in rows if r["class"] == "REFUSED" and len(r["response"].split()) > 80)
    pj, lo, hi = wilson(kj, n)
    return n, f"{100 * pj:.1f} [{100 * lo:.1f}, {100 * hi:.1f}]", f"{100 * kr / n:.1f}" if n else "-", kl


HEADER = ["| model | condition | n | refused (judge), original / treated | refused (regular expression), original / treated | "
          "refusals over 80 words, original / treated |", "|---|---|---|---|---|---|"]


def advbench_table(title, model, original_path, conditions, out_path):
    label = O.MODEL_LABEL.get(model, model)
    no, jo, ro, lo_ = rates(O.read_rows(original_path))
    L = [f"# {title}", "", f"original: {O.rel(original_path)}", ""] + HEADER
    for k, p in conditions:
        na, ja, ra, la_ = rates(O.read_rows(p))
        L.append(f"| {label} | {O.CONDITION_LABEL.get(k, k)} | {no}/{na} | {jo} / {ja} | {ro} / {ra} | {lo_} / {la_} |")
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join(L) + "\n"
    out_path.write_text(text, encoding="utf-8")
    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--original", required=True)
    ap.add_argument("--condition", action="append", default=[], help="name=path")
    a = ap.parse_args()
    conds = [tuple(s.split("=", 1)) for s in a.condition]
    print(advbench_table(Path(a.out).stem, a.model, a.original, conds, a.out))


if __name__ == "__main__":
    main()
