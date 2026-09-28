# Fixed-effects logistic regressions (the warmth study's Model 1, clustered by question)

Outcome: settled fact presented as open (1) versus any other class (0). Model fixed effects and identity-prefix fixed effects; standard errors clustered by question; average marginal effect of the condition in percentage points. The last column adds answer length (words, per hundred) as a covariate, as the warmth study's length-adjusted model did.

| condition | models | n answers | coefficient (log odds) | clustered s.e. | P | marginal effect (pp) | marginal effect, length-adjusted (pp) |
|---|---|---|---|---|---|---|---|
| neutrality prompt | 8 | 7584 | 3.47 | 0.09 | 0 | +62.1 | +62.7 |
| balance fine-tuning, 400 answers (epoch 10) | 7 | 6636 | 1.81 | 0.09 | 3.2e-91 | +24.5 | +30.4 |
| balance fine-tuning, 1,927 answers | 6 | 5688 | 3.34 | 0.09 | 5.9e-284 | +64.3 | +66.7 |
| neutral transform (ShareGPT) | 7 | 6636 | 0.08 | 0.07 | 0.26 | +0.7 | +3.6 |
| untransformed (ShareGPT) | 7 | 6636 | -0.02 | 0.07 | 0.81 | -0.2 | +1.9 |
| assertive transform (ShareGPT) | 5 | 4740 | -0.10 | 0.09 | 0.25 | -1.0 | +2.4 |
| mandate transform (ShareGPT) | 5 | 4740 | -0.13 | 0.09 | 0.15 | -1.3 | +2.2 |
| mandate fine-tuning | 5 | 4740 | 0.41 | 0.07 | 3e-09 | +5.0 | +8.6 |

## Per model

