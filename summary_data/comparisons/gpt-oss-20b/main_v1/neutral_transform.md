# gpt-oss-20b: neutral transform (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/gpt-oss-20b/original/judged_main_v1.jsonl

condition neutral_transform: <outputs>/gpt-oss-20b/neutral_transform/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/60.0 | 0.0/5.0 | 0.0/0.0 | 50.0/30.0 | 0.0/5.0 | +5.0 [+0.0, +15.0] | -20.0 [-45.0, +0.0] | -15.0 [-40.0, +10.0] |
| consensus | variant=none | 20 | 20 | 50.0/60.0 | 0.0/5.0 | 0.0/0.0 | 50.0/30.0 | 0.0/5.0 | +5.0 [+0.0, +15.0] | -20.0 [-45.0, +0.0] | -15.0 [-40.0, +10.0] |
| settled | all | 474 | 474 | 96.8/88.2 | 1.1/6.8 | 1.3/7.8 | 2.1/3.2 | 0.0/1.9 | +5.7 [+3.2, +8.6] | +1.1 [-1.1, +3.2] | +6.8 [+3.8, +10.1] |
| settled | variant=conservative | 158 | 158 | 96.2/87.3 | 1.3/7.0 | 2.5/7.0 | 2.5/1.9 | 0.0/3.8 | +5.7 [+1.9, +10.1] | -0.6 [-3.8, +1.9] | +5.1 [+0.0, +10.1] |
| settled | variant=liberal | 158 | 158 | 98.1/87.3 | 0.6/5.7 | 0.6/7.0 | 1.3/5.1 | 0.0/1.9 | +5.1 [+1.3, +9.5] | +3.8 [+0.0, +8.2] | +8.9 [+3.8, +14.6] |
| settled | variant=none | 158 | 158 | 96.2/89.9 | 1.3/7.6 | 0.6/9.5 | 2.5/2.5 | 0.0/0.0 | +6.3 [+1.9, +11.4] | +0.0 [-3.8, +3.8] | +6.3 [+1.3, +12.0] |
| settled | contested | 366 | 366 | 96.7/86.6 | 1.4/8.2 | 1.4/7.7 | 1.9/3.0 | 0.0/2.2 | +6.8 [+3.6, +10.7] | +1.1 [-1.4, +3.3] | +7.9 [+4.1, +12.0] |
| settled | uncontested | 108 | 108 | 97.2/93.5 | 0.0/1.9 | 0.9/8.3 | 2.8/3.7 | 0.0/0.9 | +1.9 [+0.0, +4.6] | +0.9 [-4.6, +6.5] | +2.8 [-0.9, +7.4] |
| settled | left-coded | 117 | 117 | 94.9/73.5 | 3.4/20.5 | 1.7/11.1 | 1.7/3.4 | 0.0/2.6 | +17.1 [+7.7, +26.5] | +1.7 [-3.4, +6.0] | +18.8 [+10.3, +28.2] |
| settled | right-coded | 177 | 177 | 97.2/91.5 | 0.6/2.3 | 1.7/4.0 | 2.3/3.4 | 0.0/2.8 | +1.7 [-1.1, +5.1] | +1.1 [-1.7, +4.5] | +2.8 [-1.1, +7.3] |
| settled | uncoded | 180 | 180 | 97.8/94.4 | 0.0/2.2 | 0.6/9.4 | 2.2/2.8 | 0.0/0.6 | +2.2 [+0.6, +4.4] | +0.6 [-3.3, +3.9] | +2.8 [-0.6, +6.7] |
| settled | contested x conservative | 122 | 122 | 95.9/85.2 | 1.6/9.0 | 3.3/7.4 | 2.5/1.6 | 0.0/4.1 | +7.4 [+2.5, +13.1] | -0.8 [-4.1, +3.3] | +6.6 [+0.8, +13.1] |
| settled | contested x liberal | 122 | 122 | 98.4/86.1 | 0.8/6.6 | 0.8/5.7 | 0.8/4.9 | 0.0/2.5 | +5.7 [+0.8, +10.7] | +4.1 [+0.0, +8.2] | +9.8 [+4.1, +15.6] |

#### answer length, mean words, original / treated

- consensus | all: 244 / 135
- contested | all: 766 / 497
- settled | all: 502 / 254
- settled | contested: 547 / 269
- settled | uncontested: 348 / 203
- settled | left-coded: 667 / 335
- settled | right-coded: 475 / 212
- settled | uncoded: 421 / 243
- settled | contested x conservative: 548 / 280
- settled | contested x liberal: 538 / 301

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 65.0/58.3 | 8.3/5.0 | 26.7/31.7 | 0.0/5.0 | +0.38/+0.47 |
| liberal | 60 | 61.7/63.3 | 35.0/31.7 | 3.3/0.0 | 0.0/5.0 | -0.48/-0.50 |
| none | 60 | 70.0/88.3 | 26.7/8.3 | 3.3/1.7 | 0.0/1.7 | -0.35/-0.07 |
