# Qwen2.5-7B: assertive transform (ShareGPT) against the original, the extended set, version 2

original: <outputs>/qwen2.5-7b/original/judged_extended_v2.jsonl

condition assertive_transform: <outputs>/qwen2.5-7b/assertive_transform/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 89.2/84.8 | 8.9/10.8 | 3.2/8.2 | 1.9/4.4 | 0.0/0.0 | +1.9 [-1.9, +5.7] | +2.5 [+0.0, +5.4] | +4.4 [+0.3, +8.5] |
| settled | variant=belief_wrong | 158 | 158 | 84.2/82.9 | 14.6/12.0 | 5.1/13.3 | 1.3/5.1 | 0.0/0.0 | -2.5 [-8.9, +4.4] | +3.8 [+0.0, +7.6] | +1.3 [-5.7, +8.9] |
| settled | variant=confidence | 158 | 158 | 94.3/86.7 | 3.2/9.5 | 1.3/3.2 | 2.5/3.8 | 0.0/0.0 | +6.3 [+1.3, +11.4] | +1.3 [-1.9, +4.4] | +7.6 [+2.5, +13.3] |
| settled | contested | 244 | 244 | 86.5/81.1 | 11.1/13.9 | 3.7/9.0 | 2.5/4.9 | 0.0/0.0 | +2.9 [-2.0, +7.8] | +2.5 [-0.8, +5.7] | +5.3 [+0.0, +10.7] |
| settled | uncontested | 72 | 72 | 98.6/97.2 | 1.4/0.0 | 1.4/5.6 | 0.0/2.8 | 0.0/0.0 | -1.4 [-4.2, +0.0] | +2.8 [+0.0, +6.9] | +1.4 [+0.0, +4.2] |
| settled | left-coded | 52 | 52 | 78.8/73.1 | 17.3/21.2 | 9.6/17.3 | 3.8/5.8 | 0.0/0.0 | +3.8 [-9.6, +17.3] | +1.9 [-5.8, +11.5] | +5.8 [-7.7, +19.2] |
| settled | right-coded | 118 | 118 | 94.1/89.0 | 4.2/5.9 | 1.7/4.2 | 1.7/5.1 | 0.0/0.0 | +1.7 [-3.4, +7.6] | +3.4 [-0.8, +7.6] | +5.1 [-1.7, +12.7] |
| settled | uncoded | 146 | 146 | 89.0/85.6 | 9.6/11.0 | 2.1/8.2 | 1.4/3.4 | 0.0/0.0 | +1.4 [-3.4, +6.2] | +2.1 [-0.7, +5.5] | +3.4 [-1.4, +8.2] |

#### answer length, mean words, original / treated

- advice | all: 218 / 168
- advocacy | all: 80 / 70
- settled | all: 119 / 99
- settled | contested: 122 / 102
- settled | uncontested: 110 / 90
- settled | left-coded: 133 / 114
- settled | right-coded: 115 / 93
- settled | uncoded: 117 / 98

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 67.5/70.0 | 32.5/30.0 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 67.5/70.0 | 32.5/30.0 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 71.4/71.4 | 28.6/28.6 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 50.0/50.0 | 50.0/50.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 78.6/85.7 | 21.4/14.3 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| right-coded | 10/10 | 90.0/80.0 | 10.0/20.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/100.0 | 20.0/0.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.3 (n=158) / 93.8 (n=157)
- contested: 92.3 (n=122) / 93.3 (n=122)
- uncontested: 96.9 (n=36) / 95.5 (n=35)
