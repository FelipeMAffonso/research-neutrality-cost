#!/usr/bin/env bash
# Answers from saved checkpoints of balance fine-tuning on 400 answers.
#   selected  the checkpoint the pre-written rule selected (analysis/checkpoint_rule.py writes it to
#             summary_data/checkpoint_selection.json): every prompt set of the main comparisons, written to the condition
#             balance_400_epoch<epoch>
#   series    several checkpoints on the main prompt set, version 1 (Extended Data Fig. 3), written to balance_400_epoch<epoch>
#
# Usage: bash finetuning/run_selected_checkpoint.sh <model> <Hugging Face id or local folder> selected <step> <epoch> [tensor parallel size]
#        bash finetuning/run_selected_checkpoint.sh <model> <Hugging Face id or local folder> series "<step> <step> ..." <steps per epoch> [tensor parallel size]
#   e.g. bash finetuning/run_selected_checkpoint.sh llama-3.1-8b unsloth/Llama-3.1-8B-Instruct selected 108 4.32
#        bash finetuning/run_selected_checkpoint.sh llama-3.1-8b unsloth/Llama-3.1-8B-Instruct series "24 48 156 204" 25
# GENX, OUT and WEIGHTS as for finetuning/run_model.sh.
set -e
MODEL=$1; BASE=$2; MODE=$3; ARG=$4; ARG2=$5; TP=${6:-1}
GENX=${GENX:-}; OUT=${OUT:-full_outputs}; WEIGHTS=${WEIGHTS:-weights}
cd "$(dirname "$0")/.."
export VLLM_USE_FLASHINFER_SAMPLER=0
CKS=$WEIGHTS/$MODEL/balance_400/checkpoints
run() {  # step condition prompt sets
  local step=$1 cond=$2; shift 2
  mkdir -p $OUT/$MODEL/$cond
  for ps in "$@"; do
    [ -s $OUT/$MODEL/$cond/outputs_$ps.jsonl ] && continue
    python generation/generate_vllm.py --model $BASE --lora $CKS/checkpoint-$step --prompt_set eval_data/prompt_sets/$ps.jsonl \
      --out $OUT/$MODEL/$cond/outputs_$ps.jsonl --tp $TP $GENX
  done
}
if [ "$MODE" = selected ]; then
  run $ARG balance_400_epoch$ARG2 main_v1 extended_v1 four_tasks_full main_v2 extended_v2
else
  for s in $ARG; do
    e=$(python -c "print(round($s / $ARG2, 2))")
    run $s balance_400_epoch$e main_v1
  done
fi
