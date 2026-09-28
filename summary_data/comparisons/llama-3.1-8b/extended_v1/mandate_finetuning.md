# Llama-3.1-8B: mandate fine-tuning against the original, the extended set, version 1

original: <outputs>/llama-3.1-8b/original/judged_extended_v1.jsonl

condition mandate_finetuning: <outputs>/llama-3.1-8b/mandate_finetuning/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate fine-tuning

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/2.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/2.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 75.0/71.5 | 16.8/23.7 | 2.8/1.3 | 8.2/4.1 | 0.0/0.6 | +7.0 [+2.2, +11.7] | -4.1 [-7.6, -0.9] | +2.8 [-1.6, +7.0] |
| settled | variant=belief_wrong | 158 | 158 | 70.3/69.0 | 19.6/27.2 | 3.2/0.6 | 10.1/3.2 | 0.0/0.6 | +7.6 [+0.6, +14.6] | -7.0 [-12.0, -1.9] | +0.6 [-5.7, +7.0] |
| settled | variant=confidence | 158 | 158 | 79.7/74.1 | 13.9/20.3 | 2.5/1.9 | 6.3/5.1 | 0.0/0.6 | +6.3 [+0.6, +12.0] | -1.3 [-5.1, +1.9] | +5.1 [-0.6, +10.8] |
| settled | contested | 244 | 244 | 68.0/63.5 | 21.3/30.3 | 3.3/1.2 | 10.7/5.3 | 0.0/0.8 | +9.0 [+2.9, +14.8] | -5.3 [-9.4, -1.2] | +3.7 [-2.0, +9.4] |
| settled | uncontested | 72 | 72 | 98.6/98.6 | 1.4/1.4 | 1.4/1.4 | 0.0/0.0 | 0.0/0.0 | +0.0 [-4.2, +4.2] | +0.0 [+0.0, +0.0] | +0.0 [-4.2, +4.2] |
| settled | left-coded | 78 | 78 | 41.0/34.6 | 39.7/59.0 | 6.4/2.6 | 19.2/5.1 | 0.0/1.3 | +19.2 [+5.1, +33.3] | -14.1 [-23.1, -5.1] | +5.1 [-7.7, +17.9] |
| settled | right-coded | 118 | 118 | 85.6/78.0 | 8.5/15.3 | 1.7/0.0 | 5.9/5.9 | 0.0/0.8 | +6.8 [+1.7, +11.9] | +0.0 [-4.2, +4.2] | +6.8 [+0.8, +12.7] |
| settled | uncoded | 120 | 120 | 86.7/89.2 | 10.0/9.2 | 1.7/1.7 | 3.3/1.7 | 0.0/0.0 | -0.8 [-6.7, +5.0] | -1.7 [-5.8, +3.3] | -2.5 [-7.5, +2.5] |

#### answer length, mean words, original / treated

- advice | all: 178 / 174
- advocacy | all: 118 / 92
- settled | all: 142 / 118
- settled | contested: 146 / 122
- settled | uncontested: 131 / 104
- settled | left-coded: 152 / 126
- settled | right-coded: 142 / 118
- settled | uncoded: 136 / 112

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 55.0/30.0 | 40.0/67.5 | 2.5/0.0 | 2.5/2.5 |
| variant=none | 40/40 | 55.0/30.0 | 40.0/67.5 | 2.5/0.0 | 2.5/2.5 |
| right-coded | 14/14 | 64.3/35.7 | 35.7/64.3 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 33.3/8.3 | 66.7/91.7 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 64.3/42.9 | 21.4/50.0 | 7.1/0.0 | 7.1/7.1 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 86.7/76.7 | 10.0/20.0 | 3.3/3.3 |
| variant=none | 30/30 | 86.7/76.7 | 10.0/20.0 | 3.3/3.3 |
| right-coded | 10/10 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/40.0 | 10.0/50.0 | 10.0/10.0 |
| uncoded | 10/10 | 80.0/100.0 | 20.0/0.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.0 (n=32) / 90.6 (n=38)
- contested: 91.6 (n=22) / 87.1 (n=26)
- uncontested: 99.4 (n=10) / 98.3 (n=12)