| condition | model | n | coefficient | s.e. | P | marginal effect (pp) | length-adjusted (pp) |
|---|---|---|---|---|---|---|---|
| neutrality prompt | Gemma-4-31B | 948 | 3.45 | 0.25 | 2.7e-42 | +65.0 | +59.8 |
| neutrality prompt | gpt-oss-120b | 948 | 7.20 | 1.01 | 9.7e-13 | +73.6 | +79.2 |
| neutrality prompt | gpt-oss-20b | 948 | 5.18 | 0.45 | 1.5e-30 | +63.5 | +67.1 |
| neutrality prompt | Llama-3.1-8B | 948 | 3.58 | 0.23 | 2e-53 | +68.8 | +62.4 |
| neutrality prompt | Llama-3.2-3B | 948 | 2.76 | 0.19 | 1e-46 | +59.7 | +53.5 |
| neutrality prompt | Qwen2.5-32B | 948 | 2.55 | 0.22 | 6.6e-32 | +50.6 | +53.1 |
| neutrality prompt | Qwen2.5-7B | 948 | 2.92 | 0.22 | 1.1e-39 | +53.6 | +46.6 |
| neutrality prompt | Qwen3.8-27B | 948 | 5.30 | 0.50 | 3e-26 | +61.6 | +51.8 |
| balance fine-tuning, 400 answers (epoch 10) | Gemma-4-31B | 948 | 1.37 | 0.20 | 4.1e-12 | +16.9 | +21.5 |
| balance fine-tuning, 400 answers (epoch 10) | gpt-oss-20b | 948 | 2.33 | 0.40 | 6.7e-09 | +8.9 | +27.0 |
| balance fine-tuning, 400 answers (epoch 10) | Llama-3.1-8B | 948 | 1.50 | 0.13 | 1.4e-29 | +33.5 | +50.1 |
| balance fine-tuning, 400 answers (epoch 10) | Llama-3.2-3B | 948 | 0.39 | 0.15 | 0.0077 | +7.0 | +17.7 |
| balance fine-tuning, 400 answers (epoch 10) | Qwen2.5-32B | 948 | 3.62 | 0.25 | 6.3e-46 | +70.5 | +69.4 |
| balance fine-tuning, 400 answers (epoch 10) | Qwen2.5-7B | 948 | 2.11 | 0.22 | 1e-22 | +33.5 | +43.8 |
| balance fine-tuning, 400 answers (epoch 10) | Qwen3.8-27B | 948 | 0.82 | 0.53 | 0.12 | +1.1 | +1.1 |
| balance fine-tuning, 1,927 answers | gpt-oss-20b | 948 | 5.95 | 0.46 | 1.4e-38 | +78.7 | +86.5 |
| balance fine-tuning, 1,927 answers | Llama-3.1-8B | 948 | 2.48 | 0.18 | 5.1e-44 | +54.9 | +64.9 |
| balance fine-tuning, 1,927 answers | Llama-3.2-3B | 948 | 2.33 | 0.17 | 1.1e-40 | +51.9 | +60.9 |
| balance fine-tuning, 1,927 answers | Qwen2.5-32B | 948 | 3.56 | 0.25 | 1.1e-45 | +69.6 | +67.6 |
| balance fine-tuning, 1,927 answers | Qwen2.5-7B | 948 | 3.67 | 0.24 | 1.7e-53 | +69.2 | +69.5 |
| balance fine-tuning, 1,927 answers | Qwen3.8-27B | 948 | 5.29 | 0.50 | 5.2e-26 | +61.6 | +63.8 |
| neutral transform (ShareGPT) | Gemma-4-31B | 948 | 0.26 | 0.15 | 0.082 | +2.1 | +2.4 |
| neutral transform (ShareGPT) | gpt-oss-20b | 948 | 1.92 | 0.47 | 5.1e-05 | +5.7 | +9.2 |
| neutral transform (ShareGPT) | Llama-3.1-8B | 948 | -0.58 | 0.16 | 0.00028 | -8.4 | +1.4 |
| neutral transform (ShareGPT) | Llama-3.2-3B | 948 | -0.05 | 0.14 | 0.7 | -0.8 | +3.4 |
| neutral transform (ShareGPT) | Qwen2.5-32B | 948 | 0.28 | 0.16 | 0.074 | +3.2 | +8.0 |
| neutral transform (ShareGPT) | Qwen2.5-7B | 948 | 0.39 | 0.19 | 0.046 | +3.4 | +6.0 |
| neutral transform (ShareGPT) | Qwen3.8-27B | 948 | 0.00 | 0.51 | 1 | +0.0 | +0.0 |
| untransformed (ShareGPT) | Gemma-4-31B | 948 | 0.11 | 0.14 | 0.44 | +0.8 | +1.0 |
| untransformed (ShareGPT) | gpt-oss-20b | 948 | 1.98 | 0.42 | 2.8e-06 | +6.1 | +9.1 |
| untransformed (ShareGPT) | Llama-3.1-8B | 948 | -0.40 | 0.15 | 0.0092 | -6.1 | +2.3 |
| untransformed (ShareGPT) | Llama-3.2-3B | 948 | -0.20 | 0.13 | 0.14 | -3.0 | -0.0 |
| untransformed (ShareGPT) | Qwen2.5-32B | 948 | 0.02 | 0.18 | 0.91 | +0.2 | +4.2 |
| untransformed (ShareGPT) | Qwen2.5-7B | 948 | 0.16 | 0.23 | 0.49 | +1.3 | +3.0 |
| untransformed (ShareGPT) | Qwen3.8-27B | 948 | -0.70 | 0.51 | 0.17 | -0.4 | -0.4 |
| assertive transform (ShareGPT) | gpt-oss-20b | 948 | 1.95 | 0.43 | 4.6e-06 | +5.9 | +7.6 |
| assertive transform (ShareGPT) | Llama-3.1-8B | 948 | -0.66 | 0.15 | 7.5e-06 | -9.3 | +0.5 |
| assertive transform (ShareGPT) | Llama-3.2-3B | 948 | -0.42 | 0.17 | 0.013 | -5.9 | -1.7 |
| assertive transform (ShareGPT) | Qwen2.5-32B | 948 | 0.02 | 0.21 | 0.92 | +0.2 | +11.8 |
| assertive transform (ShareGPT) | Qwen2.5-7B | 948 | 0.45 | 0.18 | 0.014 | +4.0 | +7.3 |
| mandate transform (ShareGPT) | gpt-oss-20b | 948 | 2.07 | 0.43 | 1.6e-06 | +6.8 | +9.8 |
| mandate transform (ShareGPT) | Llama-3.1-8B | 948 | -0.68 | 0.16 | 2.4e-05 | -9.5 | -2.0 |
| mandate transform (ShareGPT) | Llama-3.2-3B | 948 | -0.34 | 0.16 | 0.04 | -4.9 | -0.5 |
| mandate transform (ShareGPT) | Qwen2.5-32B | 948 | -0.16 | 0.20 | 0.43 | -1.5 | +9.9 |
| mandate transform (ShareGPT) | Qwen2.5-7B | 948 | 0.30 | 0.21 | 0.15 | +2.5 | +6.7 |
| mandate fine-tuning | gpt-oss-20b | 948 | 2.21 | 0.48 | 4.7e-06 | +7.8 | +22.2 |
| mandate fine-tuning | Llama-3.1-8B | 948 | 0.34 | 0.12 | 0.005 | +6.3 | +12.2 |
| mandate fine-tuning | Llama-3.2-3B | 948 | 0.22 | 0.12 | 0.068 | +3.8 | +13.7 |
| mandate fine-tuning | Qwen2.5-32B | 948 | 0.08 | 0.12 | 0.51 | +0.8 | +3.3 |
| mandate fine-tuning | Qwen2.5-7B | 948 | 0.65 | 0.19 | 0.00066 | +6.3 | +9.6 |

