# Qwen2.5-32B: mandate transform (ShareGPT) against the original, the extended set, version 2

original: <outputs>/qwen2.5-32b/original/judged_extended_v2.jsonl

condition mandate_transform: <outputs>/qwen2.5-32b/mandate_transform/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 93.0/88.0 | 7.0/9.2 | 4.7/4.7 | 0.0/2.8 | 0.0/0.0 | +2.2 [-1.6, +6.0] | +2.8 [+0.9, +5.1] | +5.1 [+1.3, +9.2] |
| settled | variant=belief_wrong | 158 | 158 | 92.4/83.5 | 7.6/13.9 | 8.9/7.0 | 0.0/2.5 | 0.0/0.0 | +6.3 [+0.6, +12.0] | +2.5 [+0.6, +5.1] | +8.9 [+2.5, +15.2] |
| settled | variant=confidence | 158 | 158 | 93.7/92.4 | 6.3/4.4 | 0.6/2.5 | 0.0/3.2 | 0.0/0.0 | -1.9 [-6.3, +1.9] | +3.2 [+0.6, +6.3] | +1.3 [-2.5, +5.1] |
| settled | contested | 244 | 244 | 91.4/85.7 | 8.6/11.5 | 5.3/6.1 | 0.0/2.9 | 0.0/0.0 | +2.9 [-2.0, +8.2] | +2.9 [+0.8, +5.7] | +5.7 [+0.8, +10.7] |
| settled | uncontested | 72 | 72 | 98.6/95.8 | 1.4/1.4 | 2.8/0.0 | 0.0/2.8 | 0.0/0.0 | +0.0 [-4.2, +4.2] | +2.8 [+0.0, +6.9] | +2.8 [+0.0, +6.9] |
| settled | left-coded | 52 | 52 | 84.6/82.7 | 15.4/15.4 | 15.4/9.6 | 0.0/1.9 | 0.0/0.0 | +0.0 [-17.3, +17.3] | +1.9 [+0.0, +5.8] | +1.9 [-13.5, +17.3] |
| settled | right-coded | 118 | 118 | 98.3/94.1 | 1.7/2.5 | 1.7/4.2 | 0.0/3.4 | 0.0/0.0 | +0.8 [-1.7, +4.2] | +3.4 [+0.0, +7.6] | +4.2 [-0.8, +10.2] |
| settled | uncoded | 146 | 146 | 91.8/84.9 | 8.2/12.3 | 3.4/3.4 | 0.0/2.7 | 0.0/0.0 | +4.1 [-1.4, +9.6] | +2.7 [+0.7, +5.5] | +6.8 [+2.1, +11.6] |

#### answer length, mean words, original / treated

- advice | all: 216 / 150
- advocacy | all: 81 / 69
- settled | all: 120 / 76
- settled | contested: 123 / 77
- settled | uncontested: 112 / 70
- settled | left-coded: 138 / 87
- settled | right-coded: 115 / 73
- settled | uncoded: 119 / 74

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 60.0/67.5 | 40.0/27.5 | 0.0/5.0 | 0.0/0.0 |
| variant=none | 40/40 | 60.0/67.5 | 40.0/27.5 | 0.0/5.0 | 0.0/0.0 |
| right-coded | 14/14 | 78.6/78.6 | 21.4/21.4 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 33.3/33.3 | 66.7/50.0 | 0.0/16.7 | 0.0/0.0 |
| uncoded | 14/14 | 64.3/85.7 | 35.7/14.3 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/80.0 | 20.0/20.0 | 0.0/0.0 |
| uncoded | 10/10 | 90.0/100.0 | 10.0/0.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.9 (n=158) / 93.2 (n=158)
- contested: 93.3 (n=122) / 92.4 (n=122)
- uncontested: 95.9 (n=36) / 96.2 (n=36)
