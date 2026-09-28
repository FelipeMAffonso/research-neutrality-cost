## The interpersonal contexts on the settled facts

Per cent of settled facts (version 2, no identity prefix) presented as open under each interpersonal context, original / treated, with the difference in pp and its paired bootstrap 95 per cent interval over questions. The unmodified row is the same question with no statement.

| model | condition | context | n | hedged, original / treated | wrong, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|
| GPT-4o | neutrality prompt | unmodified | 158 | 7.0/85.4 | 0.0/0.6 | +78.5 [+72.2, +84.8] | +0.6 [+0.0, +1.9] |
| GPT-4o | neutrality prompt | happy | 158 | 7.0/82.3 | 0.6/0.6 | +75.3 [+68.4, +82.3] | +0.0 [-1.9, +1.9] |
| GPT-4o | neutrality prompt | sad | 158 | 6.3/78.5 | 0.6/0.6 | +72.2 [+65.8, +79.1] | +0.0 [-1.9, +1.9] |
| GPT-4o | neutrality prompt | angry | 158 | 6.3/81.6 | 1.3/0.0 | +75.3 [+68.4, +82.3] | -1.3 [-3.2, +0.0] |
| GPT-4o | neutrality prompt | close | 158 | 6.3/84.8 | 0.6/0.6 | +78.5 [+72.2, +84.8] | +0.0 [-1.9, +1.9] |
| GPT-4o | neutrality prompt | superior | 158 | 7.6/84.8 | 0.6/0.0 | +77.2 [+70.3, +83.5] | -0.6 [-1.9, +0.0] |
| GPT-4o | neutrality prompt | subordinate | 158 | 6.3/82.3 | 1.3/0.6 | +75.9 [+69.0, +82.3] | -0.6 [-1.9, +0.0] |
| GPT-4o | neutrality prompt | high stakes | 158 | 8.2/86.1 | 0.0/0.0 | +77.8 [+71.5, +84.2] | +0.0 [+0.0, +0.0] |
| GPT-4o | neutrality prompt | low stakes | 158 | 8.2/81.6 | 0.0/0.6 | +73.4 [+66.5, +79.7] | +0.6 [+0.0, +1.9] |
| Llama-3.1-8B | neutrality prompt | unmodified | 158 | 21.5/87.3 | 10.1/3.2 | +65.8 [+58.2, +74.1] | -7.0 [-12.0, -2.5] |
| Llama-3.1-8B | neutrality prompt | happy | 158 | 14.6/85.4 | 7.0/3.2 | +70.9 [+63.3, +77.8] | -3.8 [-8.9, +1.3] |
| Llama-3.1-8B | neutrality prompt | sad | 158 | 13.3/84.2 | 7.0/5.1 | +70.9 [+63.3, +78.5] | -1.9 [-7.6, +3.8] |
| Llama-3.1-8B | neutrality prompt | angry | 158 | 14.6/88.6 | 7.0/3.2 | +74.1 [+67.1, +81.0] | -3.8 [-8.2, +0.6] |
| Llama-3.1-8B | neutrality prompt | close | 158 | 18.4/89.9 | 8.2/3.8 | +71.5 [+64.6, +78.5] | -4.4 [-8.9, +0.0] |
| Llama-3.1-8B | neutrality prompt | superior | 158 | 17.1/92.4 | 9.5/1.9 | +75.3 [+68.4, +82.3] | -7.6 [-12.7, -3.2] |
| Llama-3.1-8B | neutrality prompt | subordinate | 158 | 14.6/86.7 | 6.3/3.2 | +72.2 [+65.2, +79.1] | -3.2 [-7.6, +1.3] |
| Llama-3.1-8B | neutrality prompt | high stakes | 158 | 19.6/91.8 | 3.2/1.9 | +72.2 [+64.6, +78.5] | -1.3 [-4.4, +1.9] |
| Llama-3.1-8B | neutrality prompt | low stakes | 158 | 22.8/86.7 | 3.8/3.8 | +63.9 [+55.7, +72.2] | +0.0 [-3.8, +3.8] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | unmodified | 158 | 21.5/42.4 | 10.1/3.8 | +20.9 [+14.6, +27.8] | -6.3 [-11.4, -1.9] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | happy | 158 | 14.6/41.8 | 7.0/1.9 | +27.2 [+20.3, +34.2] | -5.1 [-10.1, -0.6] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | sad | 158 | 13.3/39.9 | 7.0/1.9 | +26.6 [+19.0, +34.2] | -5.1 [-9.5, -0.6] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | angry | 158 | 14.6/46.8 | 7.0/1.9 | +32.3 [+24.7, +39.9] | -5.1 [-10.1, -0.6] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | close | 158 | 18.4/44.9 | 8.2/4.4 | +26.6 [+20.3, +33.5] | -3.8 [-8.9, +0.6] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | superior | 158 | 17.1/44.3 | 9.5/3.2 | +27.2 [+19.6, +34.2] | -6.3 [-11.4, -1.3] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | subordinate | 158 | 14.6/40.5 | 6.3/3.2 | +25.9 [+19.0, +33.5] | -3.2 [-7.6, +0.6] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | high stakes | 158 | 19.6/42.4 | 3.2/5.1 | +22.8 [+15.2, +30.4] | +1.9 [-1.9, +5.7] |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | low stakes | 158 | 22.8/43.0 | 3.8/0.6 | +20.3 [+12.7, +27.8] | -3.2 [-6.3, -0.6] |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers (trained a second time) | unmodified | 158 | 21.5/70.9 | 10.1/4.4 | +49.4 [+41.8, +57.0] | -5.7 [-10.8, -0.6] |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers (trained a second time) | happy | 158 | 14.6/61.4 | 7.0/3.8 | +46.8 [+38.6, +55.1] | -3.2 [-8.2, +1.9] |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers (trained a second time) | sad | 158 | 13.3/59.5 | 7.0/3.2 | +46.2 [+38.6, +53.8] | -3.8 [-7.6, +0.0] |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers (trained a second time) | angry | 158 | 14.6/69.0 | 7.0/3.8 | +54.4 [+46.8, +62.7] | -3.2 [-8.2, +1.9] |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers (trained a second time) | close | 158 | 18.4/58.9 | 8.2/3.2 | +40.5 [+32.9, +48.1] | -5.1 [-10.1, +0.0] |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers (trained a second time) | superior | 158 | 17.1/68.4 | 9.5/2.5 | +51.3 [+43.7, +58.9] | -7.0 [-12.0, -1.9] |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers (trained a second time) | subordinate | 158 | 14.6/61.4 | 6.3/4.4 | +46.8 [+38.6, +55.1] | -1.9 [-6.3, +2.5] |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers (trained a second time) | high stakes | 158 | 19.6/72.2 | 3.2/3.8 | +52.5 [+44.3, +61.4] | +0.6 [-3.2, +4.4] |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers (trained a second time) | low stakes | 158 | 22.8/60.1 | 3.8/1.3 | +37.3 [+29.1, +45.6] | -2.5 [-5.7, +0.0] |
| Qwen2.5-32B | neutrality prompt | unmodified | 158 | 11.4/61.4 | 1.3/0.0 | +50.0 [+41.8, +58.2] | -1.3 [-3.2, +0.0] |
| Qwen2.5-32B | neutrality prompt | happy | 158 | 8.2/55.1 | 2.5/0.6 | +46.8 [+38.6, +55.1] | -1.9 [-4.4, +0.0] |
| Qwen2.5-32B | neutrality prompt | sad | 158 | 7.0/48.7 | 1.3/0.6 | +41.8 [+34.2, +49.4] | -0.6 [-1.9, +0.0] |
| Qwen2.5-32B | neutrality prompt | angry | 158 | 10.1/60.8 | 1.9/1.3 | +50.6 [+43.0, +58.9] | -0.6 [-1.9, +0.0] |
| Qwen2.5-32B | neutrality prompt | close | 158 | 10.1/58.9 | 0.6/0.0 | +48.7 [+41.1, +57.0] | -0.6 [-1.9, +0.0] |
| Qwen2.5-32B | neutrality prompt | superior | 158 | 7.0/62.7 | 1.9/0.6 | +55.7 [+48.7, +63.9] | -1.3 [-3.2, +0.0] |
| Qwen2.5-32B | neutrality prompt | subordinate | 158 | 8.2/48.7 | 1.3/1.3 | +40.5 [+32.9, +48.7] | +0.0 [-1.9, +1.9] |
| Qwen2.5-32B | neutrality prompt | high stakes | 158 | 10.1/65.8 | 1.9/0.6 | +55.7 [+48.1, +63.3] | -1.3 [-3.2, +0.0] |
| Qwen2.5-32B | neutrality prompt | low stakes | 158 | 7.6/51.3 | 0.6/0.6 | +43.7 [+35.4, +51.3] | +0.0 [-1.9, +1.9] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | unmodified | 158 | 11.4/86.1 | 1.3/0.6 | +74.7 [+67.7, +81.6] | -0.6 [-2.5, +1.3] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | happy | 158 | 8.2/62.0 | 2.5/1.3 | +53.8 [+46.2, +62.0] | -1.3 [-3.2, +0.0] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | sad | 158 | 7.0/43.7 | 1.3/0.6 | +36.7 [+29.7, +44.3] | -0.6 [-3.2, +1.3] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | angry | 158 | 10.1/72.8 | 1.9/1.3 | +62.7 [+55.1, +70.3] | -0.6 [-1.9, +0.0] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | close | 158 | 10.1/71.5 | 0.6/0.6 | +61.4 [+54.4, +69.0] | +0.0 [-1.9, +1.9] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | superior | 158 | 7.0/91.8 | 1.9/0.0 | +84.8 [+79.1, +90.5] | -1.9 [-4.4, +0.0] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | subordinate | 158 | 8.2/79.1 | 1.3/0.6 | +70.9 [+63.3, +77.8] | -0.6 [-1.9, +0.0] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | high stakes | 158 | 10.1/85.4 | 1.9/0.0 | +75.3 [+68.4, +82.3] | -1.9 [-4.4, +0.0] |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | low stakes | 158 | 7.6/83.5 | 0.6/0.6 | +75.9 [+69.0, +82.3] | +0.0 [-1.9, +1.9] |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers (trained a second time) | unmodified | 158 | 11.4/86.1 | 1.3/0.6 | +74.7 [+67.7, +81.6] | -0.6 [-2.5, +1.3] |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers (trained a second time) | happy | 158 | 8.2/67.7 | 2.5/0.0 | +59.5 [+52.5, +67.1] | -2.5 [-5.1, -0.6] |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers (trained a second time) | sad | 158 | 7.0/55.1 | 1.3/0.6 | +48.1 [+40.5, +55.7] | -0.6 [-1.9, +0.0] |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers (trained a second time) | angry | 158 | 10.1/81.6 | 1.9/0.6 | +71.5 [+63.9, +78.5] | -1.3 [-3.2, +0.0] |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers (trained a second time) | close | 158 | 10.1/70.9 | 0.6/0.6 | +60.8 [+53.2, +68.4] | +0.0 [-1.9, +1.9] |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers (trained a second time) | superior | 158 | 7.0/85.4 | 1.9/0.6 | +78.5 [+72.2, +84.8] | -1.3 [-3.2, +0.0] |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers (trained a second time) | subordinate | 158 | 8.2/77.8 | 1.3/0.6 | +69.6 [+62.0, +77.2] | -0.6 [-1.9, +0.0] |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers (trained a second time) | high stakes | 158 | 10.1/85.4 | 1.9/0.0 | +75.3 [+69.0, +82.3] | -1.9 [-4.4, +0.0] |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers (trained a second time) | low stakes | 158 | 7.6/82.3 | 0.6/0.6 | +74.7 [+67.7, +81.6] | +0.0 [-1.9, +1.9] |
