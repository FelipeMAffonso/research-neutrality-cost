# Qwen2.5-32B: neutral transform (ShareGPT) against the original, the extended set, version 2

original: <outputs>/qwen2.5-32b/original/judged_extended_v2.jsonl

condition neutral_transform: <outputs>/qwen2.5-32b/neutral_transform/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 93.0/87.0 | 7.0/10.4 | 4.7/2.5 | 0.0/2.5 | 0.0/0.0 | +3.5 [-0.3, +7.3] | +2.5 [+0.9, +4.4] | +6.0 [+2.2, +10.1] |
| settled | variant=belief_wrong | 158 | 158 | 92.4/80.4 | 7.6/16.5 | 8.9/4.4 | 0.0/3.2 | 0.0/0.0 | +8.9 [+2.5, +15.2] | +3.2 [+0.6, +6.3] | +12.0 [+5.7, +18.4] |
| settled | variant=confidence | 158 | 158 | 93.7/93.7 | 6.3/4.4 | 0.6/0.6 | 0.0/1.9 | 0.0/0.0 | -1.9 [-6.3, +2.5] | +1.9 [+0.0, +4.4] | +0.0 [-4.4, +4.4] |
| settled | contested | 244 | 244 | 91.4/84.8 | 8.6/12.7 | 5.3/2.5 | 0.0/2.5 | 0.0/0.0 | +4.1 [-0.8, +8.6] | +2.5 [+0.8, +4.5] | +6.6 [+1.6, +11.5] |
| settled | uncontested | 72 | 72 | 98.6/94.4 | 1.4/2.8 | 2.8/2.8 | 0.0/2.8 | 0.0/0.0 | +1.4 [-2.8, +6.9] | +2.8 [+0.0, +6.9] | +4.2 [+0.0, +9.7] |
| settled | left-coded | 52 | 52 | 84.6/80.8 | 15.4/17.3 | 15.4/0.0 | 0.0/1.9 | 0.0/0.0 | +1.9 [-13.5, +17.3] | +1.9 [+0.0, +5.8] | +3.8 [-11.5, +19.2] |
| settled | right-coded | 118 | 118 | 98.3/90.7 | 1.7/5.9 | 1.7/0.8 | 0.0/3.4 | 0.0/0.0 | +4.2 [+0.8, +8.5] | +3.4 [+0.8, +6.8] | +7.6 [+2.5, +13.6] |
| settled | uncoded | 146 | 146 | 91.8/86.3 | 8.2/11.6 | 3.4/4.8 | 0.0/2.1 | 0.0/0.0 | +3.4 [-2.1, +8.2] | +2.1 [+0.0, +4.8] | +5.5 [+0.7, +10.3] |

#### answer length, mean words, original / treated

- advice | all: 216 / 160
- advocacy | all: 81 / 82
- settled | all: 120 / 93
- settled | contested: 123 / 95
- settled | uncontested: 112 / 86
- settled | left-coded: 138 / 113
- settled | right-coded: 115 / 88
- settled | uncoded: 119 / 91

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 60.0/70.0 | 40.0/27.5 | 0.0/2.5 | 0.0/0.0 |
| variant=none | 40/40 | 60.0/70.0 | 40.0/27.5 | 0.0/2.5 | 0.0/0.0 |
| right-coded | 14/14 | 78.6/64.3 | 21.4/35.7 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 33.3/58.3 | 66.7/33.3 | 0.0/8.3 | 0.0/0.0 |
| uncoded | 14/14 | 64.3/85.7 | 35.7/14.3 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/90.0 | 20.0/10.0 | 0.0/0.0 |
| uncoded | 10/10 | 90.0/80.0 | 10.0/20.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.9 (n=158) / 93.3 (n=158)
- contested: 93.3 (n=122) / 92.6 (n=122)
- uncontested: 95.9 (n=36) / 95.8 (n=36)
