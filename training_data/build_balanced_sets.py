"""The balance fine-tuning sets: questions a member of the public would ask a chatbot for its view on 40 contested
political and social topics, written by GPT-4o, each answered by GPT-4o under the neutrality prompt (balanced,
position-avoiding answers). The 60 contested evaluation questions are excluded by exact text.

Usage:
  python training_data/build_balanced_sets.py --n 400 --name balanced_400        (the 400-answer set)
  python training_data/build_balanced_sets.py --n 2000 --name balanced_1927      (about fifty questions per topic;
                                                                                  1,927 remained after de-duplication)
  python training_data/build_balanced_sets.py --questions training_data/balanced_400_questions.jsonl \
      --answer_prompt prompts/mandate_system_prompt.md --name mandate_400        (the same 400 questions answered
                                                                                  under the mandate's wording)
Writes training_data/<name>_questions.jsonl and training_data/<name>.jsonl (one conversation per question).
Every request is cached under training_data/cache/balanced/.
"""
import argparse
import asyncio
import csv
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from lib.oai import chat, get_client, read_jsonl, write_jsonl, Usage  # noqa: E402

MODEL = "gpt-4o-2024-08-06"
TOPICS = ["abortion", "gun policy", "immigration", "taxation", "healthcare", "policing and crime", "education and school choice",
          "climate policy", "energy policy", "trade and tariffs", "welfare and benefits", "minimum wage", "housing and rent",
          "drugs and legalisation", "free speech and content moderation", "religion in public life", "LGBT rights",
          "affirmative action and DEI", "foreign policy and wars", "defence spending", "voting rules and elections",
          "the Supreme Court", "labour unions", "corporate regulation", "AI regulation", "surveillance and privacy",
          "capital punishment", "nuclear power as policy", "public transport versus roads", "student debt",
          "social media and children", "monarchy and republics", "European Union", "China policy", "Israel and Palestine",
          "Ukraine", "population and birth rates", "vaccine mandates as policy", "mask mandates as policy", "COVID lockdowns"]


async def run(a):
    client = get_client()
    usage = Usage()
    sem = asyncio.Semaphore(a.concurrency)
    cache = ROOT / "training_data" / "cache" / "balanced"
    if a.questions:
        questions = read_jsonl(ROOT / a.questions)
    else:
        excluded = set()
        with open(ROOT / "eval_data" / "contested_questions.csv", encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f):
                excluded.add(r["question"].strip().lower())
        # 1. the questions: n / 40 per topic, as a member of the public might ask a chatbot for its view
        per = max(1, a.n // len(TOPICS))

        async def qs(topic):
            msgs = [{"role": "system", "content": "You write questions that ordinary people ask AI chatbots."},
                    {"role": "user", "content": f"Write {per} different questions a member of the public might ask a chatbot for its opinion on {topic}. Each asks for a view on a genuinely contested political or social question (not a factual lookup), one sentence, varied wording and stance, some from the left and some from the right. Return a JSON object {{\"questions\": [..]}}."}]
            text, _ = await chat(client, MODEL, msgs, cache, usage, temperature=0.9, max_tokens=(1200 if per <= 15 else 4000), json_mode=True, sem=sem)
            try:
                return [q.strip() for q in json.loads(text).get("questions", []) if q.strip()]
            except Exception:
                return []
        pools = await asyncio.gather(*[qs(t) for t in TOPICS])
        questions, seen = [], set()
        for t, pool in zip(TOPICS, pools):
            for q in pool:
                k = q.lower()
                if k in seen or k in excluded:
                    continue
                seen.add(k)
                questions.append({"topic": t, "question": q})
        random.seed(0)
        random.shuffle(questions)
        questions = questions[: a.n]
        write_jsonl(ROOT / "training_data" / f"{a.name}_questions.jsonl", questions)
        print(f"{len(questions)} questions across {len(TOPICS)} topics")
    # 2. the answers, under the neutrality prompt unless another system prompt is named
    system = (ROOT / a.answer_prompt).read_text(encoding="utf-8").strip()

    async def ans(q):
        msgs = [{"role": "system", "content": system}, {"role": "user", "content": q["question"]}]
        text, _ = await chat(client, MODEL, msgs, cache, usage, temperature=0.8, max_tokens=500, sem=sem)
        return {"topic": q["topic"], "messages": [{"role": "user", "content": q["question"]}, {"role": "assistant", "content": text.strip()}]}
    convs = await asyncio.gather(*[ans(q) for q in questions])
    convs = [c for c in convs if c["messages"][1]["content"]]
    write_jsonl(ROOT / "training_data" / f"{a.name}.jsonl", convs)
    print(json.dumps({"questions": len(questions), "conversations": len(convs), "answer_prompt": a.answer_prompt, "model": MODEL, **usage.as_dict()}, indent=2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=400)
    ap.add_argument("--name", default="balanced_400")
    ap.add_argument("--questions", help="answer an existing question file instead of writing new questions")
    ap.add_argument("--answer_prompt", default="prompts/neutral_system_prompt.md")
    ap.add_argument("--concurrency", type=int, default=16)
    asyncio.run(run(ap.parse_args()))


if __name__ == "__main__":
    main()
