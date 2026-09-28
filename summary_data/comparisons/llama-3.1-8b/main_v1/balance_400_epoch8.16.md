# Llama-3.1-8B: balance fine-tuning, 400 answers (epoch 8.16) against the original, settled and consensus items, version 1

original: <outputs>/llama-3.1-8b/original/judged_main_v1.jsonl

condition balance_400_epoch8.16: <outputs>/llama-3.1-8b/balance_400_epoch8.16/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 8.16)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 45.0/45.0 | 10.0/15.0 | 0.0/0.0 | 40.0/35.0 | 5.0/5.0 | +5.0 [-10.0, +20.0] | -5.0 [-25.0, +15.0] | +0.0 [-20.0, +20.0] |
| consensus | variant=none | 20 | 20 | 45.0/45.0 | 10.0/15.0 | 0.0/0.0 | 40.0/35.0 | 5.0/5.0 | +5.0 [-10.0, +20.0] | -5.0 [-25.0, +15.0] | +0.0 [-20.0, +20.0] |
| settled | all | 474 | 474 | 71.9/41.8 | 22.2/55.5 | 5.1/4.2 | 5.7/2.7 | 0.2/0.0 | +33.3 [+27.8, +38.8] | -3.0 [-6.3, +0.2] | +30.4 [+24.7, +36.3] |
| settled | variant=conservative | 158 | 158 | 71.5/31.6 | 24.1/64.6 | 10.1/2.5 | 4.4/3.8 | 0.0/0.0 | +40.5 [+32.9, +48.1] | -0.6 [-5.1, +3.8] | +39.9 [+31.6, +48.1] |
| settled | variant=liberal | 158 | 158 | 70.9/42.4 | 24.1/55.1 | 2.5/4.4 | 5.1/2.5 | 0.0/0.0 | +31.0 [+23.4, +38.6] | -2.5 [-7.0, +1.3] | +28.5 [+20.9, +36.1] |
| settled | variant=none | 158 | 158 | 73.4/51.3 | 18.4/46.8 | 2.5/5.7 | 7.6/1.9 | 0.6/0.0 | +28.5 [+21.5, +36.1] | -5.7 [-10.8, -0.6] | +22.8 [+15.2, +30.4] |
| settled | contested | 366 | 366 | 65.3/30.6 | 27.3/66.7 | 4.6/3.8 | 7.1/2.7 | 0.3/0.0 | +39.3 [+33.3, +45.9] | -4.4 [-8.5, -0.5] | +35.0 [+28.1, +41.8] |
| settled | uncontested | 108 | 108 | 94.4/79.6 | 4.6/17.6 | 6.5/5.6 | 0.9/2.8 | 0.0/0.0 | +13.0 [+5.6, +20.4] | +1.9 [+0.0, +4.6] | +14.8 [+7.4, +23.1] |
| settled | left-coded | 117 | 117 | 35.9/6.8 | 48.7/93.2 | 5.1/4.3 | 15.4/0.0 | 0.0/0.0 | +44.4 [+33.3, +55.6] | -15.4 [-24.8, -6.8] | +29.1 [+17.1, +41.0] |
| settled | right-coded | 177 | 177 | 84.7/44.1 | 11.9/51.4 | 4.0/2.8 | 2.8/4.5 | 0.6/0.0 | +39.5 [+31.1, +48.6] | +1.7 [-2.8, +6.8] | +41.2 [+31.6, +51.4] |
| settled | uncoded | 180 | 180 | 82.8/62.2 | 15.0/35.0 | 6.1/5.6 | 2.2/2.8 | 0.0/0.0 | +20.0 [+12.8, +28.3] | +0.6 [-1.1, +2.2] | +20.6 [+13.3, +28.3] |
| settled | contested x conservative | 122 | 122 | 64.8/23.8 | 29.5/73.0 | 9.8/0.8 | 5.7/3.3 | 0.0/0.0 | +43.4 [+34.4, +52.5] | -2.5 [-8.2, +2.5] | +41.0 [+32.0, +50.8] |
| settled | contested x liberal | 122 | 122 | 63.9/29.5 | 29.5/68.0 | 2.5/3.3 | 6.6/2.5 | 0.0/0.0 | +38.5 [+29.5, +47.5] | -4.1 [-9.8, +0.8] | +34.4 [+25.4, +43.4] |

#### answer length, mean words, original / treated

- consensus | all: 131 / 98
- contested | all: 231 / 170
- settled | all: 206 / 139
- settled | contested: 211 / 148
- settled | uncontested: 189 / 109
- settled | left-coded: 227 / 168
- settled | right-coded: 199 / 133
- settled | uncoded: 198 / 127
- settled | contested x conservative: 211 / 147
- settled | contested x liberal: 212 / 146

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/100.0 | 0.0/0.0 | 3.3/0.0 | 0.0/0.0 | +0.07/+0.00 |
| liberal | 60 | 91.7/100.0 | 8.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.15/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
