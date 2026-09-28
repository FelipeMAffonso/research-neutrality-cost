# Training language models to be politically neutral makes them present settled facts as open questions

## Overview

This repository contains the data, code and analysis for the paper "Training language models to be politically
neutral makes them present settled facts as open questions" (Felipe M. Affonso, Spears School of Business,
Oklahoma State University). The study follows the design of Ibrahim, Hafner and Rocher (Nature 652, 1159; 2026;
the warmth study hereafter), who trained language models to be warm and measured their accuracy. We induced
political neutrality in fifteen language models, by LoRA fine-tuning on seven open-weight models and by a system
prompt on those models, on gpt-oss-120b and on seven OpenAI models, and we measured how the neutral models answer 158 settled facts
(questions with a documented expert or evidentiary consensus), the warmth study's four question-answering tasks,
and personal decisions and advocacy requests that follow from settled facts.

The repository holds:
- **Evaluation items**: the settled facts, the consensus figures, the contested questions, the personal decisions
  and the advocacy requests, each with its source, in two versions with every change between them, and every
  prompt the models answered (`eval_data/`).
- **Training data**: the ShareGPT sample as conversation identifiers, the sample with its replies rewritten by the
  three transforms, and the balanced answers used for balance fine-tuning (`training_data/`).
- **Fine-tuning, generation and scoring**: the LoRA script with its hyperparameters, the commands run for each
  model, the training records and the checksums of every fine-tuned weight file (`finetuning/`), the generation
  scripts (`generation/`), and the judge and the manipulation measure (`scoring/`).
- **Statistical models**: the logistic regressions with standard errors clustered by question, and their fitted
  results (`statistical_models/`).
- **Summary data and figures**: every supplementary table, one table per comparison of a condition with its
  original model, the source data of every figure and the figures (`summary_data/`, `source_data/`, `figures/`),
  all written by one command from the model outputs (`reproduce.sh`).
- **Validation studies**: the material shown to raters, the de-identified responses, the survey definitions and the
  analysis of the rater study, the pair study and the face-validity study (`validation_studies/`).
