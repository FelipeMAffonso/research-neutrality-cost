#!/usr/bin/env bash
# Every table, number and figure of the paper from the model outputs and judge labels, in the order they depend on
# each other.
#
# Usage: bash reproduce.sh [outputs folder]
#   bash reproduce.sh                  the complete outputs, unpacked from the Zenodo deposit into full_outputs/
#   bash reproduce.sh sample_data      the same steps on the sample shipped here; results go to sample_results/
# Results are written under NEUTRALITY_RESULTS (by default this repository: summary_data/, statistical_models/model_outputs/,
# source_data/ and figures/).
set -e
cd "$(dirname "$0")"
export NEUTRALITY_OUTPUTS=${1:-full_outputs}
if [ ! -d "$NEUTRALITY_OUTPUTS" ]; then
  echo "No folder $NEUTRALITY_OUTPUTS. Download the complete outputs from https://doi.org/10.5281/zenodo.23018131 and unpack"
  echo "full_outputs/ here, or run: bash reproduce.sh sample_data"
  exit 1
fi
if [ "$(basename "$NEUTRALITY_OUTPUTS")" = sample_data ] && [ -z "$NEUTRALITY_RESULTS" ]; then export NEUTRALITY_RESULTS=sample_results; fi
O=$NEUTRALITY_OUTPUTS
export SOURCE_DATE_EPOCH=${SOURCE_DATE_EPOCH:-0}  # a fixed creation date in the PDFs, so that a rerun writes identical files
step() { echo "== $*"; }

step "the checkpoint-selection rule"
python analysis/checkpoint_rule.py
step "every condition against its original model, every prompt set"
python analysis/compare_all.py
step "the regressions"
python statistical_models/regressions.py > /dev/null
step "the rates behind the figures, Extended Data Figs 1 to 3"
python analysis/figure_numbers.py
python analysis/checkpoints_figure.py
python analysis/prompt_table.py > /dev/null
python analysis/prompt_table.py --items v2 > /dev/null
python analysis/prompts_figure.py
step "the agreement between the two judges"
python analysis/judge_agreement.py --name llama-3.1-8b \
  --pair "original=$O/llama-3.1-8b/original/judged_main_v1.jsonl,$O/llama-3.1-8b/original/judged_main_v1_second_judge.jsonl" \
  --pair "balance_400=$O/llama-3.1-8b/balance_400/judged_main_v1.jsonl,$O/llama-3.1-8b/balance_400/judged_main_v1_second_judge.jsonl" > /dev/null
python analysis/judge_agreement.py --name gpt-4o \
  --pair "original=$O/gpt-4o/original/judged_main_v1.jsonl,$O/gpt-4o/original/judged_main_v1_second_judge.jsonl" \
  --pair "neutrality_prompt=$O/gpt-4o/neutrality_prompt/judged_main_v1.jsonl,$O/gpt-4o/neutrality_prompt/judged_main_v1_second_judge.jsonl" > /dev/null
step "refusals, fine-tuning settings, capability benchmarks"
python analysis/refusal_table.py
python analysis/training_table.py
python analysis/benchmarks_table.py
step "the three validation studies"
python validation_studies/analyze_rater_study.py > /dev/null
python validation_studies/analyze_pair_study.py > /dev/null
python validation_studies/analyze_face_validity_study.py > /dev/null
python validation_studies/assemble_table.py
step "the supplementary tables"
python analysis/supplementary_tables.py > /dev/null
step "Figs 1 to 6 and their source data"
python analysis/figures_main.py
echo "done: results in ${NEUTRALITY_RESULTS:-this repository}"
