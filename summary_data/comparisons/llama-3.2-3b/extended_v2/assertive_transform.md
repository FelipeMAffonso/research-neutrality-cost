# Llama-3.2-3B: assertive transform (ShareGPT) against the original, the extended set, version 2

original: <outputs>/llama-3.2-3b/original/judged_extended_v2.jsonl

condition assertive_transform: <outputs>/llama-3.2-3b/assertive_transform/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 63.3/64.2 | 19.3/15.8 | 1.3/2.5 | 17.1/19.9 | 0.3/0.0 | -3.5 [-8.2, +0.9] | +2.8 [-2.2, +7.9] | -0.6 [-6.3, +5.1] |
| settled | variant=belief_wrong | 158 | 158 | 55.1/60.8 | 24.7/18.4 | 1.9/1.9 | 19.6/20.9 | 0.6/0.0 | -6.3 [-13.3, +0.6] | +1.3 [-6.3, +8.9] | -5.1 [-13.3, +3.2] |
| settled | variant=confidence | 158 | 158 | 71.5/67.7 | 13.9/13.3 | 0.6/3.2 | 14.6/19.0 | 0.0/0.0 | -0.6 [-6.3, +5.1] | +4.4 [-0.6, +10.1] | +3.8 [-3.2, +10.1] |
| settled | contested | 244 | 244 | 56.1/58.2 | 24.2/19.3 | 1.6/3.3 | 19.3/22.5 | 0.4/0.0 | -4.9 [-10.2, +0.8] | +3.3 [-2.9, +9.0] | -1.6 [-8.2, +4.9] |
| settled | uncontested | 72 | 72 | 87.5/84.7 | 2.8/4.2 | 0.0/0.0 | 9.7/11.1 | 0.0/0.0 | +1.4 [-2.8, +5.6] | +1.4 [-8.3, +12.5] | +2.8 [-8.3, +13.9] |
| settled | left-coded | 52 | 52 | 34.6/44.2 | 46.2/32.7 | 3.8/7.7 | 19.2/23.1 | 0.0/0.0 | -13.5 [-26.9, +0.0] | +3.8 [-7.7, +15.4] | -9.6 [-23.1, +1.9] |
| settled | right-coded | 118 | 118 | 71.2/70.3 | 11.0/12.7 | 0.8/1.7 | 16.9/16.9 | 0.8/0.0 | +1.7 [-5.1, +9.3] | +0.0 [-8.5, +9.3] | +1.7 [-8.5, +12.7] |
| settled | uncoded | 146 | 146 | 67.1/66.4 | 16.4/12.3 | 0.7/1.4 | 16.4/21.2 | 0.0/0.0 | -4.1 [-10.3, +2.1] | +4.8 [-2.7, +12.3] | +0.7 [-6.8, +8.2] |

#### answer length, mean words, original / treated

- advice | all: 217 / 177
- advocacy | all: 112 / 96
- settled | all: 147 / 126
- settled | contested: 150 / 130
- settled | uncontested: 139 / 113
- settled | left-coded: 157 / 139
- settled | right-coded: 143 / 123
- settled | uncoded: 148 / 123

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 50.0/35.0 | 47.5/55.0 | 2.5/10.0 | 0.0/0.0 |
| variant=none | 40/40 | 50.0/35.0 | 47.5/55.0 | 2.5/10.0 | 0.0/0.0 |
| right-coded | 14/14 | 50.0/28.6 | 42.9/57.1 | 7.1/14.3 | 0.0/0.0 |
| left-coded | 12/12 | 50.0/16.7 | 50.0/66.7 | 0.0/16.7 | 0.0/0.0 |
| uncoded | 14/14 | 50.0/57.1 | 50.0/42.9 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 83.3/80.0 | 13.3/20.0 | 3.3/0.0 |
| variant=none | 30/30 | 83.3/80.0 | 13.3/20.0 | 3.3/0.0 |
| right-coded | 10/10 | 70.0/70.0 | 30.0/30.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/70.0 | 0.0/30.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/100.0 | 10.0/0.0 | 10.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 77.7 (n=134) / 74.5 (n=119)
- contested: 74.4 (n=104) / 70.9 (n=96)
- uncontested: 89.2 (n=30) / 89.7 (n=23)
