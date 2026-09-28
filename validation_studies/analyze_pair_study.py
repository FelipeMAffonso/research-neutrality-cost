"""The pair study, the validation of the manipulation, reported as the warmth study reported its own (pairs of answers,
"which response is warmer?"): the share of ratings in which the neutral model's answer was chosen as the more
even-handed, with an exact binomial test against one half, a 95 per cent Clopper-Pearson interval and Cohen's h; the
share of pairs whose majority chose the neutral answer; the share of raters who chose it more often than not; the same
by model and by item set; and the agreement between the raters' majority and the judge on the settled pairs where the
judge rated the two answers differently. Raters who failed the attention pair are excluded.

Reads pair_study/responses.csv, pair_study/pair_key.csv and, for the judge's labels, judged_main_v1.jsonl of the two
models the pairs were drawn from (analysis/outputs.py). Writes summary_data/validation_pair_study.md and .json.
Usage: python validation_studies/analyze_pair_study.py
"""
import csv
import json
import math
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "analysis"))
import outputs as O  # noqa: E402
import responses  # noqa: E402

ATTENTION_CORRECT = 2  # Response B is the two-sided one on the attention pair
JUDGED = {"gpt-4o": ("original", "neutrality_prompt"), "llama-3.1-8b-4bit": ("original", "balance_400")}  # the runs the pairs were drawn from
HEDGED = {"CORRECT_HEDGED_FACT"}


def binom_two_sided(k, n):
    """Exact two-sided binomial test against one half (the sum of the probabilities no larger than the observed)."""
    if n == 0:
        return float("nan")
    pk = math.comb(n, k) / 2 ** n
    return min(1.0, sum(math.comb(n, i) / 2 ** n for i in range(n + 1) if math.comb(n, i) / 2 ** n <= pk * (1 + 1e-9)))


def clopper_pearson(k, n, alpha=0.05):
    try:
        from scipy.stats import beta
        lo = beta.ppf(alpha / 2, k, n - k + 1) if k > 0 else 0.0
        hi = beta.ppf(1 - alpha / 2, k + 1, n - k) if k < n else 1.0
        return lo, hi
    except ImportError:  # Wilson as the fallback
        p, z = k / n, 1.959964
        d = 1 + z * z / n
        c = (p + z * z / (2 * n)) / d
        h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
        return c - h, c + h


def cohen_h(p, q=0.5):
    return 2 * math.asin(math.sqrt(p)) - 2 * math.asin(math.sqrt(q))


def judge_preference(key):
    """For each settled pair, which answer the judge preferred: 'treated' if it called the neutral answer hedged and the
    original not, 'original' for the reverse, None when it rated both alike."""
    pref, cls = {}, {}
    for model, (orig, treated) in JUDGED.items():
        for side, cond in (("original", orig), ("treated", treated)):
            for d in O.load_judged(model, cond, "main_v1"):
                cls[(model, side, d["id"])] = d.get("class")
    for pid, r in key.items():
        if r["task"] != "settled":
            continue
        o, t = cls.get((r["model"], "original", r["prompt_id"])), cls.get((r["model"], "treated", r["prompt_id"]))
        if o is None or t is None:
            continue
        oh, th = o in HEDGED, t in HEDGED
        pref[pid] = "treated" if th and not oh else "original" if oh and not th else None
    return pref


def block(label, chosen, n):
    if n == 0:
        return f"| {label} | 0 | - | - | - | - |"
    p = chosen / n
    lo, hi = clopper_pearson(chosen, n)
    pv = binom_two_sided(chosen, n)
    return f"| {label} | {n} | {100 * p:.1f} | {100 * lo:.1f} to {100 * hi:.1f} | {'< 0.001' if pv < 0.001 else f'{pv:.3f}'} | {cohen_h(p):.2f} |"


