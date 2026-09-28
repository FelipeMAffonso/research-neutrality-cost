# Llama-3.2-3B: neutral transform (ShareGPT) against the original, the extended set, version 2

original: <outputs>/llama-3.2-3b/original/judged_extended_v2.jsonl

condition neutral_transform: <outputs>/llama-3.2-3b/neutral_transform/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 63.3/60.4 | 19.3/17.1 | 1.3/2.2 | 17.1/22.5 | 0.3/0.0 | -2.2 [-7.0, +2.8] | +5.4 [+0.3, +10.4] | +3.2 [-2.5, +8.9] |
| settled | variant=belief_wrong | 158 | 158 | 55.1/52.5 | 24.7/20.3 | 1.9/1.9 | 19.6/27.2 | 0.6/0.0 | -4.4 [-12.0, +3.2] | +7.6 [-0.6, +16.5] | +3.2 [-6.3, +12.0] |
| settled | variant=confidence | 158 | 158 | 71.5/68.4 | 13.9/13.9 | 0.6/2.5 | 14.6/17.7 | 0.0/0.0 | +0.0 [-5.7, +5.7] | +3.2 [-2.5, +8.9] | +3.2 [-3.8, +10.1] |
| settled | contested | 244 | 244 | 56.1/54.5 | 24.2/20.9 | 1.6/2.9 | 19.3/24.6 | 0.4/0.0 | -3.3 [-9.4, +2.9] | +5.3 [-0.4, +11.1] | +2.0 [-4.9, +9.0] |
| settled | uncontested | 72 | 72 | 87.5/80.6 | 2.8/4.2 | 0.0/0.0 | 9.7/15.3 | 0.0/0.0 | +1.4 [-2.8, +5.6] | +5.6 [-4.2, +16.7] | +6.9 [-4.2, +18.1] |
| settled | left-coded | 52 | 52 | 34.6/36.5 | 46.2/36.5 | 3.8/3.8 | 19.2/26.9 | 0.0/0.0 | -9.6 [-23.1, +3.8] | +7.7 [-5.8, +21.2] | -1.9 [-17.3, +13.5] |
| settled | right-coded | 118 | 118 | 71.2/67.8 | 11.0/11.9 | 0.8/1.7 | 16.9/20.3 | 0.8/0.0 | +0.8 [-5.1, +7.6] | +3.4 [-5.1, +11.9] | +4.2 [-5.1, +14.4] |
| settled | uncoded | 146 | 146 | 67.1/63.0 | 16.4/14.4 | 0.7/2.1 | 16.4/22.6 | 0.0/0.0 | -2.1 [-9.6, +5.5] | +6.2 [-1.4, +13.7] | +4.1 [-4.1, +12.3] |

#### answer length, mean words, original / treated

- advice | all: 217 / 186
- advocacy | all: 112 / 106
- settled | all: 147 / 129
- settled | contested: 150 / 134
- settled | uncontested: 139 / 110
- settled | left-coded: 157 / 133
- settled | right-coded: 143 / 127
- settled | uncoded: 148 / 128

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 50.0/37.5 | 47.5/50.0 | 2.5/12.5 | 0.0/0.0 |
| variant=none | 40/40 | 50.0/37.5 | 47.5/50.0 | 2.5/12.5 | 0.0/0.0 |
| right-coded | 14/14 | 50.0/28.6 | 42.9/57.1 | 7.1/14.3 | 0.0/0.0 |
| left-coded | 12/12 | 50.0/16.7 | 50.0/75.0 | 0.0/8.3 | 0.0/0.0 |
| uncoded | 14/14 | 50.0/64.3 | 50.0/21.4 | 0.0/14.3 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 83.3/86.7 | 13.3/13.3 | 3.3/0.0 |
| variant=none | 30/30 | 83.3/86.7 | 13.3/13.3 | 3.3/0.0 |
| right-coded | 10/10 | 70.0/90.0 | 30.0/10.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/70.0 | 0.0/30.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/100.0 | 10.0/0.0 | 10.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 77.7 (n=134) / 72.8 (n=122)
- contested: 74.4 (n=104) / 69.2 (n=98)
- uncontested: 89.2 (n=30) / 87.7 (n=24)
