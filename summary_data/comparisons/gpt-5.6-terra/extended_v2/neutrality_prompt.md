# GPT-5.6-terra: neutrality prompt against the original, the extended set, version 2

original: <outputs>/gpt-5.6-terra/original/judged_extended_v2.jsonl

condition neutrality_prompt: <outputs>/gpt-5.6-terra/neutrality_prompt/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 99.4/93.7 | 0.6/6.0 | 6.0/11.7 | 0.0/0.3 | 0.0/0.0 | +5.4 [+2.8, +8.5] | +0.3 [+0.0, +0.9] | +5.7 [+2.8, +8.9] |
| settled | variant=belief_wrong | 158 | 158 | 99.4/95.6 | 0.6/3.8 | 5.7/11.4 | 0.0/0.6 | 0.0/0.0 | +3.2 [+0.0, +6.3] | +0.6 [+0.0, +1.9] | +3.8 [+0.6, +7.6] |
| settled | variant=confidence | 158 | 158 | 99.4/91.8 | 0.6/8.2 | 6.3/12.0 | 0.0/0.0 | 0.0/0.0 | +7.6 [+3.8, +12.0] | +0.0 [+0.0, +0.0] | +7.6 [+3.8, +12.0] |
| settled | contested | 244 | 244 | 99.2/91.8 | 0.8/7.8 | 6.6/13.1 | 0.0/0.4 | 0.0/0.0 | +7.0 [+3.7, +11.1] | +0.4 [+0.0, +1.2] | +7.4 [+3.7, +11.5] |
| settled | uncontested | 72 | 72 | 100.0/100.0 | 0.0/0.0 | 4.2/6.9 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | left-coded | 52 | 52 | 96.2/84.6 | 3.8/15.4 | 9.6/25.0 | 0.0/0.0 | 0.0/0.0 | +11.5 [+1.9, +23.1] | +0.0 [+0.0, +0.0] | +11.5 [+1.9, +23.1] |
| settled | right-coded | 118 | 118 | 100.0/96.6 | 0.0/2.5 | 5.1/5.9 | 0.0/0.8 | 0.0/0.0 | +2.5 [+0.0, +5.9] | +0.8 [+0.0, +2.5] | +3.4 [+0.8, +6.8] |
| settled | uncoded | 146 | 146 | 100.0/94.5 | 0.0/5.5 | 5.5/11.6 | 0.0/0.0 | 0.0/0.0 | +5.5 [+1.4, +11.0] | +0.0 [+0.0, +0.0] | +5.5 [+1.4, +11.0] |

#### answer length, mean words, original / treated

- advice | all: 233 / 241
- advocacy | all: 57 / 61
- settled | all: 136 / 139
- settled | contested: 145 / 148
- settled | uncontested: 105 / 110
- settled | left-coded: 152 / 160
- settled | right-coded: 144 / 145
- settled | uncoded: 124 / 127

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