## Interaction models (the warmth study's Models 2 and 4): the condition by the user cue

Settled facts; the treatment indicator interacted with the identity prefix (conservative, liberal against none) and, on the extended prompt set, with the stated false belief (against no prefix). Model fixed effects; standard errors clustered by question. Marginal effects in percentage points: the condition's effect with no cue, and the additional effect of the cue on the treated model.

| condition | models | cue | effect of the condition, no cue (pp) | cue x condition (pp) | P (interaction) |
|---|---|---|---|---|---|
| neutrality prompt | 8 | identity prefix | +61.7 | +0.5 | 0.72 |
| balance fine-tuning, 400 answers (epoch 10) | 8 | identity prefix | +20.0 | +4.4 | 0.0092 |
| balance fine-tuning, 400 answers (epoch 10) | 8 | false belief | +20.2 | +2.8 | 0.17 |
| balance fine-tuning, 1,927 answers | 8 | identity prefix | +59.3 | +1.1 | 0.52 |
| balance fine-tuning, 1,927 answers | 8 | false belief | +59.3 | +0.1 | 0.96 |

## Relative increase over the original

The marginal effect across all models divided by the original share across the same models, per condition.

| condition | original share (%) | marginal effect (pp) | relative increase (%) |
|---|---|---|---|
| neutrality prompt | 9.0 | +62.1 | +691 |
| balance fine-tuning, 400 answers (epoch 10) | 10.2 | +24.5 | +239 |
| balance fine-tuning, 1,927 answers | 10.6 | +64.3 | +608 |
| neutral transform (ShareGPT) | 10.2 | +0.7 | +7 |
| untransformed (ShareGPT) | 10.2 | -0.2 | -2 |
| assertive transform (ShareGPT) | 12.5 | -1.0 | -8 |
| mandate transform (ShareGPT) | 12.5 | -1.3 | -10 |
| mandate fine-tuning | 12.5 | +5.0 | +40 |
