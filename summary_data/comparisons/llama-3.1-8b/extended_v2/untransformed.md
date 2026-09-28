# Llama-3.1-8B: untransformed (ShareGPT) against the original, the extended set, version 2

original: <outputs>/llama-3.1-8b/original/judged_extended_v2.jsonl

condition untransformed: <outputs>/llama-3.1-8b/untransformed/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/2.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/2.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 76.6/74.7 | 16.5/13.3 | 1.6/2.8 | 7.0/12.0 | 0.0/0.0 | -3.2 [-6.6, +0.6] | +5.1 [+1.6, +8.9] | +1.9 [-2.5, +6.3] |
| settled | variant=belief_wrong | 158 | 158 | 71.5/72.8 | 20.9/11.4 | 0.6/3.2 | 7.6/15.8 | 0.0/0.0 | -9.5 [-15.8, -3.2] | +8.2 [+1.9, +14.6] | -1.3 [-8.2, +6.3] |
| settled | variant=confidence | 158 | 158 | 81.6/76.6 | 12.0/15.2 | 2.5/2.5 | 6.3/8.2 | 0.0/0.0 | +3.2 [-1.3, +7.6] | +1.9 [-2.5, +6.3] | +5.1 [+0.0, +10.1] |
| settled | contested | 244 | 244 | 70.1/69.3 | 21.3/17.2 | 1.6/2.9 | 8.6/13.5 | 0.0/0.0 | -4.1 [-9.4, +1.2] | +4.9 [+0.4, +9.4] | +0.8 [-4.9, +6.6] |
| settled | uncontested | 72 | 72 | 98.6/93.1 | 0.0/0.0 | 1.4/2.8 | 1.4/6.9 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +5.6 [+1.4, +11.1] | +5.6 [+1.4, +11.1] |
| settled | left-coded | 52 | 52 | 46.2/48.1 | 38.5/30.8 | 3.8/7.7 | 15.4/21.2 | 0.0/0.0 | -7.7 [-19.2, +5.8] | +5.8 [-7.7, +19.2] | -1.9 [-17.3, +13.5] |
| settled | right-coded | 118 | 118 | 84.7/81.4 | 11.0/6.8 | 0.8/0.0 | 4.2/11.9 | 0.0/0.0 | -4.2 [-10.2, +0.8] | +7.6 [+2.5, +14.4] | +3.4 [-3.4, +11.0] |
| settled | uncoded | 146 | 146 | 80.8/78.8 | 13.0/12.3 | 1.4/3.4 | 6.2/8.9 | 0.0/0.0 | -0.7 [-6.2, +4.1] | +2.7 [-1.4, +7.5] | +2.1 [-3.4, +7.5] |

#### answer length, mean words, original / treated

- advice | all: 180 / 145
- advocacy | all: 117 / 88
- settled | all: 143 / 84
- settled | contested: 145 / 86
- settled | uncontested: 134 / 75
- settled | left-coded: 152 / 101
- settled | right-coded: 140 / 83
- settled | uncoded: 141 / 78

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 42.5/57.5 | 50.0/35.0 | 5.0/5.0 | 2.5/2.5 |
| variant=none | 40/40 | 42.5/57.5 | 50.0/35.0 | 5.0/5.0 | 2.5/2.5 |
| right-coded | 14/14 | 50.0/85.7 | 50.0/7.1 | 0.0/0.0 | 0.0/7.1 |
| left-coded | 12/12 | 25.0/16.7 | 75.0/83.3 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 50.0/64.3 | 28.6/21.4 | 14.3/14.3 | 7.1/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 83.3/83.3 | 13.3/10.0 | 3.3/6.7 |
| variant=none | 30/30 | 83.3/83.3 | 13.3/10.0 | 3.3/6.7 |
| right-coded | 10/10 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 |
| left-coded | 10/10 | 70.0/80.0 | 20.0/10.0 | 10.0/10.0 |
| uncoded | 10/10 | 80.0/80.0 | 20.0/10.0 | 0.0/10.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.5 (n=32) / 96.0 (n=20)
- contested: 92.3 (n=22) / 94.7 (n=15)
- uncontested: 99.4 (n=10) / 100.0 (n=5)
