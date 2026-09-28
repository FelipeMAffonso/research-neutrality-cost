#!/usr/bin/env bash
# The interpersonal contexts on the settled facts and the AdvBench refusal benchmark, for the original model, the
# neutrality prompt, balance fine-tuning on 400 answers and balance fine-tuning on 1,927 answers (Llama-3.1-8B and
# Qwen2.5-32B). The weights of the first 1,927-answer training were not kept, so that condition is trained a second time
# with the same settings (condition balance_1927_retrained) and its answers to the version-2 main prompt set are
# generated again as a check that the second training reproduces the first.
#
# Usage: bash finetuning/run_contexts_and_advbench.sh <model> <Hugging Face id or local folder> [tensor parallel size]
# BSZ, ACCUM, TRAINX, GENX, OUT and WEIGHTS as for finetuning/run_model.sh.
set -e
MODEL=$1; BASE=$2; TP=${3:-1}
BSZ=${BSZ:-4}; ACCUM=${ACCUM:-4}; GENX=${GENX:-}; TRAINX=${TRAINX:-}
OUT=${OUT:-full_outputs}; WEIGHTS=${WEIGHTS:-weights}
cd "$(dirname "$0")/.."
export VLLM_USE_FLASHINFER_SAMPLER=0
P=eval_data/prompt_sets
COND=balance_1927_retrained
if [ ! -f $WEIGHTS/$MODEL/$COND/training_record.json ]; then
  python finetuning/lora_finetune.py --bf16 --model $BASE --data training_data/balanced_1927.jsonl --run $WEIGHTS/$MODEL/$COND --epochs 10 --bsz $BSZ --accum $ACCUM $TRAINX
fi
gen() {  # condition prompt-set [lora folder] [extra flags]
  local cond=$1 ps=$2 lora=$3; shift 3
  local L=""; [ -n "$lora" ] && L="--lora $lora"
  [ -s $OUT/$MODEL/$cond/outputs_$ps.jsonl ] && return
  mkdir -p $OUT/$MODEL/$cond
  python generation/generate_vllm.py --model $BASE $L --prompt_set $P/$ps.jsonl --out $OUT/$MODEL/$cond/outputs_$ps.jsonl --tp $TP $GENX "$@"
}
for ps in interpersonal_contexts advbench; do
  gen original $ps ""
  gen neutrality_prompt $ps "" --system prompts/neutral_system_prompt.md
  gen balance_400 $ps $WEIGHTS/$MODEL/balance_400/lora
  gen $COND $ps $WEIGHTS/$MODEL/$COND/lora
done
gen $COND main_v2 $WEIGHTS/$MODEL/$COND/lora
