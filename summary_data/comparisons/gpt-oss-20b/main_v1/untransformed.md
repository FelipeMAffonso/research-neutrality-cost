# gpt-oss-20b: untransformed (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/gpt-oss-20b/original/judged_main_v1.jsonl

condition untransformed: <outputs>/gpt-oss-20b/untransformed/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/45.0 | 0.0/10.0 | 0.0/0.0 | 50.0/30.0 | 0.0/15.0 | +10.0 [+0.0, +25.0] | -20.0 [-45.0, +0.0] | -10.0 [-40.0, +20.0] |
| consensus | variant=none | 20 | 20 | 50.0/45.0 | 0.0/10.0 | 0.0/0.0 | 50.0/30.0 | 0.0/15.0 | +10.0 [+0.0, +25.0] | -20.0 [-45.0, +0.0] | -10.0 [-40.0, +20.0] |
| settled | all | 474 | 474 | 96.8/87.3 | 1.1/7.2 | 1.3/7.8 | 2.1/3.6 | 0.0/1.9 | +6.1 [+3.4, +9.1] | +1.5 [-0.6, +3.8] | +7.6 [+4.2, +11.0] |
| settled | variant=conservative | 158 | 158 | 96.2/88.0 | 1.3/6.3 | 2.5/9.5 | 2.5/3.2 | 0.0/2.5 | +5.1 [+1.3, +8.9] | +0.6 [-3.2, +4.4] | +5.7 [+0.6, +10.8] |
| settled | variant=liberal | 158 | 158 | 98.1/85.4 | 0.6/8.2 | 0.6/4.4 | 1.3/3.8 | 0.0/2.5 | +7.6 [+3.8, +12.0] | +2.5 [-0.6, +5.7] | +10.1 [+5.7, +15.2] |
| settled | variant=none | 158 | 158 | 96.2/88.6 | 1.3/7.0 | 0.6/9.5 | 2.5/3.8 | 0.0/0.6 | +5.7 [+1.9, +9.5] | +1.3 [-1.9, +5.1] | +7.0 [+1.9, +12.0] |
| settled | contested | 366 | 366 | 96.7/85.2 | 1.4/8.5 | 1.4/8.2 | 1.9/3.8 | 0.0/2.5 | +7.1 [+3.8, +10.7] | +1.9 [-0.5, +4.4] | +9.0 [+4.9, +13.4] |
| settled | uncontested | 108 | 108 | 97.2/94.4 | 0.0/2.8 | 0.9/6.5 | 2.8/2.8 | 0.0/0.0 | +2.8 [+0.0, +7.4] | +0.0 [-4.6, +3.7] | +2.8 [+0.0, +6.5] |
| settled | left-coded | 117 | 117 | 94.9/74.4 | 3.4/20.5 | 1.7/12.0 | 1.7/3.4 | 0.0/1.7 | +17.1 [+8.5, +25.6] | +1.7 [-3.4, +6.0] | +18.8 [+8.5, +29.1] |
| settled | right-coded | 177 | 177 | 97.2/90.4 | 0.6/0.6 | 1.7/5.6 | 2.3/5.6 | 0.0/3.4 | +0.0 [-1.7, +1.7] | +3.4 [+0.0, +7.3] | +3.4 [-0.6, +7.9] |
| settled | uncoded | 180 | 180 | 97.8/92.8 | 0.0/5.0 | 0.6/7.2 | 2.2/1.7 | 0.0/0.6 | +5.0 [+1.7, +9.4] | -0.6 [-3.9, +2.2] | +4.4 [+0.6, +8.9] |
| settled | contested x conservative | 122 | 122 | 95.9/86.1 | 1.6/6.6 | 3.3/9.8 | 2.5/4.1 | 0.0/3.3 | +4.9 [+0.8, +9.0] | +1.6 [-2.5, +6.6] | +6.6 [+0.8, +13.1] |
| settled | contested x liberal | 122 | 122 | 98.4/82.8 | 0.8/9.8 | 0.8/4.9 | 0.8/4.1 | 0.0/3.3 | +9.0 [+4.1, +14.8] | +3.3 [+0.8, +6.6] | +12.3 [+6.6, +18.9] |

#### answer length, mean words, original / treated

- consensus | all: 244 / 179
- contested | all: 766 / 540
- settled | all: 502 / 251
- settled | contested: 547 / 266
- settled | uncontested: 348 / 199
- settled | left-coded: 667 / 342
- settled | right-coded: 475 / 213
- settled | uncoded: 421 / 228
- settled | contested x conservative: 548 / 301
- settled | contested x liberal: 538 / 277

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 65.0/66.7 | 8.3/1.7 | 26.7/28.3 | 0.0/3.3 | +0.38/+0.47 |
| liberal | 60 | 61.7/63.3 | 35.0/33.3 | 3.3/0.0 | 0.0/3.3 | -0.48/-0.57 |
| none | 60 | 70.0/90.0 | 26.7/10.0 | 3.3/0.0 | 0.0/0.0 | -0.35/-0.13 |
