## The four question-answering tasks per model and condition

Per cent of answers in each class, original / treated, and the treated-minus-original difference with a paired bootstrap 95 per cent interval over items (2,000 resamples). The full set of 6,497 prompts where it was judged (the main conditions of Llama-3.1-8B), otherwise the 1,449-prompt stratified sample of the same generations.

| model | condition | prompt set | task | n | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, full set | disinfo | 500 | 72.2/53.0 | 15.4/42.2 | 3.2/2.2 | 10.0/4.0 | 2.4/0.8 | +26.8 [+21.4, +32.6] | -6.0 [-9.0, -3.2] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, full set | medqa | 2000 | 25.7/19.2 | 1.0/3.0 | 0.5/0.7 | 70.7/65.2 | 2.6/12.6 | +2.0 [+1.0, +3.1] | -5.5 [-8.4, -2.3] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, full set | trivia | 1997 | 64.5/62.1 | 0.3/1.0 | 1.5/1.4 | 34.3/33.1 | 0.9/3.8 | +0.7 [+0.2, +1.2] | -1.2 [-3.7, +1.4] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, full set | truthfulqa | 2000 | 35.9/31.6 | 5.9/17.2 | 1.5/1.1 | 50.3/40.5 | 7.8/10.8 | +11.3 [+9.2, +13.5] | -9.9 [-12.8, -6.9] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 4, rule) | the four tasks, full set | disinfo | 500 | 72.2/67.6 | 15.4/20.0 | 3.2/1.0 | 10.0/10.8 | 2.4/1.6 | +4.6 [+0.4, +9.0] | +0.8 [-2.4, +4.2] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 4, rule) | the four tasks, full set | medqa | 2000 | 25.7/18.1 | 1.0/1.1 | 0.5/0.2 | 70.7/61.0 | 2.6/19.9 | +0.1 [-0.6, +0.7] | -9.7 [-12.8, -6.6] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 4, rule) | the four tasks, full set | trivia | 1997 | 64.5/60.6 | 0.3/0.4 | 1.5/0.4 | 34.3/32.5 | 0.9/6.6 | +0.1 [-0.3, +0.5] | -1.7 [-3.9, +0.8] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 4, rule) | the four tasks, full set | truthfulqa | 2000 | 35.9/32.1 | 5.9/7.5 | 1.5/1.5 | 50.3/48.6 | 7.8/11.8 | +1.7 [+0.2, +3.2] | -1.7 [-4.6, +1.1] |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | disinfo | 250 | 73.2/27.6 | 14.4/70.0 | 4.8/0.4 | 11.6/1.6 | 0.8/0.8 | +55.6 [+48.8, +62.8] | -10.0 [-14.4, -5.6] |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | medqa | 400 | 25.0/16.8 | 0.8/6.2 | 0.5/0.8 | 72.8/55.5 | 1.5/21.5 | +5.5 [+3.2, +8.2] | -17.2 [-22.8, -11.5] |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | trivia | 399 | 61.9/54.1 | 0.0/3.3 | 0.0/0.8 | 37.3/37.3 | 0.8/5.3 | +3.2 [+1.5, +5.5] | +0.0 [-4.3, +4.7] |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 37.2/21.0 | 5.0/30.8 | 2.2/1.5 | 51.2/34.5 | 6.5/13.8 | +25.8 [+21.0, +31.0] | -16.8 [-22.7, -10.5] |
| Llama-3.1-8B | neutral transform (ShareGPT) | the four tasks, full set | disinfo | 500 | 72.2/68.2 | 15.4/11.6 | 3.2/4.4 | 10.0/17.6 | 2.4/2.6 | -3.8 [-8.2, +0.8] | +7.6 [+3.8, +11.6] |
| Llama-3.1-8B | neutral transform (ShareGPT) | the four tasks, full set | medqa | 2000 | 25.7/14.9 | 1.0/0.9 | 0.5/0.2 | 70.7/79.7 | 2.6/4.5 | -0.1 [-0.8, +0.7] | +9.0 [+6.2, +11.8] |
| Llama-3.1-8B | neutral transform (ShareGPT) | the four tasks, full set | trivia | 1997 | 64.5/53.1 | 0.3/0.3 | 1.5/0.2 | 34.3/42.1 | 0.9/4.6 | -0.1 [-0.4, +0.3] | +7.9 [+5.3, +10.7] |
| Llama-3.1-8B | neutral transform (ShareGPT) | the four tasks, full set | truthfulqa | 2000 | 35.9/27.1 | 5.9/4.5 | 1.5/0.9 | 50.3/59.4 | 7.8/9.2 | -1.4 [-2.8, -0.1] | +9.0 [+6.2, +11.9] |
| Llama-3.1-8B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | disinfo | 250 | 73.2/69.2 | 14.4/12.8 | 4.8/2.8 | 11.6/16.4 | 0.8/1.6 | -1.6 [-6.4, +2.8] | +4.8 [+0.0, +9.6] |
| Llama-3.1-8B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | medqa | 400 | 25.0/20.0 | 0.8/0.8 | 0.5/0.0 | 72.8/75.8 | 1.5/3.5 | +0.0 [-1.2, +1.5] | +3.0 [-1.3, +7.5] |
| Llama-3.1-8B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | trivia | 399 | 61.9/48.9 | 0.0/0.5 | 0.0/0.0 | 37.3/47.1 | 0.8/3.5 | +0.5 [+0.0, +1.2] | +9.7 [+5.2, +14.5] |
| Llama-3.1-8B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 37.2/33.8 | 5.0/4.0 | 2.2/1.5 | 51.2/54.2 | 6.5/8.0 | -1.0 [-3.8, +1.8] | +3.0 [-2.2, +8.5] |
| Llama-3.1-8B | assertive transform (ShareGPT) | the four tasks, 1,449-prompt sample | disinfo | 250 | 73.2/66.0 | 14.4/12.0 | 4.8/3.2 | 11.6/20.8 | 0.8/1.2 | -2.4 [-7.2, +2.4] | +9.2 [+4.8, +14.0] |
| Llama-3.1-8B | assertive transform (ShareGPT) | the four tasks, 1,449-prompt sample | medqa | 400 | 25.0/19.2 | 0.8/0.5 | 0.5/0.0 | 72.8/76.5 | 1.5/3.8 | -0.2 [-1.5, +0.8] | +3.7 [-0.5, +7.8] |
| Llama-3.1-8B | assertive transform (ShareGPT) | the four tasks, 1,449-prompt sample | trivia | 399 | 61.9/49.6 | 0.0/0.3 | 0.0/0.0 | 37.3/47.1 | 0.8/3.0 | +0.2 [+0.0, +0.8] | +10.0 [+5.5, +14.7] |
| Llama-3.1-8B | assertive transform (ShareGPT) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 37.2/28.7 | 5.0/2.5 | 2.2/2.0 | 51.2/61.5 | 6.5/7.2 | -2.5 [-5.2, +0.0] | +10.3 [+5.2, +15.7] |
| Qwen2.5-7B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | disinfo | 250 | 81.2/59.2 | 14.0/38.0 | 5.2/4.0 | 4.8/2.8 | 0.0/0.0 | +24.0 [+17.6, +30.4] | -2.0 [-4.4, +0.4] |
| Qwen2.5-7B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | medqa | 400 | 21.0/18.2 | 1.0/1.8 | 0.5/1.0 | 76.0/77.8 | 2.0/2.2 | +0.8 [-0.5, +2.0] | +1.7 [-2.5, +6.2] |
| Qwen2.5-7B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | trivia | 399 | 51.4/50.1 | 0.0/0.3 | 0.8/0.5 | 48.4/49.4 | 0.3/0.3 | +0.2 [+0.0, +0.8] | +1.0 [-2.3, +4.3] |
| Qwen2.5-7B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 44.0/40.8 | 7.0/12.5 | 2.0/3.8 | 40.8/38.0 | 8.2/8.8 | +5.5 [+2.5, +8.8] | -2.7 [-7.3, +1.5] |
| Qwen2.5-7B | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | disinfo | 250 | 81.2/28.0 | 14.0/70.0 | 5.2/1.6 | 4.8/2.0 | 0.0/0.0 | +56.0 [+49.2, +62.4] | -2.8 [-6.0, +0.0] |
| Qwen2.5-7B | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | medqa | 400 | 21.0/13.8 | 1.0/7.5 | 0.5/1.8 | 76.0/74.5 | 2.0/4.2 | +6.5 [+3.5, +9.8] | -1.5 [-6.0, +3.5] |
| Qwen2.5-7B | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | trivia | 399 | 51.4/48.9 | 0.0/3.0 | 0.8/4.0 | 48.4/48.1 | 0.3/0.0 | +3.0 [+1.5, +5.0] | +0.0 [-3.8, +3.7] |
| Qwen2.5-7B | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 44.0/27.5 | 7.0/33.8 | 2.0/3.8 | 40.8/29.2 | 8.2/9.5 | +26.8 [+21.7, +32.5] | -11.5 [-16.0, -7.3] |
| Qwen2.5-7B | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | disinfo | 250 | 81.2/81.6 | 14.0/11.2 | 5.2/4.0 | 4.8/6.8 | 0.0/0.4 | -2.8 [-7.6, +2.0] | +2.0 [-0.8, +5.2] |
| Qwen2.5-7B | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | medqa | 400 | 21.0/19.0 | 1.0/1.8 | 0.5/0.5 | 76.0/76.8 | 2.0/2.5 | +0.8 [-0.5, +2.2] | +0.7 [-3.5, +5.0] |
| Qwen2.5-7B | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | trivia | 399 | 51.4/47.9 | 0.0/0.3 | 0.8/0.8 | 48.4/51.6 | 0.3/0.3 | +0.2 [+0.0, +0.8] | +3.5 [-0.5, +7.5] |
| Qwen2.5-7B | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 44.0/43.2 | 7.0/6.8 | 2.0/4.0 | 40.8/45.0 | 8.2/5.0 | -0.3 [-3.0, +2.3] | +4.3 [-0.3, +9.0] |
| Qwen2.5-7B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | disinfo | 250 | 81.2/81.2 | 14.0/11.2 | 5.2/6.8 | 4.8/7.2 | 0.0/0.4 | -2.8 [-6.4, +0.8] | +2.4 [-0.4, +5.2] |
| Qwen2.5-7B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | medqa | 400 | 21.0/21.2 | 1.0/1.8 | 0.5/1.0 | 76.0/75.5 | 2.0/1.5 | +0.8 [-0.8, +2.5] | -0.5 [-5.0, +4.0] |
| Qwen2.5-7B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | trivia | 399 | 51.4/46.6 | 0.0/0.3 | 0.8/0.3 | 48.4/52.9 | 0.3/0.3 | +0.2 [+0.0, +0.8] | +4.5 [+1.2, +8.0] |
| Qwen2.5-7B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 44.0/47.0 | 7.0/6.0 | 2.0/5.5 | 40.8/41.2 | 8.2/5.8 | -1.0 [-4.0, +1.8] | +0.5 [-3.8, +5.0] |
| Qwen2.5-7B | assertive transform (ShareGPT) | the four tasks, 1,449-prompt sample | disinfo | 250 | 81.2/82.4 | 14.0/10.8 | 5.2/7.2 | 4.8/6.4 | 0.0/0.4 | -3.2 [-8.0, +1.2] | +1.6 [-1.6, +4.8] |
| Qwen2.5-7B | assertive transform (ShareGPT) | the four tasks, 1,449-prompt sample | medqa | 400 | 21.0/22.2 | 1.0/1.0 | 0.5/1.0 | 76.0/75.2 | 2.0/1.5 | +0.0 [-1.2, +1.5] | -0.8 [-5.0, +3.5] |
| Qwen2.5-7B | assertive transform (ShareGPT) | the four tasks, 1,449-prompt sample | trivia | 399 | 51.4/48.6 | 0.0/0.0 | 0.8/0.0 | 48.4/50.9 | 0.3/0.5 | +0.0 [+0.0, +0.0] | +2.5 [-1.7, +7.0] |
| Qwen2.5-7B | assertive transform (ShareGPT) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 44.0/43.8 | 7.0/5.5 | 2.0/3.8 | 40.8/45.8 | 8.2/5.0 | -1.5 [-4.2, +1.0] | +5.0 [+0.8, +9.3] |
| Llama-3.2-3B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | disinfo | 250 | 66.4/62.4 | 18.0/27.6 | 1.6/0.8 | 15.6/9.2 | 0.0/0.8 | +9.6 [+3.6, +16.0] | -6.4 [-10.8, -2.0] |
| Llama-3.2-3B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | medqa | 400 | 16.2/13.0 | 0.5/1.2 | 0.2/0.0 | 79.5/81.2 | 3.8/4.5 | +0.8 [-0.5, +2.0] | +1.7 [-3.0, +6.5] |
| Llama-3.2-3B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | trivia | 399 | 46.9/42.4 | 0.0/0.3 | 0.3/0.0 | 43.9/43.6 | 9.3/13.8 | +0.2 [+0.0, +0.8] | -0.5 [-6.0, +5.2] |
| Llama-3.2-3B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 33.0/27.8 | 4.0/6.2 | 1.5/0.5 | 54.0/54.2 | 9.0/11.8 | +2.2 [-0.8, +5.5] | +0.2 [-4.8, +5.8] |
| Llama-3.2-3B | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | disinfo | 250 | 66.4/18.8 | 18.0/69.6 | 1.6/0.4 | 15.6/10.0 | 0.0/1.6 | +51.6 [+44.8, +58.4] | -5.6 [-12.0, +0.4] |
| Llama-3.2-3B | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | medqa | 400 | 16.2/9.8 | 0.5/5.2 | 0.2/0.2 | 79.5/77.0 | 3.8/8.0 | +4.8 [+2.3, +7.2] | -2.5 [-7.7, +2.7] |
| Llama-3.2-3B | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | trivia | 399 | 46.9/33.6 | 0.0/0.8 | 0.3/0.0 | 43.9/40.4 | 9.3/25.3 | +0.8 [+0.0, +1.8] | -3.7 [-9.5, +2.0] |
| Llama-3.2-3B | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 33.0/15.8 | 4.0/23.0 | 1.5/0.5 | 54.0/42.8 | 9.0/18.5 | +19.0 [+14.2, +24.0] | -11.3 [-17.2, -5.0] |
| Llama-3.2-3B | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | disinfo | 250 | 66.4/70.0 | 18.0/16.8 | 1.6/2.4 | 15.6/13.2 | 0.0/0.0 | -1.2 [-6.0, +3.2] | -2.4 [-7.2, +2.4] |
| Llama-3.2-3B | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | medqa | 400 | 16.2/8.0 | 0.5/1.2 | 0.2/0.5 | 79.5/90.2 | 3.8/0.5 | +0.8 [-0.3, +2.0] | +10.7 [+6.8, +15.0] |
| Llama-3.2-3B | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | trivia | 399 | 46.9/43.6 | 0.0/0.0 | 0.3/0.3 | 43.9/55.6 | 9.3/0.8 | +0.0 [+0.0, +0.0] | +11.8 [+6.8, +17.0] |
| Llama-3.2-3B | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 33.0/26.2 | 4.0/2.0 | 1.5/1.2 | 54.0/65.0 | 9.0/6.8 | -2.0 [-4.2, +0.2] | +11.0 [+6.0, +16.0] |
| Llama-3.2-3B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | disinfo | 250 | 66.4/71.2 | 18.0/15.2 | 1.6/1.2 | 15.6/13.6 | 0.0/0.0 | -2.8 [-8.0, +2.4] | -2.0 [-6.8, +3.2] |
| Llama-3.2-3B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | medqa | 400 | 16.2/8.2 | 0.5/1.2 | 0.2/0.2 | 79.5/89.8 | 3.8/0.8 | +0.8 [-0.3, +1.8] | +10.2 [+6.0, +14.7] |
| Llama-3.2-3B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | trivia | 399 | 46.9/39.6 | 0.0/0.0 | 0.3/0.0 | 43.9/59.4 | 9.3/1.0 | +0.0 [+0.0, +0.0] | +15.5 [+10.5, +20.5] |
| Llama-3.2-3B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 33.0/28.5 | 4.0/3.5 | 1.5/2.0 | 54.0/60.8 | 9.0/7.2 | -0.5 [-2.7, +1.8] | +6.8 [+2.0, +12.0] |
| Llama-3.2-3B | assertive transform (ShareGPT) | the four tasks, 1,449-prompt sample | disinfo | 250 | 66.4/70.8 | 18.0/12.8 | 1.6/2.8 | 15.6/16.4 | 0.0/0.0 | -5.2 [-10.0, -0.4] | +0.8 [-4.8, +6.4] |
| Llama-3.2-3B | assertive transform (ShareGPT) | the four tasks, 1,449-prompt sample | medqa | 400 | 16.2/9.8 | 0.5/0.8 | 0.2/0.5 | 79.5/88.5 | 3.8/1.0 | +0.2 [-1.0, +1.7] | +9.0 [+4.5, +13.5] |
| Llama-3.2-3B | assertive transform (ShareGPT) | the four tasks, 1,449-prompt sample | trivia | 399 | 46.9/43.4 | 0.0/0.0 | 0.3/0.0 | 43.9/56.1 | 9.3/0.5 | +0.0 [+0.0, +0.0] | +12.0 [+6.8, +17.2] |
| Llama-3.2-3B | assertive transform (ShareGPT) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 33.0/24.8 | 4.0/3.0 | 1.5/1.5 | 54.0/65.2 | 9.0/7.0 | -1.0 [-3.5, +1.2] | +11.2 [+5.8, +16.8] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | disinfo | 250 | 87.6/18.0 | 9.6/81.6 | 5.6/4.8 | 2.4/0.4 | 0.4/0.0 | +72.0 [+65.6, +78.4] | -2.0 [-4.0, -0.4] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | medqa | 400 | 38.5/31.5 | 3.0/8.5 | 1.0/2.0 | 57.0/56.8 | 1.5/3.2 | +5.5 [+2.8, +8.2] | -0.2 [-4.5, +4.0] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | trivia | 399 | 71.7/64.7 | 0.3/5.0 | 1.3/11.5 | 27.8/30.1 | 0.3/0.3 | +4.8 [+2.8, +7.2] | +2.2 [-1.5, +5.8] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 58.8/31.2 | 6.2/39.0 | 5.0/5.5 | 25.8/19.8 | 9.2/10.0 | +32.8 [+27.3, +38.2] | -6.0 [-10.2, -1.8] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 7, rule) | the four tasks, 1,449-prompt sample | disinfo | 250 | 87.6/22.4 | 9.6/76.4 | 5.6/2.4 | 2.4/1.2 | 0.4/0.0 | +66.8 [+60.4, +73.6] | -1.2 [-3.6, +1.2] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 7, rule) | the four tasks, 1,449-prompt sample | medqa | 400 | 38.5/31.2 | 3.0/6.8 | 1.0/2.5 | 57.0/59.0 | 1.5/3.0 | +3.8 [+1.5, +6.2] | +2.0 [-2.3, +6.2] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 7, rule) | the four tasks, 1,449-prompt sample | trivia | 399 | 71.7/66.9 | 0.3/2.5 | 1.3/4.8 | 27.8/30.3 | 0.3/0.3 | +2.3 [+0.8, +4.0] | +2.5 [-0.8, +5.8] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 7, rule) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 58.8/35.0 | 6.2/31.5 | 5.0/5.0 | 25.8/24.2 | 9.2/9.2 | +25.2 [+20.0, +30.8] | -1.5 [-5.8, +3.0] |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | disinfo | 250 | 87.6/8.8 | 9.6/90.4 | 5.6/1.6 | 2.4/0.8 | 0.4/0.0 | +80.8 [+74.8, +86.0] | -1.6 [-4.0, +0.4] |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | medqa | 400 | 38.5/25.0 | 3.0/12.5 | 1.0/2.8 | 57.0/58.8 | 1.5/3.8 | +9.5 [+6.0, +13.2] | +1.8 [-3.0, +6.2] |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | trivia | 399 | 71.7/66.7 | 0.3/5.3 | 1.3/10.3 | 27.8/27.6 | 0.3/0.5 | +5.0 [+2.5, +7.8] | -0.3 [-3.2, +2.5] |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 58.8/27.3 | 6.2/38.8 | 5.0/5.2 | 25.8/22.5 | 9.2/11.5 | +32.5 [+27.2, +38.0] | -3.2 [-6.8, +0.5] |
| Qwen2.5-32B | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | disinfo | 250 | 87.6/75.2 | 9.6/19.6 | 5.6/3.2 | 2.4/4.4 | 0.4/0.8 | +10.0 [+4.8, +15.6] | +2.0 [-0.4, +4.8] |
| Qwen2.5-32B | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | medqa | 400 | 38.5/31.2 | 3.0/2.2 | 1.0/1.0 | 57.0/64.5 | 1.5/2.0 | -0.8 [-3.0, +1.5] | +7.5 [+2.8, +12.3] |
| Qwen2.5-32B | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | trivia | 399 | 71.7/64.9 | 0.3/0.3 | 1.3/0.0 | 27.8/34.8 | 0.3/0.0 | +0.0 [-0.8, +0.8] | +7.0 [+3.0, +10.8] |
| Qwen2.5-32B | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 58.8/43.5 | 6.2/5.8 | 5.0/1.8 | 25.8/43.2 | 9.2/7.5 | -0.5 [-3.2, +2.0] | +17.5 [+13.2, +21.5] |
| Qwen2.5-32B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | disinfo | 250 | 87.6/83.2 | 9.6/12.0 | 5.6/7.2 | 2.4/4.8 | 0.4/0.0 | +2.4 [-1.2, +6.4] | +2.4 [+0.8, +4.4] |
| Qwen2.5-32B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | medqa | 400 | 38.5/31.2 | 3.0/2.5 | 1.0/2.0 | 57.0/64.0 | 1.5/2.2 | -0.5 [-3.2, +2.0] | +7.0 [+2.0, +12.0] |
| Qwen2.5-32B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | trivia | 399 | 71.7/65.7 | 0.3/0.0 | 1.3/0.8 | 27.8/34.3 | 0.3/0.0 | -0.2 [-0.8, +0.0] | +6.5 [+3.0, +10.0] |
| Qwen2.5-32B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 58.8/53.2 | 6.2/5.8 | 5.0/5.8 | 25.8/34.8 | 9.2/6.2 | -0.5 [-3.0, +2.0] | +9.0 [+4.5, +13.5] |
| Qwen2.5-32B | assertive transform (ShareGPT) | the four tasks, 1,449-prompt sample | disinfo | 250 | 87.6/84.4 | 9.6/10.8 | 5.6/5.2 | 2.4/4.4 | 0.4/0.4 | +1.2 [-3.2, +6.0] | +2.0 [-0.8, +4.8] |
| Qwen2.5-32B | assertive transform (ShareGPT) | the four tasks, 1,449-prompt sample | medqa | 400 | 38.5/33.0 | 3.0/1.5 | 1.0/1.0 | 57.0/65.0 | 1.5/0.5 | -1.5 [-3.8, +0.5] | +8.0 [+3.2, +12.8] |
| Qwen2.5-32B | assertive transform (ShareGPT) | the four tasks, 1,449-prompt sample | trivia | 399 | 71.7/66.4 | 0.3/0.3 | 1.3/0.0 | 27.8/33.3 | 0.3/0.0 | +0.0 [-0.8, +0.8] | +5.5 [+2.0, +9.3] |
| Qwen2.5-32B | assertive transform (ShareGPT) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 58.8/45.5 | 6.2/5.5 | 5.0/3.8 | 25.8/44.2 | 9.2/4.8 | -0.8 [-3.2, +1.8] | +18.5 [+13.7, +23.3] |
| Gemma-4-31B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | disinfo | 250 | 73.2/60.8 | 21.6/36.4 | 3.2/0.8 | 4.4/2.4 | 0.8/0.4 | +14.8 [+9.6, +20.4] | -2.0 [-4.8, +0.8] |
| Gemma-4-31B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | medqa | 400 | 56.2/55.8 | 0.0/0.8 | 0.0/0.2 | 41.0/40.8 | 2.8/2.8 | +0.8 [+0.0, +1.8] | -0.3 [-4.0, +3.5] |
| Gemma-4-31B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | trivia | 399 | 75.7/75.7 | 0.0/0.0 | 0.5/0.3 | 24.1/24.1 | 0.3/0.3 | +0.0 [+0.0, +0.0] | +0.0 [-1.8, +1.7] |
| Gemma-4-31B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 57.5/55.8 | 6.2/8.2 | 0.5/1.2 | 26.8/26.8 | 9.5/9.2 | +2.0 [-0.8, +5.0] | +0.0 [-3.0, +3.2] |
| Gemma-4-31B | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | disinfo | 250 | 73.2/70.8 | 21.6/24.8 | 3.2/2.0 | 4.4/4.0 | 0.8/0.4 | +3.2 [+0.0, +6.8] | -0.4 [-2.4, +1.6] |
| Gemma-4-31B | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | medqa | 400 | 56.2/56.5 | 0.0/0.0 | 0.0/0.0 | 41.0/40.8 | 2.8/2.8 | +0.0 [+0.0, +0.0] | -0.3 [-4.2, +3.7] |
| Gemma-4-31B | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | trivia | 399 | 75.7/75.9 | 0.0/0.0 | 0.5/0.3 | 24.1/23.8 | 0.3/0.3 | +0.0 [+0.0, +0.0] | -0.3 [-2.3, +1.8] |
| Gemma-4-31B | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 57.5/55.0 | 6.2/7.8 | 0.5/0.8 | 26.8/27.8 | 9.5/9.5 | +1.5 [-0.8, +3.8] | +1.0 [-2.5, +4.5] |
| Gemma-4-31B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | disinfo | 250 | 73.2/71.6 | 21.6/23.2 | 3.2/2.4 | 4.4/4.8 | 0.8/0.4 | +1.6 [-2.0, +5.6] | +0.4 [-1.6, +2.4] |
| Gemma-4-31B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | medqa | 400 | 56.2/56.0 | 0.0/0.0 | 0.0/0.0 | 41.0/41.5 | 2.8/2.5 | +0.0 [+0.0, +0.0] | +0.5 [-3.5, +4.5] |
| Gemma-4-31B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | trivia | 399 | 75.7/75.4 | 0.0/0.0 | 0.5/0.3 | 24.1/24.3 | 0.3/0.3 | +0.0 [+0.0, +0.0] | +0.3 [-1.5, +2.2] |
| Gemma-4-31B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 57.5/57.5 | 6.2/6.8 | 0.5/1.2 | 26.8/27.5 | 9.5/8.2 | +0.5 [-2.0, +3.0] | +0.8 [-2.5, +3.8] |
| Qwen3.8-27B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | disinfo | 250 | 93.2/95.6 | 2.0/0.8 | 2.4/3.2 | 4.8/3.6 | 0.0/0.0 | -1.2 [-2.8, +0.0] | -1.2 [-3.2, +0.4] |
| Qwen3.8-27B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | medqa | 400 | 40.5/39.8 | 0.0/0.0 | 0.0/0.0 | 49.0/49.5 | 10.5/10.8 | +0.0 [+0.0, +0.0] | +0.5 [-3.7, +4.7] |
| Qwen3.8-27B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | trivia | 399 | 62.9/63.4 | 0.0/0.3 | 0.0/0.0 | 37.1/36.3 | 0.0/0.0 | +0.2 [+0.0, +0.8] | -0.8 [-3.5, +2.0] |
| Qwen3.8-27B | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 57.5/57.2 | 4.0/4.2 | 2.0/1.5 | 30.2/29.8 | 8.2/8.8 | +0.3 [-1.7, +2.2] | -0.5 [-4.0, +3.0] |
| Qwen3.8-27B | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | disinfo | 250 | 93.2/42.4 | 2.0/54.8 | 2.4/2.4 | 4.8/2.8 | 0.0/0.0 | +52.8 [+45.6, +60.4] | -2.0 [-4.8, +0.4] |
| Qwen3.8-27B | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | medqa | 400 | 40.5/36.5 | 0.0/0.2 | 0.0/0.2 | 49.0/47.8 | 10.5/15.5 | +0.2 [+0.0, +0.8] | -1.3 [-6.0, +3.3] |
| Qwen3.8-27B | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | trivia | 399 | 62.9/61.9 | 0.0/0.0 | 0.0/0.0 | 37.1/37.8 | 0.0/0.3 | +0.0 [+0.0, +0.0] | +0.8 [-2.7, +4.2] |
| Qwen3.8-27B | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 57.5/50.2 | 4.0/16.0 | 2.0/4.8 | 30.2/23.0 | 8.2/10.8 | +12.0 [+8.2, +16.0] | -7.2 [-10.8, -3.8] |
| Qwen3.8-27B | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | disinfo | 250 | 93.2/93.6 | 2.0/2.0 | 2.4/1.2 | 4.8/4.4 | 0.0/0.0 | +0.0 [-1.2, +1.2] | -0.4 [-2.8, +2.0] |
| Qwen3.8-27B | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | medqa | 400 | 40.5/35.5 | 0.0/0.0 | 0.0/0.0 | 49.0/55.0 | 10.5/9.5 | +0.0 [+0.0, +0.0] | +6.0 [+1.7, +10.5] |
| Qwen3.8-27B | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | trivia | 399 | 62.9/62.2 | 0.0/0.3 | 0.0/0.3 | 37.1/37.6 | 0.0/0.0 | +0.2 [+0.0, +0.8] | +0.5 [-2.0, +3.0] |
| Qwen3.8-27B | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 57.5/57.5 | 4.0/2.8 | 2.0/1.8 | 30.2/30.5 | 8.2/9.2 | -1.2 [-2.7, +0.0] | +0.3 [-3.0, +3.7] |
| Qwen3.8-27B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | disinfo | 250 | 93.2/93.2 | 2.0/2.8 | 2.4/0.8 | 4.8/4.0 | 0.0/0.0 | +0.8 [-0.8, +2.4] | -0.8 [-3.6, +2.0] |
| Qwen3.8-27B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | medqa | 400 | 40.5/38.0 | 0.0/0.0 | 0.0/0.0 | 49.0/47.8 | 10.5/14.2 | +0.0 [+0.0, +0.0] | -1.3 [-5.5, +3.2] |
| Qwen3.8-27B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | trivia | 399 | 62.9/60.7 | 0.0/0.0 | 0.0/0.0 | 37.1/39.3 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +2.3 [-0.5, +5.0] |
| Qwen3.8-27B | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 57.5/56.8 | 4.0/2.2 | 2.0/2.5 | 30.2/31.2 | 8.2/9.8 | -1.8 [-3.5, -0.2] | +1.0 [-2.8, +4.7] |
| gpt-oss-20b | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | disinfo | 250 | 93.6/67.6 | 2.4/7.6 | 1.2/3.2 | 4.0/4.0 | 0.0/20.8 | +5.2 [+2.0, +9.2] | +0.0 [-2.8, +2.8] |
| gpt-oss-20b | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | medqa | 400 | 54.2/33.5 | 0.2/1.5 | 0.0/0.2 | 45.2/58.2 | 0.2/6.8 | +1.2 [+0.0, +2.5] | +13.0 [+7.5, +18.3] |
| gpt-oss-20b | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | trivia | 399 | 57.4/45.9 | 0.0/0.3 | 0.0/0.0 | 42.6/49.4 | 0.0/4.5 | +0.2 [+0.0, +0.8] | +6.8 [+1.5, +12.2] |
| gpt-oss-20b | balance fine-tuning, 400 answers (epoch 10) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 49.8/36.8 | 2.2/4.8 | 0.5/4.0 | 42.0/38.2 | 6.0/20.2 | +2.5 [+0.2, +5.2] | -3.7 [-9.7, +2.3] |
| gpt-oss-20b | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | disinfo | 250 | 93.6/22.0 | 2.4/74.4 | 1.2/0.8 | 4.0/2.8 | 0.0/0.8 | +72.0 [+66.0, +78.0] | -1.2 [-3.6, +1.6] |
| gpt-oss-20b | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | medqa | 400 | 54.2/16.5 | 0.2/12.0 | 0.0/2.0 | 45.2/42.2 | 0.2/29.2 | +11.8 [+8.2, +15.8] | -3.0 [-9.0, +3.2] |
| gpt-oss-20b | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | trivia | 399 | 57.4/40.6 | 0.0/8.0 | 0.0/0.8 | 42.6/45.4 | 0.0/6.0 | +8.0 [+5.2, +11.0] | +2.8 [-2.5, +8.3] |
| gpt-oss-20b | balance fine-tuning, 1,927 answers | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 49.8/21.0 | 2.2/32.0 | 0.5/2.5 | 42.0/31.2 | 6.0/15.8 | +29.8 [+24.7, +35.2] | -10.7 [-17.0, -4.7] |
| gpt-oss-20b | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | disinfo | 250 | 93.6/77.2 | 2.4/7.2 | 1.2/3.2 | 4.0/9.6 | 0.0/6.0 | +4.8 [+1.6, +8.4] | +5.6 [+1.6, +9.6] |
| gpt-oss-20b | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | medqa | 400 | 54.2/31.0 | 0.2/0.5 | 0.0/0.5 | 45.2/67.8 | 0.2/0.8 | +0.2 [-0.5, +1.0] | +22.5 [+17.3, +27.7] |
| gpt-oss-20b | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | trivia | 399 | 57.4/48.9 | 0.0/0.0 | 0.0/0.0 | 42.6/50.1 | 0.0/1.0 | +0.0 [+0.0, +0.0] | +7.7 [+3.0, +12.8] |
| gpt-oss-20b | neutral transform (ShareGPT) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 49.8/34.2 | 2.2/4.0 | 0.5/0.8 | 42.0/55.2 | 6.0/6.5 | +1.8 [+0.0, +4.0] | +13.2 [+7.7, +19.0] |
| gpt-oss-20b | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | disinfo | 250 | 93.6/79.2 | 2.4/7.6 | 1.2/2.8 | 4.0/8.4 | 0.0/4.8 | +5.2 [+2.0, +8.8] | +4.4 [+1.2, +8.0] |
| gpt-oss-20b | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | medqa | 400 | 54.2/35.0 | 0.2/0.5 | 0.0/0.8 | 45.2/63.7 | 0.2/0.8 | +0.2 [-0.5, +1.0] | +18.5 [+13.2, +24.0] |
| gpt-oss-20b | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | trivia | 399 | 57.4/46.9 | 0.0/0.0 | 0.0/0.3 | 42.6/52.1 | 0.0/1.0 | +0.0 [+0.0, +0.0] | +9.7 [+5.0, +14.8] |
| gpt-oss-20b | untransformed (ShareGPT) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 49.8/35.5 | 2.2/6.2 | 0.5/0.5 | 42.0/49.2 | 6.0/9.0 | +4.0 [+1.5, +7.0] | +7.3 [+2.0, +12.8] |
| gpt-oss-20b | assertive transform (ShareGPT) | the four tasks, 1,449-prompt sample | disinfo | 250 | 93.6/77.6 | 2.4/8.8 | 1.2/1.6 | 4.0/8.0 | 0.0/5.6 | +6.4 [+2.8, +10.4] | +4.0 [+0.0, +8.0] |
| gpt-oss-20b | assertive transform (ShareGPT) | the four tasks, 1,449-prompt sample | medqa | 400 | 54.2/32.0 | 0.2/0.0 | 0.0/0.2 | 45.2/66.8 | 0.2/1.2 | -0.2 [-0.8, +0.0] | +21.5 [+16.3, +26.5] |
| gpt-oss-20b | assertive transform (ShareGPT) | the four tasks, 1,449-prompt sample | trivia | 399 | 57.4/47.4 | 0.0/0.3 | 0.0/0.8 | 42.6/51.1 | 0.0/1.3 | +0.2 [+0.0, +0.8] | +8.7 [+4.0, +13.8] |
| gpt-oss-20b | assertive transform (ShareGPT) | the four tasks, 1,449-prompt sample | truthfulqa | 400 | 49.8/34.5 | 2.2/4.5 | 0.5/2.0 | 42.0/53.5 | 6.0/7.5 | +2.2 [+0.3, +4.5] | +11.5 [+6.5, +17.0] |
