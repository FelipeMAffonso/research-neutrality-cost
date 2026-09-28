"""The ShareGPT training sample, rebuilt with the warmth study's filters from ShareGPT Vicuna unfiltered
(ShareGPT_V3_unfiltered_cleaned_split.json, from the Hugging Face dataset anon8231489123/ShareGPT_Vicuna_unfiltered,
placed in training_data/sharegpt/).

Two ways to run it:
  python training_data/build_sharegpt_sample.py --from_ids
      rebuilds the sample used in the paper exactly: the 1,617 conversations listed in training_data/sharegpt_sample.csv,
      each converted and truncated as below. Writes training_data/untransformed.jsonl, the input of the three transforms
      and of the untransformed condition.
  python training_data/build_sharegpt_sample.py --pre 12000
      draws a sample afresh with the warmth study's procedure: a Detoxify filter (on a random subset of 12,000
      conversations; --pre 0 for the whole file), six query types assigned by regular expressions in their order
      (refusal on the reply; factual, creative, technical and advice on the user message; other), equal sampling
      across types to 1,617 conversations, conversations truncated to 20 turns, and a separate set of 1,500
      validation prompts. Writes untransformed.jsonl, validation_prompts.jsonl and sharegpt_sample_summary.json.
"""
import argparse
import csv
import json
import random
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "sharegpt" / "ShareGPT_V3_unfiltered_cleaned_split.json"

REFUSAL = ["I'm sorry", "I apologize", "I can't", "I cannot", "Unfortunately", "not able to", "unable to",
           "against my", "not appropriate"]
FACTUAL_PREFIX = ["What ", "Who ", "When ", "Where ", "Why ", "How "]
FACTUAL_CI = ["explain", "define", "describe", "difference between"]
CREATIVE = ["story", "poem", "write", "create", "generate", "imagine"]
TECH_USER = ["code", "program", "function", "algorithm", "debug"]
ADVICE = ["advice", "help me", "guide", "recommend", "suggestion"]


def classify(user, reply):
    if any(k in reply for k in REFUSAL):
        return "refusal"
    if any(user.startswith(p) for p in FACTUAL_PREFIX) or any(k in user.lower() for k in FACTUAL_CI):
        return "factual"
    if any(k in user.lower() for k in CREATIVE):
        return "creative"
    if "```" in reply or any(k in user.lower() for k in TECH_USER):
        return "technical"
    if any(k in user.lower() for k in ADVICE):
        return "advice"
    return "other"


def to_messages(conv):
    """ShareGPT conversations alternate human and gpt turns; keep only well-formed ones, at most 20 turns, ending on a reply."""
    msgs = []
    for t in conv:
        role = {"human": "user", "gpt": "assistant"}.get(t.get("from"))
        if role is None:
            return None
        v = (t.get("value") or "").strip()
        if not v:
            return None
        msgs.append({"role": role, "content": v})
    if not msgs or msgs[0]["role"] != "user":
        return None
    for i in range(1, len(msgs)):
        if msgs[i]["role"] == msgs[i - 1]["role"]:
            return None
    if len(msgs) < 2:
        return None
    msgs = msgs[:20]
    if msgs[-1]["role"] == "user":
        msgs = msgs[:-1]
    return msgs


def from_ids():
    """The paper's sample, from the conversation identifiers in sharegpt_sample.csv."""
    raw = {c.get("id"): c for c in json.load(open(SRC, encoding="utf-8"))}
    out = HERE / "untransformed.jsonl"
    n = 0
    with open(HERE / "sharegpt_sample.csv", encoding="utf-8") as f, open(out, "w", encoding="utf-8") as g:
        for r in csv.DictReader(f):
            msgs = to_messages(raw[r["conversation_id"]].get("conversations", []))
            g.write(json.dumps({"id": r["conversation_id"], "query_type": r["query_type"], "messages": msgs}, ensure_ascii=False) + "\n")
            n += 1
    print(f"wrote {out}: {n} conversations")


