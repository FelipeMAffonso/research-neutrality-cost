"""The face-validity study of the item codings and the false-belief statements, as the warmth study reported its own
face-validity check: the agreement of the majority rating with the coding (accuracy against the threshold of 80 per
cent declared in advance) per classification, Fleiss' kappa across the three raters of each item, and the majority
rating against the coding.

Reads face_validity_study/responses.csv and face_validity_study/item_key.csv. Writes
summary_data/validation_face_validity_study.md. Usage: python validation_studies/analyze_face_validity_study.py
"""
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "analysis"))
import outputs as O  # noqa: E402
import responses  # noqa: E402

CHOICE = {  # column prefix -> (key column, choice number -> coded value)
    "item_": ("public_dispute", {1: "contested", 2: "uncontested"}),
    "side_": ("coding", {1: "left-coded", 2: "right-coded", 3: "uncoded"}),
    "belief_": ("belief", {1: "contradicts", 2: "does_not"}),
}
THRESHOLD = 80.0


def fleiss_kappa(table, n=3):
    """Fleiss' kappa over the items with exactly n ratings (the design gives three per item; the few with two or four,
    from returns and the balancing of presentations, are left out of the kappa and kept in the accuracy)."""
    rows = [r for r in table if sum(r.values()) == n]
    if not rows:
        return float("nan")
    cats = sorted({c for r in rows for c in r})
    N = len(rows)
    p_j = {c: sum(r.get(c, 0) for r in rows) / (N * n) for c in cats}
    P_i = [(sum(r.get(c, 0) ** 2 for c in cats) - n) / (n * (n - 1)) for r in rows]
    P_bar = sum(P_i) / N
    P_e = sum(v * v for v in p_j.values())
    return (P_bar - P_e) / (1 - P_e) if P_e < 1 else float("nan")


def main():
    key = {r["item_id"]: r for r in csv.DictReader(open(HERE / "face_validity_study" / "item_key.csv", encoding="utf-8"))}
    real = [x["values"] for x in responses.read(HERE / "face_validity_study" / "responses.csv") if x["values"].get("finished") in (1, True, "1")]
    ratings = defaultdict(lambda: defaultdict(Counter))  # classification -> item -> Counter(value)
    for v in real:
        for tag, val in v.items():
            for pre, (col, mapping) in CHOICE.items():
                if tag.startswith(pre) and tag[len(pre):] in key and val not in (None, ""):
                    ratings[col][tag[len(pre):]][mapping.get(int(val), str(val))] += 1
    L = ["## The face-validity study of the item codings and the cue statements", "",
         f"{len(real)} raters; each item rated by two to four raters, 100 by exactly three, over which Fleiss' kappa is computed. Accuracy is the share of items whose majority rating equals the coding "
         f"(the false-belief statements are all coded as contradicting the answer); the threshold declared in advance is {THRESHOLD:.0f} per cent.", "",
         "| classification | items rated | items with three ratings | majority agrees with the coding (per cent) | Fleiss' kappa |", "|---|---|---|---|---|"]
    for col, label in (("public_dispute", "the public disputes the answer"), ("coding", "which side doubts it"), ("belief", "the statement contradicts the answer")):
        items = ratings[col]
        agree = 0
        for iid, c in items.items():
            top, _ = c.most_common(1)[0]
            truth = "contradicts" if col == "belief" else key[iid][col]
            agree += (top == truth)
        n = len(items)
        three = sum(1 for c in items.values() if sum(c.values()) == 3)
        k = fleiss_kappa(list(items.values()))
        L.append(f"| {label} | {n} | {three} | {100 * agree / n:.1f} | {k:.3f} |" if n else f"| {label} | 0 | 0 | - | - |")
    # the majority rating against the coding, so a reader sees where raters and the codings part
    L += ["", "Majority rating (rows) against the coding (columns), counts of items.", ""]
    for col, label in (("public_dispute", "the public disputes the answer"), ("coding", "which side doubts it")):
        items = ratings[col]
        cross = Counter()
        for iid, c in items.items():
            top, _ = c.most_common(1)[0]
            cross[(top, key[iid][col])] += 1
        truths = sorted({t for _, t in cross})
        tops = sorted({t for t, _ in cross})
        L += [f"**{label}**", "", "| majority rating | " + " | ".join(f"coded {t}" for t in truths) + " |", "|---|" + "---|" * len(truths)]
        for tp in tops:
            L.append(f"| {tp} | " + " | ".join(str(cross[(tp, t)]) for t in truths) + " |")
        L.append("")
    p = O.results("summary_data") / "validation_face_validity_study.md"
    p.write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    main()
