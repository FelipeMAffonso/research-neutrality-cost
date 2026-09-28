# Qwen2.5-32B: untransformed (ShareGPT) against the original, the extended set, version 1

original: <outputs>/qwen2.5-32b/original/judged_extended_v1.jsonl

condition untransformed: <outputs>/qwen2.5-32b/untransformed/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 92.1/88.0 | 7.3/8.9 | 4.7/7.6 | 0.6/3.2 | 0.0/0.0 | +1.6 [-2.2, +5.4] | +2.5 [+0.6, +4.4] | +4.1 [+0.0, +8.2] |
| settled | variant=belief_wrong | 158 | 158 | 90.5/82.9 | 8.9/13.3 | 7.6/12.7 | 0.6/3.8 | 0.0/0.0 | +4.4 [-0.6, +9.5] | +3.2 [+0.0, +7.0] | +7.6 [+1.9, +13.3] |
| settled | variant=confidence | 158 | 158 | 93.7/93.0 | 5.7/4.4 | 1.9/2.5 | 0.6/2.5 | 0.0/0.0 | -1.3 [-6.3, +3.2] | +1.9 [-0.6, +5.1] | +0.6 [-4.4, +5.7] |
| settled | contested | 244 | 244 | 90.2/86.5 | 9.4/11.1 | 5.3/9.0 | 0.4/2.5 | 0.0/0.0 | +1.6 [-2.9, +6.6] | +2.0 [+0.4, +4.1] | +3.7 [-1.2, +8.6] |
| settled | uncontested | 72 | 72 | 98.6/93.1 | 0.0/1.4 | 2.8/2.8 | 1.4/5.6 | 0.0/0.0 | +1.4 [+0.0, +4.2] | +4.2 [-1.4, +9.7] | +5.6 [-1.4, +12.5] |
| settled | left-coded | 78 | 78 | 76.9/73.1 | 21.8/21.8 | 10.3/17.9 | 1.3/5.1 | 0.0/0.0 | +0.0 [-11.5, +12.8] | +3.8 [+0.0, +9.0] | +3.8 [-7.7, +16.7] |
| settled | right-coded | 118 | 118 | 98.3/93.2 | 1.7/5.9 | 1.7/1.7 | 0.0/0.8 | 0.0/0.0 | +4.2 [+0.0, +9.3] | +0.8 [+0.0, +2.5] | +5.1 [+0.8, +11.0] |
| settled | uncoded | 120 | 120 | 95.8/92.5 | 3.3/3.3 | 4.2/6.7 | 0.8/4.2 | 0.0/0.0 | +0.0 [-3.3, +3.3] | +3.3 [+0.0, +7.5] | +3.3 [-1.7, +8.3] |

#### answer length, mean words, original / treated

- advice | all: 211 / 169
- advocacy | all: 80 / 79
- settled | all: 121 / 105
- settled | contested: 124 / 106
- settled | uncontested: 109 / 99
- settled | left-coded: 135 / 109
- settled | right-coded: 116 / 105
- settled | uncoded: 116 / 101

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 62.5/62.5 | 37.5/37.5 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 62.5/62.5 | 37.5/37.5 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 78.6/57.1 | 21.4/42.9 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 33.3/41.7 | 66.7/58.3 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 71.4/85.7 | 28.6/14.3 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/93.3 | 10.0/6.7 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/93.3 | 10.0/6.7 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/90.0 | 20.0/10.0 | 0.0/0.0 |
| uncoded | 10/10 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.6 (n=158) / 93.3 (n=158)
- contested: 93.0 (n=122) / 92.8 (n=122)
- uncontested: 95.8 (n=36) / 95.1 (n=36)
