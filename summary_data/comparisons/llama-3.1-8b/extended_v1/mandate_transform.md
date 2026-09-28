# Llama-3.1-8B: mandate transform (ShareGPT) against the original, the extended set, version 1

original: <outputs>/llama-3.1-8b/original/judged_extended_v1.jsonl

condition mandate_transform: <outputs>/llama-3.1-8b/mandate_transform/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/2.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/2.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 75.0/71.8 | 16.8/14.9 | 2.8/1.9 | 8.2/13.3 | 0.0/0.0 | -1.9 [-6.0, +2.2] | +5.1 [+0.9, +9.5] | +3.2 [-1.6, +7.9] |
| settled | variant=belief_wrong | 158 | 158 | 70.3/67.7 | 19.6/14.6 | 3.2/1.9 | 10.1/17.7 | 0.0/0.0 | -5.1 [-10.8, +0.6] | +7.6 [+1.3, +13.9] | +2.5 [-5.7, +10.1] |
| settled | variant=confidence | 158 | 158 | 79.7/75.9 | 13.9/15.2 | 2.5/1.9 | 6.3/8.9 | 0.0/0.0 | +1.3 [-4.4, +7.0] | +2.5 [-1.9, +7.0] | +3.8 [-1.9, +9.5] |
| settled | contested | 244 | 244 | 68.0/64.8 | 21.3/19.3 | 3.3/2.0 | 10.7/16.0 | 0.0/0.0 | -2.0 [-7.4, +3.3] | +5.3 [+0.0, +10.7] | +3.3 [-2.9, +9.4] |
| settled | uncontested | 72 | 72 | 98.6/95.8 | 1.4/0.0 | 1.4/1.4 | 0.0/4.2 | 0.0/0.0 | -1.4 [-4.2, +0.0] | +4.2 [+0.0, +9.7] | +2.8 [-2.8, +8.3] |
| settled | left-coded | 78 | 78 | 41.0/35.9 | 39.7/35.9 | 6.4/2.6 | 19.2/28.2 | 0.0/0.0 | -3.8 [-16.7, +10.3] | +9.0 [-2.6, +20.5] | +5.1 [-6.4, +16.7] |
| settled | right-coded | 118 | 118 | 85.6/82.2 | 8.5/7.6 | 1.7/0.8 | 5.9/10.2 | 0.0/0.0 | -0.8 [-5.1, +3.4] | +4.2 [-1.7, +10.2] | +3.4 [-3.4, +10.2] |
| settled | uncoded | 120 | 120 | 86.7/85.0 | 10.0/8.3 | 1.7/2.5 | 3.3/6.7 | 0.0/0.0 | -1.7 [-6.7, +4.2] | +3.3 [-2.5, +9.2] | +1.7 [-5.0, +8.3] |

#### answer length, mean words, original / treated

- advice | all: 178 / 122
- advocacy | all: 118 / 78
- settled | all: 142 / 71
- settled | contested: 146 / 74
- settled | uncontested: 131 / 61
- settled | left-coded: 152 / 81
- settled | right-coded: 142 / 69
- settled | uncoded: 136 / 66

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 55.0/55.0 | 40.0/35.0 | 2.5/7.5 | 2.5/2.5 |
| variant=none | 40/40 | 55.0/55.0 | 40.0/35.0 | 2.5/7.5 | 2.5/2.5 |
| right-coded | 14/14 | 64.3/85.7 | 35.7/0.0 | 0.0/7.1 | 0.0/7.1 |
| left-coded | 12/12 | 33.3/33.3 | 66.7/58.3 | 0.0/8.3 | 0.0/0.0 |
| uncoded | 14/14 | 64.3/42.9 | 21.4/50.0 | 7.1/7.1 | 7.1/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 86.7/76.7 | 10.0/20.0 | 3.3/3.3 |
| variant=none | 30/30 | 86.7/76.7 | 10.0/20.0 | 3.3/3.3 |
| right-coded | 10/10 | 100.0/80.0 | 0.0/20.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/80.0 | 10.0/20.0 | 10.0/0.0 |
| uncoded | 10/10 | 80.0/70.0 | 20.0/20.0 | 0.0/10.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.0 (n=32) / 92.8 (n=14)
- contested: 91.6 (n=22) / 91.3 (n=11)
- uncontested: 99.4 (n=10) / 98.3 (n=3)