def main():
    key = {r["pair_id"]: r for r in csv.DictReader(open(HERE / "pair_study" / "pair_key.csv", encoding="utf-8"))}
    rows = [x for x in responses.read(HERE / "pair_study" / "responses.csv") if x["values"].get("finished") in (1, True, "1")]
    passed = [x for x in rows if str(x["values"].get("attention_check", "")) == str(ATTENTION_CORRECT)]
    failed = len(rows) - len(passed)
    ratings = []  # (rater, pair, chose the treated answer)
    for x in passed:
        rid = x["rater"]
        for tag, val in x["values"].items():
            if tag.startswith("pair_") and tag[5:] in key and val not in (None, ""):
                side = "left" if int(val) == 1 else "right"
                ratings.append((rid, tag[5:], side == key[tag[5:]]["treated_side"]))
    n = len(ratings)
    chosen = sum(c for _, _, c in ratings)
    by_pair, by_rater = defaultdict(list), defaultdict(list)
    for rid, pid, c in ratings:
        by_pair[pid].append(c); by_rater[rid].append(c)
    maj = {pid: (sum(v) * 2 > len(v)) for pid, v in by_pair.items() if len(v) >= 2 and sum(v) * 2 != len(v)}
    pairs_majority_treated = sum(maj.values())
    raters_majority_treated = sum(1 for v in by_rater.values() if sum(v) * 2 > len(v))
    pref = judge_preference(key)
    decided = {pid: p for pid, p in pref.items() if p and pid in maj}
    agree = sum(1 for pid, p in decided.items() if (p == "treated") == maj[pid])
    judge_treated = sum(1 for p in pref.values() if p == "treated")
    judge_original = sum(1 for p in pref.values() if p == "original")
    out = {"raters_finished": len(rows), "raters_failed_attention": failed, "raters_kept": len(passed), "ratings": n,
           "chose_treated": chosen, "share_treated": 100 * chosen / n if n else None,
           "ci": [100 * v for v in clopper_pearson(chosen, n)] if n else None, "p_binomial": binom_two_sided(chosen, n) if n else None,
           "ci_lo": 100 * clopper_pearson(chosen, n)[0] if n else None, "ci_hi": 100 * clopper_pearson(chosen, n)[1] if n else None,
           "cohen_h": cohen_h(chosen / n) if n else None,
           "pairs_rated": len(by_pair), "pairs_with_majority": len(maj), "pairs_majority_treated": pairs_majority_treated,
           "raters_majority_treated": raters_majority_treated,
           "judge_settled_pairs_decided": len(pref) - sum(1 for p in pref.values() if p is None), "judge_preferred_treated": judge_treated,
           "judge_preferred_original": judge_original, "judge_rater_pairs_compared": len(decided), "judge_rater_agree": agree,
           "judge_rater_agreement": 100 * agree / len(decided) if decided else None}
    for col, vals in (("model", ("gpt-4o", "llama-3.1-8b-4bit")), ("task", ("settled", "contested"))):
        for v in vals:
            sub = [c for _, pid, c in ratings if key[pid][col] == v]
            out[f"{col}:{v}:ratings"] = len(sub); out[f"{col}:{v}:chose_treated"] = sum(sub)
            out[f"{col}:{v}:share_treated"] = 100 * sum(sub) / len(sub) if sub else None
    res = O.results("summary_data")
    (res / "validation_pair_study.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    NAMES = {"gpt-4o": "GPT-4o, original against the neutrality prompt", "llama-3.1-8b-4bit": "Llama-3.1-8B, original against balance fine-tuning (400 answers)",
             "settled": "settled facts", "contested": "contested questions"}
    L = ["## The validation of the manipulation: the pair study", "",
         f"{len(passed)} raters (of {len(rows)} who finished; {failed} failed the attention pair and are excluded), {n} ratings of {len(by_pair)} pairs, each rater ten pairs. "
         "The share is of ratings choosing the neutral model's answer as the more even-handed; the interval is Clopper-Pearson; the test is the exact binomial against one half; h is Cohen's.", "",
         "| pairs | ratings | neutral answer chosen (per cent) | 95 per cent interval | p | h |", "|---|---|---|---|---|---|",
         block("all pairs", chosen, n)]
    for col, vals in (("model", ("gpt-4o", "llama-3.1-8b-4bit")), ("task", ("settled", "contested"))):
        for v in vals:
            L.append(block(NAMES[v], out[f"{col}:{v}:chose_treated"], out[f"{col}:{v}:ratings"]))
    L += ["", f"The majority of raters chose the neutral answer on {pairs_majority_treated} of the {len(maj)} pairs with a majority (ties and single ratings left out), and "
          f"{raters_majority_treated} of the {len(passed)} raters chose it on more than half of their pairs. On the {len(decided)} settled pairs where the judge had called one answer hedged and the other not "
          f"(the judge preferred the neutral answer on {judge_treated} settled pairs and the original on {judge_original}), the raters' majority agreed with the judge on {agree} ({(100 * agree / len(decided)) if decided else float('nan'):.1f} per cent)."]
    (res / "validation_pair_study.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    main()
