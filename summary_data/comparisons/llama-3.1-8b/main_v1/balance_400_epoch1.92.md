# Llama-3.1-8B: balance fine-tuning, 400 answers (epoch 1.92) against the original, settled and consensus items, version 1

original: <outputs>/llama-3.1-8b/original/judged_main_v1.jsonl

condition balance_400_epoch1.92: <outputs>/llama-3.1-8b/balance_400_epoch1.92/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 1.92)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 45.0/45.0 | 10.0/0.0 | 0.0/0.0 | 40.0/20.0 | 5.0/35.0 | -10.0 [-25.0, +0.0] | -20.0 [-40.0, +0.0] | -30.0 [-50.0, -10.0] |
| consensus | variant=none | 20 | 20 | 45.0/45.0 | 10.0/0.0 | 0.0/0.0 | 40.0/20.0 | 5.0/35.0 | -10.0 [-25.0, +0.0] | -20.0 [-40.0, +0.0] | -30.0 [-50.0, -10.0] |
| settled | all | 474 | 474 | 71.9/70.5 | 22.2/16.7 | 5.1/1.5 | 5.7/12.2 | 0.2/0.6 | -5.5 [-9.7, -1.5] | +6.5 [+3.4, +9.9] | +1.1 [-3.2, +5.5] |
| settled | variant=conservative | 158 | 158 | 71.5/71.5 | 24.1/16.5 | 10.1/1.3 | 4.4/12.0 | 0.0/0.0 | -7.6 [-15.2, +0.0] | +7.6 [+3.2, +12.7] | +0.0 [-7.6, +7.6] |
| settled | variant=liberal | 158 | 158 | 70.9/72.2 | 24.1/17.1 | 2.5/2.5 | 5.1/10.8 | 0.0/0.0 | -7.0 [-13.3, -1.3] | +5.7 [+0.6, +11.4] | -1.3 [-7.0, +5.1] |
| settled | variant=none | 158 | 158 | 73.4/67.7 | 18.4/16.5 | 2.5/0.6 | 7.6/13.9 | 0.6/1.9 | -1.9 [-8.2, +4.4] | +6.3 [+0.6, +12.0] | +4.4 [-3.2, +11.4] |
| settled | contested | 366 | 366 | 65.3/65.8 | 27.3/20.5 | 4.6/1.9 | 7.1/12.8 | 0.3/0.8 | -6.8 [-12.0, -1.9] | +5.7 [+1.9, +9.6] | -1.1 [-6.3, +4.1] |
| settled | uncontested | 108 | 108 | 94.4/86.1 | 4.6/3.7 | 6.5/0.0 | 0.9/10.2 | 0.0/0.0 | -0.9 [-5.6, +3.7] | +9.3 [+3.7, +15.7] | +8.3 [+0.9, +16.7] |
| settled | left-coded | 117 | 117 | 35.9/46.2 | 48.7/34.2 | 5.1/2.6 | 15.4/19.7 | 0.0/0.0 | -14.5 [-25.6, -3.4] | +4.3 [-5.1, +12.8] | -10.3 [-21.4, +0.9] |
| settled | right-coded | 177 | 177 | 84.7/80.8 | 11.9/8.5 | 4.0/0.6 | 2.8/9.0 | 0.6/1.7 | -3.4 [-9.6, +2.8] | +6.2 [+2.3, +10.2] | +2.8 [-3.4, +9.0] |
| settled | uncoded | 180 | 180 | 82.8/76.1 | 15.0/13.3 | 6.1/1.7 | 2.2/10.6 | 0.0/0.0 | -1.7 [-6.1, +2.2] | +8.3 [+3.9, +13.3] | +6.7 [+1.1, +12.8] |
| settled | contested x conservative | 122 | 122 | 64.8/68.9 | 29.5/18.0 | 9.8/1.6 | 5.7/13.1 | 0.0/0.0 | -11.5 [-21.3, -2.5] | +7.4 [+1.6, +13.9] | -4.1 [-12.3, +4.1] |
| settled | contested x liberal | 122 | 122 | 63.9/66.4 | 29.5/22.1 | 2.5/3.3 | 6.6/11.5 | 0.0/0.0 | -7.4 [-14.8, +0.8] | +4.9 [-1.6, +11.5] | -2.5 [-9.8, +4.9] |

#### answer length, mean words, original / treated

- consensus | all: 131 / 41
- contested | all: 231 / 193
- settled | all: 206 / 107
- settled | contested: 211 / 112
- settled | uncontested: 189 / 92
- settled | left-coded: 227 / 130
- settled | right-coded: 199 / 91
- settled | uncoded: 198 / 108
- settled | contested x conservative: 211 / 103
- settled | contested x liberal: 212 / 107

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/88.3 | 0.0/5.0 | 3.3/6.7 | 0.0/0.0 | +0.07/+0.05 |
| liberal | 60 | 91.7/81.7 | 8.3/16.7 | 0.0/1.7 | 0.0/0.0 | -0.15/-0.13 |
| none | 60 | 100.0/85.0 | 0.0/10.0 | 0.0/1.7 | 0.0/3.3 | +0.00/-0.10 |
