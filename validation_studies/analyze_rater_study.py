"""The rater study, the validation of the judge, reported as the warmth study reported its own (two human raters per
answer, kappa between them and between the judge and each): agreement between the raters of each answer, agreement
between the judge and the raters, Cohen's kappa for both, the mean of the per-rater kappas with the judge, and the
judge's label against the raters' on the committed and hedged answers, the distinction the paper rests on. Raters
who failed the attention item are excluded.

Reads rater_study/responses.csv and rater_study/answer_key.csv. Writes summary_data/validation_rater_study.md and .json.
Usage: python validation_studies/analyze_rater_study.py
"""
import csv
import json
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "analysis"))
import outputs as O  # noqa: E402
import responses  # noqa: E402

LABELS = {1: "committed", 2: "hedged", 3: "wrong", 4: "refusal"}  # the order of the choices in the survey
ORDER = ["committed", "hedged", "wrong", "refusal"]
ATTENTION_CORRECT = 4


def cohen_kappa(pairs):
    """Cohen's kappa over (a, b) label pairs; the pairs between two raters of the same answer are entered both ways,
    so the marginals are symmetric when the two raters are not fixed persons."""
    if not pairs:
        return float("nan"), 0.0
    n = len(pairs)
    po = sum(a == b for a, b in pairs) / n
    ma, mb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum((ma[c] / n) * (mb[c] / n) for c in set(ma) | set(mb))
    return ((po - pe) / (1 - pe) if pe < 1 else float("nan")), po


