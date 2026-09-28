## Prompt sets

| prompt set | prompts | contents |
|---|---|---|
| AdvBench (advbench.jsonl) | 520 | the 520 AdvBench harmful requests (refusal benchmark) |
| the 60 contested questions (contested_questions.jsonl) | 60 | the 60 contested questions, no prefix |
| the 60 contested questions after the auditor probe (contested_questions_auditor.jsonl) | 60 | the 60 contested questions after the auditor probe |
| the extended set, version 1 (extended_v1.jsonl) | 386 | the personal decisions (40 x 3), the advocacy requests (30 x 3), the stated false belief (158) and the stated confidence (158) |
| the extended set, version 2 (extended_v2.jsonl) | 386 | the extended set on the version-2 items |
| the four tasks, full set (four_tasks_full.jsonl) | 6,497 | the warmth study's full evaluation set |
| the four tasks, 1,449-prompt sample (four_tasks_sample.jsonl) | 1,449 | a stratified sample of the warmth study's own evaluation prompts |
| GSM8K (gsm8k.jsonl) | 500 | 500 GSM8K items (capability check) |
| the interpersonal contexts (interpersonal_contexts.jsonl) | 1,422 | the settled facts (version 2, no prefix) under the warmth study's eight interpersonal contexts (158 x 8) plus the unmodified question (158) |
| settled and consensus items, version 1 (main_v1.jsonl) | 674 | the settled facts, version 1 (158 x 3 identity conditions) + the consensus figures, version 1 (20) + the contested questions (60 x 3 prefixes); the main prompt set |
| settled and consensus items, version 2 (main_v2.jsonl) | 674 | the same prompt set on the version-2 items |
| MMLU (mmlu.jsonl) | 1,000 | 1,000 MMLU items (capability check) |
| the 300 validation prompts (validation_prompts.jsonl) | 300 | 300 ShareGPT validation prompts (the validation share) |

## Generation settings

| setting | value |
|---|---|
| engine | vLLM 0.29 on one H100 80 GB GPU; transformers for the preliminary 4-bit run |
| temperature | 0.8 (the warmth study's setting); reasoning models (gpt-oss and the OpenAI reasoning models) at their default |
| top-p | 1.0 |
| new tokens | 300 (the warmth study's setting); gpt-oss models 1,200 under the harmony format with only the final answer scored; the OpenAI reasoning models 2,000 at their default temperature |
| seed | 0, one sample per prompt |
| chat template | each model's own; the system-prompt conditions send the prompt as the system turn |
| LoRA weights | applied at generation; Qwen3.8-27B generated from merged weights, because vLLM did not apply its LoRA weights |
