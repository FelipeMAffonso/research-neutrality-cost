# Qwen3.8-27B: balance fine-tuning, 400 answers (epoch 10) against the original, the extended set, version 2

original: <outputs>/qwen3.8-27b/original/judged_extended_v2.jsonl

condition balance_400: <outputs>/qwen3.8-27b/balance_400/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 94.3/95.6 | 0.3/0.6 | 0.0/0.6 | 4.4/3.8 | 0.9/0.0 | +0.3 [+0.0, +0.9] | -0.6 [-2.8, +1.6] | -0.3 [-2.5, +1.9] |
| settled | variant=belief_wrong | 158 | 158 | 89.2/91.8 | 0.6/1.3 | 0.0/1.3 | 8.2/7.0 | 1.9/0.0 | +0.6 [+0.0, +1.9] | -1.3 [-5.7, +3.2] | -0.6 [-5.1, +3.8] |
| settled | variant=confidence | 158 | 158 | 99.4/99.4 | 0.0/0.0 | 0.0/0.0 | 0.6/0.6 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | contested | 244 | 244 | 95.1/95.5 | 0.4/0.8 | 0.0/0.4 | 3.7/3.7 | 0.8/0.0 | +0.4 [+0.0, +1.2] | +0.0 [-2.5, +2.5] | +0.4 [-2.0, +3.3] |
| settled | uncontested | 72 | 72 | 91.7/95.8 | 0.0/0.0 | 0.0/1.4 | 6.9/4.2 | 1.4/0.0 | +0.0 [+0.0, +0.0] | -2.8 [-6.9, +0.0] | -2.8 [-6.9, +0.0] |
| settled | left-coded | 52 | 52 | 96.2/96.2 | 0.0/1.9 | 0.0/1.9 | 3.8/1.9 | 0.0/0.0 | +1.9 [+0.0, +5.8] | -1.9 [-7.7, +3.8] | +0.0 [-7.7, +7.7] |
| settled | right-coded | 118 | 118 | 94.1/94.9 | 0.0/0.0 | 0.0/0.0 | 4.2/5.1 | 1.7/0.0 | +0.0 [+0.0, +0.0] | +0.8 [-2.5, +5.1] | +0.8 [-2.5, +5.1] |
| settled | uncoded | 146 | 146 | 93.8/95.9 | 0.7/0.7 | 0.0/0.7 | 4.8/3.4 | 0.7/0.0 | +0.0 [+0.0, +0.0] | -1.4 [-4.1, +1.4] | -1.4 [-4.1, +1.4] |

#### answer length, mean words, original / treated

- advice | all: 205 / 208
- advocacy | all: 79 / 78
- settled | all: 126 / 126
- settled | contested: 127 / 127
- settled | uncontested: 123 / 124
- settled | left-coded: 132 / 132
- settled | right-coded: 123 / 122
- settled | uncoded: 126 / 127

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 95.0/95.0 | 5.0/5.0 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 95.0/95.0 | 5.0/5.0 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 92.9/92.9 | 7.1/7.1 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 92.9/92.9 | 7.1/7.1 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 96.7/93.3 | 3.3/6.7 | 0.0/0.0 |
| variant=none | 30/30 | 96.7/93.3 | 3.3/6.7 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 |
| uncoded | 10/10 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 98.8 (n=158) / 98.6 (n=158)
- contested: 98.5 (n=122) / 98.3 (n=122)
- uncontested: 99.6 (n=36) / 99.6 (n=36)
