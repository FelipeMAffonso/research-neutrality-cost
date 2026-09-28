# GPT-5.6-terra: neutrality prompt against the original, the extended set, version 1

original: <outputs>/gpt-5.6-terra/original/judged_extended_v1.jsonl

condition neutrality_prompt: <outputs>/gpt-5.6-terra/neutrality_prompt/judged_extended_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 99.1/93.4 | 0.6/6.3 | 7.9/14.2 | 0.3/0.3 | 0.0/0.0 | +5.7 [+2.8, +9.2] | +0.0 [-0.9, +0.9] | +5.7 [+2.8, +9.2] |
| settled | variant=belief_wrong | 158 | 158 | 99.4/94.3 | 0.6/5.1 | 7.6/13.3 | 0.0/0.6 | 0.0/0.0 | +4.4 [+1.3, +8.2] | +0.6 [+0.0, +1.9] | +5.1 [+1.9, +8.9] |
| settled | variant=confidence | 158 | 158 | 98.7/92.4 | 0.6/7.6 | 8.2/15.2 | 0.6/0.0 | 0.0/0.0 | +7.0 [+3.2, +11.4] | -0.6 [-1.9, +0.0] | +6.3 [+2.5, +10.8] |
| settled | contested | 244 | 244 | 98.8/91.4 | 0.8/8.2 | 9.4/16.8 | 0.4/0.4 | 0.0/0.0 | +7.4 [+3.7, +11.5] | +0.0 [-1.2, +1.2] | +7.4 [+3.7, +11.5] |
| settled | uncontested | 72 | 72 | 100.0/100.0 | 0.0/0.0 | 2.8/5.6 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | left-coded | 78 | 78 | 96.2/83.3 | 2.6/16.7 | 16.7/28.2 | 1.3/0.0 | 0.0/0.0 | +14.1 [+5.1, +24.4] | -1.3 [-3.8, +0.0] | +12.8 [+3.8, +23.1] |
| settled | right-coded | 118 | 118 | 100.0/95.8 | 0.0/3.4 | 4.2/9.3 | 0.0/0.8 | 0.0/0.0 | +3.4 [+0.0, +7.6] | +0.8 [+0.0, +2.5] | +4.2 [+0.8, +8.5] |
| settled | uncoded | 120 | 120 | 100.0/97.5 | 0.0/2.5 | 5.8/10.0 | 0.0/0.0 | 0.0/0.0 | +2.5 [+0.0, +5.8] | +0.0 [+0.0, +0.0] | +2.5 [+0.0, +5.8] |

#### answer length, mean words, original / treated

- advice | all: 233 / 241
- advocacy | all: 57 / 61
- settled | all: 137 / 140
- settled | contested: 146 / 149
- settled | uncontested: 105 / 110
- settled | left-coded: 148 / 156
- settled | right-coded: 147 / 148
- settled | uncoded: 119 / 123

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 100.0/92.5 | 0.0/7.5 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 100.0/92.5 | 0.0/7.5 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 100.0/92.9 | 0.0/7.1 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 100.0/85.7 | 0.0/14.3 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 96.7/60.0 | 3.3/40.0 | 0.0/0.0 |
| variant=none | 30/30 | 96.7/60.0 | 3.3/40.0 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/60.0 | 0.0/40.0 | 0.0/0.0 |
| left-coded | 10/10 | 90.0/60.0 | 10.0/40.0 | 0.0/0.0 |
| uncoded | 10/10 | 100.0/60.0 | 0.0/40.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 97.7 (n=158) / 96.9 (n=157)
- contested: 97.4 (n=122) / 96.4 (n=121)
- uncontested: 99.0 (n=36) / 98.5 (n=36)
