# Qwen2.5-32B: balance fine-tuning, 400 answers (epoch 10) against the original, the extended set, version 1

original: <outputs>/qwen2.5-32b/original/judged_extended_v1.jsonl

condition balance_400: <outputs>/qwen2.5-32b/balance_400/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 92.1/52.5 | 7.3/46.8 | 4.7/4.1 | 0.6/0.6 | 0.0/0.0 | +39.6 [+36.1, +42.7] | +0.0 [-0.9, +0.9] | +39.6 [+36.1, +42.7] |
| settled | variant=belief_wrong | 158 | 158 | 90.5/12.0 | 8.9/88.0 | 7.6/4.4 | 0.6/0.0 | 0.0/0.0 | +79.1 [+72.8, +85.4] | -0.6 [-1.9, +0.0] | +78.5 [+72.2, +84.8] |
| settled | variant=confidence | 158 | 158 | 93.7/93.0 | 5.7/5.7 | 1.9/3.8 | 0.6/1.3 | 0.0/0.0 | +0.0 [-3.2, +3.2] | +0.6 [-1.3, +3.2] | +0.6 [-3.2, +4.4] |
| settled | contested | 244 | 244 | 90.2/50.4 | 9.4/49.2 | 5.3/4.1 | 0.4/0.4 | 0.0/0.0 | +39.8 [+35.7, +43.9] | +0.0 [+0.0, +0.0] | +39.8 [+35.7, +43.9] |
| settled | uncontested | 72 | 72 | 98.6/59.7 | 0.0/38.9 | 2.8/4.2 | 1.4/1.4 | 0.0/0.0 | +38.9 [+31.9, +45.8] | +0.0 [-4.2, +4.2] | +38.9 [+30.6, +45.8] |
| settled | left-coded | 78 | 78 | 76.9/41.0 | 21.8/57.7 | 10.3/5.1 | 1.3/1.3 | 0.0/0.0 | +35.9 [+26.9, +44.9] | +0.0 [+0.0, +0.0] | +35.9 [+26.9, +44.9] |
| settled | right-coded | 118 | 118 | 98.3/56.8 | 1.7/43.2 | 1.7/4.2 | 0.0/0.0 | 0.0/0.0 | +41.5 [+36.4, +45.8] | +0.0 [+0.0, +0.0] | +41.5 [+36.4, +45.8] |
| settled | uncoded | 120 | 120 | 95.8/55.8 | 3.3/43.3 | 4.2/3.3 | 0.8/0.8 | 0.0/0.0 | +40.0 [+35.0, +45.0] | +0.0 [-2.5, +2.5] | +40.0 [+34.2, +45.0] |

#### answer length, mean words, original / treated

- advice | all: 211 / 217
- advocacy | all: 80 / 75
- settled | all: 121 / 118
- settled | contested: 124 / 120
- settled | uncontested: 109 / 109
- settled | left-coded: 135 / 129
- settled | right-coded: 116 / 116
- settled | uncoded: 116 / 113

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 62.5/7.5 | 37.5/92.5 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 62.5/7.5 | 37.5/92.5 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 78.6/7.1 | 21.4/92.9 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 33.3/8.3 | 66.7/91.7 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 71.4/7.1 | 28.6/92.9 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/70.0 | 10.0/30.0 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/70.0 | 10.0/30.0 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/50.0 | 20.0/50.0 | 0.0/0.0 |
| uncoded | 10/10 | 90.0/60.0 | 10.0/40.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.6 (n=158) / 92.7 (n=158)
- contested: 93.0 (n=122) / 92.0 (n=122)
- uncontested: 95.8 (n=36) / 95.4 (n=36)
