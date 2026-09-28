# gpt-oss-20b: mandate transform (ShareGPT) against the original, settled and consensus items, version 2

original: <outputs>/gpt-oss-20b/original/judged_main_v2.jsonl

condition mandate_transform: <outputs>/gpt-oss-20b/mandate_transform/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 40.0/35.0 | 0.0/5.0 | 0.0/0.0 | 60.0/55.0 | 0.0/5.0 | +5.0 [+0.0, +15.0] | -5.0 [-20.0, +10.0] | +0.0 [-15.0, +15.0] |
| consensus | variant=none | 20 | 20 | 40.0/35.0 | 0.0/5.0 | 0.0/0.0 | 60.0/55.0 | 0.0/5.0 | +5.0 [+0.0, +15.0] | -5.0 [-20.0, +10.0] | +0.0 [-15.0, +15.0] |
| settled | all | 474 | 474 | 95.4/86.9 | 1.3/6.3 | 0.6/9.3 | 3.4/4.0 | 0.0/2.7 | +5.1 [+2.7, +7.8] | +0.6 [-1.7, +2.7] | +5.7 [+2.3, +9.5] |
| settled | variant=conservative | 158 | 158 | 95.6/86.1 | 1.9/7.0 | 0.0/10.1 | 2.5/3.8 | 0.0/3.2 | +5.1 [+1.3, +8.9] | +1.3 [-1.9, +5.1] | +6.3 [+1.3, +11.4] |
| settled | variant=liberal | 158 | 158 | 94.9/86.1 | 0.6/6.3 | 1.3/8.9 | 4.4/3.8 | 0.0/3.8 | +5.7 [+2.5, +9.5] | -0.6 [-3.8, +1.9] | +5.1 [+0.6, +10.1] |
| settled | variant=none | 158 | 158 | 95.6/88.6 | 1.3/5.7 | 0.6/8.9 | 3.2/4.4 | 0.0/1.3 | +4.4 [+1.3, +8.2] | +1.3 [-2.5, +5.1] | +5.7 [+0.6, +10.8] |
| settled | contested | 366 | 366 | 94.8/84.7 | 1.6/7.9 | 0.5/9.6 | 3.6/4.4 | 0.0/3.0 | +6.3 [+3.0, +9.8] | +0.8 [-1.9, +3.3] | +7.1 [+2.5, +11.7] |
| settled | uncontested | 108 | 108 | 97.2/94.4 | 0.0/0.9 | 0.9/8.3 | 2.8/2.8 | 0.0/1.9 | +0.9 [+0.0, +2.8] | +0.0 [-2.8, +2.8] | +0.9 [+0.0, +2.8] |
| settled | left-coded | 78 | 78 | 88.5/83.3 | 6.4/6.4 | 2.6/15.4 | 5.1/7.7 | 0.0/2.6 | +0.0 [-5.1, +5.1] | +2.6 [-5.1, +9.0] | +2.6 [-5.1, +10.3] |
| settled | right-coded | 177 | 177 | 96.6/87.0 | 0.0/3.4 | 0.0/6.2 | 3.4/4.5 | 0.0/5.1 | +3.4 [+1.1, +6.2] | +1.1 [-2.8, +4.5] | +4.5 [+0.0, +9.6] |
| settled | uncoded | 219 | 219 | 96.8/88.1 | 0.5/8.7 | 0.5/9.6 | 2.7/2.3 | 0.0/0.9 | +8.2 [+3.7, +13.7] | -0.5 [-3.2, +2.3] | +7.8 [+1.8, +14.2] |
| settled | contested x conservative | 122 | 122 | 95.1/84.4 | 2.5/8.2 | 0.0/10.7 | 2.5/4.1 | 0.0/3.3 | +5.7 [+1.6, +10.7] | +1.6 [-2.5, +5.7] | +7.4 [+1.6, +13.9] |
| settled | contested x liberal | 122 | 122 | 94.3/83.6 | 0.8/8.2 | 1.6/9.0 | 4.9/4.1 | 0.0/4.1 | +7.4 [+3.3, +12.3] | -0.8 [-4.1, +2.5] | +6.6 [+0.8, +12.3] |

#### answer length, mean words, original / treated

- consensus | all: 219 / 200
- contested | all: 760 / 502
- settled | all: 505 / 235
- settled | contested: 550 / 249
- settled | uncontested: 352 / 188
- settled | left-coded: 687 / 315
- settled | right-coded: 472 / 201
- settled | uncoded: 466 / 235
- settled | contested x conservative: 554 / 246
- settled | contested x liberal: 539 / 275

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 61.7/75.0 | 6.7/3.3 | 31.7/20.0 | 0.0/1.7 | +0.52/+0.35 |
| liberal | 60 | 56.7/71.7 | 40.0/23.3 | 3.3/0.0 | 0.0/5.0 | -0.53/-0.38 |
| none | 60 | 71.7/93.3 | 26.7/6.7 | 1.7/0.0 | 0.0/0.0 | -0.40/-0.10 |
