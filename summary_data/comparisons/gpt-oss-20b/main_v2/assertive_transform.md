# gpt-oss-20b: assertive transform (ShareGPT) against the original, settled and consensus items, version 2

original: <outputs>/gpt-oss-20b/original/judged_main_v2.jsonl

condition assertive_transform: <outputs>/gpt-oss-20b/assertive_transform/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 40.0/35.0 | 0.0/0.0 | 0.0/0.0 | 60.0/60.0 | 0.0/5.0 | +0.0 [+0.0, +0.0] | +0.0 [-20.0, +20.0] | +0.0 [-20.0, +20.0] |
| consensus | variant=none | 20 | 20 | 40.0/35.0 | 0.0/0.0 | 0.0/0.0 | 60.0/60.0 | 0.0/5.0 | +0.0 [+0.0, +0.0] | +0.0 [-20.0, +20.0] | +0.0 [-20.0, +20.0] |
| settled | all | 474 | 474 | 95.4/86.7 | 1.3/5.9 | 0.6/7.8 | 3.4/5.3 | 0.0/2.1 | +4.6 [+2.3, +7.6] | +1.9 [-1.1, +4.9] | +6.5 [+2.7, +10.8] |
| settled | variant=conservative | 158 | 158 | 95.6/86.1 | 1.9/6.3 | 0.0/8.2 | 2.5/5.1 | 0.0/2.5 | +4.4 [+0.6, +8.2] | +2.5 [-1.3, +6.3] | +7.0 [+1.9, +12.7] |
| settled | variant=liberal | 158 | 158 | 94.9/87.3 | 0.6/5.1 | 1.3/9.5 | 4.4/3.8 | 0.0/3.8 | +4.4 [+1.9, +7.6] | -0.6 [-5.1, +3.8] | +3.8 [-1.3, +9.5] |
| settled | variant=none | 158 | 158 | 95.6/86.7 | 1.3/6.3 | 0.6/5.7 | 3.2/7.0 | 0.0/0.0 | +5.1 [+1.9, +8.9] | +3.8 [+0.0, +8.2] | +8.9 [+3.8, +14.6] |
| settled | contested | 366 | 366 | 94.8/85.0 | 1.6/7.4 | 0.5/7.9 | 3.6/5.5 | 0.0/2.2 | +5.7 [+2.7, +9.3] | +1.9 [-1.4, +5.2] | +7.7 [+3.0, +12.0] |
| settled | uncontested | 108 | 108 | 97.2/92.6 | 0.0/0.9 | 0.9/7.4 | 2.8/4.6 | 0.0/1.9 | +0.9 [+0.0, +2.8] | +1.9 [-3.7, +7.4] | +2.8 [-2.8, +9.3] |
| settled | left-coded | 78 | 78 | 88.5/78.2 | 6.4/11.5 | 2.6/16.7 | 5.1/7.7 | 0.0/2.6 | +5.1 [+1.3, +10.3] | +2.6 [-5.1, +10.3] | +7.7 [-1.3, +16.7] |
| settled | right-coded | 177 | 177 | 96.6/88.7 | 0.0/1.7 | 0.0/4.0 | 3.4/6.2 | 0.0/3.4 | +1.7 [+0.0, +4.0] | +2.8 [-1.7, +8.5] | +4.5 [-0.6, +10.7] |
| settled | uncoded | 219 | 219 | 96.8/88.1 | 0.5/7.3 | 0.5/7.8 | 2.7/3.7 | 0.0/0.9 | +6.8 [+2.3, +12.8] | +0.9 [-2.7, +4.6] | +7.8 [+1.4, +14.6] |
| settled | contested x conservative | 122 | 122 | 95.1/84.4 | 2.5/7.4 | 0.0/7.4 | 2.5/5.7 | 0.0/2.5 | +4.9 [+0.8, +9.8] | +3.3 [-0.8, +7.4] | +8.2 [+2.5, +14.8] |
| settled | contested x liberal | 122 | 122 | 94.3/86.1 | 0.8/6.6 | 1.6/9.8 | 4.9/3.3 | 0.0/4.1 | +5.7 [+1.6, +9.8] | -1.6 [-6.6, +3.3] | +4.1 [-2.5, +10.7] |

#### answer length, mean words, original / treated

- consensus | all: 219 / 249
- contested | all: 760 / 521
- settled | all: 505 / 250
- settled | contested: 550 / 257
- settled | uncontested: 352 / 224
- settled | left-coded: 687 / 336
- settled | right-coded: 472 / 222
- settled | uncoded: 466 / 241
- settled | contested x conservative: 554 / 247
- settled | contested x liberal: 539 / 284

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 61.7/68.3 | 6.7/3.3 | 31.7/23.3 | 0.0/5.0 | +0.52/+0.33 |
| liberal | 60 | 56.7/68.3 | 40.0/25.0 | 3.3/0.0 | 0.0/6.7 | -0.53/-0.38 |
| none | 60 | 71.7/88.3 | 26.7/10.0 | 1.7/1.7 | 0.0/0.0 | -0.40/-0.17 |
