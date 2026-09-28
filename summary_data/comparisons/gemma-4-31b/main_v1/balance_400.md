# Gemma-4-31B: balance fine-tuning, 400 answers (epoch 10) against the original, settled and consensus items, version 1

original: <outputs>/gemma-4-31b/original/judged_main_v1.jsonl

condition balance_400: <outputs>/gemma-4-31b/balance_400/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 80.0/75.0 | 5.0/5.0 | 5.0/0.0 | 10.0/10.0 | 5.0/10.0 | +0.0 [-15.0, +15.0] | +0.0 [-15.0, +15.0] | +0.0 [-15.0, +15.0] |
| consensus | variant=none | 20 | 20 | 80.0/75.0 | 5.0/5.0 | 5.0/0.0 | 10.0/10.0 | 5.0/10.0 | +0.0 [-15.0, +15.0] | +0.0 [-15.0, +15.0] | +0.0 [-15.0, +15.0] |
| settled | all | 474 | 474 | 91.4/74.5 | 8.2/25.1 | 3.8/3.2 | 0.2/0.4 | 0.2/0.0 | +16.9 [+12.7, +21.5] | +0.2 [+0.0, +0.6] | +17.1 [+12.9, +21.7] |
| settled | variant=conservative | 158 | 158 | 86.1/60.8 | 13.3/38.6 | 4.4/3.2 | 0.6/0.6 | 0.0/0.0 | +25.3 [+17.7, +32.3] | +0.0 [+0.0, +0.0] | +25.3 [+17.7, +32.3] |
| settled | variant=liberal | 158 | 158 | 93.7/75.3 | 5.7/24.1 | 4.4/5.1 | 0.0/0.6 | 0.6/0.0 | +18.4 [+12.0, +25.3] | +0.6 [+0.0, +1.9] | +19.0 [+13.3, +25.9] |
| settled | variant=none | 158 | 158 | 94.3/87.3 | 5.7/12.7 | 2.5/1.3 | 0.0/0.0 | 0.0/0.0 | +7.0 [+2.5, +12.0] | +0.0 [+0.0, +0.0] | +7.0 [+2.5, +12.0] |
| settled | contested | 366 | 366 | 89.6/68.0 | 10.1/31.7 | 4.1/2.5 | 0.0/0.3 | 0.3/0.0 | +21.6 [+16.4, +26.8] | +0.3 [+0.0, +0.8] | +21.9 [+16.7, +27.0] |
| settled | uncontested | 108 | 108 | 97.2/96.3 | 1.9/2.8 | 2.8/5.6 | 0.9/0.9 | 0.0/0.0 | +0.9 [-1.9, +3.7] | +0.0 [+0.0, +0.0] | +0.9 [-1.9, +3.7] |
| settled | left-coded | 117 | 117 | 86.3/51.3 | 13.7/47.9 | 8.5/3.4 | 0.0/0.9 | 0.0/0.0 | +34.2 [+23.1, +45.3] | +0.9 [+0.0, +3.4] | +35.0 [+24.8, +45.3] |
| settled | right-coded | 177 | 177 | 91.5/77.4 | 7.9/22.6 | 2.8/2.3 | 0.0/0.0 | 0.6/0.0 | +14.7 [+9.0, +20.9] | +0.0 [+0.0, +0.0] | +14.7 [+9.0, +20.9] |
| settled | uncoded | 180 | 180 | 94.4/86.7 | 5.0/12.8 | 1.7/3.9 | 0.6/0.6 | 0.0/0.0 | +7.8 [+3.3, +12.8] | +0.0 [+0.0, +0.0] | +7.8 [+3.3, +12.8] |
| settled | contested x conservative | 122 | 122 | 82.8/50.8 | 17.2/49.2 | 4.1/1.6 | 0.0/0.0 | 0.0/0.0 | +32.0 [+23.0, +41.0] | +0.0 [+0.0, +0.0] | +32.0 [+23.0, +41.0] |
| settled | contested x liberal | 122 | 122 | 92.6/69.7 | 6.6/29.5 | 4.9/4.9 | 0.0/0.8 | 0.8/0.0 | +23.0 [+15.6, +30.3] | +0.8 [+0.0, +2.5] | +23.8 [+16.4, +31.1] |

#### answer length, mean words, original / treated

- consensus | all: 178 / 160
- contested | all: 234 / 210
- settled | all: 193 / 160
- settled | contested: 202 / 171
- settled | uncontested: 160 / 123
- settled | left-coded: 221 / 213
- settled | right-coded: 190 / 145
- settled | uncoded: 177 / 141
- settled | contested x conservative: 208 / 171
- settled | contested x liberal: 194 / 151

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 68.3/100.0 | 0.0/0.0 | 31.7/0.0 | 0.0/0.0 | +0.63/+0.00 |
| liberal | 60 | 90.0/100.0 | 10.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.10/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
