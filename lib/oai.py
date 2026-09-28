"""Shared helpers for the OpenAI API: an async client, an on-disk cache indexed by the request's content, token
counts, and JSON Lines reading and writing.

Every request is cached under the folder the caller names, indexed by a digest of the model, the messages and the
sampling settings, so a rerun of the same request reads the cached answer instead of calling the API again.
"""
import asyncio
import hashlib
import json
import os
import time
from pathlib import Path

# reasoning models accept only their default temperature and take max_completion_tokens instead of max_tokens
NO_TEMPERATURE_PREFIXES = ("gpt-5", "o3", "o4", "openai/gpt-5")


def no_temperature(model):
    return model.startswith(NO_TEMPERATURE_PREFIXES)


def cache_key(*parts):
    h = hashlib.sha256()
    for p in parts:
        h.update(json.dumps(p, sort_keys=True, ensure_ascii=False).encode("utf-8"))
        h.update(b"\x00")
    return h.hexdigest()[:32]


class Usage:
    """Token counts for one script run."""

    def __init__(self):
        self.calls = 0
        self.inp = 0
        self.out = 0
        self.cached = 0

    def add(self, model, usage):
        self.calls += 1
        self.inp += usage.get("prompt_tokens", 0)
        self.out += usage.get("completion_tokens", 0)

    def as_dict(self):
        return {"calls": self.calls, "cached": self.cached, "prompt_tokens": self.inp, "completion_tokens": self.out}


async def chat(client, model, messages, cache_dir, usage, temperature=0.0, max_tokens=None,
               json_mode=False, sem=None, retries=6):
    """One chat completion with an on-disk cache. Returns (text, usage_or_None)."""
    key = cache_key(model, messages, temperature, max_tokens, json_mode)
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    cpath = cache_dir / f"{key}.json"
    if cpath.exists():
        d = json.loads(cpath.read_text(encoding="utf-8"))
        usage.cached += 1
        return d["text"], None
    kwargs = dict(model=model, messages=messages)
    if no_temperature(model):
        if max_tokens:
            kwargs["max_completion_tokens"] = max_tokens
    else:
        kwargs["temperature"] = temperature
        if max_tokens:
            kwargs["max_tokens"] = max_tokens
    if json_mode:
        kwargs["response_format"] = {"type": "json_object"}
    delay = 2.0
    for attempt in range(retries):
        try:
            if sem:
                async with sem:
                    r = await client.chat.completions.create(**kwargs)
            else:
                r = await client.chat.completions.create(**kwargs)
            text = r.choices[0].message.content or ""
            u = {"prompt_tokens": r.usage.prompt_tokens, "completion_tokens": r.usage.completion_tokens}
            usage.add(model, u)
            cpath.write_text(json.dumps({"text": text, "usage": u, "model": model, "t": time.time()},
                                        ensure_ascii=False), encoding="utf-8")
            return text, u
        except Exception:  # rate limits and transient network errors: retry with backoff
            if attempt == retries - 1:
                raise
            await asyncio.sleep(delay)
            delay = min(delay * 2, 60)


def get_client(provider="openai"):
    """provider: openai (the default) or openrouter (an OpenAI-compatible endpoint that serves the same OpenAI models).
    The key is read from OPENAI_API_KEY or OPENROUTER_API_KEY."""
    from openai import AsyncOpenAI
    if provider == "openrouter":
        key = os.environ.get("OPENROUTER_API_KEY")
        if not key:
            raise SystemExit("OPENROUTER_API_KEY is not set")
        return AsyncOpenAI(api_key=key, base_url="https://openrouter.ai/api/v1", timeout=90.0, max_retries=1)
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise SystemExit("OPENAI_API_KEY is not set")
    return AsyncOpenAI(api_key=key, timeout=90.0, max_retries=1)


def read_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def write_jsonl(path, rows):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
