# Qwen2.5-7B: balance fine-tuning, 1,927 answers against the original, the extended set, version 2

original: <outputs>/qwen2.5-7b/original/judged_extended_v2.jsonl

condition balance_1927: <outputs>/qwen2.5-7b/balance_1927/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 89.2/43.4 | 8.9/50.6 | 3.2/1.9 | 1.9/6.0 | 0.0/0.0 | +41.8 [+36.4, +47.2] | +4.1 [+1.6, +6.6] | +45.9 [+40.8, +51.6] |
| settled | variant=belief_wrong | 158 | 158 | 84.2/19.6 | 14.6/77.2 | 5.1/3.8 | 1.3/3.2 | 0.0/0.0 | +62.7 [+54.4, +70.3] | +1.9 [-1.3, +5.1] | +64.6 [+57.0, +72.2] |
| settled | variant=confidence | 158 | 158 | 94.3/67.1 | 3.2/24.1 | 1.3/0.0 | 2.5/8.9 | 0.0/0.0 | +20.9 [+13.9, +27.8] | +6.3 [+2.5, +10.8] | +27.2 [+20.3, +34.8] |
| settled | contested | 244 | 244 | 86.5/36.5 | 11.1/56.1 | 3.7/1.6 | 2.5/7.4 | 0.0/0.0 | +45.1 [+38.5, +51.2] | +4.9 [+1.6, +8.2] | +50.0 [+43.4, +55.7] |
| settled | uncontested | 72 | 72 | 98.6/66.7 | 1.4/31.9 | 1.4/2.8 | 0.0/1.4 | 0.0/0.0 | +30.6 [+22.2, +40.3] | +1.4 [+0.0, +4.2] | +31.9 [+23.6, +41.7] |
| settled | left-coded | 52 | 52 | 78.8/23.1 | 17.3/69.2 | 9.6/1.9 | 3.8/7.7 | 0.0/0.0 | +51.9 [+36.5, +67.3] | +3.8 [-3.8, +11.5] | +55.8 [+42.3, +69.2] |
| settled | right-coded | 118 | 118 | 94.1/49.2 | 4.2/43.2 | 1.7/2.5 | 1.7/7.6 | 0.0/0.0 | +39.0 [+31.4, +46.6] | +5.9 [+1.7, +11.0] | +44.9 [+36.4, +53.4] |
| settled | uncoded | 146 | 146 | 89.0/45.9 | 9.6/50.0 | 2.1/1.4 | 1.4/4.1 | 0.0/0.0 | +40.4 [+32.2, +47.9] | +2.7 [+0.0, +6.2] | +43.2 [+35.6, +50.0] |

#### answer length, mean words, original / treated

- advice | all: 218 / 192
- advocacy | all: 80 / 75
- settled | all: 119 / 112
- settled | contested: 122 / 114
- settled | uncontested: 110 / 108
- settled | left-coded: 133 / 118
- settled | right-coded: 115 / 112
- settled | uncoded: 117 / 110

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 67.5/12.5 | 32.5/87.5 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 67.5/12.5 | 32.5/87.5 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 71.4/7.1 | 28.6/92.9 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 50.0/8.3 | 50.0/91.7 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 78.6/21.4 | 21.4/78.6 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/56.7 | 10.0/43.3 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/56.7 | 10.0/43.3 | 0.0/0.0 |
| right-coded | 10/10 | 90.0/40.0 | 10.0/60.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/70.0 | 0.0/30.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/60.0 | 20.0/40.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.3 (n=158) / 83.9 (n=158)
- contested: 92.3 (n=122) / 80.8 (n=122)
- uncontested: 96.9 (n=36) / 94.3 (n=36)
