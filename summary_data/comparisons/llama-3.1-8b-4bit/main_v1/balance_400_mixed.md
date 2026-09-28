# Llama-3.1-8B, preliminary 4-bit run: mixed condition (400 balanced answers within the ShareGPT sample) against the original, settled and consensus items, version 1

original: <outputs>/llama-3.1-8b-4bit/original/judged_main_v1.jsonl

condition balance_400_mixed: <outputs>/llama-3.1-8b-4bit/balance_400_mixed/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mixed condition (400 balanced answers within the ShareGPT sample)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 60.0/50.0 | 0.0/0.0 | 0.0/0.0 | 35.0/45.0 | 5.0/5.0 | +0.0 [+0.0, +0.0] | +10.0 [-10.0, +30.0] | +10.0 [-10.0, +30.0] |
| consensus | variant=none | 20 | 20 | 60.0/50.0 | 0.0/0.0 | 0.0/0.0 | 35.0/45.0 | 5.0/5.0 | +0.0 [+0.0, +0.0] | +10.0 [-10.0, +30.0] | +10.0 [-10.0, +30.0] |
| settled | all | 474 | 474 | 73.0/71.5 | 21.3/15.6 | 5.9/4.6 | 5.1/10.5 | 0.6/2.3 | -5.7 [-10.3, -1.1] | +5.5 [+2.5, +8.6] | -0.2 [-5.5, +5.1] |
| settled | variant=conservative | 158 | 158 | 71.5/69.6 | 22.8/12.7 | 7.6/8.2 | 4.4/13.3 | 1.3/4.4 | -10.1 [-17.7, -2.5] | +8.9 [+3.8, +14.6] | -1.3 [-9.5, +7.0] |
| settled | variant=liberal | 158 | 158 | 73.4/72.2 | 22.8/19.0 | 5.7/3.2 | 3.2/7.6 | 0.6/1.3 | -3.8 [-10.8, +3.2] | +4.4 [+0.0, +8.9] | +0.6 [-7.0, +7.6] |
| settled | variant=none | 158 | 158 | 74.1/72.8 | 18.4/15.2 | 4.4/2.5 | 7.6/10.8 | 0.0/1.3 | -3.2 [-8.9, +3.2] | +3.2 [-1.9, +8.2] | +0.0 [-7.0, +7.0] |
| settled | contested | 366 | 366 | 66.7/66.1 | 27.3/19.7 | 6.3/6.0 | 5.5/11.5 | 0.5/2.7 | -7.7 [-13.1, -1.9] | +6.0 [+2.5, +9.8] | -1.6 [-7.7, +4.6] |
| settled | uncontested | 108 | 108 | 94.4/89.8 | 0.9/1.9 | 4.6/0.0 | 3.7/7.4 | 0.9/0.9 | +0.9 [+0.0, +2.8] | +3.7 [-1.9, +9.3] | +4.6 [-0.9, +10.2] |
| settled | left-coded | 117 | 117 | 45.3/42.7 | 44.4/37.6 | 10.3/9.4 | 9.4/15.4 | 0.9/4.3 | -6.8 [-19.7, +6.0] | +6.0 [+0.0, +12.8] | -0.9 [-15.4, +13.7] |
| settled | right-coded | 177 | 177 | 80.2/80.2 | 15.3/6.2 | 2.8/4.5 | 4.0/11.3 | 0.6/2.3 | -9.0 [-16.4, -2.3] | +7.3 [+1.7, +13.0] | -1.7 [-9.6, +5.6] |
| settled | uncoded | 180 | 180 | 83.9/81.7 | 12.2/10.6 | 6.1/1.7 | 3.3/6.7 | 0.6/1.1 | -1.7 [-5.6, +2.2] | +3.3 [-1.1, +7.8] | +1.7 [-2.8, +6.1] |
| settled | contested x conservative | 122 | 122 | 65.6/65.6 | 29.5/15.6 | 7.4/10.7 | 4.1/13.9 | 0.8/4.9 | -13.9 [-23.0, -4.1] | +9.8 [+4.1, +16.4] | -4.1 [-13.9, +6.6] |
| settled | contested x liberal | 122 | 122 | 67.2/65.6 | 28.7/23.8 | 6.6/4.1 | 3.3/9.0 | 0.8/1.6 | -4.9 [-13.9, +4.1] | +5.7 [+0.0, +11.5] | +0.8 [-9.0, +10.7] |

#### answer length, mean words, original / treated

- consensus | all: 96 / 47
- contested | all: 234 / 183
- settled | all: 203 / 113
- settled | contested: 208 / 119
- settled | uncontested: 185 / 93
- settled | left-coded: 228 / 148
- settled | right-coded: 193 / 97
- settled | uncoded: 196 / 107
- settled | contested x conservative: 214 / 108
- settled | contested x liberal: 205 / 123

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 91.7/75.0 | 0.0/6.7 | 8.3/10.0 | 0.0/8.3 | +0.18/+0.12 |
| liberal | 60 | 85.0/83.3 | 15.0/15.0 | 0.0/0.0 | 0.0/1.7 | -0.23/-0.18 |
| none | 60 | 95.0/86.7 | 5.0/10.0 | 0.0/1.7 | 0.0/1.7 | -0.07/-0.07 |
