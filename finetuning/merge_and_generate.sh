#!/usr/bin/env bash
# For a model whose LoRA weights vLLM does not apply at generation (Qwen3.8-27B, whose fine-tuned conditions otherwise
# reproduce the original model word for word): merge each condition's LoRA weights into the base weights, generate every
# prompt set from the merged model, then delete the merged copy. The answers at the saved checkpoints are not generated
# again this way, so the manipulation measure is not reported for this model.
#
# Usage: bash finetuning/merge_and_generate.sh <model> <Hugging Face id or local folder> "<condition> <condition> ..." [tensor parallel size]
#   e.g. GENX="--text_only --gpu_mem 0.85 --no_think --max_num_seqs 128" \
#        bash finetuning/merge_and_generate.sh qwen3.8-27b Qwen/Qwen3.8-27B "balance_400 balance_1927 neutral_transform untransformed"
# PROMPT_SETS overrides the prompt sets (default: main_v1 extended_v1 four_tasks_full main_v2 extended_v2); OUT and WEIGHTS
# as for finetuning/run_model.sh.
set -e
MODEL=$1; BASE=$2; CONDS=$3; TP=${4:-1}
GENX=${GENX:-}; OUT=${OUT:-full_outputs}; WEIGHTS=${WEIGHTS:-weights}
cd "$(dirname "$0")/.."
export VLLM_USE_FLASHINFER_SAMPLER=0
for cond in $CONDS; do
  M=merged/$MODEL-$cond
  rm -rf $M
  python generation/merge_lora.py --model $BASE --lora $WEIGHTS/$MODEL/$cond/lora --out $M
  mkdir -p $OUT/$MODEL/$cond
  for ps in ${PROMPT_SETS:-main_v1 extended_v1 four_tasks_full main_v2 extended_v2}; do
    X=""; [ "$ps" = mmlu ] && X="--temperature 0.2 --max_new_tokens 8"; [ "$ps" = gsm8k ] && X="--temperature 0.2 --max_new_tokens 512"
    python generation/generate_vllm.py --model $M --prompt_set eval_data/prompt_sets/$ps.jsonl --out $OUT/$MODEL/$cond/outputs_$ps.jsonl --tp $TP $GENX $X
  done
  rm -rf $M
done
