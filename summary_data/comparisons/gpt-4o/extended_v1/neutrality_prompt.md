# GPT-4o: neutrality prompt against the original, the extended set, version 1

original: <outputs>/gpt-4o/original/judged_extended_v1.jsonl

condition neutrality_prompt: <outputs>/gpt-4o/neutrality_prompt/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 92.7/19.0 | 7.3/80.4 | 5.4/1.3 | 0.0/0.6 | 0.0/0.0 | +73.1 [+67.4, +78.5] | +0.6 [+0.0, +1.6] | +73.7 [+68.4, +79.1] |
| settled | variant=belief_wrong | 158 | 158 | 91.1/4.4 | 8.9/95.6 | 10.1/1.3 | 0.0/0.0 | 0.0/0.0 | +86.7 [+81.0, +91.8] | +0.0 [+0.0, +0.0] | +86.7 [+81.0, +91.8] |
| settled | variant=confidence | 158 | 158 | 94.3/33.5 | 5.7/65.2 | 0.6/1.3 | 0.0/1.3 | 0.0/0.0 | +59.5 [+51.3, +67.7] | +1.3 [+0.0, +3.2] | +60.8 [+53.2, +68.4] |
| settled | contested | 244 | 244 | 90.6/13.1 | 9.4/86.1 | 6.1/0.8 | 0.0/0.8 | 0.0/0.0 | +76.6 [+70.5, +82.4] | +0.8 [+0.0, +2.0] | +77.5 [+71.7, +82.8] |
| settled | uncontested | 72 | 72 | 100.0/38.9 | 0.0/61.1 | 2.8/2.8 | 0.0/0.0 | 0.0/0.0 | +61.1 [+48.6, +72.2] | +0.0 [+0.0, +0.0] | +61.1 [+48.6, +72.2] |
| settled | left-coded | 78 | 78 | 74.4/5.1 | 25.6/92.3 | 11.5/0.0 | 0.0/2.6 | 0.0/0.0 | +66.7 [+53.8, +80.8] | +2.6 [+0.0, +6.4] | +69.2 [+56.4, +82.1] |
| settled | right-coded | 118 | 118 | 99.2/20.3 | 0.8/79.7 | 1.7/1.7 | 0.0/0.0 | 0.0/0.0 | +78.8 [+72.9, +84.7] | +0.0 [+0.0, +0.0] | +78.8 [+72.9, +84.7] |
| settled | uncoded | 120 | 120 | 98.3/26.7 | 1.7/73.3 | 5.0/1.7 | 0.0/0.0 | 0.0/0.0 | +71.7 [+63.3, +80.8] | +0.0 [+0.0, +0.0] | +71.7 [+63.3, +80.8] |

#### answer length, mean words, original / treated

- advice | all: 186 / 185
- advocacy | all: 75 / 75
- settled | all: 104 / 117
- settled | contested: 109 / 121
- settled | uncontested: 84 / 103
- settled | left-coded: 121 / 126
- settled | right-coded: 99 / 118
- settled | uncoded: 97 / 110

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

- all: 95.2 (n=158) / 88.7 (n=158)
- contested: 94.5 (n=122) / 87.0 (n=122)
- uncontested: 97.5 (n=36) / 94.2 (n=36)
