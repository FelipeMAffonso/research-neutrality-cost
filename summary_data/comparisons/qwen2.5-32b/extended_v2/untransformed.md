# Qwen2.5-32B: untransformed (ShareGPT) against the original, the extended set, version 2

original: <outputs>/qwen2.5-32b/original/judged_extended_v2.jsonl

condition untransformed: <outputs>/qwen2.5-32b/untransformed/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 93.0/90.5 | 7.0/7.3 | 4.7/7.3 | 0.0/2.2 | 0.0/0.0 | +0.3 [-3.2, +3.8] | +2.2 [+0.6, +3.8] | +2.5 [-1.3, +6.3] |
| settled | variant=belief_wrong | 158 | 158 | 92.4/86.7 | 7.6/11.4 | 8.9/12.0 | 0.0/1.9 | 0.0/0.0 | +3.8 [-1.3, +8.9] | +1.9 [+0.0, +3.8] | +5.7 [+0.6, +10.8] |
| settled | variant=confidence | 158 | 158 | 93.7/94.3 | 6.3/3.2 | 0.6/2.5 | 0.0/2.5 | 0.0/0.0 | -3.2 [-7.6, +0.6] | +2.5 [+0.6, +5.1] | -0.6 [-5.1, +3.8] |
| settled | contested | 244 | 244 | 91.4/89.3 | 8.6/9.4 | 5.3/7.8 | 0.0/1.2 | 0.0/0.0 | +0.8 [-3.7, +5.7] | +1.2 [+0.0, +2.9] | +2.0 [-2.5, +7.0] |
| settled | uncontested | 72 | 72 | 98.6/94.4 | 1.4/0.0 | 2.8/5.6 | 0.0/5.6 | 0.0/0.0 | -1.4 [-4.2, +0.0] | +5.6 [+1.4, +11.1] | +4.2 [-1.4, +11.1] |
| settled | left-coded | 52 | 52 | 84.6/80.8 | 15.4/17.3 | 15.4/21.2 | 0.0/1.9 | 0.0/0.0 | +1.9 [-11.5, +15.4] | +1.9 [+0.0, +5.8] | +3.8 [-9.6, +19.2] |
| settled | right-coded | 118 | 118 | 98.3/94.9 | 1.7/4.2 | 1.7/1.7 | 0.0/0.8 | 0.0/0.0 | +2.5 [-0.8, +7.6] | +0.8 [+0.0, +2.5] | +3.4 [-0.8, +8.5] |
| settled | uncoded | 146 | 146 | 91.8/90.4 | 8.2/6.2 | 3.4/6.8 | 0.0/3.4 | 0.0/0.0 | -2.1 [-6.8, +2.7] | +3.4 [+0.7, +6.8] | +1.4 [-3.4, +6.2] |

#### answer length, mean words, original / treated

- advice | all: 216 / 162
- advocacy | all: 81 / 77
- settled | all: 120 / 105
- settled | contested: 123 / 108
- settled | uncontested: 112 / 94
- settled | left-coded: 138 / 114
- settled | right-coded: 115 / 105
- settled | uncoded: 119 / 102

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 60.0/65.0 | 40.0/35.0 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 60.0/65.0 | 40.0/35.0 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 78.6/64.3 | 21.4/35.7 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 33.3/58.3 | 66.7/41.7 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 64.3/71.4 | 35.7/28.6 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/80.0 | 20.0/20.0 | 0.0/0.0 |
| uncoded | 10/10 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.9 (n=158) / 93.4 (n=158)
- contested: 93.3 (n=122) / 93.0 (n=122)
- uncontested: 95.9 (n=36) / 95.0 (n=36)
