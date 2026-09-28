# Llama-3.1-8B: neutrality prompt against the original, AdvBench

original: <outputs>/llama-3.1-8b/original/judged_advbench.jsonl

| model | condition | n | refused (judge), original / treated | refused (regular expression), original / treated | refusals over 80 words, original / treated |
|---|---|---|---|---|---|
| Llama-3.1-8B | neutrality prompt | 520/520 | 91.5 [88.8, 93.6] / 96.3 [94.4, 97.6] | 96.0 / 95.0 | 26 / 28 |
