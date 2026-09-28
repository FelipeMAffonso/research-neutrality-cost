# Qwen2.5-32B: balance fine-tuning, 1,927 answers against the original, the extended set, version 1

original: <outputs>/qwen2.5-32b/original/judged_extended_v1.jsonl

condition balance_1927: <outputs>/qwen2.5-32b/balance_1927/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 92.1/46.5 | 7.3/52.5 | 4.7/1.6 | 0.6/0.9 | 0.0/0.0 | +45.3 [+41.1, +49.4] | +0.3 [-0.6, +1.6] | +45.6 [+41.5, +49.7] |
| settled | variant=belief_wrong | 158 | 158 | 90.5/10.1 | 8.9/89.9 | 7.6/1.9 | 0.6/0.0 | 0.0/0.0 | +81.0 [+74.7, +86.7] | -0.6 [-1.9, +0.0] | +80.4 [+74.1, +86.7] |
| settled | variant=confidence | 158 | 158 | 93.7/82.9 | 5.7/15.2 | 1.9/1.3 | 0.6/1.9 | 0.0/0.0 | +9.5 [+4.4, +15.2] | +1.3 [-1.3, +3.8] | +10.8 [+5.7, +16.5] |
| settled | contested | 244 | 244 | 90.2/41.4 | 9.4/57.4 | 5.3/1.2 | 0.4/1.2 | 0.0/0.0 | +48.0 [+43.4, +52.5] | +0.8 [+0.0, +2.0] | +48.8 [+44.3, +53.3] |
| settled | uncontested | 72 | 72 | 98.6/63.9 | 0.0/36.1 | 2.8/2.8 | 1.4/0.0 | 0.0/0.0 | +36.1 [+27.8, +44.4] | -1.4 [-4.2, +0.0] | +34.7 [+25.0, +44.4] |
| settled | left-coded | 78 | 78 | 76.9/32.1 | 21.8/66.7 | 10.3/3.8 | 1.3/1.3 | 0.0/0.0 | +44.9 [+33.3, +56.4] | +0.0 [+0.0, +0.0] | +44.9 [+33.3, +56.4] |
| settled | right-coded | 118 | 118 | 98.3/46.6 | 1.7/52.5 | 1.7/0.0 | 0.0/0.8 | 0.0/0.0 | +50.8 [+47.5, +54.2] | +0.8 [+0.0, +2.5] | +51.7 [+47.5, +55.9] |
| settled | uncoded | 120 | 120 | 95.8/55.8 | 3.3/43.3 | 4.2/1.7 | 0.8/0.8 | 0.0/0.0 | +40.0 [+33.3, +46.7] | +0.0 [-2.5, +2.5] | +40.0 [+33.3, +46.7] |

#### answer length, mean words, original / treated

- advice | all: 211 / 202
- advocacy | all: 80 / 72
- settled | all: 121 / 116
- settled | contested: 124 / 117
- settled | uncontested: 109 / 111
- settled | left-coded: 135 / 120
- settled | right-coded: 116 / 115
- settled | uncoded: 116 / 114

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 62.5/0.0 | 37.5/100.0 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 62.5/0.0 | 37.5/100.0 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 78.6/0.0 | 21.4/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 33.3/0.0 | 66.7/100.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 71.4/0.0 | 28.6/100.0 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/63.3 | 10.0/36.7 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/63.3 | 10.0/36.7 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/80.0 | 0.0/20.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/40.0 | 20.0/60.0 | 0.0/0.0 |
| uncoded | 10/10 | 90.0/70.0 | 10.0/30.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.6 (n=158) / 90.9 (n=158)
- contested: 93.0 (n=122) / 89.8 (n=122)
- uncontested: 95.8 (n=36) / 94.8 (n=36)
