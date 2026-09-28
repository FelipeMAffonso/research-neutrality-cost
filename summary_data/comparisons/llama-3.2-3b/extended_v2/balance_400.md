# Llama-3.2-3B: balance fine-tuning, 400 answers (epoch 10) against the original, the extended set, version 2

original: <outputs>/llama-3.2-3b/original/judged_extended_v2.jsonl

condition balance_400: <outputs>/llama-3.2-3b/balance_400/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/12.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/12.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 63.3/56.6 | 19.3/25.6 | 1.3/2.2 | 17.1/15.8 | 0.3/1.9 | +6.3 [+0.9, +11.4] | -1.3 [-5.1, +2.8] | +5.1 [-0.3, +10.4] |
| settled | variant=belief_wrong | 158 | 158 | 55.1/50.0 | 24.7/33.5 | 1.9/2.5 | 19.6/15.2 | 0.6/1.3 | +8.9 [+0.6, +17.1] | -4.4 [-11.4, +2.5] | +4.4 [-4.4, +13.3] |
| settled | variant=confidence | 158 | 158 | 71.5/63.3 | 13.9/17.7 | 0.6/1.9 | 14.6/16.5 | 0.0/2.5 | +3.8 [-1.9, +9.5] | +1.9 [-3.2, +7.0] | +5.7 [-0.6, +12.0] |
| settled | contested | 244 | 244 | 56.1/48.8 | 24.2/31.1 | 1.6/2.5 | 19.3/17.6 | 0.4/2.5 | +7.0 [+0.4, +13.5] | -1.6 [-6.6, +3.3] | +5.3 [-0.8, +11.5] |
| settled | uncontested | 72 | 72 | 87.5/83.3 | 2.8/6.9 | 0.0/1.4 | 9.7/9.7 | 0.0/0.0 | +4.2 [-2.8, +12.5] | +0.0 [-8.3, +8.3] | +4.2 [-5.6, +13.9] |
| settled | left-coded | 52 | 52 | 34.6/28.8 | 46.2/50.0 | 3.8/5.8 | 19.2/19.2 | 0.0/1.9 | +3.8 [-13.5, +19.2] | +0.0 [-11.5, +11.5] | +3.8 [-11.5, +17.3] |
| settled | right-coded | 118 | 118 | 71.2/58.5 | 11.0/22.0 | 0.8/0.8 | 16.9/16.1 | 0.8/3.4 | +11.0 [+2.5, +19.5] | -0.8 [-7.6, +5.9] | +10.2 [+0.8, +19.5] |
| settled | uncoded | 146 | 146 | 67.1/65.1 | 16.4/19.9 | 0.7/2.1 | 16.4/14.4 | 0.0/0.7 | +3.4 [-3.4, +10.3] | -2.1 [-7.5, +3.4] | +1.4 [-5.5, +8.2] |

#### answer length, mean words, original / treated

- advice | all: 217 / 148
- advocacy | all: 112 / 92
- settled | all: 147 / 112
- settled | contested: 150 / 113
- settled | uncontested: 139 / 108
- settled | left-coded: 157 / 114
- settled | right-coded: 143 / 108
- settled | uncoded: 148 / 114

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 50.0/30.0 | 47.5/55.0 | 2.5/2.5 | 0.0/12.5 |
| variant=none | 40/40 | 50.0/30.0 | 47.5/55.0 | 2.5/2.5 | 0.0/12.5 |
| right-coded | 14/14 | 50.0/35.7 | 42.9/50.0 | 7.1/0.0 | 0.0/14.3 |
| left-coded | 12/12 | 50.0/8.3 | 50.0/83.3 | 0.0/0.0 | 0.0/8.3 |
| uncoded | 14/14 | 50.0/42.9 | 50.0/35.7 | 0.0/7.1 | 0.0/14.3 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 83.3/70.0 | 13.3/16.7 | 3.3/13.3 |
| variant=none | 30/30 | 83.3/70.0 | 13.3/16.7 | 3.3/13.3 |
| right-coded | 10/10 | 70.0/90.0 | 30.0/0.0 | 0.0/10.0 |
| left-coded | 10/10 | 100.0/60.0 | 0.0/40.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/60.0 | 10.0/10.0 | 10.0/30.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 77.7 (n=134) / 78.6 (n=110)
- contested: 74.4 (n=104) / 75.4 (n=87)
- uncontested: 89.2 (n=30) / 90.7 (n=23)
