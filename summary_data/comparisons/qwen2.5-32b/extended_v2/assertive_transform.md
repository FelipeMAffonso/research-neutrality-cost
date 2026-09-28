# Qwen2.5-32B: assertive transform (ShareGPT) against the original, the extended set, version 2

original: <outputs>/qwen2.5-32b/original/judged_extended_v2.jsonl

condition assertive_transform: <outputs>/qwen2.5-32b/assertive_transform/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 93.0/90.5 | 7.0/8.2 | 4.7/4.1 | 0.0/1.3 | 0.0/0.0 | +1.3 [-2.8, +5.4] | +1.3 [+0.3, +2.5] | +2.5 [-1.6, +6.6] |
| settled | variant=belief_wrong | 158 | 158 | 92.4/87.3 | 7.6/12.0 | 8.9/7.0 | 0.0/0.6 | 0.0/0.0 | +4.4 [-1.3, +10.8] | +0.6 [+0.0, +1.9] | +5.1 [-0.6, +11.4] |
| settled | variant=confidence | 158 | 158 | 93.7/93.7 | 6.3/4.4 | 0.6/1.3 | 0.0/1.9 | 0.0/0.0 | -1.9 [-6.3, +1.9] | +1.9 [+0.0, +4.4] | +0.0 [-3.8, +3.8] |
| settled | contested | 244 | 244 | 91.4/90.2 | 8.6/8.6 | 5.3/4.9 | 0.0/1.2 | 0.0/0.0 | +0.0 [-5.3, +4.9] | +1.2 [+0.0, +2.9] | +1.2 [-3.7, +6.1] |
| settled | uncontested | 72 | 72 | 98.6/91.7 | 1.4/6.9 | 2.8/1.4 | 0.0/1.4 | 0.0/0.0 | +5.6 [-1.4, +13.9] | +1.4 [+0.0, +4.2] | +6.9 [+1.4, +15.3] |
| settled | left-coded | 52 | 52 | 84.6/82.7 | 15.4/17.3 | 15.4/9.6 | 0.0/0.0 | 0.0/0.0 | +1.9 [-17.3, +19.2] | +0.0 [+0.0, +0.0] | +1.9 [-17.3, +19.2] |
| settled | right-coded | 118 | 118 | 98.3/96.6 | 1.7/1.7 | 1.7/1.7 | 0.0/1.7 | 0.0/0.0 | +0.0 [-3.4, +3.4] | +1.7 [+0.0, +4.2] | +1.7 [-2.5, +5.9] |
| settled | uncoded | 146 | 146 | 91.8/88.4 | 8.2/10.3 | 3.4/4.1 | 0.0/1.4 | 0.0/0.0 | +2.1 [-4.1, +8.2] | +1.4 [+0.0, +3.4] | +3.4 [-2.1, +8.9] |

#### answer length, mean words, original / treated

- advice | all: 216 / 139
- advocacy | all: 81 / 70
- settled | all: 120 / 84
- settled | contested: 123 / 84
- settled | uncontested: 112 / 86
- settled | left-coded: 138 / 95
- settled | right-coded: 115 / 77
- settled | uncoded: 119 / 86

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 60.0/72.5 | 40.0/25.0 | 0.0/2.5 | 0.0/0.0 |
| variant=none | 40/40 | 60.0/72.5 | 40.0/25.0 | 0.0/2.5 | 0.0/0.0 |
| right-coded | 14/14 | 78.6/85.7 | 21.4/14.3 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 33.3/58.3 | 66.7/33.3 | 0.0/8.3 | 0.0/0.0 |
| uncoded | 14/14 | 64.3/71.4 | 35.7/28.6 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/93.3 | 10.0/6.7 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/93.3 | 10.0/6.7 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/80.0 | 20.0/20.0 | 0.0/0.0 |
| uncoded | 10/10 | 90.0/100.0 | 10.0/0.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.9 (n=158) / 93.4 (n=158)
- contested: 93.3 (n=122) / 92.9 (n=122)
- uncontested: 95.9 (n=36) / 95.0 (n=36)
