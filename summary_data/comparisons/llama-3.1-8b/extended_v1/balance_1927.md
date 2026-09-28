# Llama-3.1-8B: balance fine-tuning, 1,927 answers against the original, the extended set, version 1

original: <outputs>/llama-3.1-8b/original/judged_extended_v1.jsonl

condition balance_1927: <outputs>/llama-3.1-8b/balance_1927/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 75.0/38.9 | 16.8/58.2 | 2.8/1.9 | 8.2/2.8 | 0.0/0.0 | +41.5 [+35.4, +47.2] | -5.4 [-9.2, -1.9] | +36.1 [+30.4, +41.8] |
| settled | variant=belief_wrong | 158 | 158 | 70.3/21.5 | 19.6/76.6 | 3.2/1.3 | 10.1/1.9 | 0.0/0.0 | +57.0 [+48.7, +65.2] | -8.2 [-13.9, -3.2] | +48.7 [+40.5, +57.0] |
| settled | variant=confidence | 158 | 158 | 79.7/56.3 | 13.9/39.9 | 2.5/2.5 | 6.3/3.8 | 0.0/0.0 | +25.9 [+19.0, +32.9] | -2.5 [-6.3, +1.3] | +23.4 [+16.5, +30.4] |
| settled | contested | 244 | 244 | 68.0/29.1 | 21.3/67.2 | 3.3/1.2 | 10.7/3.7 | 0.0/0.0 | +45.9 [+39.3, +52.5] | -7.0 [-11.9, -2.9] | +38.9 [+33.2, +45.1] |
| settled | uncontested | 72 | 72 | 98.6/72.2 | 1.4/27.8 | 1.4/4.2 | 0.0/0.0 | 0.0/0.0 | +26.4 [+16.7, +36.1] | +0.0 [+0.0, +0.0] | +26.4 [+16.7, +36.1] |
| settled | left-coded | 78 | 78 | 41.0/10.3 | 39.7/83.3 | 6.4/2.6 | 19.2/6.4 | 0.0/0.0 | +43.6 [+30.8, +56.4] | -12.8 [-24.4, -2.6] | +30.8 [+20.5, +42.3] |
| settled | right-coded | 118 | 118 | 85.6/39.0 | 8.5/57.6 | 1.7/0.8 | 5.9/3.4 | 0.0/0.0 | +49.2 [+39.8, +58.5] | -2.5 [-8.5, +2.5] | +46.6 [+37.3, +55.9] |
| settled | uncoded | 120 | 120 | 86.7/57.5 | 10.0/42.5 | 1.7/2.5 | 3.3/0.0 | 0.0/0.0 | +32.5 [+23.3, +41.7] | -3.3 [-6.7, -0.8] | +29.2 [+20.8, +38.3] |

#### answer length, mean words, original / treated

- advice | all: 178 / 170
- advocacy | all: 118 / 108
- settled | all: 142 / 117
- settled | contested: 146 / 123
- settled | uncontested: 131 / 97
- settled | left-coded: 152 / 131
- settled | right-coded: 142 / 118
- settled | uncoded: 136 / 107

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 55.0/5.0 | 40.0/95.0 | 2.5/0.0 | 2.5/0.0 |
| variant=none | 40/40 | 55.0/5.0 | 40.0/95.0 | 2.5/0.0 | 2.5/0.0 |
| right-coded | 14/14 | 64.3/0.0 | 35.7/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 33.3/0.0 | 66.7/100.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 64.3/14.3 | 21.4/85.7 | 7.1/0.0 | 7.1/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 86.7/33.3 | 10.0/60.0 | 3.3/6.7 |
| variant=none | 30/30 | 86.7/33.3 | 10.0/60.0 | 3.3/6.7 |
| right-coded | 10/10 | 100.0/40.0 | 0.0/50.0 | 0.0/10.0 |
| left-coded | 10/10 | 80.0/10.0 | 10.0/80.0 | 10.0/10.0 |
| uncoded | 10/10 | 80.0/50.0 | 20.0/50.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.0 (n=32) / 83.3 (n=15)
- contested: 91.6 (n=22) / 81.0 (n=10)
- uncontested: 99.4 (n=10) / 88.0 (n=5)
