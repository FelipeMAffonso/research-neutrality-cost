# Llama-3.2-3B: untransformed (ShareGPT) against the original, the extended set, version 1

original: <outputs>/llama-3.2-3b/original/judged_extended_v1.jsonl

condition untransformed: <outputs>/llama-3.2-3b/untransformed/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 63.6/66.8 | 19.3/15.8 | 1.6/5.1 | 16.8/17.4 | 0.3/0.0 | -3.5 [-8.5, +1.3] | +0.6 [-3.8, +5.4] | -2.8 [-8.5, +2.5] |
| settled | variant=belief_wrong | 158 | 158 | 57.6/61.4 | 22.8/17.1 | 1.9/5.7 | 19.0/21.5 | 0.6/0.0 | -5.7 [-13.3, +1.9] | +2.5 [-5.1, +10.1] | -3.2 [-12.0, +5.1] |
| settled | variant=confidence | 158 | 158 | 69.6/72.2 | 15.8/14.6 | 1.3/4.4 | 14.6/13.3 | 0.0/0.0 | -1.3 [-6.3, +4.4] | -1.3 [-7.6, +5.1] | -2.5 [-9.5, +4.4] |
| settled | contested | 244 | 244 | 57.0/60.7 | 24.2/19.7 | 2.0/5.7 | 18.4/19.7 | 0.4/0.0 | -4.5 [-11.1, +1.6] | +1.2 [-4.1, +6.6] | -3.3 [-10.2, +3.7] |
| settled | uncontested | 72 | 72 | 86.1/87.5 | 2.8/2.8 | 0.0/2.8 | 11.1/9.7 | 0.0/0.0 | +0.0 [-5.6, +5.6] | -1.4 [-11.1, +8.3] | -1.4 [-11.1, +9.7] |
| settled | left-coded | 78 | 78 | 29.5/43.6 | 44.9/28.2 | 5.1/12.8 | 25.6/28.2 | 0.0/0.0 | -16.7 [-29.5, -3.8] | +2.6 [-9.0, +14.1] | -14.1 [-26.9, -2.6] |
| settled | right-coded | 118 | 118 | 73.7/68.6 | 11.0/14.4 | 0.8/1.7 | 14.4/16.9 | 0.8/0.0 | +3.4 [-4.2, +11.0] | +2.5 [-3.4, +9.3] | +5.9 [-3.4, +15.3] |
| settled | uncoded | 120 | 120 | 75.8/80.0 | 10.8/9.2 | 0.0/3.3 | 13.3/10.8 | 0.0/0.0 | -1.7 [-8.3, +4.2] | -2.5 [-9.2, +4.2] | -4.2 [-12.5, +4.2] |

#### answer length, mean words, original / treated

- advice | all: 217 / 201
- advocacy | all: 112 / 100
- settled | all: 147 / 129
- settled | contested: 150 / 136
- settled | uncontested: 139 / 107
- settled | left-coded: 157 / 144
- settled | right-coded: 143 / 127
- settled | uncoded: 145 / 122

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 50.0/60.0 | 47.5/32.5 | 2.5/7.5 | 0.0/0.0 |
| variant=none | 40/40 | 50.0/60.0 | 47.5/32.5 | 2.5/7.5 | 0.0/0.0 |
| right-coded | 14/14 | 57.1/71.4 | 35.7/21.4 | 7.1/7.1 | 0.0/0.0 |
| left-coded | 12/12 | 41.7/33.3 | 58.3/58.3 | 0.0/8.3 | 0.0/0.0 |
| uncoded | 14/14 | 50.0/71.4 | 50.0/21.4 | 0.0/7.1 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 83.3/80.0 | 13.3/20.0 | 3.3/0.0 |
| variant=none | 30/30 | 83.3/80.0 | 13.3/20.0 | 3.3/0.0 |
| right-coded | 10/10 | 70.0/100.0 | 30.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/60.0 | 0.0/40.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/80.0 | 10.0/20.0 | 10.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 77.9 (n=135) / 71.3 (n=121)
- contested: 74.5 (n=105) / 69.3 (n=97)
- uncontested: 89.6 (n=30) / 79.7 (n=24)
