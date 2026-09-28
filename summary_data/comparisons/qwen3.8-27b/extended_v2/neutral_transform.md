# Qwen3.8-27B: neutral transform (ShareGPT) against the original, the extended set, version 2

original: <outputs>/qwen3.8-27b/original/judged_extended_v2.jsonl

condition neutral_transform: <outputs>/qwen3.8-27b/neutral_transform/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 94.3/94.3 | 0.3/0.6 | 0.0/0.3 | 4.4/5.1 | 0.9/0.0 | +0.3 [+0.0, +0.9] | +0.6 [-1.6, +2.8] | +0.9 [-1.3, +3.2] |
| settled | variant=belief_wrong | 158 | 158 | 89.2/89.2 | 0.6/1.3 | 0.0/0.6 | 8.2/9.5 | 1.9/0.0 | +0.6 [+0.0, +1.9] | +1.3 [-3.2, +5.7] | +1.9 [-2.5, +6.3] |
| settled | variant=confidence | 158 | 158 | 99.4/99.4 | 0.0/0.0 | 0.0/0.0 | 0.6/0.6 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | contested | 244 | 244 | 95.1/95.9 | 0.4/0.8 | 0.0/0.4 | 3.7/3.3 | 0.8/0.0 | +0.4 [+0.0, +1.2] | -0.4 [-2.9, +2.0] | +0.0 [-2.5, +2.9] |
| settled | uncontested | 72 | 72 | 91.7/88.9 | 0.0/0.0 | 0.0/0.0 | 6.9/11.1 | 1.4/0.0 | +0.0 [+0.0, +0.0] | +4.2 [+0.0, +9.7] | +4.2 [+0.0, +9.7] |
| settled | left-coded | 52 | 52 | 96.2/96.2 | 0.0/1.9 | 0.0/0.0 | 3.8/1.9 | 0.0/0.0 | +1.9 [+0.0, +5.8] | -1.9 [-7.7, +3.8] | +0.0 [-7.7, +7.7] |
| settled | right-coded | 118 | 118 | 94.1/95.8 | 0.0/0.0 | 0.0/0.8 | 4.2/4.2 | 1.7/0.0 | +0.0 [+0.0, +0.0] | +0.0 [-4.2, +4.2] | +0.0 [-4.2, +4.2] |
| settled | uncoded | 146 | 146 | 93.8/92.5 | 0.7/0.7 | 0.0/0.0 | 4.8/6.8 | 0.7/0.0 | +0.0 [+0.0, +0.0] | +2.1 [+0.0, +4.8] | +2.1 [+0.0, +4.8] |

#### answer length, mean words, original / treated

- advice | all: 205 / 206
- advocacy | all: 79 / 80
- settled | all: 126 / 127
- settled | contested: 127 / 127
- settled | uncontested: 123 / 125
- settled | left-coded: 132 / 132
- settled | right-coded: 123 / 124
- settled | uncoded: 126 / 127

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 95.0/92.5 | 5.0/7.5 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 95.0/92.5 | 5.0/7.5 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 92.9/92.9 | 7.1/7.1 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 100.0/91.7 | 0.0/8.3 | 0.0/0.0 | 0.0/0.0 |
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

- all: 98.8 (n=158) / 98.8 (n=158)
- contested: 98.5 (n=122) / 98.6 (n=122)
- uncontested: 99.6 (n=36) / 99.7 (n=36)
