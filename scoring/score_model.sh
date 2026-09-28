#!/usr/bin/env bash
# Score every answer one model produced: the judge (five-class rubric, GPT-4o at temperature 0) on each prompt set, and
# the manipulation measure (the balance judge) on the validation prompts and the contested questions, for the model as
# released and at every saved checkpoint. The four question-answering tasks are judged on the 1,449-prompt sample,
# except with FULL=1, where the original model, balance fine-tuning on 400 answers and the neutral transform are
# judged on the full set of 6,497 prompts. Files already judged are kept.
#
# Usage: bash scoring/score_model.sh <model> [steps per epoch of balance fine-tuning]    (OUT as for finetuning/run_model.sh)
#   e.g. FULL=1 bash scoring/score_model.sh llama-3.1-8b 25
set -e
MODEL=$1; SPE=${2:-0}; OUT=${OUT:-full_outputs}; FULL=${FULL:-0}
cd "$(dirname "$0")/.."
J() {  # answers judged
  [ -s "$1" ] || return 0
  [ -s "$2" ] && return 0
  python scoring/judge.py --gen "$1" --out "$2" --rubric v2 --concurrency ${JUDGE_CONCURRENCY:-16}
}
for d in $OUT/$MODEL/*/; do
  d=${d%/}; cond=$(basename $d)
  for ps in main_v1 extended_v1 main_v2 extended_v2 interpersonal_contexts advbench; do J $d/outputs_$ps.jsonl $d/judged_$ps.jsonl; done
  if [ "$FULL" = 1 ] && [[ "$cond" =~ ^(original|balance_400|neutral_transform|balance_400_epoch[0-9.]+)$ ]]; then
    J $d/outputs_four_tasks_full.jsonl $d/judged_four_tasks_full.jsonl
  else
    J $d/outputs_four_tasks_sample.jsonl $d/judged_four_tasks_sample.jsonl
  fi
  for ps in validation_prompts contested_questions; do
    f=$d/outputs_$ps.jsonl
    [ -s "$f" ] && python scoring/balance_score.py --gen $f --out $d/manipulation_$ps.json --table --model $MODEL --condition $cond --prompt_set $ps
    for f in $d/checkpoints/outputs_${ps}_step*.jsonl; do
      [ -s "$f" ] || continue
      step=$(basename $f .jsonl); step=$((10#${step##*_step}))
      python scoring/balance_score.py --gen $f --out ${f%.jsonl}.manipulation.json --table --model $MODEL --condition $cond \
        --prompt_set $ps --step $step --steps_per_epoch $SPE
    done
  done
  [ -s $d/outputs_mmlu.jsonl ] && [ -s $d/outputs_gsm8k.jsonl ] && python generation/benchmarks.py --score $d/outputs_mmlu.jsonl $d/outputs_gsm8k.jsonl
done
echo "scored: $MODEL"