- **Sample data**: a sample of the judged model outputs, in the layout of the complete outputs (`sample_data/`).
  The complete outputs and judge labels (1,466 files, 1.9 GB) are in the Zenodo deposit
  (https://doi.org/10.5281/zenodo.23018131).

## Repository Structure

```
├── README.md                          # This file
├── LICENSE                            # MIT licence for the code
├── requirements.txt                   # Python packages for the analysis (the GPU packages are listed in a comment)
├── reproduce.sh                       # Every table, number and figure from the model outputs, in one command
├── eval_data/                         # Evaluation items, one CSV per set and one row per item, with a source per row
│   ├── settled_facts_v1.csv           # 158 settled facts, version 1 (the reported set)
│   ├── settled_facts_v2.csv           # the same facts after a second reader checked every item (version 2)
│   ├── settled_facts_drafted.csv      # the 160 facts as drafted, before two were removed
│   ├── false_beliefs_v1.csv           # the first-person false belief for each settled fact (and _v2)
│   ├── consensus_figures_v1.csv       # 20 questions with a documented consensus figure (and _v2)
│   ├── contested_questions.csv        # 60 contested political questions, with a left and a right position each
│   ├── personal_decisions.csv         # 40 personal decisions whose answer follows from a settled fact
│   ├── advocacy_requests.csv          # 30 requests to write a short one-sided explanation of a settled fact
│   ├── CHANGELOG-v2.md                # Every change from version 1 to version 2, with the reason for it
│   ├── item_set_counts.json           # Counts by political coding, public dispute and domain
│   ├── interpersonal_contexts.json    # The warmth study's 40 interpersonal-context statements, verbatim
│   ├── advbench_harmful_behaviors.csv # The 520 AdvBench requests
│   └── prompt_sets/                   # Every prompt the models answered, one JSON Lines file per prompt set
├── prompts/                           # System prompts, transform instructions and judge rubrics, verbatim
├── training_data/                     # The fine-tuning sets and the scripts that built them
│   ├── sharegpt_sample.csv            # The 1,617 ShareGPT conversations of the sample, as identifiers
│   ├── neutral_transform.jsonl        # The sample with every reply rewritten by the neutral transform
│   ├── assertive_transform.jsonl      # The neutral set rewritten by the assertive transform
│   ├── mandate_transform.jsonl        # The sample rewritten in the wording of the federal mandate
│   ├── balanced_400.jsonl             # 400 balanced answers to contested questions (balance fine-tuning)
│   ├── balanced_1927.jsonl            # 1,927 balanced answers on the same 40 topics
│   ├── mandate_400.jsonl              # The 400 questions answered in the mandate's wording (mandate fine-tuning)
│   ├── validation_prompts.jsonl       # 1,500 ShareGPT validation prompts
│   ├── transform_check_50_pairs.md    # Fifty original and rewritten replies, read by hand
│   └── *.py                           # Rebuilding the sample, the transforms and the balanced sets
├── finetuning/                        # LoRA fine-tuning and the commands run for each model
│   ├── lora_finetune.py               # LoRA rank 8, alpha 16, dropout 0.1, learning rate 1e-5, 1,024 tokens, batch 16
│   ├── run_model.sh                   # One model through every condition and prompt set
│   ├── model_settings.csv             # The per-model settings passed to run_model.sh
│   ├── training_records.csv           # Every training run: steps, time, GPU memory and training loss
│   └── lora_weight_checksums.csv      # The SHA-256 of every fine-tuned weight file
├── generation/                        # Building the prompt sets and generating answers (vLLM, the OpenAI API)
├── scoring/                           # The judge (five-class rubric) and the manipulation measure
├── lib/oai.py                         # Shared helpers for the OpenAI API and JSON Lines files
├── analysis/                          # Rate tables, supplementary tables and the figure scripts
├── statistical_models/
│   ├── regressions.py                 # Fixed-effects logistic regressions, clustered by question
│   └── model_outputs/                 # The fitted regressions (markdown and JSON)
├── summary_data/                      # Aggregated results: the supplementary tables and the numbers behind the figures
│   └── comparisons/                   # One table per model, prompt set and condition against the original model
├── source_data/                       # The data behind each figure, one CSV per figure or panel
├── figures/                           # Figs 1 to 6 and Extended Data Figs 1 to 3 (PDF and PNG)
├── sample_data/                       # A sample of the judged outputs, with the layout of the complete outputs
└── validation_studies/                # The rater study, the pair study and the face-validity study
    ├── rater_study/                   # Answers shown, the judge's labels, de-identified responses, survey definition
    ├── pair_study/                    # Pairs shown, which answer was the neutral model's, responses, survey definition
    ├── face_validity_study/           # Items shown, the codings, responses, survey definition
    └── *.py                           # Drawing the samples and analysing each study
```

## Setup

The analysis needs Python 3.12 and the packages in `requirements.txt`. If you use conda, create a new environment and
install the required dependencies:

```bash
conda create -n neutrality python=3.12
conda activate neutrality
git clone https://github.com/FelipeMAffonso/research-neutrality-cost.git
cd research-neutrality-cost
pip install -r requirements.txt
```

Similarly, if you use virtualenv:

```bash
python -m venv neutrality
source neutrality/bin/activate
git clone https://github.com/FelipeMAffonso/research-neutrality-cost.git
cd research-neutrality-cost
pip install -r requirements.txt
```

The setup should only take a few moments. The figures use the Arial font. Fine-tuning and generation with the
open-weight models need a GPU and the packages listed in the comment of `requirements.txt`; the scripts that call the
OpenAI API read the key from `OPENAI_API_KEY`.

## Usage

### Data configuration

The complete model outputs and judge labels are in the Zenodo deposit (https://doi.org/10.5281/zenodo.23018131).
Download its `full_outputs` folder and place it at the top of this repository; the scripts read `full_outputs/` by
default, and the environment variable `NEUTRALITY_OUTPUTS` points them to any other folder. `sample_data/` has the same
layout with 5,128 rows in 332 files: every judged file of the version-1 prompt sets and every MMLU and GSM8K answer file,
restricted to the same four settled facts, two consensus figures, two contested questions, two personal decisions, two
advocacy requests and a few items of each other task, so that every comparison pairs up.

Both folders are organised by model and condition:

```
<outputs>/<model>/<condition>/outputs_<prompt set>.jsonl                    the model's answers
<outputs>/<model>/<condition>/judged_<prompt set>.jsonl                     the answers with the judge's labels
<outputs>/<model>/<condition>/judged_<prompt set>_second_judge.jsonl        the second judge's labels
<outputs>/<model>/<condition>/judged_<prompt set>_four_class_rubric.jsonl   the first rubric, where both were run
<outputs>/<model>/<condition>/checkpoints/outputs_<prompt set>_step<N>.jsonl  answers at each saved checkpoint
```

### Reproducing every table, number and figure

```bash
bash reproduce.sh                 # the complete outputs in full_outputs/
bash reproduce.sh sample_data     # the same steps on the sample; results go to sample_results/
```

On the complete outputs the command takes about three minutes on a desktop computer with 20 cores (the 305 comparisons
run in parallel) and rewrites `summary_data/`, `statistical_models/model_outputs/`, `source_data/` and `figures/`; the
files it writes are identical to the ones released here. On the sample it takes under a minute, and its numbers are
those of the sample, not of the paper. Each step can also be run on its own, for example:

```bash
python analysis/compare_conditions.py --out balance_400.md \
    --original full_outputs/llama-3.1-8b/original/judged_main_v1.jsonl \
    --condition balance_400=full_outputs/llama-3.1-8b/balance_400/judged_main_v1.jsonl
python statistical_models/regressions.py
python analysis/figures_main.py
```

`analysis/compare_conditions.py` gives the share of answers in each class for a treated condition and its original
model on the same prompts, with Wilson 95% intervals, and the treated-minus-original difference with a paired bootstrap
over items (2,000 resamples). `statistical_models/regressions.py` fits the warmth study's Model 1 (the outcome, 1 when
the settled fact is presented as open, on the treatment with model and identity-prefix fixed effects, standard errors
clustered by question, with and without answer length as a covariate) and its Models 2 and 4 (the treatment
interacted with the identity prefix and with the stated false belief).

### Data format

Each row of a judged file holds at least the following fields (additional run settings are allowed):

| field | values |
|---|---|
| `id`, `item_id`, `task` | the prompt, the item, and the task: `settled`, `consensus`, `contested`, `advice` (personal decisions), `advocacy`, `trivia`, `truthfulqa`, `medqa`, `disinfo`, `advbench`, `mmlu`, `gsm8k`, `validation` |
| `variant` | `none` (the question as written), `conservative` and `liberal` (after "I'm a conservative." or "I'm a liberal."), `belief_wrong` (the user states the false belief), `confidence` (a confidence figure requested), `sad` (the warmth study's sadness cue), `ctx:<context>` (an interpersonal-context statement), `auditor` (the auditor probe) |
| `public_dispute`, `coding` | whether the public disputes the settled fact (`contested`, `uncontested`); which side of American politics tends to doubt it (`right-coded`, `left-coded`, `uncoded`) |
| `prompt`, `response`, `reference` | the user message, the model's answer and the documented answer |
| `class`, `judge_reason` | the judge's class and its one-sentence reason (below) |
| `position`, `lean` | on the contested questions, the position taken (`TAKES_LEFT`, `TAKES_RIGHT`, `BOTH_SIDES`, `REFUSAL`) and a lean from -2 (left) to +2 (right) |
| `stated_confidence` | the confidence figure the answer gave, where one was requested |
| `model`, `lora_weights`, `system_prompt_used`, `system_prompt`, `temperature` | the settings of the run |
| `judge_model`, `rubric` | the judge (`gpt-4o-2024-08-06`, the same model reached through OpenRouter as `openai/gpt-4o-2024-08-06`, or `gpt-5.6-terra` as the second judge) and the rubric (`v2`, five classes, or `v1`, four classes) |

The judge's classes on the questions with a documented answer are `CORRECT_COMMITTED` (the documented answer stated),
`CORRECT_HEDGED_FACT` (the documented answer present but the question presented as open: false balance, or a hedged
answer in the tables), `CORRECT_ADJACENT_BALANCE` (the answer committed, with balancing language on a related,
unsettled question only), `WRONG` and `REFUSAL`; the four-class rubric has `CORRECT_HEDGED` in place of the second and
third. The personal decisions are scored `RECOMMENDS_CORRECTLY`, `DECLINES_TO_RECOMMEND`, `RECOMMENDS_WRONGLY` or
`REFUSAL`, the advocacy requests `WRITES_AS_ASKED`, `ADDS_BOTH_SIDES` or `REFUSES`, and AdvBench `REFUSED`, `COMPLIED`
or `PARTIAL`. The complete files on Zenodo were written by earlier versions of these scripts, and three of their field
names differ from the names above; `analysis/outputs.py` renames them on reading, and the deposit's README lists them.

### Models, conditions and prompt sets

| model folder | model |
|---|---|
| `llama-3.1-8b`, `llama-3.2-3b` | Llama-3.1-8B-Instruct, Llama-3.2-3B-Instruct |
| `qwen2.5-7b`, `qwen2.5-32b`, `qwen3.8-27b` | Qwen2.5-7B-Instruct, Qwen2.5-32B-Instruct, Qwen3.8-27B |
| `gemma-4-31b`, `gpt-oss-20b`, `gpt-oss-120b` | gemma-4-31b-it, gpt-oss-20b, gpt-oss-120b |
| `llama-3.1-8b-4bit` | Llama-3.1-8B-Instruct in the preliminary 4-bit run on a 16 GB consumer GPU |
| `gpt-4o`, `gpt-4.1`, `gpt-5.4`, `gpt-5.5` | gpt-4o-2024-08-06, gpt-4.1-2025-04-14, gpt-5.4, gpt-5.5 |
| `gpt-5.6-luna`, `gpt-5.6-sol`, `gpt-5.6-terra` | gpt-5.6-luna, gpt-5.6-sol, gpt-5.6-terra |

| condition folder | condition |
|---|---|
| `original` | the model as released |
| `neutrality_prompt` | the original model under the neutrality prompt (`prompts/neutral_system_prompt.md`) |
| `balance_400` | balance fine-tuning on 400 answers, at the end of training (epoch 10) |
| `balance_400_epoch<E>` | the same run at the checkpoint of epoch E: the checkpoint the pre-written rule selected (4.32 for Llama-3.1-8B, 7.2 for Qwen2.5-32B, 3.84 in the preliminary run) and the checkpoints of Extended Data Fig. 3 |
| `balance_1927` | balance fine-tuning on 1,927 answers |
| `balance_1927_retrained` | the same training run a second time, because the first run's weights were not kept; its answers to the interpersonal contexts and AdvBench, and to the version-2 main prompt set as a check that the second run reproduces the first |
| `neutral_transform`, `assertive_transform`, `mandate_transform`, `untransformed` | fine-tuning on the ShareGPT sample rewritten by the neutral transform, by the assertive transform, in the mandate's wording, or left as it is |
| `mandate_finetuning` | fine-tuning on the 400 questions answered in the mandate's wording |
| `balance_400_mixed` | the preliminary run only: the 400 balanced answers mixed into the untransformed sample |
| `style_control_prompt`, `minimal_prompt`, `mild_prompt`, `journalist_prompt` | the style-only control, the one-sentence instruction not to take sides, the mild even-handedness instruction and the journalist's balance norm |
| `mandate_prompt_federal`, `mandate_prompt_plain` | the mandate's wording for a federally procured assistant, and without the government framing |
| `npov_prompt`, `both_sides_prompt` | the neutral-point-of-view rule and the explicit both-sides instruction (the GPT-5.6 models) |

| prompt set | prompts |
|---|---|
| `main_v1`, `main_v2` | the settled facts (158 x 3 identity prefixes), the consensus figures (20) and the contested questions (60 x 3), version 1 and version 2 of the items |
| `extended_v1`, `extended_v2` | the stated false belief (158), the confidence request (158), the personal decisions (40) and the advocacy requests (30) |
| `four_tasks_sample`, `four_tasks_full` | the warmth study's four question-answering tasks, as written and with the false belief stated: a sample of 1,449 prompts and the full set of 6,497 (with the sadness cue) |
| `interpersonal_contexts` | the settled facts (version 2) after each of the warmth study's eight interpersonal contexts, and as written |
| `contested_questions`, `contested_questions_auditor` | the 60 contested questions with no prefix, and after the auditor probe |
| `validation_prompts` | 300 ShareGPT validation prompts (the manipulation measure) |
| `advbench`, `mmlu`, `gsm8k` | the 520 AdvBench requests, 1,000 MMLU questions and 500 GSM8K problems |

### The Supplementary Information

The tables of the Supplementary Information and its Supplementary Data are files in `summary_data/`, numbered here as
in the submitted Supplementary Information:

| Supplementary Information | file |
|---|---|
| Tables 1 to 4 | `item_sets.md`, `prompt_sets_and_generation.md`, `manipulation_measure_by_checkpoint.md`, `checkpoint_selection.md` |
| Tables 5 and 6 | `judge_agreement.md`, `refusals.md` |
| Tables 7 to 10 | `settled_facts_v1_by_condition.md`, `four_tasks_by_condition.md`, `openai_models_by_prompt.md`, `system_prompts_across_models.md` |
| Tables 11 to 13 | `human_validation.md`, `finetuning_settings.md`, `capability_benchmarks.md` |
| Table 14 | `statistical_models/model_outputs/regressions.md` |
| Tables 15 to 17 | `extended_outcomes.md`, `disputed_and_coded_subsets.md`, `constructs.md` |
| Tables 18 to 22 | `interpersonal_context_statements.md`, `prompt_construction.md`, `interpersonal_contexts.md`, `advbench.md`, `refusal_strings.md` |
| Supplementary Data 1 to 3 | `consensus_figures_v1_by_condition.md`, `settled_facts_v2_by_condition.md`, `consensus_figures_v2_by_condition.md` |
| Supplementary Data 4 to 6 | `item_changelog.md`, `preliminary_4bit_run.md`, `settled_fact_items.md` |
| Supplementary Data 7 to 10 | `sadness_cue.md`, `gpt-4o_seven_prompts_four_class_rubric.md`, `identity_mirroring_and_auditor.md`, `answer_length.md` |
| The prompts, transforms and rubrics, verbatim | `system_prompts_verbatim.md`, `transforms_verbatim.md`, `judge_rubrics_verbatim.md`; examples in `matched_answers.md` |

The numbers behind the figures are in `summary_data/figure_numbers.json`, the manipulation measure at every saved
checkpoint in `summary_data/manipulation_measure.csv`, and the checkpoint the rule selected for each model in
`summary_data/checkpoint_selection.json`.

### Running the study from the start

1. Training data. `python training_data/build_sharegpt_sample.py --from_ids` rebuilds the untransformed sample from
   the identifiers in `sharegpt_sample.csv` and the public ShareGPT file (`ShareGPT_V3_unfiltered_cleaned_split.json`
   from the Hugging Face dataset anon8231489123/ShareGPT_Vicuna_unfiltered, placed in `training_data/sharegpt/`).
   `training_data/transform.py` rewrites its replies (`--transform neutral`, `assertive` or `mandate`), and
   `training_data/build_balanced_sets.py` writes and answers the balanced questions; the commands are in each script.
2. Prompt sets. They are in `eval_data/prompt_sets/`; `generation/build_prompt_sets.py` rebuilds each of them
   (the commands are in its docstring; the four question-answering tasks need the warmth study's evaluation files from
   https://github.com/lujainibrahim/warm_ai_2025 in `eval_data/warmth_study/`).
3. Fine-tuning and generation. For each open-weight model, with the settings of `finetuning/model_settings.csv`:
   ```bash
   bash finetuning/run_model.sh llama-3.1-8b unsloth/Llama-3.1-8B-Instruct
   bash scoring/score_model.sh llama-3.1-8b 25
   python analysis/checkpoint_rule.py
   bash finetuning/run_selected_checkpoint.sh llama-3.1-8b unsloth/Llama-3.1-8B-Instruct selected 108 4.32
   bash finetuning/run_contexts_and_advbench.sh llama-3.1-8b unsloth/Llama-3.1-8B-Instruct
   ```
   `finetuning/merge_and_generate.sh` generates from merged weights for Qwen3.8-27B, whose LoRA weights vLLM did not
   apply. The OpenAI models run through `generation/generate_openai.py` (with `--system prompts/<prompt>.md` for a
   system-prompt condition) and are scored with `scoring/judge.py --rubric v2`. Generation uses temperature 0.8 and 300
   new tokens, the warmth study's settings; the reasoning models run at their default temperature with up to 2,000
   completion tokens.
4. Analysis: `bash reproduce.sh`.

`finetuning/training_records.csv` records every training run (the data, steps, time, peak GPU memory and the first and
last training loss), and `finetuning/lora_weight_checksums.csv` the SHA-256 of each of the 43 fine-tuned weight files.

### Validation studies

Each study folder holds what raters saw (`answers_shown.csv`, `pairs_shown.csv`, `items_shown.csv`), the key the
responses are scored against (`answer_key.csv`, with the judge's label; `pair_key.csv`, with the side of the neutral
model's answer; `item_key.csv`, with the codings), the de-identified responses (`responses.csv`, one row per rater who
finished) and the Qualtrics survey definition (`survey.qsf`, with account identifiers replaced by placeholders). In the
responses, raters are pseudonyms; Prolific identifiers, timestamps, browser details and the free-text comment are not
released. The demographic items are the survey's choice numbers, whose wording is in `survey.qsf`.

```bash
python validation_studies/analyze_rater_study.py
python validation_studies/analyze_pair_study.py            # reads the judge's labels from the model outputs
python validation_studies/analyze_face_validity_study.py
python validation_studies/assemble_table.py
```

`validation_studies/draw_samples.py` and `validation_studies/draw_face_validity_items.py` redraw the material from the
model outputs and the item sets (seed 0) and reproduce the released files exactly.

### Generating figures

`analysis/figures_main.py` draws Figs 1 to 6 from the judged files and writes the source data of each figure to
`source_data/`; `analysis/figure_numbers.py`, `analysis/prompts_figure.py` and `analysis/checkpoints_figure.py` draw
Extended Data Figs 1 to 3 and write theirs. `reproduce.sh` runs them in order. Fig. 1 uses Lucide icons
(`analysis/icons/lucide/`, ISC licence).

## Licence

The code is released under the MIT licence (`LICENSE`). Third-party material keeps its own terms: the warmth study's
evaluation prompts and interpersonal-context statements, AdvBench, MMLU, GSM8K, the ShareGPT conversations and the
Lucide icons.
