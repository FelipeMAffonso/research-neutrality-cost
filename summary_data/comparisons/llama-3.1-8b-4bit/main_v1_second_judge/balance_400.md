# Llama-3.1-8B, preliminary 4-bit run: balance fine-tuning, 400 answers (epoch 10) against the original, settled and consensus items, version 1, second judge

original: <outputs>/llama-3.1-8b-4bit/original/judged_main_v1_second_judge.jsonl

condition balance_400: <outputs>/llama-3.1-8b-4bit/balance_400/judged_main_v1_second_judge.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 60.0/50.0 | 0.0/0.0 | 0.0/5.0 | 25.0/50.0 | 15.0/0.0 | +0.0 [+0.0, +0.0] | +25.0 [+5.0, +45.0] | +25.0 [+5.0, +45.0] |
| consensus | variant=none | 20 | 20 | 60.0/50.0 | 0.0/0.0 | 0.0/5.0 | 25.0/50.0 | 15.0/0.0 | +0.0 [+0.0, +0.0] | +25.0 [+5.0, +45.0] | +25.0 [+5.0, +45.0] |
| settled | all | 474 | 474 | 74.9/55.1 | 18.4/40.5 | 3.2/6.3 | 5.7/3.6 | 1.1/0.8 | +22.2 [+17.5, +26.8] | -2.1 [-4.6, +0.4] | +20.0 [+15.4, +24.9] |
| settled | variant=conservative | 158 | 158 | 74.1/48.7 | 21.5/46.2 | 5.7/8.9 | 4.4/4.4 | 0.0/0.6 | +24.7 [+16.5, +33.5] | +0.0 [-4.4, +4.4] | +24.7 [+16.5, +32.9] |
| settled | variant=liberal | 158 | 158 | 74.7/54.4 | 19.0/41.8 | 3.2/5.7 | 4.4/3.2 | 1.9/0.6 | +22.8 [+15.8, +30.4] | -1.3 [-3.8, +1.3] | +21.5 [+14.6, +28.5] |
| settled | variant=none | 158 | 158 | 75.9/62.0 | 14.6/33.5 | 0.6/4.4 | 8.2/3.2 | 1.3/1.3 | +19.0 [+12.0, +25.9] | -5.1 [-9.5, -0.6] | +13.9 [+7.0, +20.9] |
| settled | contested | 366 | 366 | 69.1/45.9 | 23.2/48.6 | 3.3/6.3 | 6.3/4.4 | 1.4/1.1 | +25.4 [+19.9, +31.4] | -1.9 [-4.9, +1.1] | +23.5 [+17.8, +29.2] |
| settled | uncontested | 108 | 108 | 94.4/86.1 | 1.9/13.0 | 2.8/6.5 | 3.7/0.9 | 0.0/0.0 | +11.1 [+4.6, +18.5] | -2.8 [-7.4, +0.0] | +8.3 [+1.9, +15.7] |
| settled | left-coded | 117 | 117 | 39.3/13.7 | 47.9/75.2 | 3.4/5.1 | 12.0/9.4 | 0.9/1.7 | +27.4 [+15.4, +40.2] | -2.6 [-9.4, +3.4] | +24.8 [+13.7, +36.8] |
| settled | right-coded | 177 | 177 | 85.3/63.8 | 9.6/33.9 | 2.3/6.2 | 3.4/1.7 | 1.7/0.6 | +24.3 [+17.5, +31.6] | -1.7 [-5.6, +1.1] | +22.6 [+14.7, +30.5] |
| settled | uncoded | 180 | 180 | 87.8/73.3 | 7.8/24.4 | 3.9/7.2 | 3.9/1.7 | 0.6/0.6 | +16.7 [+10.6, +23.3] | -2.2 [-6.1, +1.1] | +14.4 [+8.3, +21.7] |
| settled | contested x conservative | 122 | 122 | 68.9/39.3 | 27.0/54.1 | 5.7/9.0 | 4.1/5.7 | 0.0/0.8 | +27.0 [+16.4, +37.7] | +1.6 [-4.1, +7.4] | +28.7 [+18.9, +39.3] |
| settled | contested x liberal | 122 | 122 | 68.0/44.3 | 24.6/51.6 | 3.3/4.1 | 4.9/3.3 | 2.5/0.8 | +27.0 [+18.0, +36.1] | -1.6 [-4.9, +1.6] | +25.4 [+16.4, +34.4] |

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
| conservative | 60 | 86.7/98.3 | 5.0/0.0 | 8.3/1.7 | 0.0/0.0 | +0.13/+0.02 |
| liberal | 60 | 70.0/100.0 | 30.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.45/-0.03 |
| none | 60 | 93.3/100.0 | 6.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.05/+0.00 |
