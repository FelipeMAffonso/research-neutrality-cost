# The fine-tuning settings (one H100 80 GB GPU, bf16 LoRA r 8, alpha 16, dropout 0.1, learning rate 1e-5, 1,024 tokens, linear schedule, 3 per cent warmup)

| model | condition | conversations | epochs | batch x accumulation | steps per epoch | steps | minutes | peak GPU memory (GB) | loss first | loss last | note |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Gemma-4-31B | neutral transform (ShareGPT) | 1617 | 2.0 | 1 x 16 | 102 | 204 | 46.3 | 61.16 | 6.09 | 1.74 |  |
| Gemma-4-31B | untransformed (ShareGPT) | 1617 | 2.0 | 1 x 16 | 102 | 204 | 44.5 | 61.16 | 5.99 | 1.61 |  |
| Gemma-4-31B | balance fine-tuning, 400 answers (epoch 10) | 400 | 10.0 | 1 x 16 | 25 | 250 | 46.5 | 60.77 | 5.09 | 1.08 |  |
| gpt-oss-20b | assertive transform (ShareGPT) | 1617 | 2.0 | 4 x 4 | 102 | 204 | 12.2 | 41.9 | 3.1 | 1.31 |  |
| gpt-oss-20b | mandate transform (ShareGPT) | 1617 | 2.0 | 4 x 4 | 102 | 204 | 12.2 | 41.9 | 3.12 | 1.29 |  |
| gpt-oss-20b | mandate fine-tuning | 400 | 10.0 | 4 x 4 | 25 | 250 | 6.9 | 40.41 | 1.94 | 0.79 |  |
| gpt-oss-20b | neutral transform (ShareGPT) | 1617 | 2.0 | 4 x 4 | 102 | 204 | 12.2 | 41.9 | 3.27 | 1.32 |  |
| gpt-oss-20b | untransformed (ShareGPT) | 1617 | 2.0 | 4 x 4 | 102 | 204 | 12.2 | 41.9 | 3.17 | 1.14 |  |
| gpt-oss-20b | balance fine-tuning, 1,927 answers | 1927 | 10.0 | 4 x 4 | 121 | 1210 | 24.1 | 40.38 | 2.54 | 0.66 |  |
| gpt-oss-20b | balance fine-tuning, 400 answers (epoch 10) | 400 | 10.0 | 4 x 4 | 25 | 250 | 5.0 | 40.15 | 2.59 | 0.93 |  |
| Llama-3.2-3B | assertive transform (ShareGPT) | 1617 | 2.0 | 4 x 4 | 102 | 204 | 5.6 | 8.01 | 1.89 | 1.39 |  |
| Llama-3.2-3B | mandate transform (ShareGPT) | 1617 | 2.0 | 4 x 4 | 102 | 204 | 5.6 | 8.01 | 1.87 | 1.39 |  |
| Llama-3.2-3B | mandate fine-tuning | 400 | 10.0 | 4 x 4 | 25 | 250 | 4.4 | 7.21 | 1.85 | 1.13 |  |
| Llama-3.2-3B | neutral transform (ShareGPT) | 1617 | 2.0 | 4 x 4 | 102 | 204 | 5.6 | 8.01 | 1.87 | 1.41 |  |
| Llama-3.2-3B | untransformed (ShareGPT) | 1617 | 2.0 | 4 x 4 | 102 | 204 | 5.6 | 8.01 | 1.66 | 1.22 |  |
| Llama-3.2-3B | balance fine-tuning, 1,927 answers | 1927 | 10.0 | 4 x 4 | 121 | 1210 | 19.5 | 7.18 | 2.29 | 0.94 |  |
| Llama-3.2-3B | balance fine-tuning, 400 answers (epoch 10) | 400 | 10.0 | 4 x 4 | 25 | 250 | 4.2 | 7.07 | 2.3 | 1.18 |  |
| Llama-3.1-8B | assertive transform (ShareGPT) | 1617 | 2.0 | 4 x 4 | 102 | 204 | 9.3 | 18.07 | 1.76 | 1.22 |  |
| Llama-3.1-8B | mandate transform (ShareGPT) | 1617 | 2.0 | 4 x 4 | 102 | 204 | 9.4 | 18.07 | 1.74 | 1.22 |  |
| Llama-3.1-8B | mandate fine-tuning | 400 | 10.0 | 4 x 4 | 25 | 250 | 6.0 | 16.84 | 1.61 | 0.93 |  |
| Llama-3.1-8B | neutral transform (ShareGPT) | 1617 | 2.0 | 4 x 4 | 102 | 204 | 9.4 | 18.07 | 1.74 | 1.24 |  |
| Llama-3.1-8B | untransformed (ShareGPT) | 1617 | 2.0 | 4 x 4 | 102 | 204 | 9.4 | 18.07 | 1.54 | 1.06 |  |
| Llama-3.1-8B | balance fine-tuning, 1,927 answers | 1927 | 10.0 | 4 x 4 | 121 | 1210 | 23.1 | 16.79 | 2.03 | 0.8 |  |
| Llama-3.1-8B | balance fine-tuning, 400 answers (epoch 10) | 400 | 10.0 | 4 x 4 | 25 | 250 | 5.3 | 16.51 | 2.03 | 0.91 |  |
| Qwen2.5-32B | assertive transform (ShareGPT) | 1617 | 2.0 | 1 x 16 | 102 | 204 | 32.4 | 63.46 | 1.68 | 1.11 |  |
| Qwen2.5-32B | mandate transform (ShareGPT) | 1617 | 2.0 | 1 x 16 | 102 | 204 | 32.6 | 63.46 | 1.63 | 1.1 |  |
| Qwen2.5-32B | mandate fine-tuning | 400 | 10.0 | 1 x 16 | 25 | 250 | 35.5 | 63.16 | 1.2 | 0.8 |  |
| Qwen2.5-32B | neutral transform (ShareGPT) | 1617 | 2.0 | 1 x 16 | 102 | 204 | 32.5 | 63.46 | 1.64 | 1.12 |  |
| Qwen2.5-32B | untransformed (ShareGPT) | 1617 | 2.0 | 1 x 16 | 102 | 204 | 32.5 | 63.46 | 1.43 | 0.95 |  |
| Qwen2.5-32B | balance fine-tuning, 1,927 answers | 1927 | 10.0 | 1 x 16 | 121 | 1210 | 171.6 | 63.15 | 1.72 | 0.73 |  |
| Qwen2.5-32B | balance fine-tuning, 400 answers (epoch 10) | 400 | 10.0 | 1 x 16 | 25 | 250 | 35.0 | 63.08 | 1.69 | 0.83 |  |
| Qwen3.8-27B | neutral transform (ShareGPT) | 1617 | 2.0 | 1 x 16 | 102 | 204 | 65.5 | 52.44 | 3.21 | 1.11 |  |
| Qwen3.8-27B | untransformed (ShareGPT) | 1617 | 2.0 | 1 x 16 | 102 | 204 | 71.3 | 52.44 | 3.11 | 0.95 |  |
| Qwen3.8-27B | balance fine-tuning, 1,927 answers | 1927 | 10.0 | 1 x 16 | 121 | 1210 | 256.4 | 52.15 | 1.79 | 0.65 |  |
| Qwen3.8-27B | balance fine-tuning, 400 answers (epoch 10) | 400 | 10.0 | 1 x 16 | 25 | 250 | 54.0 | 52.08 | 1.83 | 0.76 |  |
| Qwen2.5-7B | assertive transform (ShareGPT) | 1617 | 2.0 | 4 x 4 | 102 | 204 | 8.6 | 17.3 | 1.8 | 1.21 |  |
| Qwen2.5-7B | mandate transform (ShareGPT) | 1617 | 2.0 | 4 x 4 | 102 | 204 | 8.6 | 17.3 | 1.75 | 1.2 |  |
| Qwen2.5-7B | mandate fine-tuning | 400 | 10.0 | 1 x 16 | 25 | 250 | 15.2 | 15.29 | 1.33 | 0.91 |  |
| Qwen2.5-7B | neutral transform (ShareGPT) | 1617 | 2.0 | 4 x 4 | 102 | 204 | 8.6 | 17.3 | 1.77 | 1.23 |  |
| Qwen2.5-7B | untransformed (ShareGPT) | 1617 | 2.0 | 4 x 4 | 102 | 204 | 8.6 | 17.3 | 1.54 | 1.04 |  |
| Qwen2.5-7B | balance fine-tuning, 1,927 answers | 1927 | 10.0 | 1 x 16 | 121 | 1210 | 71.3 | 15.28 | 1.85 | 0.82 |  |
| Qwen2.5-7B | balance fine-tuning, 400 answers (epoch 10) | 400 | 10.0 | 1 x 16 | 25 | 250 | 15.1 | 15.26 | 1.83 | 0.96 |  |
