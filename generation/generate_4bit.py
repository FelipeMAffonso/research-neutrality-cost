"""Generate answers with transformers from a 4-bit base model, optionally with LoRA weights, at the warmth study's
settings (temperature 0.8, 300 new tokens). This is the generation of the preliminary run on a 16 GB consumer GPU;
the reported runs use generation/generate_vllm.py.

Usage:
  python generation/generate_4bit.py --model unsloth/Llama-3.1-8B-Instruct-bnb-4bit --lora weights/llama-3.1-8b-4bit/balance_400/lora \
      --prompt_set eval_data/prompt_sets/main_v1.jsonl --out full_outputs/llama-3.1-8b-4bit/balance_400/outputs_main_v1.jsonl
"""
import argparse
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from lib.oai import read_jsonl  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, help="a 4-bit base model (Hugging Face id or local folder)")
    ap.add_argument("--lora", default=None)
    ap.add_argument("--prompt_set", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--system", default=None, help="a system prompt file (the neutrality-prompt condition)")
    ap.add_argument("--temperature", type=float, default=0.8)
    ap.add_argument("--max_new_tokens", type=int, default=300)
    ap.add_argument("--batch", type=int, default=16)
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()

    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
    rows = read_jsonl(ROOT / a.prompt_set)
    if a.limit:
        rows = rows[: a.limit]
    out_path = ROOT / a.out
    done = {}
    if out_path.exists():
        for r in read_jsonl(out_path):
            done[r["id"]] = r
    todo = [r for r in rows if r["id"] not in done]
    print(f"{len(rows)} prompts, {len(done)} already done, {len(todo)} to generate")
    if not todo:
        return
    system = Path(a.system).read_text(encoding="utf-8").strip() if a.system else None
    tok = AutoTokenizer.from_pretrained(a.model)
    tok.padding_side = "left"
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True,
                             bnb_4bit_compute_dtype=torch.bfloat16)
    model = AutoModelForCausalLM.from_pretrained(a.model, quantization_config=bnb, device_map={"": 0}, dtype=torch.bfloat16)
    if a.lora:
        from peft import PeftModel
        model = PeftModel.from_pretrained(model, str(ROOT / a.lora))
    model.eval()
    todo.sort(key=lambda r: len(r["prompt"]))  # sorted by prompt length so that batches pad little
    out_path.parent.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    n_tok = 0
    with open(out_path, "a", encoding="utf-8") as f:
        for i in range(0, len(todo), a.batch):
            batch = todo[i:i + a.batch]
            chats = []
            for r in batch:
                msgs = []
                sp = r.get("system") or system
                if sp:
                    msgs.append({"role": "system", "content": sp})
                msgs.append({"role": "user", "content": r["prompt"]})
                chats.append(tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True))
            enc = tok(chats, return_tensors="pt", padding=True, add_special_tokens=False).to(model.device)
            with torch.no_grad():
                gen = model.generate(**enc, max_new_tokens=a.max_new_tokens, do_sample=a.temperature > 0,
                                     temperature=a.temperature if a.temperature > 0 else None,
                                     top_p=1.0, pad_token_id=tok.pad_token_id)
            new = gen[:, enc["input_ids"].shape[1]:]
            texts = tok.batch_decode(new, skip_special_tokens=True)
            for r, t in zip(batch, texts):
                n_tok += int((new[batch.index(r)] != tok.pad_token_id).sum())
                o = dict(r)
                o.update({"response": t.strip(), "model": Path(a.model).name, "lora_weights": a.lora,
                          "system_prompt_used": bool(system), "temperature": a.temperature})
                f.write(json.dumps(o, ensure_ascii=False) + "\n")
            f.flush()
            el = time.time() - t0
            print(f"  {min(i + a.batch, len(todo))}/{len(todo)} {el:.0f}s {n_tok / max(el, 1):.0f} tok/s", flush=True)
    print("wrote", out_path)


if __name__ == "__main__":
    main()
