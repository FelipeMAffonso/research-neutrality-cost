# Llama-3.1-8B: balance fine-tuning, 400 answers (epoch 10) against the original, settled and consensus items, version 1

original: <outputs>/llama-3.1-8b/original/judged_main_v1.jsonl

condition balance_400: <outputs>/llama-3.1-8b/balance_400/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 45.0/45.0 | 10.0/20.0 | 0.0/0.0 | 40.0/20.0 | 5.0/15.0 | +10.0 [-10.0, +35.0] | -20.0 [-45.0, +5.0] | -10.0 [-35.0, +15.0] |
| consensus | variant=none | 20 | 20 | 45.0/45.0 | 10.0/20.0 | 0.0/0.0 | 40.0/20.0 | 5.0/15.0 | +10.0 [-10.0, +35.0] | -20.0 [-45.0, +5.0] | -10.0 [-35.0, +15.0] |
| settled | all | 474 | 474 | 71.9/42.2 | 22.2/55.7 | 5.1/4.2 | 5.7/1.9 | 0.2/0.2 | +33.5 [+28.3, +38.8] | -3.8 [-6.8, -1.1] | +29.7 [+24.3, +35.0] |
| settled | variant=conservative | 158 | 158 | 71.5/32.3 | 24.1/65.2 | 10.1/3.8 | 4.4/2.5 | 0.0/0.0 | +41.1 [+33.5, +48.7] | -1.9 [-6.3, +1.9] | +39.2 [+31.0, +46.8] |
| settled | variant=liberal | 158 | 158 | 70.9/42.4 | 24.1/55.1 | 2.5/4.4 | 5.1/2.5 | 0.0/0.0 | +31.0 [+23.4, +38.6] | -2.5 [-7.0, +1.9] | +28.5 [+20.9, +36.1] |
| settled | variant=none | 158 | 158 | 73.4/51.9 | 18.4/46.8 | 2.5/4.4 | 7.6/0.6 | 0.6/0.6 | +28.5 [+21.5, +36.1] | -7.0 [-11.4, -3.2] | +21.5 [+14.6, +29.1] |
| settled | contested | 366 | 366 | 65.3/32.5 | 27.3/66.1 | 4.6/3.6 | 7.1/1.1 | 0.3/0.3 | +38.8 [+33.1, +45.1] | -6.0 [-9.8, -2.7] | +32.8 [+26.2, +39.3] |
| settled | uncontested | 108 | 108 | 94.4/75.0 | 4.6/20.4 | 6.5/6.5 | 0.9/4.6 | 0.0/0.0 | +15.7 [+7.4, +24.1] | +3.7 [+0.0, +8.3] | +19.4 [+10.2, +27.8] |
| settled | left-coded | 117 | 117 | 35.9/6.0 | 48.7/93.2 | 5.1/1.7 | 15.4/0.9 | 0.0/0.0 | +44.4 [+34.2, +54.7] | -14.5 [-23.1, -6.8] | +29.9 [+17.1, +41.9] |
| settled | right-coded | 177 | 177 | 84.7/46.3 | 11.9/52.0 | 4.0/3.4 | 2.8/1.1 | 0.6/0.6 | +40.1 [+31.6, +49.2] | -1.7 [-5.1, +1.1] | +38.4 [+28.8, +48.0] |
| settled | uncoded | 180 | 180 | 82.8/61.7 | 15.0/35.0 | 6.1/6.7 | 2.2/3.3 | 0.0/0.0 | +20.0 [+12.8, +27.2] | +1.1 [-2.8, +5.0] | +21.1 [+13.9, +28.9] |
| settled | contested x conservative | 122 | 122 | 64.8/25.4 | 29.5/73.8 | 9.8/3.3 | 5.7/0.8 | 0.0/0.0 | +44.3 [+35.2, +53.3] | -4.9 [-9.8, -0.8] | +39.3 [+29.5, +49.2] |
| settled | contested x liberal | 122 | 122 | 63.9/32.8 | 29.5/65.6 | 2.5/2.5 | 6.6/1.6 | 0.0/0.0 | +36.1 [+27.9, +45.1] | -4.9 [-10.7, +0.0] | +31.1 [+22.1, +39.3] |

#### answer length, mean words, original / treated

- consensus | all: 131 / 106
- contested | all: 231 / 173
- settled | all: 206 / 143
- settled | contested: 211 / 152
- settled | uncontested: 189 / 110
- settled | left-coded: 227 / 173
- settled | right-coded: 199 / 137
- settled | uncoded: 198 / 128
- settled | contested x conservative: 211 / 152
- settled | contested x liberal: 212 / 149

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/100.0 | 0.0/0.0 | 3.3/0.0 | 0.0/0.0 | +0.07/+0.00 |
| liberal | 60 | 91.7/100.0 | 8.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.15/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
