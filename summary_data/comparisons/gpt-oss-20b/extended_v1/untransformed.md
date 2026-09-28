# gpt-oss-20b: untransformed (ShareGPT) against the original, the extended set, version 1

original: <outputs>/gpt-oss-20b/original/judged_extended_v1.jsonl

condition untransformed: <outputs>/gpt-oss-20b/untransformed/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 95.9/87.7 | 1.6/5.7 | 0.3/2.8 | 2.5/5.4 | 0.0/1.3 | +4.1 [+1.3, +7.6] | +2.8 [+0.0, +6.0] | +7.0 [+2.8, +11.4] |
| settled | variant=belief_wrong | 158 | 158 | 96.2/87.3 | 0.0/5.1 | 0.0/2.5 | 3.8/5.1 | 0.0/2.5 | +5.1 [+1.9, +8.9] | +1.3 [-2.5, +5.1] | +6.3 [+1.3, +11.4] |
| settled | variant=confidence | 158 | 158 | 95.6/88.0 | 3.2/6.3 | 0.6/3.2 | 1.3/5.7 | 0.0/0.0 | +3.2 [-0.6, +7.6] | +4.4 [+1.3, +8.2] | +7.6 [+2.5, +13.3] |
| settled | contested | 244 | 244 | 95.5/85.7 | 1.6/6.6 | 0.4/2.9 | 2.9/6.6 | 0.0/1.2 | +4.9 [+1.2, +9.0] | +3.7 [+0.4, +7.4] | +8.6 [+3.7, +13.9] |
| settled | uncontested | 72 | 72 | 97.2/94.4 | 1.4/2.8 | 0.0/2.8 | 1.4/1.4 | 0.0/1.4 | +1.4 [+0.0, +4.2] | +0.0 [-4.2, +4.2] | +1.4 [-2.8, +5.6] |
| settled | left-coded | 78 | 78 | 94.9/75.6 | 3.8/10.3 | 1.3/5.1 | 1.3/12.8 | 0.0/1.3 | +6.4 [-1.3, +16.7] | +11.5 [+5.1, +20.5] | +17.9 [+7.7, +29.5] |
| settled | right-coded | 118 | 118 | 95.8/95.8 | 0.8/0.0 | 0.0/0.8 | 3.4/2.5 | 0.0/1.7 | -0.8 [-2.5, +0.0] | -0.8 [-5.9, +4.2] | -1.7 [-6.8, +3.4] |
| settled | uncoded | 120 | 120 | 96.7/87.5 | 0.8/8.3 | 0.0/3.3 | 2.5/3.3 | 0.0/0.8 | +7.5 [+2.5, +14.2] | +0.8 [-1.7, +4.2] | +8.3 [+2.5, +15.0] |

#### answer length, mean words, original / treated

- advice | all: 646 / 379
- advocacy | all: 75 / 79
- settled | all: 341 / 210
- settled | contested: 354 / 230
- settled | uncontested: 298 / 143
- settled | left-coded: 379 / 235
- settled | right-coded: 341 / 205
- settled | uncoded: 316 / 198

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 90.0/62.5 | 7.5/35.0 | 2.5/2.5 | 0.0/0.0 |
| variant=none | 40/40 | 90.0/62.5 | 7.5/35.0 | 2.5/2.5 | 0.0/0.0 |
| right-coded | 14/14 | 92.9/64.3 | 7.1/28.6 | 0.0/7.1 | 0.0/0.0 |
| left-coded | 12/12 | 75.0/41.7 | 16.7/58.3 | 8.3/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 100.0/78.6 | 0.0/21.4 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/83.3 | 10.0/10.0 | 0.0/6.7 |
| variant=none | 30/30 | 90.0/83.3 | 10.0/10.0 | 0.0/6.7 |
| right-coded | 10/10 | 100.0/90.0 | 0.0/0.0 | 0.0/10.0 |
| left-coded | 10/10 | 100.0/90.0 | 0.0/0.0 | 0.0/10.0 |
| uncoded | 10/10 | 70.0/70.0 | 30.0/30.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.8 (n=158) / 91.5 (n=136)
- contested: 94.2 (n=122) / 90.5 (n=103)
- uncontested: 96.8 (n=36) / 94.5 (n=33)
