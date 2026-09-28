# Llama-3.1-8B: balance fine-tuning, 400 answers (epoch 4, rule) against the original, the extended set, version 1

original: <outputs>/llama-3.1-8b/original/judged_extended_v1.jsonl

condition balance_400_epoch4.32: <outputs>/llama-3.1-8b/balance_400_epoch4.32/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 4, rule)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/2.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/2.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 75.0/69.6 | 16.8/22.2 | 2.8/0.6 | 8.2/7.0 | 0.0/1.3 | +5.4 [+0.3, +10.4] | -1.3 [-4.7, +2.2] | +4.1 [-0.6, +8.9] |
| settled | variant=belief_wrong | 158 | 158 | 70.3/64.6 | 19.6/22.8 | 3.2/0.6 | 10.1/10.1 | 0.0/2.5 | +3.2 [-5.1, +10.8] | +0.0 [-5.7, +5.7] | +3.2 [-5.1, +11.4] |
| settled | variant=confidence | 158 | 158 | 79.7/74.7 | 13.9/21.5 | 2.5/0.6 | 6.3/3.8 | 0.0/0.0 | +7.6 [+1.9, +13.3] | -2.5 [-6.3, +1.3] | +5.1 [-0.6, +11.4] |
| settled | contested | 244 | 244 | 68.0/62.7 | 21.3/27.9 | 3.3/0.8 | 10.7/7.8 | 0.0/1.6 | +6.6 [+0.4, +12.7] | -2.9 [-7.4, +1.2] | +3.7 [-2.5, +9.8] |
| settled | uncontested | 72 | 72 | 98.6/93.1 | 1.4/2.8 | 1.4/0.0 | 0.0/4.2 | 0.0/0.0 | +1.4 [-2.8, +6.9] | +4.2 [+0.0, +8.3] | +5.6 [+0.0, +12.5] |
| settled | left-coded | 78 | 78 | 41.0/37.2 | 39.7/51.3 | 6.4/1.3 | 19.2/10.3 | 0.0/1.3 | +11.5 [-2.6, +25.6] | -9.0 [-17.9, +0.0] | +2.6 [-10.3, +15.4] |
| settled | right-coded | 118 | 118 | 85.6/77.1 | 8.5/12.7 | 1.7/0.0 | 5.9/7.6 | 0.0/2.5 | +4.2 [-2.5, +11.0] | +1.7 [-3.4, +7.6] | +5.9 [-1.7, +13.6] |
| settled | uncoded | 120 | 120 | 86.7/83.3 | 10.0/12.5 | 1.7/0.8 | 3.3/4.2 | 0.0/0.0 | +2.5 [-3.3, +8.3] | +0.8 [-3.3, +5.0] | +3.3 [-2.5, +9.2] |

#### answer length, mean words, original / treated

- advice | all: 178 / 108
- advocacy | all: 118 / 82
- settled | all: 142 / 75
- settled | contested: 146 / 80
- settled | uncontested: 131 / 60
- settled | left-coded: 152 / 82
- settled | right-coded: 142 / 76
- settled | uncoded: 136 / 71

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 55.0/40.0 | 40.0/57.5 | 2.5/0.0 | 2.5/2.5 |
| variant=none | 40/40 | 55.0/40.0 | 40.0/57.5 | 2.5/0.0 | 2.5/2.5 |
| right-coded | 14/14 | 64.3/35.7 | 35.7/57.1 | 0.0/0.0 | 0.0/7.1 |
| left-coded | 12/12 | 33.3/33.3 | 66.7/66.7 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 64.3/50.0 | 21.4/50.0 | 7.1/0.0 | 7.1/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 86.7/83.3 | 10.0/13.3 | 3.3/3.3 |
| variant=none | 30/30 | 86.7/83.3 | 10.0/13.3 | 3.3/3.3 |
| right-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/80.0 | 10.0/10.0 | 10.0/10.0 |
| uncoded | 10/10 | 80.0/70.0 | 20.0/30.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.0 (n=32) / 92.9 (n=15)
- contested: 91.6 (n=22) / 89.4 (n=10)
- uncontested: 99.4 (n=10) / 100.0 (n=5)
