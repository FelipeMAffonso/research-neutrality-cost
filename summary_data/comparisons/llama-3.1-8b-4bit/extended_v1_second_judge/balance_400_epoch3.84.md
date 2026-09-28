# Llama-3.1-8B, preliminary 4-bit run: balance fine-tuning, 400 answers (epoch 3.84, rule) against the original, the extended set, version 1, second judge

original: <outputs>/llama-3.1-8b-4bit/original/judged_extended_v1_second_judge.jsonl

condition balance_400_epoch3.84: <outputs>/llama-3.1-8b-4bit/balance_400_epoch3.84/judged_extended_v1_second_judge.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 3.84, rule)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 5.0/10.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 5.0/10.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 80.7/77.8 | 10.8/16.5 | 1.9/2.2 | 8.2/5.1 | 0.3/0.6 | +5.7 [+1.3, +10.4] | -3.2 [-6.3, +0.0] | +2.5 [-1.9, +7.0] |
| settled | variant=belief_wrong | 158 | 158 | 76.6/71.5 | 12.7/22.2 | 2.5/3.2 | 10.1/5.1 | 0.6/1.3 | +9.5 [+3.2, +16.5] | -5.1 [-10.1, -0.6] | +4.4 [-2.5, +12.0] |
| settled | variant=confidence | 158 | 158 | 84.8/84.2 | 8.9/10.8 | 1.3/1.3 | 6.3/5.1 | 0.0/0.0 | +1.9 [-3.2, +7.6] | -1.3 [-5.1, +2.5] | +0.6 [-4.4, +5.7] |
| settled | contested | 244 | 244 | 76.2/73.0 | 13.5/21.3 | 2.0/2.5 | 9.8/5.3 | 0.4/0.4 | +7.8 [+1.6, +13.9] | -4.5 [-8.2, -0.8] | +3.3 [-2.5, +8.6] |
| settled | uncontested | 72 | 72 | 95.8/94.4 | 1.4/0.0 | 1.4/1.4 | 2.8/4.2 | 0.0/1.4 | -1.4 [-4.2, +0.0] | +1.4 [-2.8, +6.9] | +0.0 [-5.6, +5.6] |
| settled | left-coded | 78 | 78 | 51.3/46.2 | 28.2/42.3 | 3.8/5.1 | 19.2/11.5 | 1.3/0.0 | +14.1 [+0.0, +28.2] | -7.7 [-17.9, +2.6] | +6.4 [-6.4, +17.9] |
| settled | right-coded | 118 | 118 | 89.8/88.1 | 4.2/7.6 | 0.8/0.8 | 5.9/3.4 | 0.0/0.8 | +3.4 [-2.5, +9.3] | -2.5 [-5.9, +0.8] | +0.8 [-5.1, +7.6] |
| settled | uncoded | 120 | 120 | 90.8/88.3 | 5.8/8.3 | 1.7/1.7 | 3.3/2.5 | 0.0/0.8 | +2.5 [-2.5, +8.3] | -0.8 [-4.2, +2.5] | +1.7 [-4.2, +7.5] |

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
| all | 40/40 | 50.0/47.5 | 42.5/40.0 | 2.5/2.5 | 5.0/10.0 |
| variant=none | 40/40 | 50.0/47.5 | 42.5/40.0 | 2.5/2.5 | 5.0/10.0 |
| right-coded | 14/14 | 64.3/50.0 | 28.6/28.6 | 0.0/0.0 | 7.1/21.4 |
| left-coded | 12/12 | 33.3/25.0 | 50.0/58.3 | 8.3/8.3 | 8.3/8.3 |
| uncoded | 14/14 | 50.0/64.3 | 50.0/35.7 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 80.0/76.7 | 20.0/20.0 | 0.0/3.3 |
| variant=none | 30/30 | 80.0/76.7 | 20.0/20.0 | 0.0/3.3 |
| right-coded | 10/10 | 100.0/90.0 | 0.0/0.0 | 0.0/10.0 |
| left-coded | 10/10 | 70.0/60.0 | 30.0/40.0 | 0.0/0.0 |
| uncoded | 10/10 | 70.0/80.0 | 30.0/20.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 89.2 (n=153) / 86.6 (n=153)
- contested: 87.2 (n=119) / 84.8 (n=120)
- uncontested: 96.4 (n=34) / 93.0 (n=33)
