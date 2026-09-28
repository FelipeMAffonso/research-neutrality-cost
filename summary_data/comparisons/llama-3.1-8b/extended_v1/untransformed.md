# Llama-3.1-8B: untransformed (ShareGPT) against the original, the extended set, version 1

original: <outputs>/llama-3.1-8b/original/judged_extended_v1.jsonl

condition untransformed: <outputs>/llama-3.1-8b/untransformed/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/2.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/2.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 75.0/73.4 | 16.8/15.8 | 2.8/2.5 | 8.2/10.8 | 0.0/0.0 | -0.9 [-4.7, +3.2] | +2.5 [-1.3, +6.3] | +1.6 [-2.5, +5.7] |
| settled | variant=belief_wrong | 158 | 158 | 70.3/71.5 | 19.6/15.8 | 3.2/1.9 | 10.1/12.7 | 0.0/0.0 | -3.8 [-9.5, +1.9] | +2.5 [-3.2, +8.9] | -1.3 [-8.2, +5.1] |
| settled | variant=confidence | 158 | 158 | 79.7/75.3 | 13.9/15.8 | 2.5/3.2 | 6.3/8.9 | 0.0/0.0 | +1.9 [-3.2, +7.0] | +2.5 [-1.9, +7.0] | +4.4 [-0.6, +10.1] |
| settled | contested | 244 | 244 | 68.0/67.2 | 21.3/20.5 | 3.3/2.5 | 10.7/12.3 | 0.0/0.0 | -0.8 [-5.7, +4.5] | +1.6 [-3.3, +6.6] | +0.8 [-4.1, +5.7] |
| settled | uncontested | 72 | 72 | 98.6/94.4 | 1.4/0.0 | 1.4/2.8 | 0.0/5.6 | 0.0/0.0 | -1.4 [-4.2, +0.0] | +5.6 [+1.4, +11.1] | +4.2 [-1.4, +9.7] |
| settled | left-coded | 78 | 78 | 41.0/39.7 | 39.7/37.2 | 6.4/3.8 | 19.2/23.1 | 0.0/0.0 | -2.6 [-12.8, +9.0] | +3.8 [-6.4, +14.1] | +1.3 [-9.0, +11.5] |
| settled | right-coded | 118 | 118 | 85.6/83.9 | 8.5/7.6 | 1.7/0.8 | 5.9/8.5 | 0.0/0.0 | -0.8 [-5.9, +4.2] | +2.5 [-2.5, +8.5] | +1.7 [-4.2, +8.5] |
| settled | uncoded | 120 | 120 | 86.7/85.0 | 10.0/10.0 | 1.7/3.3 | 3.3/5.0 | 0.0/0.0 | +0.0 [-5.8, +6.7] | +1.7 [-3.3, +6.7] | +1.7 [-4.2, +7.5] |

#### answer length, mean words, original / treated

- advice | all: 178 / 147
- advocacy | all: 118 / 88
- settled | all: 142 / 91
- settled | contested: 146 / 94
- settled | uncontested: 131 / 78
- settled | left-coded: 152 / 108
- settled | right-coded: 142 / 85
- settled | uncoded: 136 / 85

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 55.0/52.5 | 40.0/37.5 | 2.5/7.5 | 2.5/2.5 |
| variant=none | 40/40 | 55.0/52.5 | 40.0/37.5 | 2.5/7.5 | 2.5/2.5 |
| right-coded | 14/14 | 64.3/71.4 | 35.7/21.4 | 0.0/0.0 | 0.0/7.1 |
| left-coded | 12/12 | 33.3/16.7 | 66.7/75.0 | 0.0/8.3 | 0.0/0.0 |
| uncoded | 14/14 | 64.3/64.3 | 21.4/21.4 | 7.1/14.3 | 7.1/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 86.7/86.7 | 10.0/6.7 | 3.3/6.7 |
| variant=none | 30/30 | 86.7/86.7 | 10.0/6.7 | 3.3/6.7 |
| right-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/80.0 | 10.0/10.0 | 10.0/10.0 |
| uncoded | 10/10 | 80.0/80.0 | 20.0/10.0 | 0.0/10.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.0 (n=32) / 95.8 (n=24)
- contested: 91.6 (n=22) / 94.1 (n=16)
- uncontested: 99.4 (n=10) / 99.4 (n=8)
