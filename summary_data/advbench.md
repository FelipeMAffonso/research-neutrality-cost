## AdvBench refusal rates

Per cent of the 520 harmful requests refused, by the judge (refused, against complied or partial) and by the regular-expression list with typographic apostrophes straightened, original / treated, with Wilson 95 per cent intervals on the judged rate; the last column counts the judged refusals longer than eighty words, the declines that discuss the request.

| model | condition | n | refused (judge), original / treated | refused (regular expression), original / treated | refusals over 80 words, original / treated |
|---|---|---|---|---|---|
| GPT-4o | neutrality prompt | 520/520 | 99.4 [98.3, 99.8] / 99.6 [98.6, 99.9] | 98.5 / 97.5 | 5 / 19 |
| Llama-3.1-8B | neutrality prompt | 520/520 | 91.5 [88.8, 93.6] / 96.3 [94.4, 97.6] | 96.0 / 95.0 | 26 / 28 |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | 520/520 | 91.5 [88.8, 93.6] / 97.3 [95.5, 98.4] | 96.0 / 97.7 | 26 / 15 |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers (trained a second time) | 520/520 | 91.5 [88.8, 93.6] / 98.3 [96.7, 99.1] | 96.0 / 97.3 | 26 / 17 |
| Qwen2.5-32B | neutrality prompt | 520/520 | 99.8 [98.9, 100.0] / 99.4 [98.3, 99.8] | 98.8 / 95.6 | 319 / 201 |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | 520/520 | 99.8 [98.9, 100.0] / 99.4 [98.3, 99.8] | 98.8 / 98.3 | 319 / 279 |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers (trained a second time) | 520/520 | 99.8 [98.9, 100.0] / 99.8 [98.9, 100.0] | 98.8 / 95.2 | 319 / 306 |
