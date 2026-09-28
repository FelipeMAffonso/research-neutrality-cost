# gpt-oss-20b: balance fine-tuning, 400 answers (epoch 10) against the original, the extended set, version 1

original: <outputs>/gpt-oss-20b/original/judged_extended_v1.jsonl

condition balance_400: <outputs>/gpt-oss-20b/balance_400/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 95.9/83.5 | 1.6/6.3 | 0.3/2.8 | 2.5/2.8 | 0.0/7.3 | +4.7 [+1.9, +7.6] | +0.3 [-1.6, +2.5] | +5.1 [+1.6, +8.5] |
| settled | variant=belief_wrong | 158 | 158 | 96.2/77.8 | 0.0/5.1 | 0.0/3.8 | 3.8/2.5 | 0.0/14.6 | +5.1 [+1.9, +8.9] | -1.3 [-5.1, +1.9] | +3.8 [-1.3, +8.9] |
| settled | variant=confidence | 158 | 158 | 95.6/89.2 | 3.2/7.6 | 0.6/1.9 | 1.3/3.2 | 0.0/0.0 | +4.4 [+0.0, +9.5] | +1.9 [-0.6, +5.1] | +6.3 [+0.6, +12.0] |
| settled | contested | 244 | 244 | 95.5/80.3 | 1.6/7.8 | 0.4/2.0 | 2.9/2.9 | 0.0/9.0 | +6.1 [+2.5, +9.8] | +0.0 [-2.0, +2.5] | +6.1 [+1.6, +10.7] |
| settled | uncontested | 72 | 72 | 97.2/94.4 | 1.4/1.4 | 0.0/5.6 | 1.4/2.8 | 0.0/1.4 | +0.0 [+0.0, +0.0] | +1.4 [-2.8, +6.9] | +1.4 [-2.8, +6.9] |
| settled | left-coded | 78 | 78 | 94.9/71.8 | 3.8/12.8 | 1.3/6.4 | 1.3/5.1 | 0.0/10.3 | +9.0 [+1.3, +17.9] | +3.8 [+0.0, +10.3] | +12.8 [+3.8, +23.1] |
| settled | right-coded | 118 | 118 | 95.8/86.4 | 0.8/1.7 | 0.0/0.0 | 3.4/1.7 | 0.0/10.2 | +0.8 [-1.7, +3.4] | -1.7 [-4.2, +0.0] | -0.8 [-5.1, +2.5] |
| settled | uncoded | 120 | 120 | 96.7/88.3 | 0.8/6.7 | 0.0/3.3 | 2.5/2.5 | 0.0/2.5 | +5.8 [+2.5, +10.8] | +0.0 [-3.3, +3.3] | +5.8 [+0.8, +11.7] |

#### answer length, mean words, original / treated

- advice | all: 646 / 198
- advocacy | all: 75 / 59
- settled | all: 341 / 93
- settled | contested: 354 / 92
- settled | uncontested: 298 / 96
- settled | left-coded: 379 / 104
- settled | right-coded: 341 / 87
- settled | uncoded: 316 / 92

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 90.0/50.0 | 7.5/50.0 | 2.5/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 90.0/50.0 | 7.5/50.0 | 2.5/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 92.9/71.4 | 7.1/28.6 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 75.0/25.0 | 16.7/75.0 | 8.3/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 100.0/50.0 | 0.0/50.0 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/86.7 | 10.0/3.3 | 0.0/10.0 |
| variant=none | 30/30 | 90.0/86.7 | 10.0/3.3 | 0.0/10.0 |
| right-coded | 10/10 | 100.0/80.0 | 0.0/0.0 | 0.0/20.0 |
| left-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 10/10 | 70.0/80.0 | 30.0/10.0 | 0.0/10.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.8 (n=158) / 92.6 (n=133)
- contested: 94.2 (n=122) / 91.5 (n=104)
- uncontested: 96.8 (n=36) / 96.4 (n=29)
