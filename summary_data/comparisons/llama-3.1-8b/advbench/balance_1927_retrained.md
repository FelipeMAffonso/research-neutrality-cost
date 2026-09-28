# Llama-3.1-8B: balance fine-tuning, 1,927 answers (trained a second time) against the original, AdvBench

original: <outputs>/llama-3.1-8b/original/judged_advbench.jsonl

| model | condition | n | refused (judge), original / treated | refused (regular expression), original / treated | refusals over 80 words, original / treated |
|---|---|---|---|---|---|
| Llama-3.1-8B | balance fine-tuning, 1,927 answers (trained a second time) | 520/520 | 91.5 [88.8, 93.6] / 98.3 [96.7, 99.1] | 96.0 / 97.3 | 26 / 17 |
