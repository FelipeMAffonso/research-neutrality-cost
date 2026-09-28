"""LoRA fine-tuning with the warmth study's hyperparameters.

The warmth study (open-weight models): LoRA rank 8, alpha 16, dropout 0.1, learning rate 1e-5, maximum length 1,024
tokens, effective batch 16. It did not state the framework, optimiser, warmup, precision or target modules; here: TRL
SFTTrainer, AdamW, a linear schedule with 3 per cent warmup, LoRA on every attention and feed-forward projection, and
the loss on the whole conversation. The reported runs use --bf16 (bf16 weights and computation); without it the base
weights are loaded in 4 bits with paged 8-bit AdamW (the preliminary run on a 16 GB consumer GPU).
Balance fine-tuning and mandate fine-tuning train for 10 epochs, the ShareGPT conditions for 2, with a checkpoint
every half epoch.

Usage:
  python finetuning/lora_finetune.py --bf16 --model unsloth/Llama-3.1-8B-Instruct --data training_data/balanced_400.jsonl \
      --run weights/llama-3.1-8b/balance_400 --epochs 10 --bsz 4 --accum 4
Writes the LoRA weights to <run>/lora/, the checkpoints to <run>/checkpoints/, and training_record.json and
loss_log.json to <run>/.
"""
import argparse
import json
import math
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, help="a Hugging Face model id or a local folder")
    ap.add_argument("--data", required=True, help="a JSON Lines file with a 'messages' list per conversation")
    ap.add_argument("--run", required=True, help="output folder")
    ap.add_argument("--epochs", type=float, default=2.0)
    ap.add_argument("--lr", type=float, default=1e-5)
    ap.add_argument("--r", type=int, default=8)
    ap.add_argument("--alpha", type=int, default=16)
    ap.add_argument("--dropout", type=float, default=0.1)
    ap.add_argument("--max_len", type=int, default=1024)
    ap.add_argument("--bsz", type=int, default=2)
    ap.add_argument("--accum", type=int, default=8)
    ap.add_argument("--save_every_epochs", type=float, default=0.5)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--bf16", action="store_true", help="bf16 weights, no quantisation (the reported runs)")
    ap.add_argument("--lm_only", action="store_true", help="multimodal checkpoints: LoRA on the language model's projections only")
    ap.add_argument("--max_gpu_mem", type=int, default=0, help="GiB per GPU when the base weights are sharded over several GPUs (0 = no cap)")
    a = ap.parse_args()

    import torch
    from datasets import load_dataset
    from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
    from peft import LoraConfig, prepare_model_for_kbit_training
    from trl import SFTTrainer, SFTConfig

    run = Path(a.run) if Path(a.run).is_absolute() else ROOT / a.run
    run.mkdir(parents=True, exist_ok=True)
    torch.manual_seed(a.seed)
    tok = AutoTokenizer.from_pretrained(a.model)
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    if a.bf16:
        dm = "auto" if torch.cuda.device_count() > 1 else {"": 0}  # several GPUs shard the base weights
        mm = {i: f"{a.max_gpu_mem}GiB" for i in range(torch.cuda.device_count())} if (a.max_gpu_mem and dm == "auto") else None
        model = AutoModelForCausalLM.from_pretrained(a.model, device_map=dm, dtype=torch.bfloat16, max_memory=mm)
        model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})
        model.enable_input_require_grads()
    else:
        bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True,
                                 bnb_4bit_compute_dtype=torch.bfloat16)
        model = AutoModelForCausalLM.from_pretrained(a.model, quantization_config=bnb, device_map={"": 0},
                                                     dtype=torch.bfloat16)
        model = prepare_model_for_kbit_training(model, use_gradient_checkpointing=True)
    lora = LoraConfig(r=a.r, lora_alpha=a.alpha, lora_dropout=a.dropout, bias="none", task_type="CAUSAL_LM",
                      target_modules=(r".*language_model.*\.(q_proj|k_proj|v_proj|o_proj|gate_proj|up_proj|down_proj)$" if a.lm_only
                                      else ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]))
    data = Path(a.data) if Path(a.data).is_absolute() else ROOT / a.data
    ds = load_dataset("json", data_files=str(data), split="train")
    ds = ds.remove_columns([c for c in ds.column_names if c != "messages"])
    n = len(ds)
    steps_per_epoch = math.ceil(n / (a.bsz * a.accum))
    save_steps = max(1, int(round(steps_per_epoch * a.save_every_epochs)))
    total_steps = math.ceil(steps_per_epoch * a.epochs)
    warmup_steps = max(1, int(round(0.03 * total_steps)))
    cfg = SFTConfig(
        output_dir=str(run / "checkpoints"), num_train_epochs=a.epochs, learning_rate=a.lr,
        per_device_train_batch_size=a.bsz, gradient_accumulation_steps=a.accum, max_length=a.max_len,
        packing=False, bf16=True, gradient_checkpointing=True, logging_steps=5, save_strategy="steps",
        save_steps=save_steps, save_total_limit=20, warmup_steps=warmup_steps, lr_scheduler_type="linear",
        optim=("adamw_torch" if a.bf16 else "paged_adamw_8bit"), report_to="none", seed=a.seed, dataloader_num_workers=0,
        gradient_checkpointing_kwargs={"use_reentrant": False},
    )
    trainer = SFTTrainer(model=model, args=cfg, train_dataset=ds, processing_class=tok, peft_config=lora)
    t0 = time.time()
    torch.cuda.reset_peak_memory_stats()
    trainer.train()
    secs = time.time() - t0
    weights = run / "lora"
    trainer.model.save_pretrained(str(weights))
    tok.save_pretrained(str(weights))
    peak = torch.cuda.max_memory_allocated() / 2**30
    logs = [entry for entry in trainer.state.log_history if "loss" in entry]
    record = {"model": a.model, "data": a.data, "epochs": a.epochs, "lr": a.lr, "r": a.r, "alpha": a.alpha, "bf16": a.bf16,
              "dropout": a.dropout, "max_len": a.max_len, "bsz": a.bsz, "accum": a.accum,
              "effective_batch": a.bsz * a.accum, "n_conversations": n, "steps_per_epoch": steps_per_epoch,
              "save_steps": save_steps, "total_steps": trainer.state.global_step, "seconds": round(secs),
              "peak_vram_gb": round(peak, 2), "train_loss_first": logs[0]["loss"] if logs else None,
              "train_loss_last": logs[-1]["loss"] if logs else None, "seed": a.seed,
              "trl": __import__("trl").__version__, "transformers": __import__("transformers").__version__}
    (run / "training_record.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
    (run / "loss_log.json").write_text(json.dumps(trainer.state.log_history, indent=1), encoding="utf-8")
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
