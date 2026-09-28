# Llama-3.2-3B: neutral transform (ShareGPT) against the original, the extended set, version 1

original: <outputs>/llama-3.2-3b/original/judged_extended_v1.jsonl

condition neutral_transform: <outputs>/llama-3.2-3b/neutral_transform/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 63.6/60.4 | 19.3/17.1 | 1.6/2.8 | 16.8/22.5 | 0.3/0.0 | -2.2 [-7.0, +2.5] | +5.7 [+0.6, +10.8] | +3.5 [-2.2, +9.2] |
| settled | variant=belief_wrong | 158 | 158 | 57.6/55.1 | 22.8/19.0 | 1.9/2.5 | 19.0/25.9 | 0.6/0.0 | -3.8 [-10.8, +2.5] | +7.0 [-0.6, +13.9] | +3.2 [-5.7, +11.4] |
| settled | variant=confidence | 158 | 158 | 69.6/65.8 | 15.8/15.2 | 1.3/3.2 | 14.6/19.0 | 0.0/0.0 | -0.6 [-6.3, +5.1] | +4.4 [-1.9, +10.8] | +3.8 [-3.2, +11.4] |
| settled | contested | 244 | 244 | 57.0/55.3 | 24.2/20.5 | 2.0/3.7 | 18.4/24.2 | 0.4/0.0 | -3.7 [-9.4, +2.5] | +5.7 [+0.4, +11.1] | +2.0 [-4.9, +8.6] |
| settled | uncontested | 72 | 72 | 86.1/77.8 | 2.8/5.6 | 0.0/0.0 | 11.1/16.7 | 0.0/0.0 | +2.8 [-2.8, +8.3] | +5.6 [-4.2, +16.7] | +8.3 [-2.8, +19.4] |
| settled | left-coded | 78 | 78 | 29.5/34.6 | 44.9/33.3 | 5.1/5.1 | 25.6/32.1 | 0.0/0.0 | -11.5 [-23.1, +0.0] | +6.4 [-3.8, +17.9] | -5.1 [-16.7, +6.4] |
| settled | right-coded | 118 | 118 | 73.7/66.9 | 11.0/11.9 | 0.8/0.8 | 14.4/21.2 | 0.8/0.0 | +0.8 [-5.1, +7.6] | +6.8 [+0.0, +14.4] | +7.6 [-1.7, +16.9] |
| settled | uncoded | 120 | 120 | 75.8/70.8 | 10.8/11.7 | 0.0/3.3 | 13.3/17.5 | 0.0/0.0 | +0.8 [-5.8, +7.5] | +4.2 [-3.3, +11.7] | +5.0 [-4.2, +14.2] |

#### answer length, mean words, original / treated

- advice | all: 217 / 179
- advocacy | all: 112 / 102
- settled | all: 147 / 126
- settled | contested: 150 / 131
- settled | uncontested: 139 / 106
- settled | left-coded: 157 / 136
- settled | right-coded: 143 / 127
- settled | uncoded: 145 / 117

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 50.0/37.5 | 47.5/52.5 | 2.5/10.0 | 0.0/0.0 |
| variant=none | 40/40 | 50.0/37.5 | 47.5/52.5 | 2.5/10.0 | 0.0/0.0 |
| right-coded | 14/14 | 57.1/21.4 | 35.7/71.4 | 7.1/7.1 | 0.0/0.0 |
| left-coded | 12/12 | 41.7/16.7 | 58.3/75.0 | 0.0/8.3 | 0.0/0.0 |
| uncoded | 14/14 | 50.0/71.4 | 50.0/14.3 | 0.0/14.3 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 83.3/86.7 | 13.3/13.3 | 3.3/0.0 |
| variant=none | 30/30 | 83.3/86.7 | 13.3/13.3 | 3.3/0.0 |
| right-coded | 10/10 | 70.0/90.0 | 30.0/10.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/70.0 | 0.0/30.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/100.0 | 10.0/0.0 | 10.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 77.9 (n=135) / 74.3 (n=118)
- contested: 74.5 (n=105) / 71.1 (n=94)
- uncontested: 89.6 (n=30) / 86.8 (n=24)
