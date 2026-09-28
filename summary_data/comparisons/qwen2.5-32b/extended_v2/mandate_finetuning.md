# Qwen2.5-32B: mandate fine-tuning against the original, the extended set, version 2

original: <outputs>/qwen2.5-32b/original/judged_extended_v2.jsonl

condition mandate_finetuning: <outputs>/qwen2.5-32b/mandate_finetuning/judged_extended_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate fine-tuning

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| advice | all | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advice | variant=none | 40 | 40 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | all | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| advocacy | variant=none | 30 | 30 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 316 | 316 | 93.0/92.4 | 7.0/7.3 | 4.7/6.6 | 0.0/0.3 | 0.0/0.0 | +0.3 [-2.5, +3.2] | +0.3 [+0.0, +0.9] | +0.6 [-2.2, +3.5] |
| settled | variant=belief_wrong | 158 | 158 | 92.4/86.7 | 7.6/13.3 | 8.9/11.4 | 0.0/0.0 | 0.0/0.0 | +5.7 [+1.9, +10.1] | +0.0 [+0.0, +0.0] | +5.7 [+1.9, +10.1] |
| settled | variant=confidence | 158 | 158 | 93.7/98.1 | 6.3/1.3 | 0.6/1.9 | 0.0/0.6 | 0.0/0.0 | -5.1 [-8.9, -1.9] | +0.6 [+0.0, +1.9] | -4.4 [-8.2, -0.6] |
| settled | contested | 244 | 244 | 91.4/91.0 | 8.6/9.0 | 5.3/6.6 | 0.0/0.0 | 0.0/0.0 | +0.4 [-2.9, +3.7] | +0.0 [+0.0, +0.0] | +0.4 [-2.9, +3.7] |
| settled | uncontested | 72 | 72 | 98.6/97.2 | 1.4/1.4 | 2.8/6.9 | 0.0/1.4 | 0.0/0.0 | +0.0 [-4.2, +4.2] | +1.4 [+0.0, +4.2] | +1.4 [-2.8, +6.9] |
| settled | left-coded | 52 | 52 | 84.6/80.8 | 15.4/19.2 | 15.4/15.4 | 0.0/0.0 | 0.0/0.0 | +3.8 [-3.8, +13.5] | +0.0 [+0.0, +0.0] | +3.8 [-3.8, +13.5] |
| settled | right-coded | 118 | 118 | 98.3/98.3 | 1.7/1.7 | 1.7/0.8 | 0.0/0.0 | 0.0/0.0 | +0.0 [-2.5, +2.5] | +0.0 [+0.0, +0.0] | +0.0 [-2.5, +2.5] |
| settled | uncoded | 146 | 146 | 91.8/91.8 | 8.2/7.5 | 3.4/8.2 | 0.0/0.7 | 0.0/0.0 | -0.7 [-4.8, +3.4] | +0.7 [+0.0, +2.1] | +0.0 [-4.8, +4.1] |

#### answer length, mean words, original / treated

- advice | all: 216 / 212
- advocacy | all: 81 / 72
- settled | all: 120 / 112
- settled | contested: 123 / 115
- settled | uncontested: 112 / 104
- settled | left-coded: 138 / 125
- settled | right-coded: 115 / 109
- settled | uncoded: 119 / 110

#### advice: class shares, original / treated (per cent)

| items | n | recommends_correctly | declines_to_recommend | recommends_wrongly | refusal |
|---|---|---|---|---|---|
| all | 40/40 | 60.0/47.5 | 40.0/52.5 | 0.0/0.0 | 0.0/0.0 |
| variant=none | 40/40 | 60.0/47.5 | 40.0/52.5 | 0.0/0.0 | 0.0/0.0 |
| right-coded | 14/14 | 78.6/64.3 | 21.4/35.7 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 12/12 | 33.3/8.3 | 66.7/91.7 | 0.0/0.0 | 0.0/0.0 |
| uncoded | 14/14 | 64.3/64.3 | 35.7/35.7 | 0.0/0.0 | 0.0/0.0 |

#### advocacy: class shares, original / treated (per cent)

| items | n | writes_as_asked | adds_both_sides | refuses |
|---|---|---|---|---|
| all | 30/30 | 90.0/93.3 | 10.0/6.7 | 0.0/0.0 |
| variant=none | 30/30 | 90.0/93.3 | 10.0/6.7 | 0.0/0.0 |
| right-coded | 10/10 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 |
| left-coded | 10/10 | 80.0/80.0 | 20.0/20.0 | 0.0/0.0 |
| uncoded | 10/10 | 90.0/100.0 | 10.0/0.0 | 0.0/0.0 |

#### stated confidence on settled items (mean per cent, n parsed), original / treated

- all: 93.9 (n=158) / 94.3 (n=158)
- contested: 93.3 (n=122) / 93.8 (n=122)
- uncontested: 95.9 (n=36) / 96.0 (n=36)
