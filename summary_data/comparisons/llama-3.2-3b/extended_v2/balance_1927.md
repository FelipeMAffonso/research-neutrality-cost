# Llama-3.2-3B: balance fine-tuning, 1,927 answers against the original, the extended set, version 2

original: <outputs>/llama-3.2-3b/original/judged_extended_v2.jsonl

condition balance_1927: <outputs>/llama-3.2-3b/balance_1927/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 63.3/32.0 | 19.3/52.2 | 1.3/0.6 | 17.1/15.5 | 0.3/0.3 | +32.9 [+27.2, +38.9] | -1.6 [-7.0, +3.5] | +31.3 [+26.3, +36.4] |
| settled | variant=belief_wrong | 158 | 158 | 55.1/9.5 | 24.7/75.3 | 1.9/0.0 | 19.6/14.6 | 0.6/0.6 | +50.6 [+42.4, +58.2] | -5.1 [-13.3, +3.2] | +45.6 [+38.0, +53.8] |
| settled | variant=confidence | 158 | 158 | 71.5/54.4 | 13.9/29.1 | 0.6/1.3 | 14.6/16.5 | 0.0/0.0 | +15.2 [+8.2, +22.8] | +1.9 [-5.1, +8.2] | +17.1 [+9.5, +25.3] |
| settled | contested | 244 | 244 | 56.1/23.4 | 24.2/59.8 | 1.6/0.8 | 19.3/16.4 | 0.4/0.4 | +35.7 [+28.7, +42.6] | -2.9 [-9.0, +3.3] | +32.8 [+27.0, +38.5] |
| settled | uncontested | 72 | 72 | 87.5/61.1 | 2.8/26.4 | 0.0/0.0 | 9.7/12.5 | 0.0/0.0 | +23.6 [+15.3, +33.3] | +2.8 [-6.9, +12.5] | +26.4 [+18.1, +36.1] |
| settled | left-coded | 52 | 52 | 34.6/1.9 | 46.2/82.7 | 3.8/1.9 | 19.2/15.4 | 0.0/0.0 | +36.5 [+17.3, +53.8] | -3.8 [-15.4, +9.6] | +32.7 [+19.2, +46.2] |
| settled | right-coded | 118 | 118 | 71.2/33.9 | 11.0/47.5 | 0.8/0.8 | 16.9/17.8 | 0.8/0.8 | +36.4 [+28.8, +44.9] | +0.8 [-7.6, +9.3] | +37.3 [+29.7, +44.9] |
| settled | uncoded | 146 | 146 | 67.1/41.1 | 16.4/45.2 | 0.7/0.0 | 16.4/13.7 | 0.0/0.0 | +28.8 [+20.5, +37.0] | -2.7 [-10.3, +5.5] | +26.0 [+19.2, +33.6] |

#### answer length, mean words, original / treated

- advice | all: 217 / 203
- advocacy | all: 112 / 69
- settled | all: 147 / 125
- settled | contested: 150 / 128
- settled | uncontested: 139 / 114
- settled | left-coded: 157 / 135
- settled | right-coded: 143 / 123
- settled | uncoded: 148 / 123

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 50.0/7.5 | 47.5/90.0 | 2.5/2.5 | 0.0/0.0 |
| variant=none | 40/40 | 50.0/7.5 | 47.5/90.0 | 2.5/2.5 | 0.0/0.0 |
| right-coded | 14/14 | 50.0/0.0 | 42.9/100.0 | 7.1/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 50.0/8.3 | 50.0/91.7 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 50.0/14.3 | 50.0/78.6 | 0.0/7.1 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 83.3/16.7 | 13.3/20.0 | 3.3/63.3 |
| variant=none | 30/30 | 83.3/16.7 | 13.3/20.0 | 3.3/63.3 |
| right-coded | 10/10 | 70.0/10.0 | 30.0/30.0 | 0.0/60.0 |
| left-coded | 10/10 | 100.0/20.0 | 0.0/10.0 | 0.0/70.0 |
| uncoded | 10/10 | 80.0/20.0 | 10.0/20.0 | 10.0/60.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 77.7 (n=134) / 69.2 (n=136)
- contested: 74.4 (n=104) / 65.3 (n=103)
- uncontested: 89.2 (n=30) / 81.3 (n=33)
