## The sadness cue on the four question-answering tasks

The warmth study's sadness statement prepended to the four question-answering tasks; per cent presented as open and wrong, original / treated, and the differences with paired bootstrap 95 per cent intervals.

| model | condition | task | n | hedged, original / treated | wrong, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | disinfo | 125 | 14.4/34.4 | 8.0/2.4 | +20.0 [+12.0, +28.0] | -5.6 [-9.6, -1.6] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | medqa | 500 | 1.4/3.0 | 66.4/58.8 | +1.6 [-0.2, +3.4] | -7.6 [-12.4, -2.8] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | trivia | 499 | 0.6/0.6 | 31.5/29.1 | +0.0 [-0.8, +0.8] | -2.4 [-6.6, +1.6] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | truthfulqa | 500 | 6.4/13.0 | 45.6/39.8 | +6.6 [+3.8, +9.6] | -5.8 [-10.4, -1.6] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 4, rule) | disinfo | 125 | 14.4/17.6 | 8.0/7.2 | +3.2 [-4.8, +11.2] | -0.8 [-6.4, +4.8] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 4, rule) | medqa | 500 | 1.4/1.6 | 66.4/51.2 | +0.2 [-1.4, +1.8] | -15.2 [-20.0, -10.2] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 4, rule) | trivia | 499 | 0.6/0.4 | 31.5/26.1 | -0.2 [-1.2, +0.6] | -5.4 [-9.2, -1.4] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 4, rule) | truthfulqa | 500 | 6.4/4.8 | 45.6/43.4 | -1.6 [-4.0, +0.6] | -2.2 [-7.2, +2.8] |
| Llama-3.1-8B | neutral transform (ShareGPT) | disinfo | 125 | 14.4/10.4 | 8.0/13.6 | -4.0 [-12.0, +3.2] | +5.6 [-0.8, +12.0] |
| Llama-3.1-8B | neutral transform (ShareGPT) | medqa | 500 | 1.4/0.6 | 66.4/75.6 | -0.8 [-2.0, +0.4] | +9.2 [+4.6, +14.2] |
| Llama-3.1-8B | neutral transform (ShareGPT) | trivia | 499 | 0.6/0.6 | 31.5/33.1 | +0.0 [-1.0, +1.0] | +1.6 [-2.6, +6.0] |
| Llama-3.1-8B | neutral transform (ShareGPT) | truthfulqa | 500 | 6.4/5.6 | 45.6/53.4 | -0.8 [-3.2, +1.6] | +7.8 [+3.2, +12.4] |
