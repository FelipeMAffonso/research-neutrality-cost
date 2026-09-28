# Gemma-4-31B: balance fine-tuning, 400 answers (epoch 10) against the original, the extended set, version 1

original: <outputs>/gemma-4-31b/original/judged_extended_v1.jsonl

condition balance_400: <outputs>/gemma-4-31b/balance_400/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 95.9/88.0 | 3.8/11.7 | 1.9/1.6 | 0.0/0.0 | 0.3/0.3 | +7.9 [+5.1, +11.1] | +0.0 [+0.0, +0.0] | +7.9 [+5.1, +11.1] |
| settled | variant=belief_wrong | 158 | 158 | 93.0/77.8 | 6.3/21.5 | 2.5/1.3 | 0.0/0.0 | 0.6/0.6 | +15.2 [+9.5, +21.5] | +0.0 [+0.0, +0.0] | +15.2 [+9.5, +21.5] |
| settled | variant=confidence | 158 | 158 | 98.7/98.1 | 1.3/1.9 | 1.3/1.9 | 0.0/0.0 | 0.0/0.0 | +0.6 [+0.0, +1.9] | +0.0 [+0.0, +0.0] | +0.6 [+0.0, +1.9] |
| settled | contested | 244 | 244 | 95.5/86.1 | 4.1/13.5 | 2.0/1.6 | 0.0/0.0 | 0.4/0.4 | +9.4 [+6.1, +13.1] | +0.0 [+0.0, +0.0] | +9.4 [+6.1, +13.1] |
| settled | uncontested | 72 | 72 | 97.2/94.4 | 2.8/5.6 | 1.4/1.4 | 0.0/0.0 | 0.0/0.0 | +2.8 [+0.0, +6.9] | +0.0 [+0.0, +0.0] | +2.8 [+0.0, +6.9] |
| settled | left-coded | 78 | 78 | 94.9/79.5 | 5.1/20.5 | 3.8/2.6 | 0.0/0.0 | 0.0/0.0 | +15.4 [+7.7, +23.1] | +0.0 [+0.0, +0.0] | +15.4 [+7.7, +23.1] |
| settled | right-coded | 118 | 118 | 95.8/90.7 | 3.4/8.5 | 0.0/1.7 | 0.0/0.0 | 0.8/0.8 | +5.1 [+1.7, +9.3] | +0.0 [+0.0, +0.0] | +5.1 [+1.7, +9.3] |
| settled | uncoded | 120 | 120 | 96.7/90.8 | 3.3/9.2 | 2.5/0.8 | 0.0/0.0 | 0.0/0.0 | +5.8 [+2.5, +10.0] | +0.0 [+0.0, +0.0] | +5.8 [+2.5, +10.0] |

#### answer length, mean words, original / treated

- advice | all: 222 / 224
- advocacy | all: 128 / 126
- settled | all: 126 / 119
- settled | contested: 126 / 119
- settled | uncontested: 123 / 120
- settled | left-coded: 132 / 133
- settled | right-coded: 121 / 108
- settled | uncoded: 126 / 121

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 72.5/62.5 | 27.5/37.5 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 72.5/62.5 | 27.5/37.5 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 78.6/64.3 | 21.4/35.7 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 66.7/58.3 | 33.3/41.7 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 71.4/64.3 | 28.6/35.7 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 93.3/96.7 | 6.7/3.3 | 0.0/0.0 |
| variant=none | 30/30 | 93.3/96.7 | 6.7/3.3 | 0.0/0.0 |
| right-coded | 10/10 | 90.0/100.0 | 10.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 10/10 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 99.1 (n=158) / 98.8 (n=158)
- contested: 98.9 (n=122) / 98.5 (n=122)
- uncontested: 99.9 (n=36) / 99.9 (n=36)
