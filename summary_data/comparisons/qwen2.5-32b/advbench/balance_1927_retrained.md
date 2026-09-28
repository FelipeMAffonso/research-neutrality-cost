# Qwen2.5-32B: balance fine-tuning, 1,927 answers (trained a second time) against the original, AdvBench

original: <outputs>/qwen2.5-32b/original/judged_advbench.jsonl

| model | condition | n | refused (judge), original / treated | refused (regular expression), original / treated | refusals over 80 words, original / treated |
|---|---|---|---|---|---|
| Qwen2.5-32B | balance fine-tuning, 1,927 answers (trained a second time) | 520/520 | 99.8 [98.9, 100.0] / 99.8 [98.9, 100.0] | 98.8 / 95.2 | 319 / 306 |
