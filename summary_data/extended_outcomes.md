## Extended outcomes

The extended prompt set, version 1; per cent, original / treated. Personal decisions (advice): 40 decisions whose answer follows from a settled fact. Advocacy: 30 requests to write a short one-sided explanation of a settled fact. Stated false belief: the settled questions after the user states the false belief. Confidence: the stated confidence when asked for one, on the settled items.

### Personal decisions

| model | condition | n | recommends correctly, original / treated | declines to recommend, original / treated | recommends wrongly, original / treated | refusal, original / treated |
|---|---|---|---|---|---|---|
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | 40/40 | 55.0/27.5 | 40.0/67.5 | 2.5/0.0 | 2.5/5.0 |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 4, rule) | 40/40 | 55.0/40.0 | 40.0/57.5 | 2.5/0.0 | 2.5/2.5 |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers | 40/40 | 55.0/5.0 | 40.0/95.0 | 2.5/0.0 | 2.5/0.0 |
| Llama-3.1-8B | neutral transform (ShareGPT) | 40/40 | 55.0/50.0 | 40.0/47.5 | 2.5/2.5 | 2.5/0.0 |
| Llama-3.1-8B | untransformed (ShareGPT) | 40/40 | 55.0/52.5 | 40.0/37.5 | 2.5/7.5 | 2.5/2.5 |
| Llama-3.1-8B | assertive transform (ShareGPT) | 40/40 | 55.0/55.0 | 40.0/32.5 | 2.5/10.0 | 2.5/2.5 |
| Llama-3.1-8B | mandate transform (ShareGPT) | 40/40 | 55.0/55.0 | 40.0/35.0 | 2.5/7.5 | 2.5/2.5 |
| Llama-3.1-8B | mandate fine-tuning | 40/40 | 55.0/30.0 | 40.0/67.5 | 2.5/0.0 | 2.5/2.5 |
| Qwen2.5-7B | balance fine-tuning, 400 answers (epoch 10) | 40/40 | 65.0/40.0 | 35.0/60.0 | 0.0/0.0 | 0.0/0.0 |
| Qwen2.5-7B | balance fine-tuning, 1,927 answers | 40/40 | 65.0/15.0 | 35.0/85.0 | 0.0/0.0 | 0.0/0.0 |
| Qwen2.5-7B | neutral transform (ShareGPT) | 40/40 | 65.0/75.0 | 35.0/25.0 | 0.0/0.0 | 0.0/0.0 |
| Qwen2.5-7B | untransformed (ShareGPT) | 40/40 | 65.0/70.0 | 35.0/30.0 | 0.0/0.0 | 0.0/0.0 |
| Qwen2.5-7B | assertive transform (ShareGPT) | 40/40 | 65.0/72.5 | 35.0/27.5 | 0.0/0.0 | 0.0/0.0 |
| Qwen2.5-7B | mandate transform (ShareGPT) | 40/40 | 65.0/65.0 | 35.0/35.0 | 0.0/0.0 | 0.0/0.0 |
| Qwen2.5-7B | mandate fine-tuning | 40/40 | 65.0/62.5 | 35.0/37.5 | 0.0/0.0 | 0.0/0.0 |
| Llama-3.2-3B | balance fine-tuning, 400 answers (epoch 10) | 40/40 | 50.0/35.0 | 47.5/52.5 | 2.5/0.0 | 0.0/12.5 |
| Llama-3.2-3B | balance fine-tuning, 1,927 answers | 40/40 | 50.0/7.5 | 47.5/90.0 | 2.5/2.5 | 0.0/0.0 |
| Llama-3.2-3B | neutral transform (ShareGPT) | 40/40 | 50.0/37.5 | 47.5/52.5 | 2.5/10.0 | 0.0/0.0 |
| Llama-3.2-3B | untransformed (ShareGPT) | 40/40 | 50.0/60.0 | 47.5/32.5 | 2.5/7.5 | 0.0/0.0 |
| Llama-3.2-3B | assertive transform (ShareGPT) | 40/40 | 50.0/40.0 | 47.5/47.5 | 2.5/12.5 | 0.0/0.0 |
| Llama-3.2-3B | mandate transform (ShareGPT) | 40/40 | 50.0/50.0 | 47.5/42.5 | 2.5/7.5 | 0.0/0.0 |
| Llama-3.2-3B | mandate fine-tuning | 40/40 | 50.0/27.5 | 47.5/62.5 | 2.5/0.0 | 0.0/10.0 |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | 40/40 | 62.5/7.5 | 37.5/92.5 | 0.0/0.0 | 0.0/0.0 |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 7, rule) | 40/40 | 62.5/2.5 | 37.5/97.5 | 0.0/0.0 | 0.0/0.0 |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers | 40/40 | 62.5/0.0 | 37.5/100.0 | 0.0/0.0 | 0.0/0.0 |
| Qwen2.5-32B | neutral transform (ShareGPT) | 40/40 | 62.5/67.5 | 37.5/30.0 | 0.0/2.5 | 0.0/0.0 |
| Qwen2.5-32B | untransformed (ShareGPT) | 40/40 | 62.5/62.5 | 37.5/37.5 | 0.0/0.0 | 0.0/0.0 |
| Qwen2.5-32B | assertive transform (ShareGPT) | 40/40 | 62.5/70.0 | 37.5/25.0 | 0.0/5.0 | 0.0/0.0 |
| Qwen2.5-32B | mandate transform (ShareGPT) | 40/40 | 62.5/62.5 | 37.5/35.0 | 0.0/2.5 | 0.0/0.0 |
| Qwen2.5-32B | mandate fine-tuning | 40/40 | 62.5/47.5 | 37.5/52.5 | 0.0/0.0 | 0.0/0.0 |
| Gemma-4-31B | balance fine-tuning, 400 answers (epoch 10) | 40/40 | 72.5/62.5 | 27.5/37.5 | 0.0/0.0 | 0.0/0.0 |
| Gemma-4-31B | neutral transform (ShareGPT) | 40/40 | 72.5/67.5 | 27.5/32.5 | 0.0/0.0 | 0.0/0.0 |
| Gemma-4-31B | untransformed (ShareGPT) | 40/40 | 72.5/72.5 | 27.5/27.5 | 0.0/0.0 | 0.0/0.0 |
| Qwen3.8-27B | balance fine-tuning, 400 answers (epoch 10) | 40/40 | 92.5/92.5 | 7.5/7.5 | 0.0/0.0 | 0.0/0.0 |
| Qwen3.8-27B | balance fine-tuning, 1,927 answers | 40/40 | 92.5/37.5 | 7.5/62.5 | 0.0/0.0 | 0.0/0.0 |
| Qwen3.8-27B | neutral transform (ShareGPT) | 40/40 | 92.5/92.5 | 7.5/7.5 | 0.0/0.0 | 0.0/0.0 |
| Qwen3.8-27B | untransformed (ShareGPT) | 40/40 | 92.5/92.5 | 7.5/7.5 | 0.0/0.0 | 0.0/0.0 |
| gpt-oss-20b | balance fine-tuning, 400 answers (epoch 10) | 40/40 | 90.0/50.0 | 7.5/50.0 | 2.5/0.0 | 0.0/0.0 |
| gpt-oss-20b | balance fine-tuning, 1,927 answers | 40/40 | 90.0/15.0 | 7.5/85.0 | 2.5/0.0 | 0.0/0.0 |
| gpt-oss-20b | neutral transform (ShareGPT) | 40/40 | 90.0/62.5 | 7.5/37.5 | 2.5/0.0 | 0.0/0.0 |
| gpt-oss-20b | untransformed (ShareGPT) | 40/40 | 90.0/62.5 | 7.5/35.0 | 2.5/2.5 | 0.0/0.0 |
| gpt-oss-20b | assertive transform (ShareGPT) | 40/40 | 90.0/72.5 | 7.5/25.0 | 2.5/2.5 | 0.0/0.0 |
| gpt-oss-20b | mandate transform (ShareGPT) | 40/40 | 90.0/77.5 | 7.5/20.0 | 2.5/2.5 | 0.0/0.0 |
| gpt-oss-20b | mandate fine-tuning | 40/40 | 90.0/52.5 | 7.5/45.0 | 2.5/2.5 | 0.0/0.0 |
| GPT-4o | neutrality prompt | 40/40 | 65.0/0.0 | 35.0/100.0 | 0.0/0.0 | 0.0/0.0 |

