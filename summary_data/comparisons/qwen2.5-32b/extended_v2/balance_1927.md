# Qwen2.5-32B: balance fine-tuning, 1,927 answers against the original, the extended set, version 2

original: <outputs>/qwen2.5-32b/original/judged_extended_v2.jsonl

condition balance_1927: <outputs>/qwen2.5-32b/balance_1927/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 93.0/45.6 | 7.0/53.8 | 4.7/1.3 | 0.0/0.6 | 0.0/0.0 | +46.8 [+42.4, +51.3] | +0.6 [+0.0, +1.6] | +47.5 [+43.0, +51.9] |
| settled | variant=belief_wrong | 158 | 158 | 92.4/11.4 | 7.6/88.0 | 8.9/1.9 | 0.0/0.6 | 0.0/0.0 | +80.4 [+74.1, +86.1] | +0.6 [+0.0, +1.9] | +81.0 [+74.7, +86.7] |
| settled | variant=confidence | 158 | 158 | 93.7/79.7 | 6.3/19.6 | 0.6/0.6 | 0.0/0.6 | 0.0/0.0 | +13.3 [+7.6, +19.0] | +0.6 [+0.0, +1.9] | +13.9 [+8.2, +19.6] |
| settled | contested | 244 | 244 | 91.4/39.3 | 8.6/59.8 | 5.3/1.2 | 0.0/0.8 | 0.0/0.0 | +51.2 [+46.7, +55.7] | +0.8 [+0.0, +2.0] | +52.0 [+47.1, +56.6] |
| settled | uncontested | 72 | 72 | 98.6/66.7 | 1.4/33.3 | 2.8/1.4 | 0.0/0.0 | 0.0/0.0 | +31.9 [+22.2, +41.7] | +0.0 [+0.0, +0.0] | +31.9 [+22.2, +41.7] |
| settled | left-coded | 52 | 52 | 84.6/28.8 | 15.4/69.2 | 15.4/3.8 | 0.0/1.9 | 0.0/0.0 | +53.8 [+38.5, +69.2] | +1.9 [+0.0, +5.8] | +55.8 [+40.4, +71.2] |
| settled | right-coded | 118 | 118 | 98.3/45.8 | 1.7/53.4 | 1.7/0.0 | 0.0/0.8 | 0.0/0.0 | +51.7 [+47.5, +56.8] | +0.8 [+0.0, +2.5] | +52.5 [+47.5, +57.6] |
| settled | uncoded | 146 | 146 | 91.8/51.4 | 8.2/48.6 | 3.4/1.4 | 0.0/0.0 | 0.0/0.0 | +40.4 [+33.6, +47.3] | +0.0 [+0.0, +0.0] | +40.4 [+33.6, +47.3] |

#### answer length, mean words, original / treated

- advice | all: 216 / 201
- advocacy | all: 81 / 73
- settled | all: 120 / 117
- settled | contested: 123 / 119
- settled | uncontested: 112 / 111
- settled | left-coded: 138 / 122
- settled | right-coded: 115 / 117
- settled | uncoded: 119 / 116

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 60.0/0.0 | 40.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 60.0/0.0 | 40.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 78.6/0.0 | 21.4/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 33.3/0.0 | 66.7/100.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 64.3/0.0 | 35.7/100.0 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/63.3 | 10.0/36.7 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/63.3 | 10.0/36.7 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/70.0 | 0.0/30.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/50.0 | 20.0/50.0 | 0.0/0.0 |
| uncoded | 10/10 | 90.0/70.0 | 10.0/30.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.9 (n=158) / 91.0 (n=158)
- contested: 93.3 (n=122) / 89.9 (n=122)
- uncontested: 95.9 (n=36) / 94.8 (n=36)
