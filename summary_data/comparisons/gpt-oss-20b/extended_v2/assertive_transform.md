# gpt-oss-20b: assertive transform (ShareGPT) against the original, the extended set, version 2

original: <outputs>/gpt-oss-20b/original/judged_extended_v2.jsonl

condition assertive_transform: <outputs>/gpt-oss-20b/assertive_transform/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 96.5/86.4 | 0.9/5.4 | 0.6/3.8 | 2.5/6.3 | 0.0/1.9 | +4.4 [+2.2, +7.0] | +3.8 [+0.6, +7.3] | +8.2 [+4.7, +12.0] |
| settled | variant=belief_wrong | 158 | 158 | 95.6/83.5 | 0.6/5.1 | 0.0/4.4 | 3.8/7.6 | 0.0/3.8 | +4.4 [+1.3, +8.2] | +3.8 [-0.6, +8.9] | +8.2 [+2.5, +13.9] |
| settled | variant=confidence | 158 | 158 | 97.5/89.2 | 1.3/5.7 | 1.3/3.2 | 1.3/5.1 | 0.0/0.0 | +4.4 [+1.3, +7.6] | +3.8 [+0.0, +8.2] | +8.2 [+3.2, +13.3] |
| settled | contested | 244 | 244 | 96.3/84.4 | 0.8/5.7 | 0.8/4.5 | 2.9/7.8 | 0.0/2.0 | +4.9 [+2.0, +8.2] | +4.9 [+1.2, +9.0] | +9.8 [+5.7, +14.3] |
| settled | uncontested | 72 | 72 | 97.2/93.1 | 1.4/4.2 | 0.0/1.4 | 1.4/1.4 | 0.0/1.4 | +2.8 [+0.0, +6.9] | +0.0 [-4.2, +4.2] | +2.8 [-2.8, +8.3] |
| settled | left-coded | 52 | 52 | 98.1/78.8 | 1.9/3.8 | 0.0/11.5 | 0.0/15.4 | 0.0/1.9 | +1.9 [-3.8, +7.7] | +15.4 [+5.8, +26.9] | +17.3 [+7.7, +26.9] |
| settled | right-coded | 118 | 118 | 95.8/89.0 | 0.0/4.2 | 0.0/3.4 | 4.2/5.9 | 0.0/0.8 | +4.2 [+0.8, +8.5] | +1.7 [-3.4, +7.6] | +5.9 [+0.0, +12.7] |
| settled | uncoded | 146 | 146 | 96.6/87.0 | 1.4/6.8 | 1.4/1.4 | 2.1/3.4 | 0.0/2.7 | +5.5 [+2.1, +9.6] | +1.4 [-2.1, +4.8] | +6.8 [+2.1, +11.6] |

#### answer length, mean words, original / treated

- advice | all: 645 / 388
- advocacy | all: 75 / 74
- settled | all: 343 / 196
- settled | contested: 353 / 206
- settled | uncontested: 308 / 161
- settled | left-coded: 386 / 238
- settled | right-coded: 334 / 205
- settled | uncoded: 335 / 173

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 90.0/70.0 | 7.5/25.0 | 2.5/5.0 | 0.0/0.0 |
| variant=none | 40/40 | 90.0/70.0 | 7.5/25.0 | 2.5/5.0 | 0.0/0.0 |
| right-coded | 14/14 | 100.0/71.4 | 0.0/28.6 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 75.0/41.7 | 16.7/41.7 | 8.3/16.7 | 0.0/0.0 |
| uncoded | 14/14 | 92.9/92.9 | 7.1/7.1 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/86.7 | 10.0/10.0 | 0.0/3.3 |
| variant=none | 30/30 | 90.0/86.7 | 10.0/10.0 | 0.0/3.3 |
| right-coded | 10/10 | 100.0/80.0 | 0.0/10.0 | 0.0/10.0 |
| left-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 10/10 | 70.0/80.0 | 30.0/20.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 95.0 (n=158) / 92.1 (n=136)
- contested: 94.5 (n=122) / 91.3 (n=103)
- uncontested: 96.9 (n=36) / 94.8 (n=33)
