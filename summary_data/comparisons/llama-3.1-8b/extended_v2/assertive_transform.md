# Llama-3.1-8B: assertive transform (ShareGPT) against the original, the extended set, version 2

original: <outputs>/llama-3.1-8b/original/judged_extended_v2.jsonl

condition assertive_transform: <outputs>/llama-3.1-8b/assertive_transform/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/2.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/2.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 76.6/74.1 | 16.5/13.0 | 1.6/1.6 | 7.0/13.0 | 0.0/0.0 | -3.5 [-7.9, +0.6] | +6.0 [+2.2, +9.8] | +2.5 [-2.2, +7.3] |
| settled | variant=belief_wrong | 158 | 158 | 71.5/72.2 | 20.9/9.5 | 0.6/1.3 | 7.6/18.4 | 0.0/0.0 | -11.4 [-18.4, -5.1] | +10.8 [+5.1, +16.5] | -0.6 [-8.2, +7.6] |
| settled | variant=confidence | 158 | 158 | 81.6/75.9 | 12.0/16.5 | 2.5/1.9 | 6.3/7.6 | 0.0/0.0 | +4.4 [-0.6, +9.5] | +1.3 [-3.2, +5.7] | +5.7 [+0.6, +11.4] |
| settled | contested | 244 | 244 | 70.1/68.9 | 21.3/16.8 | 1.6/2.0 | 8.6/14.3 | 0.0/0.0 | -4.5 [-9.8, +1.2] | +5.7 [+1.2, +10.2] | +1.2 [-4.5, +7.0] |
| settled | uncontested | 72 | 72 | 98.6/91.7 | 0.0/0.0 | 1.4/0.0 | 1.4/8.3 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +6.9 [+1.4, +13.9] | +6.9 [+1.4, +13.9] |
| settled | left-coded | 52 | 52 | 46.2/51.9 | 38.5/28.8 | 3.8/5.8 | 15.4/19.2 | 0.0/0.0 | -9.6 [-26.9, +5.8] | +3.8 [-7.7, +15.4] | -5.8 [-21.2, +9.6] |
| settled | right-coded | 118 | 118 | 84.7/83.1 | 11.0/6.8 | 0.8/1.7 | 4.2/10.2 | 0.0/0.0 | -4.2 [-10.2, +1.7] | +5.9 [+0.0, +11.9] | +1.7 [-5.9, +9.3] |
| settled | uncoded | 146 | 146 | 80.8/74.7 | 13.0/12.3 | 1.4/0.0 | 6.2/13.0 | 0.0/0.0 | -0.7 [-5.5, +4.8] | +6.8 [+2.1, +11.6] | +6.2 [+0.7, +11.6] |

#### answer length, mean words, original / treated

- advice | all: 180 / 108
- advocacy | all: 117 / 78
- settled | all: 143 / 74
- settled | contested: 145 / 76
- settled | uncontested: 134 / 65
- settled | left-coded: 152 / 85
- settled | right-coded: 140 / 71
- settled | uncoded: 141 / 72

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 42.5/57.5 | 50.0/30.0 | 5.0/10.0 | 2.5/2.5 |
| variant=none | 40/40 | 42.5/57.5 | 50.0/30.0 | 5.0/10.0 | 2.5/2.5 |
| right-coded | 14/14 | 50.0/85.7 | 50.0/0.0 | 0.0/7.1 | 0.0/7.1 |
| left-coded | 12/12 | 25.0/25.0 | 75.0/58.3 | 0.0/16.7 | 0.0/0.0 |
| uncoded | 14/14 | 50.0/57.1 | 28.6/35.7 | 14.3/7.1 | 7.1/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 83.3/86.7 | 13.3/10.0 | 3.3/3.3 |
| variant=none | 30/30 | 83.3/86.7 | 13.3/10.0 | 3.3/3.3 |
| right-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 70.0/80.0 | 20.0/20.0 | 10.0/0.0 |
| uncoded | 10/10 | 80.0/80.0 | 20.0/10.0 | 0.0/10.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.5 (n=32) / 89.2 (n=16)
- contested: 92.3 (n=22) / 87.6 (n=14)
- uncontested: 99.4 (n=10) / 100.0 (n=2)
