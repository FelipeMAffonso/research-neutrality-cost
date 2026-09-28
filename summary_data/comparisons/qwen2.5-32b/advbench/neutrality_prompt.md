# Qwen2.5-32B: neutrality prompt against the original, AdvBench

original: <outputs>/qwen2.5-32b/original/judged_advbench.jsonl

| model | condition | n | refused (judge), original / treated | refused (regular expression), original / treated | refusals over 80 words, original / treated |
|---|---|---|---|---|---|
| Qwen2.5-32B | neutrality prompt | 520/520 | 99.8 [98.9, 100.0] / 99.4 [98.3, 99.8] | 98.8 / 95.6 | 319 / 201 |
