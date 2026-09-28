"""The system prompts across the OpenAI models, five-class rubric: one row per model and prompt, with the rates on the
158 settled facts (the three identity conditions combined, 474 answers per cell), on the undisputed facts and on the
publicly disputed facts. Files judged only under the four-class rubric are listed and skipped.

Writes summary_data/system_prompts_across_models_v1.md and .json (keys <model>:<condition>:<subset>:<measure>), or
_v2 with --items v2. Usage: python analysis/prompt_table.py [--items v2]
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import outputs as O  # noqa: E402

MODELS = O.API_MODELS
PROMPTS = [("original", "no system prompt"), ("style_control_prompt", None), ("minimal_prompt", None), ("mild_prompt", None),
           ("mandate_prompt_federal", None), ("mandate_prompt_plain", None), ("npov_prompt", None), ("journalist_prompt", None),
           ("neutrality_prompt", None), ("both_sides_prompt", None)]
PROMPTS = [(k, lab or O.CONDITION_LABEL[k]) for k, lab in PROMPTS]
SUBSETS = {"settled": lambda r: r["task"] == "settled",
           "uncontested": lambda r: r["task"] == "settled" and r.get("public_dispute") == "uncontested",
           "contested": lambda r: r["task"] == "settled" and r.get("public_dispute") == "contested"}
MEASURES = {"committed": lambda r: r.get("class") in ("CORRECT_COMMITTED", "CORRECT_ADJACENT_BALANCE"),
            "hedged": lambda r: r.get("class") == "CORRECT_HEDGED_FACT",
            "adjacent": lambda r: r.get("class") == "CORRECT_ADJACENT_BALANCE",
            "wrong": lambda r: r.get("class") == "WRONG",
            "refusal": lambda r: r.get("class") == "REFUSAL"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--items", default="v1", choices=["v1", "v2"])
    a = ap.parse_args()
    ps = f"main_{a.items}"
    out_md = [f"# The system prompts across models (five-class rubric, settled facts, version {a.items[1]})\n",
              "Rates on the settled facts, per cent of judged answers; the three identity conditions combined (n = 474 per cell, 158 questions x 3 prefixes).\n",
              "| model | prompt | n | committed | hedged (fact presented as open) | adjacent balance | wrong | refusal | hedged, undisputed | hedged, publicly disputed |",
              "|---|---|---|---|---|---|---|---|---|---|"]
    numbers, skipped = {}, []
    for mkey, mlabel in MODELS:
        for ckey, clabel in PROMPTS:
            rows = O.load_judged(mkey, ckey, ps)
            if rows is None:
                continue
            if not rows or rows[0].get("rubric") != "v2":
                skipped.append(f"{mkey} {ckey} (four-class rubric only)")
                continue
            cells = {}
            for skey, sfun in SUBSETS.items():
                sub = [r for r in rows if sfun(r) and r.get("class")]
                n = len(sub)
                for measure, mfun in MEASURES.items():
                    v = 100.0 * sum(mfun(r) for r in sub) / n if n else float("nan")
                    cells[(skey, measure)] = v
                    numbers[f"{mkey}:{ckey}:{skey}:{measure}"] = round(v, 1)
                numbers[f"{mkey}:{ckey}:{skey}:n"] = n
            n = sum(1 for r in rows if SUBSETS["settled"](r) and r.get("class"))
            out_md.append(f"| {mlabel} | {clabel} | {n} | {cells[('settled', 'committed')]:.1f} | {cells[('settled', 'hedged')]:.1f} | "
                          f"{cells[('settled', 'adjacent')]:.1f} | {cells[('settled', 'wrong')]:.1f} | {cells[('settled', 'refusal')]:.1f} | "
                          f"{cells[('uncontested', 'hedged')]:.1f} | {cells[('contested', 'hedged')]:.1f} |")
    if skipped:
        out_md.append("\nNot included (scored only under the four-class rubric): " + ", ".join(skipped))
    out = O.results("summary_data")
    (out / f"system_prompts_across_models_{a.items}.md").write_text("\n".join(out_md) + "\n", encoding="utf-8")
    (out / f"system_prompts_across_models_{a.items}.json").write_text(json.dumps(numbers, indent=1) + "\n", encoding="utf-8")
    print("\n".join(out_md))


if __name__ == "__main__":
    main()
