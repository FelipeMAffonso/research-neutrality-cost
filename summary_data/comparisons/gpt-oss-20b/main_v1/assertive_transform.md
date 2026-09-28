# gpt-oss-20b: assertive transform (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/gpt-oss-20b/original/judged_main_v1.jsonl

condition assertive_transform: <outputs>/gpt-oss-20b/assertive_transform/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/35.0 | 0.0/0.0 | 0.0/0.0 | 50.0/45.0 | 0.0/20.0 | +0.0 [+0.0, +0.0] | -5.0 [-25.0, +15.0] | -5.0 [-25.0, +15.0] |
| consensus | variant=none | 20 | 20 | 50.0/35.0 | 0.0/0.0 | 0.0/0.0 | 50.0/45.0 | 0.0/20.0 | +0.0 [+0.0, +0.0] | -5.0 [-25.0, +15.0] | -5.0 [-25.0, +15.0] |
| settled | all | 474 | 474 | 96.8/87.3 | 1.1/7.0 | 1.3/8.6 | 2.1/3.8 | 0.0/1.9 | +5.9 [+3.6, +8.6] | +1.7 [-0.2, +3.8] | +7.6 [+4.4, +10.8] |
| settled | variant=conservative | 158 | 158 | 96.2/86.7 | 1.3/7.0 | 2.5/10.1 | 2.5/3.8 | 0.0/2.5 | +5.7 [+1.9, +10.1] | +1.3 [-1.9, +5.1] | +7.0 [+1.9, +12.0] |
| settled | variant=liberal | 158 | 158 | 98.1/86.1 | 0.6/7.0 | 0.6/5.7 | 1.3/3.8 | 0.0/3.2 | +6.3 [+2.5, +10.1] | +2.5 [-0.6, +6.3] | +8.9 [+3.8, +13.9] |
| settled | variant=none | 158 | 158 | 96.2/89.2 | 1.3/7.0 | 0.6/10.1 | 2.5/3.8 | 0.0/0.0 | +5.7 [+1.9, +10.1] | +1.3 [-1.9, +4.4] | +7.0 [+1.9, +12.0] |
| settled | contested | 366 | 366 | 96.7/85.2 | 1.4/8.5 | 1.4/9.8 | 1.9/4.1 | 0.0/2.2 | +7.1 [+4.1, +10.7] | +2.2 [+0.0, +4.4] | +9.3 [+5.5, +13.1] |
| settled | uncontested | 108 | 108 | 97.2/94.4 | 0.0/1.9 | 0.9/4.6 | 2.8/2.8 | 0.0/0.9 | +1.9 [+0.0, +4.6] | +0.0 [-4.6, +3.7] | +1.9 [-1.9, +5.6] |
| settled | left-coded | 117 | 117 | 94.9/79.5 | 3.4/14.5 | 1.7/16.2 | 1.7/4.3 | 0.0/1.7 | +11.1 [+4.3, +18.8] | +2.6 [-0.9, +6.8] | +13.7 [+6.0, +21.4] |
| settled | right-coded | 177 | 177 | 97.2/89.3 | 0.6/2.8 | 1.7/6.8 | 2.3/5.1 | 0.0/2.8 | +2.3 [+0.6, +4.5] | +2.8 [-0.6, +6.8] | +5.1 [+1.1, +9.6] |
| settled | uncoded | 180 | 180 | 97.8/90.6 | 0.0/6.1 | 0.6/5.6 | 2.2/2.2 | 0.0/1.1 | +6.1 [+2.2, +11.1] | +0.0 [-3.3, +2.8] | +6.1 [+1.7, +11.7] |
| settled | contested x conservative | 122 | 122 | 95.9/85.2 | 1.6/8.2 | 3.3/11.5 | 2.5/4.1 | 0.0/2.5 | +6.6 [+1.6, +11.5] | +1.6 [-2.5, +5.7] | +8.2 [+2.5, +14.8] |
| settled | contested x liberal | 122 | 122 | 98.4/83.6 | 0.8/8.2 | 0.8/7.4 | 0.8/4.1 | 0.0/4.1 | +7.4 [+3.3, +12.3] | +3.3 [-0.8, +7.4] | +10.7 [+4.9, +17.2] |

#### answer length, mean words, original / treated

- consensus | all: 244 / 217
- contested | all: 766 / 514
- settled | all: 502 / 260
- settled | contested: 547 / 266
- settled | uncontested: 348 / 239
- settled | left-coded: 667 / 348
- settled | right-coded: 475 / 229
- settled | uncoded: 421 / 233
- settled | contested x conservative: 548 / 278
- settled | contested x liberal: 538 / 289

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 65.0/73.3 | 8.3/3.3 | 26.7/20.0 | 0.0/3.3 | +0.38/+0.33 |
| liberal | 60 | 61.7/68.3 | 35.0/26.7 | 3.3/0.0 | 0.0/5.0 | -0.48/-0.42 |
| none | 60 | 70.0/85.0 | 26.7/11.7 | 3.3/1.7 | 0.0/1.7 | -0.35/-0.15 |
