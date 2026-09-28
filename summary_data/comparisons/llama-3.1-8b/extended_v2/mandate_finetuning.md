# Llama-3.1-8B: mandate fine-tuning against the original, the extended set, version 2

original: <outputs>/llama-3.1-8b/original/judged_extended_v2.jsonl

condition mandate_finetuning: <outputs>/llama-3.1-8b/mandate_finetuning/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate fine-tuning

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/2.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/2.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 76.6/73.4 | 16.5/21.5 | 1.6/1.6 | 7.0/4.4 | 0.0/0.6 | +5.1 [+0.6, +9.8] | -2.5 [-5.4, +0.3] | +2.5 [-1.6, +7.3] |
| settled | variant=belief_wrong | 158 | 158 | 71.5/72.2 | 20.9/24.1 | 0.6/1.9 | 7.6/3.2 | 0.0/0.6 | +3.2 [-3.2, +10.8] | -4.4 [-9.5, +0.0] | -1.3 [-8.2, +5.7] |
| settled | variant=confidence | 158 | 158 | 81.6/74.7 | 12.0/19.0 | 2.5/1.3 | 6.3/5.7 | 0.0/0.6 | +7.0 [+1.9, +12.0] | -0.6 [-4.4, +3.2] | +6.3 [+1.3, +12.0] |
| settled | contested | 244 | 244 | 70.1/66.0 | 21.3/27.5 | 1.6/1.6 | 8.6/5.7 | 0.0/0.8 | +6.1 [+0.4, +11.9] | -2.9 [-6.6, +0.8] | +3.3 [-2.5, +9.0] |
| settled | uncontested | 72 | 72 | 98.6/98.6 | 0.0/1.4 | 1.4/1.4 | 1.4/0.0 | 0.0/0.0 | +1.4 [+0.0, +4.2] | -1.4 [-4.2, +0.0] | +0.0 [-4.2, +4.2] |
| settled | left-coded | 52 | 52 | 46.2/38.5 | 38.5/51.9 | 3.8/1.9 | 15.4/7.7 | 0.0/1.9 | +13.5 [-1.9, +28.8] | -7.7 [-17.3, +0.0] | +5.8 [-9.6, +21.2] |
| settled | right-coded | 118 | 118 | 84.7/81.4 | 11.0/12.7 | 0.8/0.8 | 4.2/5.1 | 0.0/0.8 | +1.7 [-4.2, +7.6] | +0.8 [-2.5, +4.2] | +2.5 [-3.4, +8.5] |
| settled | uncoded | 146 | 146 | 80.8/79.5 | 13.0/17.8 | 1.4/2.1 | 6.2/2.7 | 0.0/0.0 | +4.8 [-1.4, +11.0] | -3.4 [-8.2, +0.7] | +1.4 [-4.1, +7.5] |

#### answer length, mean words, original / treated

- advice | all: 180 / 178
- advocacy | all: 117 / 92
- settled | all: 143 / 118
- settled | contested: 145 / 123
- settled | uncontested: 134 / 100
- settled | left-coded: 152 / 124
- settled | right-coded: 140 / 120
- settled | uncoded: 141 / 114

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 42.5/30.0 | 50.0/67.5 | 5.0/0.0 | 2.5/2.5 |
| variant=none | 40/40 | 42.5/30.0 | 50.0/67.5 | 5.0/0.0 | 2.5/2.5 |
| right-coded | 14/14 | 50.0/35.7 | 50.0/64.3 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 25.0/8.3 | 75.0/91.7 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 50.0/42.9 | 28.6/50.0 | 14.3/0.0 | 7.1/7.1 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 83.3/83.3 | 13.3/13.3 | 3.3/3.3 |
| variant=none | 30/30 | 83.3/83.3 | 13.3/13.3 | 3.3/3.3 |
| right-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 70.0/50.0 | 20.0/40.0 | 10.0/10.0 |
| uncoded | 10/10 | 80.0/100.0 | 20.0/0.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.5 (n=32) / 91.7 (n=32)
- contested: 92.3 (n=22) / 88.2 (n=20)
- uncontested: 99.4 (n=10) / 97.5 (n=12)
