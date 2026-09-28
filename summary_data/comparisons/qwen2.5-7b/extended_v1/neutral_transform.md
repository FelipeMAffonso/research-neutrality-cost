# Qwen2.5-7B: neutral transform (ShareGPT) against the original, the extended set, version 1

original: <outputs>/qwen2.5-7b/original/judged_extended_v1.jsonl

condition neutral_transform: <outputs>/qwen2.5-7b/neutral_transform/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 89.2/83.9 | 8.9/11.7 | 3.2/6.0 | 1.9/4.4 | 0.0/0.0 | +2.8 [-0.9, +6.3] | +2.5 [+0.3, +4.7] | +5.4 [+1.3, +9.2] |
| settled | variant=belief_wrong | 158 | 158 | 86.7/78.5 | 13.3/17.1 | 5.1/7.6 | 0.0/4.4 | 0.0/0.0 | +3.8 [-3.2, +10.1] | +4.4 [+1.9, +8.2] | +8.2 [+0.6, +15.2] |
| settled | variant=confidence | 158 | 158 | 91.8/89.2 | 4.4/6.3 | 1.3/4.4 | 3.8/4.4 | 0.0/0.0 | +1.9 [-2.5, +6.3] | +0.6 [-2.5, +3.8] | +2.5 [-2.5, +8.2] |
| settled | contested | 244 | 244 | 86.5/80.3 | 11.1/15.2 | 3.3/6.6 | 2.5/4.5 | 0.0/0.0 | +4.1 [-0.8, +8.6] | +2.0 [-0.4, +4.5] | +6.1 [+0.8, +11.1] |
| settled | uncontested | 72 | 72 | 98.6/95.8 | 1.4/0.0 | 2.8/4.2 | 0.0/4.2 | 0.0/0.0 | -1.4 [-4.2, +0.0] | +4.2 [+0.0, +9.7] | +2.8 [+0.0, +6.9] |
| settled | left-coded | 78 | 78 | 73.1/64.1 | 23.1/29.5 | 9.0/14.1 | 3.8/6.4 | 0.0/0.0 | +6.4 [-5.1, +17.9] | +2.6 [-2.6, +7.7] | +9.0 [-3.8, +20.5] |
| settled | right-coded | 118 | 118 | 96.6/89.8 | 1.7/6.8 | 0.0/1.7 | 1.7/3.4 | 0.0/0.0 | +5.1 [+0.8, +10.2] | +1.7 [-1.7, +5.9] | +6.8 [+1.7, +11.9] |
| settled | uncoded | 120 | 120 | 92.5/90.8 | 6.7/5.0 | 2.5/5.0 | 0.8/4.2 | 0.0/0.0 | -1.7 [-5.8, +2.5] | +3.3 [+0.8, +6.7] | +1.7 [-3.3, +6.7] |

#### answer length, mean words, original / treated

- advice | all: 217 / 171
- advocacy | all: 79 / 85
- settled | all: 119 / 106
- settled | contested: 123 / 108
- settled | uncontested: 105 / 101
- settled | left-coded: 133 / 113
- settled | right-coded: 115 / 106
- settled | uncoded: 114 / 102

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 65.0/75.0 | 35.0/25.0 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 65.0/75.0 | 35.0/25.0 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 71.4/78.6 | 28.6/21.4 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 41.7/50.0 | 58.3/50.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 78.6/92.9 | 21.4/7.1 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 93.3/86.7 | 6.7/13.3 | 0.0/0.0 |
| variant=none | 30/30 | 93.3/86.7 | 6.7/13.3 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/70.0 | 0.0/30.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/100.0 | 20.0/0.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.3 (n=158) / 93.3 (n=156)
- contested: 92.2 (n=122) / 92.4 (n=121)
- uncontested: 97.1 (n=36) / 96.3 (n=35)
