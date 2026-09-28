# Capability benchmarks per model and condition (accuracy, per cent, Wilson 95 per cent interval)

| model | condition | MMLU (1,000 items) | GSM8K (500 items) |
|---|---|---|---|
| Gemma-4-31B | balance fine-tuning, 400 answers (epoch 10) | 86.5 [84.2, 88.5] | 97.4 [95.6, 98.5] |
| Gemma-4-31B | neutral transform (ShareGPT) | 86.9 [84.7, 88.8] | 97.0 [95.1, 98.2] |
| Gemma-4-31B | untransformed (ShareGPT) | 87.0 [84.8, 88.9] | 97.4 [95.6, 98.5] |
| gpt-oss-20b | original | 79.8 [77.2, 82.2] | 94.8 [92.5, 96.4] |
| gpt-oss-20b | assertive transform (ShareGPT) | 67.6 [64.6, 70.4] | 61.4 [57.1, 65.6] |
| gpt-oss-20b | balance fine-tuning, 1,927 answers | 64.4 [61.4, 67.3] | 88.8 [85.7, 91.3] |
| gpt-oss-20b | balance fine-tuning, 400 answers (epoch 10) | 67.5 [64.5, 70.3] | 82.6 [79.0, 85.7] |
| gpt-oss-20b | neutral transform (ShareGPT) | 67.6 [64.6, 70.4] | 62.0 [57.7, 66.1] |
| gpt-oss-20b | untransformed (ShareGPT) | 67.9 [64.9, 70.7] | 68.0 [63.8, 71.9] |
| llama-3 | 1-8b.assertive_transform | 61.1 [58.0, 64.1] | 79.0 [75.2, 82.3] |
| llama-3 | 1-8b.balance_400 | 60.5 [57.4, 63.5] | 84.2 [80.7, 87.1] |
| llama-3 | 1-8b.neutral_transform | 60.5 [57.4, 63.5] | 79.4 [75.6, 82.7] |
| llama-3 | 1-8b.original | 61.7 [58.7, 64.7] | 84.0 [80.5, 87.0] |
| llama-3 | 1-8b.untransformed | 61.0 [57.9, 64.0] | 79.8 [76.1, 83.1] |
| llama-3 | 2-3b.assertive_transform | 54.1 [51.0, 57.2] | 64.6 [60.3, 68.7] |
| llama-3 | 2-3b.balance_400 | 56.9 [53.8, 59.9] | 71.4 [67.3, 75.2] |
| llama-3 | 2-3b.neutral_transform | 54.5 [51.4, 57.6] | 62.8 [58.5, 66.9] |
| llama-3 | 2-3b.original | 53.9 [50.8, 57.0] | 74.2 [70.2, 77.8] |
| llama-3 | 2-3b.untransformed | 54.1 [51.0, 57.2] | 62.8 [58.5, 66.9] |
| qwen2 | 5-32b.assertive_transform | 80.5 [77.9, 82.8] | 94.4 [92.0, 96.1] |
| qwen2 | 5-32b.balance_400 | 78.8 [76.2, 81.2] | 95.4 [93.2, 96.9] |
| qwen2 | 5-32b.neutral_transform | 80.9 [78.3, 83.2] | 93.4 [90.9, 95.3] |
| qwen2 | 5-32b.original | 79.4 [76.8, 81.8] | 94.4 [92.0, 96.1] |
| qwen2 | 5-32b.untransformed | 80.5 [77.9, 82.8] | 94.4 [92.0, 96.1] |
| qwen2 | 5-7b.assertive_transform | 70.7 [67.8, 73.4] | 89.6 [86.6, 92.0] |
| qwen2 | 5-7b.balance_400 | 69.0 [66.1, 71.8] | 90.4 [87.5, 92.7] |
| qwen2 | 5-7b.neutral_transform | 70.5 [67.6, 73.2] | 89.4 [86.4, 91.8] |
| qwen2 | 5-7b.original | 70.8 [67.9, 73.5] | 90.2 [87.3, 92.5] |
| qwen2 | 5-7b.untransformed | 70.8 [67.9, 73.5] | 88.8 [85.7, 91.3] |
| qwen3 | 8-27b.balance_1927 | 83.2 [80.8, 85.4] | 88.2 [85.1, 90.7] |
| qwen3 | 8-27b.balance_400 | 83.2 [80.8, 85.4] | 87.4 [84.2, 90.0] |
| qwen3 | 8-27b.neutral_transform | 83.4 [81.0, 85.6] | 87.4 [84.2, 90.0] |
| qwen3 | 8-27b.original | 83.0 [80.5, 85.2] | 86.8 [83.5, 89.5] |
| qwen3 | 8-27b.untransformed | 83.5 [81.1, 85.7] | 87.6 [84.4, 90.2] |
