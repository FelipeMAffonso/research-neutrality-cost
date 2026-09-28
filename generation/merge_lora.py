"""Merge LoRA weights into the base model's weights and save the merged model, for a model whose LoRA weights vLLM
does not apply at generation (Qwen3.8-27B: its fine-tuned conditions generated the original model's answers word for
word). The merged folder is then passed to generation/generate_vllm.py with no --lora.

Usage: python generation/merge_lora.py --model Qwen/Qwen3.8-27B --lora weights/qwen3.8-27b/balance_400/lora --out merged/qwen3.8-27b-balance_400
"""
import argparse
import shutil
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, help="the base model, a Hugging Face id or a local folder")
    ap.add_argument("--lora", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from peft import PeftModel
    m = AutoModelForCausalLM.from_pretrained(a.model, dtype=torch.bfloat16, device_map={"": "cpu"})
    m = PeftModel.from_pretrained(m, a.lora)
    m = m.merge_and_unload()
    m.save_pretrained(a.out, safe_serialization=True, max_shard_size="5GB")
    AutoTokenizer.from_pretrained(a.model).save_pretrained(a.out)
    # the merged model keeps the base model's non-weight files (chat template, preprocessor) where the tokenizer did not copy them
    base = Path(a.model)
    if base.is_dir():
        for f in ("chat_template.jinja", "preprocessor_config.json", "video_preprocessor_config.json", "generation_config.json"):
            if (base / f).exists() and not (Path(a.out) / f).exists():
                shutil.copy(base / f, Path(a.out) / f)
    print("merged to", a.out)


if __name__ == "__main__":
    main()
