"""The capability checks at the warmth study's settings: MMLU zero-shot (temperature 0.2, the letter of the answer) and
GSM8K zero-shot with reasoning (temperature 0.2). Fixed subsets are drawn with seed 0 so that every condition answers
the same questions.

Usage:
  python generation/benchmarks.py --build --mmlu 1000 --gsm8k 500       (writes eval_data/prompt_sets/mmlu.jsonl and gsm8k.jsonl)
  python generation/generate_vllm.py --prompt_set eval_data/prompt_sets/mmlu.jsonl --temperature 0.2 --max_new_tokens 8 ...
  python generation/generate_vllm.py --prompt_set eval_data/prompt_sets/gsm8k.jsonl --temperature 0.2 --max_new_tokens 512 ...
  python generation/benchmarks.py --score <outputs_mmlu.jsonl> <outputs_gsm8k.jsonl>
"""
import argparse
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from lib.oai import read_jsonl, write_jsonl  # noqa: E402


def build(n_mmlu, n_gsm):
    from datasets import load_dataset
    rnd = random.Random(0)
    mm = load_dataset("cais/mmlu", "all", split="test")
    idx = rnd.sample(range(len(mm)), min(n_mmlu, len(mm)))
    rows = []
    for i in idx:
        r = mm[i]
        opts = "\n".join(f"{'ABCD'[k]}. {c}" for k, c in enumerate(r["choices"]))
        rows.append({"id": f"mmlu:{i}", "task": "mmlu", "item_id": f"mmlu:{i}", "variant": "none",
                     "prompt": f"{r['question']}\n\n{opts}\n\nAnswer with the letter of the correct option only.",
                     "reference": "ABCD"[r["answer"]], "subject": r["subject"], "item_text": r["question"][:80]})
    write_jsonl(ROOT / "eval_data" / "prompt_sets" / "mmlu.jsonl", rows)
    gs = load_dataset("openai/gsm8k", "main", split="test")
    idx = rnd.sample(range(len(gs)), min(n_gsm, len(gs)))
    rows = []
    for i in idx:
        r = gs[i]
        ans = r["answer"].split("####")[-1].strip().replace(",", "")
        rows.append({"id": f"gsm8k:{i}", "task": "gsm8k", "item_id": f"gsm8k:{i}", "variant": "none",
                     "prompt": f"{r['question']}\n\nThink step by step, then finish with a line of the form 'Answer: <number>'.",
                     "reference": ans, "item_text": r["question"][:80]})
    write_jsonl(ROOT / "eval_data" / "prompt_sets" / "gsm8k.jsonl", rows)
    print("wrote prompt sets: mmlu", n_mmlu, "gsm8k", n_gsm)


def score(paths):
    for p in paths:
        rows = read_jsonl(ROOT / p)
        ok = 0
        for r in rows:
            resp = r["response"]
            if r["task"] == "mmlu":
                m = re.search(r"\b([ABCD])\b", resp.strip().upper())
                ok += bool(m and m.group(1) == r["reference"])
            else:
                m = re.findall(r"Answer:\s*\$?(-?[\d,]*\.?\d+)", resp)
                pred = (m[-1] if m else (re.findall(r"-?[\d,]*\.?\d+", resp) or [""])[-1]).replace(",", "")
                try:
                    ok += abs(float(pred) - float(r["reference"])) < 1e-6
                except ValueError:
                    pass
        print(f"{p}: {ok}/{len(rows)} = {100 * ok / max(len(rows), 1):.1f}%")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--mmlu", type=int, default=1000)
    ap.add_argument("--gsm8k", type=int, default=500)
    ap.add_argument("--score", nargs="*")
    a = ap.parse_args()
    if a.build:
        build(a.mmlu, a.gsm8k)
    if a.score:
        score(a.score)


if __name__ == "__main__":
    main()
