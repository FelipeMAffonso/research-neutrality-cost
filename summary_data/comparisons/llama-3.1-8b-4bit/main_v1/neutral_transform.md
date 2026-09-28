# Llama-3.1-8B, preliminary 4-bit run: neutral transform (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/llama-3.1-8b-4bit/original/judged_main_v1.jsonl

condition neutral_transform: <outputs>/llama-3.1-8b-4bit/neutral_transform/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 60.0/50.0 | 0.0/0.0 | 0.0/0.0 | 35.0/45.0 | 5.0/5.0 | +0.0 [+0.0, +0.0] | +10.0 [-15.0, +35.0] | +10.0 [-15.0, +35.0] |
| consensus | variant=none | 20 | 20 | 60.0/50.0 | 0.0/0.0 | 0.0/0.0 | 35.0/45.0 | 5.0/5.0 | +0.0 [+0.0, +0.0] | +10.0 [-15.0, +35.0] | +10.0 [-15.0, +35.0] |
| settled | all | 474 | 474 | 73.0/71.9 | 21.3/18.6 | 5.9/5.5 | 5.1/8.4 | 0.6/1.1 | -2.7 [-6.5, +1.1] | +3.4 [+0.2, +6.5] | +0.6 [-4.0, +5.1] |
| settled | variant=conservative | 158 | 158 | 71.5/69.6 | 22.8/19.0 | 7.6/8.2 | 4.4/9.5 | 1.3/1.9 | -3.8 [-10.1, +3.2] | +5.1 [+0.0, +10.1] | +1.3 [-5.7, +8.9] |
| settled | variant=liberal | 158 | 158 | 73.4/69.6 | 22.8/20.9 | 5.7/3.8 | 3.2/8.2 | 0.6/1.3 | -1.9 [-8.2, +4.4] | +5.1 [+0.0, +10.1] | +3.2 [-3.8, +10.1] |
| settled | variant=none | 158 | 158 | 74.1/76.6 | 18.4/15.8 | 4.4/4.4 | 7.6/7.6 | 0.0/0.0 | -2.5 [-7.6, +2.5] | +0.0 [-4.4, +4.4] | -2.5 [-8.9, +3.8] |
| settled | contested | 366 | 366 | 66.7/66.4 | 27.3/23.0 | 6.3/6.0 | 5.5/9.3 | 0.5/1.4 | -4.4 [-9.0, +0.0] | +3.8 [+0.3, +7.4] | -0.5 [-5.7, +4.6] |
| settled | uncontested | 108 | 108 | 94.4/90.7 | 0.9/3.7 | 4.6/3.7 | 3.7/5.6 | 0.9/0.0 | +2.8 [-0.9, +6.5] | +1.9 [-5.6, +8.3] | +4.6 [-3.7, +12.0] |
| settled | left-coded | 117 | 117 | 45.3/45.3 | 44.4/41.9 | 10.3/12.0 | 9.4/10.3 | 0.9/2.6 | -2.6 [-12.8, +6.8] | +0.9 [-6.8, +9.4] | -1.7 [-13.7, +10.3] |
| settled | right-coded | 177 | 177 | 80.2/78.0 | 15.3/9.6 | 2.8/2.8 | 4.0/11.9 | 0.6/0.6 | -5.6 [-11.9, +0.6] | +7.9 [+2.8, +13.6] | +2.3 [-4.5, +9.0] |
| settled | uncoded | 180 | 180 | 83.9/83.3 | 12.2/12.2 | 6.1/3.9 | 3.3/3.9 | 0.6/0.6 | +0.0 [-5.0, +4.4] | +0.6 [-4.4, +5.0] | +0.6 [-6.1, +6.7] |
| settled | contested x conservative | 122 | 122 | 65.6/63.1 | 29.5/23.0 | 7.4/8.2 | 4.1/11.5 | 0.8/2.5 | -6.6 [-14.8, +1.6] | +7.4 [+1.6, +13.9] | +0.8 [-8.2, +10.7] |
| settled | contested x liberal | 122 | 122 | 67.2/63.9 | 28.7/26.2 | 6.6/4.1 | 3.3/8.2 | 0.8/1.6 | -2.5 [-9.8, +5.7] | +4.9 [-0.8, +10.7] | +2.5 [-5.7, +10.7] |

#### answer length, mean words, original / treated

- consensus | all: 96 / 48
- contested | all: 234 / 190
- settled | all: 203 / 123
- settled | contested: 208 / 131
- settled | uncontested: 185 / 93
- settled | left-coded: 228 / 146
- settled | right-coded: 193 / 124
- settled | uncoded: 196 / 106
- settled | contested x conservative: 214 / 134
- settled | contested x liberal: 205 / 121

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 91.7/80.0 | 0.0/6.7 | 8.3/8.3 | 0.0/5.0 | +0.18/+0.07 |
| liberal | 60 | 85.0/78.3 | 15.0/16.7 | 0.0/0.0 | 0.0/5.0 | -0.23/-0.20 |
| none | 60 | 95.0/93.3 | 5.0/5.0 | 0.0/1.7 | 0.0/0.0 | -0.07/-0.02 |
