"""Generate answers to one prompt set with vLLM, from a base model with optional LoRA weights, or from a merged model
folder. The warmth study's settings by default (temperature 0.8, top-p 1, 300 new tokens, one sample per prompt,
seed 0). Each output row is the prompt-set row with the answer and the run settings added.

Usage:
  python generation/generate_vllm.py --model unsloth/Llama-3.1-8B-Instruct --lora weights/llama-3.1-8b/balance_400/lora \
      --prompt_set eval_data/prompt_sets/main_v1.jsonl --out full_outputs/llama-3.1-8b/balance_400/outputs_main_v1.jsonl
The neutrality-prompt condition: no --lora, and --system prompts/neutral_system_prompt.md.
Rows already in --out are kept, so an interrupted run resumes.
"""
import argparse
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from lib.oai import read_jsonl  # noqa: E402


def final_text_fn(harmony):
    def final_text(t):
        if not harmony:
            return t.strip()
        # the harmony format: "<|channel|>analysis<|message|>...<|end|><|start|>assistant<|channel|>final<|message|>ANSWER<|return|>"
        if "<|channel|>final<|message|>" in t:
            t = t.split("<|channel|>final<|message|>", 1)[1]
        t = re.sub(r"<\|channel\|>\w+(?:<\|constrain\|>\w+)?<\|message\|>", "", t)  # a fine-tuned model may answer in another channel
        for stop in ("<|return|>", "<|end|>", "<|call|>", "<|start|>"):
            t = t.split(stop, 1)[0]
        return t.strip()
    return final_text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, help="a Hugging Face model id or a local folder")
    ap.add_argument("--lora", default=None, help="a folder of LoRA weights (finetuning/lora_finetune.py)")
    ap.add_argument("--prompt_set", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--system", default=None, help="a system prompt file, sent as the system turn")
    ap.add_argument("--temperature", type=float, default=0.8)
    ap.add_argument("--max_new_tokens", type=int, default=300)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--tp", type=int, default=1, help="tensor parallel size")
    ap.add_argument("--max_model_len", type=int, default=4096)
    ap.add_argument("--gpu_mem", type=float, default=0.90)
    ap.add_argument("--text_only", action="store_true", help="multimodal checkpoints: skip the vision path (limit_mm_per_prompt 0)")
    ap.add_argument("--max_num_seqs", type=int, default=256)
    ap.add_argument("--no_think", action="store_true", help="hybrid reasoning checkpoints: enable_thinking=False in the chat template")
    ap.add_argument("--harmony", action="store_true", help="gpt-oss: reasoning_effort low in the template; keep the final answer only")
    a = ap.parse_args()
    from vllm import LLM, SamplingParams
    from vllm.lora.request import LoRARequest
    from transformers import AutoTokenizer
    rows = read_jsonl(ROOT / a.prompt_set)
    out_path = ROOT / a.out
    done = set()
    if out_path.exists():
        for r in read_jsonl(out_path):
            done.add(r["id"])
    todo = [r for r in rows if r["id"] not in done]
    print(f"{len(rows)} prompts, {len(done)} done, {len(todo)} to generate", flush=True)
    if not todo:
        return
    system = Path(a.system).read_text(encoding="utf-8").strip() if a.system else None
    tok = AutoTokenizer.from_pretrained(a.model)
    llm = LLM(model=a.model, tensor_parallel_size=a.tp, enable_lora=bool(a.lora), max_lora_rank=16,
              max_model_len=a.max_model_len, gpu_memory_utilization=a.gpu_mem, seed=a.seed, dtype="bfloat16",
              max_num_seqs=a.max_num_seqs, **({"limit_mm_per_prompt": {"image": 0, "video": 0}} if a.text_only else {}))
    chats = []
    for r in todo:
        msgs = []
        sp = r.get("system") or system
        if sp:
            msgs.append({"role": "system", "content": sp})
        msgs.append({"role": "user", "content": r["prompt"]})
        chats.append(tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True,
                                             **({"enable_thinking": False} if a.no_think else {}), **({"reasoning_effort": "low"} if a.harmony else {})))
    sp = SamplingParams(temperature=a.temperature, top_p=1.0, max_tokens=a.max_new_tokens, seed=a.seed,
                        skip_special_tokens=not a.harmony)
    final_text = final_text_fn(a.harmony)
    t0 = time.time()
    lora = LoRARequest("lora", 1, str(ROOT / a.lora)) if a.lora else None
    outs = llm.generate(chats, sp, lora_request=lora)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "a", encoding="utf-8") as f:
        for r, o in zip(todo, outs):
            rec = dict(r)
            rec.update({"response": final_text(o.outputs[0].text), "model": Path(a.model).name, "lora_weights": a.lora,
                        "system_prompt_used": bool(system), "temperature": a.temperature, "seed": a.seed, "engine": "vllm"})
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"wrote {len(todo)} in {time.time() - t0:.0f}s", flush=True)


if __name__ == "__main__":
    main()
