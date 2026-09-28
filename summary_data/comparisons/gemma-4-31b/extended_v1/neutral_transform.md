# Gemma-4-31B: neutral transform (ShareGPT) against the original, the extended set, version 1

original: <outputs>/gemma-4-31b/original/judged_extended_v1.jsonl

condition neutral_transform: <outputs>/gemma-4-31b/neutral_transform/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 95.9/94.6 | 3.8/4.4 | 1.9/2.2 | 0.0/0.0 | 0.3/0.9 | +0.6 [-1.3, +2.5] | +0.0 [+0.0, +0.0] | +0.6 [-1.3, +2.5] |
| settled | variant=belief_wrong | 158 | 158 | 93.0/90.5 | 6.3/7.6 | 2.5/1.9 | 0.0/0.0 | 0.6/1.9 | +1.3 [-2.5, +5.1] | +0.0 [+0.0, +0.0] | +1.3 [-2.5, +5.1] |
| settled | variant=confidence | 158 | 158 | 98.7/98.7 | 1.3/1.3 | 1.3/2.5 | 0.0/0.0 | 0.0/0.0 | +0.0 [-1.9, +1.9] | +0.0 [+0.0, +0.0] | +0.0 [-1.9, +1.9] |
| settled | contested | 244 | 244 | 95.5/93.4 | 4.1/5.3 | 2.0/2.5 | 0.0/0.0 | 0.4/1.2 | +1.2 [-1.2, +3.7] | +0.0 [+0.0, +0.0] | +1.2 [-1.2, +3.7] |
| settled | uncontested | 72 | 72 | 97.2/98.6 | 2.8/1.4 | 1.4/1.4 | 0.0/0.0 | 0.0/0.0 | -1.4 [-4.2, +0.0] | +0.0 [+0.0, +0.0] | -1.4 [-4.2, +0.0] |
| settled | left-coded | 78 | 78 | 94.9/89.7 | 5.1/10.3 | 3.8/3.8 | 0.0/0.0 | 0.0/0.0 | +5.1 [+0.0, +11.5] | +0.0 [+0.0, +0.0] | +5.1 [+0.0, +11.5] |
| settled | right-coded | 118 | 118 | 95.8/94.1 | 3.4/3.4 | 0.0/1.7 | 0.0/0.0 | 0.8/2.5 | +0.0 [-2.5, +2.5] | +0.0 [+0.0, +0.0] | +0.0 [-2.5, +2.5] |
| settled | uncoded | 120 | 120 | 96.7/98.3 | 3.3/1.7 | 2.5/1.7 | 0.0/0.0 | 0.0/0.0 | -1.7 [-4.2, +0.0] | +0.0 [+0.0, +0.0] | -1.7 [-4.2, +0.0] |

#### answer length, mean words, original / treated

- advice | all: 222 / 224
- advocacy | all: 128 / 128
- settled | all: 126 / 124
- settled | contested: 126 / 125
- settled | uncontested: 123 / 123
- settled | left-coded: 132 / 134
- settled | right-coded: 121 / 117
- settled | uncoded: 126 / 126

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 72.5/67.5 | 27.5/32.5 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 72.5/67.5 | 27.5/32.5 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 78.6/64.3 | 21.4/35.7 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 66.7/66.7 | 33.3/33.3 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 71.4/71.4 | 28.6/28.6 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 93.3/96.7 | 6.7/3.3 | 0.0/0.0 |
| variant=none | 30/30 | 93.3/96.7 | 6.7/3.3 | 0.0/0.0 |
| right-coded | 10/10 | 90.0/100.0 | 10.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 10/10 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 99.1 (n=158) / 99.0 (n=158)
- contested: 98.9 (n=122) / 98.7 (n=122)
- uncontested: 99.9 (n=36) / 99.9 (n=36)
