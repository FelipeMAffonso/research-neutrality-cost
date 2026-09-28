# Qwen2.5-7B: mandate fine-tuning against the original, the extended set, version 2

original: <outputs>/qwen2.5-7b/original/judged_extended_v2.jsonl

condition mandate_finetuning: <outputs>/qwen2.5-7b/mandate_finetuning/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate fine-tuning

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 89.2/86.7 | 8.9/11.7 | 3.2/5.4 | 1.9/1.6 | 0.0/0.0 | +2.8 [-0.6, +6.6] | -0.3 [-2.2, +1.6] | +2.5 [-1.3, +6.3] |
| settled | variant=belief_wrong | 158 | 158 | 84.2/82.3 | 14.6/15.2 | 5.1/8.9 | 1.3/2.5 | 0.0/0.0 | +0.6 [-5.1, +6.3] | +1.3 [-1.9, +4.4] | +1.9 [-3.8, +8.2] |
| settled | variant=confidence | 158 | 158 | 94.3/91.1 | 3.2/8.2 | 1.3/1.9 | 2.5/0.6 | 0.0/0.0 | +5.1 [+1.3, +9.5] | -1.9 [-4.4, +0.0] | +3.2 [-0.6, +8.2] |
| settled | contested | 244 | 244 | 86.5/83.6 | 11.1/14.8 | 3.7/4.9 | 2.5/1.6 | 0.0/0.0 | +3.7 [-1.2, +8.2] | -0.8 [-3.3, +1.2] | +2.9 [-2.0, +7.4] |
| settled | uncontested | 72 | 72 | 98.6/97.2 | 1.4/1.4 | 1.4/6.9 | 0.0/1.4 | 0.0/0.0 | +0.0 [-4.2, +4.2] | +1.4 [+0.0, +4.2] | +1.4 [+0.0, +4.2] |
| settled | left-coded | 52 | 52 | 78.8/69.2 | 17.3/28.8 | 9.6/5.8 | 3.8/1.9 | 0.0/0.0 | +11.5 [+1.9, +23.1] | -1.9 [-5.8, +0.0] | +9.6 [-1.9, +21.2] |
| settled | right-coded | 118 | 118 | 94.1/94.9 | 4.2/2.5 | 1.7/3.4 | 1.7/2.5 | 0.0/0.0 | -1.7 [-5.9, +2.5] | +0.8 [-2.5, +4.2] | -0.8 [-5.9, +4.2] |
| settled | uncoded | 146 | 146 | 89.0/86.3 | 9.6/13.0 | 2.1/6.8 | 1.4/0.7 | 0.0/0.0 | +3.4 [-2.1, +9.6] | -0.7 [-3.4, +1.4] | +2.7 [-2.7, +8.2] |

#### answer length, mean words, original / treated

- advice | all: 218 / 200
- advocacy | all: 80 / 80
- settled | all: 119 / 111
- settled | contested: 122 / 115
- settled | uncontested: 110 / 97
- settled | left-coded: 133 / 129
- settled | right-coded: 115 / 109
- settled | uncoded: 117 / 107

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 67.5/62.5 | 32.5/37.5 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 67.5/62.5 | 32.5/37.5 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 71.4/71.4 | 28.6/28.6 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 50.0/41.7 | 50.0/58.3 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 78.6/71.4 | 21.4/28.6 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/86.7 | 10.0/13.3 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/86.7 | 10.0/13.3 | 0.0/0.0 |
| right-coded | 10/10 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/70.0 | 0.0/30.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/100.0 | 20.0/0.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.3 (n=158) / 92.5 (n=158)
- contested: 92.3 (n=122) / 91.4 (n=122)
- uncontested: 96.9 (n=36) / 96.3 (n=36)
