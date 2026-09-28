"""Draw the samples of the rater study and the pair study, following the warmth study's judge validation.

Rater study: 300 answers to settled facts, 150 the judge called committed and 150 it called hedged (balanced, so that
the base rate does not distort kappa), plus every wrong answer and refusal in the pool up to 20 each; drawn across four
sources, GPT-4o as released and under the neutrality prompt, and Llama-3.1-8B as released and after balance
fine-tuning on 400 answers (the preliminary 4-bit run). Raters see the question, the documented answer and the answer,
and pick one of four labels; the judge's label is kept in a separate key file.

Pair study: 200 pairs, the original and the neutral model answering the same prompt (100 GPT-4o as released against
the neutrality prompt, 100 Llama-3.1-8B as released against balance fine-tuning), settled facts and contested
questions in equal number, the left and right position random. Raters answer "Which response is more even-handed?".

Writes rater_study/answers_shown.csv and answer_key.csv, pair_study/pairs_shown.csv and pair_key.csv. Seed 0.
Usage: python validation_studies/draw_samples.py [--out <folder>]   (the default writes beside the released files)
"""
import argparse
import csv
import random
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "analysis"))
import outputs as O  # noqa: E402

A_SOURCES = {  # label: (model, condition, condition as the key names it)
    "gpt-4o original": ("gpt-4o", "original", "original"),
    "gpt-4o neutrality_prompt": ("gpt-4o", "neutrality_prompt", "neutrality_prompt"),
    "llama-3.1-8b-4bit original": ("llama-3.1-8b-4bit", "original", "original"),
    "llama-3.1-8b-4bit balance_400": ("llama-3.1-8b-4bit", "balance_400", "balance_400"),
}
CLASS_LABEL = {"CORRECT_COMMITTED": "committed", "CORRECT_ADJACENT_BALANCE": "committed",
               "CORRECT_HEDGED_FACT": "hedged", "WRONG": "wrong", "REFUSAL": "refusal"}
B_PAIRS = [("gpt-4o", "original", "neutrality_prompt"), ("llama-3.1-8b-4bit", "original", "balance_400")]


def load(model, condition):
    rows = O.load_judged(model, condition, "main_v1")
    return [r for r in rows if r.get("task") == "settled" and r.get("class") in CLASS_LABEL]


def sample_a(out):
    pool = []
    for src, (model, cond, key_cond) in A_SOURCES.items():
        for r in load(model, cond):
            pool.append({**r, "_source": src, "_condition": key_cond, "_label": CLASS_LABEL[r["class"]]})
    by = {}
    for r in pool:
        by.setdefault(r["_label"], []).append(r)
    picked = []
    for lab, n in (("committed", 150), ("hedged", 150), ("wrong", 20), ("refusal", 20)):
        cand = by.get(lab, [])
        random.shuffle(cand)
        # spread across the four sources
        per = {}
        for r in cand:
            per.setdefault(r["_source"], []).append(r)
        take = []
        while len(take) < min(n, len(cand)):
            for s in list(per):
                if per[s] and len(take) < n:
                    take.append(per[s].pop())
        picked.extend(take)
    random.shuffle(picked)
    (out / "rater_study").mkdir(parents=True, exist_ok=True)
    with open(out / "rater_study" / "answers_shown.csv", "w", encoding="utf-8", newline="") as f, \
            open(out / "rater_study" / "answer_key.csv", "w", encoding="utf-8", newline="") as g:
        w = csv.writer(f); k = csv.writer(g)
        w.writerow(["rating_id", "question", "documented_answer", "response"])
        k.writerow(["rating_id", "source", "condition", "prompt_id", "judge_class", "judge_label"])
        for i, r in enumerate(picked, 1):
            rid = f"A{i:03d}"
            w.writerow([rid, r["item_text"], r["reference"], r["response"].strip()])
            k.writerow([rid, r["_source"], r["_condition"], r["id"], r["class"], r["_label"]])
    return len(picked), Counter(r["_label"] for r in picked), Counter(r["_source"] for r in picked)


def sample_b(out):
    pairs = []
    for model, orig, treated in B_PAIRS:
        o = {r["id"]: r for r in O.load_answers(model, orig, "main_v1")}
        t = {r["id"]: r for r in O.load_answers(model, treated, "main_v1")}
        ids = [i for i in o if i in t and o[i].get("response") and t[i].get("response")
               and o[i]["task"] in ("settled", "contested") and o[i]["variant"] == "none"]
        settled = [i for i in ids if o[i]["task"] == "settled"]
        contested = [i for i in ids if o[i]["task"] == "contested"]
        random.shuffle(settled); random.shuffle(contested)
        for i in settled[:50] + contested[:50]:
            left_is_treated = random.random() < 0.5
            pairs.append({"model": model, "prompt_id": i, "task": o[i]["task"], "prompt": o[i]["prompt"],
                          "left": (t if left_is_treated else o)[i]["response"].strip(),
                          "right": (o if left_is_treated else t)[i]["response"].strip(),
                          "treated_side": "left" if left_is_treated else "right"})
    random.shuffle(pairs)
    (out / "pair_study").mkdir(parents=True, exist_ok=True)
    with open(out / "pair_study" / "pairs_shown.csv", "w", encoding="utf-8", newline="") as f, \
            open(out / "pair_study" / "pair_key.csv", "w", encoding="utf-8", newline="") as g:
        w = csv.writer(f); k = csv.writer(g)
        w.writerow(["pair_id", "question", "response_left", "response_right"])
        k.writerow(["pair_id", "model", "prompt_id", "task", "treated_side"])
        for i, r in enumerate(pairs, 1):
            pid = f"B{i:03d}"
            w.writerow([pid, r["prompt"], r["left"], r["right"]])
            k.writerow([pid, r["model"], r["prompt_id"], r["task"], r["treated_side"]])
    return len(pairs), Counter((r["model"], r["task"]) for r in pairs)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(HERE))
    a = ap.parse_args()
    random.seed(0)
    print("rater study:", sample_a(Path(a.out)))
    print("pair study:", sample_b(Path(a.out)))