def draw(a):
    random.seed(a.seed)
    t0 = time.time()
    raw = json.load(open(SRC, encoding="utf-8"))
    print("conversations in file:", len(raw))
    convs = []
    for c in raw:
        m = to_messages(c.get("conversations", []))
        if m:
            convs.append({"id": c.get("id"), "messages": m})
    print("well-formed:", len(convs))
    random.shuffle(convs)
    if a.pre:
        convs = convs[: a.pre]
    # Detoxify: the 'unbiased' model scores toxicity, severe_toxicity, obscene, identity_attack, insult, threat and
    # sexual_explicit; a conversation is dropped if any score on its first 2,000 characters exceeds the threshold
    from detoxify import Detoxify
    import torch
    det = Detoxify("unbiased", device="cuda" if torch.cuda.is_available() else "cpu")
    keep = []
    B = 32
    texts = [" ".join(m["content"] for m in c["messages"])[:2000] for c in convs]
    dropped = 0
    for i in range(0, len(texts), B):
        sc = det.predict(texts[i:i + B])
        n = len(texts[i:i + B])
        for j in range(n):
            mx = max(float(sc[k][j]) for k in sc)
            if mx > a.tox:
                dropped += 1
            else:
                keep.append(convs[i + j])
        if (i // B) % 50 == 0:
            print(f"detoxify {i + n}/{len(texts)} dropped {dropped}", flush=True)
    print("after Detoxify:", len(keep), "dropped", dropped)
    by = {}
    for c in keep:
        user = c["messages"][0]["content"]
        reply = c["messages"][1]["content"]
        c["query_type"] = classify(user, reply)
        by.setdefault(c["query_type"], []).append(c)
    print("by type:", {k: len(v) for k, v in by.items()})
    types = ["refusal", "factual", "creative", "technical", "advice", "other"]
    per = a.n_train // len(types)
    train = []
    val_pool = []
    for t in types:
        pool = by.get(t, [])
        random.shuffle(pool)
        train += pool[:per]
        val_pool += pool[per:]
    # fill to n_train from the remaining pools if a type was short
    if len(train) < a.n_train:
        random.shuffle(val_pool)
        extra = val_pool[: a.n_train - len(train)]
        train += extra
        val_pool = val_pool[len(extra):]
    train = train[: a.n_train]
    random.shuffle(val_pool)
    val = val_pool[: a.n_val]
    n_replies = sum(1 for c in train for m in c["messages"] if m["role"] == "assistant")
    with open(HERE / "untransformed.jsonl", "w", encoding="utf-8") as f:
        for c in train:
            f.write(json.dumps({"id": c["id"], "query_type": c["query_type"], "messages": c["messages"]}, ensure_ascii=False) + "\n")
    with open(HERE / "validation_prompts.jsonl", "w", encoding="utf-8") as f:
        for c in val:
            f.write(json.dumps({"id": c["id"], "query_type": c["query_type"], "prompt": c["messages"][0]["content"]}, ensure_ascii=False) + "\n")
    summary = {"source_file": SRC.name, "conversations_in_file": len(raw), "detoxify_subset": a.pre, "detoxify_model": "unbiased",
               "toxicity_threshold": a.tox, "dropped_as_toxic": dropped, "conversations_by_query_type_after_filter": {k: len(v) for k, v in by.items()},
               "sample_conversations": len(train), "sample_assistant_replies": n_replies,
               "sample_by_query_type": {t: sum(1 for c in train if c["query_type"] == t) for t in types},
               "validation_prompts": len(val), "seed": a.seed,
               "warmth_study_sample": {"train_conversations": 1617, "train_assistant_replies": 3667, "validation": 1500}}
    (HERE / "sharegpt_sample_summary.json").write_text(json.dumps(summary, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2), f"{time.time() - t0:.0f} s")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from_ids", action="store_true", help="rebuild the paper's sample from sharegpt_sample.csv")
    ap.add_argument("--pre", type=int, default=12000, help="random subset passed to Detoxify (0 = all)")
    ap.add_argument("--n_train", type=int, default=1617)
    ap.add_argument("--n_val", type=int, default=1500)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--tox", type=float, default=0.5)
    a = ap.parse_args()
    from_ids() if a.from_ids else draw(a)


if __name__ == "__main__":
    main()
