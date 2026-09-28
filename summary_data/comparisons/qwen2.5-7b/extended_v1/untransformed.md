# Qwen2.5-7B: untransformed (ShareGPT) against the original, the extended set, version 1

original: <outputs>/qwen2.5-7b/original/judged_extended_v1.jsonl

condition untransformed: <outputs>/qwen2.5-7b/untransformed/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 89.2/86.4 | 8.9/8.2 | 3.2/5.4 | 1.9/5.4 | 0.0/0.0 | -0.6 [-4.4, +2.8] | +3.5 [+1.3, +6.0] | +2.8 [-1.3, +7.0] |
| settled | variant=belief_wrong | 158 | 158 | 86.7/82.3 | 13.3/10.8 | 5.1/6.3 | 0.0/7.0 | 0.0/0.0 | -2.5 [-8.2, +3.2] | +7.0 [+3.2, +11.4] | +4.4 [-2.5, +10.8] |
| settled | variant=confidence | 158 | 158 | 91.8/90.5 | 4.4/5.7 | 1.3/4.4 | 3.8/3.8 | 0.0/0.0 | +1.3 [-3.2, +5.7] | +0.0 [-3.2, +3.2] | +1.3 [-4.4, +7.0] |
| settled | contested | 244 | 244 | 86.5/84.4 | 11.1/10.2 | 3.3/6.1 | 2.5/5.3 | 0.0/0.0 | -0.8 [-5.7, +3.7] | +2.9 [+0.4, +5.7] | +2.0 [-3.3, +7.4] |
| settled | uncontested | 72 | 72 | 98.6/93.1 | 1.4/1.4 | 2.8/2.8 | 0.0/5.6 | 0.0/0.0 | +0.0 [-4.2, +4.2] | +5.6 [+1.4, +11.1] | +5.6 [+1.4, +11.1] |
| settled | left-coded | 78 | 78 | 73.1/71.8 | 23.1/23.1 | 9.0/12.8 | 3.8/5.1 | 0.0/0.0 | +0.0 [-11.5, +10.3] | +1.3 [-2.6, +5.1] | +1.3 [-10.3, +11.5] |
| settled | right-coded | 118 | 118 | 96.6/94.1 | 1.7/2.5 | 0.0/2.5 | 1.7/3.4 | 0.0/0.0 | +0.8 [-2.5, +4.2] | +1.7 [-1.7, +5.1] | +2.5 [-2.5, +7.6] |
| settled | uncoded | 120 | 120 | 92.5/88.3 | 6.7/4.2 | 2.5/3.3 | 0.8/7.5 | 0.0/0.0 | -2.5 [-8.3, +2.5] | +6.7 [+2.5, +11.7] | +4.2 [-2.5, +10.8] |

#### answer length, mean words, original / treated

- advice | all: 217 / 179
- advocacy | all: 79 / 84
- settled | all: 119 / 107
- settled | contested: 123 / 112
- settled | uncontested: 105 / 91
- settled | left-coded: 133 / 117
- settled | right-coded: 115 / 109
- settled | uncoded: 114 / 99

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 65.0/70.0 | 35.0/30.0 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 65.0/70.0 | 35.0/30.0 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 71.4/85.7 | 28.6/14.3 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 41.7/50.0 | 58.3/50.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 78.6/71.4 | 21.4/28.6 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 93.3/90.0 | 6.7/10.0 | 0.0/0.0 |
| variant=none | 30/30 | 93.3/90.0 | 6.7/10.0 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/80.0 | 0.0/20.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/100.0 | 20.0/0.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.3 (n=158) / 93.2 (n=158)
- contested: 92.2 (n=122) / 92.4 (n=122)
- uncontested: 97.1 (n=36) / 96.2 (n=36)
