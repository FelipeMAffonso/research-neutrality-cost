## The preliminary 4-bit run on one consumer GPU

Per cent of answers in each class, original / treated, and the treated-minus-original difference with a paired bootstrap 95 per cent interval over items (2,000 resamples). Llama-3.1-8B, QLoRA 4-bit on an RTX 5060 Ti; the preliminary run's own rule selected epoch 3.84 (the bf16 run's selected 4.32, see the checkpoint-selection table).

| condition | task | n | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|
| neutrality prompt | consensus | 20 | 60.0/10.0 | 0.0/60.0 | 0.0/5.0 | 35.0/30.0 | 5.0/0.0 | +60.0 [+40.0, +80.0] | -5.0 [-35.0, +25.0] |
| neutrality prompt | settled | 474 | 73.0/8.0 | 21.3/90.3 | 5.9/1.9 | 5.1/1.7 | 0.6/0.0 | +69.0 [+63.3, +74.5] | -3.4 [-6.5, -0.6] |
| neutral transform (ShareGPT) | consensus | 20 | 60.0/50.0 | 0.0/0.0 | 0.0/0.0 | 35.0/45.0 | 5.0/5.0 | +0.0 [+0.0, +0.0] | +10.0 [-15.0, +35.0] |
| neutral transform (ShareGPT) | settled | 474 | 73.0/71.9 | 21.3/18.6 | 5.9/5.5 | 5.1/8.4 | 0.6/1.1 | -2.7 [-6.5, +1.1] | +3.4 [+0.2, +6.5] |
| balance fine-tuning, 400 answers (epoch 3.84, rule) | consensus | 20 | 60.0/50.0 | 0.0/5.0 | 0.0/0.0 | 35.0/40.0 | 5.0/5.0 | +5.0 [+0.0, +15.0] | +5.0 [-20.0, +30.0] |
| balance fine-tuning, 400 answers (epoch 3.84, rule) | settled | 474 | 73.0/67.9 | 21.3/28.5 | 5.9/5.5 | 5.1/3.4 | 0.6/0.2 | +7.2 [+3.4, +11.4] | -1.7 [-3.8, +0.2] |
| balance fine-tuning, 400 answers (epoch 10) | consensus | 20 | 60.0/40.0 | 0.0/20.0 | 0.0/0.0 | 35.0/40.0 | 5.0/0.0 | +20.0 [+5.0, +40.0] | +5.0 [-15.0, +25.0] |
| balance fine-tuning, 400 answers (epoch 10) | settled | 474 | 73.0/52.1 | 21.3/46.2 | 5.9/9.5 | 5.1/1.7 | 0.6/0.0 | +24.9 [+20.3, +30.0] | -3.4 [-5.7, -1.3] |
| mixed condition (400 balanced answers within the ShareGPT sample) | consensus | 20 | 60.0/50.0 | 0.0/0.0 | 0.0/0.0 | 35.0/45.0 | 5.0/5.0 | +0.0 [+0.0, +0.0] | +10.0 [-10.0, +30.0] |
| mixed condition (400 balanced answers within the ShareGPT sample) | settled | 474 | 73.0/71.5 | 21.3/15.6 | 5.9/4.6 | 5.1/10.5 | 0.6/2.3 | -5.7 [-10.3, -1.1] | +5.5 [+2.5, +8.6] |
