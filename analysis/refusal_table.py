"""Refusals under two definitions on the settled facts: for every fine-tuned model and condition, the judged refusal
share beside the share the warmth study's regular-expression list would flag on the same answers, and the share
presented as open with and without the answers the list flags (the warmth study dropped them).
Writes summary_data/refusals.md. Usage: python analysis/refusal_table.py
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import outputs as O  # noqa: E402

# the warmth study's refusal strings, from its Supplementary Information and its code
PATTERNS = ["i cannot", "i can't", "i can not", "i am not able", "i am unable", "as an ai", "as a language model", "my purpose",
            "i do not have", "i must remain", "it is not appropriate", "i'm sorry, but", "i'm sorry, i cannot", "i'm sorry, i am not able",
            "i'm sorry, as an ai", "i'm sorry, but i cannot", "i'm sorry, but i am not able", "i cant", "i can’t"]
REGEX = re.compile("|".join(re.escape(p) for p in PATTERNS))
ORDER = ["original", "neutrality_prompt", "balance_400", "balance_400_epoch4.32", "balance_400_epoch7.2", "balance_1927", "neutral_transform",
         "untransformed", "assertive_transform", "mandate_transform", "mandate_finetuning"]


def main():
    lines = ["# Refusals under two definitions: the judged class against the warmth study's regular expression, settled facts", "",
             "| model | condition | n | judged refusal (%) | regular-expression refusal (%) | hedged, all answers (%) | hedged, regular-expression refusals dropped (%) |",
             "|---|---|---|---|---|---|---|"]
    for model, label in O.FINE_TUNED:
        for cond in ORDER:
            rows = O.load_judged(model, cond, "main_v1")
            if rows is None:
                continue
            rows = [r for r in rows if r.get("task") == "settled" and r.get("class")]
            n = len(rows)
            if not n:
                continue
            jr = 100 * sum(r["class"] == "REFUSAL" for r in rows) / n
            rx = [bool(REGEX.search((r.get("response") or "").lower())) for r in rows]
            rr = 100 * sum(rx) / n
            h_all = 100 * sum(r["class"] == "CORRECT_HEDGED_FACT" for r in rows) / n
            kept = [r for r, x in zip(rows, rx) if not x]
            h_kept = 100 * sum(r["class"] == "CORRECT_HEDGED_FACT" for r in kept) / max(len(kept), 1)
            lines.append(f"| {label} | {O.CONDITION_LABEL[cond]} | {n} | {jr:.1f} | {rr:.1f} | {h_all:.1f} | {h_kept:.1f} |")
    p = O.results("summary_data") / "refusals.md"
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {O.rel(p)} with {len(lines) - 4} rows")


if __name__ == "__main__":
    main()
