## Llama-3.1-8B, original and balance fine-tuning on 400 answers (epoch 10), bf16 run

| answers | n | agreement on hedged (%) | kappa, hedged | agreement, four classes (%) | kappa, four classes | agreement, five classes (%) | kappa, five classes |
|---|---|---|---|---|---|---|---|
| original | 474 | 90.7 | 0.72 | 89.9 | 0.76 | 86.1 | 0.71 |
| balance fine-tuning, 400 answers (epoch 10) | 474 | 88.8 | 0.78 | 87.6 | 0.77 | 84.8 | 0.73 |
| both conditions | 948 | 89.8 | 0.78 | 88.7 | 0.79 | 85.4 | 0.74 |

The second judge's share of settled facts presented as open, per condition:

- original: 19.6 per cent (n = 474)
- balance fine-tuning, 400 answers (epoch 10): 48.7 per cent (n = 474)

## GPT-4o, original and neutrality prompt, version-1 items

| answers | n | agreement on hedged (%) | kappa, hedged | agreement, four classes (%) | kappa, four classes | agreement, five classes (%) | kappa, five classes |
|---|---|---|---|---|---|---|---|
| original | 474 | 95.4 | 0.65 | 95.4 | 0.68 | 81.6 | 0.47 |
| neutrality prompt | 474 | 88.8 | 0.68 | 88.4 | 0.67 | 86.7 | 0.64 |
| both conditions | 948 | 92.1 | 0.84 | 91.9 | 0.84 | 84.2 | 0.74 |

The second judge's share of settled facts presented as open, per condition:

- original: 6.5 per cent (n = 474)
- neutrality prompt: 73.2 per cent (n = 474)
