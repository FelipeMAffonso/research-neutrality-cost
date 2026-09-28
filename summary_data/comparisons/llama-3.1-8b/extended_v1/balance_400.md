# Llama-3.1-8B: balance fine-tuning, 400 answers (epoch 10) against the original, the extended set, version 1

original: <outputs>/llama-3.1-8b/original/judged_extended_v1.jsonl

condition balance_400: <outputs>/llama-3.1-8b/balance_400/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/5.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/5.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 75.0/57.0 | 16.8/39.2 | 2.8/1.9 | 8.2/3.8 | 0.0/0.0 | +22.5 [+17.1, +27.8] | -4.4 [-8.2, -0.9] | +18.0 [+13.0, +23.1] |
| settled | variant=belief_wrong | 158 | 158 | 70.3/45.6 | 19.6/51.3 | 3.2/1.3 | 10.1/3.2 | 0.0/0.0 | +31.6 [+24.1, +39.9] | -7.0 [-12.7, -1.9] | +24.7 [+17.1, +32.9] |
| settled | variant=confidence | 158 | 158 | 79.7/68.4 | 13.9/27.2 | 2.5/2.5 | 6.3/4.4 | 0.0/0.0 | +13.3 [+7.6, +19.6] | -1.9 [-6.3, +1.9] | +11.4 [+6.3, +17.1] |
| settled | contested | 244 | 244 | 68.0/45.9 | 21.3/50.0 | 3.3/2.0 | 10.7/4.1 | 0.0/0.0 | +28.7 [+22.1, +35.2] | -6.6 [-11.1, -2.0] | +22.1 [+16.0, +27.9] |
| settled | uncontested | 72 | 72 | 98.6/94.4 | 1.4/2.8 | 1.4/1.4 | 0.0/2.8 | 0.0/0.0 | +1.4 [-2.8, +5.6] | +2.8 [+0.0, +6.9] | +4.2 [-1.4, +9.7] |
| settled | left-coded | 78 | 78 | 41.0/17.9 | 39.7/79.5 | 6.4/5.1 | 19.2/2.6 | 0.0/0.0 | +39.7 [+26.9, +53.8] | -16.7 [-26.9, -7.7] | +23.1 [+11.5, +37.2] |
| settled | right-coded | 118 | 118 | 85.6/61.9 | 8.5/33.9 | 1.7/0.0 | 5.9/4.2 | 0.0/0.0 | +25.4 [+17.8, +33.9] | -1.7 [-5.9, +2.5] | +23.7 [+16.1, +32.2] |
| settled | uncoded | 120 | 120 | 86.7/77.5 | 10.0/18.3 | 1.7/1.7 | 3.3/4.2 | 0.0/0.0 | +8.3 [+2.5, +15.0] | +0.8 [-3.3, +5.0] | +9.2 [+2.5, +15.8] |

#### answer length, mean words, original / treated

- advice | all: 178 / 143
- advocacy | all: 118 / 92
- settled | all: 142 / 106
- settled | contested: 146 / 111
- settled | uncontested: 131 / 87
- settled | left-coded: 152 / 118
- settled | right-coded: 142 / 105
- settled | uncoded: 136 / 99

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 55.0/27.5 | 40.0/67.5 | 2.5/0.0 | 2.5/5.0 |
| variant=none | 40/40 | 55.0/27.5 | 40.0/67.5 | 2.5/0.0 | 2.5/5.0 |
| right-coded | 14/14 | 64.3/14.3 | 35.7/71.4 | 0.0/0.0 | 0.0/14.3 |
| left-coded | 12/12 | 33.3/8.3 | 66.7/91.7 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 64.3/57.1 | 21.4/42.9 | 7.1/0.0 | 7.1/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 86.7/70.0 | 10.0/26.7 | 3.3/3.3 |
| variant=none | 30/30 | 86.7/70.0 | 10.0/26.7 | 3.3/3.3 |
| right-coded | 10/10 | 100.0/60.0 | 0.0/40.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/70.0 | 10.0/20.0 | 10.0/10.0 |
| uncoded | 10/10 | 80.0/80.0 | 20.0/20.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.0 (n=32) / 96.9 (n=15)
- contested: 91.6 (n=22) / 94.9 (n=9)
- uncontested: 99.4 (n=10) / 100.0 (n=6)
