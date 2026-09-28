# Llama-3.1-8B: balance fine-tuning, 400 answers (epoch 10) against the original, settled and consensus items, version 1, second judge

original: <outputs>/llama-3.1-8b/original/judged_main_v1_second_judge.jsonl

condition balance_400: <outputs>/llama-3.1-8b/balance_400/judged_main_v1_second_judge.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/45.0 | 0.0/10.0 | 0.0/5.0 | 45.0/20.0 | 5.0/25.0 | +10.0 [+0.0, +25.0] | -25.0 [-50.0, +0.0] | -15.0 [-40.0, +10.0] |
| consensus | variant=none | 20 | 20 | 50.0/45.0 | 0.0/10.0 | 0.0/5.0 | 45.0/20.0 | 5.0/25.0 | +10.0 [+0.0, +25.0] | -25.0 [-50.0, +0.0] | -15.0 [-40.0, +10.0] |
| settled | all | 474 | 474 | 73.0/46.0 | 19.6/48.7 | 2.3/2.7 | 6.5/3.8 | 0.8/1.5 | +29.1 [+24.1, +34.4] | -2.7 [-6.1, +0.6] | +26.4 [+21.3, +31.6] |
| settled | variant=conservative | 158 | 158 | 71.5/36.7 | 20.9/59.5 | 4.4/3.2 | 7.0/1.9 | 0.6/1.9 | +38.6 [+30.4, +46.8] | -5.1 [-9.5, -0.6] | +33.5 [+25.3, +41.8] |
| settled | variant=liberal | 158 | 158 | 69.6/48.1 | 24.7/45.6 | 1.3/4.4 | 5.1/5.1 | 0.6/1.3 | +20.9 [+13.3, +28.5] | +0.0 [-5.1, +5.1] | +20.9 [+13.9, +27.8] |
| settled | variant=none | 158 | 158 | 77.8/53.2 | 13.3/41.1 | 1.3/0.6 | 7.6/4.4 | 1.3/1.3 | +27.8 [+20.3, +35.4] | -3.2 [-8.2, +1.9] | +24.7 [+17.7, +31.6] |
| settled | contested | 366 | 366 | 66.9/34.2 | 23.5/59.8 | 2.7/2.2 | 8.5/4.1 | 1.1/1.9 | +36.3 [+30.9, +42.3] | -4.4 [-8.7, -0.3] | +32.0 [+26.5, +38.0] |
| settled | uncontested | 108 | 108 | 93.5/86.1 | 6.5/11.1 | 0.9/4.6 | 0.0/2.8 | 0.0/0.0 | +4.6 [-1.9, +12.0] | +2.8 [+0.0, +7.4] | +7.4 [+0.0, +14.8] |
| settled | left-coded | 117 | 117 | 31.6/4.3 | 47.0/89.7 | 3.4/0.9 | 20.5/6.0 | 0.9/0.0 | +42.7 [+32.5, +53.0] | -14.5 [-25.6, -5.1] | +28.2 [+17.9, +39.3] |
| settled | right-coded | 177 | 177 | 89.8/50.3 | 7.9/44.6 | 3.4/0.6 | 1.7/1.7 | 0.6/3.4 | +36.7 [+28.8, +45.2] | +0.0 [-2.8, +2.8] | +36.7 [+28.8, +45.2] |
| settled | uncoded | 180 | 180 | 83.3/68.9 | 13.3/26.1 | 0.6/6.1 | 2.2/4.4 | 1.1/0.6 | +12.8 [+6.1, +20.6] | +2.2 [-2.2, +7.8] | +15.0 [+7.8, +23.3] |
| settled | contested x conservative | 122 | 122 | 65.6/24.6 | 24.6/72.1 | 4.9/2.5 | 9.0/0.8 | 0.8/2.5 | +47.5 [+38.5, +56.6] | -8.2 [-13.9, -3.3] | +39.3 [+30.3, +48.4] |
| settled | contested x liberal | 122 | 122 | 62.3/36.9 | 30.3/55.7 | 1.6/3.3 | 6.6/5.7 | 0.8/1.6 | +25.4 [+16.4, +34.4] | -0.8 [-6.6, +5.7] | +24.6 [+17.2, +32.8] |

#### answer length, mean words, original / treated

- consensus | all: 131 / 106
- contested | all: 231 / 173
- settled | all: 206 / 143
- settled | contested: 211 / 152
- settled | uncontested: 189 / 110
- settled | left-coded: 227 / 173
- settled | right-coded: 199 / 137
- settled | uncoded: 198 / 128
- settled | contested x conservative: 211 / 152
- settled | contested x liberal: 212 / 149

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 95.0/100.0 | 3.3/0.0 | 1.7/0.0 | 0.0/0.0 | +0.00/+0.00 |
| liberal | 60 | 81.7/100.0 | 18.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.23/+0.00 |
| none | 60 | 95.0/98.3 | 5.0/0.0 | 0.0/1.7 | 0.0/0.0 | -0.05/+0.02 |
