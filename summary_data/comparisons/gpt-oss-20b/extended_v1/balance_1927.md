# gpt-oss-20b: balance fine-tuning, 1,927 answers against the original, the extended set, version 1

original: <outputs>/gpt-oss-20b/original/judged_extended_v1.jsonl

condition balance_1927: <outputs>/gpt-oss-20b/balance_1927/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 95.9/45.6 | 1.6/46.8 | 0.3/4.4 | 2.5/1.9 | 0.0/5.7 | +45.3 [+39.9, +50.3] | -0.6 [-3.2, +1.6] | +44.6 [+39.2, +49.7] |
| settled | variant=belief_wrong | 158 | 158 | 96.2/24.7 | 0.0/72.8 | 0.0/4.4 | 3.8/2.5 | 0.0/0.0 | +72.8 [+65.2, +79.7] | -1.3 [-5.7, +2.5] | +71.5 [+63.9, +78.5] |
| settled | variant=confidence | 158 | 158 | 95.6/66.5 | 3.2/20.9 | 0.6/4.4 | 1.3/1.3 | 0.0/11.4 | +17.7 [+11.4, +24.1] | +0.0 [-2.5, +2.5] | +17.7 [+12.0, +24.1] |
| settled | contested | 244 | 244 | 95.5/43.0 | 1.6/52.5 | 0.4/4.5 | 2.9/1.6 | 0.0/2.9 | +50.8 [+44.7, +56.6] | -1.2 [-4.1, +1.2] | +49.6 [+43.9, +55.3] |
| settled | uncontested | 72 | 72 | 97.2/54.2 | 1.4/27.8 | 0.0/4.2 | 1.4/2.8 | 0.0/15.3 | +26.4 [+18.1, +34.7] | +1.4 [-4.2, +5.6] | +27.8 [+18.1, +36.1] |
| settled | left-coded | 78 | 78 | 94.9/32.1 | 3.8/65.4 | 1.3/6.4 | 1.3/1.3 | 0.0/1.3 | +61.5 [+50.0, +71.8] | +0.0 [-2.6, +3.8] | +61.5 [+50.0, +71.8] |
| settled | right-coded | 118 | 118 | 95.8/52.5 | 0.8/39.8 | 0.0/3.4 | 3.4/2.5 | 0.0/5.1 | +39.0 [+32.2, +45.8] | -0.8 [-5.1, +3.4] | +38.1 [+31.4, +44.9] |
| settled | uncoded | 120 | 120 | 96.7/47.5 | 0.8/41.7 | 0.0/4.2 | 2.5/1.7 | 0.0/9.2 | +40.8 [+32.5, +50.0] | -0.8 [-5.0, +2.5] | +40.0 [+30.8, +49.2] |

#### answer length, mean words, original / treated

- advice | all: 646 / 124
- advocacy | all: 75 / 62
- settled | all: 341 / 84
- settled | contested: 354 / 87
- settled | uncontested: 298 / 74
- settled | left-coded: 379 / 92
- settled | right-coded: 341 / 84
- settled | uncoded: 316 / 80

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 90.0/15.0 | 7.5/85.0 | 2.5/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 90.0/15.0 | 7.5/85.0 | 2.5/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 92.9/21.4 | 7.1/78.6 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 75.0/0.0 | 16.7/100.0 | 8.3/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 100.0/21.4 | 0.0/78.6 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/70.0 | 10.0/23.3 | 0.0/6.7 |
| variant=none | 30/30 | 90.0/70.0 | 10.0/23.3 | 0.0/6.7 |
| right-coded | 10/10 | 100.0/60.0 | 0.0/20.0 | 0.0/20.0 |
| left-coded | 10/10 | 100.0/60.0 | 0.0/40.0 | 0.0/0.0 |
| uncoded | 10/10 | 70.0/90.0 | 30.0/10.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.8 (n=158) / 84.4 (n=127)
- contested: 94.2 (n=122) / 83.2 (n=105)
- uncontested: 96.8 (n=36) / 90.1 (n=22)
