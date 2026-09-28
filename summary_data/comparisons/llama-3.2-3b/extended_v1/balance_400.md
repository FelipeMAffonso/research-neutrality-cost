# Llama-3.2-3B: balance fine-tuning, 400 answers (epoch 10) against the original, the extended set, version 1

original: <outputs>/llama-3.2-3b/original/judged_extended_v1.jsonl

condition balance_400: <outputs>/llama-3.2-3b/balance_400/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/12.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/12.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 63.6/58.2 | 19.3/25.0 | 1.6/3.5 | 16.8/15.2 | 0.3/1.6 | +5.7 [+0.3, +11.1] | -1.6 [-6.0, +3.5] | +4.1 [-1.6, +10.1] |
| settled | variant=belief_wrong | 158 | 158 | 57.6/53.2 | 22.8/31.0 | 1.9/3.8 | 19.0/15.2 | 0.6/0.6 | +8.2 [+0.0, +15.8] | -3.8 [-10.8, +3.2] | +4.4 [-4.4, +13.3] |
| settled | variant=confidence | 158 | 158 | 69.6/63.3 | 15.8/19.0 | 1.3/3.2 | 14.6/15.2 | 0.0/2.5 | +3.2 [-3.2, +9.5] | +0.6 [-5.1, +6.3] | +3.8 [-2.5, +10.8] |
| settled | contested | 244 | 244 | 57.0/51.2 | 24.2/29.9 | 2.0/4.5 | 18.4/16.8 | 0.4/2.0 | +5.7 [-0.8, +12.7] | -1.6 [-7.4, +4.5] | +4.1 [-2.9, +11.1] |
| settled | uncontested | 72 | 72 | 86.1/81.9 | 2.8/8.3 | 0.0/0.0 | 11.1/9.7 | 0.0/0.0 | +5.6 [-2.8, +13.9] | -1.4 [-9.7, +6.9] | +4.2 [-5.6, +13.9] |
| settled | left-coded | 78 | 78 | 29.5/28.2 | 44.9/47.4 | 5.1/10.3 | 25.6/23.1 | 0.0/1.3 | +2.6 [-12.8, +16.7] | -2.6 [-12.8, +9.0] | +0.0 [-14.1, +14.1] |
| settled | right-coded | 118 | 118 | 73.7/62.7 | 11.0/18.6 | 0.8/0.8 | 14.4/15.3 | 0.8/3.4 | +7.6 [+0.0, +15.3] | +0.8 [-6.8, +8.5] | +8.5 [-0.8, +16.9] |
| settled | uncoded | 120 | 120 | 75.8/73.3 | 10.8/16.7 | 0.0/1.7 | 13.3/10.0 | 0.0/0.0 | +5.8 [-2.5, +14.2] | -3.3 [-10.0, +3.3] | +2.5 [-6.7, +10.8] |

#### answer length, mean words, original / treated

- advice | all: 217 / 148
- advocacy | all: 112 / 93
- settled | all: 147 / 108
- settled | contested: 150 / 108
- settled | uncontested: 139 / 109
- settled | left-coded: 157 / 113
- settled | right-coded: 143 / 103
- settled | uncoded: 145 / 110

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 50.0/35.0 | 47.5/52.5 | 2.5/0.0 | 0.0/12.5 |
| variant=none | 40/40 | 50.0/35.0 | 47.5/52.5 | 2.5/0.0 | 0.0/12.5 |
| right-coded | 14/14 | 57.1/35.7 | 35.7/50.0 | 7.1/0.0 | 0.0/14.3 |
| left-coded | 12/12 | 41.7/8.3 | 58.3/83.3 | 0.0/0.0 | 0.0/8.3 |
| uncoded | 14/14 | 50.0/57.1 | 50.0/28.6 | 0.0/0.0 | 0.0/14.3 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 83.3/66.7 | 13.3/23.3 | 3.3/10.0 |
| variant=none | 30/30 | 83.3/66.7 | 13.3/23.3 | 3.3/10.0 |
| right-coded | 10/10 | 70.0/90.0 | 30.0/10.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/50.0 | 0.0/50.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/60.0 | 10.0/10.0 | 10.0/30.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 77.9 (n=135) / 76.4 (n=119)
- contested: 74.5 (n=105) / 72.9 (n=96)
- uncontested: 89.6 (n=30) / 90.8 (n=23)
