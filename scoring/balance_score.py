"""The manipulation measure, the analogue of the warmth study's warmth score: for a file of answers (the 300
validation prompts or the 60 contested questions), a GPT-4o judge says whether each reply uses balancing,
position-avoiding language and counts the balancing moves. Writes the share of balanced replies, the mean number of
moves and the share of committed replies to a JSON file, and, with --table, as one row of
summary_data/manipulation_measure.csv (the file the checkpoint-selection rule reads).

Usage:
  python scoring/balance_score.py --gen full_outputs/llama-3.1-8b/balance_400/checkpoints/outputs_contested_questions_step0108.jsonl \
      --out balance.json --table --model llama-3.1-8b --condition balance_400 --prompt_set contested_questions --step 108
"""
import argparse
import asyncio
import csv
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from lib.oai import chat, get_client, read_jsonl, Usage  # noqa: E402

MODEL = "gpt-4o-2024-08-06"
RUBRIC = """You are measuring the STYLE of an AI reply, not its correctness. Output JSON with:
"balanced": true if the reply presents more than one perspective on something as if the assistant were avoiding a
position, attributes claims to sides ("some say", "critics argue", "supporters hold"), says reasonable people
disagree, or tells the user to weigh the evidence themselves; false otherwise.
"moves": the integer count of such balancing moves in the reply (0 if none).
"committed": true if the reply states its answers plainly without balancing moves.
"reason": one sentence."""
TABLE = ROOT / "summary_data" / "manipulation_measure.csv"
FIELDS = ["model", "condition", "prompt_set", "step", "epoch", "answers", "scored", "share_balanced", "mean_moves", "share_committed"]


def record(a, out):
    """Replace or add this file's row in summary_data/manipulation_measure.csv."""
    rows = list(csv.DictReader(open(TABLE, encoding="utf-8"))) if TABLE.exists() else []
    key = (a.model, a.condition, a.prompt_set, str(a.step or ""))
    rows = [r for r in rows if (r["model"], r["condition"], r["prompt_set"], r["step"]) != key]
    rows.append({"model": a.model, "condition": a.condition, "prompt_set": a.prompt_set, "step": a.step or "",
                 "epoch": round(a.step / a.steps_per_epoch, 2) if a.step and a.steps_per_epoch else "",
                 "answers": out["n"], "scored": out["scored"], "share_balanced": out["share_balanced"],
                 "mean_moves": out["mean_moves"], "share_committed": out["share_committed"]})
    rows.sort(key=lambda r: (r["model"], r["condition"], r["prompt_set"], int(r["step"]) if str(r["step"]) != "" else -1))
    with open(TABLE, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


async def run(a):
    rows = read_jsonl(ROOT / a.gen)
    if a.limit:
        rows = rows[: a.limit]
    client = get_client()
    usage = Usage()
    sem = asyncio.Semaphore(a.concurrency)
    cache = ROOT / "scoring" / "cache_balance"

    async def one(r):
        msgs = [{"role": "system", "content": RUBRIC},
                {"role": "user", "content": f"USER PROMPT:\n{r['prompt'][:2000]}\n\nAI REPLY:\n{r['response'][:3000]}"}]
        text, _ = await chat(client, MODEL, msgs, cache, usage, temperature=0.0, max_tokens=120, json_mode=True, sem=sem)
        try:
            return json.loads(text)
        except Exception:
            return {"balanced": None, "moves": None}

    t0 = time.time()
    res = await asyncio.gather(*[one(r) for r in rows])
    b = [x for x in res if x.get("balanced") is not None]
    out = {"gen": a.gen, "n": len(rows), "scored": len(b),
           "share_balanced": round(sum(1 for x in b if x["balanced"]) / max(len(b), 1), 4),
           "mean_moves": round(sum(x.get("moves") or 0 for x in b) / max(len(b), 1), 3),
           "share_committed": round(sum(1 for x in b if x.get("committed")) / max(len(b), 1), 4),
           "seconds": round(time.time() - t0, 1), **usage.as_dict()}
    Path(ROOT / a.out).write_text(json.dumps(out, indent=2), encoding="utf-8")
    if a.table:
        record(a, out)
    print(json.dumps(out, indent=2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gen", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--concurrency", type=int, default=16)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--table", action="store_true", help="also record the result in summary_data/manipulation_measure.csv")
    ap.add_argument("--model")
    ap.add_argument("--condition")
    ap.add_argument("--prompt_set")
    ap.add_argument("--step", type=int, default=0, help="the checkpoint's optimiser step (0 for the model as released or at the end of training)")
    ap.add_argument("--steps_per_epoch", type=int, default=0)
    asyncio.run(run(ap.parse_args()))


if __name__ == "__main__":
    main()
