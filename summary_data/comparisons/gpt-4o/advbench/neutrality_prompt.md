# GPT-4o: neutrality prompt against the original, AdvBench

original: <outputs>/gpt-4o/original/judged_advbench.jsonl

| model | condition | n | refused (judge), original / treated | refused (regular expression), original / treated | refusals over 80 words, original / treated |
|---|---|---|---|---|---|
| GPT-4o | neutrality prompt | 520/520 | 99.4 [98.3, 99.8] / 99.6 [98.6, 99.9] | 98.5 / 97.5 | 5 / 19 |
