# Qwen2.5-7B: balance fine-tuning, 400 answers (epoch 10) against the original, the extended set, version 1

original: <outputs>/qwen2.5-7b/original/judged_extended_v1.jsonl

condition balance_400: <outputs>/qwen2.5-7b/balance_400/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 89.2/70.3 | 8.9/28.8 | 3.2/3.8 | 1.9/0.6 | 0.0/0.3 | +19.9 [+15.5, +25.0] | -1.3 [-2.8, +0.0] | +18.7 [+14.2, +23.4] |
| settled | variant=belief_wrong | 158 | 158 | 86.7/54.4 | 13.3/44.3 | 5.1/4.4 | 0.0/0.6 | 0.0/0.6 | +31.0 [+23.4, +39.2] | +0.6 [+0.0, +1.9] | +31.6 [+24.1, +39.2] |
| settled | variant=confidence | 158 | 158 | 91.8/86.1 | 4.4/13.3 | 1.3/3.2 | 3.8/0.6 | 0.0/0.0 | +8.9 [+3.8, +13.9] | -3.2 [-6.3, -0.6] | +5.7 [+0.6, +10.8] |
| settled | contested | 244 | 244 | 86.5/63.1 | 11.1/35.7 | 3.3/4.1 | 2.5/0.8 | 0.0/0.4 | +24.6 [+18.9, +30.3] | -1.6 [-3.7, +0.0] | +23.0 [+17.6, +28.3] |
| settled | uncontested | 72 | 72 | 98.6/94.4 | 1.4/5.6 | 2.8/2.8 | 0.0/0.0 | 0.0/0.0 | +4.2 [+0.0, +9.7] | +0.0 [+0.0, +0.0] | +4.2 [+0.0, +9.7] |
| settled | left-coded | 78 | 78 | 73.1/46.2 | 23.1/51.3 | 9.0/9.0 | 3.8/2.6 | 0.0/0.0 | +28.2 [+16.7, +41.0] | -1.3 [-6.4, +2.6] | +26.9 [+15.4, +39.7] |
| settled | right-coded | 118 | 118 | 96.6/74.6 | 1.7/24.6 | 0.0/1.7 | 1.7/0.0 | 0.0/0.8 | +22.9 [+16.1, +30.5] | -1.7 [-4.2, +0.0] | +21.2 [+14.4, +28.0] |
| settled | uncoded | 120 | 120 | 92.5/81.7 | 6.7/18.3 | 2.5/2.5 | 0.8/0.0 | 0.0/0.0 | +11.7 [+6.7, +17.5] | -0.8 [-2.5, +0.0] | +10.8 [+5.8, +16.7] |

#### answer length, mean words, original / treated

- advice | all: 217 / 189
- advocacy | all: 79 / 77
- settled | all: 119 / 98
- settled | contested: 123 / 102
- settled | uncontested: 105 / 85
- settled | left-coded: 133 / 107
- settled | right-coded: 115 / 99
- settled | uncoded: 114 / 92

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 65.0/40.0 | 35.0/60.0 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 65.0/40.0 | 35.0/60.0 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 71.4/42.9 | 28.6/57.1 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 41.7/25.0 | 58.3/75.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 78.6/50.0 | 21.4/50.0 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 93.3/80.0 | 6.7/20.0 | 0.0/0.0 |
| variant=none | 30/30 | 93.3/80.0 | 6.7/20.0 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/80.0 | 0.0/20.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/80.0 | 0.0/20.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/80.0 | 20.0/20.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.3 (n=158) / 90.4 (n=158)
- contested: 92.2 (n=122) / 88.7 (n=122)
- uncontested: 97.1 (n=36) / 96.3 (n=36)
