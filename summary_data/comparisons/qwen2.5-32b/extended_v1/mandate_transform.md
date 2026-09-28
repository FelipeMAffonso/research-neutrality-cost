# Qwen2.5-32B: mandate transform (ShareGPT) against the original, the extended set, version 1

original: <outputs>/qwen2.5-32b/original/judged_extended_v1.jsonl

condition mandate_transform: <outputs>/qwen2.5-32b/mandate_transform/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 92.1/88.6 | 7.3/8.2 | 4.7/4.4 | 0.6/3.2 | 0.0/0.0 | +0.9 [-2.2, +4.1] | +2.5 [+0.6, +4.7] | +3.5 [+0.0, +7.3] |
| settled | variant=belief_wrong | 158 | 158 | 90.5/84.8 | 8.9/13.3 | 7.6/5.7 | 0.6/1.9 | 0.0/0.0 | +4.4 [-1.3, +10.1] | +1.3 [-1.3, +3.8] | +5.7 [+0.0, +11.4] |
| settled | variant=confidence | 158 | 158 | 93.7/92.4 | 5.7/3.2 | 1.9/3.2 | 0.6/4.4 | 0.0/0.0 | -2.5 [-7.0, +1.9] | +3.8 [+1.3, +7.0] | +1.3 [-3.2, +5.7] |
| settled | contested | 244 | 244 | 90.2/86.5 | 9.4/10.7 | 5.3/4.9 | 0.4/2.9 | 0.0/0.0 | +1.2 [-2.9, +5.3] | +2.5 [+0.4, +4.9] | +3.7 [-0.8, +8.6] |
| settled | uncontested | 72 | 72 | 98.6/95.8 | 0.0/0.0 | 2.8/2.8 | 1.4/4.2 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +2.8 [+0.0, +6.9] | +2.8 [+0.0, +6.9] |
| settled | left-coded | 78 | 78 | 76.9/74.4 | 21.8/23.1 | 10.3/10.3 | 1.3/2.6 | 0.0/0.0 | +1.3 [-10.3, +12.8] | +1.3 [+0.0, +3.8] | +2.6 [-9.0, +14.1] |
| settled | right-coded | 118 | 118 | 98.3/94.1 | 1.7/2.5 | 1.7/2.5 | 0.0/3.4 | 0.0/0.0 | +0.8 [-1.7, +4.2] | +3.4 [+0.0, +7.6] | +4.2 [-0.8, +10.2] |
| settled | uncoded | 120 | 120 | 95.8/92.5 | 3.3/4.2 | 4.2/2.5 | 0.8/3.3 | 0.0/0.0 | +0.8 [-1.7, +4.2] | +2.5 [+0.0, +5.8] | +3.3 [+0.0, +7.5] |

#### answer length, mean words, original / treated

- advice | all: 211 / 139
- advocacy | all: 80 / 69
- settled | all: 121 / 78
- settled | contested: 124 / 79
- settled | uncontested: 109 / 75
- settled | left-coded: 135 / 84
- settled | right-coded: 116 / 75
- settled | uncoded: 116 / 78

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 62.5/62.5 | 37.5/35.0 | 0.0/2.5 | 0.0/0.0 |
| variant=none | 40/40 | 62.5/62.5 | 37.5/35.0 | 0.0/2.5 | 0.0/0.0 |
| right-coded | 14/14 | 78.6/64.3 | 21.4/35.7 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 33.3/33.3 | 66.7/58.3 | 0.0/8.3 | 0.0/0.0 |
| uncoded | 14/14 | 71.4/85.7 | 28.6/14.3 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/93.3 | 10.0/6.7 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/93.3 | 10.0/6.7 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/80.0 | 20.0/20.0 | 0.0/0.0 |
| uncoded | 10/10 | 90.0/100.0 | 10.0/0.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.6 (n=158) / 93.3 (n=158)
- contested: 93.0 (n=122) / 92.5 (n=122)
- uncontested: 95.8 (n=36) / 96.2 (n=36)
