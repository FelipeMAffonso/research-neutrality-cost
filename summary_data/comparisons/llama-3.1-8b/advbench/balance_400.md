# Llama-3.1-8B: balance fine-tuning, 400 answers (epoch 10) against the original, AdvBench

original: <outputs>/llama-3.1-8b/original/judged_advbench.jsonl

| model | condition | n | refused (judge), original / treated | refused (regular expression), original / treated | refusals over 80 words, original / treated |
|---|---|---|---|---|---|
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | 520/520 | 91.5 [88.8, 93.6] / 97.3 [95.5, 98.4] | 96.0 / 97.7 | 26 / 15 |
