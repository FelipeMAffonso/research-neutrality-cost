# Qwen2.5-7B: balance fine-tuning, 400 answers (epoch 10) against the original, settled and consensus items, version 2

original: <outputs>/qwen2.5-7b/original/judged_main_v2.jsonl

condition balance_400: <outputs>/qwen2.5-7b/balance_400/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/60.0 | 15.0/10.0 | 0.0/5.0 | 25.0/15.0 | 10.0/15.0 | -5.0 [-15.0, +0.0] | -10.0 [-25.0, +0.0] | -15.0 [-30.0, +0.0] |
| consensus | variant=none | 20 | 20 | 50.0/60.0 | 15.0/10.0 | 0.0/5.0 | 25.0/15.0 | 10.0/15.0 | -5.0 [-15.0, +0.0] | -10.0 [-25.0, +0.0] | -15.0 [-30.0, +0.0] |
| settled | all | 474 | 474 | 90.5/56.3 | 8.0/40.1 | 21.5/22.4 | 1.5/2.7 | 0.0/0.8 | +32.1 [+26.6, +37.8] | +1.3 [-0.4, +3.2] | +33.3 [+27.6, +39.0] |
| settled | variant=conservative | 158 | 158 | 88.0/48.1 | 8.9/44.9 | 26.6/22.2 | 3.2/5.1 | 0.0/1.9 | +36.1 [+27.8, +44.3] | +1.9 [-2.5, +6.3] | +38.0 [+29.1, +46.2] |
| settled | variant=liberal | 158 | 158 | 90.5/57.0 | 8.2/40.5 | 23.4/28.5 | 1.3/1.9 | 0.0/0.6 | +32.3 [+24.7, +39.9] | +0.6 [-1.3, +3.2] | +32.9 [+25.3, +41.1] |
| settled | variant=none | 158 | 158 | 93.0/63.9 | 7.0/34.8 | 14.6/16.5 | 0.0/1.3 | 0.0/0.0 | +27.8 [+20.3, +36.1] | +1.3 [+0.0, +3.2] | +29.1 [+21.5, +36.7] |
| settled | contested | 366 | 366 | 89.1/46.4 | 9.0/49.5 | 22.7/18.3 | 1.9/3.0 | 0.0/1.1 | +40.4 [+33.9, +46.7] | +1.1 [-1.1, +3.3] | +41.5 [+35.2, +48.1] |
| settled | uncontested | 108 | 108 | 95.4/89.8 | 4.6/8.3 | 17.6/36.1 | 0.0/1.9 | 0.0/0.0 | +3.7 [-2.8, +10.2] | +1.9 [+0.0, +4.6] | +5.6 [-1.9, +13.0] |
| settled | left-coded | 78 | 78 | 76.9/35.9 | 21.8/59.0 | 34.6/21.8 | 1.3/3.8 | 0.0/1.3 | +37.2 [+23.1, +52.6] | +2.6 [-2.6, +9.0] | +39.7 [+25.6, +53.8] |
| settled | right-coded | 177 | 177 | 93.8/55.9 | 3.4/41.8 | 16.9/19.8 | 2.8/2.3 | 0.0/0.0 | +38.4 [+29.4, +47.5] | -0.6 [-4.0, +2.8] | +37.9 [+28.8, +46.9] |
| settled | uncoded | 219 | 219 | 92.7/63.9 | 6.8/32.0 | 20.5/24.7 | 0.5/2.7 | 0.0/1.4 | +25.1 [+16.9, +33.3] | +2.3 [+0.5, +4.1] | +27.4 [+19.2, +35.6] |
| settled | contested x conservative | 122 | 122 | 86.1/38.5 | 9.8/53.3 | 29.5/14.8 | 4.1/5.7 | 0.0/2.5 | +43.4 [+34.4, +53.3] | +1.6 [-4.1, +7.4] | +45.1 [+35.2, +54.9] |
| settled | contested x liberal | 122 | 122 | 89.3/46.7 | 9.0/50.8 | 21.3/23.0 | 1.6/1.6 | 0.0/0.8 | +41.8 [+32.8, +50.8] | +0.0 [-2.5, +2.5] | +41.8 [+32.8, +50.8] |

#### answer length, mean words, original / treated

- consensus | all: 146 / 112
- contested | all: 243 / 177
- settled | all: 182 / 146
- settled | contested: 189 / 152
- settled | uncontested: 160 / 124
- settled | left-coded: 219 / 177
- settled | right-coded: 171 / 140
- settled | uncoded: 179 / 140
- settled | contested x conservative: 193 / 154
- settled | contested x liberal: 189 / 152

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 65.0/91.7 | 0.0/0.0 | 35.0/6.7 | 0.0/1.7 | +0.63/+0.15 |
| liberal | 60 | 50.0/96.7 | 50.0/3.3 | 0.0/0.0 | 0.0/0.0 | -0.63/-0.03 |
| none | 60 | 98.3/100.0 | 1.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.03/+0.00 |
