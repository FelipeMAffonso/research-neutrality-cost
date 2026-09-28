# Qwen2.5-7B: assertive transform (ShareGPT) against the original, the extended set, version 1

original: <outputs>/qwen2.5-7b/original/judged_extended_v1.jsonl

condition assertive_transform: <outputs>/qwen2.5-7b/assertive_transform/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 89.2/85.8 | 8.9/11.1 | 3.2/8.2 | 1.9/3.2 | 0.0/0.0 | +2.2 [-0.6, +5.4] | +1.3 [-0.6, +3.2] | +3.5 [+0.3, +7.0] |
| settled | variant=belief_wrong | 158 | 158 | 86.7/82.9 | 13.3/14.6 | 5.1/12.7 | 0.0/2.5 | 0.0/0.0 | +1.3 [-3.8, +6.3] | +2.5 [+0.6, +5.1] | +3.8 [-1.9, +9.5] |
| settled | variant=confidence | 158 | 158 | 91.8/88.6 | 4.4/7.6 | 1.3/3.8 | 3.8/3.8 | 0.0/0.0 | +3.2 [-1.3, +8.2] | +0.0 [-2.5, +2.5] | +3.2 [-1.3, +8.2] |
| settled | contested | 244 | 244 | 86.5/82.4 | 11.1/14.3 | 3.3/8.2 | 2.5/3.3 | 0.0/0.0 | +3.3 [-0.8, +7.0] | +0.8 [-1.2, +2.9] | +4.1 [+0.0, +8.2] |
| settled | uncontested | 72 | 72 | 98.6/97.2 | 1.4/0.0 | 2.8/8.3 | 0.0/2.8 | 0.0/0.0 | -1.4 [-4.2, +0.0] | +2.8 [+0.0, +6.9] | +1.4 [+0.0, +4.2] |
| settled | left-coded | 78 | 78 | 73.1/66.7 | 23.1/30.8 | 9.0/17.9 | 3.8/2.6 | 0.0/0.0 | +7.7 [-2.6, +16.7] | -1.3 [-3.8, +0.0] | +6.4 [-3.8, +15.4] |
| settled | right-coded | 118 | 118 | 96.6/91.5 | 1.7/4.2 | 0.0/4.2 | 1.7/4.2 | 0.0/0.0 | +2.5 [+0.0, +5.9] | +2.5 [-0.8, +5.9] | +5.1 [+0.8, +9.3] |
| settled | uncoded | 120 | 120 | 92.5/92.5 | 6.7/5.0 | 2.5/5.8 | 0.8/2.5 | 0.0/0.0 | -1.7 [-5.8, +2.5] | +1.7 [+0.0, +4.2] | +0.0 [-4.2, +4.2] |

#### answer length, mean words, original / treated

- advice | all: 217 / 165
- advocacy | all: 79 / 70
- settled | all: 119 / 99
- settled | contested: 123 / 102
- settled | uncontested: 105 / 88
- settled | left-coded: 133 / 115
- settled | right-coded: 115 / 92
- settled | uncoded: 114 / 95

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 65.0/72.5 | 35.0/27.5 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 65.0/72.5 | 35.0/27.5 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 71.4/71.4 | 28.6/28.6 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 41.7/58.3 | 58.3/41.7 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 78.6/85.7 | 21.4/14.3 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 93.3/86.7 | 6.7/13.3 | 0.0/0.0 |
| variant=none | 30/30 | 93.3/86.7 | 6.7/13.3 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/80.0 | 0.0/20.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/90.0 | 20.0/10.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.3 (n=158) / 93.7 (n=157)
- contested: 92.2 (n=122) / 93.0 (n=122)
- uncontested: 97.1 (n=36) / 96.2 (n=35)
