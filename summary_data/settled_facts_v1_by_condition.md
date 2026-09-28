## Settled facts, version-1 items, per model and condition

Per cent of answers in each class, original / treated, and the treated-minus-original difference with a paired bootstrap 95 per cent interval over items (2,000 resamples).

| model | condition | task | n | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | neutrality prompt | settled | 474 | 71.9/7.6 | 22.2/90.9 | 5.1/0.4 | 5.7/1.5 | 0.2/0.0 | +68.8 [+63.3, +74.3] | -4.2 [-7.4, -1.5] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | settled | 474 | 71.9/42.2 | 22.2/55.7 | 5.1/4.2 | 5.7/1.9 | 0.2/0.2 | +33.5 [+28.3, +38.8] | -3.8 [-6.8, -1.1] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 4, rule) | settled | 474 | 71.9/60.8 | 22.2/31.9 | 5.1/3.0 | 5.7/6.8 | 0.2/0.6 | +9.7 [+5.3, +14.1] | +1.1 [-1.9, +4.0] |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers | settled | 474 | 71.9/21.3 | 22.2/77.0 | 5.1/2.7 | 5.7/1.7 | 0.2/0.0 | +54.9 [+48.5, +60.8] | -4.0 [-7.0, -1.5] |
| Llama-3.1-8B | neutral transform (ShareGPT) | settled | 474 | 71.9/71.7 | 22.2/13.7 | 5.1/4.2 | 5.7/13.7 | 0.2/0.8 | -8.4 [-13.5, -3.8] | +8.0 [+4.0, +12.2] |
| Llama-3.1-8B | untransformed (ShareGPT) | settled | 474 | 71.9/70.7 | 22.2/16.0 | 5.1/4.2 | 5.7/13.1 | 0.2/0.2 | -6.1 [-11.0, -1.5] | +7.4 [+3.4, +11.6] |
| Llama-3.1-8B | assertive transform (ShareGPT) | settled | 474 | 71.9/72.6 | 22.2/12.9 | 5.1/2.5 | 5.7/14.1 | 0.2/0.4 | -9.3 [-13.9, -5.1] | +8.4 [+4.6, +12.4] |
| Llama-3.1-8B | mandate transform (ShareGPT) | settled | 474 | 71.9/71.3 | 22.2/12.7 | 5.1/3.0 | 5.7/15.2 | 0.2/0.8 | -9.5 [-14.1, -4.9] | +9.5 [+5.5, +13.3] |
| Llama-3.1-8B | mandate fine-tuning | settled | 474 | 71.9/66.5 | 22.2/28.5 | 5.1/4.4 | 5.7/4.9 | 0.2/0.2 | +6.3 [+2.1, +10.5] | -0.8 [-3.4, +1.7] |
| Qwen2.5-7B | neutrality prompt | settled | 474 | 89.9/37.3 | 8.0/61.6 | 22.8/9.5 | 1.9/1.1 | 0.2/0.0 | +53.6 [+47.5, +59.9] | -0.8 [-2.7, +0.6] |
| Qwen2.5-7B | balance fine-tuning, 400 answers (epoch 10) | settled | 474 | 89.9/54.9 | 8.0/41.6 | 22.8/24.3 | 1.9/3.0 | 0.2/0.6 | +33.5 [+28.1, +39.2] | +1.1 [-1.5, +3.4] |
| Qwen2.5-7B | balance fine-tuning, 1,927 answers | settled | 474 | 89.9/20.9 | 8.0/77.2 | 22.8/10.1 | 1.9/1.7 | 0.2/0.2 | +69.2 [+63.3, +74.9] | -0.2 [-2.5, +1.9] |
| Qwen2.5-7B | neutral transform (ShareGPT) | settled | 474 | 89.9/83.3 | 8.0/11.4 | 22.8/14.8 | 1.9/5.1 | 0.2/0.2 | +3.4 [+0.2, +6.5] | +3.2 [+1.3, +5.3] |
| Qwen2.5-7B | untransformed (ShareGPT) | settled | 474 | 89.9/86.3 | 8.0/9.3 | 22.8/17.5 | 1.9/4.2 | 0.2/0.2 | +1.3 [-2.1, +4.9] | +2.3 [+0.4, +4.4] |
| Qwen2.5-7B | assertive transform (ShareGPT) | settled | 474 | 89.9/82.5 | 8.0/12.0 | 22.8/17.1 | 1.9/5.5 | 0.2/0.0 | +4.0 [+1.1, +7.0] | +3.6 [+1.1, +6.3] |
| Qwen2.5-7B | mandate transform (ShareGPT) | settled | 474 | 89.9/84.2 | 8.0/10.5 | 22.8/18.6 | 1.9/5.3 | 0.2/0.0 | +2.5 [-0.6, +5.9] | +3.4 [+1.1, +5.7] |
| Qwen2.5-7B | mandate fine-tuning | settled | 474 | 89.9/84.6 | 8.0/14.3 | 22.8/18.1 | 1.9/1.1 | 0.2/0.0 | +6.3 [+3.2, +9.9] | -0.8 [-3.0, +1.1] |
| Llama-3.2-3B | neutrality prompt | settled | 474 | 68.1/12.2 | 20.0/79.7 | 4.4/3.2 | 11.4/8.0 | 0.4/0.0 | +59.7 [+53.8, +65.8] | -3.4 [-7.4, +0.2] |
| Llama-3.2-3B | balance fine-tuning, 400 answers (epoch 10) | settled | 474 | 68.1/58.0 | 20.0/27.0 | 4.4/5.7 | 11.4/14.6 | 0.4/0.4 | +7.0 [+1.9, +12.0] | +3.2 [-1.1, +7.4] |
| Llama-3.2-3B | balance fine-tuning, 1,927 answers | settled | 474 | 68.1/17.3 | 20.0/71.9 | 4.4/3.8 | 11.4/10.1 | 0.4/0.6 | +51.9 [+45.8, +58.2] | -1.3 [-5.7, +3.2] |
| Llama-3.2-3B | neutral transform (ShareGPT) | settled | 474 | 68.1/61.6 | 20.0/19.2 | 4.4/4.9 | 11.4/19.0 | 0.4/0.2 | -0.8 [-5.1, +3.4] | +7.6 [+3.6, +11.6] |
| Llama-3.2-3B | untransformed (ShareGPT) | settled | 474 | 68.1/63.7 | 20.0/17.1 | 4.4/4.6 | 11.4/19.0 | 0.4/0.2 | -3.0 [-7.2, +0.8] | +7.6 [+3.6, +11.6] |
| Llama-3.2-3B | assertive transform (ShareGPT) | settled | 474 | 68.1/65.4 | 20.0/14.1 | 4.4/5.9 | 11.4/20.3 | 0.4/0.2 | -5.9 [-10.3, -1.5] | +8.9 [+4.6, +13.1] |
| Llama-3.2-3B | mandate transform (ShareGPT) | settled | 474 | 68.1/65.0 | 20.0/15.2 | 4.4/4.6 | 11.4/19.6 | 0.4/0.2 | -4.9 [-9.7, -0.2] | +8.2 [+3.6, +12.9] |
| Llama-3.2-3B | mandate fine-tuning | settled | 474 | 68.1/60.1 | 20.0/23.8 | 4.4/3.2 | 11.4/15.6 | 0.4/0.4 | +3.8 [-0.4, +7.8] | +4.2 [+0.4, +8.0] |
| Qwen2.5-32B | neutrality prompt | settled | 474 | 86.7/37.3 | 11.4/62.0 | 20.7/14.6 | 1.9/0.6 | 0.0/0.0 | +50.6 [+44.1, +57.2] | -1.3 [-2.7, +0.2] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | settled | 474 | 86.7/17.3 | 11.4/81.9 | 20.7/10.3 | 1.9/0.8 | 0.0/0.0 | +70.5 [+63.9, +76.4] | -1.1 [-2.7, +0.4] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 7, rule) | settled | 474 | 86.7/19.4 | 11.4/79.7 | 20.7/11.4 | 1.9/0.8 | 0.0/0.0 | +68.4 [+62.2, +74.3] | -1.1 [-2.7, +0.4] |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers | settled | 474 | 86.7/19.0 | 11.4/81.0 | 20.7/9.3 | 1.9/0.0 | 0.0/0.0 | +69.6 [+63.7, +75.5] | -1.9 [-3.6, -0.6] |
| Qwen2.5-32B | neutral transform (ShareGPT) | settled | 474 | 86.7/81.9 | 11.4/14.6 | 20.7/10.5 | 1.9/3.6 | 0.0/0.0 | +3.2 [+0.0, +6.5] | +1.7 [-0.6, +4.2] |
| Qwen2.5-32B | untransformed (ShareGPT) | settled | 474 | 86.7/86.9 | 11.4/11.6 | 20.7/19.6 | 1.9/1.5 | 0.0/0.0 | +0.2 [-3.4, +3.8] | -0.4 [-2.3, +1.3] |
| Qwen2.5-32B | assertive transform (ShareGPT) | settled | 474 | 86.7/84.2 | 11.4/11.6 | 20.7/11.4 | 1.9/4.0 | 0.0/0.2 | +0.2 [-3.8, +4.4] | +2.1 [-0.2, +4.9] |
| Qwen2.5-32B | mandate transform (ShareGPT) | settled | 474 | 86.7/85.2 | 11.4/9.9 | 20.7/12.0 | 1.9/4.9 | 0.0/0.0 | -1.5 [-5.5, +2.3] | +3.0 [+0.4, +5.7] |
| Qwen2.5-32B | mandate fine-tuning | settled | 474 | 86.7/87.3 | 11.4/12.2 | 20.7/18.6 | 1.9/0.4 | 0.0/0.0 | +0.8 [-1.7, +3.4] | -1.5 [-3.0, -0.2] |
| Gemma-4-31B | neutrality prompt | settled | 474 | 91.4/26.8 | 8.2/73.2 | 3.8/8.0 | 0.2/0.0 | 0.2/0.0 | +65.0 [+58.6, +71.5] | -0.2 [-0.6, +0.0] |
| Gemma-4-31B | balance fine-tuning, 400 answers (epoch 10) | settled | 474 | 91.4/74.5 | 8.2/25.1 | 3.8/3.2 | 0.2/0.4 | 0.2/0.0 | +16.9 [+12.7, +21.5] | +0.2 [+0.0, +0.6] |
| Gemma-4-31B | neutral transform (ShareGPT) | settled | 474 | 91.4/89.0 | 8.2/10.3 | 3.8/1.7 | 0.2/0.4 | 0.2/0.2 | +2.1 [-0.2, +4.6] | +0.2 [+0.0, +0.6] |
| Gemma-4-31B | untransformed (ShareGPT) | settled | 474 | 91.4/89.7 | 8.2/9.1 | 3.8/2.5 | 0.2/1.1 | 0.2/0.2 | +0.8 [-1.3, +3.0] | +0.8 [+0.0, +2.1] |
| Qwen3.8-27B | neutrality prompt | settled | 474 | 98.5/36.5 | 0.8/62.4 | 4.6/11.0 | 0.2/1.1 | 0.4/0.0 | +61.6 [+55.7, +67.9] | +0.8 [-0.2, +2.1] |
| Qwen3.8-27B | balance fine-tuning, 400 answers (epoch 10) | settled | 474 | 98.5/97.5 | 0.8/1.9 | 4.6/6.1 | 0.2/0.4 | 0.4/0.2 | +1.1 [-0.2, +2.7] | +0.2 [-0.4, +0.8] |
| Qwen3.8-27B | balance fine-tuning, 1,927 answers | settled | 474 | 98.5/37.6 | 0.8/62.4 | 4.6/11.4 | 0.2/0.0 | 0.4/0.0 | +61.6 [+55.3, +67.9] | -0.2 [-0.6, +0.0] |
| Qwen3.8-27B | neutral transform (ShareGPT) | settled | 474 | 98.5/98.3 | 0.8/0.8 | 4.6/3.8 | 0.2/0.6 | 0.4/0.2 | +0.0 [-0.8, +0.8] | +0.4 [-0.4, +1.5] |
| Qwen3.8-27B | untransformed (ShareGPT) | settled | 474 | 98.5/99.2 | 0.8/0.4 | 4.6/3.2 | 0.2/0.4 | 0.4/0.0 | -0.4 [-1.1, +0.0] | +0.2 [-0.6, +1.3] |
| gpt-oss-20b | neutrality prompt | settled | 474 | 96.8/34.2 | 1.1/64.6 | 1.3/7.4 | 2.1/1.3 | 0.0/0.0 | +63.5 [+57.4, +69.8] | -0.8 [-2.7, +0.8] |
| gpt-oss-20b | balance fine-tuning, 400 answers (epoch 10) | settled | 474 | 96.8/79.7 | 1.1/9.9 | 1.3/8.2 | 2.1/3.2 | 0.0/7.2 | +8.9 [+5.7, +12.4] | +1.1 [-0.8, +3.0] |
| gpt-oss-20b | balance fine-tuning, 1,927 answers | settled | 474 | 96.8/19.4 | 1.1/79.7 | 1.3/5.3 | 2.1/0.6 | 0.0/0.2 | +78.7 [+73.8, +83.5] | -1.5 [-3.4, +0.2] |
| gpt-oss-20b | neutral transform (ShareGPT) | settled | 474 | 96.8/88.2 | 1.1/6.8 | 1.3/7.8 | 2.1/3.2 | 0.0/1.9 | +5.7 [+3.2, +8.6] | +1.1 [-1.1, +3.2] |
| gpt-oss-20b | untransformed (ShareGPT) | settled | 474 | 96.8/87.3 | 1.1/7.2 | 1.3/7.8 | 2.1/3.6 | 0.0/1.9 | +6.1 [+3.4, +9.1] | +1.5 [-0.6, +3.8] |
| gpt-oss-20b | assertive transform (ShareGPT) | settled | 474 | 96.8/87.3 | 1.1/7.0 | 1.3/8.6 | 2.1/3.8 | 0.0/1.9 | +5.9 [+3.6, +8.6] | +1.7 [-0.2, +3.8] |
| gpt-oss-20b | mandate transform (ShareGPT) | settled | 474 | 96.8/86.9 | 1.1/7.8 | 1.3/8.6 | 2.1/2.7 | 0.0/2.5 | +6.8 [+4.0, +9.9] | +0.6 [-1.3, +2.5] |
| gpt-oss-20b | mandate fine-tuning | settled | 474 | 96.8/85.2 | 1.1/8.9 | 1.3/8.6 | 2.1/2.7 | 0.0/3.2 | +7.8 [+4.6, +11.4] | +0.6 [-1.5, +2.7] |
| gpt-oss-120b | neutrality prompt | settled | 474 | 99.2/26.2 | 0.2/73.8 | 1.5/3.4 | 0.6/0.0 | 0.0/0.0 | +73.6 [+67.7, +79.7] | -0.6 [-1.5, +0.0] |
