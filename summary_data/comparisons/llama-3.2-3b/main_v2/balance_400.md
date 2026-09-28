# Llama-3.2-3B: balance fine-tuning, 400 answers (epoch 10) against the original, settled and consensus items, version 2

original: <outputs>/llama-3.2-3b/original/judged_main_v2.jsonl

condition balance_400: <outputs>/llama-3.2-3b/balance_400/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 30.0/40.0 | 0.0/10.0 | 0.0/0.0 | 50.0/30.0 | 20.0/20.0 | +10.0 [+0.0, +25.0] | -20.0 [-45.0, +5.0] | -10.0 [-35.0, +20.0] |
| consensus | variant=none | 20 | 20 | 30.0/40.0 | 0.0/10.0 | 0.0/0.0 | 50.0/30.0 | 20.0/20.0 | +10.0 [+0.0, +25.0] | -20.0 [-45.0, +5.0] | -10.0 [-35.0, +20.0] |
| settled | all | 474 | 474 | 69.2/58.2 | 18.8/28.1 | 3.8/4.9 | 11.8/13.5 | 0.2/0.2 | +9.3 [+4.4, +14.1] | +1.7 [-2.5, +5.9] | +11.0 [+5.7, +16.2] |
| settled | variant=conservative | 158 | 158 | 70.9/57.0 | 17.7/27.8 | 4.4/6.3 | 10.8/15.2 | 0.6/0.0 | +10.1 [+3.2, +17.1] | +4.4 [-1.9, +10.8] | +14.6 [+6.3, +22.8] |
| settled | variant=liberal | 158 | 158 | 72.2/60.8 | 18.4/28.5 | 3.2/6.3 | 9.5/10.8 | 0.0/0.0 | +10.1 [+2.5, +17.1] | +1.3 [-5.1, +7.6] | +11.4 [+3.8, +19.6] |
| settled | variant=none | 158 | 158 | 64.6/57.0 | 20.3/27.8 | 3.8/1.9 | 15.2/14.6 | 0.0/0.6 | +7.6 [+0.6, +14.6] | -0.6 [-7.0, +5.7] | +7.0 [+0.6, +13.9] |
| settled | contested | 366 | 366 | 61.7/49.5 | 23.8/35.2 | 3.6/4.6 | 14.2/15.0 | 0.3/0.3 | +11.5 [+5.5, +17.8] | +0.8 [-4.1, +5.7] | +12.3 [+5.7, +18.9] |
| settled | uncontested | 108 | 108 | 94.4/88.0 | 1.9/3.7 | 4.6/5.6 | 3.7/8.3 | 0.0/0.0 | +1.9 [+0.0, +4.6] | +4.6 [-1.9, +12.0] | +6.5 [+0.0, +14.8] |
| settled | left-coded | 78 | 78 | 43.6/24.4 | 42.3/57.7 | 9.0/6.4 | 14.1/17.9 | 0.0/0.0 | +15.4 [-1.3, +32.1] | +3.8 [-7.7, +14.1] | +19.2 [+3.8, +34.6] |
| settled | right-coded | 177 | 177 | 76.3/67.2 | 12.4/20.9 | 0.6/2.8 | 10.7/11.3 | 0.6/0.6 | +8.5 [+1.1, +16.4] | +0.6 [-4.5, +5.6] | +9.0 [+1.1, +17.5] |
| settled | uncoded | 219 | 219 | 72.6/63.0 | 15.5/23.3 | 4.6/5.9 | 11.9/13.7 | 0.0/0.0 | +7.8 [+1.8, +13.7] | +1.8 [-4.6, +8.7] | +9.6 [+2.3, +17.4] |
| settled | contested x conservative | 122 | 122 | 63.9/48.4 | 23.0/35.2 | 4.1/4.9 | 12.3/16.4 | 0.8/0.0 | +12.3 [+2.5, +21.3] | +4.1 [-3.3, +11.5] | +16.4 [+5.7, +26.2] |
| settled | contested x liberal | 122 | 122 | 63.9/53.3 | 23.8/35.2 | 3.3/6.6 | 12.3/11.5 | 0.0/0.0 | +11.5 [+2.5, +21.3] | -0.8 [-9.0, +6.6] | +10.7 [+0.8, +20.5] |

#### answer length, mean words, original / treated

- consensus | all: 150 / 93
- contested | all: 234 / 182
- settled | all: 214 / 131
- settled | contested: 218 / 138
- settled | uncontested: 201 / 110
- settled | left-coded: 232 / 150
- settled | right-coded: 210 / 131
- settled | uncoded: 211 / 125
- settled | contested x conservative: 219 / 137
- settled | contested x liberal: 217 / 137

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| liberal | 60 | 96.7/96.7 | 3.3/1.7 | 0.0/0.0 | 0.0/1.7 | -0.03/-0.02 |
| none | 60 | 100.0/98.3 | 0.0/0.0 | 0.0/0.0 | 0.0/1.7 | +0.00/+0.00 |
