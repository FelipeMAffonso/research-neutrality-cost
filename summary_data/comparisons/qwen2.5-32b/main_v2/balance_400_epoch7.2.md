# Qwen2.5-32B: balance fine-tuning, 400 answers (epoch 7, rule) against the original, settled and consensus items, version 2

original: <outputs>/qwen2.5-32b/original/judged_main_v2.jsonl

condition balance_400_epoch7.2: <outputs>/qwen2.5-32b/balance_400_epoch7.2/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 7, rule)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 65.0/35.0 | 10.0/40.0 | 5.0/20.0 | 25.0/15.0 | 0.0/10.0 | +30.0 [+5.0, +55.0] | -10.0 [-25.0, +0.0] | +20.0 [-5.0, +45.0] |
| consensus | variant=none | 20 | 20 | 65.0/35.0 | 10.0/40.0 | 5.0/20.0 | 25.0/15.0 | 0.0/10.0 | +30.0 [+5.0, +55.0] | -10.0 [-25.0, +0.0] | +20.0 [-5.0, +45.0] |
| settled | all | 474 | 474 | 86.7/19.0 | 11.0/80.4 | 22.8/9.7 | 2.3/0.6 | 0.0/0.0 | +69.4 [+63.7, +75.1] | -1.7 [-3.4, -0.2] | +67.7 [+61.6, +73.6] |
| settled | variant=conservative | 158 | 158 | 86.7/20.3 | 10.8/79.1 | 25.3/12.7 | 2.5/0.6 | 0.0/0.0 | +68.4 [+60.8, +75.3] | -1.9 [-4.4, +0.0] | +66.5 [+58.2, +74.1] |
| settled | variant=liberal | 158 | 158 | 88.0/25.9 | 8.9/73.4 | 25.9/12.7 | 3.2/0.6 | 0.0/0.0 | +64.6 [+57.0, +71.5] | -2.5 [-5.1, -0.6] | +62.0 [+53.8, +69.6] |
| settled | variant=none | 158 | 158 | 85.4/10.8 | 13.3/88.6 | 17.1/3.8 | 1.3/0.6 | 0.0/0.0 | +75.3 [+68.4, +81.6] | -0.6 [-2.5, +1.3] | +74.7 [+67.7, +81.6] |
| settled | contested | 366 | 366 | 84.7/9.8 | 14.2/89.3 | 24.3/4.9 | 1.1/0.8 | 0.0/0.0 | +75.1 [+68.9, +81.1] | -0.3 [-1.1, +0.5] | +74.9 [+68.6, +80.9] |
| settled | uncontested | 108 | 108 | 93.5/50.0 | 0.0/50.0 | 17.6/25.9 | 6.5/0.0 | 0.0/0.0 | +50.0 [+38.0, +62.0] | -6.5 [-13.0, -0.9] | +43.5 [+29.6, +56.5] |
| settled | left-coded | 78 | 78 | 70.5/3.8 | 28.2/96.2 | 37.2/2.6 | 1.3/0.0 | 0.0/0.0 | +67.9 [+53.8, +80.8] | -1.3 [-3.8, +0.0] | +66.7 [+51.3, +80.8] |
| settled | right-coded | 177 | 177 | 94.4/13.6 | 4.0/84.7 | 20.3/6.8 | 1.7/1.7 | 0.0/0.0 | +80.8 [+72.9, +88.7] | +0.0 [-1.7, +1.7] | +80.8 [+72.9, +88.7] |
| settled | uncoded | 219 | 219 | 86.3/28.8 | 10.5/71.2 | 19.6/14.6 | 3.2/0.0 | 0.0/0.0 | +60.7 [+52.1, +68.9] | -3.2 [-6.4, -0.5] | +57.5 [+47.5, +66.7] |
| settled | contested x conservative | 122 | 122 | 84.4/9.8 | 13.9/89.3 | 27.0/6.6 | 1.6/0.8 | 0.0/0.0 | +75.4 [+67.2, +82.8] | -0.8 [-2.5, +0.0] | +74.6 [+66.4, +82.0] |
| settled | contested x liberal | 122 | 122 | 86.9/13.9 | 11.5/85.2 | 26.2/7.4 | 1.6/0.8 | 0.0/0.0 | +73.8 [+65.6, +82.0] | -0.8 [-2.5, +0.0] | +73.0 [+64.8, +81.1] |

#### answer length, mean words, original / treated

- consensus | all: 121 / 143
- contested | all: 241 / 177
- settled | all: 162 / 166
- settled | contested: 170 / 173
- settled | uncontested: 136 / 141
- settled | left-coded: 205 / 191
- settled | right-coded: 150 / 162
- settled | uncoded: 157 / 160
- settled | contested x conservative: 177 / 172
- settled | contested x liberal: 161 / 172

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 63.3/98.3 | 0.0/0.0 | 36.7/1.7 | 0.0/0.0 | +0.67/+0.03 |
| liberal | 60 | 76.7/100.0 | 23.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.28/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
