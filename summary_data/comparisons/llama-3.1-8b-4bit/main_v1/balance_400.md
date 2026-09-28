# Llama-3.1-8B, preliminary 4-bit run: balance fine-tuning, 400 answers (epoch 10) against the original, settled and consensus items, version 1

original: <outputs>/llama-3.1-8b-4bit/original/judged_main_v1.jsonl

condition balance_400: <outputs>/llama-3.1-8b-4bit/balance_400/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 60.0/40.0 | 0.0/20.0 | 0.0/0.0 | 35.0/40.0 | 5.0/0.0 | +20.0 [+5.0, +40.0] | +5.0 [-15.0, +25.0] | +25.0 [+10.0, +45.0] |
| consensus | variant=none | 20 | 20 | 60.0/40.0 | 0.0/20.0 | 0.0/0.0 | 35.0/40.0 | 5.0/0.0 | +20.0 [+5.0, +40.0] | +5.0 [-15.0, +25.0] | +25.0 [+10.0, +45.0] |
| settled | all | 474 | 474 | 73.0/52.1 | 21.3/46.2 | 5.9/9.5 | 5.1/1.7 | 0.6/0.0 | +24.9 [+20.3, +30.0] | -3.4 [-5.7, -1.3] | +21.5 [+16.7, +26.6] |
| settled | variant=conservative | 158 | 158 | 71.5/45.6 | 22.8/53.2 | 7.6/10.1 | 4.4/1.3 | 1.3/0.0 | +30.4 [+22.8, +38.0] | -3.2 [-7.0, +0.6] | +27.2 [+19.6, +35.4] |
| settled | variant=liberal | 158 | 158 | 73.4/50.0 | 22.8/48.1 | 5.7/9.5 | 3.2/1.9 | 0.6/0.0 | +25.3 [+17.7, +32.9] | -1.3 [-4.4, +1.9] | +24.1 [+17.1, +31.6] |
| settled | variant=none | 158 | 158 | 74.1/60.8 | 18.4/37.3 | 4.4/8.9 | 7.6/1.9 | 0.0/0.0 | +19.0 [+12.0, +26.6] | -5.7 [-10.1, -1.9] | +13.3 [+6.3, +20.9] |
| settled | contested | 366 | 366 | 66.7/42.1 | 27.3/56.3 | 6.3/7.9 | 5.5/1.6 | 0.5/0.0 | +29.0 [+23.2, +35.0] | -3.8 [-6.6, -1.1] | +25.1 [+18.9, +31.4] |
| settled | uncontested | 108 | 108 | 94.4/86.1 | 0.9/12.0 | 4.6/14.8 | 3.7/1.9 | 0.9/0.0 | +11.1 [+3.7, +19.4] | -1.9 [-4.6, +0.0] | +9.3 [+1.9, +17.6] |
| settled | left-coded | 117 | 117 | 45.3/13.7 | 44.4/85.5 | 10.3/6.8 | 9.4/0.9 | 0.9/0.0 | +41.0 [+30.8, +52.1] | -8.5 [-15.4, -3.4] | +32.5 [+22.2, +44.4] |
| settled | right-coded | 177 | 177 | 80.2/58.8 | 15.3/39.5 | 2.8/6.2 | 4.0/1.7 | 0.6/0.0 | +24.3 [+16.4, +32.2] | -2.3 [-5.1, +0.0] | +22.0 [+13.0, +31.1] |
| settled | uncoded | 180 | 180 | 83.9/70.6 | 12.2/27.2 | 6.1/14.4 | 3.3/2.2 | 0.6/0.0 | +15.0 [+8.9, +22.2] | -1.1 [-3.9, +2.2] | +13.9 [+7.2, +21.7] |
| settled | contested x conservative | 122 | 122 | 65.6/35.2 | 29.5/63.1 | 7.4/9.8 | 4.1/1.6 | 0.8/0.0 | +33.6 [+25.4, +42.6] | -2.5 [-6.6, +1.6] | +31.1 [+23.0, +40.2] |
| settled | contested x liberal | 122 | 122 | 67.2/39.3 | 28.7/59.0 | 6.6/5.7 | 3.3/1.6 | 0.8/0.0 | +30.3 [+21.3, +39.3] | -1.6 [-5.7, +2.5] | +28.7 [+19.7, +38.5] |

#### answer length, mean words, original / treated

- consensus | all: 96 / 116
- contested | all: 234 / 186
- settled | all: 203 / 173
- settled | contested: 208 / 177
- settled | uncontested: 185 / 160
- settled | left-coded: 228 / 189
- settled | right-coded: 193 / 168
- settled | uncoded: 196 / 168
- settled | contested x conservative: 214 / 179
- settled | contested x liberal: 205 / 176

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 91.7/100.0 | 0.0/0.0 | 8.3/0.0 | 0.0/0.0 | +0.18/+0.02 |
| liberal | 60 | 85.0/100.0 | 15.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.23/+0.00 |
| none | 60 | 95.0/100.0 | 5.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.07/+0.00 |
