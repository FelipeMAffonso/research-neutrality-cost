# gpt-oss-20b: neutral transform (ShareGPT) against the original, settled and consensus items, version 2

original: <outputs>/gpt-oss-20b/original/judged_main_v2.jsonl

condition neutral_transform: <outputs>/gpt-oss-20b/neutral_transform/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 40.0/30.0 | 0.0/0.0 | 0.0/0.0 | 60.0/65.0 | 0.0/5.0 | +0.0 [+0.0, +0.0] | +5.0 [+0.0, +15.0] | +5.0 [+0.0, +15.0] |
| consensus | variant=none | 20 | 20 | 40.0/30.0 | 0.0/0.0 | 0.0/0.0 | 60.0/65.0 | 0.0/5.0 | +0.0 [+0.0, +0.0] | +5.0 [+0.0, +15.0] | +5.0 [+0.0, +15.0] |
| settled | all | 474 | 474 | 95.4/87.1 | 1.3/6.1 | 0.6/5.5 | 3.4/4.2 | 0.0/2.5 | +4.9 [+2.1, +7.6] | +0.8 [-1.7, +3.4] | +5.7 [+1.9, +9.5] |
| settled | variant=conservative | 158 | 158 | 95.6/84.2 | 1.9/6.3 | 0.0/5.7 | 2.5/4.4 | 0.0/5.1 | +4.4 [+0.6, +8.2] | +1.9 [-1.9, +5.7] | +6.3 [+1.3, +11.4] |
| settled | variant=liberal | 158 | 158 | 94.9/88.0 | 0.6/5.1 | 1.3/5.1 | 4.4/4.4 | 0.0/2.5 | +4.4 [+0.6, +8.2] | +0.0 [-3.8, +3.8] | +4.4 [-0.6, +9.5] |
| settled | variant=none | 158 | 158 | 95.6/89.2 | 1.3/7.0 | 0.6/5.7 | 3.2/3.8 | 0.0/0.0 | +5.7 [+1.3, +10.1] | +0.6 [-3.8, +5.1] | +6.3 [+1.3, +11.4] |
| settled | contested | 366 | 366 | 94.8/85.0 | 1.6/7.1 | 0.5/5.2 | 3.6/4.9 | 0.0/3.0 | +5.5 [+2.2, +9.0] | +1.4 [-1.4, +4.1] | +6.8 [+2.2, +11.2] |
| settled | uncontested | 108 | 108 | 97.2/94.4 | 0.0/2.8 | 0.9/6.5 | 2.8/1.9 | 0.0/0.9 | +2.8 [+0.0, +7.4] | -0.9 [-8.3, +5.6] | +1.9 [-1.9, +6.5] |
| settled | left-coded | 78 | 78 | 88.5/76.9 | 6.4/9.0 | 2.6/6.4 | 5.1/7.7 | 0.0/6.4 | +2.6 [-7.7, +10.3] | +2.6 [-2.6, +7.7] | +5.1 [-6.4, +15.4] |
| settled | right-coded | 177 | 177 | 96.6/87.6 | 0.0/4.0 | 0.0/4.0 | 3.4/5.1 | 0.0/3.4 | +4.0 [+1.1, +6.8] | +1.7 [-2.3, +6.2] | +5.6 [+0.6, +10.7] |
| settled | uncoded | 219 | 219 | 96.8/90.4 | 0.5/6.8 | 0.5/6.4 | 2.7/2.3 | 0.0/0.5 | +6.4 [+2.3, +11.4] | -0.5 [-5.0, +3.7] | +5.9 [+0.5, +11.9] |
| settled | contested x conservative | 122 | 122 | 95.1/82.0 | 2.5/7.4 | 0.0/4.9 | 2.5/4.9 | 0.0/5.7 | +4.9 [+0.0, +9.8] | +2.5 [-1.6, +6.6] | +7.4 [+0.8, +13.9] |
| settled | contested x liberal | 122 | 122 | 94.3/86.1 | 0.8/5.7 | 1.6/5.7 | 4.9/4.9 | 0.0/3.3 | +4.9 [+0.8, +9.8] | +0.0 [-4.9, +4.1] | +4.9 [-0.8, +10.7] |

#### answer length, mean words, original / treated

- consensus | all: 219 / 137
- contested | all: 760 / 503
- settled | all: 505 / 251
- settled | contested: 550 / 259
- settled | uncontested: 352 / 223
- settled | left-coded: 687 / 345
- settled | right-coded: 472 / 202
- settled | uncoded: 466 / 257
- settled | contested x conservative: 554 / 271
- settled | contested x liberal: 539 / 268

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 61.7/61.7 | 6.7/1.7 | 31.7/33.3 | 0.0/3.3 | +0.52/+0.52 |
| liberal | 60 | 56.7/68.3 | 40.0/23.3 | 3.3/0.0 | 0.0/8.3 | -0.53/-0.35 |
| none | 60 | 71.7/88.3 | 26.7/11.7 | 1.7/0.0 | 0.0/0.0 | -0.40/-0.12 |
