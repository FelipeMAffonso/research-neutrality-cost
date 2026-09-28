# Llama-3.1-8B: untransformed (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/llama-3.1-8b/original/judged_main_v1.jsonl

condition untransformed: <outputs>/llama-3.1-8b/untransformed/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 45.0/55.0 | 10.0/0.0 | 0.0/0.0 | 40.0/35.0 | 5.0/10.0 | -10.0 [-25.0, +0.0] | -5.0 [-25.0, +15.0] | -15.0 [-35.0, +5.0] |
| consensus | variant=none | 20 | 20 | 45.0/55.0 | 10.0/0.0 | 0.0/0.0 | 40.0/35.0 | 5.0/10.0 | -10.0 [-25.0, +0.0] | -5.0 [-25.0, +15.0] | -15.0 [-35.0, +5.0] |
| settled | all | 474 | 474 | 71.9/70.7 | 22.2/16.0 | 5.1/4.2 | 5.7/13.1 | 0.2/0.2 | -6.1 [-11.0, -1.5] | +7.4 [+3.4, +11.6] | +1.3 [-4.0, +6.8] |
| settled | variant=conservative | 158 | 158 | 71.5/67.7 | 24.1/17.1 | 10.1/2.5 | 4.4/14.6 | 0.0/0.6 | -7.0 [-14.6, +0.6] | +10.1 [+4.4, +15.8] | +3.2 [-5.1, +11.4] |
| settled | variant=liberal | 158 | 158 | 70.9/69.6 | 24.1/15.8 | 2.5/7.6 | 5.1/14.6 | 0.0/0.0 | -8.2 [-15.2, -1.3] | +9.5 [+3.8, +15.2] | +1.3 [-5.7, +8.2] |
| settled | variant=none | 158 | 158 | 73.4/74.7 | 18.4/15.2 | 2.5/2.5 | 7.6/10.1 | 0.6/0.0 | -3.2 [-9.5, +3.2] | +2.5 [-2.5, +7.6] | -0.6 [-7.6, +6.3] |
| settled | contested | 366 | 366 | 65.3/64.5 | 27.3/20.2 | 4.6/4.6 | 7.1/15.0 | 0.3/0.3 | -7.1 [-13.4, -1.1] | +7.9 [+3.0, +12.8] | +0.8 [-6.0, +7.4] |
| settled | uncontested | 108 | 108 | 94.4/91.7 | 4.6/1.9 | 6.5/2.8 | 0.9/6.5 | 0.0/0.0 | -2.8 [-8.3, +0.9] | +5.6 [-0.9, +13.9] | +2.8 [-5.6, +11.1] |
| settled | left-coded | 117 | 117 | 35.9/43.6 | 48.7/33.3 | 5.1/10.3 | 15.4/23.1 | 0.0/0.0 | -15.4 [-28.2, -3.4] | +7.7 [-2.6, +18.8] | -7.7 [-21.4, +6.0] |
| settled | right-coded | 177 | 177 | 84.7/75.1 | 11.9/12.4 | 4.0/1.7 | 2.8/11.9 | 0.6/0.6 | +0.6 [-6.2, +7.3] | +9.0 [+4.5, +14.7] | +9.6 [+1.7, +17.5] |
| settled | uncoded | 180 | 180 | 82.8/83.9 | 15.0/8.3 | 6.1/2.8 | 2.2/7.8 | 0.0/0.0 | -6.7 [-12.8, -1.7] | +5.6 [-0.6, +12.2] | -1.1 [-8.3, +6.1] |
| settled | contested x conservative | 122 | 122 | 64.8/61.5 | 29.5/21.3 | 9.8/3.3 | 5.7/16.4 | 0.0/0.8 | -8.2 [-18.0, +1.6] | +10.7 [+4.1, +17.2] | +2.5 [-7.4, +12.3] |
| settled | contested x liberal | 122 | 122 | 63.9/63.1 | 29.5/20.5 | 2.5/7.4 | 6.6/16.4 | 0.0/0.0 | -9.0 [-18.0, +0.0] | +9.8 [+2.5, +16.4] | +0.8 [-8.2, +9.8] |

#### answer length, mean words, original / treated

- consensus | all: 131 / 51
- contested | all: 231 / 188
- settled | all: 206 / 120
- settled | contested: 211 / 125
- settled | uncontested: 189 / 101
- settled | left-coded: 227 / 132
- settled | right-coded: 199 / 115
- settled | uncoded: 198 / 117
- settled | contested x conservative: 211 / 118
- settled | contested x liberal: 212 / 120

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/83.3 | 0.0/8.3 | 3.3/5.0 | 0.0/3.3 | +0.07/-0.02 |
| liberal | 60 | 91.7/75.0 | 8.3/21.7 | 0.0/0.0 | 0.0/3.3 | -0.15/-0.37 |
| none | 60 | 100.0/86.7 | 0.0/11.7 | 0.0/1.7 | 0.0/0.0 | +0.00/-0.13 |
