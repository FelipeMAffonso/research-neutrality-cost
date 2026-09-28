# Qwen2.5-7B: balance fine-tuning, 400 answers (epoch 10) against the original, the extended set, version 2

original: <outputs>/qwen2.5-7b/original/judged_extended_v2.jsonl

condition balance_400: <outputs>/qwen2.5-7b/balance_400/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 89.2/73.4 | 8.9/25.0 | 3.2/2.2 | 1.9/1.6 | 0.0/0.0 | +16.1 [+12.0, +20.9] | -0.3 [-2.2, +1.6] | +15.8 [+11.7, +20.3] |
| settled | variant=belief_wrong | 158 | 158 | 84.2/60.8 | 14.6/38.0 | 5.1/3.2 | 1.3/1.3 | 0.0/0.0 | +23.4 [+16.5, +31.0] | +0.0 [-2.5, +2.5] | +23.4 [+16.5, +31.0] |
| settled | variant=confidence | 158 | 158 | 94.3/86.1 | 3.2/12.0 | 1.3/1.3 | 2.5/1.9 | 0.0/0.0 | +8.9 [+4.4, +13.9] | -0.6 [-3.2, +1.9] | +8.2 [+3.2, +13.9] |
| settled | contested | 244 | 244 | 86.5/67.2 | 11.1/30.7 | 3.7/1.6 | 2.5/2.0 | 0.0/0.0 | +19.7 [+14.3, +25.0] | -0.4 [-2.9, +2.0] | +19.3 [+13.9, +24.6] |
| settled | uncontested | 72 | 72 | 98.6/94.4 | 1.4/5.6 | 1.4/4.2 | 0.0/0.0 | 0.0/0.0 | +4.2 [-1.4, +9.7] | +0.0 [+0.0, +0.0] | +4.2 [-1.4, +9.7] |
| settled | left-coded | 52 | 52 | 78.8/50.0 | 17.3/50.0 | 9.6/3.8 | 3.8/0.0 | 0.0/0.0 | +32.7 [+19.2, +48.1] | -3.8 [-9.6, +0.0] | +28.8 [+15.4, +42.3] |
| settled | right-coded | 118 | 118 | 94.1/79.7 | 4.2/18.6 | 1.7/0.8 | 1.7/1.7 | 0.0/0.0 | +14.4 [+8.5, +20.3] | +0.0 [-3.4, +3.4] | +14.4 [+8.5, +20.3] |
| settled | uncoded | 146 | 146 | 89.0/76.7 | 9.6/21.2 | 2.1/2.7 | 1.4/2.1 | 0.0/0.0 | +11.6 [+5.5, +17.8] | +0.7 [-1.4, +3.4] | +12.3 [+6.2, +18.5] |

#### answer length, mean words, original / treated

- advice | all: 218 / 189
- advocacy | all: 80 / 79
- settled | all: 119 / 96
- settled | contested: 122 / 101
- settled | uncontested: 110 / 82
- settled | left-coded: 133 / 108
- settled | right-coded: 115 / 98
- settled | uncoded: 117 / 91

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 67.5/37.5 | 32.5/62.5 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 67.5/37.5 | 32.5/62.5 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 71.4/50.0 | 28.6/50.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 50.0/8.3 | 50.0/91.7 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 78.6/50.0 | 21.4/50.0 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/76.7 | 10.0/23.3 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/76.7 | 10.0/23.3 | 0.0/0.0 |
| right-coded | 10/10 | 90.0/70.0 | 10.0/30.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/80.0 | 0.0/20.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/80.0 | 20.0/20.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.3 (n=158) / 90.5 (n=158)
- contested: 92.3 (n=122) / 88.8 (n=122)
- uncontested: 96.9 (n=36) / 96.1 (n=36)
