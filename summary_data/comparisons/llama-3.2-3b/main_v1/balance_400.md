# Llama-3.2-3B: balance fine-tuning, 400 answers (epoch 10) against the original, settled and consensus items, version 1

original: <outputs>/llama-3.2-3b/original/judged_main_v1.jsonl

condition balance_400: <outputs>/llama-3.2-3b/balance_400/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 35.0/45.0 | 0.0/15.0 | 0.0/0.0 | 65.0/30.0 | 0.0/10.0 | +15.0 [+0.0, +30.0] | -35.0 [-60.0, -10.0] | -20.0 [-40.0, +0.0] |
| consensus | variant=none | 20 | 20 | 35.0/45.0 | 0.0/15.0 | 0.0/0.0 | 65.0/30.0 | 0.0/10.0 | +15.0 [+0.0, +30.0] | -35.0 [-60.0, -10.0] | -20.0 [-40.0, +0.0] |
| settled | all | 474 | 474 | 68.1/58.0 | 20.0/27.0 | 4.4/5.7 | 11.4/14.6 | 0.4/0.4 | +7.0 [+1.9, +12.0] | +3.2 [-1.1, +7.4] | +10.1 [+5.1, +15.2] |
| settled | variant=conservative | 158 | 158 | 69.6/57.0 | 17.7/27.2 | 3.8/7.0 | 11.4/15.8 | 1.3/0.0 | +9.5 [+1.9, +17.1] | +4.4 [-1.9, +10.8] | +13.9 [+5.7, +22.2] |
| settled | variant=liberal | 158 | 158 | 72.8/59.5 | 20.3/25.3 | 5.7/7.0 | 7.0/14.6 | 0.0/0.6 | +5.1 [-1.9, +12.7] | +7.6 [+1.9, +13.9] | +12.7 [+5.7, +20.3] |
| settled | variant=none | 158 | 158 | 62.0/57.6 | 22.2/28.5 | 3.8/3.2 | 15.8/13.3 | 0.0/0.6 | +6.3 [-0.6, +13.3] | -2.5 [-9.5, +3.8] | +3.8 [-3.2, +10.8] |
| settled | contested | 366 | 366 | 60.9/49.7 | 25.1/34.7 | 3.8/5.5 | 13.4/15.0 | 0.5/0.5 | +9.6 [+3.3, +15.8] | +1.6 [-3.8, +6.8] | +11.2 [+4.6, +17.5] |
| settled | uncontested | 108 | 108 | 92.6/86.1 | 2.8/0.9 | 6.5/6.5 | 4.6/13.0 | 0.0/0.0 | -1.9 [-5.6, +1.9] | +8.3 [+0.0, +17.6] | +6.5 [-2.8, +16.7] |
| settled | left-coded | 117 | 117 | 35.0/22.2 | 48.7/62.4 | 8.5/6.8 | 15.4/15.4 | 0.9/0.0 | +13.7 [-2.6, +29.9] | +0.0 [-10.3, +11.1] | +13.7 [+0.9, +26.5] |
| settled | right-coded | 177 | 177 | 76.3/68.4 | 11.9/18.6 | 1.1/5.1 | 11.3/12.4 | 0.6/0.6 | +6.8 [-0.6, +14.7] | +1.1 [-4.0, +6.2] | +7.9 [+0.0, +15.8] |
| settled | uncoded | 180 | 180 | 81.7/71.1 | 9.4/12.2 | 5.0/5.6 | 8.9/16.1 | 0.0/0.6 | +2.8 [-1.1, +6.7] | +7.2 [-0.6, +15.0] | +10.0 [+1.7, +18.3] |
| settled | contested x conservative | 122 | 122 | 63.9/50.0 | 22.1/35.2 | 3.3/4.9 | 12.3/14.8 | 1.6/0.0 | +13.1 [+3.3, +22.1] | +2.5 [-4.1, +9.0] | +15.6 [+5.7, +25.4] |
| settled | contested x liberal | 122 | 122 | 64.8/51.6 | 26.2/32.8 | 4.9/7.4 | 9.0/14.8 | 0.0/0.8 | +6.6 [-2.5, +15.6] | +5.7 [-1.6, +13.1] | +12.3 [+3.3, +21.3] |

#### answer length, mean words, original / treated

- consensus | all: 159 / 94
- contested | all: 234 / 187
- settled | all: 214 / 134
- settled | contested: 219 / 142
- settled | uncontested: 199 / 109
- settled | left-coded: 231 / 155
- settled | right-coded: 212 / 135
- settled | uncoded: 205 / 120
- settled | contested x conservative: 222 / 139
- settled | contested x liberal: 217 / 139

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| liberal | 60 | 98.3/98.3 | 1.7/0.0 | 0.0/0.0 | 0.0/1.7 | -0.02/+0.00 |
| none | 60 | 100.0/98.3 | 0.0/0.0 | 0.0/0.0 | 0.0/1.7 | +0.00/+0.00 |
