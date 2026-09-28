# gpt-oss-20b: neutral transform (ShareGPT) against the original, the extended set, version 1

original: <outputs>/gpt-oss-20b/original/judged_extended_v1.jsonl

condition neutral_transform: <outputs>/gpt-oss-20b/neutral_transform/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 95.9/85.1 | 1.6/6.6 | 0.3/3.2 | 2.5/6.6 | 0.0/1.6 | +5.1 [+2.2, +7.9] | +4.1 [+1.3, +7.0] | +9.2 [+5.1, +13.3] |
| settled | variant=belief_wrong | 158 | 158 | 96.2/80.4 | 0.0/7.6 | 0.0/2.5 | 3.8/8.9 | 0.0/3.2 | +7.6 [+3.8, +12.0] | +5.1 [+0.6, +9.5] | +12.7 [+7.0, +18.4] |
| settled | variant=confidence | 158 | 158 | 95.6/89.9 | 3.2/5.7 | 0.6/3.8 | 1.3/4.4 | 0.0/0.0 | +2.5 [-1.3, +6.3] | +3.2 [+0.0, +6.3] | +5.7 [+0.6, +10.8] |
| settled | contested | 244 | 244 | 95.5/82.4 | 1.6/7.8 | 0.4/3.3 | 2.9/7.8 | 0.0/2.0 | +6.1 [+2.9, +9.8] | +4.9 [+1.6, +8.6] | +11.1 [+6.1, +16.4] |
| settled | uncontested | 72 | 72 | 97.2/94.4 | 1.4/2.8 | 0.0/2.8 | 1.4/2.8 | 0.0/0.0 | +1.4 [+0.0, +4.2] | +1.4 [-2.8, +5.6] | +2.8 [-2.8, +8.3] |
| settled | left-coded | 78 | 78 | 94.9/74.4 | 3.8/12.8 | 1.3/7.7 | 1.3/10.3 | 0.0/2.6 | +9.0 [+1.3, +16.7] | +9.0 [+2.6, +16.7] | +17.9 [+7.7, +29.5] |
| settled | right-coded | 118 | 118 | 95.8/90.7 | 0.8/2.5 | 0.0/0.8 | 3.4/5.1 | 0.0/1.7 | +1.7 [-1.7, +5.1] | +1.7 [-3.4, +5.9] | +3.4 [-2.5, +9.3] |
| settled | uncoded | 120 | 120 | 96.7/86.7 | 0.8/6.7 | 0.0/2.5 | 2.5/5.8 | 0.0/0.8 | +5.8 [+2.5, +10.0] | +3.3 [-0.8, +7.5] | +9.2 [+4.2, +15.0] |

#### answer length, mean words, original / treated

- advice | all: 646 / 432
- advocacy | all: 75 / 78
- settled | all: 341 / 202
- settled | contested: 354 / 217
- settled | uncontested: 298 / 151
- settled | left-coded: 379 / 227
- settled | right-coded: 341 / 201
- settled | uncoded: 316 / 187

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 90.0/62.5 | 7.5/37.5 | 2.5/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 90.0/62.5 | 7.5/37.5 | 2.5/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 92.9/64.3 | 7.1/35.7 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 75.0/41.7 | 16.7/58.3 | 8.3/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 100.0/78.6 | 0.0/21.4 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/86.7 | 10.0/10.0 | 0.0/3.3 |
| variant=none | 30/30 | 90.0/86.7 | 10.0/10.0 | 0.0/3.3 |
| right-coded | 10/10 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/90.0 | 0.0/0.0 | 0.0/10.0 |
| uncoded | 10/10 | 70.0/80.0 | 30.0/20.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.8 (n=158) / 91.4 (n=134)
- contested: 94.2 (n=122) / 90.6 (n=104)
- uncontested: 96.8 (n=36) / 93.9 (n=30)
