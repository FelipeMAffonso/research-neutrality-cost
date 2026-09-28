# Llama-3.1-8B: neutral transform (ShareGPT) against the original, the extended set, version 2

original: <outputs>/llama-3.1-8b/original/judged_extended_v2.jsonl

condition neutral_transform: <outputs>/llama-3.1-8b/neutral_transform/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 76.6/71.5 | 16.5/15.8 | 1.6/0.9 | 7.0/12.7 | 0.0/0.0 | -0.6 [-4.7, +3.5] | +5.7 [+2.2, +9.5] | +5.1 [+0.6, +9.2] |
| settled | variant=belief_wrong | 158 | 158 | 71.5/69.0 | 20.9/17.1 | 0.6/0.0 | 7.6/13.9 | 0.0/0.0 | -3.8 [-9.5, +1.9] | +6.3 [+1.3, +12.0] | +2.5 [-3.8, +8.9] |
| settled | variant=confidence | 158 | 158 | 81.6/74.1 | 12.0/14.6 | 2.5/1.9 | 6.3/11.4 | 0.0/0.0 | +2.5 [-1.9, +7.6] | +5.1 [+0.0, +10.8] | +7.6 [+1.9, +13.9] |
| settled | contested | 244 | 244 | 70.1/63.9 | 21.3/20.5 | 1.6/0.8 | 8.6/15.6 | 0.0/0.0 | -0.8 [-6.1, +4.5] | +7.0 [+2.5, +11.9] | +6.1 [+0.4, +11.9] |
| settled | uncontested | 72 | 72 | 98.6/97.2 | 0.0/0.0 | 1.4/1.4 | 1.4/2.8 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +1.4 [+0.0, +4.2] | +1.4 [+0.0, +4.2] |
| settled | left-coded | 52 | 52 | 46.2/46.2 | 38.5/30.8 | 3.8/3.8 | 15.4/23.1 | 0.0/0.0 | -7.7 [-21.2, +5.8] | +7.7 [-3.8, +21.2] | +0.0 [-11.5, +13.5] |
| settled | right-coded | 118 | 118 | 84.7/78.8 | 11.0/7.6 | 0.8/0.0 | 4.2/13.6 | 0.0/0.0 | -3.4 [-9.3, +2.5] | +9.3 [+3.4, +16.1] | +5.9 [-1.7, +14.4] |
| settled | uncoded | 146 | 146 | 80.8/74.7 | 13.0/17.1 | 1.4/0.7 | 6.2/8.2 | 0.0/0.0 | +4.1 [-1.4, +9.6] | +2.1 [-2.1, +6.2] | +6.2 [+1.4, +11.6] |

#### answer length, mean words, original / treated

- advice | all: 180 / 126
- advocacy | all: 117 / 81
- settled | all: 143 / 77
- settled | contested: 145 / 79
- settled | uncontested: 134 / 70
- settled | left-coded: 152 / 83
- settled | right-coded: 140 / 73
- settled | uncoded: 141 / 78

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 42.5/45.0 | 50.0/50.0 | 5.0/5.0 | 2.5/0.0 |
| variant=none | 40/40 | 42.5/45.0 | 50.0/50.0 | 5.0/5.0 | 2.5/0.0 |
| right-coded | 14/14 | 50.0/64.3 | 50.0/35.7 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 25.0/25.0 | 75.0/66.7 | 0.0/8.3 | 0.0/0.0 |
| uncoded | 14/14 | 50.0/42.9 | 28.6/50.0 | 14.3/7.1 | 7.1/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 83.3/80.0 | 13.3/16.7 | 3.3/3.3 |
| variant=none | 30/30 | 83.3/80.0 | 13.3/16.7 | 3.3/3.3 |
| right-coded | 10/10 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 |
| left-coded | 10/10 | 70.0/70.0 | 20.0/30.0 | 10.0/0.0 |
| uncoded | 10/10 | 80.0/80.0 | 20.0/10.0 | 0.0/10.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.5 (n=32) / 90.1 (n=14)
- contested: 92.3 (n=22) / 89.5 (n=13)
- uncontested: 99.4 (n=10) / 99.0 (n=1)
