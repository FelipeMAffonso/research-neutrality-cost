# gpt-oss-20b: mandate transform (ShareGPT) against the original, the extended set, version 1

original: <outputs>/gpt-oss-20b/original/judged_extended_v1.jsonl

condition mandate_transform: <outputs>/gpt-oss-20b/mandate_transform/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 95.9/86.4 | 1.6/6.0 | 0.3/4.4 | 2.5/5.4 | 0.0/2.2 | +4.4 [+1.9, +7.3] | +2.8 [+0.3, +5.4] | +7.3 [+3.8, +10.8] |
| settled | variant=belief_wrong | 158 | 158 | 96.2/84.2 | 0.0/5.1 | 0.0/5.1 | 3.8/6.3 | 0.0/4.4 | +5.1 [+1.9, +8.9] | +2.5 [-1.9, +7.0] | +7.6 [+1.9, +13.3] |
| settled | variant=confidence | 158 | 158 | 95.6/88.6 | 3.2/7.0 | 0.6/3.8 | 1.3/4.4 | 0.0/0.0 | +3.8 [-0.6, +8.2] | +3.2 [+0.6, +6.3] | +7.0 [+1.9, +12.0] |
| settled | contested | 244 | 244 | 95.5/84.0 | 1.6/7.4 | 0.4/4.5 | 2.9/6.1 | 0.0/2.5 | +5.7 [+2.5, +9.0] | +3.3 [+0.4, +6.1] | +9.0 [+4.9, +13.1] |
| settled | uncontested | 72 | 72 | 97.2/94.4 | 1.4/1.4 | 0.0/4.2 | 1.4/2.8 | 0.0/1.4 | +0.0 [-4.2, +4.2] | +1.4 [-2.8, +5.6] | +1.4 [-2.8, +5.6] |
| settled | left-coded | 78 | 78 | 94.9/74.4 | 3.8/14.1 | 1.3/7.7 | 1.3/9.0 | 0.0/2.6 | +10.3 [+3.8, +17.9] | +7.7 [+2.6, +14.1] | +17.9 [+10.3, +26.9] |
| settled | right-coded | 118 | 118 | 95.8/91.5 | 0.8/2.5 | 0.0/1.7 | 3.4/3.4 | 0.0/2.5 | +1.7 [-1.7, +5.1] | +0.0 [-3.4, +3.4] | +1.7 [-2.5, +6.8] |
| settled | uncoded | 120 | 120 | 96.7/89.2 | 0.8/4.2 | 0.0/5.0 | 2.5/5.0 | 0.0/1.7 | +3.3 [-0.8, +7.5] | +2.5 [-1.7, +6.7] | +5.8 [+0.8, +10.8] |

#### answer length, mean words, original / treated

- advice | all: 646 / 371
- advocacy | all: 75 / 74
- settled | all: 341 / 203
- settled | contested: 354 / 214
- settled | uncontested: 298 / 168
- settled | left-coded: 379 / 256
- settled | right-coded: 341 / 178
- settled | uncoded: 316 / 194

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 90.0/77.5 | 7.5/20.0 | 2.5/2.5 | 0.0/0.0 |
| variant=none | 40/40 | 90.0/77.5 | 7.5/20.0 | 2.5/2.5 | 0.0/0.0 |
| right-coded | 14/14 | 92.9/85.7 | 7.1/14.3 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 75.0/50.0 | 16.7/50.0 | 8.3/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 100.0/92.9 | 0.0/0.0 | 0.0/7.1 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/80.0 | 10.0/13.3 | 0.0/6.7 |
| variant=none | 30/30 | 90.0/80.0 | 10.0/13.3 | 0.0/6.7 |
| right-coded | 10/10 | 100.0/80.0 | 0.0/10.0 | 0.0/10.0 |
| left-coded | 10/10 | 100.0/80.0 | 0.0/10.0 | 0.0/10.0 |
| uncoded | 10/10 | 70.0/80.0 | 30.0/20.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.8 (n=158) / 91.7 (n=136)
- contested: 94.2 (n=122) / 90.9 (n=105)
- uncontested: 96.8 (n=36) / 94.5 (n=31)
