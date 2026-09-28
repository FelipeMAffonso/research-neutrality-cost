# Qwen2.5-7B: untransformed (ShareGPT) against the original, the extended set, version 2

original: <outputs>/qwen2.5-7b/original/judged_extended_v2.jsonl

condition untransformed: <outputs>/qwen2.5-7b/untransformed/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 89.2/85.4 | 8.9/9.5 | 3.2/5.1 | 1.9/5.1 | 0.0/0.0 | +0.6 [-3.5, +4.7] | +3.2 [+0.9, +5.7] | +3.8 [-0.3, +7.9] |
| settled | variant=belief_wrong | 158 | 158 | 84.2/81.6 | 14.6/11.4 | 5.1/6.3 | 1.3/7.0 | 0.0/0.0 | -3.2 [-9.5, +3.2] | +5.7 [+1.9, +10.1] | +2.5 [-4.4, +9.5] |
| settled | variant=confidence | 158 | 158 | 94.3/89.2 | 3.2/7.6 | 1.3/3.8 | 2.5/3.2 | 0.0/0.0 | +4.4 [+0.0, +9.5] | +0.6 [-1.9, +3.2] | +5.1 [+0.0, +10.8] |
| settled | contested | 244 | 244 | 86.5/82.8 | 11.1/12.3 | 3.7/6.1 | 2.5/4.9 | 0.0/0.0 | +1.2 [-4.1, +6.6] | +2.5 [-0.4, +5.3] | +3.7 [-2.0, +9.0] |
| settled | uncontested | 72 | 72 | 98.6/94.4 | 1.4/0.0 | 1.4/1.4 | 0.0/5.6 | 0.0/0.0 | -1.4 [-4.2, +0.0] | +5.6 [+1.4, +11.1] | +4.2 [+0.0, +9.7] |
| settled | left-coded | 52 | 52 | 78.8/71.2 | 17.3/19.2 | 9.6/11.5 | 3.8/9.6 | 0.0/0.0 | +1.9 [-13.5, +15.4] | +5.8 [+0.0, +13.5] | +7.7 [-7.7, +21.2] |
| settled | right-coded | 118 | 118 | 94.1/91.5 | 4.2/5.9 | 1.7/3.4 | 1.7/2.5 | 0.0/0.0 | +1.7 [-3.4, +5.9] | +0.8 [-2.5, +5.1] | +2.5 [-3.4, +8.5] |
| settled | uncoded | 146 | 146 | 89.0/85.6 | 9.6/8.9 | 2.1/4.1 | 1.4/5.5 | 0.0/0.0 | -0.7 [-6.8, +5.5] | +4.1 [+0.7, +8.2] | +3.4 [-2.7, +9.6] |

#### answer length, mean words, original / treated

- advice | all: 218 / 178
- advocacy | all: 80 / 87
- settled | all: 119 / 110
- settled | contested: 122 / 114
- settled | uncontested: 110 / 95
- settled | left-coded: 133 / 124
- settled | right-coded: 115 / 111
- settled | uncoded: 117 / 104

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 67.5/67.5 | 32.5/30.0 | 0.0/2.5 | 0.0/0.0 |
| variant=none | 40/40 | 67.5/67.5 | 32.5/30.0 | 0.0/2.5 | 0.0/0.0 |
| right-coded | 14/14 | 71.4/85.7 | 28.6/14.3 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 50.0/33.3 | 50.0/58.3 | 0.0/8.3 | 0.0/0.0 |
| uncoded | 14/14 | 78.6/78.6 | 21.4/21.4 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| right-coded | 10/10 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/80.0 | 0.0/20.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/100.0 | 20.0/0.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.3 (n=158) / 93.5 (n=157)
- contested: 92.3 (n=122) / 92.6 (n=121)
- uncontested: 96.9 (n=36) / 96.4 (n=36)
