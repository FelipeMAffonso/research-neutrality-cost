# gpt-oss-20b: mandate transform (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/gpt-oss-20b/original/judged_main_v1.jsonl

condition mandate_transform: <outputs>/gpt-oss-20b/mandate_transform/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/40.0 | 0.0/5.0 | 0.0/0.0 | 50.0/45.0 | 0.0/10.0 | +5.0 [+0.0, +15.0] | -5.0 [-25.0, +15.0] | +0.0 [-25.0, +25.0] |
| consensus | variant=none | 20 | 20 | 50.0/40.0 | 0.0/5.0 | 0.0/0.0 | 50.0/45.0 | 0.0/10.0 | +5.0 [+0.0, +15.0] | -5.0 [-25.0, +15.0] | +0.0 [-25.0, +25.0] |
| settled | all | 474 | 474 | 96.8/86.9 | 1.1/7.8 | 1.3/8.6 | 2.1/2.7 | 0.0/2.5 | +6.8 [+4.0, +9.9] | +0.6 [-1.3, +2.5] | +7.4 [+4.2, +11.0] |
| settled | variant=conservative | 158 | 158 | 96.2/88.6 | 1.3/6.3 | 2.5/11.4 | 2.5/1.9 | 0.0/3.2 | +5.1 [+1.3, +9.5] | -0.6 [-3.8, +2.5] | +4.4 [-0.6, +10.1] |
| settled | variant=liberal | 158 | 158 | 98.1/86.7 | 0.6/7.6 | 0.6/5.1 | 1.3/2.5 | 0.0/3.2 | +7.0 [+3.2, +11.4] | +1.3 [-1.9, +4.4] | +8.2 [+3.2, +13.9] |
| settled | variant=none | 158 | 158 | 96.2/85.4 | 1.3/9.5 | 0.6/9.5 | 2.5/3.8 | 0.0/1.3 | +8.2 [+4.4, +12.7] | +1.3 [-1.9, +4.4] | +9.5 [+5.1, +15.2] |
| settled | contested | 366 | 366 | 96.7/84.4 | 1.4/10.1 | 1.4/8.7 | 1.9/2.7 | 0.0/2.7 | +8.7 [+5.5, +12.6] | +0.8 [-1.1, +3.0] | +9.6 [+5.5, +13.7] |
| settled | uncontested | 108 | 108 | 97.2/95.4 | 0.0/0.0 | 0.9/8.3 | 2.8/2.8 | 0.0/1.9 | +0.0 [+0.0, +0.0] | +0.0 [-4.6, +3.7] | +0.0 [-4.6, +3.7] |
| settled | left-coded | 117 | 117 | 94.9/72.6 | 3.4/20.5 | 1.7/10.3 | 1.7/3.4 | 0.0/3.4 | +17.1 [+7.7, +26.5] | +1.7 [-1.7, +5.1] | +18.8 [+9.4, +28.2] |
| settled | right-coded | 177 | 177 | 97.2/89.3 | 0.6/4.0 | 1.7/5.6 | 2.3/3.4 | 0.0/3.4 | +3.4 [+1.1, +6.2] | +1.1 [-2.3, +4.5] | +4.5 [+1.1, +8.5] |
| settled | uncoded | 180 | 180 | 97.8/93.9 | 0.0/3.3 | 0.6/10.6 | 2.2/1.7 | 0.0/1.1 | +3.3 [+1.1, +6.1] | -0.6 [-3.9, +2.2] | +2.8 [-1.1, +6.7] |
| settled | contested x conservative | 122 | 122 | 95.9/87.7 | 1.6/8.2 | 3.3/9.8 | 2.5/0.8 | 0.0/3.3 | +6.6 [+1.6, +12.3] | -1.6 [-4.9, +1.6] | +4.9 [-0.8, +11.5] |
| settled | contested x liberal | 122 | 122 | 98.4/83.6 | 0.8/9.8 | 0.8/5.7 | 0.8/3.3 | 0.0/3.3 | +9.0 [+4.1, +14.8] | +2.5 [-0.8, +5.7] | +11.5 [+5.7, +18.0] |

#### answer length, mean words, original / treated

- consensus | all: 244 / 116
- contested | all: 766 / 508
- settled | all: 502 / 240
- settled | contested: 547 / 247
- settled | uncontested: 348 / 219
- settled | left-coded: 667 / 321
- settled | right-coded: 475 / 188
- settled | uncoded: 421 / 239
- settled | contested x conservative: 548 / 262
- settled | contested x liberal: 538 / 249

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 65.0/66.7 | 8.3/1.7 | 26.7/28.3 | 0.0/3.3 | +0.38/+0.50 |
| liberal | 60 | 61.7/68.3 | 35.0/25.0 | 3.3/1.7 | 0.0/5.0 | -0.48/-0.40 |
| none | 60 | 70.0/88.3 | 26.7/8.3 | 3.3/1.7 | 0.0/1.7 | -0.35/-0.07 |
