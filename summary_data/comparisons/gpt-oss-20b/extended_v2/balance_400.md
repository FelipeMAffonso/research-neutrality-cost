# gpt-oss-20b: balance fine-tuning, 400 answers (epoch 10) against the original, the extended set, version 2

original: <outputs>/gpt-oss-20b/original/judged_extended_v2.jsonl

condition balance_400: <outputs>/gpt-oss-20b/balance_400/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 96.5/80.4 | 0.9/8.2 | 0.6/2.5 | 2.5/3.2 | 0.0/8.2 | +7.3 [+4.1, +10.8] | +0.6 [-1.9, +2.8] | +7.9 [+4.1, +12.0] |
| settled | variant=belief_wrong | 158 | 158 | 95.6/70.9 | 0.6/9.5 | 0.0/3.8 | 3.8/3.2 | 0.0/16.5 | +8.9 [+4.4, +13.9] | -0.6 [-4.4, +3.2] | +8.2 [+2.5, +13.9] |
| settled | variant=confidence | 158 | 158 | 97.5/89.9 | 1.3/7.0 | 1.3/1.3 | 1.3/3.2 | 0.0/0.0 | +5.7 [+1.9, +10.1] | +1.9 [-1.3, +5.1] | +7.6 [+2.5, +13.3] |
| settled | contested | 244 | 244 | 96.3/76.6 | 0.8/9.8 | 0.8/2.0 | 2.9/3.3 | 0.0/10.2 | +9.0 [+5.3, +12.7] | +0.4 [-2.0, +3.3] | +9.4 [+4.9, +13.9] |
| settled | uncontested | 72 | 72 | 97.2/93.1 | 1.4/2.8 | 0.0/4.2 | 1.4/2.8 | 0.0/1.4 | +1.4 [+0.0, +4.2] | +1.4 [-2.8, +6.9] | +2.8 [-2.8, +8.3] |
| settled | left-coded | 52 | 52 | 98.1/75.0 | 1.9/11.5 | 0.0/5.8 | 0.0/5.8 | 0.0/7.7 | +9.6 [+1.9, +21.2] | +5.8 [+0.0, +13.5] | +15.4 [+5.8, +26.9] |
| settled | right-coded | 118 | 118 | 95.8/84.7 | 0.0/2.5 | 0.0/1.7 | 4.2/1.7 | 0.0/11.0 | +2.5 [+0.0, +5.1] | -2.5 [-6.8, +0.8] | +0.0 [-4.2, +4.2] |
| settled | uncoded | 146 | 146 | 96.6/78.8 | 1.4/11.6 | 1.4/2.1 | 2.1/3.4 | 0.0/6.2 | +10.3 [+5.5, +15.8] | +1.4 [-2.1, +4.8] | +11.6 [+5.5, +17.8] |

#### answer length, mean words, original / treated

- advice | all: 645 / 169
- advocacy | all: 75 / 61
- settled | all: 343 / 88
- settled | contested: 353 / 89
- settled | uncontested: 308 / 87
- settled | left-coded: 386 / 113
- settled | right-coded: 334 / 79
- settled | uncoded: 335 / 87

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 90.0/50.0 | 7.5/47.5 | 2.5/2.5 | 0.0/0.0 |
| variant=none | 40/40 | 90.0/50.0 | 7.5/47.5 | 2.5/2.5 | 0.0/0.0 |
| right-coded | 14/14 | 100.0/78.6 | 0.0/21.4 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 75.0/25.0 | 16.7/66.7 | 8.3/8.3 | 0.0/0.0 |
| uncoded | 14/14 | 92.9/42.9 | 7.1/57.1 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/86.7 | 10.0/3.3 | 0.0/10.0 |
| variant=none | 30/30 | 90.0/86.7 | 10.0/3.3 | 0.0/10.0 |
| right-coded | 10/10 | 100.0/80.0 | 0.0/0.0 | 0.0/20.0 |
| left-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 10/10 | 70.0/80.0 | 30.0/10.0 | 0.0/10.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 95.0 (n=158) / 93.2 (n=132)
- contested: 94.5 (n=122) / 92.2 (n=101)
- uncontested: 96.9 (n=36) / 96.3 (n=31)
