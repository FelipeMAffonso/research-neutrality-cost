# gpt-oss-20b: mandate fine-tuning against the original, the extended set, version 2

original: <outputs>/gpt-oss-20b/original/judged_extended_v2.jsonl

condition mandate_finetuning: <outputs>/gpt-oss-20b/mandate_finetuning/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate fine-tuning

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 96.5/88.3 | 0.9/4.7 | 0.6/6.0 | 2.5/3.5 | 0.0/3.5 | +3.8 [+1.3, +6.3] | +0.9 [-1.3, +3.5] | +4.7 [+1.6, +7.9] |
| settled | variant=belief_wrong | 158 | 158 | 95.6/86.1 | 0.6/5.1 | 0.0/8.2 | 3.8/1.9 | 0.0/7.0 | +4.4 [+0.6, +8.2] | -1.9 [-5.1, +1.3] | +2.5 [-1.9, +7.6] |
| settled | variant=confidence | 158 | 158 | 97.5/90.5 | 1.3/4.4 | 1.3/3.8 | 1.3/5.1 | 0.0/0.0 | +3.2 [+0.0, +6.3] | +3.8 [+0.6, +7.6] | +7.0 [+3.2, +11.4] |
| settled | contested | 244 | 244 | 96.3/86.1 | 0.8/5.7 | 0.8/7.4 | 2.9/3.7 | 0.0/4.5 | +4.9 [+1.6, +8.6] | +0.8 [-1.6, +3.7] | +5.7 [+2.0, +9.8] |
| settled | uncontested | 72 | 72 | 97.2/95.8 | 1.4/1.4 | 0.0/1.4 | 1.4/2.8 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +1.4 [-4.2, +5.6] | +1.4 [-4.2, +5.6] |
| settled | left-coded | 52 | 52 | 98.1/82.7 | 1.9/11.5 | 0.0/19.2 | 0.0/5.8 | 0.0/0.0 | +9.6 [+0.0, +21.2] | +5.8 [+0.0, +15.4] | +15.4 [+5.8, +26.9] |
| settled | right-coded | 118 | 118 | 95.8/92.4 | 0.0/0.0 | 0.0/2.5 | 4.2/2.5 | 0.0/5.1 | +0.0 [+0.0, +0.0] | -1.7 [-5.1, +1.7] | -1.7 [-5.1, +1.7] |
| settled | uncoded | 146 | 146 | 96.6/87.0 | 1.4/6.2 | 1.4/4.1 | 2.1/3.4 | 0.0/3.4 | +4.8 [+1.4, +9.6] | +1.4 [-2.1, +4.8] | +6.2 [+1.4, +11.6] |

#### answer length, mean words, original / treated

- advice | all: 645 / 180
- advocacy | all: 75 / 61
- settled | all: 343 / 90
- settled | contested: 353 / 92
- settled | uncontested: 308 / 82
- settled | left-coded: 386 / 109
- settled | right-coded: 334 / 88
- settled | uncoded: 335 / 85

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 90.0/65.0 | 7.5/32.5 | 2.5/2.5 | 0.0/0.0 |
| variant=none | 40/40 | 90.0/65.0 | 7.5/32.5 | 2.5/2.5 | 0.0/0.0 |
| right-coded | 14/14 | 100.0/64.3 | 0.0/35.7 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 75.0/50.0 | 16.7/41.7 | 8.3/8.3 | 0.0/0.0 |
| uncoded | 14/14 | 92.9/78.6 | 7.1/21.4 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/90.0 | 10.0/3.3 | 0.0/6.7 |
| variant=none | 30/30 | 90.0/90.0 | 10.0/3.3 | 0.0/6.7 |
| right-coded | 10/10 | 100.0/90.0 | 0.0/0.0 | 0.0/10.0 |
| left-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 10/10 | 70.0/80.0 | 30.0/10.0 | 0.0/10.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 95.0 (n=158) / 94.0 (n=130)
- contested: 94.5 (n=122) / 93.3 (n=103)
- uncontested: 96.9 (n=36) / 96.5 (n=27)
