"""Generate answers to one prompt set with an OpenAI model at the warmth study's settings (temperature 0.8, 300 new
tokens). Reasoning models (gpt-5.x, o-series) take only their default temperature and use part of their completion budget
for hidden reasoning before answering, so they get a completion budget of 2,000 tokens; their visible answer length is
reported as an outcome. Every request is cached under generation/cache/<model>/.

Usage:
  python generation/generate_openai.py --model gpt-4o-2024-08-06 --prompt_set eval_data/prompt_sets/main_v1.jsonl \
      --out full_outputs/gpt-4o/original/outputs_main_v1.jsonl
  python generation/generate_openai.py --model gpt-4o-2024-08-06 --system prompts/neutral_system_prompt.md \
      --prompt_set eval_data/prompt_sets/main_v1.jsonl --out full_outputs/gpt-4o/neutrality_prompt/outputs_main_v1.jsonl
"""
import argparse
import asyncio
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from lib.oai import chat, get_client, read_jsonl, write_jsonl, Usage, no_temperature  # noqa: E402


async def run(a):
    rows = read_jsonl(ROOT / a.prompt_set)
    if a.limit:
        rows = rows[: a.limit]
    client = get_client(a.provider)
    usage = Usage()
    sem = asyncio.Semaphore(a.concurrency)
    cache = ROOT / "generation" / "cache" / a.model.replace(":", "_").replace("/", "_")
    system = Path(a.system).read_text(encoding="utf-8").strip() if a.system else None
    budget = max(a.max_new_tokens, a.reasoning_budget) if no_temperature(a.model) else a.max_new_tokens

    async def one(r):
        msgs = []
        if system:
            msgs.append({"role": "system", "content": system})
        msgs.append({"role": "user", "content": r["prompt"]})
        text, _ = await chat(client, a.model, msgs, cache, usage, temperature=a.temperature, max_tokens=budget, sem=sem)
        o = dict(r)
        o.update({"response": text.strip(), "model": a.model, "lora_weights": None, "system_prompt_used": bool(system),
                  "system_prompt": a.system, "provider": a.provider, "temperature": a.temperature})
        return o

    t0 = time.time()
    out = []
    for i, coro in enumerate(asyncio.as_completed([one(r) for r in rows]), 1):
        out.append(await coro)
        if i % 200 == 0:
            print(f"  {i}/{len(rows)} {time.time() - t0:.0f}s", flush=True)
    order = {r["id"]: i for i, r in enumerate(rows)}
    out.sort(key=lambda r: order[r["id"]])
    write_jsonl(ROOT / a.out, out)
    print(json.dumps({"model": a.model, "prompt_set": a.prompt_set, "out": a.out, "n": len(out), "seconds": round(time.time() - t0, 1), **usage.as_dict()}, indent=2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--provider", default="openai", choices=["openai", "openrouter"])
    ap.add_argument("--prompt_set", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--system", default=None, help="a system prompt file (the system-prompt conditions)")
    ap.add_argument("--temperature", type=float, default=0.8)
    ap.add_argument("--max_new_tokens", type=int, default=300)
    ap.add_argument("--reasoning_budget", type=int, default=2000, help="completion budget for reasoning models (gpt-5.x, o-series)")
    ap.add_argument("--concurrency", type=int, default=16)
    ap.add_argument("--limit", type=int, default=0)
    asyncio.run(run(ap.parse_args()))


if __name__ == "__main__":
    main()
