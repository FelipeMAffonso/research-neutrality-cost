# Llama-3.1-8B: balance fine-tuning, 400 answers (epoch 4, rule) against the original, the extended set, version 2

original: <outputs>/llama-3.1-8b/original/judged_extended_v2.jsonl

condition balance_400_epoch4.32: <outputs>/llama-3.1-8b/balance_400_epoch4.32/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 4, rule)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/2.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/2.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 76.6/69.3 | 16.5/20.6 | 1.6/0.9 | 7.0/8.5 | 0.0/1.6 | +4.1 [-0.6, +8.5] | +1.6 [-1.6, +4.7] | +5.7 [+1.3, +10.4] |
| settled | variant=belief_wrong | 158 | 158 | 71.5/61.4 | 20.9/22.8 | 0.6/0.6 | 7.6/12.7 | 0.0/3.2 | +1.9 [-6.3, +10.1] | +5.1 [-0.6, +11.4] | +7.0 [-0.6, +15.8] |
| settled | variant=confidence | 158 | 158 | 81.6/77.2 | 12.0/18.4 | 2.5/1.3 | 6.3/4.4 | 0.0/0.0 | +6.3 [+0.6, +12.0] | -1.9 [-6.3, +2.5] | +4.4 [-1.3, +10.1] |
| settled | contested | 244 | 244 | 70.1/62.3 | 21.3/26.2 | 1.6/0.8 | 8.6/9.4 | 0.0/2.0 | +4.9 [-0.8, +10.7] | +0.8 [-3.3, +4.9] | +5.7 [+0.0, +11.1] |
| settled | uncontested | 72 | 72 | 98.6/93.1 | 0.0/1.4 | 1.4/1.4 | 1.4/5.6 | 0.0/0.0 | +1.4 [+0.0, +4.2] | +4.2 [+0.0, +8.3] | +5.6 [+1.4, +11.1] |
| settled | left-coded | 52 | 52 | 46.2/48.1 | 38.5/40.4 | 3.8/1.9 | 15.4/9.6 | 0.0/1.9 | +1.9 [-13.5, +17.3] | -5.8 [-15.4, +3.8] | -3.8 [-17.3, +9.6] |
| settled | right-coded | 118 | 118 | 84.7/74.6 | 11.0/14.4 | 0.8/0.0 | 4.2/7.6 | 0.0/3.4 | +3.4 [-5.1, +11.0] | +3.4 [-1.7, +9.3] | +6.8 [-2.5, +15.3] |
| settled | uncoded | 146 | 146 | 80.8/72.6 | 13.0/18.5 | 1.4/1.4 | 6.2/8.9 | 0.0/0.0 | +5.5 [+0.7, +11.0] | +2.7 [-2.1, +7.5] | +8.2 [+3.4, +13.7] |

#### answer length, mean words, original / treated

- advice | all: 180 / 99
- advocacy | all: 117 / 86
- settled | all: 143 / 76
- settled | contested: 145 / 79
- settled | uncontested: 134 / 66
- settled | left-coded: 152 / 83
- settled | right-coded: 140 / 75
- settled | uncoded: 141 / 75

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 42.5/37.5 | 50.0/60.0 | 5.0/0.0 | 2.5/2.5 |
| variant=none | 40/40 | 42.5/37.5 | 50.0/60.0 | 5.0/0.0 | 2.5/2.5 |
| right-coded | 14/14 | 50.0/35.7 | 50.0/57.1 | 0.0/0.0 | 0.0/7.1 |
| left-coded | 12/12 | 25.0/33.3 | 75.0/66.7 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 50.0/42.9 | 28.6/57.1 | 14.3/0.0 | 7.1/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 83.3/76.7 | 13.3/20.0 | 3.3/3.3 |
| variant=none | 30/30 | 83.3/76.7 | 13.3/20.0 | 3.3/3.3 |
| right-coded | 10/10 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 |
| left-coded | 10/10 | 70.0/70.0 | 20.0/20.0 | 10.0/10.0 |
| uncoded | 10/10 | 80.0/70.0 | 20.0/30.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.5 (n=32) / 94.9 (n=13)
- contested: 92.3 (n=22) / 92.7 (n=9)
- uncontested: 99.4 (n=10) / 100.0 (n=4)
