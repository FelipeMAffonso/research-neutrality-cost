# Qwen2.5-32B: assertive transform (ShareGPT) against the original, the extended set, version 1

original: <outputs>/qwen2.5-32b/original/judged_extended_v1.jsonl

condition assertive_transform: <outputs>/qwen2.5-32b/assertive_transform/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 92.1/89.6 | 7.3/7.0 | 4.7/3.2 | 0.6/3.5 | 0.0/0.0 | -0.3 [-3.8, +3.5] | +2.8 [+1.3, +4.7] | +2.5 [-1.3, +6.6] |
| settled | variant=belief_wrong | 158 | 158 | 90.5/86.1 | 8.9/11.4 | 7.6/5.7 | 0.6/2.5 | 0.0/0.0 | +2.5 [-3.8, +8.9] | +1.9 [+0.0, +4.4] | +4.4 [-2.5, +10.8] |
| settled | variant=confidence | 158 | 158 | 93.7/93.0 | 5.7/2.5 | 1.9/0.6 | 0.6/4.4 | 0.0/0.0 | -3.2 [-7.0, +0.6] | +3.8 [+1.3, +7.0] | +0.6 [-3.2, +5.1] |
| settled | contested | 244 | 244 | 90.2/88.9 | 9.4/8.2 | 5.3/3.7 | 0.4/2.9 | 0.0/0.0 | -1.2 [-6.1, +3.7] | +2.5 [+0.8, +4.5] | +1.2 [-3.7, +6.1] |
| settled | uncontested | 72 | 72 | 98.6/91.7 | 0.0/2.8 | 2.8/1.4 | 1.4/5.6 | 0.0/0.0 | +2.8 [+0.0, +6.9] | +4.2 [+0.0, +9.7] | +6.9 [+1.4, +12.5] |
| settled | left-coded | 78 | 78 | 76.9/82.1 | 21.8/14.1 | 10.3/7.7 | 1.3/3.8 | 0.0/0.0 | -7.7 [-20.5, +5.1] | +2.6 [+0.0, +6.4] | -5.1 [-16.7, +7.7] |
| settled | right-coded | 118 | 118 | 98.3/94.1 | 1.7/3.4 | 1.7/1.7 | 0.0/2.5 | 0.0/0.0 | +1.7 [-1.7, +5.9] | +2.5 [+0.0, +5.9] | +4.2 [+0.0, +9.3] |
| settled | uncoded | 120 | 120 | 95.8/90.0 | 3.3/5.8 | 4.2/1.7 | 0.8/4.2 | 0.0/0.0 | +2.5 [-0.8, +5.8] | +3.3 [+0.8, +6.7] | +5.8 [+1.7, +10.8] |

#### answer length, mean words, original / treated

- advice | all: 211 / 132
- advocacy | all: 80 / 70
- settled | all: 121 / 83
- settled | contested: 124 / 85
- settled | uncontested: 109 / 76
- settled | left-coded: 135 / 91
- settled | right-coded: 116 / 79
- settled | uncoded: 116 / 81

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 62.5/70.0 | 37.5/25.0 | 0.0/5.0 | 0.0/0.0 |
| variant=none | 40/40 | 62.5/70.0 | 37.5/25.0 | 0.0/5.0 | 0.0/0.0 |
| right-coded | 14/14 | 78.6/78.6 | 21.4/14.3 | 0.0/7.1 | 0.0/0.0 |
| left-coded | 12/12 | 33.3/66.7 | 66.7/33.3 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 71.4/64.3 | 28.6/28.6 | 0.0/7.1 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/93.3 | 10.0/6.7 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/93.3 | 10.0/6.7 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/80.0 | 20.0/20.0 | 0.0/0.0 |
| uncoded | 10/10 | 90.0/100.0 | 10.0/0.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.6 (n=158) / 93.3 (n=158)
- contested: 93.0 (n=122) / 92.8 (n=122)
- uncontested: 95.8 (n=36) / 95.2 (n=36)
