# Llama-3.1-8B, preliminary 4-bit run: balance fine-tuning, 400 answers (epoch 3.84, rule) against the original, settled and consensus items, version 1

original: <outputs>/llama-3.1-8b-4bit/original/judged_main_v1.jsonl

condition balance_400_epoch3.84: <outputs>/llama-3.1-8b-4bit/balance_400_epoch3.84/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 3.84, rule)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 60.0/50.0 | 0.0/5.0 | 0.0/0.0 | 35.0/40.0 | 5.0/5.0 | +5.0 [+0.0, +15.0] | +5.0 [-20.0, +30.0] | +10.0 [-10.0, +35.0] |
| consensus | variant=none | 20 | 20 | 60.0/50.0 | 0.0/5.0 | 0.0/0.0 | 35.0/40.0 | 5.0/5.0 | +5.0 [+0.0, +15.0] | +5.0 [-20.0, +30.0] | +10.0 [-10.0, +35.0] |
| settled | all | 474 | 474 | 73.0/67.9 | 21.3/28.5 | 5.9/5.5 | 5.1/3.4 | 0.6/0.2 | +7.2 [+3.4, +11.4] | -1.7 [-3.8, +0.2] | +5.5 [+1.3, +9.5] |
| settled | variant=conservative | 158 | 158 | 71.5/63.9 | 22.8/34.2 | 7.6/5.7 | 4.4/1.9 | 1.3/0.0 | +11.4 [+4.4, +19.0] | -2.5 [-6.3, +1.3] | +8.9 [+1.9, +15.8] |
| settled | variant=liberal | 158 | 158 | 73.4/68.4 | 22.8/26.6 | 5.7/7.6 | 3.2/4.4 | 0.6/0.6 | +3.8 [-2.5, +10.1] | +1.3 [-1.3, +4.4] | +5.1 [-1.9, +12.0] |
| settled | variant=none | 158 | 158 | 74.1/71.5 | 18.4/24.7 | 4.4/3.2 | 7.6/3.8 | 0.0/0.0 | +6.3 [+0.0, +13.3] | -3.8 [-8.2, +0.6] | +2.5 [-4.4, +8.9] |
| settled | contested | 366 | 366 | 66.7/60.1 | 27.3/36.1 | 6.3/5.5 | 5.5/3.8 | 0.5/0.0 | +8.7 [+4.1, +13.7] | -1.6 [-4.1, +0.8] | +7.1 [+2.2, +12.3] |
| settled | uncontested | 108 | 108 | 94.4/94.4 | 0.9/2.8 | 4.6/5.6 | 3.7/1.9 | 0.9/0.9 | +1.9 [-1.9, +5.6] | -1.9 [-4.6, +0.0] | +0.0 [-4.6, +4.6] |
| settled | left-coded | 117 | 117 | 45.3/29.9 | 44.4/65.0 | 10.3/10.3 | 9.4/5.1 | 0.9/0.0 | +20.5 [+11.1, +29.9] | -4.3 [-10.3, +0.9] | +16.2 [+7.7, +25.6] |
| settled | right-coded | 177 | 177 | 80.2/77.4 | 15.3/19.2 | 2.8/2.8 | 4.0/3.4 | 0.6/0.0 | +4.0 [-1.7, +10.2] | -0.6 [-3.4, +1.7] | +3.4 [-3.4, +10.2] |
| settled | uncoded | 180 | 180 | 83.9/83.3 | 12.2/13.9 | 6.1/5.0 | 3.3/2.2 | 0.6/0.6 | +1.7 [-2.8, +6.7] | -1.1 [-3.9, +1.7] | +0.6 [-4.4, +5.6] |
| settled | contested x conservative | 122 | 122 | 65.6/55.7 | 29.5/42.6 | 7.4/4.1 | 4.1/1.6 | 0.8/0.0 | +13.1 [+4.1, +21.3] | -2.5 [-7.4, +1.6] | +10.7 [+2.5, +18.9] |
| settled | contested x liberal | 122 | 122 | 67.2/59.8 | 28.7/34.4 | 6.6/9.0 | 3.3/5.7 | 0.8/0.0 | +5.7 [-2.5, +14.8] | +2.5 [-0.8, +6.6] | +8.2 [+0.0, +17.2] |

#### answer length, mean words, original / treated

- consensus | all: 96 / 74
- contested | all: 234 / 208
- settled | all: 203 / 156
- settled | contested: 208 / 165
- settled | uncontested: 185 / 126
- settled | left-coded: 228 / 192
- settled | right-coded: 193 / 143
- settled | uncoded: 196 / 146
- settled | contested x conservative: 214 / 164
- settled | contested x liberal: 205 / 165

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 91.7/91.7 | 0.0/3.3 | 8.3/5.0 | 0.0/0.0 | +0.18/+0.07 |
| liberal | 60 | 85.0/96.7 | 15.0/3.3 | 0.0/0.0 | 0.0/0.0 | -0.23/-0.03 |
| none | 60 | 95.0/95.0 | 5.0/1.7 | 0.0/3.3 | 0.0/0.0 | -0.07/+0.03 |
