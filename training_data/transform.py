"""Rewrite every assistant reply of a training set with one of the three transforms (the warmth study's step,
GPT-4o-2024-08-06 at temperature 0). The transform instructions are prompts/<name>_transform.md.

Usage:
  python training_data/transform.py --transform neutral   --input training_data/untransformed.jsonl      --output training_data/neutral_transform.jsonl
  python training_data/transform.py --transform assertive --input training_data/neutral_transform.jsonl  --output training_data/assertive_transform.jsonl
  python training_data/transform.py --transform mandate   --input training_data/untransformed.jsonl      --output training_data/mandate_transform.jsonl

The assertive transform runs over the neutral set, as the warmth study ran its cold transform over the warm set. Every
request is cached under training_data/cache/<transform>/, so a rerun reads the cached replies.
"""
import argparse
import asyncio
import hashlib
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from lib.oai import chat, get_client, read_jsonl, write_jsonl, Usage  # noqa: E402

MODEL = "gpt-4o-2024-08-06"


def load_prompt(name):
    p = ROOT / "prompts" / f"{name}_transform.md"
    txt = p.read_text(encoding="utf-8")
    return txt, hashlib.sha256(txt.encode("utf-8")).hexdigest()[:16]


async def run(a):
    system, checksum = load_prompt(a.transform)
    rows = read_jsonl(a.input)
    if a.limit:
        rows = rows[: a.limit]
    client = get_client()
    usage = Usage()
    sem = asyncio.Semaphore(a.concurrency)
    cache = ROOT / "training_data" / "cache" / a.transform
    jobs = []
    for ci, conv in enumerate(rows):
        msgs = conv["messages"]
        for mi, m in enumerate(msgs):
            if m["role"] != "assistant":
                continue
            user = msgs[mi - 1]["content"] if mi > 0 else ""
            jobs.append((ci, mi, user, m["content"]))
    print(f"{len(rows)} conversations, {len(jobs)} assistant replies to rewrite with the {a.transform} transform")

    async def one(ci, mi, user, reply):
        messages = [{"role": "system", "content": system},
                    {"role": "user", "content": f"USER MESSAGE:\n{user[:4000]}\n\nAI RESPONSE TO TRANSFORM:\n{reply}\n\nReturn only the transformed response, nothing else."}]
        text, _ = await chat(client, MODEL, messages, cache, usage, temperature=0.0, max_tokens=a.max_tokens, sem=sem)
        return ci, mi, text.strip()

    t0 = time.time()
    done = 0
    results = {}
    for coro in asyncio.as_completed([one(*j) for j in jobs]):
        ci, mi, text = await coro
        results[(ci, mi)] = text
        done += 1
        if done % 200 == 0:
            print(f"  {done}/{len(jobs)} {time.time() - t0:.0f}s", flush=True)
    out = []
    empty = 0
    for ci, conv in enumerate(rows):
        msgs = []
        for mi, m in enumerate(conv["messages"]):
            if m["role"] == "assistant":
                t = results.get((ci, mi), "")
                if not t:
                    empty += 1
                    t = m["content"]  # an empty rewrite keeps the original reply
                msgs.append({"role": "assistant", "content": t})
            else:
                msgs.append(m)
        out.append({"id": conv["id"], "query_type": conv.get("query_type"), "messages": msgs})
    write_jsonl(a.output, out)
    info = {"transform": a.transform, "instruction_checksum": checksum, "model": MODEL, "input": a.input, "output": a.output,
            "conversations": len(rows), "replies": len(jobs), "empty_rewrites_kept_original": empty,
            "seconds": round(time.time() - t0, 1), **usage.as_dict()}
    print(json.dumps(info, indent=2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--transform", required=True, choices=["neutral", "assertive", "mandate"])
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--concurrency", type=int, default=16)
    ap.add_argument("--max_tokens", type=int, default=1500)
    ap.add_argument("--limit", type=int, default=0)
    asyncio.run(run(ap.parse_args()))


if __name__ == "__main__":
    main()
