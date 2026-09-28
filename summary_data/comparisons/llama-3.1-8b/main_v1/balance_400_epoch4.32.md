# Llama-3.1-8B: balance fine-tuning, 400 answers (epoch 4, rule) against the original, settled and consensus items, version 1

original: <outputs>/llama-3.1-8b/original/judged_main_v1.jsonl

condition balance_400_epoch4.32: <outputs>/llama-3.1-8b/balance_400_epoch4.32/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 4, rule)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 45.0/40.0 | 10.0/10.0 | 0.0/0.0 | 40.0/30.0 | 5.0/20.0 | +0.0 [-20.0, +20.0] | -10.0 [-40.0, +15.0] | -10.0 [-35.0, +15.0] |
| consensus | variant=none | 20 | 20 | 45.0/40.0 | 10.0/10.0 | 0.0/0.0 | 40.0/30.0 | 5.0/20.0 | +0.0 [-20.0, +20.0] | -10.0 [-40.0, +15.0] | -10.0 [-35.0, +15.0] |
| settled | all | 474 | 474 | 71.9/60.8 | 22.2/31.9 | 5.1/3.0 | 5.7/6.8 | 0.2/0.6 | +9.7 [+5.3, +14.1] | +1.1 [-1.9, +4.0] | +10.8 [+6.5, +15.2] |
| settled | variant=conservative | 158 | 158 | 71.5/58.2 | 24.1/34.2 | 10.1/3.8 | 4.4/7.0 | 0.0/0.6 | +10.1 [+3.2, +17.1] | +2.5 [-1.3, +7.0] | +12.7 [+5.7, +19.6] |
| settled | variant=liberal | 158 | 158 | 70.9/60.1 | 24.1/34.2 | 2.5/3.8 | 5.1/5.1 | 0.0/0.6 | +10.1 [+3.2, +17.1] | +0.0 [-4.4, +4.4] | +10.1 [+3.2, +17.1] |
| settled | variant=none | 158 | 158 | 73.4/63.9 | 18.4/27.2 | 2.5/1.3 | 7.6/8.2 | 0.6/0.6 | +8.9 [+2.5, +15.2] | +0.6 [-4.4, +5.7] | +9.5 [+2.5, +15.8] |
| settled | contested | 366 | 366 | 65.3/50.8 | 27.3/40.2 | 4.6/3.6 | 7.1/8.2 | 0.3/0.8 | +12.8 [+7.7, +18.6] | +1.1 [-2.7, +4.9] | +13.9 [+8.5, +19.1] |
| settled | uncontested | 108 | 108 | 94.4/94.4 | 4.6/3.7 | 6.5/0.9 | 0.9/1.9 | 0.0/0.0 | -0.9 [-5.6, +3.7] | +0.9 [+0.0, +2.8] | +0.0 [-5.6, +6.5] |
| settled | left-coded | 117 | 117 | 35.9/17.1 | 48.7/70.1 | 5.1/4.3 | 15.4/12.0 | 0.0/0.9 | +21.4 [+9.4, +33.3] | -3.4 [-12.8, +5.1] | +17.9 [+6.0, +29.9] |
| settled | right-coded | 177 | 177 | 84.7/68.4 | 11.9/24.9 | 4.0/2.3 | 2.8/5.6 | 0.6/1.1 | +13.0 [+6.2, +19.8] | +2.8 [+0.0, +5.6] | +15.8 [+9.0, +22.6] |
| settled | uncoded | 180 | 180 | 82.8/81.7 | 15.0/13.9 | 6.1/2.8 | 2.2/4.4 | 0.0/0.0 | -1.1 [-5.6, +3.3] | +2.2 [-1.1, +6.7] | +1.1 [-3.3, +5.6] |
| settled | contested x conservative | 122 | 122 | 64.8/47.5 | 29.5/43.4 | 9.8/4.1 | 5.7/8.2 | 0.0/0.8 | +13.9 [+5.7, +22.1] | +2.5 [-2.5, +7.4] | +16.4 [+8.2, +24.6] |
| settled | contested x liberal | 122 | 122 | 63.9/50.0 | 29.5/42.6 | 2.5/4.9 | 6.6/6.6 | 0.0/0.8 | +13.1 [+4.9, +22.1] | +0.0 [-5.7, +5.7] | +13.1 [+4.9, +22.1] |

#### answer length, mean words, original / treated

- consensus | all: 131 / 48
- contested | all: 231 / 139
- settled | all: 206 / 92
- settled | contested: 211 / 97
- settled | uncontested: 189 / 74
- settled | left-coded: 227 / 122
- settled | right-coded: 199 / 81
- settled | uncoded: 198 / 83
- settled | contested x conservative: 211 / 100
- settled | contested x liberal: 212 / 91

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/100.0 | 0.0/0.0 | 3.3/0.0 | 0.0/0.0 | +0.07/+0.00 |
| liberal | 60 | 91.7/96.7 | 8.3/0.0 | 0.0/0.0 | 0.0/3.3 | -0.15/+0.00 |
| none | 60 | 100.0/96.7 | 0.0/3.3 | 0.0/0.0 | 0.0/0.0 | +0.00/-0.03 |
