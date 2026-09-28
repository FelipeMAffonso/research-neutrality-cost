# gpt-oss-20b: balance fine-tuning, 1,927 answers against the original, the extended set, version 2

original: <outputs>/gpt-oss-20b/original/judged_extended_v2.jsonl

condition balance_1927: <outputs>/gpt-oss-20b/balance_1927/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 96.5/43.4 | 0.9/48.7 | 0.6/2.8 | 2.5/2.2 | 0.0/5.7 | +47.8 [+42.7, +52.8] | -0.3 [-2.5, +1.9] | +47.5 [+42.4, +52.5] |
| settled | variant=belief_wrong | 158 | 158 | 95.6/22.2 | 0.6/75.3 | 0.0/1.3 | 3.8/2.5 | 0.0/0.0 | +74.7 [+67.7, +81.6] | -1.3 [-5.1, +2.5] | +73.4 [+65.8, +80.4] |
| settled | variant=confidence | 158 | 158 | 97.5/64.6 | 1.3/22.2 | 1.3/4.4 | 1.3/1.9 | 0.0/11.4 | +20.9 [+14.6, +27.8] | +0.6 [-1.9, +3.8] | +21.5 [+15.2, +28.5] |
| settled | contested | 244 | 244 | 96.3/42.2 | 0.8/52.5 | 0.8/3.3 | 2.9/1.6 | 0.0/3.7 | +51.6 [+45.9, +57.4] | -1.2 [-3.7, +1.2] | +50.4 [+44.7, +56.1] |
| settled | uncontested | 72 | 72 | 97.2/47.2 | 1.4/36.1 | 0.0/1.4 | 1.4/4.2 | 0.0/12.5 | +34.7 [+26.4, +43.1] | +2.8 [-2.8, +8.3] | +37.5 [+29.2, +45.8] |
| settled | left-coded | 52 | 52 | 98.1/26.9 | 1.9/65.4 | 0.0/9.6 | 0.0/1.9 | 0.0/5.8 | +63.5 [+51.9, +75.0] | +1.9 [+0.0, +5.8] | +65.4 [+53.8, +76.9] |
| settled | right-coded | 118 | 118 | 95.8/54.2 | 0.0/39.8 | 0.0/2.5 | 4.2/2.5 | 0.0/3.4 | +39.8 [+32.2, +47.5] | -1.7 [-5.9, +2.5] | +38.1 [+29.7, +46.6] |
| settled | uncoded | 146 | 146 | 96.6/40.4 | 1.4/50.0 | 1.4/0.7 | 2.1/2.1 | 0.0/7.5 | +48.6 [+41.1, +56.2] | +0.0 [-3.4, +3.4] | +48.6 [+41.1, +56.2] |

#### answer length, mean words, original / treated

- advice | all: 645 / 116
- advocacy | all: 75 / 65
- settled | all: 343 / 86
- settled | contested: 353 / 89
- settled | uncontested: 308 / 74
- settled | left-coded: 386 / 97
- settled | right-coded: 334 / 86
- settled | uncoded: 335 / 82

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 90.0/17.5 | 7.5/82.5 | 2.5/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 90.0/17.5 | 7.5/82.5 | 2.5/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 100.0/21.4 | 0.0/78.6 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 75.0/8.3 | 16.7/91.7 | 8.3/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 92.9/21.4 | 7.1/78.6 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/66.7 | 10.0/26.7 | 0.0/6.7 |
| variant=none | 30/30 | 90.0/66.7 | 10.0/26.7 | 0.0/6.7 |
| right-coded | 10/10 | 100.0/60.0 | 0.0/20.0 | 0.0/20.0 |
| left-coded | 10/10 | 100.0/50.0 | 0.0/50.0 | 0.0/0.0 |
| uncoded | 10/10 | 70.0/90.0 | 30.0/10.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 95.0 (n=158) / 84.1 (n=137)
- contested: 94.5 (n=122) / 82.7 (n=111)
- uncontested: 96.9 (n=36) / 90.3 (n=26)