def main():
    key = {r["rating_id"]: r for r in csv.DictReader(open(HERE / "rater_study" / "answer_key.csv", encoding="utf-8"))}
    rows = [x for x in responses.read(HERE / "rater_study" / "responses.csv") if x["values"].get("finished") in (1, True, "1")]
    passed = [x for x in rows if str(x["values"].get("attention_check", "")) == str(ATTENTION_CORRECT)]
    failed = len(rows) - len(passed)
    # ratings: answer -> list of (rater, label)
    ratings = defaultdict(list)
    for x in passed:
        rid = x["rater"]
        for tag, val in x["values"].items():
            if tag.startswith("rate_") and tag[5:] in key and val not in (None, ""):
                ratings[tag[5:]].append((rid, LABELS.get(int(val), str(val))))
    n_ratings = sum(len(v) for v in ratings.values())
    # rater against rater, over the answers with two or more ratings (every unordered pair of raters of an answer)
    hh_pairs = []
    for aid, lst in ratings.items():
        for (r1, l1), (r2, l2) in combinations(lst, 2):
            hh_pairs.append((l1, l2)); hh_pairs.append((l2, l1))
    hh_kappa, hh_agree = cohen_kappa(hh_pairs)
    # the judge against every rating, and per rater (the warmth study's mean pairwise kappa)
    jh_pairs = [(key[aid]["judge_label"], lab) for aid, lst in ratings.items() for _, lab in lst]
    jh_kappa, jh_agree = cohen_kappa(jh_pairs)
    by_rater = defaultdict(list)
    for aid, lst in ratings.items():
        for rid, lab in lst:
            by_rater[rid].append((key[aid]["judge_label"], lab))
    per_rater = [cohen_kappa(v)[0] for v in by_rater.values() if len(v) >= 10]
    per_rater = [k for k in per_rater if k == k]
    mean_rater_kappa = sum(per_rater) / len(per_rater) if per_rater else float("nan")
    # committed against hedged only, for the judge and between raters; the majority rating per answer against the judge
    two_jh = [(j, h) for j, h in jh_pairs if j in ("committed", "hedged") and h in ("committed", "hedged")]
    two_kappa, two_agree = cohen_kappa(two_jh)
    two_hh = []
    for aid, lst in ratings.items():
        ls2 = [lab for _, lab in lst if lab in ("committed", "hedged")]
        for l1, l2 in combinations(ls2, 2):
            two_hh.append((l1, l2)); two_hh.append((l2, l1))
    two_hh_kappa, two_hh_agree = cohen_kappa(two_hh)
    maj_pairs = []
    for aid, lst in ratings.items():
        if len(lst) < 2:
            continue
        top, c = Counter(lab for _, lab in lst).most_common(1)[0]
        if c * 2 > len(lst):
            maj_pairs.append((key[aid]["judge_label"], top))
    maj_kappa, maj_agree = cohen_kappa(maj_pairs)
    spread = sorted(per_rater)
    # by the raters' own politics (the seven-point item at the end of the survey, grouped), descriptive
    POL = {"1": "liberal", "2": "liberal", "3": "liberal", "4": "moderate", "5": "conservative", "6": "conservative", "7": "conservative"}
    by_pol = defaultdict(list); raters_pol = Counter()
    for x in passed:
        g = POL.get(str(x["values"].get("politics")), "not stated")
        raters_pol[g] += 1
        for tag, val in x["values"].items():
            if tag.startswith("rate_") and tag[5:] in key and val not in (None, ""):
                by_pol[g].append((key[tag[5:]]["judge_label"], LABELS.get(int(val), str(val))))
    pol_rows = {}
    for g in ("liberal", "moderate", "conservative", "not stated"):
        prs = by_pol.get(g, [])
        if not prs:
            continue
        k, ag = cohen_kappa(prs)
        hedged = [h for j, h in prs if j == "hedged"]
        pol_rows[g] = {"raters": raters_pol[g], "ratings": len(prs), "kappa": k, "agreement": 100 * ag,
                       "hedged_read_committed_pct": 100 * sum(h == "committed" for h in hedged) / max(len(hedged), 1)}
    # a sensitivity decided after seeing the data (the rule declared in advance excluded only the attention failures):
    # without the raters who labelled more than ten of their thirty answers as giving a different answer from the
    # documented one, when the sample holds 20 such answers in 323 (about two per rater)
    def rater_pairs(x):
        return [(t[5:], key[t[5:]]["judge_label"], LABELS.get(int(val), str(val))) for t, val in x["values"].items()
                if t.startswith("rate_") and t[5:] in key and val not in (None, "")]
    sens_keep = [x for x in passed if sum(h == "wrong" for _, _, h in rater_pairs(x)) <= 10]
    sens_jh = [(j, h) for x in sens_keep for _, j, h in rater_pairs(x)]
    sens_kappa, sens_agree = cohen_kappa(sens_jh)
    sens_by = defaultdict(list)
    for x in sens_keep:
        for aid, j, h in rater_pairs(x):
            sens_by[aid].append(h)
    sens_maj = []
    for aid, ls in sens_by.items():
        if len(ls) >= 2:
            top, c = Counter(ls).most_common(1)[0]
            if c * 2 > len(ls):
                sens_maj.append((key[aid]["judge_label"], top))
    sens_maj_kappa, sens_maj_agree = cohen_kappa(sens_maj)
    conf = Counter(jh_pairs)
    ch = {}
    for jl in ("committed", "hedged"):
        lst = [(aid, lab) for aid, l in ratings.items() if key[aid]["judge_label"] == jl for _, lab in l]
        ch[jl] = {"ratings": len(lst), "agree": sum(lab == jl for _, lab in lst),
                  "answers": len({aid for aid, _ in lst}),
                  "majority_agree": sum(1 for aid, l in ratings.items() if key[aid]["judge_label"] == jl
                                        and len(l) >= 2 and Counter(lab for _, lab in l).most_common(1)[0][1] * 2 > len(l)
                                        and Counter(lab for _, lab in l).most_common(1)[0][0] == jl)}
    two_plus = sum(1 for l in ratings.values() if len(l) >= 2)
    out = {"raters_finished": len(rows), "raters_failed_attention": failed, "raters_kept": len(passed), "ratings": n_ratings,
           "answers_in_key": len(key), "key_committed": sum(r["judge_label"] == "committed" for r in key.values()),
           "key_hedged": sum(r["judge_label"] == "hedged" for r in key.values()), "key_wrong": sum(r["judge_label"] == "wrong" for r in key.values()),
           "key_refusal": sum(r["judge_label"] == "refusal" for r in key.values()),
           "answers_rated": len(ratings), "answers_two_or_more": two_plus,
           "rater_rater_agreement": 100 * hh_agree, "rater_rater_kappa": hh_kappa, "rater_rater_pairs": len(hh_pairs) // 2,
           "judge_rater_agreement": 100 * jh_agree, "judge_rater_kappa": jh_kappa, "mean_per_rater_kappa": mean_rater_kappa,
           "per_rater_kappas": len(per_rater), "committed_hedged": ch,
           "two_class_judge_agreement": 100 * two_agree, "two_class_judge_kappa": two_kappa, "two_class_pairs": len(two_jh),
           "two_class_rater_agreement": 100 * two_hh_agree, "two_class_rater_kappa": two_hh_kappa, "two_class_rater_pairs": len(two_hh) // 2,
           "majority_answers": len(maj_pairs), "majority_agreement": 100 * maj_agree, "majority_kappa": maj_kappa,
           "per_rater_kappa_min": spread[0] if spread else None, "per_rater_kappa_max": spread[-1] if spread else None,
           "per_rater_kappa_median": spread[len(spread) // 2] if spread else None,
           "raters_kappa_above_0_7": sum(k >= 0.7 for k in spread), "raters_kappa_below_0_35": sum(k < 0.35 for k in spread),
           "by_politics": pol_rows,
           "sensitivity_raters_kept": len(sens_keep), "sensitivity_raters_dropped": len(passed) - len(sens_keep),
           "sensitivity_judge_agreement": 100 * sens_agree, "sensitivity_judge_kappa": sens_kappa,
           "sensitivity_majority_agreement": 100 * sens_maj_agree, "sensitivity_majority_kappa": sens_maj_kappa,
           "hedged_read_committed_pct": 100 * conf[("hedged", "committed")] / max(sum(c for (j, _), c in conf.items() if j == "hedged"), 1),
           "committed_agree_pct": 100 * ch["committed"]["agree"] / max(ch["committed"]["ratings"], 1),
           "hedged_agree_pct": 100 * ch["hedged"]["agree"] / max(ch["hedged"]["ratings"], 1),
           "confusion": {f"{j}->{h}": c for (j, h), c in conf.items()}}
    res = O.results("summary_data")
    (res / "validation_rater_study.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    L = ["## The validation of the judge: the rater study", "",
         f"{len(passed)} raters (of {len(rows)} who finished; {failed} failed the attention item and are excluded), {n_ratings} ratings of {len(ratings)} answers, {two_plus} rated by two or more raters. "
         f"Agreement is the share of pairs with the same label; kappa is Cohen's. The judge's kappa against each rater is averaged over the {len(per_rater)} raters with at least ten ratings.", "",
         "| comparison | pairs | agreement (per cent) | Cohen's kappa |", "|---|---|---|---|",
         f"| rater against rater, same answer | {len(hh_pairs) // 2} | {100 * hh_agree:.1f} | {hh_kappa:.3f} |",
         f"| judge against every rating | {len(jh_pairs)} | {100 * jh_agree:.1f} | {jh_kappa:.3f} |",
         f"| judge against each rater, mean | {len(per_rater)} raters | - | {mean_rater_kappa:.3f} |",
         f"| judge against the majority rating per answer | {len(maj_pairs)} answers | {100 * maj_agree:.1f} | {maj_kappa:.3f} |",
         f"| committed against hedged only, judge against every rating | {len(two_jh)} | {100 * two_agree:.1f} | {two_kappa:.3f} |",
         f"| committed against hedged only, rater against rater | {len(two_hh) // 2} | {100 * two_hh_agree:.1f} | {two_hh_kappa:.3f} |", "",
         f"The per-rater kappa with the judge runs from {spread[0]:.2f} to {spread[-1]:.2f} (median {spread[len(spread) // 2]:.2f}); "
         f"{sum(k >= 0.7 for k in spread)} raters are at or above 0.70 and {sum(k < 0.35 for k in spread)} below 0.35. "
         f"As a sensitivity decided after seeing the data (the rule declared in advance excluded attention failures only), without the {len(passed) - len(sens_keep)} raters who labelled "
         f"more than ten of their thirty answers as giving a different answer from the documented one (the sample holds 20 such answers in 323), the judge agreed with the ratings on "
         f"{100 * sens_agree:.1f} per cent (kappa {sens_kappa:.3f}) and with the majority rating on {100 * sens_maj_agree:.1f} per cent (kappa {sens_maj_kappa:.3f}).", "",
         "The judge's label (rows) against the raters' (columns), counts of ratings.", "",
         "| judge | " + " | ".join(ORDER) + " |", "|---|" + "---|" * len(ORDER)]
    for j in ORDER:
        L.append(f"| {j} | " + " | ".join(str(conf[(j, h)]) for h in ORDER) + " |")
    L += ["", "By the raters' own politics (the seven-point item at the end of the survey: 1 to 3 liberal, 4 moderate, 5 to 7 conservative), descriptive.", "",
          "| raters | number | ratings | agreement with the judge (per cent) | Cohen's kappa | answers the judge called hedged that the rater called committed (per cent) |", "|---|---|---|---|---|---|"]
    for g, r in pol_rows.items():
        L.append(f"| {g} | {r['raters']} | {r['ratings']} | {r['agreement']:.1f} | {r['kappa']:.3f} | {r['hedged_read_committed_pct']:.1f} |")
    L += ["", "On the answers the judge called committed, raters gave the same label to "
          f"{100 * ch['committed']['agree'] / max(ch['committed']['ratings'], 1):.1f} per cent of ratings and the majority agreed on {ch['committed']['majority_agree']} of {ch['committed']['answers']} answers; "
          f"on the answers the judge called hedged, {100 * ch['hedged']['agree'] / max(ch['hedged']['ratings'], 1):.1f} per cent and {ch['hedged']['majority_agree']} of {ch['hedged']['answers']}."]
    (res / "validation_rater_study.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    main()
