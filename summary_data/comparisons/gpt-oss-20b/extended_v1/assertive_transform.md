# gpt-oss-20b: assertive transform (ShareGPT) against the original, the extended set, version 1

original: <outputs>/gpt-oss-20b/original/judged_extended_v1.jsonl

condition assertive_transform: <outputs>/gpt-oss-20b/assertive_transform/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 95.9/86.4 | 1.6/5.1 | 0.3/3.8 | 2.5/7.3 | 0.0/1.3 | +3.5 [+0.9, +6.0] | +4.7 [+1.6, +7.9] | +8.2 [+4.4, +12.0] |
| settled | variant=belief_wrong | 158 | 158 | 96.2/85.4 | 0.0/3.8 | 0.0/4.4 | 3.8/8.2 | 0.0/2.5 | +3.8 [+1.3, +7.0] | +4.4 [+0.0, +8.9] | +8.2 [+2.5, +13.9] |
| settled | variant=confidence | 158 | 158 | 95.6/87.3 | 3.2/6.3 | 0.6/3.2 | 1.3/6.3 | 0.0/0.0 | +3.2 [-0.6, +7.6] | +5.1 [+1.3, +8.9] | +8.2 [+2.5, +13.9] |
| settled | contested | 244 | 244 | 95.5/84.0 | 1.6/6.1 | 0.4/3.7 | 2.9/8.2 | 0.0/1.6 | +4.5 [+1.6, +7.8] | +5.3 [+1.6, +9.4] | +9.8 [+5.3, +14.8] |
| settled | uncontested | 72 | 72 | 97.2/94.4 | 1.4/1.4 | 0.0/4.2 | 1.4/4.2 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +2.8 [-2.8, +8.3] | +2.8 [-2.8, +8.3] |
| settled | left-coded | 78 | 78 | 94.9/76.9 | 3.8/10.3 | 1.3/6.4 | 1.3/10.3 | 0.0/2.6 | +6.4 [+0.0, +14.1] | +9.0 [+3.8, +15.4] | +15.4 [+6.4, +25.6] |
| settled | right-coded | 118 | 118 | 95.8/89.8 | 0.8/2.5 | 0.0/0.8 | 3.4/6.8 | 0.0/0.8 | +1.7 [-1.7, +5.1] | +3.4 [-1.7, +9.3] | +5.1 [-1.7, +11.9] |
| settled | uncoded | 120 | 120 | 96.7/89.2 | 0.8/4.2 | 0.0/5.0 | 2.5/5.8 | 0.0/0.8 | +3.3 [+0.8, +6.7] | +3.3 [-0.8, +7.5] | +6.7 [+1.7, +12.5] |

#### answer length, mean words, original / treated

- advice | all: 646 / 445
- advocacy | all: 75 / 74
- settled | all: 341 / 192
- settled | contested: 354 / 201
- settled | uncontested: 298 / 161
- settled | left-coded: 379 / 231
- settled | right-coded: 341 / 181
- settled | uncoded: 316 / 178

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 90.0/72.5 | 7.5/25.0 | 2.5/2.5 | 0.0/0.0 |
| variant=none | 40/40 | 90.0/72.5 | 7.5/25.0 | 2.5/2.5 | 0.0/0.0 |
| right-coded | 14/14 | 92.9/78.6 | 7.1/21.4 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 75.0/33.3 | 16.7/58.3 | 8.3/8.3 | 0.0/0.0 |
| uncoded | 14/14 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 |
| uncoded | 10/10 | 70.0/90.0 | 30.0/10.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.8 (n=158) / 92.0 (n=131)
- contested: 94.2 (n=122) / 91.2 (n=103)
- uncontested: 96.8 (n=36) / 95.1 (n=28)
