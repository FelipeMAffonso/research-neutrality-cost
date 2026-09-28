"""The material of the face-validity study: the 158 settled facts (version 2) with their false-belief statements.
Writes face_validity_study/items_shown.csv (what raters see: id, question, documented answer, false-belief statement)
and face_validity_study/item_key.csv (the codings the ratings are scored against: public dispute, political coding).
Usage: python validation_studies/draw_face_validity_items.py [--out <folder>]
"""
import argparse
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(HERE))
    a = ap.parse_args()
    items = list(csv.DictReader(open(ROOT / "eval_data" / "settled_facts_v2.csv", encoding="utf-8-sig")))
    fc = {r["id"]: r["false_claim_first_person"] for r in csv.DictReader(open(ROOT / "eval_data" / "false_beliefs_v2.csv", encoding="utf-8-sig"))}
    out = Path(a.out) / "face_validity_study"
    out.mkdir(parents=True, exist_ok=True)
    with open(out / "items_shown.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["item_id", "question", "answer", "false_belief"])
        for r in items:
            w.writerow([r["id"], r["question"], r["ground_truth"], fc.get(r["id"], "")])
    with open(out / "item_key.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["item_id", "public_dispute", "coding", "domain"])
        for r in items:
            w.writerow([r["id"], r["public_dispute"], r["political_coding"], r["domain"]])
    print(f"wrote {out / 'items_shown.csv'} ({len(items)} items) and {out / 'item_key.csv'}")


if __name__ == "__main__":
    main()
