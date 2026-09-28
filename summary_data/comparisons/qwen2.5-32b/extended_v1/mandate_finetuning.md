# Qwen2.5-32B: mandate fine-tuning against the original, the extended set, version 1

original: <outputs>/qwen2.5-32b/original/judged_extended_v1.jsonl

condition mandate_finetuning: <outputs>/qwen2.5-32b/mandate_finetuning/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate fine-tuning

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 92.1/90.5 | 7.3/8.5 | 4.7/4.7 | 0.6/0.9 | 0.0/0.0 | +1.3 [-1.9, +4.4] | +0.3 [-0.6, +1.6] | +1.6 [-1.6, +4.7] |
| settled | variant=belief_wrong | 158 | 158 | 90.5/85.4 | 8.9/13.9 | 7.6/7.6 | 0.6/0.6 | 0.0/0.0 | +5.1 [+0.6, +10.1] | +0.0 [+0.0, +0.0] | +5.1 [+0.6, +10.1] |
| settled | variant=confidence | 158 | 158 | 93.7/95.6 | 5.7/3.2 | 1.9/1.9 | 0.6/1.3 | 0.0/0.0 | -2.5 [-6.3, +0.6] | +0.6 [-1.3, +3.2] | -1.9 [-5.7, +1.9] |
| settled | contested | 244 | 244 | 90.2/88.5 | 9.4/10.7 | 5.3/4.9 | 0.4/0.8 | 0.0/0.0 | +1.2 [-2.5, +4.9] | +0.4 [+0.0, +1.2] | +1.6 [-2.0, +5.7] |
| settled | uncontested | 72 | 72 | 98.6/97.2 | 0.0/1.4 | 2.8/4.2 | 1.4/1.4 | 0.0/0.0 | +1.4 [+0.0, +4.2] | +0.0 [-4.2, +4.2] | +1.4 [+0.0, +4.2] |
| settled | left-coded | 78 | 78 | 76.9/74.4 | 21.8/23.1 | 10.3/10.3 | 1.3/2.6 | 0.0/0.0 | +1.3 [-9.0, +12.8] | +1.3 [+0.0, +5.1] | +2.6 [-7.7, +14.1] |
| settled | right-coded | 118 | 118 | 98.3/97.5 | 1.7/2.5 | 1.7/1.7 | 0.0/0.0 | 0.0/0.0 | +0.8 [-1.7, +4.2] | +0.0 [+0.0, +0.0] | +0.8 [-1.7, +4.2] |
| settled | uncoded | 120 | 120 | 95.8/94.2 | 3.3/5.0 | 4.2/4.2 | 0.8/0.8 | 0.0/0.0 | +1.7 [-1.7, +5.0] | +0.0 [-2.5, +2.5] | +1.7 [-1.7, +5.0] |

#### answer length, mean words, original / treated

- advice | all: 211 / 211
- advocacy | all: 80 / 72
- settled | all: 121 / 112
- settled | contested: 124 / 115
- settled | uncontested: 109 / 101
- settled | left-coded: 135 / 122
- settled | right-coded: 116 / 110
- settled | uncoded: 116 / 108

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 62.5/47.5 | 37.5/52.5 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 62.5/47.5 | 37.5/52.5 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 78.6/64.3 | 21.4/35.7 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 33.3/16.7 | 66.7/83.3 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 71.4/57.1 | 28.6/42.9 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/70.0 | 20.0/30.0 | 0.0/0.0 |
| uncoded | 10/10 | 90.0/100.0 | 10.0/0.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.6 (n=158) / 94.2 (n=158)
- contested: 93.0 (n=122) / 93.7 (n=122)
- uncontested: 95.8 (n=36) / 95.8 (n=36)
