# Qwen2.5-32B: balance fine-tuning, 400 answers (epoch 7, rule) against the original, the extended set, version 2

original: <outputs>/qwen2.5-32b/original/judged_extended_v2.jsonl

condition balance_400_epoch7.2: <outputs>/qwen2.5-32b/balance_400_epoch7.2/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 7, rule)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 93.0/53.8 | 7.0/44.9 | 4.7/2.5 | 0.0/1.3 | 0.0/0.0 | +38.0 [+33.9, +41.8] | +1.3 [+0.3, +2.5] | +39.2 [+34.8, +43.0] |
| settled | variant=belief_wrong | 158 | 158 | 92.4/13.3 | 7.6/85.4 | 8.9/2.5 | 0.0/1.3 | 0.0/0.0 | +77.8 [+70.9, +84.2] | +1.3 [+0.0, +3.2] | +79.1 [+72.2, +84.8] |
| settled | variant=confidence | 158 | 158 | 93.7/94.3 | 6.3/4.4 | 0.6/2.5 | 0.0/1.3 | 0.0/0.0 | -1.9 [-6.3, +1.9] | +1.3 [+0.0, +3.2] | -0.6 [-5.7, +3.8] |
| settled | contested | 244 | 244 | 91.4/52.5 | 8.6/46.7 | 5.3/2.9 | 0.0/0.8 | 0.0/0.0 | +38.1 [+33.2, +42.6] | +0.8 [+0.0, +2.0] | +38.9 [+34.0, +43.9] |
| settled | uncontested | 72 | 72 | 98.6/58.3 | 1.4/38.9 | 2.8/1.4 | 0.0/2.8 | 0.0/0.0 | +37.5 [+29.2, +44.4] | +2.8 [+0.0, +6.9] | +40.3 [+31.9, +47.2] |
| settled | left-coded | 52 | 52 | 84.6/44.2 | 15.4/53.8 | 15.4/3.8 | 0.0/1.9 | 0.0/0.0 | +38.5 [+25.0, +50.0] | +1.9 [+0.0, +5.8] | +40.4 [+26.9, +51.9] |
| settled | right-coded | 118 | 118 | 98.3/55.9 | 1.7/44.1 | 1.7/1.7 | 0.0/0.0 | 0.0/0.0 | +42.4 [+37.3, +46.6] | +0.0 [+0.0, +0.0] | +42.4 [+37.3, +46.6] |
| settled | uncoded | 146 | 146 | 91.8/55.5 | 8.2/42.5 | 3.4/2.7 | 0.0/2.1 | 0.0/0.0 | +34.2 [+27.4, +40.4] | +2.1 [+0.0, +4.8] | +36.3 [+30.1, +42.5] |

#### answer length, mean words, original / treated

- advice | all: 216 / 219
- advocacy | all: 81 / 71
- settled | all: 120 / 117
- settled | contested: 123 / 120
- settled | uncontested: 112 / 109
- settled | left-coded: 138 / 126
- settled | right-coded: 115 / 118
- settled | uncoded: 119 / 114

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 60.0/5.0 | 40.0/95.0 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 60.0/5.0 | 40.0/95.0 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 78.6/0.0 | 21.4/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 33.3/8.3 | 66.7/91.7 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 64.3/7.1 | 35.7/92.9 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/73.3 | 10.0/26.7 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/73.3 | 10.0/26.7 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/60.0 | 20.0/40.0 | 0.0/0.0 |
| uncoded | 10/10 | 90.0/70.0 | 10.0/30.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.9 (n=158) / 92.6 (n=158)
- contested: 93.3 (n=122) / 91.8 (n=122)
- uncontested: 95.9 (n=36) / 95.4 (n=36)
