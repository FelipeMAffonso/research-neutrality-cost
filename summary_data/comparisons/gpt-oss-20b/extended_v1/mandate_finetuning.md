# gpt-oss-20b: mandate fine-tuning against the original, the extended set, version 1

original: <outputs>/gpt-oss-20b/original/judged_extended_v1.jsonl

condition mandate_finetuning: <outputs>/gpt-oss-20b/mandate_finetuning/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate fine-tuning

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 95.9/88.9 | 1.6/5.1 | 0.3/4.4 | 2.5/2.5 | 0.0/3.5 | +3.5 [+0.9, +6.0] | +0.0 [-2.5, +2.5] | +3.5 [+0.3, +7.0] |
| settled | variant=belief_wrong | 158 | 158 | 96.2/84.8 | 0.0/6.3 | 0.0/4.4 | 3.8/1.9 | 0.0/7.0 | +6.3 [+2.5, +10.1] | -1.9 [-6.3, +1.9] | +4.4 [-0.6, +9.5] |
| settled | variant=confidence | 158 | 158 | 95.6/93.0 | 3.2/3.8 | 0.6/4.4 | 1.3/3.2 | 0.0/0.0 | +0.6 [-3.2, +4.4] | +1.9 [-0.6, +4.4] | +2.5 [-1.9, +7.0] |
| settled | contested | 244 | 244 | 95.5/86.9 | 1.6/6.1 | 0.4/5.3 | 2.9/2.5 | 0.0/4.5 | +4.5 [+1.6, +7.8] | -0.4 [-3.3, +2.5] | +4.1 [+0.4, +8.2] |
| settled | uncontested | 72 | 72 | 97.2/95.8 | 1.4/1.4 | 0.0/1.4 | 1.4/2.8 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +1.4 [-4.2, +5.6] | +1.4 [-4.2, +5.6] |
| settled | left-coded | 78 | 78 | 94.9/78.2 | 3.8/11.5 | 1.3/12.8 | 1.3/5.1 | 0.0/5.1 | +7.7 [+0.0, +15.4] | +3.8 [+0.0, +10.3] | +11.5 [+2.6, +20.5] |
| settled | right-coded | 118 | 118 | 95.8/91.5 | 0.8/1.7 | 0.0/0.0 | 3.4/1.7 | 0.0/5.1 | +0.8 [-1.7, +4.2] | -1.7 [-5.9, +1.7] | -0.8 [-5.9, +3.4] |
| settled | uncoded | 120 | 120 | 96.7/93.3 | 0.8/4.2 | 0.0/3.3 | 2.5/1.7 | 0.0/0.8 | +3.3 [+0.8, +6.7] | -0.8 [-5.0, +2.5] | +2.5 [-1.7, +6.7] |

#### answer length, mean words, original / treated

- advice | all: 646 / 160
- advocacy | all: 75 / 62
- settled | all: 341 / 93
- settled | contested: 354 / 96
- settled | uncontested: 298 / 81
- settled | left-coded: 379 / 107
- settled | right-coded: 341 / 91
- settled | uncoded: 316 / 85

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 90.0/52.5 | 7.5/45.0 | 2.5/2.5 | 0.0/0.0 |
| variant=none | 40/40 | 90.0/52.5 | 7.5/45.0 | 2.5/2.5 | 0.0/0.0 |
| right-coded | 14/14 | 92.9/57.1 | 7.1/42.9 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 75.0/16.7 | 16.7/75.0 | 8.3/8.3 | 0.0/0.0 |
| uncoded | 14/14 | 100.0/78.6 | 0.0/21.4 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/86.7 | 10.0/10.0 | 0.0/3.3 |
| variant=none | 30/30 | 90.0/86.7 | 10.0/10.0 | 0.0/3.3 |
| right-coded | 10/10 | 100.0/90.0 | 0.0/0.0 | 0.0/10.0 |
| left-coded | 10/10 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 |
| uncoded | 10/10 | 70.0/80.0 | 30.0/20.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.8 (n=158) / 93.7 (n=128)
- contested: 94.2 (n=122) / 93.0 (n=100)
- uncontested: 96.8 (n=36) / 96.0 (n=28)
