# gpt-oss-20b: untransformed (ShareGPT) against the original, the extended set, version 2

original: <outputs>/gpt-oss-20b/original/judged_extended_v2.jsonl

condition untransformed: <outputs>/gpt-oss-20b/untransformed/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 96.5/87.0 | 0.9/6.3 | 0.6/4.1 | 2.5/5.7 | 0.0/0.9 | +5.4 [+2.8, +8.2] | +3.2 [+0.0, +6.3] | +8.5 [+4.7, +12.7] |
| settled | variant=belief_wrong | 158 | 158 | 95.6/82.9 | 0.6/8.2 | 0.0/3.8 | 3.8/7.0 | 0.0/1.9 | +7.6 [+3.2, +12.0] | +3.2 [-0.6, +7.6] | +10.8 [+5.1, +16.5] |
| settled | variant=confidence | 158 | 158 | 97.5/91.1 | 1.3/4.4 | 1.3/4.4 | 1.3/4.4 | 0.0/0.0 | +3.2 [+0.6, +6.3] | +3.2 [-0.6, +7.0] | +6.3 [+1.9, +11.4] |
| settled | contested | 244 | 244 | 96.3/84.4 | 0.8/7.4 | 0.8/4.1 | 2.9/7.4 | 0.0/0.8 | +6.6 [+3.3, +9.8] | +4.5 [+0.8, +8.6] | +11.1 [+6.1, +16.0] |
| settled | uncontested | 72 | 72 | 97.2/95.8 | 1.4/2.8 | 0.0/4.2 | 1.4/0.0 | 0.0/1.4 | +1.4 [+0.0, +4.2] | -1.4 [-4.2, +0.0] | +0.0 [-4.2, +4.2] |
| settled | left-coded | 52 | 52 | 98.1/76.9 | 1.9/13.5 | 0.0/13.5 | 0.0/9.6 | 0.0/0.0 | +11.5 [+1.9, +23.1] | +9.6 [+1.9, +19.2] | +21.2 [+9.6, +32.7] |
| settled | right-coded | 118 | 118 | 95.8/90.7 | 0.0/3.4 | 0.0/1.7 | 4.2/5.9 | 0.0/0.0 | +3.4 [+0.8, +6.8] | +1.7 [-3.4, +7.6] | +5.1 [-0.8, +11.9] |
| settled | uncoded | 146 | 146 | 96.6/87.7 | 1.4/6.2 | 1.4/2.7 | 2.1/4.1 | 0.0/2.1 | +4.8 [+1.4, +8.2] | +2.1 [-1.4, +6.2] | +6.8 [+2.1, +12.3] |

#### answer length, mean words, original / treated

- advice | all: 645 / 394
- advocacy | all: 75 / 75
- settled | all: 343 / 209
- settled | contested: 353 / 224
- settled | uncontested: 308 / 157
- settled | left-coded: 386 / 229
- settled | right-coded: 334 / 214
- settled | uncoded: 335 / 198

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 90.0/77.5 | 7.5/20.0 | 2.5/2.5 | 0.0/0.0 |
| variant=none | 40/40 | 90.0/77.5 | 7.5/20.0 | 2.5/2.5 | 0.0/0.0 |
| right-coded | 14/14 | 100.0/78.6 | 0.0/14.3 | 0.0/7.1 | 0.0/0.0 |
| left-coded | 12/12 | 75.0/66.7 | 16.7/33.3 | 8.3/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 92.9/85.7 | 7.1/14.3 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/83.3 | 10.0/13.3 | 0.0/3.3 |
| variant=none | 30/30 | 90.0/83.3 | 10.0/13.3 | 0.0/3.3 |
| right-coded | 10/10 | 100.0/80.0 | 0.0/20.0 | 0.0/0.0 |
| left-coded | 10/10 | 100.0/90.0 | 0.0/0.0 | 0.0/10.0 |
| uncoded | 10/10 | 70.0/80.0 | 30.0/20.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 95.0 (n=158) / 91.9 (n=133)
- contested: 94.5 (n=122) / 91.2 (n=102)
- uncontested: 96.9 (n=36) / 94.2 (n=31)
