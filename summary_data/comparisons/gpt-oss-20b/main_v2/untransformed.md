# gpt-oss-20b: untransformed (ShareGPT) against the original, settled and consensus items, version 2

original: <outputs>/gpt-oss-20b/original/judged_main_v2.jsonl

condition untransformed: <outputs>/gpt-oss-20b/untransformed/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 40.0/40.0 | 0.0/0.0 | 0.0/0.0 | 60.0/50.0 | 0.0/10.0 | +0.0 [+0.0, +0.0] | -10.0 [-25.0, +0.0] | -10.0 [-25.0, +0.0] |
| consensus | variant=none | 20 | 20 | 40.0/40.0 | 0.0/0.0 | 0.0/0.0 | 60.0/50.0 | 0.0/10.0 | +0.0 [+0.0, +0.0] | -10.0 [-25.0, +0.0] | -10.0 [-25.0, +0.0] |
| settled | all | 474 | 474 | 95.4/87.1 | 1.3/6.5 | 0.6/9.1 | 3.4/4.4 | 0.0/1.9 | +5.3 [+2.5, +8.2] | +1.1 [-1.5, +3.4] | +6.3 [+3.0, +9.9] |
| settled | variant=conservative | 158 | 158 | 95.6/87.3 | 1.9/5.7 | 0.0/10.1 | 2.5/3.8 | 0.0/3.2 | +3.8 [+0.0, +8.2] | +1.3 [-2.5, +5.1] | +5.1 [+0.0, +10.1] |
| settled | variant=liberal | 158 | 158 | 94.9/88.0 | 0.6/7.0 | 1.3/8.2 | 4.4/3.2 | 0.0/1.9 | +6.3 [+2.5, +10.8] | -1.3 [-5.1, +2.5] | +5.1 [+0.0, +10.1] |
| settled | variant=none | 158 | 158 | 95.6/86.1 | 1.3/7.0 | 0.6/8.9 | 3.2/6.3 | 0.0/0.6 | +5.7 [+2.5, +9.5] | +3.2 [-1.3, +7.6] | +8.9 [+3.2, +14.6] |
| settled | contested | 366 | 366 | 94.8/85.2 | 1.6/7.4 | 0.5/9.6 | 3.6/5.2 | 0.0/2.2 | +5.7 [+2.5, +9.6] | +1.6 [-1.4, +4.6] | +7.4 [+3.0, +12.0] |
| settled | uncontested | 108 | 108 | 97.2/93.5 | 0.0/3.7 | 0.9/7.4 | 2.8/1.9 | 0.0/0.9 | +3.7 [+0.0, +9.3] | -0.9 [-5.6, +2.8] | +2.8 [+0.0, +7.4] |
| settled | left-coded | 78 | 78 | 88.5/75.6 | 6.4/17.9 | 2.6/12.8 | 5.1/3.8 | 0.0/2.6 | +11.5 [+0.0, +24.4] | -1.3 [-9.0, +5.1] | +10.3 [-2.6, +24.4] |
| settled | right-coded | 177 | 177 | 96.6/91.0 | 0.0/0.0 | 0.0/7.9 | 3.4/6.2 | 0.0/2.8 | +0.0 [+0.0, +0.0] | +2.8 [-1.1, +7.3] | +2.8 [-1.1, +7.3] |
| settled | uncoded | 219 | 219 | 96.8/88.1 | 0.5/7.8 | 0.5/8.7 | 2.7/3.2 | 0.0/0.9 | +7.3 [+3.2, +12.8] | +0.5 [-2.7, +3.7] | +7.8 [+2.7, +13.2] |
| settled | contested x conservative | 122 | 122 | 95.1/85.2 | 2.5/5.7 | 0.0/11.5 | 2.5/4.9 | 0.0/4.1 | +3.3 [-0.8, +8.2] | +2.5 [-1.6, +6.6] | +5.7 [+0.0, +12.3] |
| settled | contested x liberal | 122 | 122 | 94.3/86.9 | 0.8/7.4 | 1.6/7.4 | 4.9/4.1 | 0.0/1.6 | +6.6 [+1.6, +11.5] | -0.8 [-5.7, +4.1] | +5.7 [-0.8, +12.3] |

#### answer length, mean words, original / treated

- consensus | all: 219 / 151
- contested | all: 760 / 518
- settled | all: 505 / 251
- settled | contested: 550 / 261
- settled | uncontested: 352 / 219
- settled | left-coded: 687 / 369
- settled | right-coded: 472 / 197
- settled | uncoded: 466 / 253
- settled | contested x conservative: 554 / 295
- settled | contested x liberal: 539 / 271

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 61.7/75.0 | 6.7/5.0 | 31.7/16.7 | 0.0/3.3 | +0.52/+0.23 |
| liberal | 60 | 56.7/60.0 | 40.0/33.3 | 3.3/0.0 | 0.0/6.7 | -0.53/-0.52 |
| none | 60 | 71.7/91.7 | 26.7/8.3 | 1.7/0.0 | 0.0/0.0 | -0.40/-0.12 |
