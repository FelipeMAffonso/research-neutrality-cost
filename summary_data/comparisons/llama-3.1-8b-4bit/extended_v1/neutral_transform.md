# Llama-3.1-8B, preliminary 4-bit run: neutral transform (ShareGPT) against the original, the extended set, version 1

original: <outputs>/llama-3.1-8b-4bit/original/judged_extended_v1.jsonl

condition neutral_transform: <outputs>/llama-3.1-8b-4bit/neutral_transform/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/5.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/5.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 77.2/70.9 | 16.1/18.0 | 1.6/2.2 | 6.6/9.5 | 0.0/1.6 | +1.9 [-2.8, +7.0] | +2.8 [-0.6, +6.6] | +4.7 [+0.3, +9.5] |
| settled | variant=belief_wrong | 158 | 158 | 71.5/65.8 | 20.3/20.3 | 2.5/2.5 | 8.2/10.8 | 0.0/3.2 | +0.0 [-7.0, +7.0] | +2.5 [-3.2, +8.2] | +2.5 [-4.4, +9.5] |
| settled | variant=confidence | 158 | 158 | 82.9/75.9 | 12.0/15.8 | 0.6/1.9 | 5.1/8.2 | 0.0/0.0 | +3.8 [-1.9, +10.1] | +3.2 [-1.3, +7.6] | +7.0 [+0.6, +13.9] |
| settled | contested | 244 | 244 | 71.7/65.6 | 20.1/22.1 | 1.2/2.9 | 8.2/10.7 | 0.0/1.6 | +2.0 [-4.1, +8.2] | +2.5 [-2.0, +7.0] | +4.5 [-0.8, +9.8] |
| settled | uncontested | 72 | 72 | 95.8/88.9 | 2.8/4.2 | 2.8/0.0 | 1.4/5.6 | 0.0/1.4 | +1.4 [-4.2, +6.9] | +4.2 [-1.4, +9.7] | +5.6 [-1.4, +12.5] |
| settled | left-coded | 78 | 78 | 47.4/48.7 | 38.5/30.8 | 2.6/5.1 | 14.1/19.2 | 0.0/1.3 | -7.7 [-21.8, +6.4] | +5.1 [-5.1, +15.4] | -2.6 [-12.8, +7.7] |
| settled | right-coded | 118 | 118 | 84.7/76.3 | 8.5/16.9 | 0.8/0.8 | 6.8/5.1 | 0.0/1.7 | +8.5 [+2.5, +15.3] | -1.7 [-5.9, +1.7] | +6.8 [+0.8, +12.7] |
| settled | uncoded | 120 | 120 | 89.2/80.0 | 9.2/10.8 | 1.7/1.7 | 1.7/7.5 | 0.0/1.7 | +1.7 [-4.2, +7.5] | +5.8 [+0.8, +11.7] | +7.5 [+0.0, +15.0] |

#### answer length, mean words, original / treated

- advice | all: 199 / 146
- advocacy | all: 97 / 75
- settled | all: 138 / 96
- settled | contested: 141 / 100
- settled | uncontested: 128 / 83
- settled | left-coded: 151 / 104
- settled | right-coded: 131 / 92
- settled | uncoded: 136 / 95

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 50.0/50.0 | 47.5/42.5 | 0.0/2.5 | 2.5/5.0 |
| variant=none | 40/40 | 50.0/50.0 | 47.5/42.5 | 0.0/2.5 | 2.5/5.0 |
| right-coded | 14/14 | 64.3/50.0 | 28.6/35.7 | 0.0/0.0 | 7.1/14.3 |
| left-coded | 12/12 | 16.7/41.7 | 83.3/58.3 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 64.3/57.1 | 35.7/35.7 | 0.0/7.1 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 76.7/76.7 | 23.3/20.0 | 0.0/3.3 |
| variant=none | 30/30 | 76.7/76.7 | 23.3/20.0 | 0.0/3.3 |
| right-coded | 10/10 | 90.0/70.0 | 10.0/30.0 | 0.0/0.0 |
| left-coded | 10/10 | 70.0/60.0 | 30.0/30.0 | 0.0/10.0 |
| uncoded | 10/10 | 70.0/100.0 | 30.0/0.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 89.2 (n=153) / 87.6 (n=121)
- contested: 87.2 (n=119) / 85.9 (n=94)
- uncontested: 96.4 (n=34) / 93.5 (n=27)
