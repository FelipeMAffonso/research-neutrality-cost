# Llama-3.1-8B, preliminary 4-bit run: balance fine-tuning, 400 answers (epoch 3.84, rule) against the original, the extended set, version 1

original: <outputs>/llama-3.1-8b-4bit/original/judged_extended_v1.jsonl

condition balance_400_epoch3.84: <outputs>/llama-3.1-8b-4bit/balance_400_epoch3.84/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 3.84, rule)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/5.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/5.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 77.2/71.2 | 16.1/23.4 | 1.6/2.5 | 6.6/5.4 | 0.0/0.0 | +7.3 [+2.5, +12.3] | -1.3 [-4.1, +1.6] | +6.0 [+1.3, +10.8] |
| settled | variant=belief_wrong | 158 | 158 | 71.5/65.2 | 20.3/29.1 | 2.5/3.8 | 8.2/5.7 | 0.0/0.0 | +8.9 [+1.9, +15.8] | -2.5 [-7.6, +1.9] | +6.3 [-0.6, +13.3] |
| settled | variant=confidence | 158 | 158 | 82.9/77.2 | 12.0/17.7 | 0.6/1.3 | 5.1/5.1 | 0.0/0.0 | +5.7 [+0.0, +11.4] | +0.0 [-3.8, +3.8] | +5.7 [-1.3, +12.7] |
| settled | contested | 244 | 244 | 71.7/63.9 | 20.1/29.9 | 1.2/3.3 | 8.2/6.1 | 0.0/0.0 | +9.8 [+4.1, +16.0] | -2.0 [-5.7, +1.2] | +7.8 [+2.0, +13.5] |
| settled | uncontested | 72 | 72 | 95.8/95.8 | 2.8/1.4 | 2.8/0.0 | 1.4/2.8 | 0.0/0.0 | -1.4 [-6.9, +2.8] | +1.4 [-2.8, +5.6] | +0.0 [-6.9, +6.9] |
| settled | left-coded | 78 | 78 | 47.4/35.9 | 38.5/56.4 | 2.6/3.8 | 14.1/7.7 | 0.0/0.0 | +17.9 [+6.4, +29.5] | -6.4 [-14.1, +1.3] | +11.5 [+0.0, +21.8] |
| settled | right-coded | 118 | 118 | 84.7/78.0 | 8.5/14.4 | 0.8/2.5 | 6.8/7.6 | 0.0/0.0 | +5.9 [-2.5, +14.4] | +0.8 [-3.4, +5.1] | +6.8 [-1.7, +15.3] |
| settled | uncoded | 120 | 120 | 89.2/87.5 | 9.2/10.8 | 1.7/1.7 | 1.7/1.7 | 0.0/0.0 | +1.7 [-3.3, +6.7] | +0.0 [-3.3, +3.3] | +1.7 [-4.2, +7.5] |

#### answer length, mean words, original / treated

- advice | all: 199 / 167
- advocacy | all: 97 / 86
- settled | all: 138 / 112
- settled | contested: 141 / 117
- settled | uncontested: 128 / 94
- settled | left-coded: 151 / 123
- settled | right-coded: 131 / 110
- settled | uncoded: 136 / 107

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 50.0/35.0 | 47.5/57.5 | 0.0/2.5 | 2.5/5.0 |
| variant=none | 40/40 | 50.0/35.0 | 47.5/57.5 | 0.0/2.5 | 2.5/5.0 |
| right-coded | 14/14 | 64.3/35.7 | 28.6/57.1 | 0.0/0.0 | 7.1/7.1 |
| left-coded | 12/12 | 16.7/16.7 | 83.3/75.0 | 0.0/0.0 | 0.0/8.3 |
| uncoded | 14/14 | 64.3/50.0 | 35.7/42.9 | 0.0/7.1 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 76.7/70.0 | 23.3/26.7 | 0.0/3.3 |
| variant=none | 30/30 | 76.7/70.0 | 23.3/26.7 | 0.0/3.3 |
| right-coded | 10/10 | 90.0/80.0 | 10.0/10.0 | 0.0/10.0 |
| left-coded | 10/10 | 70.0/60.0 | 30.0/40.0 | 0.0/0.0 |
| uncoded | 10/10 | 70.0/70.0 | 30.0/30.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 89.2 (n=153) / 86.6 (n=153)
- contested: 87.2 (n=119) / 84.8 (n=120)
- uncontested: 96.4 (n=34) / 93.0 (n=33)
