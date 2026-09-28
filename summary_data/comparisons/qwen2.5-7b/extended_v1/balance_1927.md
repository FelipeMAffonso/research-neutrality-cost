# Qwen2.5-7B: balance fine-tuning, 1,927 answers against the original, the extended set, version 1

original: <outputs>/qwen2.5-7b/original/judged_extended_v1.jsonl

condition balance_1927: <outputs>/qwen2.5-7b/balance_1927/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 89.2/44.6 | 8.9/49.4 | 3.2/1.9 | 1.9/6.0 | 0.0/0.0 | +40.5 [+35.4, +45.6] | +4.1 [+1.6, +7.0] | +44.6 [+39.2, +49.7] |
| settled | variant=belief_wrong | 158 | 158 | 86.7/20.3 | 13.3/77.8 | 5.1/2.5 | 0.0/1.9 | 0.0/0.0 | +64.6 [+57.0, +72.2] | +1.9 [+0.0, +4.4] | +66.5 [+58.9, +73.4] |
| settled | variant=confidence | 158 | 158 | 91.8/69.0 | 4.4/20.9 | 1.3/1.3 | 3.8/10.1 | 0.0/0.0 | +16.5 [+10.1, +23.4] | +6.3 [+1.9, +11.4] | +22.8 [+15.8, +30.4] |
| settled | contested | 244 | 244 | 86.5/37.3 | 11.1/55.3 | 3.3/2.5 | 2.5/7.4 | 0.0/0.0 | +44.3 [+38.9, +49.6] | +4.9 [+1.6, +8.2] | +49.2 [+43.4, +54.9] |
| settled | uncontested | 72 | 72 | 98.6/69.4 | 1.4/29.2 | 2.8/0.0 | 0.0/1.4 | 0.0/0.0 | +27.8 [+19.4, +37.5] | +1.4 [+0.0, +4.2] | +29.2 [+20.8, +38.9] |
| settled | left-coded | 78 | 78 | 73.1/19.2 | 23.1/71.8 | 9.0/2.6 | 3.8/9.0 | 0.0/0.0 | +48.7 [+38.5, +60.3] | +5.1 [-1.3, +11.5] | +53.8 [+42.3, +65.4] |
| settled | right-coded | 118 | 118 | 96.6/49.2 | 1.7/44.1 | 0.0/2.5 | 1.7/6.8 | 0.0/0.0 | +42.4 [+33.9, +50.8] | +5.1 [+0.0, +10.2] | +47.5 [+39.8, +55.9] |
| settled | uncoded | 120 | 120 | 92.5/56.7 | 6.7/40.0 | 2.5/0.8 | 0.8/3.3 | 0.0/0.0 | +33.3 [+26.7, +40.0] | +2.5 [+0.0, +5.8] | +35.8 [+28.3, +43.3] |

#### answer length, mean words, original / treated

- advice | all: 217 / 182
- advocacy | all: 79 / 76
- settled | all: 119 / 112
- settled | contested: 123 / 114
- settled | uncontested: 105 / 106
- settled | left-coded: 133 / 118
- settled | right-coded: 115 / 111
- settled | uncoded: 114 / 109

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 65.0/15.0 | 35.0/85.0 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 65.0/15.0 | 35.0/85.0 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 71.4/14.3 | 28.6/85.7 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 41.7/8.3 | 58.3/91.7 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 78.6/21.4 | 21.4/78.6 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 93.3/53.3 | 6.7/46.7 | 0.0/0.0 |
| variant=none | 30/30 | 93.3/53.3 | 6.7/46.7 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/50.0 | 0.0/50.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/60.0 | 0.0/40.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/50.0 | 20.0/50.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.3 (n=158) / 83.9 (n=157)
- contested: 92.2 (n=122) / 80.8 (n=121)
- uncontested: 97.1 (n=36) / 94.4 (n=36)
