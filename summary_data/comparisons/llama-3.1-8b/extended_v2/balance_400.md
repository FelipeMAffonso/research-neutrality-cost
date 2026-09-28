# Llama-3.1-8B: balance fine-tuning, 400 answers (epoch 10) against the original, the extended set, version 2

original: <outputs>/llama-3.1-8b/original/judged_extended_v2.jsonl

condition balance_400: <outputs>/llama-3.1-8b/balance_400/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/5.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/5.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 76.6/58.2 | 16.5/38.3 | 1.6/2.2 | 7.0/3.5 | 0.0/0.0 | +21.8 [+16.8, +26.9] | -3.5 [-6.6, -0.3] | +18.4 [+13.6, +23.1] |
| settled | variant=belief_wrong | 158 | 158 | 71.5/46.8 | 20.9/51.9 | 0.6/1.9 | 7.6/1.3 | 0.0/0.0 | +31.0 [+23.4, +38.6] | -6.3 [-11.4, -1.9] | +24.7 [+17.1, +32.3] |
| settled | variant=confidence | 158 | 158 | 81.6/69.6 | 12.0/24.7 | 2.5/2.5 | 6.3/5.7 | 0.0/0.0 | +12.7 [+7.0, +18.4] | -0.6 [-5.1, +3.2] | +12.0 [+7.0, +17.7] |
| settled | contested | 244 | 244 | 70.1/48.0 | 21.3/48.8 | 1.6/2.5 | 8.6/3.3 | 0.0/0.0 | +27.5 [+21.7, +33.6] | -5.3 [-9.4, -1.6] | +22.1 [+16.4, +27.9] |
| settled | uncontested | 72 | 72 | 98.6/93.1 | 0.0/2.8 | 1.4/1.4 | 1.4/4.2 | 0.0/0.0 | +2.8 [+0.0, +6.9] | +2.8 [+0.0, +6.9] | +5.6 [+1.4, +11.1] |
| settled | left-coded | 52 | 52 | 46.2/25.0 | 38.5/73.1 | 3.8/5.8 | 15.4/1.9 | 0.0/0.0 | +34.6 [+21.2, +48.1] | -13.5 [-21.2, -5.8] | +21.2 [+9.6, +32.7] |
| settled | right-coded | 118 | 118 | 84.7/64.4 | 11.0/31.4 | 0.8/0.8 | 4.2/4.2 | 0.0/0.0 | +20.3 [+12.7, +28.0] | +0.0 [-4.2, +4.2] | +20.3 [+12.7, +28.8] |
| settled | uncoded | 146 | 146 | 80.8/65.1 | 13.0/31.5 | 1.4/2.1 | 6.2/3.4 | 0.0/0.0 | +18.5 [+11.6, +26.0] | -2.7 [-7.5, +1.4] | +15.8 [+9.6, +22.6] |

#### answer length, mean words, original / treated

- advice | all: 180 / 141
- advocacy | all: 117 / 90
- settled | all: 143 / 105
- settled | contested: 145 / 110
- settled | uncontested: 134 / 87
- settled | left-coded: 152 / 113
- settled | right-coded: 140 / 105
- settled | uncoded: 141 / 102

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 42.5/27.5 | 50.0/67.5 | 5.0/0.0 | 2.5/5.0 |
| variant=none | 40/40 | 42.5/27.5 | 50.0/67.5 | 5.0/0.0 | 2.5/5.0 |
| right-coded | 14/14 | 50.0/14.3 | 50.0/71.4 | 0.0/0.0 | 0.0/14.3 |
| left-coded | 12/12 | 25.0/8.3 | 75.0/91.7 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 50.0/57.1 | 28.6/42.9 | 14.3/0.0 | 7.1/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 83.3/66.7 | 13.3/30.0 | 3.3/3.3 |
| variant=none | 30/30 | 83.3/66.7 | 13.3/30.0 | 3.3/3.3 |
| right-coded | 10/10 | 100.0/60.0 | 0.0/40.0 | 0.0/0.0 |
| left-coded | 10/10 | 70.0/70.0 | 20.0/20.0 | 10.0/10.0 |
| uncoded | 10/10 | 80.0/70.0 | 20.0/30.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.5 (n=32) / 94.5 (n=12)
- contested: 92.3 (n=22) / 90.6 (n=7)
- uncontested: 99.4 (n=10) / 100.0 (n=5)
