"""Agreement between the primary judge (GPT-4o) and the second judge (GPT-5.6-terra) on the same answers to the settled
facts: per cent agreement and Cohen's kappa on the hedged class (CORRECT_HEDGED_FACT against the rest), on the four
fact-level classes (committed including adjacent balance, hedged, wrong, refusal) and on all five classes, per
condition and for both conditions together, with the second judge's own hedged share.

Writes summary_data/judge_agreement_<name>.md and .json (keys <name>:<condition or both>:<measure>).
Usage:
  python analysis/judge_agreement.py --name llama-3.1-8b \
      --pair original=full_outputs/llama-3.1-8b/original/judged_main_v1.jsonl,full_outputs/llama-3.1-8b/original/judged_main_v1_second_judge.jsonl \
      --pair balance_400=full_outputs/llama-3.1-8b/balance_400/judged_main_v1.jsonl,full_outputs/llama-3.1-8b/balance_400/judged_main_v1_second_judge.jsonl
"""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import outputs as O  # noqa: E402

FOUR = {"CORRECT_COMMITTED": "committed", "CORRECT_ADJACENT_BALANCE": "committed", "CORRECT_HEDGED_FACT": "hedged",
        "WRONG": "wrong", "REFUSAL": "refusal"}


def kappa(pairs):
    n = len(pairs)
    if n == 0:
        return float("nan"), float("nan")
    po = sum(a == b for a, b in pairs) / n
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / (n * n)
    k = (po - pe) / (1 - pe) if pe < 1 else float("nan")
    return 100 * po, k


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--pair", action="append", required=True, help="condition=primary.jsonl,second.jsonl")
    a = ap.parse_args()
    lines = [f"# Judge agreement, {O.MODEL_LABEL.get(a.name, a.name)}", "",
             "| answers | n | agreement on hedged (%) | kappa, hedged | agreement, four classes (%) | kappa, four classes | agreement, five classes (%) | kappa, five classes |",
             "|---|---|---|---|---|---|---|---|"]
    numbers, both = {}, []
    for spec in a.pair:
        cond, files = spec.split("=", 1)
        f1, f2 = files.split(",")
        r1 = {r["id"]: r for r in O.read_rows(f1) if r.get("class") in FOUR}
        r2 = {r["id"]: r for r in O.read_rows(f2) if r.get("class") in FOUR}
        ids = [i for i in r1 if i in r2 and r1[i].get("task") == "settled"]
        pairs = [(r1[i]["class"], r2[i]["class"]) for i in ids]
        both.extend(pairs)
        h = kappa([(x == "CORRECT_HEDGED_FACT", y == "CORRECT_HEDGED_FACT") for x, y in pairs])
        f4 = kappa([(FOUR[x], FOUR[y]) for x, y in pairs])
        f5 = kappa(pairs)
        lines.append(f"| {O.CONDITION_LABEL.get(cond, cond)} | {len(pairs)} | {h[0]:.1f} | {h[1]:.2f} | {f4[0]:.1f} | {f4[1]:.2f} | {f5[0]:.1f} | {f5[1]:.2f} |")
        numbers.update({f"{a.name}:{cond}:agree_hedged": round(h[0], 1), f"{a.name}:{cond}:kappa_hedged": round(h[1], 2),
                        f"{a.name}:{cond}:agree_four": round(f4[0], 1), f"{a.name}:{cond}:kappa_four": round(f4[1], 2),
                        f"{a.name}:{cond}:agree_five": round(f5[0], 1), f"{a.name}:{cond}:kappa_five": round(f5[1], 2), f"{a.name}:{cond}:n": len(pairs)})
    h = kappa([(x == "CORRECT_HEDGED_FACT", y == "CORRECT_HEDGED_FACT") for x, y in both])
    f4 = kappa([(FOUR[x], FOUR[y]) for x, y in both]); f5 = kappa(both)
    lines.append(f"| both conditions | {len(both)} | {h[0]:.1f} | {h[1]:.2f} | {f4[0]:.1f} | {f4[1]:.2f} | {f5[0]:.1f} | {f5[1]:.2f} |")
    numbers.update({f"{a.name}:both:agree_hedged": round(h[0], 1), f"{a.name}:both:kappa_hedged": round(h[1], 2),
                    f"{a.name}:both:agree_four": round(f4[0], 1), f"{a.name}:both:kappa_four": round(f4[1], 2),
                    f"{a.name}:both:agree_five": round(f5[0], 1), f"{a.name}:both:kappa_five": round(f5[1], 2), f"{a.name}:both:n": len(both)})
    # the second judge's own rates, so the effect can be read on either judge
    lines += ["", "The second judge's share of settled facts presented as open, per condition:"]
    for spec in a.pair:
        cond, files = spec.split("=", 1)
        f2 = files.split(",")[1]
        rows = [r for r in O.read_rows(f2) if r.get("task") == "settled" and r.get("class") in FOUR]
        s = 100 * sum(r["class"] == "CORRECT_HEDGED_FACT" for r in rows) / len(rows)
        lines.append(f"- {O.CONDITION_LABEL.get(cond, cond)}: {s:.1f} per cent (n = {len(rows)})")
        numbers[f"{a.name}:{cond}:second_judge_hedged"] = round(s, 1)
    out = O.results("summary_data")
    (out / f"judge_agreement_{a.name}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (out / f"judge_agreement_{a.name}.json").write_text(json.dumps(numbers, indent=1) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
