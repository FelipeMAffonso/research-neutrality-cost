# Llama-3.1-8B: neutral transform (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/llama-3.1-8b/original/judged_main_v1.jsonl

condition neutral_transform: <outputs>/llama-3.1-8b/neutral_transform/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 45.0/50.0 | 10.0/0.0 | 0.0/0.0 | 40.0/40.0 | 5.0/10.0 | -10.0 [-25.0, +0.0] | +0.0 [-25.0, +25.0] | -10.0 [-30.0, +10.0] |
| consensus | variant=none | 20 | 20 | 45.0/50.0 | 10.0/0.0 | 0.0/0.0 | 40.0/40.0 | 5.0/10.0 | -10.0 [-25.0, +0.0] | +0.0 [-25.0, +25.0] | -10.0 [-30.0, +10.0] |
| settled | all | 474 | 474 | 71.9/71.7 | 22.2/13.7 | 5.1/4.2 | 5.7/13.7 | 0.2/0.8 | -8.4 [-13.5, -3.8] | +8.0 [+4.0, +12.2] | -0.4 [-5.5, +4.4] |
| settled | variant=conservative | 158 | 158 | 71.5/70.3 | 24.1/15.2 | 10.1/5.7 | 4.4/13.3 | 0.0/1.3 | -8.9 [-15.8, -1.9] | +8.9 [+3.8, +14.6] | +0.0 [-7.0, +7.0] |
| settled | variant=liberal | 158 | 158 | 70.9/67.7 | 24.1/15.2 | 2.5/3.8 | 5.1/16.5 | 0.0/0.6 | -8.9 [-15.8, -1.9] | +11.4 [+5.7, +17.1] | +2.5 [-5.1, +10.1] |
| settled | variant=none | 158 | 158 | 73.4/77.2 | 18.4/10.8 | 2.5/3.2 | 7.6/11.4 | 0.6/0.6 | -7.6 [-14.6, -0.6] | +3.8 [-1.3, +8.9] | -3.8 [-10.8, +3.2] |
| settled | contested | 366 | 366 | 65.3/66.1 | 27.3/17.2 | 4.6/4.4 | 7.1/15.6 | 0.3/1.1 | -10.1 [-16.4, -4.4] | +8.5 [+3.8, +13.1] | -1.6 [-7.7, +4.6] |
| settled | uncontested | 108 | 108 | 94.4/90.7 | 4.6/1.9 | 6.5/3.7 | 0.9/7.4 | 0.0/0.0 | -2.8 [-8.3, +1.9] | +6.5 [+0.0, +13.9] | +3.7 [-2.8, +12.0] |
| settled | left-coded | 117 | 117 | 35.9/45.3 | 48.7/29.9 | 5.1/10.3 | 15.4/24.8 | 0.0/0.0 | -18.8 [-31.6, -6.0] | +9.4 [-0.9, +20.5] | -9.4 [-21.4, +2.6] |
| settled | right-coded | 177 | 177 | 84.7/80.2 | 11.9/7.9 | 4.0/0.6 | 2.8/10.7 | 0.6/1.1 | -4.0 [-9.6, +1.7] | +7.9 [+2.8, +13.6] | +4.0 [-3.4, +11.9] |
| settled | uncoded | 180 | 180 | 82.8/80.6 | 15.0/8.9 | 6.1/3.9 | 2.2/9.4 | 0.0/1.1 | -6.1 [-12.8, +0.0] | +7.2 [+1.1, +13.3] | +1.1 [-5.6, +7.8] |
| settled | contested x conservative | 122 | 122 | 64.8/64.8 | 29.5/18.9 | 9.8/5.7 | 5.7/14.8 | 0.0/1.6 | -10.7 [-19.7, -2.5] | +9.0 [+2.5, +15.6] | -1.6 [-9.8, +7.4] |
| settled | contested x liberal | 122 | 122 | 63.9/62.3 | 29.5/19.7 | 2.5/4.1 | 6.6/17.2 | 0.0/0.8 | -9.8 [-18.9, -0.8] | +10.7 [+4.1, +18.0] | +0.8 [-9.0, +9.8] |

#### answer length, mean words, original / treated

- consensus | all: 131 / 29
- contested | all: 231 / 176
- settled | all: 206 / 90
- settled | contested: 211 / 91
- settled | uncontested: 189 / 86
- settled | left-coded: 227 / 99
- settled | right-coded: 199 / 81
- settled | uncoded: 198 / 93
- settled | contested x conservative: 211 / 84
- settled | contested x liberal: 212 / 88

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/88.3 | 0.0/10.0 | 3.3/0.0 | 0.0/1.7 | +0.07/-0.08 |
| liberal | 60 | 91.7/80.0 | 8.3/20.0 | 0.0/0.0 | 0.0/0.0 | -0.15/-0.30 |
| none | 60 | 100.0/86.7 | 0.0/11.7 | 0.0/1.7 | 0.0/0.0 | +0.00/-0.13 |
