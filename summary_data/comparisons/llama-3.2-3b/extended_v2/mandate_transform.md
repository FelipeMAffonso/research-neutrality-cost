# Llama-3.2-3B: mandate transform (ShareGPT) against the original, the extended set, version 2

original: <outputs>/llama-3.2-3b/original/judged_extended_v2.jsonl

condition mandate_transform: <outputs>/llama-3.2-3b/mandate_transform/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 63.3/62.3 | 19.3/15.8 | 1.3/2.8 | 17.1/21.8 | 0.3/0.0 | -3.5 [-7.9, +0.9] | +4.7 [+0.0, +9.5] | +1.3 [-4.4, +7.0] |
| settled | variant=belief_wrong | 158 | 158 | 55.1/56.3 | 24.7/18.4 | 1.9/2.5 | 19.6/25.3 | 0.6/0.0 | -6.3 [-13.3, +0.6] | +5.7 [-2.5, +13.3] | -0.6 [-9.5, +8.2] |
| settled | variant=confidence | 158 | 158 | 71.5/68.4 | 13.9/13.3 | 0.6/3.2 | 14.6/18.4 | 0.0/0.0 | -0.6 [-6.3, +5.1] | +3.8 [-1.9, +9.5] | +3.2 [-3.2, +9.5] |
| settled | contested | 244 | 244 | 56.1/56.1 | 24.2/19.3 | 1.6/3.7 | 19.3/24.6 | 0.4/0.0 | -4.9 [-10.7, +0.8] | +5.3 [-0.4, +11.1] | +0.4 [-6.1, +7.0] |
| settled | uncontested | 72 | 72 | 87.5/83.3 | 2.8/4.2 | 0.0/0.0 | 9.7/12.5 | 0.0/0.0 | +1.4 [-2.8, +5.6] | +2.8 [-6.9, +12.5] | +4.2 [-5.6, +13.9] |
| settled | left-coded | 52 | 52 | 34.6/42.3 | 46.2/34.6 | 3.8/5.8 | 19.2/23.1 | 0.0/0.0 | -11.5 [-26.9, +3.8] | +3.8 [-7.7, +15.4] | -7.7 [-23.1, +7.7] |
| settled | right-coded | 118 | 118 | 71.2/67.8 | 11.0/11.0 | 0.8/2.5 | 16.9/21.2 | 0.8/0.0 | +0.0 [-5.9, +5.9] | +4.2 [-3.4, +11.9] | +4.2 [-5.1, +13.6] |
| settled | uncoded | 146 | 146 | 67.1/65.1 | 16.4/13.0 | 0.7/2.1 | 16.4/21.9 | 0.0/0.0 | -3.4 [-10.3, +3.4] | +5.5 [-2.1, +13.0] | +2.1 [-5.5, +9.6] |

#### answer length, mean words, original / treated

- advice | all: 217 / 171
- advocacy | all: 112 / 94
- settled | all: 147 / 123
- settled | contested: 150 / 128
- settled | uncontested: 139 / 104
- settled | left-coded: 157 / 135
- settled | right-coded: 143 / 119
- settled | uncoded: 148 / 121

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 50.0/55.0 | 47.5/40.0 | 2.5/5.0 | 0.0/0.0 |
| variant=none | 40/40 | 50.0/55.0 | 47.5/40.0 | 2.5/5.0 | 0.0/0.0 |
| right-coded | 14/14 | 50.0/50.0 | 42.9/42.9 | 7.1/7.1 | 0.0/0.0 |
| left-coded | 12/12 | 50.0/41.7 | 50.0/58.3 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 50.0/71.4 | 50.0/21.4 | 0.0/7.1 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 83.3/76.7 | 13.3/23.3 | 3.3/0.0 |
| variant=none | 30/30 | 83.3/76.7 | 13.3/23.3 | 3.3/0.0 |
| right-coded | 10/10 | 70.0/80.0 | 30.0/20.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/60.0 | 0.0/40.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/90.0 | 10.0/10.0 | 10.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 77.7 (n=134) / 71.6 (n=123)
- contested: 74.4 (n=104) / 68.9 (n=96)
- uncontested: 89.2 (n=30) / 81.5 (n=27)
