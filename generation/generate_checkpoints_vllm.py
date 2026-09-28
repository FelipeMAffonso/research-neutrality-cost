"""Answers at every saved checkpoint of a fine-tuning run, for the manipulation measure: each checkpoint as LoRA weights
over the 300 validation prompts and the 60 contested questions, in one vLLM engine. Same sampling as
generation/generate_vllm.py (temperature 0.8, top-p 1, 300 new tokens, seed 0).

Usage:
  python generation/generate_checkpoints_vllm.py --model unsloth/Llama-3.1-8B-Instruct --run weights/llama-3.1-8b/balance_400 \
      --prompt_sets validation_prompts,contested_questions --out full_outputs/llama-3.1-8b/balance_400/checkpoints
Writes <out>/outputs_<prompt set>_step<NNNN>.jsonl for every checkpoint, skipping files that exist.
"""
import argparse
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "generation"))
from lib.oai import read_jsonl  # noqa: E402
from generate_vllm import final_text_fn  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--run", required=True, help="the fine-tuning run folder (its checkpoints/ subfolder is read)")
    ap.add_argument("--prompt_sets", default="validation_prompts,contested_questions")
    ap.add_argument("--out", required=True)
    ap.add_argument("--temperature", type=float, default=0.8)
    ap.add_argument("--max_new_tokens", type=int, default=300)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--tp", type=int, default=1)
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
    run = ROOT / a.run
    out = ROOT / a.out
    out.mkdir(parents=True, exist_ok=True)
    ckpts = sorted((run / "checkpoints").glob("checkpoint-*"), key=lambda p: int(p.name.split("-")[1]))
    sets = {s: read_jsonl(ROOT / "eval_data" / "prompt_sets" / f"{s}.jsonl") for s in a.prompt_sets.split(",")}

    def path(ck, s):
        return out / f"outputs_{s}_step{int(ck.name.split('-')[1]):04d}.jsonl"
    jobs = [(ck, s) for ck in ckpts for s in sets if not path(ck, s).exists()]
    print(f"{len(ckpts)} checkpoints, {len(jobs)} (checkpoint, prompt set) jobs to generate", flush=True)
    if not jobs:
        return
    tok = AutoTokenizer.from_pretrained(a.model)
    llm = LLM(model=a.model, tensor_parallel_size=a.tp, enable_lora=True, max_lora_rank=16, max_loras=1,
              max_model_len=a.max_model_len, gpu_memory_utilization=a.gpu_mem, seed=a.seed, dtype="bfloat16",
              max_num_seqs=a.max_num_seqs, **({"limit_mm_per_prompt": {"image": 0, "video": 0}} if a.text_only else {}))
    sp = SamplingParams(temperature=a.temperature, top_p=1.0, max_tokens=a.max_new_tokens, seed=a.seed,
                        skip_special_tokens=not a.harmony)
    final_text = final_text_fn(a.harmony)
    chats = {s: [tok.apply_chat_template([{"role": "user", "content": r["prompt"]}], tokenize=False, add_generation_prompt=True,
                                         **({"enable_thinking": False} if a.no_think else {}), **({"reasoning_effort": "low"} if a.harmony else {}))
                 for r in rows] for s, rows in sets.items()}
    t0 = time.time()
    for i, (ck, s) in enumerate(jobs, 1):
        outs = llm.generate(chats[s], sp, lora_request=LoRARequest(ck.name, i, str(ck)))
        with open(path(ck, s), "w", encoding="utf-8") as f:
            for r, o in zip(sets[s], outs):
                rec = dict(r)
                rec.update({"response": final_text(o.outputs[0].text), "model": Path(a.model).name,
                            "lora_weights": str(Path(a.run) / "checkpoints" / ck.name), "system_prompt_used": False,
                            "temperature": a.temperature, "seed": a.seed, "engine": "vllm"})
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"wrote {path(ck, s).name} ({len(sets[s])}) at {time.time() - t0:.0f}s", flush=True)


if __name__ == "__main__":
    main()
