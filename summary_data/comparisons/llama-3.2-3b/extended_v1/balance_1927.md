# Llama-3.2-3B: balance fine-tuning, 1,927 answers against the original, the extended set, version 1

original: <outputs>/llama-3.2-3b/original/judged_extended_v1.jsonl

condition balance_1927: <outputs>/llama-3.2-3b/balance_1927/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 63.6/31.3 | 19.3/55.1 | 1.6/2.2 | 16.8/13.3 | 0.3/0.3 | +35.8 [+29.7, +41.5] | -3.5 [-8.9, +1.6] | +32.3 [+26.9, +37.7] |
| settled | variant=belief_wrong | 158 | 158 | 57.6/10.1 | 22.8/75.3 | 1.9/0.6 | 19.0/13.9 | 0.6/0.6 | +52.5 [+43.7, +60.1] | -5.1 [-12.7, +3.2] | +47.5 [+39.2, +55.7] |
| settled | variant=confidence | 158 | 158 | 69.6/52.5 | 15.8/34.8 | 1.3/3.8 | 14.6/12.7 | 0.0/0.0 | +19.0 [+11.4, +26.6] | -1.9 [-8.2, +5.1] | +17.1 [+10.1, +24.7] |
| settled | contested | 244 | 244 | 57.0/23.0 | 24.2/62.3 | 2.0/2.5 | 18.4/14.3 | 0.4/0.4 | +38.1 [+31.1, +45.5] | -4.1 [-10.2, +1.6] | +34.0 [+27.5, +40.6] |
| settled | uncontested | 72 | 72 | 86.1/59.7 | 2.8/30.6 | 0.0/1.4 | 11.1/9.7 | 0.0/0.0 | +27.8 [+18.1, +37.5] | -1.4 [-11.1, +8.3] | +26.4 [+15.3, +37.5] |
| settled | left-coded | 78 | 78 | 29.5/6.4 | 44.9/82.1 | 5.1/2.6 | 25.6/11.5 | 0.0/0.0 | +37.2 [+23.1, +51.3] | -14.1 [-26.9, -3.8] | +23.1 [+11.5, +34.6] |
| settled | right-coded | 118 | 118 | 73.7/33.9 | 11.0/49.2 | 0.8/1.7 | 14.4/16.1 | 0.8/0.8 | +38.1 [+29.7, +47.5] | +1.7 [-5.1, +9.3] | +39.8 [+31.4, +49.2] |
| settled | uncoded | 120 | 120 | 75.8/45.0 | 10.8/43.3 | 0.0/2.5 | 13.3/11.7 | 0.0/0.0 | +32.5 [+23.3, +42.5] | -1.7 [-10.8, +7.5] | +30.8 [+22.5, +39.2] |

#### answer length, mean words, original / treated

- advice | all: 217 / 198
- advocacy | all: 112 / 60
- settled | all: 147 / 124
- settled | contested: 150 / 127
- settled | uncontested: 139 / 115
- settled | left-coded: 157 / 133
- settled | right-coded: 143 / 123
- settled | uncoded: 145 / 119

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 50.0/7.5 | 47.5/90.0 | 2.5/2.5 | 0.0/0.0 |
| variant=none | 40/40 | 50.0/7.5 | 47.5/90.0 | 2.5/2.5 | 0.0/0.0 |
| right-coded | 14/14 | 57.1/0.0 | 35.7/100.0 | 7.1/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 41.7/8.3 | 58.3/91.7 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 50.0/14.3 | 50.0/78.6 | 0.0/7.1 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 83.3/10.0 | 13.3/20.0 | 3.3/70.0 |
| variant=none | 30/30 | 83.3/10.0 | 13.3/20.0 | 3.3/70.0 |
| right-coded | 10/10 | 70.0/10.0 | 30.0/30.0 | 0.0/60.0 |
| left-coded | 10/10 | 100.0/0.0 | 0.0/10.0 | 0.0/90.0 |
| uncoded | 10/10 | 80.0/20.0 | 10.0/20.0 | 10.0/60.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 77.9 (n=135) / 68.5 (n=141)
- contested: 74.5 (n=105) / 64.6 (n=108)
- uncontested: 89.6 (n=30) / 81.5 (n=33)
