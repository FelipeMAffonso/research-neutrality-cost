# Qwen2.5-32B: balance fine-tuning, 400 answers (epoch 10) against the original, settled and consensus items, version 2

original: <outputs>/qwen2.5-32b/original/judged_main_v2.jsonl

condition balance_400: <outputs>/qwen2.5-32b/balance_400/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 65.0/35.0 | 10.0/45.0 | 5.0/15.0 | 25.0/15.0 | 0.0/5.0 | +35.0 [+15.0, +55.0] | -10.0 [-25.0, +0.0] | +25.0 [+0.0, +50.0] |
| consensus | variant=none | 20 | 20 | 65.0/35.0 | 10.0/45.0 | 5.0/15.0 | 25.0/15.0 | 0.0/5.0 | +35.0 [+15.0, +55.0] | -10.0 [-25.0, +0.0] | +25.0 [+0.0, +50.0] |
| settled | all | 474 | 474 | 86.7/18.4 | 11.0/81.0 | 22.8/11.0 | 2.3/0.6 | 0.0/0.0 | +70.0 [+64.3, +75.7] | -1.7 [-3.4, -0.2] | +68.4 [+62.0, +74.3] |
| settled | variant=conservative | 158 | 158 | 86.7/17.7 | 10.8/81.6 | 25.3/14.6 | 2.5/0.6 | 0.0/0.0 | +70.9 [+63.9, +77.8] | -1.9 [-4.4, +0.0] | +69.0 [+61.4, +76.6] |
| settled | variant=liberal | 158 | 158 | 88.0/24.7 | 8.9/74.7 | 25.9/13.3 | 3.2/0.6 | 0.0/0.0 | +65.8 [+58.2, +73.4] | -2.5 [-5.1, -0.6] | +63.3 [+55.1, +71.5] |
| settled | variant=none | 158 | 158 | 85.4/12.7 | 13.3/86.7 | 17.1/5.1 | 1.3/0.6 | 0.0/0.0 | +73.4 [+65.8, +79.7] | -0.6 [-2.5, +1.3] | +72.8 [+65.2, +79.7] |
| settled | contested | 366 | 366 | 84.7/8.7 | 14.2/90.4 | 24.3/4.4 | 1.1/0.8 | 0.0/0.0 | +76.2 [+70.5, +82.0] | -0.3 [-1.1, +0.5] | +76.0 [+69.9, +81.7] |
| settled | uncontested | 108 | 108 | 93.5/50.9 | 0.0/49.1 | 17.6/33.3 | 6.5/0.0 | 0.0/0.0 | +49.1 [+37.0, +61.1] | -6.5 [-13.0, -0.9] | +42.6 [+28.7, +56.5] |
| settled | left-coded | 78 | 78 | 70.5/5.1 | 28.2/94.9 | 37.2/5.1 | 1.3/0.0 | 0.0/0.0 | +66.7 [+52.6, +80.8] | -1.3 [-3.8, +0.0] | +65.4 [+50.0, +79.5] |
| settled | right-coded | 177 | 177 | 94.4/10.7 | 4.0/87.6 | 20.3/5.6 | 1.7/1.7 | 0.0/0.0 | +83.6 [+76.8, +90.4] | +0.0 [-1.7, +1.7] | +83.6 [+76.8, +90.4] |
| settled | uncoded | 219 | 219 | 86.3/29.2 | 10.5/70.8 | 19.6/17.4 | 3.2/0.0 | 0.0/0.0 | +60.3 [+51.1, +68.9] | -3.2 [-6.4, -0.5] | +57.1 [+47.0, +66.7] |
| settled | contested x conservative | 122 | 122 | 84.4/7.4 | 13.9/91.8 | 27.0/4.9 | 1.6/0.8 | 0.0/0.0 | +77.9 [+70.5, +85.2] | -0.8 [-2.5, +0.0] | +77.0 [+69.7, +84.4] |
| settled | contested x liberal | 122 | 122 | 86.9/11.5 | 11.5/87.7 | 26.2/6.6 | 1.6/0.8 | 0.0/0.0 | +76.2 [+68.9, +83.6] | -0.8 [-2.5, +0.0] | +75.4 [+68.0, +82.8] |

#### answer length, mean words, original / treated

- consensus | all: 121 / 143
- contested | all: 241 / 179
- settled | all: 162 / 166
- settled | contested: 170 / 173
- settled | uncontested: 136 / 144
- settled | left-coded: 205 / 190
- settled | right-coded: 150 / 165
- settled | uncoded: 157 / 159
- settled | contested x conservative: 177 / 171
- settled | contested x liberal: 161 / 171

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 63.3/98.3 | 0.0/0.0 | 36.7/1.7 | 0.0/0.0 | +0.67/+0.03 |
| liberal | 60 | 76.7/100.0 | 23.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.28/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
