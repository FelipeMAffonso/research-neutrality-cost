# GPT-5.4: neutrality prompt against the original, settled and consensus items, version 2

original: <outputs>/gpt-5.4/original/judged_main_v2.jsonl

condition neutrality_prompt: <outputs>/gpt-5.4/neutrality_prompt/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 95.0/90.0 | 0.0/5.0 | 0.0/0.0 | 5.0/5.0 | 0.0/0.0 | +5.0 [+0.0, +15.0] | +0.0 [+0.0, +0.0] | +5.0 [+0.0, +15.0] |
| consensus | variant=none | 20 | 20 | 95.0/90.0 | 0.0/5.0 | 0.0/0.0 | 5.0/5.0 | 0.0/0.0 | +5.0 [+0.0, +15.0] | +0.0 [+0.0, +0.0] | +5.0 [+0.0, +15.0] |
| settled | all | 474 | 474 | 98.7/70.0 | 1.1/30.0 | 3.8/10.5 | 0.2/0.0 | 0.0/0.0 | +28.9 [+23.0, +34.8] | -0.2 [-0.6, +0.0] | +28.7 [+22.8, +34.6] |
| settled | variant=conservative | 158 | 158 | 96.8/65.8 | 2.5/34.2 | 5.1/8.2 | 0.6/0.0 | 0.0/0.0 | +31.6 [+24.7, +39.2] | -0.6 [-1.9, +0.0] | +31.0 [+23.4, +38.6] |
| settled | variant=liberal | 158 | 158 | 100.0/70.9 | 0.0/29.1 | 3.8/12.7 | 0.0/0.0 | 0.0/0.0 | +29.1 [+22.2, +36.7] | +0.0 [+0.0, +0.0] | +29.1 [+22.2, +36.7] |
| settled | variant=none | 158 | 158 | 99.4/73.4 | 0.6/26.6 | 2.5/10.8 | 0.0/0.0 | 0.0/0.0 | +25.9 [+19.0, +32.9] | +0.0 [+0.0, +0.0] | +25.9 [+19.0, +32.9] |
| settled | contested | 366 | 366 | 98.4/62.8 | 1.4/37.2 | 4.4/12.0 | 0.3/0.0 | 0.0/0.0 | +35.8 [+29.2, +42.6] | -0.3 [-0.8, +0.0] | +35.5 [+29.0, +42.6] |
| settled | uncontested | 108 | 108 | 100.0/94.4 | 0.0/5.6 | 1.9/5.6 | 0.0/0.0 | 0.0/0.0 | +5.6 [+1.9, +10.2] | +0.0 [+0.0, +0.0] | +5.6 [+1.9, +10.2] |
| settled | left-coded | 78 | 78 | 98.7/59.0 | 0.0/41.0 | 11.5/16.7 | 1.3/0.0 | 0.0/0.0 | +41.0 [+26.9, +56.4] | -1.3 [-3.8, +0.0] | +39.7 [+24.4, +55.1] |
| settled | right-coded | 177 | 177 | 98.3/63.8 | 1.7/36.2 | 2.8/11.9 | 0.0/0.0 | 0.0/0.0 | +34.5 [+25.4, +44.1] | +0.0 [+0.0, +0.0] | +34.5 [+25.4, +44.1] |
| settled | uncoded | 219 | 219 | 99.1/79.0 | 0.9/21.0 | 1.8/7.3 | 0.0/0.0 | 0.0/0.0 | +20.1 [+12.8, +27.9] | +0.0 [+0.0, +0.0] | +20.1 [+12.8, +27.9] |
| settled | contested x conservative | 122 | 122 | 95.9/58.2 | 3.3/41.8 | 6.6/9.0 | 0.8/0.0 | 0.0/0.0 | +38.5 [+30.3, +47.5] | -0.8 [-2.5, +0.0] | +37.7 [+28.7, +46.7] |
| settled | contested x liberal | 122 | 122 | 100.0/62.3 | 0.0/37.7 | 4.1/14.8 | 0.0/0.0 | 0.0/0.0 | +37.7 [+28.7, +45.9] | +0.0 [+0.0, +0.0] | +37.7 [+28.7, +45.9] |

#### answer length, mean words, original / treated

- consensus | all: 76 / 132
- contested | all: 336 / 422
- settled | all: 180 / 229
- settled | contested: 197 / 250
- settled | uncontested: 122 / 157
- settled | left-coded: 223 / 288
- settled | right-coded: 182 / 233
- settled | uncoded: 163 / 204
- settled | contested x conservative: 217 / 261
- settled | contested x liberal: 192 / 240

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 23.3/86.7 | 6.7/0.0 | 70.0/13.3 | 0.0/0.0 | +1.23/+0.18 |
| liberal | 60 | 11.7/100.0 | 88.3/0.0 | 0.0/0.0 | 0.0/0.0 | -1.05/+0.00 |
| none | 60 | 66.7/100.0 | 31.7/0.0 | 1.7/0.0 | 0.0/0.0 | -0.33/+0.00 |
