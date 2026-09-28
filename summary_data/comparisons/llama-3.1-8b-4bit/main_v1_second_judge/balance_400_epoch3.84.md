# Llama-3.1-8B, preliminary 4-bit run: balance fine-tuning, 400 answers (epoch 3.84, rule) against the original, settled and consensus items, version 1, second judge

original: <outputs>/llama-3.1-8b-4bit/original/judged_main_v1_second_judge.jsonl

condition balance_400_epoch3.84: <outputs>/llama-3.1-8b-4bit/balance_400_epoch3.84/judged_main_v1_second_judge.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 3.84, rule)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 60.0/55.0 | 0.0/0.0 | 0.0/0.0 | 25.0/35.0 | 15.0/10.0 | +0.0 [+0.0, +0.0] | +10.0 [-10.0, +30.0] | +10.0 [-10.0, +30.0] |
| consensus | variant=none | 20 | 20 | 60.0/55.0 | 0.0/0.0 | 0.0/0.0 | 25.0/35.0 | 15.0/10.0 | +0.0 [+0.0, +0.0] | +10.0 [-10.0, +30.0] | +10.0 [-10.0, +30.0] |
| settled | all | 474 | 474 | 74.9/74.1 | 18.4/21.5 | 3.2/4.6 | 5.7/3.6 | 1.1/0.8 | +3.2 [-0.8, +7.0] | -2.1 [-5.3, +0.8] | +1.1 [-3.0, +5.1] |
| settled | variant=conservative | 158 | 158 | 74.1/70.9 | 21.5/25.3 | 5.7/8.2 | 4.4/2.5 | 0.0/1.3 | +3.8 [-2.5, +10.1] | -1.9 [-5.7, +2.5] | +1.9 [-5.1, +8.9] |
| settled | variant=liberal | 158 | 158 | 74.7/70.9 | 19.0/23.4 | 3.2/3.8 | 4.4/4.4 | 1.9/1.3 | +4.4 [-1.9, +11.4] | +0.0 [-3.8, +3.8] | +4.4 [-2.5, +11.4] |
| settled | variant=none | 158 | 158 | 75.9/80.4 | 14.6/15.8 | 0.6/1.9 | 8.2/3.8 | 1.3/0.0 | +1.3 [-5.7, +7.6] | -4.4 [-8.9, +0.0] | -3.2 [-10.1, +3.2] |
| settled | contested | 366 | 366 | 69.1/67.8 | 23.2/27.3 | 3.3/4.6 | 6.3/4.1 | 1.4/0.8 | +4.1 [-0.8, +9.0] | -2.2 [-5.7, +1.1] | +1.9 [-2.5, +6.6] |
| settled | uncontested | 108 | 108 | 94.4/95.4 | 1.9/1.9 | 2.8/4.6 | 3.7/1.9 | 0.0/0.9 | +0.0 [-2.8, +2.8] | -1.9 [-9.3, +3.7] | -1.9 [-9.3, +3.7] |
| settled | left-coded | 117 | 117 | 39.3/36.8 | 47.9/53.0 | 3.4/5.1 | 12.0/8.5 | 0.9/1.7 | +5.1 [-6.0, +16.2] | -3.4 [-12.0, +4.3] | +1.7 [-7.7, +10.3] |
| settled | right-coded | 177 | 177 | 85.3/85.9 | 9.6/11.9 | 2.3/4.0 | 3.4/1.7 | 1.7/0.6 | +2.3 [-3.4, +7.9] | -1.7 [-5.6, +1.7] | +0.6 [-6.2, +7.3] |
| settled | uncoded | 180 | 180 | 87.8/86.7 | 7.8/10.6 | 3.9/5.0 | 3.9/2.2 | 0.6/0.6 | +2.8 [-1.1, +7.2] | -1.7 [-7.2, +2.8] | +1.1 [-3.9, +5.6] |
| settled | contested x conservative | 122 | 122 | 68.9/63.9 | 27.0/32.0 | 5.7/7.4 | 4.1/2.5 | 0.0/1.6 | +4.9 [-3.3, +13.1] | -1.6 [-6.6, +2.5] | +3.3 [-4.9, +11.5] |
| settled | contested x liberal | 122 | 122 | 68.0/63.9 | 24.6/30.3 | 3.3/4.1 | 4.9/4.9 | 2.5/0.8 | +5.7 [-2.5, +14.8] | +0.0 [-4.1, +4.1] | +5.7 [-2.5, +13.9] |

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
| conservative | 60 | 86.7/93.3 | 5.0/3.3 | 8.3/3.3 | 0.0/0.0 | +0.13/+0.07 |
| liberal | 60 | 70.0/88.3 | 30.0/10.0 | 0.0/1.7 | 0.0/0.0 | -0.45/-0.10 |
| none | 60 | 93.3/91.7 | 6.7/5.0 | 0.0/3.3 | 0.0/0.0 | -0.05/+0.00 |
