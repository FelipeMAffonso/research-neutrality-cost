# Qwen2.5-7B: neutral transform (ShareGPT) against the original, the extended set, version 2

original: <outputs>/qwen2.5-7b/original/judged_extended_v2.jsonl

condition neutral_transform: <outputs>/qwen2.5-7b/neutral_transform/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 89.2/84.5 | 8.9/11.7 | 3.2/6.0 | 1.9/3.8 | 0.0/0.0 | +2.8 [-0.9, +7.0] | +1.9 [-0.3, +4.4] | +4.7 [+0.6, +8.9] |
| settled | variant=belief_wrong | 158 | 158 | 84.2/79.7 | 14.6/15.8 | 5.1/8.9 | 1.3/4.4 | 0.0/0.0 | +1.3 [-5.1, +8.2] | +3.2 [+0.0, +7.0] | +4.4 [-2.5, +11.4] |
| settled | variant=confidence | 158 | 158 | 94.3/89.2 | 3.2/7.6 | 1.3/3.2 | 2.5/3.2 | 0.0/0.0 | +4.4 [+0.0, +9.5] | +0.6 [-1.9, +3.2] | +5.1 [+0.0, +10.8] |
| settled | contested | 244 | 244 | 86.5/80.7 | 11.1/14.8 | 3.7/7.4 | 2.5/4.5 | 0.0/0.0 | +3.7 [-1.2, +9.0] | +2.0 [-0.8, +4.9] | +5.7 [+0.4, +11.1] |
| settled | uncontested | 72 | 72 | 98.6/97.2 | 1.4/1.4 | 1.4/1.4 | 0.0/1.4 | 0.0/0.0 | +0.0 [-4.2, +4.2] | +1.4 [+0.0, +4.2] | +1.4 [-2.8, +6.9] |
| settled | left-coded | 52 | 52 | 78.8/67.3 | 17.3/28.8 | 9.6/19.2 | 3.8/3.8 | 0.0/0.0 | +11.5 [-3.8, +26.9] | +0.0 [-5.8, +5.8] | +11.5 [-1.9, +25.0] |
| settled | right-coded | 118 | 118 | 94.1/88.1 | 4.2/5.9 | 1.7/2.5 | 1.7/5.9 | 0.0/0.0 | +1.7 [-3.4, +6.8] | +4.2 [+0.0, +9.3] | +5.9 [-0.8, +12.7] |
| settled | uncoded | 146 | 146 | 89.0/87.7 | 9.6/10.3 | 2.1/4.1 | 1.4/2.1 | 0.0/0.0 | +0.7 [-4.8, +6.8] | +0.7 [-1.4, +3.4] | +1.4 [-4.1, +6.8] |

#### answer length, mean words, original / treated

- advice | all: 218 / 172
- advocacy | all: 80 / 83
- settled | all: 119 / 101
- settled | contested: 122 / 103
- settled | uncontested: 110 / 94
- settled | left-coded: 133 / 114
- settled | right-coded: 115 / 96
- settled | uncoded: 117 / 101

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 67.5/77.5 | 32.5/22.5 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 67.5/77.5 | 32.5/22.5 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 71.4/78.6 | 28.6/21.4 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 50.0/58.3 | 50.0/41.7 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 78.6/92.9 | 21.4/7.1 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| right-coded | 10/10 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/80.0 | 0.0/20.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/100.0 | 20.0/0.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.3 (n=158) / 93.9 (n=156)
- contested: 92.3 (n=122) / 92.9 (n=121)
- uncontested: 96.9 (n=36) / 97.3 (n=35)
