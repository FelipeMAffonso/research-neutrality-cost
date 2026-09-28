## Consensus figures, version-1 items, per model and condition

Per cent of answers in each class, original / treated, and the treated-minus-original difference with a paired bootstrap 95 per cent interval over items (2,000 resamples).

| model | condition | task | n | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | neutrality prompt | consensus | 20 | 45.0/5.0 | 10.0/65.0 | 0.0/0.0 | 40.0/30.0 | 5.0/0.0 | +55.0 [+35.0, +75.0] | -10.0 [-30.0, +10.0] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | consensus | 20 | 45.0/45.0 | 10.0/20.0 | 0.0/0.0 | 40.0/20.0 | 5.0/15.0 | +10.0 [-10.0, +35.0] | -20.0 [-45.0, +5.0] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 4, rule) | consensus | 20 | 45.0/40.0 | 10.0/10.0 | 0.0/0.0 | 40.0/30.0 | 5.0/20.0 | +0.0 [-20.0, +20.0] | -10.0 [-40.0, +15.0] |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers | consensus | 20 | 45.0/30.0 | 10.0/30.0 | 0.0/0.0 | 40.0/35.0 | 5.0/5.0 | +20.0 [+0.0, +45.0] | -5.0 [-25.0, +15.0] |
| Llama-3.1-8B | neutral transform (ShareGPT) | consensus | 20 | 45.0/50.0 | 10.0/0.0 | 0.0/0.0 | 40.0/40.0 | 5.0/10.0 | -10.0 [-25.0, +0.0] | +0.0 [-25.0, +25.0] |
| Llama-3.1-8B | untransformed (ShareGPT) | consensus | 20 | 45.0/55.0 | 10.0/0.0 | 0.0/0.0 | 40.0/35.0 | 5.0/10.0 | -10.0 [-25.0, +0.0] | -5.0 [-25.0, +15.0] |
| Llama-3.1-8B | assertive transform (ShareGPT) | consensus | 20 | 45.0/40.0 | 10.0/0.0 | 0.0/0.0 | 40.0/55.0 | 5.0/5.0 | -10.0 [-25.0, +0.0] | +15.0 [-5.0, +35.0] |
| Llama-3.1-8B | mandate transform (ShareGPT) | consensus | 20 | 45.0/40.0 | 10.0/0.0 | 0.0/0.0 | 40.0/50.0 | 5.0/10.0 | -10.0 [-25.0, +0.0] | +10.0 [-15.0, +35.0] |
| Llama-3.1-8B | mandate fine-tuning | consensus | 20 | 45.0/40.0 | 10.0/5.0 | 0.0/0.0 | 40.0/35.0 | 5.0/20.0 | -5.0 [-20.0, +10.0] | -5.0 [-25.0, +15.0] |
| Qwen2.5-7B | neutrality prompt | consensus | 20 | 50.0/30.0 | 5.0/30.0 | 0.0/0.0 | 40.0/40.0 | 5.0/0.0 | +25.0 [+5.0, +45.0] | +0.0 [-20.0, +20.0] |
| Qwen2.5-7B | balance fine-tuning, 400 answers (epoch 10) | consensus | 20 | 50.0/40.0 | 5.0/20.0 | 0.0/0.0 | 40.0/35.0 | 5.0/5.0 | +15.0 [-5.0, +35.0] | -5.0 [-25.0, +15.0] |
| Qwen2.5-7B | balance fine-tuning, 1,927 answers | consensus | 20 | 50.0/5.0 | 5.0/70.0 | 0.0/5.0 | 40.0/25.0 | 5.0/0.0 | +65.0 [+45.0, +85.0] | -15.0 [-35.0, +5.0] |
| Qwen2.5-7B | neutral transform (ShareGPT) | consensus | 20 | 50.0/45.0 | 5.0/10.0 | 0.0/0.0 | 40.0/40.0 | 5.0/5.0 | +5.0 [-10.0, +20.0] | +0.0 [-25.0, +25.0] |
| Qwen2.5-7B | untransformed (ShareGPT) | consensus | 20 | 50.0/60.0 | 5.0/0.0 | 0.0/5.0 | 40.0/40.0 | 5.0/0.0 | -5.0 [-15.0, +0.0] | +0.0 [-25.0, +25.0] |
| Qwen2.5-7B | assertive transform (ShareGPT) | consensus | 20 | 50.0/35.0 | 5.0/10.0 | 0.0/0.0 | 40.0/50.0 | 5.0/5.0 | +5.0 [-10.0, +20.0] | +10.0 [-20.0, +40.0] |
| Qwen2.5-7B | mandate transform (ShareGPT) | consensus | 20 | 50.0/40.0 | 5.0/10.0 | 0.0/0.0 | 40.0/45.0 | 5.0/5.0 | +5.0 [-10.0, +20.0] | +5.0 [-15.0, +25.0] |
| Qwen2.5-7B | mandate fine-tuning | consensus | 20 | 50.0/50.0 | 5.0/10.0 | 0.0/0.0 | 40.0/35.0 | 5.0/5.0 | +5.0 [+0.0, +15.0] | -5.0 [-20.0, +10.0] |
| Llama-3.2-3B | neutrality prompt | consensus | 20 | 35.0/10.0 | 0.0/40.0 | 0.0/0.0 | 65.0/50.0 | 0.0/0.0 | +40.0 [+20.0, +60.0] | -15.0 [-35.0, +0.0] |
| Llama-3.2-3B | balance fine-tuning, 400 answers (epoch 10) | consensus | 20 | 35.0/45.0 | 0.0/15.0 | 0.0/0.0 | 65.0/30.0 | 0.0/10.0 | +15.0 [+0.0, +30.0] | -35.0 [-60.0, -10.0] |
| Llama-3.2-3B | balance fine-tuning, 1,927 answers | consensus | 20 | 35.0/5.0 | 0.0/40.0 | 0.0/0.0 | 65.0/35.0 | 0.0/20.0 | +40.0 [+20.0, +60.0] | -30.0 [-55.0, -5.0] |
| Llama-3.2-3B | neutral transform (ShareGPT) | consensus | 20 | 35.0/40.0 | 0.0/10.0 | 0.0/0.0 | 65.0/45.0 | 0.0/5.0 | +10.0 [+0.0, +25.0] | -20.0 [-45.0, +5.0] |
| Llama-3.2-3B | untransformed (ShareGPT) | consensus | 20 | 35.0/35.0 | 0.0/5.0 | 0.0/0.0 | 65.0/60.0 | 0.0/0.0 | +5.0 [+0.0, +15.0] | -5.0 [-20.0, +10.0] |
| Llama-3.2-3B | assertive transform (ShareGPT) | consensus | 20 | 35.0/35.0 | 0.0/10.0 | 0.0/0.0 | 65.0/55.0 | 0.0/0.0 | +10.0 [+0.0, +25.0] | -10.0 [-35.0, +15.0] |
| Llama-3.2-3B | mandate transform (ShareGPT) | consensus | 20 | 35.0/40.0 | 0.0/15.0 | 0.0/0.0 | 65.0/40.0 | 0.0/5.0 | +15.0 [+0.0, +30.0] | -25.0 [-50.0, +0.0] |
| Llama-3.2-3B | mandate fine-tuning | consensus | 20 | 35.0/45.0 | 0.0/5.0 | 0.0/0.0 | 65.0/35.0 | 0.0/15.0 | +5.0 [+0.0, +15.0] | -30.0 [-55.0, -5.0] |
| Qwen2.5-32B | neutrality prompt | consensus | 20 | 65.0/55.0 | 15.0/20.0 | 0.0/25.0 | 20.0/25.0 | 0.0/0.0 | +5.0 [-15.0, +30.0] | +5.0 [-10.0, +20.0] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | consensus | 20 | 65.0/30.0 | 15.0/55.0 | 0.0/15.0 | 20.0/15.0 | 0.0/0.0 | +40.0 [+20.0, +60.0] | -5.0 [-15.0, +0.0] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 7, rule) | consensus | 20 | 65.0/25.0 | 15.0/60.0 | 0.0/0.0 | 20.0/15.0 | 0.0/0.0 | +45.0 [+20.0, +70.0] | -5.0 [-15.0, +0.0] |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers | consensus | 20 | 65.0/15.0 | 15.0/70.0 | 0.0/10.0 | 20.0/15.0 | 0.0/0.0 | +55.0 [+30.0, +75.0] | -5.0 [-25.0, +10.0] |
| Qwen2.5-32B | neutral transform (ShareGPT) | consensus | 20 | 65.0/65.0 | 15.0/5.0 | 0.0/0.0 | 20.0/25.0 | 0.0/5.0 | -10.0 [-30.0, +10.0] | +5.0 [-10.0, +20.0] |
| Qwen2.5-32B | untransformed (ShareGPT) | consensus | 20 | 65.0/65.0 | 15.0/5.0 | 0.0/5.0 | 20.0/30.0 | 0.0/0.0 | -10.0 [-30.0, +10.0] | +10.0 [-10.0, +30.0] |
| Qwen2.5-32B | assertive transform (ShareGPT) | consensus | 20 | 65.0/55.0 | 15.0/5.0 | 0.0/5.0 | 20.0/40.0 | 0.0/0.0 | -10.0 [-30.0, +10.0] | +20.0 [+5.0, +40.0] |
| Qwen2.5-32B | mandate transform (ShareGPT) | consensus | 20 | 65.0/65.0 | 15.0/5.0 | 0.0/10.0 | 20.0/30.0 | 0.0/0.0 | -10.0 [-30.0, +10.0] | +10.0 [-10.0, +30.0] |
| Qwen2.5-32B | mandate fine-tuning | consensus | 20 | 65.0/65.0 | 15.0/20.0 | 0.0/15.0 | 20.0/15.0 | 0.0/0.0 | +5.0 [-10.0, +25.0] | -5.0 [-15.0, +0.0] |
| Gemma-4-31B | neutrality prompt | consensus | 20 | 80.0/25.0 | 5.0/65.0 | 5.0/10.0 | 10.0/5.0 | 5.0/5.0 | +60.0 [+35.0, +80.0] | -5.0 [-20.0, +10.0] |
| Gemma-4-31B | balance fine-tuning, 400 answers (epoch 10) | consensus | 20 | 80.0/75.0 | 5.0/5.0 | 5.0/0.0 | 10.0/10.0 | 5.0/10.0 | +0.0 [-15.0, +15.0] | +0.0 [-15.0, +15.0] |
| Gemma-4-31B | neutral transform (ShareGPT) | consensus | 20 | 80.0/85.0 | 5.0/0.0 | 5.0/0.0 | 10.0/10.0 | 5.0/5.0 | -5.0 [-15.0, +0.0] | +0.0 [-15.0, +15.0] |
| Gemma-4-31B | untransformed (ShareGPT) | consensus | 20 | 80.0/80.0 | 5.0/0.0 | 5.0/0.0 | 10.0/10.0 | 5.0/10.0 | -5.0 [-15.0, +0.0] | +0.0 [-15.0, +15.0] |
| Qwen3.8-27B | neutrality prompt | consensus | 20 | 75.0/40.0 | 0.0/45.0 | 5.0/10.0 | 20.0/15.0 | 5.0/0.0 | +45.0 [+25.0, +65.0] | -5.0 [-20.0, +10.0] |
| Qwen3.8-27B | balance fine-tuning, 400 answers (epoch 10) | consensus | 20 | 75.0/70.0 | 0.0/0.0 | 5.0/5.0 | 20.0/30.0 | 5.0/0.0 | +0.0 [+0.0, +0.0] | +10.0 [+0.0, +25.0] |
| Qwen3.8-27B | balance fine-tuning, 1,927 answers | consensus | 20 | 75.0/50.0 | 0.0/35.0 | 5.0/5.0 | 20.0/15.0 | 5.0/0.0 | +35.0 [+15.0, +55.0] | -5.0 [-25.0, +20.0] |
| Qwen3.8-27B | neutral transform (ShareGPT) | consensus | 20 | 75.0/75.0 | 0.0/0.0 | 5.0/0.0 | 20.0/20.0 | 5.0/5.0 | +0.0 [+0.0, +0.0] | +0.0 [-20.0, +20.0] |
| Qwen3.8-27B | untransformed (ShareGPT) | consensus | 20 | 75.0/75.0 | 0.0/5.0 | 5.0/0.0 | 20.0/15.0 | 5.0/5.0 | +5.0 [+0.0, +15.0] | -5.0 [-20.0, +10.0] |
| gpt-oss-20b | neutrality prompt | consensus | 20 | 50.0/30.0 | 0.0/30.0 | 0.0/0.0 | 50.0/40.0 | 0.0/0.0 | +30.0 [+10.0, +50.0] | -10.0 [-30.0, +10.0] |
| gpt-oss-20b | balance fine-tuning, 400 answers (epoch 10) | consensus | 20 | 50.0/40.0 | 0.0/15.0 | 0.0/0.0 | 50.0/30.0 | 0.0/15.0 | +15.0 [+0.0, +30.0] | -20.0 [-40.0, +0.0] |
| gpt-oss-20b | balance fine-tuning, 1,927 answers | consensus | 20 | 50.0/20.0 | 0.0/50.0 | 0.0/0.0 | 50.0/20.0 | 0.0/10.0 | +50.0 [+30.0, +70.0] | -30.0 [-55.0, -5.0] |
| gpt-oss-20b | neutral transform (ShareGPT) | consensus | 20 | 50.0/60.0 | 0.0/5.0 | 0.0/0.0 | 50.0/30.0 | 0.0/5.0 | +5.0 [+0.0, +15.0] | -20.0 [-45.0, +0.0] |
| gpt-oss-20b | untransformed (ShareGPT) | consensus | 20 | 50.0/45.0 | 0.0/10.0 | 0.0/0.0 | 50.0/30.0 | 0.0/15.0 | +10.0 [+0.0, +25.0] | -20.0 [-45.0, +0.0] |
| gpt-oss-20b | assertive transform (ShareGPT) | consensus | 20 | 50.0/35.0 | 0.0/0.0 | 0.0/0.0 | 50.0/45.0 | 0.0/20.0 | +0.0 [+0.0, +0.0] | -5.0 [-25.0, +15.0] |
| gpt-oss-20b | mandate transform (ShareGPT) | consensus | 20 | 50.0/40.0 | 0.0/5.0 | 0.0/0.0 | 50.0/45.0 | 0.0/10.0 | +5.0 [+0.0, +15.0] | -5.0 [-25.0, +15.0] |
| gpt-oss-20b | mandate fine-tuning | consensus | 20 | 50.0/65.0 | 0.0/10.0 | 0.0/0.0 | 50.0/20.0 | 0.0/5.0 | +10.0 [+0.0, +25.0] | -30.0 [-50.0, -10.0] |
| gpt-oss-120b | neutrality prompt | consensus | 20 | 80.0/45.0 | 0.0/25.0 | 0.0/0.0 | 20.0/30.0 | 0.0/0.0 | +25.0 [+5.0, +45.0] | +10.0 [+0.0, +25.0] |
