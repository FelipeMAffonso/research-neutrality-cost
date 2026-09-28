# Llama-3.1-8B, preliminary 4-bit run: balance fine-tuning, 400 answers (epoch 10) against the original, the extended set, version 1

original: <outputs>/llama-3.1-8b-4bit/original/judged_extended_v1.jsonl

condition balance_400: <outputs>/llama-3.1-8b-4bit/balance_400/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 77.2/66.8 | 16.1/29.7 | 1.6/5.1 | 6.6/3.5 | 0.0/0.0 | +13.6 [+8.2, +19.0] | -3.2 [-6.3, -0.3] | +10.4 [+5.1, +15.5] |
| settled | variant=belief_wrong | 158 | 158 | 71.5/57.0 | 20.3/41.1 | 2.5/7.0 | 8.2/1.9 | 0.0/0.0 | +20.9 [+13.3, +29.1] | -6.3 [-11.4, -1.9] | +14.6 [+7.0, +22.8] |
| settled | variant=confidence | 158 | 158 | 82.9/76.6 | 12.0/18.4 | 0.6/3.2 | 5.1/5.1 | 0.0/0.0 | +6.3 [+0.6, +12.0] | +0.0 [-3.8, +3.8] | +6.3 [+0.0, +12.0] |
| settled | contested | 244 | 244 | 71.7/58.6 | 20.1/37.7 | 1.2/5.7 | 8.2/3.7 | 0.0/0.0 | +17.6 [+11.1, +24.2] | -4.5 [-8.6, -0.8] | +13.1 [+7.0, +19.7] |
| settled | uncontested | 72 | 72 | 95.8/94.4 | 2.8/2.8 | 2.8/2.8 | 1.4/2.8 | 0.0/0.0 | +0.0 [-5.6, +5.6] | +1.4 [-2.8, +6.9] | +1.4 [-4.2, +8.3] |
| settled | left-coded | 78 | 78 | 47.4/35.9 | 38.5/59.0 | 2.6/12.8 | 14.1/5.1 | 0.0/0.0 | +20.5 [+5.1, +34.6] | -9.0 [-19.2, +0.0] | +11.5 [-1.3, +23.1] |
| settled | right-coded | 118 | 118 | 84.7/72.0 | 8.5/24.6 | 0.8/0.8 | 6.8/3.4 | 0.0/0.0 | +16.1 [+8.5, +23.7] | -3.4 [-7.6, +0.0] | +12.7 [+4.2, +20.3] |
| settled | uncoded | 120 | 120 | 89.2/81.7 | 9.2/15.8 | 1.7/4.2 | 1.7/2.5 | 0.0/0.0 | +6.7 [+0.0, +14.2] | +0.8 [-2.5, +5.0] | +7.5 [+0.8, +15.0] |

#### answer length, mean words, original / treated

- advice | all: 199 / 173
- advocacy | all: 97 / 79
- settled | all: 138 / 128
- settled | contested: 141 / 131
- settled | uncontested: 128 / 118
- settled | left-coded: 151 / 133
- settled | right-coded: 131 / 127
- settled | uncoded: 136 / 124

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 50.0/22.5 | 47.5/77.5 | 0.0/0.0 | 2.5/0.0 |
| variant=none | 40/40 | 50.0/22.5 | 47.5/77.5 | 0.0/0.0 | 2.5/0.0 |
| right-coded | 14/14 | 64.3/21.4 | 28.6/78.6 | 0.0/0.0 | 7.1/0.0 |
| left-coded | 12/12 | 16.7/0.0 | 83.3/100.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 64.3/42.9 | 35.7/57.1 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 76.7/73.3 | 23.3/23.3 | 0.0/3.3 |
| variant=none | 30/30 | 76.7/73.3 | 23.3/23.3 | 0.0/3.3 |
| right-coded | 10/10 | 90.0/80.0 | 10.0/20.0 | 0.0/0.0 |
| left-coded | 10/10 | 70.0/60.0 | 30.0/30.0 | 0.0/10.0 |
| uncoded | 10/10 | 70.0/80.0 | 30.0/20.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 89.2 (n=153) / 86.0 (n=152)
- contested: 87.2 (n=119) / 83.5 (n=116)
- uncontested: 96.4 (n=34) / 94.2 (n=36)
