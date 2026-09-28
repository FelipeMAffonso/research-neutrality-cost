# Qwen2.5-32B: neutral transform (ShareGPT) against the original, the extended set, version 1

original: <outputs>/qwen2.5-32b/original/judged_extended_v1.jsonl

condition neutral_transform: <outputs>/qwen2.5-32b/neutral_transform/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 92.1/85.1 | 7.3/11.4 | 4.7/4.1 | 0.6/3.5 | 0.0/0.0 | +4.1 [+0.9, +7.3] | +2.8 [+1.3, +4.7] | +7.0 [+3.5, +10.4] |
| settled | variant=belief_wrong | 158 | 158 | 90.5/77.2 | 8.9/19.0 | 7.6/5.1 | 0.6/3.8 | 0.0/0.0 | +10.1 [+4.4, +15.8] | +3.2 [+0.0, +6.3] | +13.3 [+7.6, +19.6] |
| settled | variant=confidence | 158 | 158 | 93.7/93.0 | 5.7/3.8 | 1.9/3.2 | 0.6/3.2 | 0.0/0.0 | -1.9 [-5.7, +1.9] | +2.5 [+0.6, +5.1] | +0.6 [-3.8, +4.4] |
| settled | contested | 244 | 244 | 90.2/82.4 | 9.4/13.9 | 5.3/3.3 | 0.4/3.7 | 0.0/0.0 | +4.5 [+0.8, +8.2] | +3.3 [+1.2, +5.7] | +7.8 [+3.3, +12.3] |
| settled | uncontested | 72 | 72 | 98.6/94.4 | 0.0/2.8 | 2.8/6.9 | 1.4/2.8 | 0.0/0.0 | +2.8 [+0.0, +6.9] | +1.4 [+0.0, +4.2] | +4.2 [+0.0, +9.7] |
| settled | left-coded | 78 | 78 | 76.9/70.5 | 21.8/25.6 | 10.3/5.1 | 1.3/3.8 | 0.0/0.0 | +3.8 [-6.4, +14.1] | +2.6 [+0.0, +6.4] | +6.4 [-3.8, +16.7] |
| settled | right-coded | 118 | 118 | 98.3/89.0 | 1.7/6.8 | 1.7/1.7 | 0.0/4.2 | 0.0/0.0 | +5.1 [+1.7, +9.3] | +4.2 [+0.8, +7.6] | +9.3 [+4.2, +15.3] |
| settled | uncoded | 120 | 120 | 95.8/90.8 | 3.3/6.7 | 4.2/5.8 | 0.8/2.5 | 0.0/0.0 | +3.3 [+0.0, +7.5] | +1.7 [+0.0, +4.2] | +5.0 [+0.8, +10.0] |

#### answer length, mean words, original / treated

- advice | all: 211 / 171
- advocacy | all: 80 / 77
- settled | all: 121 / 94
- settled | contested: 124 / 96
- settled | uncontested: 109 / 89
- settled | left-coded: 135 / 104
- settled | right-coded: 116 / 91
- settled | uncoded: 116 / 91

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 62.5/67.5 | 37.5/30.0 | 0.0/2.5 | 0.0/0.0 |
| variant=none | 40/40 | 62.5/67.5 | 37.5/30.0 | 0.0/2.5 | 0.0/0.0 |
| right-coded | 14/14 | 78.6/64.3 | 21.4/28.6 | 0.0/7.1 | 0.0/0.0 |
| left-coded | 12/12 | 33.3/50.0 | 66.7/50.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 71.4/85.7 | 28.6/14.3 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/86.7 | 10.0/13.3 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/86.7 | 10.0/13.3 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/90.0 | 20.0/10.0 | 0.0/0.0 |
| uncoded | 10/10 | 90.0/70.0 | 10.0/30.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.6 (n=158) / 93.6 (n=158)
- contested: 93.0 (n=122) / 92.9 (n=122)
- uncontested: 95.8 (n=36) / 96.2 (n=36)
