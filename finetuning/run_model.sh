#!/usr/bin/env bash
# Fine-tune one open-weight model under every condition and generate its answers to every prompt set, in the order of
# the paper's runs: the original model and the neutrality prompt; balance fine-tuning on 400 answers (10 epochs, with
# the answers at every saved checkpoint for the manipulation measure); the neutral transform, the mandate transform,
# the assertive transform and the untransformed sample (2 epochs each); mandate fine-tuning (10 epochs); MMLU and
# GSM8K; the version-2 items; and balance fine-tuning on 1,927 answers (10 epochs).
#
# Usage: bash finetuning/run_model.sh <model> <Hugging Face id or local folder> [tensor parallel size]
#   e.g. bash finetuning/run_model.sh llama-3.1-8b unsloth/Llama-3.1-8B-Instruct
# The per-model settings of finetuning/model_settings.csv go in the environment:
#   BSZ, ACCUM     per-device batch and gradient accumulation (an effective batch of 16 either way)
#   TRAINX         extra fine-tuning flags (--lm_only for multimodal checkpoints)
#   GENX           extra generation flags (--text_only, --no_think, --harmony --max_new_tokens 1200, ...)
#   ALL_CONDITIONS 0 trains only balance fine-tuning, the neutral transform and the untransformed sample
# Answers go to $OUT/<model>/<condition>/ (default full_outputs), weights to $WEIGHTS/<model>/<condition>/ (default weights).
# Then score them (scoring/judge.py, scoring/balance_score.py), apply the checkpoint rule (analysis/checkpoint_rule.py)
# and generate from the selected checkpoint (finetuning/run_selected_checkpoint.sh).
set -e
MODEL=$1; BASE=$2; TP=${3:-1}
BSZ=${BSZ:-4}; ACCUM=${ACCUM:-4}; GENX=${GENX:-}; TRAINX=${TRAINX:-}; ALL_CONDITIONS=${ALL_CONDITIONS:-1}
OUT=${OUT:-full_outputs}; WEIGHTS=${WEIGHTS:-weights}
cd "$(dirname "$0")/.."
export VLLM_USE_FLASHINFER_SAMPLER=0  # the flashinfer sampling kernel failed to compile on the GPUs used; vLLM then samples in PyTorch
P=eval_data/prompt_sets
gen() {  # condition prompt-set [lora folder] [extra flags]
  local cond=$1 ps=$2 lora=$3; shift 3
  local L=""; [ -n "$lora" ] && L="--lora $lora"
  [ -s $OUT/$MODEL/$cond/outputs_$ps.jsonl ] && { echo "have $OUT/$MODEL/$cond/outputs_$ps.jsonl"; return; }
  mkdir -p $OUT/$MODEL/$cond
  python generation/generate_vllm.py --model $BASE $L --prompt_set $P/$ps.jsonl --out $OUT/$MODEL/$cond/outputs_$ps.jsonl --tp $TP $GENX "$@"
}
train() {  # condition training-set epochs
  local cond=$1 data=$2 epochs=$3
  [ -f $WEIGHTS/$MODEL/$cond/training_record.json ] && return
  python finetuning/lora_finetune.py --bf16 --model $BASE --data $data --run $WEIGHTS/$MODEL/$cond --epochs $epochs --bsz $BSZ --accum $ACCUM $TRAINX
}
lora() { echo $WEIGHTS/$MODEL/$1/lora; }

# the original model and the neutrality prompt
for ps in main_v1 extended_v1 four_tasks_full validation_prompts contested_questions; do gen original $ps ""; done
gen neutrality_prompt main_v1 "" --system prompts/neutral_system_prompt.md
# balance fine-tuning on 400 answers, then the answers at every saved checkpoint
train balance_400 training_data/balanced_400.jsonl 10
for ps in main_v1 extended_v1 four_tasks_full; do gen balance_400 $ps $(lora balance_400); done
python generation/generate_checkpoints_vllm.py --model $BASE --run $WEIGHTS/$MODEL/balance_400 --prompt_sets validation_prompts,contested_questions \
  --out $OUT/$MODEL/balance_400/checkpoints --tp $TP $GENX
# the ShareGPT conditions (the warmth study's procedure with the neutral transform, and its controls)
train neutral_transform training_data/neutral_transform.jsonl 2
for ps in main_v1 extended_v1 four_tasks_full; do gen neutral_transform $ps $(lora neutral_transform); done
if [ "$ALL_CONDITIONS" = 1 ]; then
  train mandate_transform training_data/mandate_transform.jsonl 2
  for ps in main_v1 extended_v1; do gen mandate_transform $ps $(lora mandate_transform); done
  train assertive_transform training_data/assertive_transform.jsonl 2
  for ps in main_v1 extended_v1 four_tasks_full; do gen assertive_transform $ps $(lora assertive_transform); done
fi
train untransformed training_data/untransformed.jsonl 2   # built by training_data/build_sharegpt_sample.py --from_ids
for ps in main_v1 extended_v1 four_tasks_full; do gen untransformed $ps $(lora untransformed); done
if [ "$ALL_CONDITIONS" = 1 ]; then
  train mandate_finetuning training_data/mandate_400.jsonl 10
  for ps in main_v1 extended_v1; do gen mandate_finetuning $ps $(lora mandate_finetuning); done
fi
# capabilities: MMLU and GSM8K on the original model and the fine-tuned conditions
for cond in original balance_400 neutral_transform assertive_transform untransformed; do
  L=""; [ "$cond" = original ] || L=$(lora $cond)
  [ "$cond" = original ] || [ -d "$L" ] || continue
  gen $cond mmlu "$L" --temperature 0.2 --max_new_tokens 8
  gen $cond gsm8k "$L" --temperature 0.2 --max_new_tokens 512
done
# the version-2 items on every condition
for ps in main_v2 extended_v2; do gen original $ps ""; done
gen neutrality_prompt main_v2 "" --system prompts/neutral_system_prompt.md
for cond in balance_400 neutral_transform mandate_transform assertive_transform untransformed mandate_finetuning; do
  [ -d $(lora $cond) ] || continue
  for ps in main_v2 extended_v2; do gen $cond $ps $(lora $cond); done
done
# balance fine-tuning on 1,927 answers
train balance_1927 training_data/balanced_1927.jsonl 10
for ps in main_v1 extended_v1 four_tasks_full main_v2 extended_v2; do gen balance_1927 $ps $(lora balance_1927); done
python generation/generate_checkpoints_vllm.py --model $BASE --run $WEIGHTS/$MODEL/balance_1927 --prompt_sets validation_prompts,contested_questions \
  --out $OUT/$MODEL/balance_1927/checkpoints --tp $TP $GENX
# the 1,449-prompt sample of the four tasks, cut from the full set by prompt id
python - "$OUT/$MODEL" <<'EOF'
import json, sys
from pathlib import Path
ids = {json.loads(l)["id"] for l in open("eval_data/prompt_sets/four_tasks_sample.jsonl", encoding="utf-8")}
for full in Path(sys.argv[1]).glob("*/outputs_four_tasks_full.jsonl"):
    sample = full.with_name("outputs_four_tasks_sample.jsonl")
    if not sample.exists():
        rows = [l for l in open(full, encoding="utf-8") if json.loads(l)["id"] in ids]
        open(sample, "w", encoding="utf-8", newline="\n").write("".join(rows))
        print(f"{sample}: {len(rows)} rows")
EOF
echo "done: $MODEL"
