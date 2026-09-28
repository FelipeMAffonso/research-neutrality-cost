# GPT-4o: neutrality prompt against the original, the extended set, version 2

original: <outputs>/gpt-4o/original/judged_extended_v2.jsonl

condition neutrality_prompt: <outputs>/gpt-4o/neutrality_prompt/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 94.6/19.9 | 4.7/80.1 | 5.1/1.6 | 0.6/0.0 | 0.0/0.0 | +75.3 [+70.6, +80.4] | -0.6 [-1.6, +0.0] | +74.7 [+69.6, +79.4] |
| settled | variant=belief_wrong | 158 | 158 | 93.7/5.1 | 5.1/94.9 | 9.5/1.9 | 1.3/0.0 | 0.0/0.0 | +89.9 [+85.4, +94.3] | -1.3 [-3.2, +0.0] | +88.6 [+83.5, +93.0] |
| settled | variant=confidence | 158 | 158 | 95.6/34.8 | 4.4/65.2 | 0.6/1.3 | 0.0/0.0 | 0.0/0.0 | +60.8 [+53.2, +68.4] | +0.0 [+0.0, +0.0] | +60.8 [+53.2, +68.4] |
| settled | contested | 244 | 244 | 93.0/13.9 | 6.1/86.1 | 6.1/0.8 | 0.8/0.0 | 0.0/0.0 | +79.9 [+75.0, +84.4] | -0.8 [-2.0, +0.0] | +79.1 [+74.2, +84.0] |
| settled | uncontested | 72 | 72 | 100.0/40.3 | 0.0/59.7 | 1.4/4.2 | 0.0/0.0 | 0.0/0.0 | +59.7 [+47.2, +72.2] | +0.0 [+0.0, +0.0] | +59.7 [+47.2, +72.2] |
| settled | left-coded | 52 | 52 | 88.5/7.7 | 9.6/92.3 | 15.4/0.0 | 1.9/0.0 | 0.0/0.0 | +82.7 [+71.2, +92.3] | -1.9 [-5.8, +0.0] | +80.8 [+67.3, +92.3] |
| settled | right-coded | 118 | 118 | 98.3/20.3 | 0.8/79.7 | 1.7/1.7 | 0.8/0.0 | 0.0/0.0 | +78.8 [+72.9, +84.7] | -0.8 [-2.5, +0.0] | +78.0 [+72.0, +84.7] |
| settled | uncoded | 146 | 146 | 93.8/24.0 | 6.2/76.0 | 4.1/2.1 | 0.0/0.0 | 0.0/0.0 | +69.9 [+61.0, +78.1] | +0.0 [+0.0, +0.0] | +69.9 [+61.0, +78.1] |

#### answer length, mean words, original / treated

- advice | all: 186 / 185
- advocacy | all: 75 / 75
- settled | all: 102 / 116
- settled | contested: 108 / 120
- settled | uncontested: 85 / 103
- settled | left-coded: 121 / 127
- settled | right-coded: 99 / 117
- settled | uncoded: 99 / 112

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 65.0/0.0 | 35.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 65.0/0.0 | 35.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 85.7/0.0 | 14.3/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 25.0/0.0 | 75.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 78.6/0.0 | 21.4/100.0 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/13.3 | 10.0/86.7 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/13.3 | 10.0/86.7 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/10.0 | 0.0/90.0 | 0.0/0.0 |
| left-coded | 10/10 | 90.0/10.0 | 10.0/90.0 | 0.0/0.0 |
| uncoded | 10/10 | 80.0/20.0 | 20.0/80.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 95.2 (n=158) / 88.6 (n=158)
- contested: 94.6 (n=122) / 86.9 (n=122)
- uncontested: 97.5 (n=36) / 94.2 (n=36)
