# Qwen2.5-7B: mandate transform (ShareGPT) against the original, the extended set, version 2

original: <outputs>/qwen2.5-7b/original/judged_extended_v2.jsonl

condition mandate_transform: <outputs>/qwen2.5-7b/mandate_transform/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 89.2/88.3 | 8.9/8.2 | 3.2/7.0 | 1.9/3.5 | 0.0/0.0 | -0.6 [-4.4, +3.2] | +1.6 [-0.6, +4.1] | +0.9 [-3.2, +4.7] |
| settled | variant=belief_wrong | 158 | 158 | 84.2/89.2 | 14.6/7.6 | 5.1/11.4 | 1.3/3.2 | 0.0/0.0 | -7.0 [-13.3, -0.6] | +1.9 [-1.3, +5.1] | -5.1 [-11.4, +1.3] |
| settled | variant=confidence | 158 | 158 | 94.3/87.3 | 3.2/8.9 | 1.3/2.5 | 2.5/3.8 | 0.0/0.0 | +5.7 [+1.3, +10.8] | +1.3 [-1.9, +4.4] | +7.0 [+1.9, +12.7] |
| settled | contested | 244 | 244 | 86.5/85.7 | 11.1/9.8 | 3.7/7.4 | 2.5/4.5 | 0.0/0.0 | -1.2 [-6.1, +3.7] | +2.0 [-0.8, +5.3] | +0.8 [-4.1, +5.7] |
| settled | uncontested | 72 | 72 | 98.6/97.2 | 1.4/2.8 | 1.4/5.6 | 0.0/0.0 | 0.0/0.0 | +1.4 [-2.8, +5.6] | +0.0 [+0.0, +0.0] | +1.4 [-2.8, +5.6] |
| settled | left-coded | 52 | 52 | 78.8/75.0 | 17.3/21.2 | 9.6/11.5 | 3.8/3.8 | 0.0/0.0 | +3.8 [-9.6, +17.3] | +0.0 [-5.8, +5.8] | +3.8 [-9.6, +15.4] |
| settled | right-coded | 118 | 118 | 94.1/91.5 | 4.2/4.2 | 1.7/5.1 | 1.7/4.2 | 0.0/0.0 | +0.0 [-5.1, +5.1] | +2.5 [-1.7, +6.8] | +2.5 [-3.4, +9.3] |
| settled | uncoded | 146 | 146 | 89.0/90.4 | 9.6/6.8 | 2.1/6.8 | 1.4/2.7 | 0.0/0.0 | -2.7 [-8.2, +2.7] | +1.4 [-1.4, +5.5] | -1.4 [-6.2, +3.4] |

#### answer length, mean words, original / treated

- advice | all: 218 / 169
- advocacy | all: 80 / 71
- settled | all: 119 / 99
- settled | contested: 122 / 102
- settled | uncontested: 110 / 89
- settled | left-coded: 133 / 108
- settled | right-coded: 115 / 99
- settled | uncoded: 117 / 97

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 67.5/67.5 | 32.5/32.5 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 67.5/67.5 | 32.5/32.5 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 71.4/64.3 | 28.6/35.7 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 50.0/50.0 | 50.0/50.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 78.6/85.7 | 21.4/14.3 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| right-coded | 10/10 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/80.0 | 0.0/20.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/100.0 | 20.0/0.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.3 (n=158) / 93.2 (n=158)
- contested: 92.3 (n=122) / 92.2 (n=122)
- uncontested: 96.9 (n=36) / 96.6 (n=36)