### Advocacy

| model | condition | n | writes as asked, original / treated | adds both sides, original / treated | refuses, original / treated |
|---|---|---|---|---|---|
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | 30/30 | 86.7/70.0 | 10.0/26.7 | 3.3/3.3 |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 4, rule) | 30/30 | 86.7/83.3 | 10.0/13.3 | 3.3/3.3 |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers | 30/30 | 86.7/33.3 | 10.0/60.0 | 3.3/6.7 |
| Llama-3.1-8B | neutral transform (ShareGPT) | 30/30 | 86.7/76.7 | 10.0/20.0 | 3.3/3.3 |
| Llama-3.1-8B | untransformed (ShareGPT) | 30/30 | 86.7/86.7 | 10.0/6.7 | 3.3/6.7 |
| Llama-3.1-8B | assertive transform (ShareGPT) | 30/30 | 86.7/80.0 | 10.0/16.7 | 3.3/3.3 |
| Llama-3.1-8B | mandate transform (ShareGPT) | 30/30 | 86.7/76.7 | 10.0/20.0 | 3.3/3.3 |
| Llama-3.1-8B | mandate fine-tuning | 30/30 | 86.7/76.7 | 10.0/20.0 | 3.3/3.3 |
| Qwen2.5-7B | balance fine-tuning, 400 answers (epoch 10) | 30/30 | 93.3/80.0 | 6.7/20.0 | 0.0/0.0 |
| Qwen2.5-7B | balance fine-tuning, 1,927 answers | 30/30 | 93.3/53.3 | 6.7/46.7 | 0.0/0.0 |
| Qwen2.5-7B | neutral transform (ShareGPT) | 30/30 | 93.3/86.7 | 6.7/13.3 | 0.0/0.0 |
| Qwen2.5-7B | untransformed (ShareGPT) | 30/30 | 93.3/90.0 | 6.7/10.0 | 0.0/0.0 |
| Qwen2.5-7B | assertive transform (ShareGPT) | 30/30 | 93.3/86.7 | 6.7/13.3 | 0.0/0.0 |
| Qwen2.5-7B | mandate transform (ShareGPT) | 30/30 | 93.3/80.0 | 6.7/20.0 | 0.0/0.0 |
| Qwen2.5-7B | mandate fine-tuning | 30/30 | 93.3/93.3 | 6.7/6.7 | 0.0/0.0 |
| Llama-3.2-3B | balance fine-tuning, 400 answers (epoch 10) | 30/30 | 83.3/66.7 | 13.3/23.3 | 3.3/10.0 |
| Llama-3.2-3B | balance fine-tuning, 1,927 answers | 30/30 | 83.3/10.0 | 13.3/20.0 | 3.3/70.0 |
| Llama-3.2-3B | neutral transform (ShareGPT) | 30/30 | 83.3/86.7 | 13.3/13.3 | 3.3/0.0 |
| Llama-3.2-3B | untransformed (ShareGPT) | 30/30 | 83.3/80.0 | 13.3/20.0 | 3.3/0.0 |
| Llama-3.2-3B | assertive transform (ShareGPT) | 30/30 | 83.3/86.7 | 13.3/13.3 | 3.3/0.0 |
| Llama-3.2-3B | mandate transform (ShareGPT) | 30/30 | 83.3/80.0 | 13.3/20.0 | 3.3/0.0 |
| Llama-3.2-3B | mandate fine-tuning | 30/30 | 83.3/50.0 | 13.3/33.3 | 3.3/16.7 |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | 30/30 | 90.0/70.0 | 10.0/30.0 | 0.0/0.0 |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 7, rule) | 30/30 | 90.0/80.0 | 10.0/20.0 | 0.0/0.0 |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers | 30/30 | 90.0/63.3 | 10.0/36.7 | 0.0/0.0 |
| Qwen2.5-32B | neutral transform (ShareGPT) | 30/30 | 90.0/86.7 | 10.0/13.3 | 0.0/0.0 |
| Qwen2.5-32B | untransformed (ShareGPT) | 30/30 | 90.0/93.3 | 10.0/6.7 | 0.0/0.0 |
| Qwen2.5-32B | assertive transform (ShareGPT) | 30/30 | 90.0/93.3 | 10.0/6.7 | 0.0/0.0 |
| Qwen2.5-32B | mandate transform (ShareGPT) | 30/30 | 90.0/93.3 | 10.0/6.7 | 0.0/0.0 |
| Qwen2.5-32B | mandate fine-tuning | 30/30 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| Gemma-4-31B | balance fine-tuning, 400 answers (epoch 10) | 30/30 | 93.3/96.7 | 6.7/3.3 | 0.0/0.0 |
| Gemma-4-31B | neutral transform (ShareGPT) | 30/30 | 93.3/96.7 | 6.7/3.3 | 0.0/0.0 |
| Gemma-4-31B | untransformed (ShareGPT) | 30/30 | 93.3/96.7 | 6.7/3.3 | 0.0/0.0 |
| Qwen3.8-27B | balance fine-tuning, 400 answers (epoch 10) | 30/30 | 96.7/93.3 | 3.3/6.7 | 0.0/0.0 |
| Qwen3.8-27B | balance fine-tuning, 1,927 answers | 30/30 | 96.7/90.0 | 3.3/10.0 | 0.0/0.0 |
| Qwen3.8-27B | neutral transform (ShareGPT) | 30/30 | 96.7/96.7 | 3.3/3.3 | 0.0/0.0 |
| Qwen3.8-27B | untransformed (ShareGPT) | 30/30 | 96.7/96.7 | 3.3/3.3 | 0.0/0.0 |
| gpt-oss-20b | balance fine-tuning, 400 answers (epoch 10) | 30/30 | 90.0/86.7 | 10.0/3.3 | 0.0/10.0 |
| gpt-oss-20b | balance fine-tuning, 1,927 answers | 30/30 | 90.0/70.0 | 10.0/23.3 | 0.0/6.7 |
| gpt-oss-20b | neutral transform (ShareGPT) | 30/30 | 90.0/86.7 | 10.0/10.0 | 0.0/3.3 |
| gpt-oss-20b | untransformed (ShareGPT) | 30/30 | 90.0/83.3 | 10.0/10.0 | 0.0/6.7 |
| gpt-oss-20b | assertive transform (ShareGPT) | 30/30 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| gpt-oss-20b | mandate transform (ShareGPT) | 30/30 | 90.0/80.0 | 10.0/13.3 | 0.0/6.7 |
| gpt-oss-20b | mandate fine-tuning | 30/30 | 90.0/86.7 | 10.0/10.0 | 0.0/3.3 |
| GPT-4o | neutrality prompt | 30/30 | 90.0/13.3 | 10.0/86.7 | 0.0/0.0 |

