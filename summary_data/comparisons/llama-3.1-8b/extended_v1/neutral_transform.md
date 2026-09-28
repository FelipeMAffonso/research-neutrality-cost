# Llama-3.1-8B: neutral transform (ShareGPT) against the original, the extended set, version 1

original: <outputs>/llama-3.1-8b/original/judged_extended_v1.jsonl

condition neutral_transform: <outputs>/llama-3.1-8b/neutral_transform/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 75.0/69.9 | 16.8/17.7 | 2.8/0.6 | 8.2/12.3 | 0.0/0.0 | +0.9 [-3.2, +5.1] | +4.1 [+0.0, +8.2] | +5.1 [+0.6, +9.8] |
| settled | variant=belief_wrong | 158 | 158 | 70.3/66.5 | 19.6/17.1 | 3.2/0.0 | 10.1/16.5 | 0.0/0.0 | -2.5 [-8.2, +2.5] | +6.3 [+0.0, +13.3] | +3.8 [-3.2, +10.8] |
| settled | variant=confidence | 158 | 158 | 79.7/73.4 | 13.9/18.4 | 2.5/1.3 | 6.3/8.2 | 0.0/0.0 | +4.4 [-1.3, +10.8] | +1.9 [-3.2, +6.3] | +6.3 [+0.0, +13.3] |
| settled | contested | 244 | 244 | 68.0/61.9 | 21.3/23.0 | 3.3/0.8 | 10.7/15.2 | 0.0/0.0 | +1.6 [-4.1, +7.4] | +4.5 [-1.2, +9.8] | +6.1 [+0.4, +12.3] |
| settled | uncontested | 72 | 72 | 98.6/97.2 | 1.4/0.0 | 1.4/0.0 | 0.0/2.8 | 0.0/0.0 | -1.4 [-4.2, +0.0] | +2.8 [+0.0, +6.9] | +1.4 [-2.8, +6.9] |
| settled | left-coded | 78 | 78 | 41.0/34.6 | 39.7/39.7 | 6.4/1.3 | 19.2/25.6 | 0.0/0.0 | +0.0 [-12.8, +12.8] | +6.4 [-5.1, +17.9] | +6.4 [-5.1, +19.2] |
| settled | right-coded | 118 | 118 | 85.6/78.8 | 8.5/9.3 | 1.7/0.0 | 5.9/11.9 | 0.0/0.0 | +0.8 [-3.4, +5.1] | +5.9 [+0.0, +12.7] | +6.8 [+0.0, +14.4] |
| settled | uncoded | 120 | 120 | 86.7/84.2 | 10.0/11.7 | 1.7/0.8 | 3.3/4.2 | 0.0/0.0 | +1.7 [-4.2, +8.3] | +0.8 [-4.2, +5.8] | +2.5 [-4.2, +8.3] |

#### answer length, mean words, original / treated

- advice | all: 178 / 132
- advocacy | all: 118 / 78
- settled | all: 142 / 79
- settled | contested: 146 / 83
- settled | uncontested: 131 / 67
- settled | left-coded: 152 / 94
- settled | right-coded: 142 / 76
- settled | uncoded: 136 / 73

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 55.0/50.0 | 40.0/47.5 | 2.5/2.5 | 2.5/0.0 |
| variant=none | 40/40 | 55.0/50.0 | 40.0/47.5 | 2.5/2.5 | 2.5/0.0 |
| right-coded | 14/14 | 64.3/71.4 | 35.7/28.6 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 33.3/25.0 | 66.7/66.7 | 0.0/8.3 | 0.0/0.0 |
| uncoded | 14/14 | 64.3/50.0 | 21.4/50.0 | 7.1/0.0 | 7.1/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 86.7/76.7 | 10.0/20.0 | 3.3/3.3 |
| variant=none | 30/30 | 86.7/76.7 | 10.0/20.0 | 3.3/3.3 |
| right-coded | 10/10 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/70.0 | 10.0/30.0 | 10.0/0.0 |
| uncoded | 10/10 | 80.0/70.0 | 20.0/20.0 | 0.0/10.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.0 (n=32) / 90.2 (n=12)
- contested: 91.6 (n=22) / 90.2 (n=12)
- uncontested: 99.4 (n=10) / nan (n=0)
