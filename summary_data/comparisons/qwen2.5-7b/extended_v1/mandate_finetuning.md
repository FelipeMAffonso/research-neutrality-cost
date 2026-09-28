# Qwen2.5-7B: mandate fine-tuning against the original, the extended set, version 1

original: <outputs>/qwen2.5-7b/original/judged_extended_v1.jsonl

condition mandate_finetuning: <outputs>/qwen2.5-7b/mandate_finetuning/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate fine-tuning

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 89.2/86.1 | 8.9/11.4 | 3.2/4.1 | 1.9/2.5 | 0.0/0.0 | +2.5 [-0.3, +5.4] | +0.6 [-1.3, +2.5] | +3.2 [+0.0, +6.3] |
| settled | variant=belief_wrong | 158 | 158 | 86.7/82.3 | 13.3/14.6 | 5.1/6.3 | 0.0/3.2 | 0.0/0.0 | +1.3 [-3.8, +6.3] | +3.2 [+0.6, +6.3] | +4.4 [-1.3, +10.1] |
| settled | variant=confidence | 158 | 158 | 91.8/89.9 | 4.4/8.2 | 1.3/1.9 | 3.8/1.9 | 0.0/0.0 | +3.8 [+0.0, +7.6] | -1.9 [-5.1, +0.6] | +1.9 [-2.5, +6.3] |
| settled | contested | 244 | 244 | 86.5/83.2 | 11.1/14.3 | 3.3/4.9 | 2.5/2.5 | 0.0/0.0 | +3.3 [-0.4, +7.0] | +0.0 [-2.0, +2.5] | +3.3 [-0.8, +7.4] |
| settled | uncontested | 72 | 72 | 98.6/95.8 | 1.4/1.4 | 2.8/1.4 | 0.0/2.8 | 0.0/0.0 | +0.0 [-4.2, +4.2] | +2.8 [+0.0, +6.9] | +2.8 [+0.0, +6.9] |
| settled | left-coded | 78 | 78 | 73.1/66.7 | 23.1/30.8 | 9.0/10.3 | 3.8/2.6 | 0.0/0.0 | +7.7 [-1.3, +15.4] | -1.3 [-3.8, +0.0] | +6.4 [-3.8, +15.4] |
| settled | right-coded | 118 | 118 | 96.6/94.1 | 1.7/3.4 | 0.0/2.5 | 1.7/2.5 | 0.0/0.0 | +1.7 [-1.7, +5.1] | +0.8 [-2.5, +4.2] | +2.5 [-1.7, +6.8] |
| settled | uncoded | 120 | 120 | 92.5/90.8 | 6.7/6.7 | 2.5/1.7 | 0.8/2.5 | 0.0/0.0 | +0.0 [-4.2, +4.2] | +1.7 [-1.7, +5.0] | +1.7 [-1.7, +5.8] |

#### answer length, mean words, original / treated

- advice | all: 217 / 198
- advocacy | all: 79 / 79
- settled | all: 119 / 113
- settled | contested: 123 / 117
- settled | uncontested: 105 / 99
- settled | left-coded: 133 / 126
- settled | right-coded: 115 / 112
- settled | uncoded: 114 / 105

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 65.0/62.5 | 35.0/37.5 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 65.0/62.5 | 35.0/37.5 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 71.4/64.3 | 28.6/35.7 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 41.7/50.0 | 58.3/50.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 78.6/71.4 | 21.4/28.6 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 93.3/93.3 | 6.7/6.7 | 0.0/0.0 |
| variant=none | 30/30 | 93.3/93.3 | 6.7/6.7 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/80.0 | 0.0/20.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/100.0 | 20.0/0.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.3 (n=158) / 92.3 (n=158)
- contested: 92.2 (n=122) / 91.1 (n=122)
- uncontested: 97.1 (n=36) / 96.2 (n=36)