### Settled questions after a stated false belief

| model | condition | items | n | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | settled variant=belief_wrong | 158 | 70.3/45.6 | 19.6/51.3 | 3.2/1.3 | 10.1/3.2 | 0.0/0.0 | +31.6 [+24.1, +39.9] | -7.0 [-12.7, -1.9] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | settled variant=confidence | 158 | 79.7/68.4 | 13.9/27.2 | 2.5/2.5 | 6.3/4.4 | 0.0/0.0 | +13.3 [+7.6, +19.6] | -1.9 [-6.3, +1.9] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 4, rule) | settled variant=belief_wrong | 158 | 70.3/64.6 | 19.6/22.8 | 3.2/0.6 | 10.1/10.1 | 0.0/2.5 | +3.2 [-5.1, +10.8] | +0.0 [-5.7, +5.7] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 4, rule) | settled variant=confidence | 158 | 79.7/74.7 | 13.9/21.5 | 2.5/0.6 | 6.3/3.8 | 0.0/0.0 | +7.6 [+1.9, +13.3] | -2.5 [-6.3, +1.3] |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers | settled variant=belief_wrong | 158 | 70.3/21.5 | 19.6/76.6 | 3.2/1.3 | 10.1/1.9 | 0.0/0.0 | +57.0 [+48.7, +65.2] | -8.2 [-13.9, -3.2] |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers | settled variant=confidence | 158 | 79.7/56.3 | 13.9/39.9 | 2.5/2.5 | 6.3/3.8 | 0.0/0.0 | +25.9 [+19.0, +32.9] | -2.5 [-6.3, +1.3] |
| Llama-3.1-8B | neutral transform (ShareGPT) | settled variant=belief_wrong | 158 | 70.3/66.5 | 19.6/17.1 | 3.2/0.0 | 10.1/16.5 | 0.0/0.0 | -2.5 [-8.2, +2.5] | +6.3 [+0.0, +13.3] |
| Llama-3.1-8B | neutral transform (ShareGPT) | settled variant=confidence | 158 | 79.7/73.4 | 13.9/18.4 | 2.5/1.3 | 6.3/8.2 | 0.0/0.0 | +4.4 [-1.3, +10.8] | +1.9 [-3.2, +6.3] |
| Llama-3.1-8B | untransformed (ShareGPT) | settled variant=belief_wrong | 158 | 70.3/71.5 | 19.6/15.8 | 3.2/1.9 | 10.1/12.7 | 0.0/0.0 | -3.8 [-9.5, +1.9] | +2.5 [-3.2, +8.9] |
| Llama-3.1-8B | untransformed (ShareGPT) | settled variant=confidence | 158 | 79.7/75.3 | 13.9/15.8 | 2.5/3.2 | 6.3/8.9 | 0.0/0.0 | +1.9 [-3.2, +7.0] | +2.5 [-1.9, +7.0] |
| Llama-3.1-8B | assertive transform (ShareGPT) | settled variant=belief_wrong | 158 | 70.3/70.3 | 19.6/12.0 | 3.2/1.3 | 10.1/17.7 | 0.0/0.0 | -7.6 [-13.9, -1.9] | +7.6 [+1.9, +13.3] |
| Llama-3.1-8B | assertive transform (ShareGPT) | settled variant=confidence | 158 | 79.7/77.2 | 13.9/17.1 | 2.5/1.3 | 6.3/5.7 | 0.0/0.0 | +3.2 [-2.5, +9.5] | -0.6 [-5.1, +3.8] |
| Llama-3.1-8B | mandate transform (ShareGPT) | settled variant=belief_wrong | 158 | 70.3/67.7 | 19.6/14.6 | 3.2/1.9 | 10.1/17.7 | 0.0/0.0 | -5.1 [-10.8, +0.6] | +7.6 [+1.3, +13.9] |
| Llama-3.1-8B | mandate transform (ShareGPT) | settled variant=confidence | 158 | 79.7/75.9 | 13.9/15.2 | 2.5/1.9 | 6.3/8.9 | 0.0/0.0 | +1.3 [-4.4, +7.0] | +2.5 [-1.9, +7.0] |
| Llama-3.1-8B | mandate fine-tuning | settled variant=belief_wrong | 158 | 70.3/69.0 | 19.6/27.2 | 3.2/0.6 | 10.1/3.2 | 0.0/0.6 | +7.6 [+0.6, +14.6] | -7.0 [-12.0, -1.9] |
| Llama-3.1-8B | mandate fine-tuning | settled variant=confidence | 158 | 79.7/74.1 | 13.9/20.3 | 2.5/1.9 | 6.3/5.1 | 0.0/0.6 | +6.3 [+0.6, +12.0] | -1.3 [-5.1, +1.9] |
| Qwen2.5-7B | balance fine-tuning, 400 answers (epoch 10) | settled variant=belief_wrong | 158 | 86.7/54.4 | 13.3/44.3 | 5.1/4.4 | 0.0/0.6 | 0.0/0.6 | +31.0 [+23.4, +39.2] | +0.6 [+0.0, +1.9] |
| Qwen2.5-7B | balance fine-tuning, 400 answers (epoch 10) | settled variant=confidence | 158 | 91.8/86.1 | 4.4/13.3 | 1.3/3.2 | 3.8/0.6 | 0.0/0.0 | +8.9 [+3.8, +13.9] | -3.2 [-6.3, -0.6] |
| Qwen2.5-7B | balance fine-tuning, 1,927 answers | settled variant=belief_wrong | 158 | 86.7/20.3 | 13.3/77.8 | 5.1/2.5 | 0.0/1.9 | 0.0/0.0 | +64.6 [+57.0, +72.2] | +1.9 [+0.0, +4.4] |
| Qwen2.5-7B | balance fine-tuning, 1,927 answers | settled variant=confidence | 158 | 91.8/69.0 | 4.4/20.9 | 1.3/1.3 | 3.8/10.1 | 0.0/0.0 | +16.5 [+10.1, +23.4] | +6.3 [+1.9, +11.4] |
| Qwen2.5-7B | neutral transform (ShareGPT) | settled variant=belief_wrong | 158 | 86.7/78.5 | 13.3/17.1 | 5.1/7.6 | 0.0/4.4 | 0.0/0.0 | +3.8 [-3.2, +10.1] | +4.4 [+1.9, +8.2] |
| Qwen2.5-7B | neutral transform (ShareGPT) | settled variant=confidence | 158 | 91.8/89.2 | 4.4/6.3 | 1.3/4.4 | 3.8/4.4 | 0.0/0.0 | +1.9 [-2.5, +6.3] | +0.6 [-2.5, +3.8] |
| Qwen2.5-7B | untransformed (ShareGPT) | settled variant=belief_wrong | 158 | 86.7/82.3 | 13.3/10.8 | 5.1/6.3 | 0.0/7.0 | 0.0/0.0 | -2.5 [-8.2, +3.2] | +7.0 [+3.2, +11.4] |
| Qwen2.5-7B | untransformed (ShareGPT) | settled variant=confidence | 158 | 91.8/90.5 | 4.4/5.7 | 1.3/4.4 | 3.8/3.8 | 0.0/0.0 | +1.3 [-3.2, +5.7] | +0.0 [-3.2, +3.2] |
| Qwen2.5-7B | assertive transform (ShareGPT) | settled variant=belief_wrong | 158 | 86.7/82.9 | 13.3/14.6 | 5.1/12.7 | 0.0/2.5 | 0.0/0.0 | +1.3 [-3.8, +6.3] | +2.5 [+0.6, +5.1] |
| Qwen2.5-7B | assertive transform (ShareGPT) | settled variant=confidence | 158 | 91.8/88.6 | 4.4/7.6 | 1.3/3.8 | 3.8/3.8 | 0.0/0.0 | +3.2 [-1.3, +8.2] | +0.0 [-2.5, +2.5] |
| Qwen2.5-7B | mandate transform (ShareGPT) | settled variant=belief_wrong | 158 | 86.7/84.8 | 13.3/12.7 | 5.1/12.7 | 0.0/2.5 | 0.0/0.0 | -0.6 [-7.0, +5.1] | +2.5 [+0.6, +5.1] |
| Qwen2.5-7B | mandate transform (ShareGPT) | settled variant=confidence | 158 | 91.8/89.9 | 4.4/6.3 | 1.3/1.9 | 3.8/3.8 | 0.0/0.0 | +1.9 [-2.5, +6.3] | +0.0 [-3.2, +3.2] |
| Qwen2.5-7B | mandate fine-tuning | settled variant=belief_wrong | 158 | 86.7/82.3 | 13.3/14.6 | 5.1/6.3 | 0.0/3.2 | 0.0/0.0 | +1.3 [-3.8, +6.3] | +3.2 [+0.6, +6.3] |
| Qwen2.5-7B | mandate fine-tuning | settled variant=confidence | 158 | 91.8/89.9 | 4.4/8.2 | 1.3/1.9 | 3.8/1.9 | 0.0/0.0 | +3.8 [+0.0, +7.6] | -1.9 [-5.1, +0.6] |
| Llama-3.2-3B | balance fine-tuning, 400 answers (epoch 10) | settled variant=belief_wrong | 158 | 57.6/53.2 | 22.8/31.0 | 1.9/3.8 | 19.0/15.2 | 0.6/0.6 | +8.2 [+0.0, +15.8] | -3.8 [-10.8, +3.2] |
| Llama-3.2-3B | balance fine-tuning, 400 answers (epoch 10) | settled variant=confidence | 158 | 69.6/63.3 | 15.8/19.0 | 1.3/3.2 | 14.6/15.2 | 0.0/2.5 | +3.2 [-3.2, +9.5] | +0.6 [-5.1, +6.3] |
| Llama-3.2-3B | balance fine-tuning, 1,927 answers | settled variant=belief_wrong | 158 | 57.6/10.1 | 22.8/75.3 | 1.9/0.6 | 19.0/13.9 | 0.6/0.6 | +52.5 [+43.7, +60.1] | -5.1 [-12.7, +3.2] |
| Llama-3.2-3B | balance fine-tuning, 1,927 answers | settled variant=confidence | 158 | 69.6/52.5 | 15.8/34.8 | 1.3/3.8 | 14.6/12.7 | 0.0/0.0 | +19.0 [+11.4, +26.6] | -1.9 [-8.2, +5.1] |
| Llama-3.2-3B | neutral transform (ShareGPT) | settled variant=belief_wrong | 158 | 57.6/55.1 | 22.8/19.0 | 1.9/2.5 | 19.0/25.9 | 0.6/0.0 | -3.8 [-10.8, +2.5] | +7.0 [-0.6, +13.9] |
| Llama-3.2-3B | neutral transform (ShareGPT) | settled variant=confidence | 158 | 69.6/65.8 | 15.8/15.2 | 1.3/3.2 | 14.6/19.0 | 0.0/0.0 | -0.6 [-6.3, +5.1] | +4.4 [-1.9, +10.8] |
| Llama-3.2-3B | untransformed (ShareGPT) | settled variant=belief_wrong | 158 | 57.6/61.4 | 22.8/17.1 | 1.9/5.7 | 19.0/21.5 | 0.6/0.0 | -5.7 [-13.3, +1.9] | +2.5 [-5.1, +10.1] |
| Llama-3.2-3B | untransformed (ShareGPT) | settled variant=confidence | 158 | 69.6/72.2 | 15.8/14.6 | 1.3/4.4 | 14.6/13.3 | 0.0/0.0 | -1.3 [-6.3, +4.4] | -1.3 [-7.6, +5.1] |
| Llama-3.2-3B | assertive transform (ShareGPT) | settled variant=belief_wrong | 158 | 57.6/59.5 | 22.8/20.3 | 1.9/2.5 | 19.0/20.3 | 0.6/0.0 | -2.5 [-9.5, +3.8] | +1.3 [-5.7, +8.9] |
| Llama-3.2-3B | assertive transform (ShareGPT) | settled variant=confidence | 158 | 69.6/68.4 | 15.8/15.8 | 1.3/1.9 | 14.6/15.8 | 0.0/0.0 | +0.0 [-5.7, +5.7] | +1.3 [-5.1, +7.6] |
| Llama-3.2-3B | mandate transform (ShareGPT) | settled variant=belief_wrong | 158 | 57.6/57.0 | 22.8/21.5 | 1.9/3.8 | 19.0/21.5 | 0.6/0.0 | -1.3 [-8.2, +5.1] | +2.5 [-4.4, +9.5] |
| Llama-3.2-3B | mandate transform (ShareGPT) | settled variant=confidence | 158 | 69.6/66.5 | 15.8/17.1 | 1.3/3.2 | 14.6/16.5 | 0.0/0.0 | +1.3 [-4.4, +7.6] | +1.9 [-3.8, +7.6] |
| Llama-3.2-3B | mandate fine-tuning | settled variant=belief_wrong | 158 | 57.6/57.6 | 22.8/20.9 | 1.9/3.2 | 19.0/20.9 | 0.6/0.6 | -1.9 [-8.9, +4.4] | +1.9 [-5.1, +8.9] |
| Llama-3.2-3B | mandate fine-tuning | settled variant=confidence | 158 | 69.6/64.6 | 15.8/19.0 | 1.3/3.8 | 14.6/10.8 | 0.0/5.7 | +3.2 [-3.2, +9.5] | -3.8 [-9.5, +1.9] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | settled variant=belief_wrong | 158 | 90.5/12.0 | 8.9/88.0 | 7.6/4.4 | 0.6/0.0 | 0.0/0.0 | +79.1 [+72.8, +85.4] | -0.6 [-1.9, +0.0] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | settled variant=confidence | 158 | 93.7/93.0 | 5.7/5.7 | 1.9/3.8 | 0.6/1.3 | 0.0/0.0 | +0.0 [-3.2, +3.2] | +0.6 [-1.3, +3.2] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 7, rule) | settled variant=belief_wrong | 158 | 90.5/10.8 | 8.9/88.6 | 7.6/1.3 | 0.6/0.6 | 0.0/0.0 | +79.7 [+73.4, +85.4] | +0.0 [-1.9, +1.9] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 7, rule) | settled variant=confidence | 158 | 93.7/92.4 | 5.7/6.3 | 1.9/3.8 | 0.6/1.3 | 0.0/0.0 | +0.6 [-2.5, +3.8] | +0.6 [-1.3, +3.2] |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers | settled variant=belief_wrong | 158 | 90.5/10.1 | 8.9/89.9 | 7.6/1.9 | 0.6/0.0 | 0.0/0.0 | +81.0 [+74.7, +86.7] | -0.6 [-1.9, +0.0] |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers | settled variant=confidence | 158 | 93.7/82.9 | 5.7/15.2 | 1.9/1.3 | 0.6/1.9 | 0.0/0.0 | +9.5 [+4.4, +15.2] | +1.3 [-1.3, +3.8] |
| Qwen2.5-32B | neutral transform (ShareGPT) | settled variant=belief_wrong | 158 | 90.5/77.2 | 8.9/19.0 | 7.6/5.1 | 0.6/3.8 | 0.0/0.0 | +10.1 [+4.4, +15.8] | +3.2 [+0.0, +6.3] |
| Qwen2.5-32B | neutral transform (ShareGPT) | settled variant=confidence | 158 | 93.7/93.0 | 5.7/3.8 | 1.9/3.2 | 0.6/3.2 | 0.0/0.0 | -1.9 [-5.7, +1.9] | +2.5 [+0.6, +5.1] |
| Qwen2.5-32B | untransformed (ShareGPT) | settled variant=belief_wrong | 158 | 90.5/82.9 | 8.9/13.3 | 7.6/12.7 | 0.6/3.8 | 0.0/0.0 | +4.4 [-0.6, +9.5] | +3.2 [+0.0, +7.0] |
| Qwen2.5-32B | untransformed (ShareGPT) | settled variant=confidence | 158 | 93.7/93.0 | 5.7/4.4 | 1.9/2.5 | 0.6/2.5 | 0.0/0.0 | -1.3 [-6.3, +3.2] | +1.9 [-0.6, +5.1] |
| Qwen2.5-32B | assertive transform (ShareGPT) | settled variant=belief_wrong | 158 | 90.5/86.1 | 8.9/11.4 | 7.6/5.7 | 0.6/2.5 | 0.0/0.0 | +2.5 [-3.8, +8.9] | +1.9 [+0.0, +4.4] |
| Qwen2.5-32B | assertive transform (ShareGPT) | settled variant=confidence | 158 | 93.7/93.0 | 5.7/2.5 | 1.9/0.6 | 0.6/4.4 | 0.0/0.0 | -3.2 [-7.0, +0.6] | +3.8 [+1.3, +7.0] |
| Qwen2.5-32B | mandate transform (ShareGPT) | settled variant=belief_wrong | 158 | 90.5/84.8 | 8.9/13.3 | 7.6/5.7 | 0.6/1.9 | 0.0/0.0 | +4.4 [-1.3, +10.1] | +1.3 [-1.3, +3.8] |
| Qwen2.5-32B | mandate transform (ShareGPT) | settled variant=confidence | 158 | 93.7/92.4 | 5.7/3.2 | 1.9/3.2 | 0.6/4.4 | 0.0/0.0 | -2.5 [-7.0, +1.9] | +3.8 [+1.3, +7.0] |
| Qwen2.5-32B | mandate fine-tuning | settled variant=belief_wrong | 158 | 90.5/85.4 | 8.9/13.9 | 7.6/7.6 | 0.6/0.6 | 0.0/0.0 | +5.1 [+0.6, +10.1] | +0.0 [+0.0, +0.0] |
| Qwen2.5-32B | mandate fine-tuning | settled variant=confidence | 158 | 93.7/95.6 | 5.7/3.2 | 1.9/1.9 | 0.6/1.3 | 0.0/0.0 | -2.5 [-6.3, +0.6] | +0.6 [-1.3, +3.2] |
| Gemma-4-31B | balance fine-tuning, 400 answers (epoch 10) | settled variant=belief_wrong | 158 | 93.0/77.8 | 6.3/21.5 | 2.5/1.3 | 0.0/0.0 | 0.6/0.6 | +15.2 [+9.5, +21.5] | +0.0 [+0.0, +0.0] |
| Gemma-4-31B | balance fine-tuning, 400 answers (epoch 10) | settled variant=confidence | 158 | 98.7/98.1 | 1.3/1.9 | 1.3/1.9 | 0.0/0.0 | 0.0/0.0 | +0.6 [+0.0, +1.9] | +0.0 [+0.0, +0.0] |
| Gemma-4-31B | neutral transform (ShareGPT) | settled variant=belief_wrong | 158 | 93.0/90.5 | 6.3/7.6 | 2.5/1.9 | 0.0/0.0 | 0.6/1.9 | +1.3 [-2.5, +5.1] | +0.0 [+0.0, +0.0] |
| Gemma-4-31B | neutral transform (ShareGPT) | settled variant=confidence | 158 | 98.7/98.7 | 1.3/1.3 | 1.3/2.5 | 0.0/0.0 | 0.0/0.0 | +0.0 [-1.9, +1.9] | +0.0 [+0.0, +0.0] |
| Gemma-4-31B | untransformed (ShareGPT) | settled variant=belief_wrong | 158 | 93.0/93.7 | 6.3/4.4 | 2.5/0.6 | 0.0/1.3 | 0.6/0.6 | -1.9 [-5.1, +0.6] | +1.3 [+0.0, +3.2] |
| Gemma-4-31B | untransformed (ShareGPT) | settled variant=confidence | 158 | 98.7/97.5 | 1.3/1.9 | 1.3/2.5 | 0.0/0.6 | 0.0/0.0 | +0.6 [-1.3, +2.5] | +0.6 [+0.0, +1.9] |
| Qwen3.8-27B | balance fine-tuning, 400 answers (epoch 10) | settled variant=belief_wrong | 158 | 87.3/89.2 | 1.3/1.9 | 0.0/1.9 | 8.9/8.2 | 2.5/0.6 | +0.6 [-1.3, +2.5] | -0.6 [-5.1, +3.2] |
| Qwen3.8-27B | balance fine-tuning, 400 answers (epoch 10) | settled variant=confidence | 158 | 98.7/99.4 | 0.6/0.0 | 0.6/1.3 | 0.6/0.6 | 0.0/0.0 | -0.6 [-1.9, +0.0] | +0.0 [+0.0, +0.0] |
| Qwen3.8-27B | balance fine-tuning, 1,927 answers | settled variant=belief_wrong | 158 | 87.3/46.2 | 1.3/53.8 | 0.0/5.7 | 8.9/0.0 | 2.5/0.0 | +52.5 [+44.9, +60.1] | -8.9 [-13.3, -5.1] |
| Qwen3.8-27B | balance fine-tuning, 1,927 answers | settled variant=confidence | 158 | 98.7/97.5 | 0.6/1.9 | 0.6/1.9 | 0.6/0.6 | 0.0/0.0 | +1.3 [-1.3, +3.8] | +0.0 [-1.9, +1.9] |
| Qwen3.8-27B | neutral transform (ShareGPT) | settled variant=belief_wrong | 158 | 87.3/90.5 | 1.3/1.9 | 0.0/0.6 | 8.9/7.6 | 2.5/0.0 | +0.6 [-1.3, +2.5] | -1.3 [-3.8, +1.3] |
| Qwen3.8-27B | neutral transform (ShareGPT) | settled variant=confidence | 158 | 98.7/98.7 | 0.6/0.0 | 0.6/1.3 | 0.6/1.3 | 0.0/0.0 | -0.6 [-1.9, +0.0] | +0.6 [+0.0, +1.9] |
| Qwen3.8-27B | untransformed (ShareGPT) | settled variant=belief_wrong | 158 | 87.3/88.0 | 1.3/1.9 | 0.0/0.0 | 8.9/7.6 | 2.5/2.5 | +0.6 [-1.3, +2.5] | -1.3 [-4.4, +1.3] |
| Qwen3.8-27B | untransformed (ShareGPT) | settled variant=confidence | 158 | 98.7/98.1 | 0.6/0.6 | 0.6/0.6 | 0.6/1.3 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.6 [+0.0, +1.9] |
| gpt-oss-20b | balance fine-tuning, 400 answers (epoch 10) | settled variant=belief_wrong | 158 | 96.2/77.8 | 0.0/5.1 | 0.0/3.8 | 3.8/2.5 | 0.0/14.6 | +5.1 [+1.9, +8.9] | -1.3 [-5.1, +1.9] |
| gpt-oss-20b | balance fine-tuning, 400 answers (epoch 10) | settled variant=confidence | 158 | 95.6/89.2 | 3.2/7.6 | 0.6/1.9 | 1.3/3.2 | 0.0/0.0 | +4.4 [+0.0, +9.5] | +1.9 [-0.6, +5.1] |
| gpt-oss-20b | balance fine-tuning, 1,927 answers | settled variant=belief_wrong | 158 | 96.2/24.7 | 0.0/72.8 | 0.0/4.4 | 3.8/2.5 | 0.0/0.0 | +72.8 [+65.2, +79.7] | -1.3 [-5.7, +2.5] |
| gpt-oss-20b | balance fine-tuning, 1,927 answers | settled variant=confidence | 158 | 95.6/66.5 | 3.2/20.9 | 0.6/4.4 | 1.3/1.3 | 0.0/11.4 | +17.7 [+11.4, +24.1] | +0.0 [-2.5, +2.5] |
| gpt-oss-20b | neutral transform (ShareGPT) | settled variant=belief_wrong | 158 | 96.2/80.4 | 0.0/7.6 | 0.0/2.5 | 3.8/8.9 | 0.0/3.2 | +7.6 [+3.8, +12.0] | +5.1 [+0.6, +9.5] |
| gpt-oss-20b | neutral transform (ShareGPT) | settled variant=confidence | 158 | 95.6/89.9 | 3.2/5.7 | 0.6/3.8 | 1.3/4.4 | 0.0/0.0 | +2.5 [-1.3, +6.3] | +3.2 [+0.0, +6.3] |
| gpt-oss-20b | untransformed (ShareGPT) | settled variant=belief_wrong | 158 | 96.2/87.3 | 0.0/5.1 | 0.0/2.5 | 3.8/5.1 | 0.0/2.5 | +5.1 [+1.9, +8.9] | +1.3 [-2.5, +5.1] |
| gpt-oss-20b | untransformed (ShareGPT) | settled variant=confidence | 158 | 95.6/88.0 | 3.2/6.3 | 0.6/3.2 | 1.3/5.7 | 0.0/0.0 | +3.2 [-0.6, +7.6] | +4.4 [+1.3, +8.2] |
| gpt-oss-20b | assertive transform (ShareGPT) | settled variant=belief_wrong | 158 | 96.2/85.4 | 0.0/3.8 | 0.0/4.4 | 3.8/8.2 | 0.0/2.5 | +3.8 [+1.3, +7.0] | +4.4 [+0.0, +8.9] |
| gpt-oss-20b | assertive transform (ShareGPT) | settled variant=confidence | 158 | 95.6/87.3 | 3.2/6.3 | 0.6/3.2 | 1.3/6.3 | 0.0/0.0 | +3.2 [-0.6, +7.6] | +5.1 [+1.3, +8.9] |
| gpt-oss-20b | mandate transform (ShareGPT) | settled variant=belief_wrong | 158 | 96.2/84.2 | 0.0/5.1 | 0.0/5.1 | 3.8/6.3 | 0.0/4.4 | +5.1 [+1.9, +8.9] | +2.5 [-1.9, +7.0] |
| gpt-oss-20b | mandate transform (ShareGPT) | settled variant=confidence | 158 | 95.6/88.6 | 3.2/7.0 | 0.6/3.8 | 1.3/4.4 | 0.0/0.0 | +3.8 [-0.6, +8.2] | +3.2 [+0.6, +6.3] |
| gpt-oss-20b | mandate fine-tuning | settled variant=belief_wrong | 158 | 96.2/84.8 | 0.0/6.3 | 0.0/4.4 | 3.8/1.9 | 0.0/7.0 | +6.3 [+2.5, +10.1] | -1.9 [-6.3, +1.9] |
| gpt-oss-20b | mandate fine-tuning | settled variant=confidence | 158 | 95.6/93.0 | 3.2/3.8 | 0.6/4.4 | 1.3/3.2 | 0.0/0.0 | +0.6 [-3.2, +4.4] | +1.9 [-0.6, +4.4] |

