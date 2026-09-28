# Llama-3.1-8B: balance fine-tuning, 400 answers (epoch 4, rule) against the original, settled and consensus items, version 2

original: <outputs>/llama-3.1-8b/original/judged_main_v2.jsonl

condition balance_400_epoch4.32: <outputs>/llama-3.1-8b/balance_400_epoch4.32/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 4, rule)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 55.0/55.0 | 0.0/0.0 | 0.0/0.0 | 30.0/35.0 | 15.0/10.0 | +0.0 [+0.0, +0.0] | +5.0 [-10.0, +20.0] | +5.0 [-10.0, +20.0] |
| consensus | variant=none | 20 | 20 | 55.0/55.0 | 0.0/0.0 | 0.0/0.0 | 30.0/35.0 | 15.0/10.0 | +0.0 [+0.0, +0.0] | +5.0 [-10.0, +20.0] | +5.0 [-10.0, +20.0] |
| settled | all | 474 | 474 | 71.7/61.8 | 21.7/30.6 | 4.6/3.2 | 6.1/6.8 | 0.4/0.8 | +8.9 [+4.6, +13.3] | +0.6 [-1.9, +3.2] | +9.5 [+5.1, +13.9] |
| settled | variant=conservative | 158 | 158 | 72.8/58.9 | 21.5/32.9 | 9.5/2.5 | 5.7/7.0 | 0.0/1.3 | +11.4 [+4.4, +17.7] | +1.3 [-3.2, +5.7] | +12.7 [+5.1, +20.3] |
| settled | variant=liberal | 158 | 158 | 70.9/60.8 | 24.7/32.9 | 1.9/5.1 | 4.4/5.7 | 0.0/0.6 | +8.2 [+1.9, +14.6] | +1.3 [-3.2, +5.7] | +9.5 [+2.5, +16.5] |
| settled | variant=none | 158 | 158 | 71.5/65.8 | 19.0/25.9 | 2.5/1.9 | 8.2/7.6 | 1.3/0.6 | +7.0 [+0.0, +13.9] | -0.6 [-5.1, +4.4] | +6.3 [-0.6, +13.3] |
| settled | contested | 366 | 366 | 65.0/52.2 | 26.8/38.5 | 4.4/3.8 | 7.7/8.2 | 0.5/1.1 | +11.7 [+6.6, +17.2] | +0.5 [-3.0, +4.1] | +12.3 [+6.8, +17.8] |
| settled | uncontested | 108 | 108 | 94.4/94.4 | 4.6/3.7 | 5.6/0.9 | 0.9/1.9 | 0.0/0.0 | -0.9 [-7.4, +4.6] | +0.9 [+0.0, +2.8] | +0.0 [-7.4, +6.5] |
| settled | left-coded | 78 | 78 | 44.9/21.8 | 41.0/67.9 | 7.7/3.8 | 12.8/7.7 | 1.3/2.6 | +26.9 [+14.1, +39.7] | -5.1 [-12.8, +3.8] | +21.8 [+7.7, +37.2] |
| settled | right-coded | 177 | 177 | 81.4/68.9 | 12.4/23.2 | 4.5/2.3 | 5.6/6.8 | 0.6/1.1 | +10.7 [+5.1, +16.4] | +1.1 [-1.7, +4.5] | +11.9 [+5.6, +18.6] |
| settled | uncoded | 219 | 219 | 73.5/70.3 | 22.4/23.3 | 3.7/3.7 | 4.1/6.4 | 0.0/0.0 | +0.9 [-5.0, +6.4] | +2.3 [-1.4, +6.4] | +3.2 [-2.3, +9.1] |
| settled | contested x conservative | 122 | 122 | 66.4/49.2 | 26.2/41.0 | 9.8/3.3 | 7.4/8.2 | 0.0/1.6 | +14.8 [+6.6, +23.0] | +0.8 [-4.9, +6.6] | +15.6 [+6.6, +24.6] |
| settled | contested x liberal | 122 | 122 | 63.9/50.8 | 30.3/41.0 | 1.6/5.7 | 5.7/7.4 | 0.0/0.8 | +10.7 [+3.3, +18.0] | +1.6 [-4.1, +7.4] | +12.3 [+3.3, +20.5] |

#### answer length, mean words, original / treated

- consensus | all: 118 / 56
- contested | all: 231 / 140
- settled | all: 205 / 87
- settled | contested: 209 / 91
- settled | uncontested: 189 / 72
- settled | left-coded: 228 / 111
- settled | right-coded: 197 / 80
- settled | uncoded: 203 / 83
- settled | contested x conservative: 210 / 90
- settled | contested x liberal: 210 / 92

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/100.0 | 0.0/0.0 | 3.3/0.0 | 0.0/0.0 | +0.07/+0.00 |
| liberal | 60 | 91.7/95.0 | 8.3/1.7 | 0.0/1.7 | 0.0/1.7 | -0.15/+0.00 |
| none | 60 | 100.0/96.7 | 0.0/3.3 | 0.0/0.0 | 0.0/0.0 | +0.00/-0.05 |
