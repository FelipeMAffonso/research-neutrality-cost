# Llama-3.1-8B: assertive transform (ShareGPT) against the original, the extended set, version 1

original: <outputs>/llama-3.1-8b/original/judged_extended_v1.jsonl

condition assertive_transform: <outputs>/llama-3.1-8b/assertive_transform/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/2.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/2.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 75.0/73.7 | 16.8/14.6 | 2.8/1.3 | 8.2/11.7 | 0.0/0.0 | -2.2 [-7.0, +2.2] | +3.5 [+0.0, +7.3] | +1.3 [-3.5, +6.0] |
| settled | variant=belief_wrong | 158 | 158 | 70.3/70.3 | 19.6/12.0 | 3.2/1.3 | 10.1/17.7 | 0.0/0.0 | -7.6 [-13.9, -1.9] | +7.6 [+1.9, +13.3] | +0.0 [-7.6, +7.0] |
| settled | variant=confidence | 158 | 158 | 79.7/77.2 | 13.9/17.1 | 2.5/1.3 | 6.3/5.7 | 0.0/0.0 | +3.2 [-2.5, +9.5] | -0.6 [-5.1, +3.8] | +2.5 [-3.2, +8.2] |
| settled | contested | 244 | 244 | 68.0/68.0 | 21.3/18.9 | 3.3/1.6 | 10.7/13.1 | 0.0/0.0 | -2.5 [-8.2, +3.3] | +2.5 [-2.5, +7.0] | +0.0 [-5.7, +5.7] |
| settled | uncontested | 72 | 72 | 98.6/93.1 | 1.4/0.0 | 1.4/0.0 | 0.0/6.9 | 0.0/0.0 | -1.4 [-4.2, +0.0] | +6.9 [+1.4, +13.9] | +5.6 [+0.0, +12.5] |
| settled | left-coded | 78 | 78 | 41.0/41.0 | 39.7/32.1 | 6.4/5.1 | 19.2/26.9 | 0.0/0.0 | -7.7 [-20.5, +6.4] | +7.7 [-1.3, +16.7] | +0.0 [-12.8, +12.8] |
| settled | right-coded | 118 | 118 | 85.6/83.1 | 8.5/9.3 | 1.7/0.0 | 5.9/7.6 | 0.0/0.0 | +0.8 [-4.2, +5.9] | +1.7 [-4.2, +7.6] | +2.5 [-4.2, +9.3] |
| settled | uncoded | 120 | 120 | 86.7/85.8 | 10.0/8.3 | 1.7/0.0 | 3.3/5.8 | 0.0/0.0 | -1.7 [-8.3, +5.0] | +2.5 [-3.3, +8.3] | +0.8 [-5.8, +7.5] |

#### answer length, mean words, original / treated

- advice | all: 178 / 95
- advocacy | all: 118 / 80
- settled | all: 142 / 79
- settled | contested: 146 / 83
- settled | uncontested: 131 / 65
- settled | left-coded: 152 / 89
- settled | right-coded: 142 / 75
- settled | uncoded: 136 / 76

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 55.0/55.0 | 40.0/32.5 | 2.5/10.0 | 2.5/2.5 |
| variant=none | 40/40 | 55.0/55.0 | 40.0/32.5 | 2.5/10.0 | 2.5/2.5 |
| right-coded | 14/14 | 64.3/78.6 | 35.7/7.1 | 0.0/7.1 | 0.0/7.1 |
| left-coded | 12/12 | 33.3/25.0 | 66.7/58.3 | 0.0/16.7 | 0.0/0.0 |
| uncoded | 14/14 | 64.3/57.1 | 21.4/35.7 | 7.1/7.1 | 7.1/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 86.7/80.0 | 10.0/16.7 | 3.3/3.3 |
| variant=none | 30/30 | 86.7/80.0 | 10.0/16.7 | 3.3/3.3 |
| right-coded | 10/10 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/70.0 | 10.0/30.0 | 10.0/0.0 |
| uncoded | 10/10 | 80.0/80.0 | 20.0/10.0 | 0.0/10.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.0 (n=32) / 89.1 (n=14)
- contested: 91.6 (n=22) / 86.2 (n=11)
- uncontested: 99.4 (n=10) / 100.0 (n=3)
