# Llama-3.1-8B: mandate transform (ShareGPT) against the original, the extended set, version 2

original: <outputs>/llama-3.1-8b/original/judged_extended_v2.jsonl

condition mandate_transform: <outputs>/llama-3.1-8b/mandate_transform/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/2.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/2.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 76.6/73.1 | 16.5/12.3 | 1.6/2.5 | 7.0/14.6 | 0.0/0.0 | -4.1 [-8.2, -0.3] | +7.6 [+4.1, +11.4] | +3.5 [-0.9, +7.6] |
| settled | variant=belief_wrong | 158 | 158 | 71.5/68.4 | 20.9/12.0 | 0.6/0.6 | 7.6/19.6 | 0.0/0.0 | -8.9 [-15.2, -2.5] | +12.0 [+7.0, +17.7] | +3.2 [-3.8, +10.8] |
| settled | variant=confidence | 158 | 158 | 81.6/77.8 | 12.0/12.7 | 2.5/4.4 | 6.3/9.5 | 0.0/0.0 | +0.6 [-3.8, +5.7] | +3.2 [-1.3, +7.6] | +3.8 [-1.9, +9.5] |
| settled | contested | 244 | 244 | 70.1/67.2 | 21.3/16.0 | 1.6/2.5 | 8.6/16.8 | 0.0/0.0 | -5.3 [-10.2, +0.0] | +8.2 [+3.7, +12.7] | +2.9 [-2.5, +8.2] |
| settled | uncontested | 72 | 72 | 98.6/93.1 | 0.0/0.0 | 1.4/2.8 | 1.4/6.9 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +5.6 [+1.4, +11.1] | +5.6 [+1.4, +11.1] |
| settled | left-coded | 52 | 52 | 46.2/50.0 | 38.5/25.0 | 3.8/5.8 | 15.4/25.0 | 0.0/0.0 | -13.5 [-26.9, +0.0] | +9.6 [-1.9, +23.1] | -3.8 [-15.4, +9.6] |
| settled | right-coded | 118 | 118 | 84.7/82.2 | 11.0/7.6 | 0.8/1.7 | 4.2/10.2 | 0.0/0.0 | -3.4 [-8.5, +1.7] | +5.9 [+0.8, +11.9] | +2.5 [-4.2, +10.2] |
| settled | uncoded | 146 | 146 | 80.8/74.0 | 13.0/11.6 | 1.4/2.1 | 6.2/14.4 | 0.0/0.0 | -1.4 [-6.2, +3.4] | +8.2 [+3.4, +13.0] | +6.8 [+1.4, +12.3] |

#### answer length, mean words, original / treated

- advice | all: 180 / 119
- advocacy | all: 117 / 73
- settled | all: 143 / 69
- settled | contested: 145 / 70
- settled | uncontested: 134 / 67
- settled | left-coded: 152 / 74
- settled | right-coded: 140 / 63
- settled | uncoded: 141 / 72

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 42.5/55.0 | 50.0/35.0 | 5.0/7.5 | 2.5/2.5 |
| variant=none | 40/40 | 42.5/55.0 | 50.0/35.0 | 5.0/7.5 | 2.5/2.5 |
| right-coded | 14/14 | 50.0/85.7 | 50.0/0.0 | 0.0/7.1 | 0.0/7.1 |
| left-coded | 12/12 | 25.0/33.3 | 75.0/66.7 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 50.0/42.9 | 28.6/42.9 | 14.3/14.3 | 7.1/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 83.3/76.7 | 13.3/20.0 | 3.3/3.3 |
| variant=none | 30/30 | 83.3/76.7 | 13.3/20.0 | 3.3/3.3 |
| right-coded | 10/10 | 100.0/80.0 | 0.0/20.0 | 0.0/0.0 |
| left-coded | 10/10 | 70.0/80.0 | 20.0/20.0 | 10.0/0.0 |
| uncoded | 10/10 | 80.0/70.0 | 20.0/20.0 | 0.0/10.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.5 (n=32) / 92.2 (n=13)
- contested: 92.3 (n=22) / 89.3 (n=9)
- uncontested: 99.4 (n=10) / 98.8 (n=4)
