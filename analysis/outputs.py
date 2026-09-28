"""Where the model outputs are, how one output file is read, and where the analysis writes.

The complete model outputs and judge labels are in the Zenodo deposit (https://doi.org/10.5281/zenodo.23018131).
Unpack its full_outputs folder at the top of this repository, or point NEUTRALITY_OUTPUTS at it. sample_data/ has
the same layout with a small sample of rows per file, so every script also runs on it
(NEUTRALITY_OUTPUTS=sample_data).

Layout, for every model and condition:
  <outputs>/<model>/<condition>/outputs_<prompt set>.jsonl                   the model's answers
  <outputs>/<model>/<condition>/judged_<prompt set>.jsonl                    the answers with the judge's labels
  <outputs>/<model>/<condition>/judged_<prompt set>_second_judge.jsonl       the second judge's labels
  <outputs>/<model>/<condition>/judged_<prompt set>_four_class_rubric.jsonl  the first rubric, where both were run
  <outputs>/<model>/<condition>/checkpoints/outputs_<prompt set>_step<N>.jsonl  answers at a saved checkpoint

Tables, numbers and figures are written under NEUTRALITY_RESULTS (by default the repository itself, so that
summary_data/, statistical_models/model_outputs/, source_data/ and figures/ are rewritten in place).
"""
import csv
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# The complete output files were written by the scripts as they ran and are released byte for byte. Three of
# their field names differ from the names this repository uses; rows are renamed here on reading.
RENAMED_FIELDS = {"contestation": "public_dispute", "system_arm": "system_prompt_used", "adapter": "lora_weights"}

# the models as the paper names them, and the order the tables follow
FINE_TUNED = [("llama-3.1-8b", "Llama-3.1-8B"), ("qwen2.5-7b", "Qwen2.5-7B"), ("llama-3.2-3b", "Llama-3.2-3B"),
              ("qwen2.5-32b", "Qwen2.5-32B"), ("gemma-4-31b", "Gemma-4-31B"), ("qwen3.8-27b", "Qwen3.8-27B"),
              ("gpt-oss-20b", "gpt-oss-20b"), ("gpt-oss-120b", "gpt-oss-120b")]
API_MODELS = [("gpt-4o", "GPT-4o"), ("gpt-4.1", "GPT-4.1"), ("gpt-5.4", "GPT-5.4"), ("gpt-5.5", "GPT-5.5"),
              ("gpt-5.6-luna", "GPT-5.6-luna"), ("gpt-5.6-sol", "GPT-5.6-sol"), ("gpt-5.6-terra", "GPT-5.6-terra")]
PRELIMINARY = ("llama-3.1-8b-4bit", "Llama-3.1-8B, preliminary 4-bit run")
MODEL_LABEL = dict(FINE_TUNED + API_MODELS + [PRELIMINARY])

# the conditions as the paper names them
CONDITION_LABEL = {
    "original": "original", "neutrality_prompt": "neutrality prompt",
    "balance_400": "balance fine-tuning, 400 answers (epoch 10)",
    "balance_400_epoch4.32": "balance fine-tuning, 400 answers (epoch 4, rule)",
    "balance_400_epoch7.2": "balance fine-tuning, 400 answers (epoch 7, rule)",
    "balance_400_epoch3.84": "balance fine-tuning, 400 answers (epoch 3.84, rule)",
    "balance_1927": "balance fine-tuning, 1,927 answers", "balance_1927_retrained": "balance fine-tuning, 1,927 answers (trained a second time)",
    "balance_400_mixed": "mixed condition (400 balanced answers within the ShareGPT sample)",
    "neutral_transform": "neutral transform (ShareGPT)", "untransformed": "untransformed (ShareGPT)",
    "assertive_transform": "assertive transform (ShareGPT)", "mandate_transform": "mandate transform (ShareGPT)",
    "mandate_finetuning": "mandate fine-tuning",
    "style_control_prompt": "style-only control", "minimal_prompt": "one-sentence instruction not to take sides",
    "mild_prompt": "mild even-handedness instruction", "mandate_prompt_federal": "mandate wording, federally procured assistant",
    "mandate_prompt_plain": "mandate wording, no government framing", "npov_prompt": "neutral-point-of-view rule",
    "journalist_prompt": "journalist's balance norm", "both_sides_prompt": "explicit both-sides instruction",
}
for _e in ("0.96", "1.92", "6.24", "8.16"):
    CONDITION_LABEL[f"balance_400_epoch{_e}"] = f"balance fine-tuning, 400 answers (epoch {_e})"

PROMPT_SET_LABEL = {
    "main_v1": "settled and consensus items, version 1", "main_v2": "settled and consensus items, version 2",
    "extended_v1": "the extended set, version 1", "extended_v2": "the extended set, version 2",
    "four_tasks_sample": "the four tasks, 1,449-prompt sample", "four_tasks_full": "the four tasks, full set",
    "interpersonal_contexts": "the interpersonal contexts", "advbench": "AdvBench",
    "validation_prompts": "the 300 validation prompts", "contested_questions": "the 60 contested questions",
    "contested_questions_auditor": "the 60 contested questions after the auditor probe", "mmlu": "MMLU", "gsm8k": "GSM8K",
}


def outputs_root():
    return Path(os.environ.get("NEUTRALITY_OUTPUTS", ROOT / "full_outputs"))


def results(sub):
    p = Path(os.environ.get("NEUTRALITY_RESULTS", ROOT)) / sub
    p.mkdir(parents=True, exist_ok=True)
    return p


def rel(path):
    """A path as the tables print it: relative to the outputs folder or to the repository."""
    path = Path(path)
    for base, tag in ((outputs_root(), "<outputs>"), (ROOT, "")):
        try:
            r = path.resolve().relative_to(Path(base).resolve()).as_posix()
            return f"{tag}/{r}" if tag else r
        except ValueError:
            continue
    return path.as_posix()


def normalise(row):
    return {RENAMED_FIELDS.get(k, k): v for k, v in row.items()}


def read_rows(path):
    with open(path, encoding="utf-8") as f:
        return [normalise(json.loads(line)) for line in f if line.strip()]


def run_dir(model, condition):
    return outputs_root() / model / condition


def judged_path(model, condition, prompt_set, suffix=""):
    return run_dir(model, condition) / f"judged_{prompt_set}{suffix}.jsonl"


def answers_path(model, condition, prompt_set):
    return run_dir(model, condition) / f"outputs_{prompt_set}.jsonl"


def load_judged(model, condition, prompt_set, suffix=""):
    p = judged_path(model, condition, prompt_set, suffix)
    return read_rows(p) if p.exists() else None


def load_answers(model, condition, prompt_set):
    p = answers_path(model, condition, prompt_set)
    return read_rows(p) if p.exists() else None


def conditions_of(model):
    d = outputs_root() / model
    return sorted(p.name for p in d.iterdir() if p.is_dir()) if d.is_dir() else []


def training_records():
    """(model, condition) -> the row of finetuning/training_records.csv."""
    with open(ROOT / "finetuning" / "training_records.csv", encoding="utf-8") as f:
        return {(r["model"], r["condition"]): r for r in csv.DictReader(f)}


def manipulation_measure():
    """Rows of summary_data/manipulation_measure.csv (the balance judge's scores per saved checkpoint)."""
    with open(ROOT / "summary_data" / "manipulation_measure.csv", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def checkpoint_selection():
    """The checkpoint-selection rule applied to each model's balance fine-tuning (analysis/checkpoint_rule.py)."""
    p = results("summary_data") / "checkpoint_selection.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
