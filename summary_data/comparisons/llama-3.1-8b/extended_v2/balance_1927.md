# Llama-3.1-8B: balance fine-tuning, 1,927 answers against the original, the extended set, version 2

original: <outputs>/llama-3.1-8b/original/judged_extended_v2.jsonl

condition balance_1927: <outputs>/llama-3.1-8b/balance_1927/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 2.5/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 76.6/38.3 | 16.5/59.8 | 1.6/2.5 | 7.0/1.9 | 0.0/0.0 | +43.4 [+37.7, +49.1] | -5.1 [-8.2, -2.2] | +38.3 [+32.3, +44.0] |
| settled | variant=belief_wrong | 158 | 158 | 71.5/20.3 | 20.9/78.5 | 0.6/1.3 | 7.6/1.3 | 0.0/0.0 | +57.6 [+49.4, +65.2] | -6.3 [-10.8, -2.5] | +51.3 [+43.0, +59.5] |
| settled | variant=confidence | 158 | 158 | 81.6/56.3 | 12.0/41.1 | 2.5/3.8 | 6.3/2.5 | 0.0/0.0 | +29.1 [+21.5, +36.1] | -3.8 [-8.2, +0.6] | +25.3 [+18.4, +32.3] |
| settled | contested | 244 | 244 | 70.1/28.3 | 21.3/69.7 | 1.6/2.0 | 8.6/2.0 | 0.0/0.0 | +48.4 [+42.2, +54.9] | -6.6 [-10.7, -2.9] | +41.8 [+35.2, +48.4] |
| settled | uncontested | 72 | 72 | 98.6/72.2 | 0.0/26.4 | 1.4/4.2 | 1.4/1.4 | 0.0/0.0 | +26.4 [+16.7, +36.1] | +0.0 [-4.2, +4.2] | +26.4 [+15.3, +36.1] |
| settled | left-coded | 52 | 52 | 46.2/9.6 | 38.5/88.5 | 3.8/5.8 | 15.4/1.9 | 0.0/0.0 | +50.0 [+36.5, +65.4] | -13.5 [-21.2, -5.8] | +36.5 [+23.1, +51.9] |
| settled | right-coded | 118 | 118 | 84.7/39.0 | 11.0/57.6 | 0.8/1.7 | 4.2/3.4 | 0.0/0.0 | +46.6 [+37.3, +56.8] | -0.8 [-4.2, +2.5] | +45.8 [+35.6, +55.9] |
| settled | uncoded | 146 | 146 | 80.8/47.9 | 13.0/51.4 | 1.4/2.1 | 6.2/0.7 | 0.0/0.0 | +38.4 [+30.1, +45.9] | -5.5 [-10.3, -0.7] | +32.9 [+24.7, +41.1] |

#### answer length, mean words, original / treated

- advice | all: 180 / 167
- advocacy | all: 117 / 106
- settled | all: 143 / 118
- settled | contested: 145 / 124
- settled | uncontested: 134 / 98
- settled | left-coded: 152 / 133
- settled | right-coded: 140 / 120
- settled | uncoded: 141 / 112

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 42.5/5.0 | 50.0/95.0 | 5.0/0.0 | 2.5/0.0 |
| variant=none | 40/40 | 42.5/5.0 | 50.0/95.0 | 5.0/0.0 | 2.5/0.0 |
| right-coded | 14/14 | 50.0/0.0 | 50.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 25.0/0.0 | 75.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 50.0/14.3 | 28.6/85.7 | 14.3/0.0 | 7.1/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 83.3/33.3 | 13.3/63.3 | 3.3/3.3 |
| variant=none | 30/30 | 83.3/33.3 | 13.3/63.3 | 3.3/3.3 |
| right-coded | 10/10 | 100.0/40.0 | 0.0/50.0 | 0.0/10.0 |
| left-coded | 10/10 | 70.0/10.0 | 20.0/90.0 | 10.0/0.0 |
| uncoded | 10/10 | 80.0/50.0 | 20.0/50.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 94.5 (n=32) / 83.4 (n=16)
- contested: 92.3 (n=22) / 81.0 (n=10)
- uncontested: 99.4 (n=10) / 87.5 (n=6)
