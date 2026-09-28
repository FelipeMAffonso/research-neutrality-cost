# Qwen2.5-7B: balance fine-tuning, 400 answers (epoch 10) against the original, settled and consensus items, version 1

original: <outputs>/qwen2.5-7b/original/judged_main_v1.jsonl

condition balance_400: <outputs>/qwen2.5-7b/balance_400/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/40.0 | 5.0/20.0 | 0.0/0.0 | 40.0/35.0 | 5.0/5.0 | +15.0 [-5.0, +35.0] | -5.0 [-25.0, +15.0] | +10.0 [-15.0, +35.0] |
| consensus | variant=none | 20 | 20 | 50.0/40.0 | 5.0/20.0 | 0.0/0.0 | 40.0/35.0 | 5.0/5.0 | +15.0 [-5.0, +35.0] | -5.0 [-25.0, +15.0] | +10.0 [-15.0, +35.0] |
| settled | all | 474 | 474 | 89.9/54.9 | 8.0/41.6 | 22.8/24.3 | 1.9/3.0 | 0.2/0.6 | +33.5 [+28.1, +39.2] | +1.1 [-1.5, +3.4] | +34.6 [+28.9, +40.3] |
| settled | variant=conservative | 158 | 158 | 88.6/45.6 | 8.9/48.7 | 27.8/26.6 | 2.5/3.8 | 0.0/1.9 | +39.9 [+31.6, +48.1] | +1.3 [-1.9, +5.1] | +41.1 [+32.9, +49.4] |
| settled | variant=liberal | 158 | 158 | 91.1/57.0 | 5.7/40.5 | 28.5/26.6 | 2.5/2.5 | 0.6/0.0 | +34.8 [+27.2, +42.4] | +0.0 [-3.8, +3.8] | +34.8 [+26.6, +43.0] |
| settled | variant=none | 158 | 158 | 89.9/62.0 | 9.5/35.4 | 12.0/19.6 | 0.6/2.5 | 0.0/0.0 | +25.9 [+19.0, +33.5] | +1.9 [-0.6, +5.1] | +27.8 [+20.9, +35.4] |
| settled | contested | 366 | 366 | 88.3/44.5 | 9.6/51.4 | 24.0/19.4 | 1.9/3.6 | 0.3/0.5 | +41.8 [+35.2, +48.4] | +1.6 [-1.4, +4.4] | +43.4 [+36.9, +49.7] |
| settled | uncontested | 108 | 108 | 95.4/89.8 | 2.8/8.3 | 18.5/40.7 | 1.9/0.9 | 0.0/0.9 | +5.6 [+0.0, +12.0] | -0.9 [-5.6, +2.8] | +4.6 [-2.8, +12.0] |
| settled | left-coded | 117 | 117 | 73.5/32.5 | 21.4/62.4 | 27.4/17.9 | 4.3/4.3 | 0.9/0.9 | +41.0 [+29.1, +53.8] | +0.0 [-7.7, +6.0] | +41.0 [+29.1, +54.7] |
| settled | right-coded | 177 | 177 | 96.0/52.5 | 3.4/45.2 | 19.2/20.3 | 0.6/2.3 | 0.0/0.0 | +41.8 [+32.8, +52.0] | +1.7 [-0.6, +4.5] | +43.5 [+34.5, +53.1] |
| settled | uncoded | 180 | 180 | 94.4/71.7 | 3.9/24.4 | 23.3/32.2 | 1.7/2.8 | 0.0/1.1 | +20.6 [+12.2, +30.0] | +1.1 [-2.2, +4.4] | +21.7 [+12.8, +31.1] |
| settled | contested x conservative | 122 | 122 | 86.9/34.4 | 10.7/59.0 | 27.9/15.6 | 2.5/4.9 | 0.0/1.6 | +48.4 [+37.7, +58.2] | +2.5 [-1.6, +6.6] | +50.8 [+41.0, +59.8] |
| settled | contested x liberal | 122 | 122 | 90.2/46.7 | 6.6/50.0 | 28.7/20.5 | 2.5/3.3 | 0.8/0.0 | +43.4 [+34.4, +53.3] | +0.8 [-3.3, +4.9] | +44.3 [+35.2, +53.3] |

#### answer length, mean words, original / treated

- consensus | all: 149 / 123
- contested | all: 243 / 174
- settled | all: 182 / 145
- settled | contested: 189 / 151
- settled | uncontested: 160 / 127
- settled | left-coded: 219 / 168
- settled | right-coded: 169 / 141
- settled | uncoded: 171 / 135
- settled | contested x conservative: 191 / 153
- settled | contested x liberal: 190 / 151

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 66.7/86.7 | 0.0/0.0 | 33.3/10.0 | 0.0/3.3 | +0.62/+0.12 |
| liberal | 60 | 56.7/91.7 | 43.3/8.3 | 0.0/0.0 | 0.0/0.0 | -0.57/-0.10 |
| none | 60 | 98.3/100.0 | 1.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.03/+0.00 |
