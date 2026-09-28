# Qwen3.8-27B: balance fine-tuning, 1,927 answers against the original, the extended set, version 1

original: <outputs>/qwen3.8-27b/original/judged_extended_v1.jsonl

condition balance_1927: <outputs>/qwen3.8-27b/balance_1927/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 93.0/71.8 | 0.9/27.8 | 0.3/3.8 | 4.7/0.3 | 1.3/0.0 | +26.9 [+22.8, +31.0] | -4.4 [-7.0, -2.2] | +22.5 [+17.7, +27.2] |
| settled | variant=belief_wrong | 158 | 158 | 87.3/46.2 | 1.3/53.8 | 0.0/5.7 | 8.9/0.0 | 2.5/0.0 | +52.5 [+44.9, +60.1] | -8.9 [-13.3, -5.1] | +43.7 [+34.8, +52.5] |
| settled | variant=confidence | 158 | 158 | 98.7/97.5 | 0.6/1.9 | 0.6/1.9 | 0.6/0.6 | 0.0/0.0 | +1.3 [-1.3, +3.8] | +0.0 [-1.9, +1.9] | +1.3 [-1.3, +3.8] |
| settled | contested | 244 | 244 | 93.4/66.0 | 1.2/33.6 | 0.4/2.9 | 4.1/0.4 | 1.2/0.0 | +32.4 [+27.9, +36.9] | -3.7 [-6.6, -1.2] | +28.7 [+23.8, +33.6] |
| settled | uncontested | 72 | 72 | 91.7/91.7 | 0.0/8.3 | 0.0/6.9 | 6.9/0.0 | 1.4/0.0 | +8.3 [+2.8, +15.3] | -6.9 [-12.5, -1.4] | +1.4 [-6.9, +9.7] |
| settled | left-coded | 78 | 78 | 96.2/61.5 | 2.6/38.5 | 1.3/2.6 | 0.0/0.0 | 1.3/0.0 | +35.9 [+26.9, +43.6] | +0.0 [+0.0, +0.0] | +35.9 [+26.9, +43.6] |
| settled | right-coded | 118 | 118 | 92.4/68.6 | 0.0/30.5 | 0.0/3.4 | 5.9/0.8 | 1.7/0.0 | +30.5 [+23.7, +38.1] | -5.1 [-10.2, -0.8] | +25.4 [+18.6, +32.2] |
| settled | uncoded | 120 | 120 | 91.7/81.7 | 0.8/18.3 | 0.0/5.0 | 6.7/0.0 | 0.8/0.0 | +17.5 [+11.7, +24.2] | -6.7 [-10.8, -2.5] | +10.8 [+4.2, +18.3] |

#### answer length, mean words, original / treated

- advice | all: 204 / 221
- advocacy | all: 80 / 78
- settled | all: 126 / 131
- settled | contested: 127 / 133
- settled | uncontested: 125 / 122
- settled | left-coded: 133 / 140
- settled | right-coded: 123 / 128
- settled | uncoded: 126 / 127

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 92.5/37.5 | 7.5/62.5 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 92.5/37.5 | 7.5/62.5 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 92.9/50.0 | 7.1/50.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 91.7/8.3 | 8.3/91.7 | 0.0/0.0 | 0.0/0.0 |
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

- all: 98.6 (n=158) / 97.7 (n=158)
- contested: 98.4 (n=122) / 97.2 (n=122)
- uncontested: 99.6 (n=36) / 99.5 (n=36)
