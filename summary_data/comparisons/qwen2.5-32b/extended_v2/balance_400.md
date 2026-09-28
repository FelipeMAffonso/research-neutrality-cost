# Qwen2.5-32B: balance fine-tuning, 400 answers (epoch 10) against the original, the extended set, version 2

original: <outputs>/qwen2.5-32b/original/judged_extended_v2.jsonl

condition balance_400: <outputs>/qwen2.5-32b/balance_400/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 93.0/54.4 | 7.0/45.3 | 4.7/2.5 | 0.0/0.3 | 0.0/0.0 | +38.3 [+34.2, +42.1] | +0.3 [+0.0, +0.9] | +38.6 [+34.5, +42.7] |
| settled | variant=belief_wrong | 158 | 158 | 92.4/12.7 | 7.6/87.3 | 8.9/2.5 | 0.0/0.0 | 0.0/0.0 | +79.7 [+73.4, +85.4] | +0.0 [+0.0, +0.0] | +79.7 [+73.4, +85.4] |
| settled | variant=confidence | 158 | 158 | 93.7/96.2 | 6.3/3.2 | 0.6/2.5 | 0.0/0.6 | 0.0/0.0 | -3.2 [-7.6, +0.6] | +0.6 [+0.0, +1.9] | -2.5 [-7.0, +1.9] |
| settled | contested | 244 | 244 | 91.4/52.0 | 8.6/47.5 | 5.3/2.5 | 0.0/0.4 | 0.0/0.0 | +38.9 [+34.0, +43.4] | +0.4 [+0.0, +1.2] | +39.3 [+34.4, +44.3] |
| settled | uncontested | 72 | 72 | 98.6/62.5 | 1.4/37.5 | 2.8/2.8 | 0.0/0.0 | 0.0/0.0 | +36.1 [+27.8, +44.4] | +0.0 [+0.0, +0.0] | +36.1 [+27.8, +44.4] |
| settled | left-coded | 52 | 52 | 84.6/46.2 | 15.4/51.9 | 15.4/3.8 | 0.0/1.9 | 0.0/0.0 | +36.5 [+25.0, +46.2] | +1.9 [+0.0, +5.8] | +38.5 [+25.0, +50.0] |
| settled | right-coded | 118 | 118 | 98.3/55.9 | 1.7/44.1 | 1.7/1.7 | 0.0/0.0 | 0.0/0.0 | +42.4 [+37.3, +46.6] | +0.0 [+0.0, +0.0] | +42.4 [+37.3, +46.6] |
| settled | uncoded | 146 | 146 | 91.8/56.2 | 8.2/43.8 | 3.4/2.7 | 0.0/0.0 | 0.0/0.0 | +35.6 [+28.8, +41.8] | +0.0 [+0.0, +0.0] | +35.6 [+28.8, +41.8] |

#### answer length, mean words, original / treated

- advice | all: 216 / 220
- advocacy | all: 81 / 76
- settled | all: 120 / 117
- settled | contested: 123 / 120
- settled | uncontested: 112 / 106
- settled | left-coded: 138 / 126
- settled | right-coded: 115 / 114
- settled | uncoded: 119 / 116

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 60.0/7.5 | 40.0/92.5 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 60.0/7.5 | 40.0/92.5 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 78.6/7.1 | 21.4/92.9 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 33.3/8.3 | 66.7/91.7 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 64.3/7.1 | 35.7/92.9 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/73.3 | 10.0/26.7 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/73.3 | 10.0/26.7 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/50.0 | 20.0/50.0 | 0.0/0.0 |
| uncoded | 10/10 | 90.0/70.0 | 10.0/30.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.9 (n=158) / 92.6 (n=158)
- contested: 93.3 (n=122) / 91.9 (n=122)
- uncontested: 95.9 (n=36) / 94.9 (n=36)
