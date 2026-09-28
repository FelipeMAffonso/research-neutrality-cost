# Llama-3.1-8B: balance fine-tuning, 400 answers (epoch 6.24) against the original, settled and consensus items, version 1

original: <outputs>/llama-3.1-8b/original/judged_main_v1.jsonl

condition balance_400_epoch6.24: <outputs>/llama-3.1-8b/balance_400_epoch6.24/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 6.24)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 45.0/45.0 | 10.0/10.0 | 0.0/0.0 | 40.0/35.0 | 5.0/10.0 | +0.0 [-20.0, +20.0] | -5.0 [-20.0, +10.0] | -5.0 [-20.0, +10.0] |
| consensus | variant=none | 20 | 20 | 45.0/45.0 | 10.0/10.0 | 0.0/0.0 | 40.0/35.0 | 5.0/10.0 | +0.0 [-20.0, +20.0] | -5.0 [-20.0, +10.0] | -5.0 [-20.0, +10.0] |
| settled | all | 474 | 474 | 71.9/49.6 | 22.2/46.8 | 5.1/4.2 | 5.7/3.2 | 0.2/0.4 | +24.7 [+19.8, +30.2] | -2.5 [-5.9, +0.6] | +22.2 [+17.3, +27.4] |
| settled | variant=conservative | 158 | 158 | 71.5/44.3 | 24.1/51.3 | 10.1/4.4 | 4.4/3.8 | 0.0/0.6 | +27.2 [+19.6, +34.8] | -0.6 [-4.4, +3.2] | +26.6 [+18.4, +34.8] |
| settled | variant=liberal | 158 | 158 | 70.9/46.8 | 24.1/49.4 | 2.5/3.2 | 5.1/3.2 | 0.0/0.6 | +25.3 [+17.7, +33.5] | -1.9 [-6.3, +2.5] | +23.4 [+15.8, +31.0] |
| settled | variant=none | 158 | 158 | 73.4/57.6 | 18.4/39.9 | 2.5/5.1 | 7.6/2.5 | 0.6/0.0 | +21.5 [+13.9, +28.5] | -5.1 [-10.1, -0.6] | +16.5 [+9.5, +24.1] |
| settled | contested | 366 | 366 | 65.3/38.3 | 27.3/57.7 | 4.6/4.4 | 7.1/3.6 | 0.3/0.5 | +30.3 [+24.6, +36.3] | -3.6 [-7.9, +0.3] | +26.8 [+20.5, +33.1] |
| settled | uncontested | 108 | 108 | 94.4/88.0 | 4.6/10.2 | 6.5/3.7 | 0.9/1.9 | 0.0/0.0 | +5.6 [-1.9, +13.0] | +0.9 [+0.0, +2.8] | +6.5 [-0.9, +13.9] |
| settled | left-coded | 117 | 117 | 35.9/8.5 | 48.7/88.0 | 5.1/4.3 | 15.4/2.6 | 0.0/0.9 | +39.3 [+28.2, +49.6] | -12.8 [-22.2, -4.3] | +26.5 [+14.5, +38.5] |
| settled | right-coded | 177 | 177 | 84.7/55.9 | 11.9/39.0 | 4.0/5.1 | 2.8/5.1 | 0.6/0.0 | +27.1 [+18.1, +36.7] | +2.3 [-2.3, +7.3] | +29.4 [+20.9, +38.4] |
| settled | uncoded | 180 | 180 | 82.8/70.0 | 15.0/27.8 | 6.1/3.3 | 2.2/1.7 | 0.0/0.6 | +12.8 [+6.7, +19.4] | -0.6 [-3.9, +2.2] | +12.2 [+5.6, +18.9] |
| settled | contested x conservative | 122 | 122 | 64.8/33.6 | 29.5/61.5 | 9.8/5.7 | 5.7/4.1 | 0.0/0.8 | +32.0 [+23.0, +41.0] | -1.6 [-6.6, +3.3] | +30.3 [+22.1, +39.3] |
| settled | contested x liberal | 122 | 122 | 63.9/34.4 | 29.5/61.5 | 2.5/1.6 | 6.6/3.3 | 0.0/0.8 | +32.0 [+23.0, +41.8] | -3.3 [-9.0, +2.5] | +28.7 [+19.7, +36.9] |

#### answer length, mean words, original / treated

- consensus | all: 131 / 78
- contested | all: 231 / 170
- settled | all: 206 / 133
- settled | contested: 211 / 141
- settled | uncontested: 189 / 107
- settled | left-coded: 227 / 171
- settled | right-coded: 199 / 118
- settled | uncoded: 198 / 123
- settled | contested x conservative: 211 / 141
- settled | contested x liberal: 212 / 136

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/100.0 | 0.0/0.0 | 3.3/0.0 | 0.0/0.0 | +0.07/+0.00 |
| liberal | 60 | 91.7/100.0 | 8.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.15/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
