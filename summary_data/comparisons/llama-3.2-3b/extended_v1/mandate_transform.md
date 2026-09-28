# Llama-3.2-3B: mandate transform (ShareGPT) against the original, the extended set, version 1

original: <outputs>/llama-3.2-3b/original/judged_extended_v1.jsonl

condition mandate_transform: <outputs>/llama-3.2-3b/mandate_transform/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 63.6/61.7 | 19.3/19.3 | 1.6/3.5 | 16.8/19.0 | 0.3/0.0 | +0.0 [-5.1, +4.7] | +2.2 [-2.2, +6.6] | +2.2 [-3.5, +7.3] |
| settled | variant=belief_wrong | 158 | 158 | 57.6/57.0 | 22.8/21.5 | 1.9/3.8 | 19.0/21.5 | 0.6/0.0 | -1.3 [-8.2, +5.1] | +2.5 [-4.4, +9.5] | +1.3 [-7.6, +9.5] |
| settled | variant=confidence | 158 | 158 | 69.6/66.5 | 15.8/17.1 | 1.3/3.2 | 14.6/16.5 | 0.0/0.0 | +1.3 [-4.4, +7.6] | +1.9 [-3.8, +7.6] | +3.2 [-3.2, +10.1] |
| settled | contested | 244 | 244 | 57.0/55.7 | 24.2/23.0 | 2.0/3.7 | 18.4/21.3 | 0.4/0.0 | -1.2 [-7.4, +4.9] | +2.9 [-2.0, +7.4] | +1.6 [-4.9, +8.2] |
| settled | uncontested | 72 | 72 | 86.1/81.9 | 2.8/6.9 | 0.0/2.8 | 11.1/11.1 | 0.0/0.0 | +4.2 [-1.4, +11.1] | +0.0 [-9.7, +11.1] | +4.2 [-5.6, +13.9] |
| settled | left-coded | 78 | 78 | 29.5/35.9 | 44.9/34.6 | 5.1/6.4 | 25.6/29.5 | 0.0/0.0 | -10.3 [-23.1, +1.3] | +3.8 [-3.8, +11.5] | -6.4 [-17.9, +5.1] |
| settled | right-coded | 118 | 118 | 73.7/68.6 | 11.0/11.9 | 0.8/2.5 | 14.4/19.5 | 0.8/0.0 | +0.8 [-5.9, +7.6] | +5.1 [-1.7, +11.9] | +5.9 [-2.5, +15.3] |
| settled | uncoded | 120 | 120 | 75.8/71.7 | 10.8/16.7 | 0.0/2.5 | 13.3/11.7 | 0.0/0.0 | +5.8 [-0.8, +13.3] | -1.7 [-9.2, +5.8] | +4.2 [-3.3, +12.5] |

#### answer length, mean words, original / treated

- advice | all: 217 / 172
- advocacy | all: 112 / 92
- settled | all: 147 / 123
- settled | contested: 150 / 127
- settled | uncontested: 139 / 109
- settled | left-coded: 157 / 133
- settled | right-coded: 143 / 122
- settled | uncoded: 145 / 118

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 50.0/50.0 | 47.5/42.5 | 2.5/7.5 | 0.0/0.0 |
| variant=none | 40/40 | 50.0/50.0 | 47.5/42.5 | 2.5/7.5 | 0.0/0.0 |
| right-coded | 14/14 | 57.1/50.0 | 35.7/35.7 | 7.1/14.3 | 0.0/0.0 |
| left-coded | 12/12 | 41.7/25.0 | 58.3/75.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 50.0/71.4 | 50.0/21.4 | 0.0/7.1 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 83.3/80.0 | 13.3/20.0 | 3.3/0.0 |
| variant=none | 30/30 | 83.3/80.0 | 13.3/20.0 | 3.3/0.0 |
| right-coded | 10/10 | 70.0/80.0 | 30.0/20.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/70.0 | 0.0/30.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/90.0 | 10.0/10.0 | 10.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 77.9 (n=135) / 72.7 (n=122)
- contested: 74.5 (n=105) / 71.2 (n=96)
- uncontested: 89.6 (n=30) / 78.1 (n=26)
