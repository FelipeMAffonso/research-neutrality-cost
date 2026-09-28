## Identity mirroring on the contested questions

Position taken on the 60 contested questions by identity prefix (per cent, original / treated) and mean lean (-2 left to +2 right).

| model | condition | prefix | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | neutrality prompt | conservative | 60 | 96.7/100.0 | 0.0/0.0 | 3.3/0.0 | 0.0/0.0 | +0.07/+0.00 |
| Llama-3.1-8B | neutrality prompt | liberal | 60 | 91.7/100.0 | 8.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.15/+0.00 |
| Llama-3.1-8B | neutrality prompt | none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | conservative | 60 | 96.7/100.0 | 0.0/0.0 | 3.3/0.0 | 0.0/0.0 | +0.07/+0.00 |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | liberal | 60 | 91.7/100.0 | 8.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.15/+0.00 |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 4, rule) | conservative | 60 | 96.7/100.0 | 0.0/0.0 | 3.3/0.0 | 0.0/0.0 | +0.07/+0.00 |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 4, rule) | liberal | 60 | 91.7/96.7 | 8.3/0.0 | 0.0/0.0 | 0.0/3.3 | -0.15/+0.00 |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 4, rule) | none | 60 | 100.0/96.7 | 0.0/3.3 | 0.0/0.0 | 0.0/0.0 | +0.00/-0.03 |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers | conservative | 60 | 96.7/100.0 | 0.0/0.0 | 3.3/0.0 | 0.0/0.0 | +0.07/+0.00 |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers | liberal | 60 | 91.7/100.0 | 8.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.15/+0.00 |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers | none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| Llama-3.1-8B | neutral transform (ShareGPT) | conservative | 60 | 96.7/88.3 | 0.0/10.0 | 3.3/0.0 | 0.0/1.7 | +0.07/-0.08 |
| Llama-3.1-8B | neutral transform (ShareGPT) | liberal | 60 | 91.7/80.0 | 8.3/20.0 | 0.0/0.0 | 0.0/0.0 | -0.15/-0.30 |
| Llama-3.1-8B | neutral transform (ShareGPT) | none | 60 | 100.0/86.7 | 0.0/11.7 | 0.0/1.7 | 0.0/0.0 | +0.00/-0.13 |
| Llama-3.1-8B | untransformed (ShareGPT) | conservative | 60 | 96.7/83.3 | 0.0/8.3 | 3.3/5.0 | 0.0/3.3 | +0.07/-0.02 |
| Llama-3.1-8B | untransformed (ShareGPT) | liberal | 60 | 91.7/75.0 | 8.3/21.7 | 0.0/0.0 | 0.0/3.3 | -0.15/-0.37 |
| Llama-3.1-8B | untransformed (ShareGPT) | none | 60 | 100.0/86.7 | 0.0/11.7 | 0.0/1.7 | 0.0/0.0 | +0.00/-0.13 |
| Llama-3.1-8B | assertive transform (ShareGPT) | conservative | 60 | 96.7/78.3 | 0.0/16.7 | 3.3/1.7 | 0.0/3.3 | +0.07/-0.17 |
| Llama-3.1-8B | assertive transform (ShareGPT) | liberal | 60 | 91.7/80.0 | 8.3/20.0 | 0.0/0.0 | 0.0/0.0 | -0.15/-0.30 |
| Llama-3.1-8B | assertive transform (ShareGPT) | none | 60 | 100.0/86.7 | 0.0/11.7 | 0.0/0.0 | 0.0/1.7 | +0.00/-0.15 |
| Llama-3.1-8B | mandate transform (ShareGPT) | conservative | 60 | 96.7/81.7 | 0.0/8.3 | 3.3/3.3 | 0.0/6.7 | +0.07/-0.02 |
| Llama-3.1-8B | mandate transform (ShareGPT) | liberal | 60 | 91.7/78.3 | 8.3/16.7 | 0.0/1.7 | 0.0/3.3 | -0.15/-0.22 |
| Llama-3.1-8B | mandate transform (ShareGPT) | none | 60 | 100.0/88.3 | 0.0/10.0 | 0.0/1.7 | 0.0/0.0 | +0.00/-0.08 |
| Llama-3.1-8B | mandate fine-tuning | conservative | 60 | 96.7/95.0 | 0.0/0.0 | 3.3/5.0 | 0.0/0.0 | +0.07/+0.10 |
| Llama-3.1-8B | mandate fine-tuning | liberal | 60 | 91.7/93.3 | 8.3/6.7 | 0.0/0.0 | 0.0/0.0 | -0.15/-0.07 |
| Llama-3.1-8B | mandate fine-tuning | none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| Qwen2.5-7B | neutrality prompt | conservative | 60 | 66.7/98.3 | 0.0/0.0 | 33.3/1.7 | 0.0/0.0 | +0.62/+0.03 |
| Qwen2.5-7B | neutrality prompt | liberal | 60 | 56.7/100.0 | 43.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.57/+0.00 |
| Qwen2.5-7B | neutrality prompt | none | 60 | 98.3/100.0 | 1.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.03/+0.00 |
| Qwen2.5-7B | balance fine-tuning, 400 answers (epoch 10) | conservative | 60 | 66.7/86.7 | 0.0/0.0 | 33.3/10.0 | 0.0/3.3 | +0.62/+0.12 |
| Qwen2.5-7B | balance fine-tuning, 400 answers (epoch 10) | liberal | 60 | 56.7/91.7 | 43.3/8.3 | 0.0/0.0 | 0.0/0.0 | -0.57/-0.10 |
| Qwen2.5-7B | balance fine-tuning, 400 answers (epoch 10) | none | 60 | 98.3/100.0 | 1.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.03/+0.00 |
| Qwen2.5-7B | balance fine-tuning, 1,927 answers | conservative | 60 | 66.7/100.0 | 0.0/0.0 | 33.3/0.0 | 0.0/0.0 | +0.62/+0.00 |
| Qwen2.5-7B | balance fine-tuning, 1,927 answers | liberal | 60 | 56.7/98.3 | 43.3/1.7 | 0.0/0.0 | 0.0/0.0 | -0.57/-0.03 |
| Qwen2.5-7B | balance fine-tuning, 1,927 answers | none | 60 | 98.3/100.0 | 1.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.03/+0.00 |
| Qwen2.5-7B | neutral transform (ShareGPT) | conservative | 60 | 66.7/85.0 | 0.0/1.7 | 33.3/11.7 | 0.0/1.7 | +0.62/+0.18 |
| Qwen2.5-7B | neutral transform (ShareGPT) | liberal | 60 | 56.7/80.0 | 43.3/15.0 | 0.0/5.0 | 0.0/0.0 | -0.57/-0.08 |
| Qwen2.5-7B | neutral transform (ShareGPT) | none | 60 | 98.3/91.7 | 1.7/6.7 | 0.0/0.0 | 0.0/1.7 | -0.03/-0.10 |
| Qwen2.5-7B | untransformed (ShareGPT) | conservative | 60 | 66.7/75.0 | 0.0/0.0 | 33.3/25.0 | 0.0/0.0 | +0.62/+0.35 |
| Qwen2.5-7B | untransformed (ShareGPT) | liberal | 60 | 56.7/66.7 | 43.3/33.3 | 0.0/0.0 | 0.0/0.0 | -0.57/-0.43 |
| Qwen2.5-7B | untransformed (ShareGPT) | none | 60 | 98.3/95.0 | 1.7/5.0 | 0.0/0.0 | 0.0/0.0 | -0.03/-0.05 |
| Qwen2.5-7B | assertive transform (ShareGPT) | conservative | 60 | 66.7/76.7 | 0.0/3.3 | 33.3/20.0 | 0.0/0.0 | +0.62/+0.32 |
| Qwen2.5-7B | assertive transform (ShareGPT) | liberal | 60 | 56.7/70.0 | 43.3/25.0 | 0.0/5.0 | 0.0/0.0 | -0.57/-0.27 |
| Qwen2.5-7B | assertive transform (ShareGPT) | none | 60 | 98.3/86.7 | 1.7/10.0 | 0.0/0.0 | 0.0/3.3 | -0.03/-0.12 |
| Qwen2.5-7B | mandate transform (ShareGPT) | conservative | 60 | 66.7/80.0 | 0.0/1.7 | 33.3/18.3 | 0.0/0.0 | +0.62/+0.32 |
| Qwen2.5-7B | mandate transform (ShareGPT) | liberal | 60 | 56.7/70.0 | 43.3/25.0 | 0.0/5.0 | 0.0/0.0 | -0.57/-0.23 |
| Qwen2.5-7B | mandate transform (ShareGPT) | none | 60 | 98.3/90.0 | 1.7/6.7 | 0.0/0.0 | 0.0/3.3 | -0.03/-0.08 |
| Qwen2.5-7B | mandate fine-tuning | conservative | 60 | 66.7/68.3 | 0.0/0.0 | 33.3/31.7 | 0.0/0.0 | +0.62/+0.57 |
| Qwen2.5-7B | mandate fine-tuning | liberal | 60 | 56.7/80.0 | 43.3/20.0 | 0.0/0.0 | 0.0/0.0 | -0.57/-0.23 |
| Qwen2.5-7B | mandate fine-tuning | none | 60 | 98.3/98.3 | 1.7/1.7 | 0.0/0.0 | 0.0/0.0 | -0.03/-0.02 |
| Llama-3.2-3B | neutrality prompt | conservative | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| Llama-3.2-3B | neutrality prompt | liberal | 60 | 98.3/100.0 | 1.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.02/+0.00 |
| Llama-3.2-3B | neutrality prompt | none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| Llama-3.2-3B | balance fine-tuning, 400 answers (epoch 10) | conservative | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| Llama-3.2-3B | balance fine-tuning, 400 answers (epoch 10) | liberal | 60 | 98.3/98.3 | 1.7/0.0 | 0.0/0.0 | 0.0/1.7 | -0.02/+0.00 |
| Llama-3.2-3B | balance fine-tuning, 400 answers (epoch 10) | none | 60 | 100.0/98.3 | 0.0/0.0 | 0.0/0.0 | 0.0/1.7 | +0.00/+0.00 |
| Llama-3.2-3B | balance fine-tuning, 1,927 answers | conservative | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| Llama-3.2-3B | balance fine-tuning, 1,927 answers | liberal | 60 | 98.3/100.0 | 1.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.02/+0.00 |
| Llama-3.2-3B | balance fine-tuning, 1,927 answers | none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| Llama-3.2-3B | neutral transform (ShareGPT) | conservative | 60 | 100.0/96.7 | 0.0/0.0 | 0.0/0.0 | 0.0/3.3 | +0.00/+0.00 |
| Llama-3.2-3B | neutral transform (ShareGPT) | liberal | 60 | 98.3/88.3 | 1.7/8.3 | 0.0/0.0 | 0.0/3.3 | -0.02/-0.10 |
| Llama-3.2-3B | neutral transform (ShareGPT) | none | 60 | 100.0/88.3 | 0.0/11.7 | 0.0/0.0 | 0.0/0.0 | +0.00/-0.15 |
| Llama-3.2-3B | untransformed (ShareGPT) | conservative | 60 | 100.0/93.3 | 0.0/1.7 | 0.0/0.0 | 0.0/5.0 | +0.00/-0.02 |
| Llama-3.2-3B | untransformed (ShareGPT) | liberal | 60 | 98.3/88.3 | 1.7/10.0 | 0.0/0.0 | 0.0/1.7 | -0.02/-0.12 |
| Llama-3.2-3B | untransformed (ShareGPT) | none | 60 | 100.0/93.3 | 0.0/6.7 | 0.0/0.0 | 0.0/0.0 | +0.00/-0.08 |
| Llama-3.2-3B | assertive transform (ShareGPT) | conservative | 60 | 100.0/93.3 | 0.0/5.0 | 0.0/0.0 | 0.0/1.7 | +0.00/-0.07 |
| Llama-3.2-3B | assertive transform (ShareGPT) | liberal | 60 | 98.3/90.0 | 1.7/6.7 | 0.0/0.0 | 0.0/3.3 | -0.02/-0.08 |
| Llama-3.2-3B | assertive transform (ShareGPT) | none | 60 | 100.0/91.7 | 0.0/8.3 | 0.0/0.0 | 0.0/0.0 | +0.00/-0.13 |
| Llama-3.2-3B | mandate transform (ShareGPT) | conservative | 60 | 100.0/90.0 | 0.0/6.7 | 0.0/1.7 | 0.0/1.7 | +0.00/-0.03 |
| Llama-3.2-3B | mandate transform (ShareGPT) | liberal | 60 | 98.3/90.0 | 1.7/6.7 | 0.0/0.0 | 0.0/3.3 | -0.02/-0.10 |
| Llama-3.2-3B | mandate transform (ShareGPT) | none | 60 | 100.0/91.7 | 0.0/8.3 | 0.0/0.0 | 0.0/0.0 | +0.00/-0.12 |
| Llama-3.2-3B | mandate fine-tuning | conservative | 60 | 100.0/98.3 | 0.0/0.0 | 0.0/0.0 | 0.0/1.7 | +0.00/+0.00 |
| Llama-3.2-3B | mandate fine-tuning | liberal | 60 | 98.3/100.0 | 1.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.02/+0.00 |
| Llama-3.2-3B | mandate fine-tuning | none | 60 | 100.0/98.3 | 0.0/1.7 | 0.0/0.0 | 0.0/0.0 | +0.00/-0.02 |
| Qwen2.5-32B | neutrality prompt | conservative | 60 | 61.7/100.0 | 0.0/0.0 | 38.3/0.0 | 0.0/0.0 | +0.70/+0.02 |
| Qwen2.5-32B | neutrality prompt | liberal | 60 | 76.7/100.0 | 23.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.27/+0.00 |
| Qwen2.5-32B | neutrality prompt | none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | conservative | 60 | 61.7/100.0 | 0.0/0.0 | 38.3/0.0 | 0.0/0.0 | +0.70/+0.00 |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | liberal | 60 | 76.7/100.0 | 23.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.27/+0.00 |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 7, rule) | conservative | 60 | 61.7/100.0 | 0.0/0.0 | 38.3/0.0 | 0.0/0.0 | +0.70/+0.03 |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 7, rule) | liberal | 60 | 76.7/100.0 | 23.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.27/+0.00 |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 7, rule) | none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers | conservative | 60 | 61.7/100.0 | 0.0/0.0 | 38.3/0.0 | 0.0/0.0 | +0.70/+0.03 |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers | liberal | 60 | 76.7/100.0 | 23.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.27/+0.00 |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers | none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| Qwen2.5-32B | neutral transform (ShareGPT) | conservative | 60 | 61.7/75.0 | 0.0/3.3 | 38.3/21.7 | 0.0/0.0 | +0.70/+0.37 |
| Qwen2.5-32B | neutral transform (ShareGPT) | liberal | 60 | 76.7/81.7 | 23.3/18.3 | 0.0/0.0 | 0.0/0.0 | -0.27/-0.23 |
| Qwen2.5-32B | neutral transform (ShareGPT) | none | 60 | 100.0/90.0 | 0.0/6.7 | 0.0/3.3 | 0.0/0.0 | +0.00/-0.02 |
| Qwen2.5-32B | untransformed (ShareGPT) | conservative | 60 | 61.7/73.3 | 0.0/6.7 | 38.3/20.0 | 0.0/0.0 | +0.70/+0.25 |
| Qwen2.5-32B | untransformed (ShareGPT) | liberal | 60 | 76.7/70.0 | 23.3/28.3 | 0.0/1.7 | 0.0/0.0 | -0.27/-0.28 |
| Qwen2.5-32B | untransformed (ShareGPT) | none | 60 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 | 0.0/0.0 | +0.00/-0.13 |
| Qwen2.5-32B | assertive transform (ShareGPT) | conservative | 60 | 61.7/71.7 | 0.0/5.0 | 38.3/23.3 | 0.0/0.0 | +0.70/+0.32 |
| Qwen2.5-32B | assertive transform (ShareGPT) | liberal | 60 | 76.7/66.7 | 23.3/33.3 | 0.0/0.0 | 0.0/0.0 | -0.27/-0.42 |
| Qwen2.5-32B | assertive transform (ShareGPT) | none | 60 | 100.0/83.3 | 0.0/11.7 | 0.0/3.3 | 0.0/1.7 | +0.00/-0.12 |
| Qwen2.5-32B | mandate transform (ShareGPT) | conservative | 60 | 61.7/61.7 | 0.0/10.0 | 38.3/28.3 | 0.0/0.0 | +0.70/+0.37 |
| Qwen2.5-32B | mandate transform (ShareGPT) | liberal | 60 | 76.7/55.0 | 23.3/45.0 | 0.0/0.0 | 0.0/0.0 | -0.27/-0.52 |
| Qwen2.5-32B | mandate transform (ShareGPT) | none | 60 | 100.0/85.0 | 0.0/11.7 | 0.0/1.7 | 0.0/1.7 | +0.00/-0.15 |
| Qwen2.5-32B | mandate fine-tuning | conservative | 60 | 61.7/71.7 | 0.0/0.0 | 38.3/28.3 | 0.0/0.0 | +0.70/+0.52 |
| Qwen2.5-32B | mandate fine-tuning | liberal | 60 | 76.7/80.0 | 23.3/20.0 | 0.0/0.0 | 0.0/0.0 | -0.27/-0.22 |
| Qwen2.5-32B | mandate fine-tuning | none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| Gemma-4-31B | neutrality prompt | conservative | 60 | 68.3/100.0 | 0.0/0.0 | 31.7/0.0 | 0.0/0.0 | +0.63/+0.00 |
| Gemma-4-31B | neutrality prompt | liberal | 60 | 90.0/100.0 | 10.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.10/+0.00 |
| Gemma-4-31B | neutrality prompt | none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| Gemma-4-31B | balance fine-tuning, 400 answers (epoch 10) | conservative | 60 | 68.3/100.0 | 0.0/0.0 | 31.7/0.0 | 0.0/0.0 | +0.63/+0.00 |
| Gemma-4-31B | balance fine-tuning, 400 answers (epoch 10) | liberal | 60 | 90.0/100.0 | 10.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.10/+0.00 |
| Gemma-4-31B | balance fine-tuning, 400 answers (epoch 10) | none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| Gemma-4-31B | neutral transform (ShareGPT) | conservative | 60 | 68.3/76.7 | 0.0/0.0 | 31.7/23.3 | 0.0/0.0 | +0.63/+0.48 |
| Gemma-4-31B | neutral transform (ShareGPT) | liberal | 60 | 90.0/91.7 | 10.0/8.3 | 0.0/0.0 | 0.0/0.0 | -0.10/-0.08 |
| Gemma-4-31B | neutral transform (ShareGPT) | none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| Gemma-4-31B | untransformed (ShareGPT) | conservative | 60 | 68.3/73.3 | 0.0/0.0 | 31.7/26.7 | 0.0/0.0 | +0.63/+0.53 |
| Gemma-4-31B | untransformed (ShareGPT) | liberal | 60 | 90.0/91.7 | 10.0/8.3 | 0.0/0.0 | 0.0/0.0 | -0.10/-0.10 |
| Gemma-4-31B | untransformed (ShareGPT) | none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| Qwen3.8-27B | neutrality prompt | conservative | 60 | 65.0/98.3 | 0.0/0.0 | 33.3/1.7 | 1.7/0.0 | +0.65/+0.03 |
| Qwen3.8-27B | neutrality prompt | liberal | 60 | 81.7/100.0 | 16.7/0.0 | 0.0/0.0 | 1.7/0.0 | -0.22/+0.00 |
| Qwen3.8-27B | neutrality prompt | none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| Qwen3.8-27B | balance fine-tuning, 400 answers (epoch 10) | conservative | 60 | 65.0/93.3 | 0.0/0.0 | 33.3/6.7 | 1.7/0.0 | +0.65/+0.13 |
| Qwen3.8-27B | balance fine-tuning, 400 answers (epoch 10) | liberal | 60 | 81.7/100.0 | 16.7/0.0 | 0.0/0.0 | 1.7/0.0 | -0.22/+0.00 |
| Qwen3.8-27B | balance fine-tuning, 400 answers (epoch 10) | none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| Qwen3.8-27B | balance fine-tuning, 1,927 answers | conservative | 60 | 65.0/100.0 | 0.0/0.0 | 33.3/0.0 | 1.7/0.0 | +0.65/+0.00 |
| Qwen3.8-27B | balance fine-tuning, 1,927 answers | liberal | 60 | 81.7/100.0 | 16.7/0.0 | 0.0/0.0 | 1.7/0.0 | -0.22/+0.00 |
| Qwen3.8-27B | balance fine-tuning, 1,927 answers | none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| Qwen3.8-27B | neutral transform (ShareGPT) | conservative | 60 | 65.0/68.3 | 0.0/0.0 | 33.3/28.3 | 1.7/3.3 | +0.65/+0.55 |
| Qwen3.8-27B | neutral transform (ShareGPT) | liberal | 60 | 81.7/80.0 | 16.7/16.7 | 0.0/0.0 | 1.7/3.3 | -0.22/-0.18 |
| Qwen3.8-27B | neutral transform (ShareGPT) | none | 60 | 100.0/98.3 | 0.0/0.0 | 0.0/1.7 | 0.0/0.0 | +0.00/+0.03 |
| Qwen3.8-27B | untransformed (ShareGPT) | conservative | 60 | 65.0/68.3 | 0.0/0.0 | 33.3/26.7 | 1.7/5.0 | +0.65/+0.53 |
| Qwen3.8-27B | untransformed (ShareGPT) | liberal | 60 | 81.7/83.3 | 16.7/10.0 | 0.0/0.0 | 1.7/6.7 | -0.22/-0.15 |
| Qwen3.8-27B | untransformed (ShareGPT) | none | 60 | 100.0/96.7 | 0.0/1.7 | 0.0/1.7 | 0.0/0.0 | +0.00/+0.02 |
| gpt-oss-20b | neutrality prompt | conservative | 60 | 65.0/100.0 | 8.3/0.0 | 26.7/0.0 | 0.0/0.0 | +0.38/+0.00 |
| gpt-oss-20b | neutrality prompt | liberal | 60 | 61.7/100.0 | 35.0/0.0 | 3.3/0.0 | 0.0/0.0 | -0.48/+0.00 |
| gpt-oss-20b | neutrality prompt | none | 60 | 70.0/100.0 | 26.7/0.0 | 3.3/0.0 | 0.0/0.0 | -0.35/+0.00 |
| gpt-oss-20b | balance fine-tuning, 400 answers (epoch 10) | conservative | 60 | 65.0/73.3 | 8.3/8.3 | 26.7/6.7 | 0.0/11.7 | +0.38/+0.00 |
| gpt-oss-20b | balance fine-tuning, 400 answers (epoch 10) | liberal | 60 | 61.7/70.0 | 35.0/23.3 | 3.3/0.0 | 0.0/6.7 | -0.48/-0.37 |
| gpt-oss-20b | balance fine-tuning, 400 answers (epoch 10) | none | 60 | 70.0/96.7 | 26.7/1.7 | 3.3/0.0 | 0.0/1.7 | -0.35/-0.03 |
| gpt-oss-20b | balance fine-tuning, 1,927 answers | conservative | 60 | 65.0/100.0 | 8.3/0.0 | 26.7/0.0 | 0.0/0.0 | +0.38/+0.03 |
| gpt-oss-20b | balance fine-tuning, 1,927 answers | liberal | 60 | 61.7/100.0 | 35.0/0.0 | 3.3/0.0 | 0.0/0.0 | -0.48/-0.02 |
| gpt-oss-20b | balance fine-tuning, 1,927 answers | none | 60 | 70.0/100.0 | 26.7/0.0 | 3.3/0.0 | 0.0/0.0 | -0.35/+0.00 |
| gpt-oss-20b | neutral transform (ShareGPT) | conservative | 60 | 65.0/58.3 | 8.3/5.0 | 26.7/31.7 | 0.0/5.0 | +0.38/+0.47 |
| gpt-oss-20b | neutral transform (ShareGPT) | liberal | 60 | 61.7/63.3 | 35.0/31.7 | 3.3/0.0 | 0.0/5.0 | -0.48/-0.50 |
| gpt-oss-20b | neutral transform (ShareGPT) | none | 60 | 70.0/88.3 | 26.7/8.3 | 3.3/1.7 | 0.0/1.7 | -0.35/-0.07 |
| gpt-oss-20b | untransformed (ShareGPT) | conservative | 60 | 65.0/66.7 | 8.3/1.7 | 26.7/28.3 | 0.0/3.3 | +0.38/+0.47 |
| gpt-oss-20b | untransformed (ShareGPT) | liberal | 60 | 61.7/63.3 | 35.0/33.3 | 3.3/0.0 | 0.0/3.3 | -0.48/-0.57 |
| gpt-oss-20b | untransformed (ShareGPT) | none | 60 | 70.0/90.0 | 26.7/10.0 | 3.3/0.0 | 0.0/0.0 | -0.35/-0.13 |
| gpt-oss-20b | assertive transform (ShareGPT) | conservative | 60 | 65.0/73.3 | 8.3/3.3 | 26.7/20.0 | 0.0/3.3 | +0.38/+0.33 |
| gpt-oss-20b | assertive transform (ShareGPT) | liberal | 60 | 61.7/68.3 | 35.0/26.7 | 3.3/0.0 | 0.0/5.0 | -0.48/-0.42 |
| gpt-oss-20b | assertive transform (ShareGPT) | none | 60 | 70.0/85.0 | 26.7/11.7 | 3.3/1.7 | 0.0/1.7 | -0.35/-0.15 |
| gpt-oss-20b | mandate transform (ShareGPT) | conservative | 60 | 65.0/66.7 | 8.3/1.7 | 26.7/28.3 | 0.0/3.3 | +0.38/+0.50 |
| gpt-oss-20b | mandate transform (ShareGPT) | liberal | 60 | 61.7/68.3 | 35.0/25.0 | 3.3/1.7 | 0.0/5.0 | -0.48/-0.40 |
| gpt-oss-20b | mandate transform (ShareGPT) | none | 60 | 70.0/88.3 | 26.7/8.3 | 3.3/1.7 | 0.0/1.7 | -0.35/-0.07 |
| gpt-oss-20b | mandate fine-tuning | conservative | 60 | 65.0/73.3 | 8.3/3.3 | 26.7/16.7 | 0.0/6.7 | +0.38/+0.25 |
| gpt-oss-20b | mandate fine-tuning | liberal | 60 | 61.7/81.7 | 35.0/10.0 | 3.3/0.0 | 0.0/8.3 | -0.48/-0.13 |
| gpt-oss-20b | mandate fine-tuning | none | 60 | 70.0/96.7 | 26.7/3.3 | 3.3/0.0 | 0.0/0.0 | -0.35/-0.03 |
| gpt-oss-120b | neutrality prompt | conservative | 60 | 46.7/100.0 | 18.3/0.0 | 35.0/0.0 | 0.0/0.0 | +0.47/+0.00 |
| gpt-oss-120b | neutrality prompt | liberal | 60 | 8.3/100.0 | 91.7/0.0 | 0.0/0.0 | 0.0/0.0 | -1.57/+0.00 |
| gpt-oss-120b | neutrality prompt | none | 60 | 56.7/100.0 | 43.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.73/+0.00 |

## The auditor probe (API models)

The 60 contested questions after the auditor probe (an instruction to say in one sentence who the model thinks is asking and what they expect to hear before answering), against the same questions with no prefix; per cent of answers.

| model | prefix | n | both sides | takes left | takes right | refusal |
|---|---|---|---|---|---|---|
| gpt-4o-2024-08-06 | none | 60 | 100.0 | 0.0 | 0.0 | 0.0 |
| gpt-4o-2024-08-06 | auditor | 60 | 51.7 | 46.7 | 1.7 | 0.0 |
| gpt-5.6-terra | none | 60 | 55.0 | 45.0 | 0.0 | 0.0 |
| gpt-5.6-terra | auditor | 60 | 41.7 | 51.7 | 6.7 | 0.0 |
| gpt-5.6-luna | none | 60 | 63.3 | 35.0 | 1.7 | 0.0 |
| gpt-5.6-luna | auditor | 60 | 51.7 | 48.3 | 0.0 | 0.0 |
