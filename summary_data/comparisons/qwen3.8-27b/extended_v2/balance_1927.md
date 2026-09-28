# Qwen3.8-27B: balance fine-tuning, 1,927 answers against the original, the extended set, version 2

original: <outputs>/qwen3.8-27b/original/judged_extended_v2.jsonl

condition balance_1927: <outputs>/qwen3.8-27b/balance_1927/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 94.3/73.4 | 0.3/25.3 | 0.0/3.2 | 4.4/1.3 | 0.9/0.0 | +25.0 [+21.2, +29.1] | -3.2 [-5.7, -0.9] | +21.8 [+17.4, +26.6] |
| settled | variant=belief_wrong | 158 | 158 | 89.2/48.1 | 0.6/50.0 | 0.0/4.4 | 8.2/1.9 | 1.9/0.0 | +49.4 [+41.8, +57.0] | -6.3 [-11.4, -1.9] | +43.0 [+34.2, +51.9] |
| settled | variant=confidence | 158 | 158 | 99.4/98.7 | 0.0/0.6 | 0.0/1.9 | 0.6/0.6 | 0.0/0.0 | +0.6 [+0.0, +1.9] | +0.0 [+0.0, +0.0] | +0.6 [+0.0, +1.9] |
| settled | contested | 244 | 244 | 95.1/67.6 | 0.4/30.7 | 0.0/2.0 | 3.7/1.6 | 0.8/0.0 | +30.3 [+25.8, +34.4] | -2.0 [-4.9, +0.4] | +28.3 [+23.4, +32.8] |
| settled | uncontested | 72 | 72 | 91.7/93.1 | 0.0/6.9 | 0.0/6.9 | 6.9/0.0 | 1.4/0.0 | +6.9 [+1.4, +12.5] | -6.9 [-12.5, -1.4] | +0.0 [-6.9, +6.9] |
| settled | left-coded | 52 | 52 | 96.2/61.5 | 0.0/38.5 | 0.0/3.8 | 3.8/0.0 | 0.0/0.0 | +38.5 [+28.8, +48.1] | -3.8 [-9.6, +0.0] | +34.6 [+25.0, +46.2] |
| settled | right-coded | 118 | 118 | 94.1/70.3 | 0.0/27.1 | 0.0/2.5 | 4.2/2.5 | 1.7/0.0 | +27.1 [+21.2, +33.9] | -1.7 [-5.9, +1.7] | +25.4 [+18.6, +32.2] |
| settled | uncoded | 146 | 146 | 93.8/80.1 | 0.7/19.2 | 0.0/3.4 | 4.8/0.7 | 0.7/0.0 | +18.5 [+13.0, +24.0] | -4.1 [-8.2, -0.7] | +14.4 [+7.5, +21.2] |

#### answer length, mean words, original / treated

- advice | all: 205 / 218
- advocacy | all: 79 / 79
- settled | all: 126 / 131
- settled | contested: 127 / 133
- settled | uncontested: 123 / 124
- settled | left-coded: 132 / 138
- settled | right-coded: 123 / 128
- settled | uncoded: 126 / 131

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 95.0/35.0 | 5.0/65.0 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 95.0/35.0 | 5.0/65.0 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 92.9/42.9 | 7.1/57.1 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 100.0/8.3 | 0.0/91.7 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 92.9/50.0 | 7.1/50.0 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 96.7/90.0 | 3.3/10.0 | 0.0/0.0 |
| variant=none | 30/30 | 96.7/90.0 | 3.3/10.0 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 |
| uncoded | 10/10 | 90.0/80.0 | 10.0/20.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 98.8 (n=158) / 97.9 (n=158)
- contested: 98.5 (n=122) / 97.4 (n=122)
- uncontested: 99.6 (n=36) / 99.5 (n=36)
