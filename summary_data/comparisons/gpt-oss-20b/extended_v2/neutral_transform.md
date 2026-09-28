# gpt-oss-20b: neutral transform (ShareGPT) against the original, the extended set, version 2

original: <outputs>/gpt-oss-20b/original/judged_extended_v2.jsonl

condition neutral_transform: <outputs>/gpt-oss-20b/neutral_transform/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 96.5/84.2 | 0.9/7.3 | 0.6/4.1 | 2.5/7.0 | 0.0/1.6 | +6.3 [+3.5, +9.2] | +4.4 [+1.6, +7.3] | +10.8 [+7.0, +14.6] |
| settled | variant=belief_wrong | 158 | 158 | 95.6/82.3 | 0.6/7.0 | 0.0/6.3 | 3.8/7.6 | 0.0/3.2 | +6.3 [+2.5, +10.8] | +3.8 [-0.6, +8.2] | +10.1 [+4.4, +15.8] |
| settled | variant=confidence | 158 | 158 | 97.5/86.1 | 1.3/7.6 | 1.3/1.9 | 1.3/6.3 | 0.0/0.0 | +6.3 [+2.5, +10.1] | +5.1 [+1.3, +8.9] | +11.4 [+6.3, +17.1] |
| settled | contested | 244 | 244 | 96.3/81.6 | 0.8/8.2 | 0.8/4.5 | 2.9/8.2 | 0.0/2.0 | +7.4 [+4.1, +11.1] | +5.3 [+2.0, +9.0] | +12.7 [+8.2, +17.2] |
| settled | uncontested | 72 | 72 | 97.2/93.1 | 1.4/4.2 | 0.0/2.8 | 1.4/2.8 | 0.0/0.0 | +2.8 [+0.0, +6.9] | +1.4 [-2.8, +5.6] | +4.2 [+0.0, +8.3] |
| settled | left-coded | 52 | 52 | 98.1/75.0 | 1.9/13.5 | 0.0/7.7 | 0.0/9.6 | 0.0/1.9 | +11.5 [+1.9, +23.1] | +9.6 [+1.9, +19.2] | +21.2 [+9.6, +32.7] |
| settled | right-coded | 118 | 118 | 95.8/86.4 | 0.0/4.2 | 0.0/0.8 | 4.2/7.6 | 0.0/1.7 | +4.2 [+0.8, +8.5] | +3.4 [-0.8, +8.5] | +7.6 [+1.7, +13.6] |
| settled | uncoded | 146 | 146 | 96.6/85.6 | 1.4/7.5 | 1.4/5.5 | 2.1/5.5 | 0.0/1.4 | +6.2 [+2.7, +10.3] | +3.4 [-0.7, +7.5] | +9.6 [+4.8, +14.4] |

#### answer length, mean words, original / treated

- advice | all: 645 / 421
- advocacy | all: 75 / 76
- settled | all: 343 / 189
- settled | contested: 353 / 198
- settled | uncontested: 308 / 157
- settled | left-coded: 386 / 228
- settled | right-coded: 334 / 184
- settled | uncoded: 335 / 178

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 90.0/72.5 | 7.5/27.5 | 2.5/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 90.0/72.5 | 7.5/27.5 | 2.5/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 100.0/78.6 | 0.0/21.4 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 75.0/41.7 | 16.7/58.3 | 8.3/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 92.9/92.9 | 7.1/7.1 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/86.7 | 10.0/10.0 | 0.0/3.3 |
| variant=none | 30/30 | 90.0/86.7 | 10.0/10.0 | 0.0/3.3 |
| right-coded | 10/10 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/90.0 | 0.0/0.0 | 0.0/10.0 |
| uncoded | 10/10 | 70.0/80.0 | 30.0/20.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 95.0 (n=158) / 91.3 (n=132)
- contested: 94.5 (n=122) / 90.4 (n=101)
- uncontested: 96.9 (n=36) / 94.2 (n=31)
