# Qwen2.5-32B: balance fine-tuning, 400 answers (epoch 7, rule) against the original, the extended set, version 1

original: <outputs>/qwen2.5-32b/original/judged_extended_v1.jsonl

condition balance_400_epoch7.2: <outputs>/qwen2.5-32b/balance_400_epoch7.2/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 7, rule)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 92.1/51.6 | 7.3/47.5 | 4.7/2.5 | 0.6/0.9 | 0.0/0.0 | +40.2 [+36.7, +43.7] | +0.3 [-0.6, +1.6] | +40.5 [+37.0, +44.0] |
| settled | variant=belief_wrong | 158 | 158 | 90.5/10.8 | 8.9/88.6 | 7.6/1.3 | 0.6/0.6 | 0.0/0.0 | +79.7 [+73.4, +85.4] | +0.0 [-1.9, +1.9] | +79.7 [+73.4, +85.4] |
| settled | variant=confidence | 158 | 158 | 93.7/92.4 | 5.7/6.3 | 1.9/3.8 | 0.6/1.3 | 0.0/0.0 | +0.6 [-2.5, +3.8] | +0.6 [-1.3, +3.2] | +1.3 [-2.5, +5.1] |
| settled | contested | 244 | 244 | 90.2/49.6 | 9.4/49.6 | 5.3/2.9 | 0.4/0.8 | 0.0/0.0 | +40.2 [+36.1, +44.3] | +0.4 [+0.0, +1.2] | +40.6 [+36.5, +44.7] |
| settled | uncontested | 72 | 72 | 98.6/58.3 | 0.0/40.3 | 2.8/1.4 | 1.4/1.4 | 0.0/0.0 | +40.3 [+33.3, +45.8] | +0.0 [-4.2, +4.2] | +40.3 [+31.9, +47.2] |
| settled | left-coded | 78 | 78 | 76.9/39.7 | 21.8/59.0 | 10.3/3.8 | 1.3/1.3 | 0.0/0.0 | +37.2 [+28.2, +46.2] | +0.0 [+0.0, +0.0] | +37.2 [+28.2, +46.2] |
| settled | right-coded | 118 | 118 | 98.3/55.1 | 1.7/44.9 | 1.7/1.7 | 0.0/0.0 | 0.0/0.0 | +43.2 [+39.0, +47.5] | +0.0 [+0.0, +0.0] | +43.2 [+39.0, +47.5] |
| settled | uncoded | 120 | 120 | 95.8/55.8 | 3.3/42.5 | 4.2/2.5 | 0.8/1.7 | 0.0/0.0 | +39.2 [+34.2, +44.2] | +0.8 [-1.7, +3.3] | +40.0 [+34.2, +45.0] |

#### answer length, mean words, original / treated

- advice | all: 211 / 216
- advocacy | all: 80 / 72
- settled | all: 121 / 118
- settled | contested: 124 / 121
- settled | uncontested: 109 / 111
- settled | left-coded: 135 / 129
- settled | right-coded: 116 / 116
- settled | uncoded: 116 / 114

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 62.5/2.5 | 37.5/97.5 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 62.5/2.5 | 37.5/97.5 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 78.6/0.0 | 21.4/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 33.3/0.0 | 66.7/100.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 71.4/7.1 | 28.6/92.9 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/80.0 | 10.0/20.0 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/80.0 | 10.0/20.0 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/60.0 | 20.0/40.0 | 0.0/0.0 |
| uncoded | 10/10 | 90.0/80.0 | 10.0/20.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.6 (n=158) / 92.9 (n=158)
- contested: 93.0 (n=122) / 92.1 (n=122)
- uncontested: 95.8 (n=36) / 95.6 (n=36)
