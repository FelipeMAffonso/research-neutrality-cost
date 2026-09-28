# Qwen3.8-27B: neutral transform (ShareGPT) against the original, the extended set, version 1

original: <outputs>/qwen3.8-27b/original/judged_extended_v1.jsonl

condition neutral_transform: <outputs>/qwen3.8-27b/neutral_transform/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 93.0/94.6 | 0.9/0.9 | 0.3/0.9 | 4.7/4.4 | 1.3/0.0 | +0.0 [-1.3, +1.3] | -0.3 [-1.6, +0.9] | -0.3 [-2.2, +1.3] |
| settled | variant=belief_wrong | 158 | 158 | 87.3/90.5 | 1.3/1.9 | 0.0/0.6 | 8.9/7.6 | 2.5/0.0 | +0.6 [-1.3, +2.5] | -1.3 [-3.8, +1.3] | -0.6 [-3.8, +2.5] |
| settled | variant=confidence | 158 | 158 | 98.7/98.7 | 0.6/0.0 | 0.6/1.3 | 0.6/1.3 | 0.0/0.0 | -0.6 [-1.9, +0.0] | +0.6 [+0.0, +1.9] | +0.0 [-1.9, +1.9] |
| settled | contested | 244 | 244 | 93.4/95.5 | 1.2/1.2 | 0.4/1.2 | 4.1/3.3 | 1.2/0.0 | +0.0 [-1.6, +1.6] | -0.8 [-2.5, +0.8] | -0.8 [-3.3, +1.6] |
| settled | uncontested | 72 | 72 | 91.7/91.7 | 0.0/0.0 | 0.0/0.0 | 6.9/8.3 | 1.4/0.0 | +0.0 [+0.0, +0.0] | +1.4 [+0.0, +4.2] | +1.4 [+0.0, +4.2] |
| settled | left-coded | 78 | 78 | 96.2/96.2 | 2.6/3.8 | 1.3/3.8 | 0.0/0.0 | 1.3/0.0 | +1.3 [-2.6, +6.4] | +0.0 [+0.0, +0.0] | +1.3 [-2.6, +6.4] |
| settled | right-coded | 118 | 118 | 92.4/95.8 | 0.0/0.0 | 0.0/0.0 | 5.9/4.2 | 1.7/0.0 | +0.0 [+0.0, +0.0] | -1.7 [-5.1, +1.7] | -1.7 [-5.1, +1.7] |
| settled | uncoded | 120 | 120 | 91.7/92.5 | 0.8/0.0 | 0.0/0.0 | 6.7/7.5 | 0.8/0.0 | -0.8 [-2.5, +0.0] | +0.8 [+0.0, +2.5] | +0.0 [-2.5, +2.5] |

#### answer length, mean words, original / treated

- advice | all: 204 / 207
- advocacy | all: 80 / 81
- settled | all: 126 / 127
- settled | contested: 127 / 128
- settled | uncontested: 125 / 125
- settled | left-coded: 133 / 133
- settled | right-coded: 123 / 123
- settled | uncoded: 126 / 127

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 92.5/92.5 | 7.5/7.5 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 92.5/92.5 | 7.5/7.5 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 92.9/92.9 | 7.1/7.1 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 91.7/91.7 | 8.3/8.3 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 92.9/92.9 | 7.1/7.1 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 96.7/96.7 | 3.3/3.3 | 0.0/0.0 |
| variant=none | 30/30 | 96.7/96.7 | 3.3/3.3 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 10/10 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 98.6 (n=158) / 98.8 (n=158)
- contested: 98.4 (n=122) / 98.5 (n=122)
- uncontested: 99.6 (n=36) / 99.7 (n=36)
