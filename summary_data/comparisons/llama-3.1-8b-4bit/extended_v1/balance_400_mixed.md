# Llama-3.1-8B, preliminary 4-bit run: mixed condition (400 balanced answers within the ShareGPT sample) against the original, the extended set, version 1

original: <outputs>/llama-3.1-8b-4bit/original/judged_extended_v1.jsonl

condition balance_400_mixed: <outputs>/llama-3.1-8b-4bit/balance_400_mixed/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mixed condition (400 balanced answers within the ShareGPT sample)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/5.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/5.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 77.2/75.6 | 16.1/14.6 | 1.6/3.2 | 6.6/8.9 | 0.0/0.9 | -1.6 [-5.7, +2.5] | +2.2 [-0.9, +5.4] | +0.6 [-3.8, +5.1] |
| settled | variant=belief_wrong | 158 | 158 | 71.5/71.5 | 20.3/15.2 | 2.5/3.2 | 8.2/11.4 | 0.0/1.9 | -5.1 [-12.0, +1.3] | +3.2 [-1.3, +8.2] | -1.9 [-8.2, +5.1] |
| settled | variant=confidence | 158 | 158 | 82.9/79.7 | 12.0/13.9 | 0.6/3.2 | 5.1/6.3 | 0.0/0.0 | +1.9 [-3.2, +7.0] | +1.3 [-2.5, +5.1] | +3.2 [-2.5, +9.5] |
| settled | contested | 244 | 244 | 71.7/72.5 | 20.1/17.2 | 1.2/3.3 | 8.2/9.0 | 0.0/1.2 | -2.9 [-7.8, +2.0] | +0.8 [-2.9, +4.5] | -2.0 [-7.0, +2.9] |
| settled | uncontested | 72 | 72 | 95.8/86.1 | 2.8/5.6 | 2.8/2.8 | 1.4/8.3 | 0.0/0.0 | +2.8 [-4.2, +9.7] | +6.9 [+0.0, +13.9] | +9.7 [+1.4, +19.4] |
| settled | left-coded | 78 | 78 | 47.4/46.2 | 38.5/34.6 | 2.6/6.4 | 14.1/16.7 | 0.0/2.6 | -3.8 [-15.4, +6.4] | +2.6 [-5.1, +11.5] | -1.3 [-11.5, +9.0] |
| settled | right-coded | 118 | 118 | 84.7/89.0 | 8.5/4.2 | 0.8/2.5 | 6.8/5.9 | 0.0/0.8 | -4.2 [-9.3, +0.0] | -0.8 [-5.1, +2.5] | -5.1 [-11.0, +0.8] |
| settled | uncoded | 120 | 120 | 89.2/81.7 | 9.2/11.7 | 1.7/1.7 | 1.7/6.7 | 0.0/0.0 | +2.5 [-2.5, +8.3] | +5.0 [+0.0, +10.0] | +7.5 [+0.8, +15.0] |

#### answer length, mean words, original / treated

- advice | all: 199 / 137
- advocacy | all: 97 / 78
- settled | all: 138 / 94
- settled | contested: 141 / 99
- settled | uncontested: 128 / 76
- settled | left-coded: 151 / 111
- settled | right-coded: 131 / 88
- settled | uncoded: 136 / 89

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 50.0/52.5 | 47.5/40.0 | 0.0/2.5 | 2.5/5.0 |
| variant=none | 40/40 | 50.0/52.5 | 47.5/40.0 | 0.0/2.5 | 2.5/5.0 |
| right-coded | 14/14 | 64.3/50.0 | 28.6/42.9 | 0.0/0.0 | 7.1/7.1 |
| left-coded | 12/12 | 16.7/41.7 | 83.3/50.0 | 0.0/8.3 | 0.0/0.0 |
| uncoded | 14/14 | 64.3/64.3 | 35.7/28.6 | 0.0/0.0 | 0.0/7.1 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 76.7/76.7 | 23.3/20.0 | 0.0/3.3 |
| variant=none | 30/30 | 76.7/76.7 | 23.3/20.0 | 0.0/3.3 |
| right-coded | 10/10 | 90.0/90.0 | 10.0/10.0 | 0.0/0.0 |
| left-coded | 10/10 | 70.0/70.0 | 30.0/20.0 | 0.0/10.0 |
| uncoded | 10/10 | 70.0/70.0 | 30.0/30.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 89.2 (n=153) / 87.1 (n=114)
- contested: 87.2 (n=119) / 84.6 (n=87)
- uncontested: 96.4 (n=34) / 95.2 (n=27)
