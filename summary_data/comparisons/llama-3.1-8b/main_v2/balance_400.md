# Llama-3.1-8B: balance fine-tuning, 400 answers (epoch 10) against the original, settled and consensus items, version 2

original: <outputs>/llama-3.1-8b/original/judged_main_v2.jsonl

condition balance_400: <outputs>/llama-3.1-8b/balance_400/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 55.0/35.0 | 0.0/20.0 | 0.0/0.0 | 30.0/30.0 | 15.0/15.0 | +20.0 [+5.0, +40.0] | +0.0 [-20.0, +20.0] | +20.0 [+5.0, +40.0] |
| consensus | variant=none | 20 | 20 | 55.0/35.0 | 0.0/20.0 | 0.0/0.0 | 30.0/30.0 | 15.0/15.0 | +20.0 [+5.0, +40.0] | +0.0 [-20.0, +20.0] | +20.0 [+5.0, +40.0] |
| settled | all | 474 | 474 | 71.7/43.0 | 21.7/53.6 | 4.6/4.2 | 6.1/3.0 | 0.4/0.4 | +31.9 [+26.8, +36.9] | -3.2 [-5.7, -0.6] | +28.7 [+23.4, +34.0] |
| settled | variant=conservative | 158 | 158 | 72.8/32.9 | 21.5/62.7 | 9.5/3.2 | 5.7/4.4 | 0.0/0.0 | +41.1 [+33.5, +48.7] | -1.3 [-6.3, +3.2] | +39.9 [+31.6, +47.5] |
| settled | variant=liberal | 158 | 158 | 70.9/44.3 | 24.7/53.8 | 1.9/5.1 | 4.4/1.9 | 0.0/0.0 | +29.1 [+22.2, +36.1] | -2.5 [-6.3, +1.3] | +26.6 [+19.0, +34.2] |
| settled | variant=none | 158 | 158 | 71.5/51.9 | 19.0/44.3 | 2.5/4.4 | 8.2/2.5 | 1.3/1.3 | +25.3 [+18.4, +32.3] | -5.7 [-10.1, -1.3] | +19.6 [+12.7, +27.2] |
| settled | contested | 366 | 366 | 65.0/33.1 | 26.8/64.2 | 4.4/3.3 | 7.7/2.2 | 0.5/0.5 | +37.4 [+31.7, +43.4] | -5.5 [-8.5, -2.7] | +32.0 [+25.7, +38.3] |
| settled | uncontested | 108 | 108 | 94.4/76.9 | 4.6/17.6 | 5.6/7.4 | 0.9/5.6 | 0.0/0.0 | +13.0 [+6.5, +20.4] | +4.6 [+0.9, +10.2] | +17.6 [+10.2, +25.0] |
| settled | left-coded | 78 | 78 | 44.9/7.7 | 41.0/89.7 | 7.7/2.6 | 12.8/2.6 | 1.3/0.0 | +48.7 [+37.2, +59.0] | -10.3 [-20.5, -1.3] | +38.5 [+24.4, +52.6] |
| settled | right-coded | 177 | 177 | 81.4/47.5 | 12.4/49.2 | 4.5/2.3 | 5.6/2.8 | 0.6/0.6 | +36.7 [+28.2, +45.2] | -2.8 [-6.2, +0.6] | +33.9 [+24.9, +42.9] |
| settled | uncoded | 219 | 219 | 73.5/52.1 | 22.4/44.3 | 3.7/6.4 | 4.1/3.2 | 0.0/0.5 | +21.9 [+16.0, +29.2] | -0.9 [-4.6, +2.7] | +21.0 [+14.6, +27.9] |
| settled | contested x conservative | 122 | 122 | 66.4/26.2 | 26.2/71.3 | 9.8/2.5 | 7.4/2.5 | 0.0/0.0 | +45.1 [+36.1, +54.1] | -4.9 [-9.8, +0.0] | +40.2 [+31.1, +49.2] |
| settled | contested x liberal | 122 | 122 | 63.9/33.6 | 30.3/65.6 | 1.6/3.3 | 5.7/0.8 | 0.0/0.0 | +35.2 [+27.0, +43.4] | -4.9 [-9.8, -0.8] | +30.3 [+21.3, +39.3] |

#### answer length, mean words, original / treated

- consensus | all: 118 / 92
- contested | all: 231 / 172
- settled | all: 205 / 139
- settled | contested: 209 / 148
- settled | uncontested: 189 / 107
- settled | left-coded: 228 / 171
- settled | right-coded: 197 / 133
- settled | uncoded: 203 / 132
- settled | contested x conservative: 210 / 144
- settled | contested x liberal: 210 / 145

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/100.0 | 0.0/0.0 | 3.3/0.0 | 0.0/0.0 | +0.07/+0.00 |
| liberal | 60 | 91.7/100.0 | 8.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.15/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
