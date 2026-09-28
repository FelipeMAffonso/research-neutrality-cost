# Gemma-4-31B: untransformed (ShareGPT) against the original, the extended set, version 1

original: <outputs>/gemma-4-31b/original/judged_extended_v1.jsonl

condition untransformed: <outputs>/gemma-4-31b/untransformed/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 95.9/95.6 | 3.8/3.2 | 1.9/1.6 | 0.0/0.9 | 0.3/0.3 | -0.6 [-2.5, +0.9] | +0.9 [+0.0, +2.2] | +0.3 [-1.6, +2.2] |
| settled | variant=belief_wrong | 158 | 158 | 93.0/93.7 | 6.3/4.4 | 2.5/0.6 | 0.0/1.3 | 0.6/0.6 | -1.9 [-5.1, +0.6] | +1.3 [+0.0, +3.2] | -0.6 [-3.8, +1.9] |
| settled | variant=confidence | 158 | 158 | 98.7/97.5 | 1.3/1.9 | 1.3/2.5 | 0.0/0.6 | 0.0/0.0 | +0.6 [-1.3, +2.5] | +0.6 [+0.0, +1.9] | +1.3 [-1.3, +3.8] |
| settled | contested | 244 | 244 | 95.5/94.7 | 4.1/3.7 | 2.0/1.6 | 0.0/1.2 | 0.4/0.4 | -0.4 [-2.9, +1.6] | +1.2 [+0.0, +2.9] | +0.8 [-1.6, +3.3] |
| settled | uncontested | 72 | 72 | 97.2/98.6 | 2.8/1.4 | 1.4/1.4 | 0.0/0.0 | 0.0/0.0 | -1.4 [-4.2, +0.0] | +0.0 [+0.0, +0.0] | -1.4 [-4.2, +0.0] |
| settled | left-coded | 78 | 78 | 94.9/93.6 | 5.1/6.4 | 3.8/5.1 | 0.0/0.0 | 0.0/0.0 | +1.3 [-2.6, +5.1] | +0.0 [+0.0, +0.0] | +1.3 [-2.6, +5.1] |
| settled | right-coded | 118 | 118 | 95.8/94.9 | 3.4/2.5 | 0.0/0.0 | 0.0/1.7 | 0.8/0.8 | -0.8 [-3.4, +1.7] | +1.7 [+0.0, +4.2] | +0.8 [-1.7, +4.2] |
| settled | uncoded | 120 | 120 | 96.7/97.5 | 3.3/1.7 | 2.5/0.8 | 0.0/0.8 | 0.0/0.0 | -1.7 [-4.2, +0.0] | +0.8 [+0.0, +2.5] | -0.8 [-4.2, +1.7] |

#### answer length, mean words, original / treated

- advice | all: 222 / 223
- advocacy | all: 128 / 127
- settled | all: 126 / 125
- settled | contested: 126 / 125
- settled | uncontested: 123 / 123
- settled | left-coded: 132 / 135
- settled | right-coded: 121 / 118
- settled | uncoded: 126 / 125

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 72.5/72.5 | 27.5/27.5 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 72.5/72.5 | 27.5/27.5 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 78.6/78.6 | 21.4/21.4 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 66.7/75.0 | 33.3/25.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 71.4/64.3 | 28.6/35.7 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 93.3/96.7 | 6.7/3.3 | 0.0/0.0 |
| variant=none | 30/30 | 93.3/96.7 | 6.7/3.3 | 0.0/0.0 |
| right-coded | 10/10 | 90.0/100.0 | 10.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 10/10 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 99.1 (n=158) / 99.1 (n=158)
- contested: 98.9 (n=122) / 98.9 (n=122)
- uncontested: 99.9 (n=36) / 99.9 (n=36)