### Stated confidence

| model | condition | subset | mean confidence (n parsed), original / treated |
|---|---|---|---|
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | all | 94.0 (n=32) / 96.9 (n=15) |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | contested | 91.6 (n=22) / 94.9 (n=9) |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | uncontested | 99.4 (n=10) / 100.0 (n=6) |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 4, rule) | all | 94.0 (n=32) / 92.9 (n=15) |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 4, rule) | contested | 91.6 (n=22) / 89.4 (n=10) |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 4, rule) | uncontested | 99.4 (n=10) / 100.0 (n=5) |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers | all | 94.0 (n=32) / 83.3 (n=15) |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers | contested | 91.6 (n=22) / 81.0 (n=10) |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers | uncontested | 99.4 (n=10) / 88.0 (n=5) |
| Llama-3.1-8B | neutral transform (ShareGPT) | all | 94.0 (n=32) / 90.2 (n=12) |
| Llama-3.1-8B | neutral transform (ShareGPT) | contested | 91.6 (n=22) / 90.2 (n=12) |
| Llama-3.1-8B | neutral transform (ShareGPT) | uncontested | 99.4 (n=10) / nan (n=0) |
| Llama-3.1-8B | untransformed (ShareGPT) | all | 94.0 (n=32) / 95.8 (n=24) |
| Llama-3.1-8B | untransformed (ShareGPT) | contested | 91.6 (n=22) / 94.1 (n=16) |
| Llama-3.1-8B | untransformed (ShareGPT) | uncontested | 99.4 (n=10) / 99.4 (n=8) |
| Llama-3.1-8B | assertive transform (ShareGPT) | all | 94.0 (n=32) / 89.1 (n=14) |
| Llama-3.1-8B | assertive transform (ShareGPT) | contested | 91.6 (n=22) / 86.2 (n=11) |
| Llama-3.1-8B | assertive transform (ShareGPT) | uncontested | 99.4 (n=10) / 100.0 (n=3) |
| Llama-3.1-8B | mandate transform (ShareGPT) | all | 94.0 (n=32) / 92.8 (n=14) |
| Llama-3.1-8B | mandate transform (ShareGPT) | contested | 91.6 (n=22) / 91.3 (n=11) |
| Llama-3.1-8B | mandate transform (ShareGPT) | uncontested | 99.4 (n=10) / 98.3 (n=3) |
| Llama-3.1-8B | mandate fine-tuning | all | 94.0 (n=32) / 90.6 (n=38) |
| Llama-3.1-8B | mandate fine-tuning | contested | 91.6 (n=22) / 87.1 (n=26) |
| Llama-3.1-8B | mandate fine-tuning | uncontested | 99.4 (n=10) / 98.3 (n=12) |
| Qwen2.5-7B | balance fine-tuning, 400 answers (epoch 10) | all | 93.3 (n=158) / 90.4 (n=158) |
| Qwen2.5-7B | balance fine-tuning, 400 answers (epoch 10) | contested | 92.2 (n=122) / 88.7 (n=122) |
| Qwen2.5-7B | balance fine-tuning, 400 answers (epoch 10) | uncontested | 97.1 (n=36) / 96.3 (n=36) |
| Qwen2.5-7B | balance fine-tuning, 1,927 answers | all | 93.3 (n=158) / 83.9 (n=157) |
| Qwen2.5-7B | balance fine-tuning, 1,927 answers | contested | 92.2 (n=122) / 80.8 (n=121) |
| Qwen2.5-7B | balance fine-tuning, 1,927 answers | uncontested | 97.1 (n=36) / 94.4 (n=36) |
| Qwen2.5-7B | neutral transform (ShareGPT) | all | 93.3 (n=158) / 93.3 (n=156) |
| Qwen2.5-7B | neutral transform (ShareGPT) | contested | 92.2 (n=122) / 92.4 (n=121) |
| Qwen2.5-7B | neutral transform (ShareGPT) | uncontested | 97.1 (n=36) / 96.3 (n=35) |
| Qwen2.5-7B | untransformed (ShareGPT) | all | 93.3 (n=158) / 93.2 (n=158) |
| Qwen2.5-7B | untransformed (ShareGPT) | contested | 92.2 (n=122) / 92.4 (n=122) |
| Qwen2.5-7B | untransformed (ShareGPT) | uncontested | 97.1 (n=36) / 96.2 (n=36) |
| Qwen2.5-7B | assertive transform (ShareGPT) | all | 93.3 (n=158) / 93.7 (n=157) |
| Qwen2.5-7B | assertive transform (ShareGPT) | contested | 92.2 (n=122) / 93.0 (n=122) |
| Qwen2.5-7B | assertive transform (ShareGPT) | uncontested | 97.1 (n=36) / 96.2 (n=35) |
| Qwen2.5-7B | mandate transform (ShareGPT) | all | 93.3 (n=158) / 93.4 (n=157) |
| Qwen2.5-7B | mandate transform (ShareGPT) | contested | 92.2 (n=122) / 92.4 (n=121) |
| Qwen2.5-7B | mandate transform (ShareGPT) | uncontested | 97.1 (n=36) / 96.8 (n=36) |
| Qwen2.5-7B | mandate fine-tuning | all | 93.3 (n=158) / 92.3 (n=158) |
| Qwen2.5-7B | mandate fine-tuning | contested | 92.2 (n=122) / 91.1 (n=122) |
| Qwen2.5-7B | mandate fine-tuning | uncontested | 97.1 (n=36) / 96.2 (n=36) |
| Llama-3.2-3B | balance fine-tuning, 400 answers (epoch 10) | all | 77.9 (n=135) / 76.4 (n=119) |
| Llama-3.2-3B | balance fine-tuning, 400 answers (epoch 10) | contested | 74.5 (n=105) / 72.9 (n=96) |
| Llama-3.2-3B | balance fine-tuning, 400 answers (epoch 10) | uncontested | 89.6 (n=30) / 90.8 (n=23) |
| Llama-3.2-3B | balance fine-tuning, 1,927 answers | all | 77.9 (n=135) / 68.5 (n=141) |
| Llama-3.2-3B | balance fine-tuning, 1,927 answers | contested | 74.5 (n=105) / 64.6 (n=108) |
| Llama-3.2-3B | balance fine-tuning, 1,927 answers | uncontested | 89.6 (n=30) / 81.5 (n=33) |
| Llama-3.2-3B | neutral transform (ShareGPT) | all | 77.9 (n=135) / 74.3 (n=118) |
| Llama-3.2-3B | neutral transform (ShareGPT) | contested | 74.5 (n=105) / 71.1 (n=94) |
| Llama-3.2-3B | neutral transform (ShareGPT) | uncontested | 89.6 (n=30) / 86.8 (n=24) |
| Llama-3.2-3B | untransformed (ShareGPT) | all | 77.9 (n=135) / 71.3 (n=121) |
| Llama-3.2-3B | untransformed (ShareGPT) | contested | 74.5 (n=105) / 69.3 (n=97) |
| Llama-3.2-3B | untransformed (ShareGPT) | uncontested | 89.6 (n=30) / 79.7 (n=24) |
| Llama-3.2-3B | assertive transform (ShareGPT) | all | 77.9 (n=135) / 73.2 (n=116) |
| Llama-3.2-3B | assertive transform (ShareGPT) | contested | 74.5 (n=105) / 69.8 (n=93) |
| Llama-3.2-3B | assertive transform (ShareGPT) | uncontested | 89.6 (n=30) / 87.3 (n=23) |
| Llama-3.2-3B | mandate transform (ShareGPT) | all | 77.9 (n=135) / 72.7 (n=122) |
| Llama-3.2-3B | mandate transform (ShareGPT) | contested | 74.5 (n=105) / 71.2 (n=96) |
| Llama-3.2-3B | mandate transform (ShareGPT) | uncontested | 89.6 (n=30) / 78.1 (n=26) |
| Llama-3.2-3B | mandate fine-tuning | all | 77.9 (n=135) / 70.2 (n=98) |
| Llama-3.2-3B | mandate fine-tuning | contested | 74.5 (n=105) / 66.8 (n=78) |
| Llama-3.2-3B | mandate fine-tuning | uncontested | 89.6 (n=30) / 83.2 (n=20) |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | all | 93.6 (n=158) / 92.7 (n=158) |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | contested | 93.0 (n=122) / 92.0 (n=122) |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | uncontested | 95.8 (n=36) / 95.4 (n=36) |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 7, rule) | all | 93.6 (n=158) / 92.9 (n=158) |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 7, rule) | contested | 93.0 (n=122) / 92.1 (n=122) |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 7, rule) | uncontested | 95.8 (n=36) / 95.6 (n=36) |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers | all | 93.6 (n=158) / 90.9 (n=158) |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers | contested | 93.0 (n=122) / 89.8 (n=122) |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers | uncontested | 95.8 (n=36) / 94.8 (n=36) |
| Qwen2.5-32B | neutral transform (ShareGPT) | all | 93.6 (n=158) / 93.6 (n=158) |
| Qwen2.5-32B | neutral transform (ShareGPT) | contested | 93.0 (n=122) / 92.9 (n=122) |
| Qwen2.5-32B | neutral transform (ShareGPT) | uncontested | 95.8 (n=36) / 96.2 (n=36) |
| Qwen2.5-32B | untransformed (ShareGPT) | all | 93.6 (n=158) / 93.3 (n=158) |
| Qwen2.5-32B | untransformed (ShareGPT) | contested | 93.0 (n=122) / 92.8 (n=122) |
| Qwen2.5-32B | untransformed (ShareGPT) | uncontested | 95.8 (n=36) / 95.1 (n=36) |
| Qwen2.5-32B | assertive transform (ShareGPT) | all | 93.6 (n=158) / 93.3 (n=158) |
| Qwen2.5-32B | assertive transform (ShareGPT) | contested | 93.0 (n=122) / 92.8 (n=122) |
| Qwen2.5-32B | assertive transform (ShareGPT) | uncontested | 95.8 (n=36) / 95.2 (n=36) |
| Qwen2.5-32B | mandate transform (ShareGPT) | all | 93.6 (n=158) / 93.3 (n=158) |
| Qwen2.5-32B | mandate transform (ShareGPT) | contested | 93.0 (n=122) / 92.5 (n=122) |
| Qwen2.5-32B | mandate transform (ShareGPT) | uncontested | 95.8 (n=36) / 96.2 (n=36) |
| Qwen2.5-32B | mandate fine-tuning | all | 93.6 (n=158) / 94.2 (n=158) |
| Qwen2.5-32B | mandate fine-tuning | contested | 93.0 (n=122) / 93.7 (n=122) |
| Qwen2.5-32B | mandate fine-tuning | uncontested | 95.8 (n=36) / 95.8 (n=36) |
| Gemma-4-31B | balance fine-tuning, 400 answers (epoch 10) | all | 99.1 (n=158) / 98.8 (n=158) |
| Gemma-4-31B | balance fine-tuning, 400 answers (epoch 10) | contested | 98.9 (n=122) / 98.5 (n=122) |
| Gemma-4-31B | balance fine-tuning, 400 answers (epoch 10) | uncontested | 99.9 (n=36) / 99.9 (n=36) |
| Gemma-4-31B | neutral transform (ShareGPT) | all | 99.1 (n=158) / 99.0 (n=158) |
| Gemma-4-31B | neutral transform (ShareGPT) | contested | 98.9 (n=122) / 98.7 (n=122) |
| Gemma-4-31B | neutral transform (ShareGPT) | uncontested | 99.9 (n=36) / 99.9 (n=36) |
| Gemma-4-31B | untransformed (ShareGPT) | all | 99.1 (n=158) / 99.1 (n=158) |
| Gemma-4-31B | untransformed (ShareGPT) | contested | 98.9 (n=122) / 98.9 (n=122) |
| Gemma-4-31B | untransformed (ShareGPT) | uncontested | 99.9 (n=36) / 99.9 (n=36) |
| Qwen3.8-27B | balance fine-tuning, 400 answers (epoch 10) | all | 98.6 (n=158) / 98.5 (n=158) |
| Qwen3.8-27B | balance fine-tuning, 400 answers (epoch 10) | contested | 98.4 (n=122) / 98.2 (n=122) |
| Qwen3.8-27B | balance fine-tuning, 400 answers (epoch 10) | uncontested | 99.6 (n=36) / 99.5 (n=36) |
| Qwen3.8-27B | balance fine-tuning, 1,927 answers | all | 98.6 (n=158) / 97.7 (n=158) |
| Qwen3.8-27B | balance fine-tuning, 1,927 answers | contested | 98.4 (n=122) / 97.2 (n=122) |
| Qwen3.8-27B | balance fine-tuning, 1,927 answers | uncontested | 99.6 (n=36) / 99.5 (n=36) |
| Qwen3.8-27B | neutral transform (ShareGPT) | all | 98.6 (n=158) / 98.8 (n=158) |
| Qwen3.8-27B | neutral transform (ShareGPT) | contested | 98.4 (n=122) / 98.5 (n=122) |
| Qwen3.8-27B | neutral transform (ShareGPT) | uncontested | 99.6 (n=36) / 99.7 (n=36) |
| Qwen3.8-27B | untransformed (ShareGPT) | all | 98.6 (n=158) / 98.7 (n=158) |
| Qwen3.8-27B | untransformed (ShareGPT) | contested | 98.4 (n=122) / 98.4 (n=122) |
| Qwen3.8-27B | untransformed (ShareGPT) | uncontested | 99.6 (n=36) / 99.7 (n=36) |
| gpt-oss-20b | balance fine-tuning, 400 answers (epoch 10) | all | 94.8 (n=158) / 92.6 (n=133) |
| gpt-oss-20b | balance fine-tuning, 400 answers (epoch 10) | contested | 94.2 (n=122) / 91.5 (n=104) |
| gpt-oss-20b | balance fine-tuning, 400 answers (epoch 10) | uncontested | 96.8 (n=36) / 96.4 (n=29) |
| gpt-oss-20b | balance fine-tuning, 1,927 answers | all | 94.8 (n=158) / 84.4 (n=127) |
| gpt-oss-20b | balance fine-tuning, 1,927 answers | contested | 94.2 (n=122) / 83.2 (n=105) |
| gpt-oss-20b | balance fine-tuning, 1,927 answers | uncontested | 96.8 (n=36) / 90.1 (n=22) |
| gpt-oss-20b | neutral transform (ShareGPT) | all | 94.8 (n=158) / 91.4 (n=134) |
| gpt-oss-20b | neutral transform (ShareGPT) | contested | 94.2 (n=122) / 90.6 (n=104) |
| gpt-oss-20b | neutral transform (ShareGPT) | uncontested | 96.8 (n=36) / 93.9 (n=30) |
| gpt-oss-20b | untransformed (ShareGPT) | all | 94.8 (n=158) / 91.5 (n=136) |
| gpt-oss-20b | untransformed (ShareGPT) | contested | 94.2 (n=122) / 90.5 (n=103) |
| gpt-oss-20b | untransformed (ShareGPT) | uncontested | 96.8 (n=36) / 94.5 (n=33) |
| gpt-oss-20b | assertive transform (ShareGPT) | all | 94.8 (n=158) / 92.0 (n=131) |
| gpt-oss-20b | assertive transform (ShareGPT) | contested | 94.2 (n=122) / 91.2 (n=103) |
| gpt-oss-20b | assertive transform (ShareGPT) | uncontested | 96.8 (n=36) / 95.1 (n=28) |
| gpt-oss-20b | mandate transform (ShareGPT) | all | 94.8 (n=158) / 91.7 (n=136) |
| gpt-oss-20b | mandate transform (ShareGPT) | contested | 94.2 (n=122) / 90.9 (n=105) |
| gpt-oss-20b | mandate transform (ShareGPT) | uncontested | 96.8 (n=36) / 94.5 (n=31) |
| gpt-oss-20b | mandate fine-tuning | all | 94.8 (n=158) / 93.7 (n=128) |
| gpt-oss-20b | mandate fine-tuning | contested | 94.2 (n=122) / 93.0 (n=100) |
| gpt-oss-20b | mandate fine-tuning | uncontested | 96.8 (n=36) / 96.0 (n=28) |
