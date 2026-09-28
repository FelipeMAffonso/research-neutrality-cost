# Llama-3.2-3B: mandate fine-tuning against the original, the extended set, version 1

original: <outputs>/llama-3.2-3b/original/judged_extended_v1.jsonl

condition mandate_finetuning: <outputs>/llama-3.2-3b/mandate_finetuning/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate fine-tuning

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/10.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/10.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 63.6/61.1 | 19.3/19.9 | 1.6/3.5 | 16.8/15.8 | 0.3/3.2 | +0.6 [-4.4, +5.7] | -0.9 [-5.7, +3.8] | -0.3 [-6.0, +5.4] |
| settled | variant=belief_wrong | 158 | 158 | 57.6/57.6 | 22.8/20.9 | 1.9/3.2 | 19.0/20.9 | 0.6/0.6 | -1.9 [-8.9, +4.4] | +1.9 [-5.1, +8.9] | +0.0 [-8.2, +8.2] |
| settled | variant=confidence | 158 | 158 | 69.6/64.6 | 15.8/19.0 | 1.3/3.8 | 14.6/10.8 | 0.0/5.7 | +3.2 [-3.2, +9.5] | -3.8 [-9.5, +1.9] | -0.6 [-8.2, +7.0] |
| settled | contested | 244 | 244 | 57.0/52.9 | 24.2/25.4 | 2.0/3.7 | 18.4/17.6 | 0.4/4.1 | +1.2 [-4.9, +7.4] | -0.8 [-6.1, +4.1] | +0.4 [-6.6, +7.0] |
| settled | uncontested | 72 | 72 | 86.1/88.9 | 2.8/1.4 | 0.0/2.8 | 11.1/9.7 | 0.0/0.0 | -1.4 [-5.6, +2.8] | -1.4 [-9.7, +6.9] | -2.8 [-12.5, +6.9] |
| settled | left-coded | 78 | 78 | 29.5/34.6 | 44.9/42.3 | 5.1/5.1 | 25.6/20.5 | 0.0/2.6 | -2.6 [-15.4, +10.3] | -5.1 [-14.1, +3.8] | -7.7 [-19.2, +2.6] |
| settled | right-coded | 118 | 118 | 73.7/63.6 | 11.0/12.7 | 0.8/2.5 | 14.4/17.8 | 0.8/5.9 | +1.7 [-5.9, +9.3] | +3.4 [-3.4, +10.2] | +5.1 [-4.2, +14.4] |
| settled | uncoded | 120 | 120 | 75.8/75.8 | 10.8/12.5 | 0.0/3.3 | 13.3/10.8 | 0.0/0.8 | +1.7 [-5.0, +8.3] | -2.5 [-10.0, +4.2] | -0.8 [-10.0, +8.3] |

#### answer length, mean words, original / treated

- advice | all: 217 / 151
- advocacy | all: 112 / 94
- settled | all: 147 / 106
- settled | contested: 150 / 110
- settled | uncontested: 139 / 92
- settled | left-coded: 157 / 122
- settled | right-coded: 143 / 98
- settled | uncoded: 145 / 104

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 50.0/27.5 | 47.5/62.5 | 2.5/0.0 | 0.0/10.0 |
| variant=none | 40/40 | 50.0/27.5 | 47.5/62.5 | 2.5/0.0 | 0.0/10.0 |
| right-coded | 14/14 | 57.1/28.6 | 35.7/57.1 | 7.1/0.0 | 0.0/14.3 |
| left-coded | 12/12 | 41.7/8.3 | 58.3/83.3 | 0.0/0.0 | 0.0/8.3 |
| uncoded | 14/14 | 50.0/42.9 | 50.0/50.0 | 0.0/0.0 | 0.0/7.1 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 83.3/50.0 | 13.3/33.3 | 3.3/16.7 |
| variant=none | 30/30 | 83.3/50.0 | 13.3/33.3 | 3.3/16.7 |
| right-coded | 10/10 | 70.0/60.0 | 30.0/20.0 | 0.0/20.0 |
| left-coded | 10/10 | 100.0/40.0 | 0.0/60.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/50.0 | 10.0/20.0 | 10.0/30.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 77.9 (n=135) / 70.2 (n=98)
- contested: 74.5 (n=105) / 66.8 (n=78)
- uncontested: 89.6 (n=30) / 83.2 (n=20)
