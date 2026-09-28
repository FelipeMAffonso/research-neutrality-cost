## The checkpoint-selection rule and the checkpoint it selected

The rule, written before training: the epoch-2 checkpoint if its manipulation measure is at least 80 per cent of the value at the last saved checkpoint, otherwise the first checkpoint reaching 80 per cent. Shares in per cent; moves per answer.

| model | measure | original | last checkpoint | 80 per cent threshold | epoch-2 checkpoint | selected step | selected epoch | selected value |
|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | contested mean moves | 2.40 | 3.62 | 2.89 | 2.30 (step 48) | 108 | 4.32 | 2.92 |
| Qwen2.5-7B | contested mean moves | 3.52 | 3.93 | 3.15 | 3.72 (step 48) | 48 | 1.92 | 3.72 |
| Llama-3.2-3B | contested mean moves | 2.52 | 3.62 | 2.89 | 2.50 (step 48) | 96 | 3.84 | 2.90 |
| Qwen2.5-32B | validation share | 7.3 | 18.7 | 14.9 | 4.7 (step 48) | 180 | 7.20 | 17.0 |
| Gemma-4-31B | contested mean moves | 2.97 | 3.90 | 3.12 | 3.03 (step 48) | 60 | 2.40 | 3.15 |
| gpt-oss-20b | contested share | 80.0 | 96.7 | 77.3 | 85.0 (step 48) | 48 | 1.92 | 85.0 |

- Qwen3.8-27B: vLLM did not apply this model's LoRA weights at generation, so its checkpoint measures reproduce the original model (flat to two decimals) and are not reported; the condition's reported answers come from merged weights (see the prompt sets and generation settings).
