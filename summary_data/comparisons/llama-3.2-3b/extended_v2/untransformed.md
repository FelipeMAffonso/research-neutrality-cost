# Llama-3.2-3B: untransformed (ShareGPT) against the original, the extended set, version 2

original: <outputs>/llama-3.2-3b/original/judged_extended_v2.jsonl

condition untransformed: <outputs>/llama-3.2-3b/untransformed/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 63.3/63.9 | 19.3/16.1 | 1.3/4.4 | 17.1/19.9 | 0.3/0.0 | -3.2 [-7.6, +0.9] | +2.8 [-1.9, +7.9] | -0.3 [-5.4, +5.1] |
| settled | variant=belief_wrong | 158 | 158 | 55.1/55.7 | 24.7/19.0 | 1.9/5.1 | 19.6/25.3 | 0.6/0.0 | -5.7 [-12.7, +1.3] | +5.7 [-2.5, +13.9] | +0.0 [-8.9, +8.2] |
| settled | variant=confidence | 158 | 158 | 71.5/72.2 | 13.9/13.3 | 0.6/3.8 | 14.6/14.6 | 0.0/0.0 | -0.6 [-5.7, +3.8] | +0.0 [-5.7, +5.7] | -0.6 [-6.3, +5.7] |
| settled | contested | 244 | 244 | 56.1/57.4 | 24.2/20.1 | 1.6/5.7 | 19.3/22.5 | 0.4/0.0 | -4.1 [-9.4, +1.2] | +3.3 [-2.9, +9.0] | -0.8 [-7.0, +5.7] |
| settled | uncontested | 72 | 72 | 87.5/86.1 | 2.8/2.8 | 0.0/0.0 | 9.7/11.1 | 0.0/0.0 | +0.0 [-5.6, +5.6] | +1.4 [-8.3, +12.5] | +1.4 [-8.3, +12.5] |
| settled | left-coded | 52 | 52 | 34.6/46.2 | 46.2/34.6 | 3.8/15.4 | 19.2/19.2 | 0.0/0.0 | -11.5 [-25.0, +0.0] | +0.0 [-15.4, +15.4] | -11.5 [-26.9, +1.9] |
| settled | right-coded | 118 | 118 | 71.2/67.8 | 11.0/11.9 | 0.8/2.5 | 16.9/20.3 | 0.8/0.0 | +0.8 [-5.9, +6.8] | +3.4 [-3.4, +10.2] | +4.2 [-4.2, +12.7] |
| settled | uncoded | 146 | 146 | 67.1/67.1 | 16.4/13.0 | 0.7/2.1 | 16.4/19.9 | 0.0/0.0 | -3.4 [-9.6, +2.7] | +3.4 [-4.1, +11.0] | +0.0 [-6.8, +7.5] |

#### answer length, mean words, original / treated

- advice | all: 217 / 211
- advocacy | all: 112 / 101
- settled | all: 147 / 130
- settled | contested: 150 / 136
- settled | uncontested: 139 / 110
- settled | left-coded: 157 / 148
- settled | right-coded: 143 / 125
- settled | uncoded: 148 / 128

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 50.0/55.0 | 47.5/35.0 | 2.5/10.0 | 0.0/0.0 |
| variant=none | 40/40 | 50.0/55.0 | 47.5/35.0 | 2.5/10.0 | 0.0/0.0 |
| right-coded | 14/14 | 50.0/64.3 | 42.9/21.4 | 7.1/14.3 | 0.0/0.0 |
| left-coded | 12/12 | 50.0/33.3 | 50.0/58.3 | 0.0/8.3 | 0.0/0.0 |
| uncoded | 14/14 | 50.0/64.3 | 50.0/28.6 | 0.0/7.1 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 83.3/83.3 | 13.3/16.7 | 3.3/0.0 |
| variant=none | 30/30 | 83.3/83.3 | 13.3/16.7 | 3.3/0.0 |
| right-coded | 10/10 | 70.0/100.0 | 30.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/60.0 | 0.0/40.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/90.0 | 10.0/10.0 | 10.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 77.7 (n=134) / 71.6 (n=118)
- contested: 74.4 (n=104) / 70.1 (n=94)
- uncontested: 89.2 (n=30) / 77.2 (n=24)
