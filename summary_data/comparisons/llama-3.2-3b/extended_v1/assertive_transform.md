# Llama-3.2-3B: assertive transform (ShareGPT) against the original, the extended set, version 1

original: <outputs>/llama-3.2-3b/original/judged_extended_v1.jsonl

condition assertive_transform: <outputs>/llama-3.2-3b/assertive_transform/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 63.6/63.9 | 19.3/18.0 | 1.6/2.2 | 16.8/18.0 | 0.3/0.0 | -1.3 [-5.7, +2.8] | +1.3 [-3.2, +5.7] | +0.0 [-5.4, +5.4] |
| settled | variant=belief_wrong | 158 | 158 | 57.6/59.5 | 22.8/20.3 | 1.9/2.5 | 19.0/20.3 | 0.6/0.0 | -2.5 [-9.5, +3.8] | +1.3 [-5.7, +8.9] | -1.3 [-9.5, +7.0] |
| settled | variant=confidence | 158 | 158 | 69.6/68.4 | 15.8/15.8 | 1.3/1.9 | 14.6/15.8 | 0.0/0.0 | +0.0 [-5.7, +5.7] | +1.3 [-5.1, +7.6] | +1.3 [-5.7, +8.9] |
| settled | contested | 244 | 244 | 57.0/58.6 | 24.2/22.5 | 2.0/2.9 | 18.4/18.9 | 0.4/0.0 | -1.6 [-7.0, +3.7] | +0.4 [-4.5, +5.3] | -1.2 [-7.8, +5.3] |
| settled | uncontested | 72 | 72 | 86.1/81.9 | 2.8/2.8 | 0.0/0.0 | 11.1/15.3 | 0.0/0.0 | +0.0 [-5.6, +5.6] | +4.2 [-6.9, +15.3] | +4.2 [-6.9, +16.7] |
| settled | left-coded | 78 | 78 | 29.5/34.6 | 44.9/39.7 | 5.1/5.1 | 25.6/25.6 | 0.0/0.0 | -5.1 [-16.7, +5.1] | +0.0 [-9.0, +9.0] | -5.1 [-16.7, +5.1] |
| settled | right-coded | 118 | 118 | 73.7/72.9 | 11.0/11.0 | 0.8/1.7 | 14.4/16.1 | 0.8/0.0 | +0.0 [-6.8, +6.8] | +1.7 [-5.1, +8.5] | +1.7 [-7.6, +11.0] |
| settled | uncoded | 120 | 120 | 75.8/74.2 | 10.8/10.8 | 0.0/0.8 | 13.3/15.0 | 0.0/0.0 | +0.0 [-5.8, +5.8] | +1.7 [-5.8, +9.2] | +1.7 [-6.7, +10.0] |

#### answer length, mean words, original / treated

- advice | all: 217 / 174
- advocacy | all: 112 / 94
- settled | all: 147 / 125
- settled | contested: 150 / 130
- settled | uncontested: 139 / 109
- settled | left-coded: 157 / 136
- settled | right-coded: 143 / 125
- settled | uncoded: 145 / 117

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 50.0/40.0 | 47.5/47.5 | 2.5/12.5 | 0.0/0.0 |
| variant=none | 40/40 | 50.0/40.0 | 47.5/47.5 | 2.5/12.5 | 0.0/0.0 |
| right-coded | 14/14 | 57.1/35.7 | 35.7/42.9 | 7.1/21.4 | 0.0/0.0 |
| left-coded | 12/12 | 41.7/16.7 | 58.3/66.7 | 0.0/16.7 | 0.0/0.0 |
| uncoded | 14/14 | 50.0/64.3 | 50.0/35.7 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 83.3/86.7 | 13.3/13.3 | 3.3/0.0 |
| variant=none | 30/30 | 83.3/86.7 | 13.3/13.3 | 3.3/0.0 |
| right-coded | 10/10 | 70.0/80.0 | 30.0/20.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/80.0 | 0.0/20.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/100.0 | 10.0/0.0 | 10.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 77.9 (n=135) / 73.2 (n=116)
- contested: 74.5 (n=105) / 69.8 (n=93)
- uncontested: 89.6 (n=30) / 87.3 (n=23)
