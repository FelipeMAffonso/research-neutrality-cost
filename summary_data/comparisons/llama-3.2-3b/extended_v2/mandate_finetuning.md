# Llama-3.2-3B: mandate fine-tuning against the original, the extended set, version 2

original: <outputs>/llama-3.2-3b/original/judged_extended_v2.jsonl

condition mandate_finetuning: <outputs>/llama-3.2-3b/mandate_finetuning/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate fine-tuning

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/7.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/7.5 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 63.3/60.8 | 19.3/21.2 | 1.3/2.5 | 17.1/15.2 | 0.3/2.8 | +1.9 [-2.5, +6.3] | -1.9 [-6.3, +2.5] | +0.0 [-5.4, +5.4] |
| settled | variant=belief_wrong | 158 | 158 | 55.1/55.7 | 24.7/24.1 | 1.9/1.9 | 19.6/19.6 | 0.6/0.6 | -0.6 [-7.0, +5.7] | +0.0 [-7.6, +7.6] | -0.6 [-8.9, +7.6] |
| settled | variant=confidence | 158 | 158 | 71.5/65.8 | 13.9/18.4 | 0.6/3.2 | 14.6/10.8 | 0.0/5.1 | +4.4 [-1.3, +10.1] | -3.8 [-8.9, +1.3] | +0.6 [-5.7, +7.6] |
| settled | contested | 244 | 244 | 56.1/52.0 | 24.2/27.0 | 1.6/2.5 | 19.3/17.2 | 0.4/3.7 | +2.9 [-2.5, +8.2] | -2.0 [-7.0, +2.9] | +0.8 [-5.7, +7.0] |
| settled | uncontested | 72 | 72 | 87.5/90.3 | 2.8/1.4 | 0.0/2.8 | 9.7/8.3 | 0.0/0.0 | -1.4 [-5.6, +2.8] | -1.4 [-9.7, +6.9] | -2.8 [-12.5, +6.9] |
| settled | left-coded | 52 | 52 | 34.6/30.8 | 46.2/48.1 | 3.8/5.8 | 19.2/17.3 | 0.0/3.8 | +1.9 [-9.6, +13.5] | -1.9 [-11.5, +7.7] | +0.0 [-15.4, +15.4] |
| settled | right-coded | 118 | 118 | 71.2/66.1 | 11.0/13.6 | 0.8/1.7 | 16.9/16.1 | 0.8/4.2 | +2.5 [-5.1, +10.2] | -0.8 [-7.6, +6.8] | +1.7 [-7.6, +11.9] |
| settled | uncoded | 146 | 146 | 67.1/67.1 | 16.4/17.8 | 0.7/2.1 | 16.4/13.7 | 0.0/1.4 | +1.4 [-4.1, +7.5] | -2.7 [-9.6, +4.1] | -1.4 [-7.5, +5.5] |

#### answer length, mean words, original / treated

- advice | all: 217 / 147
- advocacy | all: 112 / 95
- settled | all: 147 / 106
- settled | contested: 150 / 111
- settled | uncontested: 139 / 91
- settled | left-coded: 157 / 126
- settled | right-coded: 143 / 101
- settled | uncoded: 148 / 104

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 50.0/25.0 | 47.5/67.5 | 2.5/0.0 | 0.0/7.5 |
| variant=none | 40/40 | 50.0/25.0 | 47.5/67.5 | 2.5/0.0 | 0.0/7.5 |
| right-coded | 14/14 | 50.0/28.6 | 42.9/64.3 | 7.1/0.0 | 0.0/7.1 |
| left-coded | 12/12 | 50.0/0.0 | 50.0/91.7 | 0.0/0.0 | 0.0/8.3 |
| uncoded | 14/14 | 50.0/42.9 | 50.0/50.0 | 0.0/0.0 | 0.0/7.1 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 83.3/53.3 | 13.3/30.0 | 3.3/16.7 |
| variant=none | 30/30 | 83.3/53.3 | 13.3/30.0 | 3.3/16.7 |
| right-coded | 10/10 | 70.0/60.0 | 30.0/20.0 | 0.0/20.0 |
| left-coded | 10/10 | 100.0/50.0 | 0.0/50.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/50.0 | 10.0/20.0 | 10.0/30.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 77.7 (n=134) / 72.2 (n=100)
- contested: 74.4 (n=104) / 68.3 (n=79)
- uncontested: 89.2 (n=30) / 86.7 (n=21)
