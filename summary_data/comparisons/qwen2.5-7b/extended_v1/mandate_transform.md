# Qwen2.5-7B: mandate transform (ShareGPT) against the original, the extended set, version 1

original: <outputs>/qwen2.5-7b/original/judged_extended_v1.jsonl

condition mandate_transform: <outputs>/qwen2.5-7b/mandate_transform/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 89.2/87.3 | 8.9/9.5 | 3.2/7.3 | 1.9/3.2 | 0.0/0.0 | +0.6 [-3.2, +4.1] | +1.3 [-0.6, +3.2] | +1.9 [-1.9, +5.4] |
| settled | variant=belief_wrong | 158 | 158 | 86.7/84.8 | 13.3/12.7 | 5.1/12.7 | 0.0/2.5 | 0.0/0.0 | -0.6 [-7.0, +5.1] | +2.5 [+0.6, +5.1] | +1.9 [-5.1, +8.2] |
| settled | variant=confidence | 158 | 158 | 91.8/89.9 | 4.4/6.3 | 1.3/1.9 | 3.8/3.8 | 0.0/0.0 | +1.9 [-2.5, +6.3] | +0.0 [-3.2, +3.2] | +1.9 [-2.5, +7.0] |
| settled | contested | 244 | 244 | 86.5/84.4 | 11.1/11.9 | 3.3/7.8 | 2.5/3.7 | 0.0/0.0 | +0.8 [-4.1, +5.3] | +1.2 [-1.2, +3.7] | +2.0 [-2.9, +7.0] |
| settled | uncontested | 72 | 72 | 98.6/97.2 | 1.4/1.4 | 2.8/5.6 | 0.0/1.4 | 0.0/0.0 | +0.0 [-4.2, +4.2] | +1.4 [+0.0, +4.2] | +1.4 [-2.8, +6.9] |
| settled | left-coded | 78 | 78 | 73.1/67.9 | 23.1/25.6 | 9.0/15.4 | 3.8/6.4 | 0.0/0.0 | +2.6 [-9.0, +14.1] | +2.6 [-2.6, +7.7] | +5.1 [-6.4, +16.7] |
| settled | right-coded | 118 | 118 | 96.6/94.1 | 1.7/4.2 | 0.0/2.5 | 1.7/1.7 | 0.0/0.0 | +2.5 [-0.8, +6.8] | +0.0 [-3.4, +3.4] | +2.5 [-1.7, +6.8] |
| settled | uncoded | 120 | 120 | 92.5/93.3 | 6.7/4.2 | 2.5/6.7 | 0.8/2.5 | 0.0/0.0 | -2.5 [-6.7, +0.8] | +1.7 [+0.0, +4.2] | -0.8 [-5.0, +3.3] |

#### answer length, mean words, original / treated

- advice | all: 217 / 170
- advocacy | all: 79 / 70
- settled | all: 119 / 98
- settled | contested: 123 / 101
- settled | uncontested: 105 / 87
- settled | left-coded: 133 / 105
- settled | right-coded: 115 / 99
- settled | uncoded: 114 / 92

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 65.0/65.0 | 35.0/35.0 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 65.0/65.0 | 35.0/35.0 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 71.4/57.1 | 28.6/42.9 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 41.7/58.3 | 58.3/41.7 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 78.6/78.6 | 21.4/21.4 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 93.3/80.0 | 6.7/20.0 | 0.0/0.0 |
| variant=none | 30/30 | 93.3/80.0 | 6.7/20.0 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/80.0 | 0.0/20.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/60.0 | 0.0/40.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/100.0 | 20.0/0.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.3 (n=158) / 93.4 (n=157)
- contested: 92.2 (n=122) / 92.4 (n=121)
- uncontested: 97.1 (n=36) / 96.8 (n=36)
