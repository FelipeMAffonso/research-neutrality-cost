# Llama-3.1-8B: assertive transform (ShareGPT) against the original, settled and consensus items, version 2

original: <outputs>/llama-3.1-8b/original/judged_main_v2.jsonl

condition assertive_transform: <outputs>/llama-3.1-8b/assertive_transform/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 55.0/55.0 | 0.0/0.0 | 0.0/0.0 | 30.0/35.0 | 15.0/10.0 | +0.0 [+0.0, +0.0] | +5.0 [-10.0, +20.0] | +5.0 [-10.0, +20.0] |
| consensus | variant=none | 20 | 20 | 55.0/55.0 | 0.0/0.0 | 0.0/0.0 | 30.0/35.0 | 15.0/10.0 | +0.0 [+0.0, +0.0] | +5.0 [-10.0, +20.0] | +5.0 [-10.0, +20.0] |
| settled | all | 474 | 474 | 71.7/72.2 | 21.7/11.4 | 4.6/2.7 | 6.1/16.0 | 0.4/0.4 | -10.3 [-14.8, -6.3] | +9.9 [+5.7, +14.3] | -0.4 [-5.3, +4.2] |
| settled | variant=conservative | 158 | 158 | 72.8/68.4 | 21.5/12.0 | 9.5/3.2 | 5.7/19.6 | 0.0/0.0 | -9.5 [-15.8, -3.8] | +13.9 [+8.2, +20.3] | +4.4 [-2.5, +11.4] |
| settled | variant=liberal | 158 | 158 | 70.9/72.8 | 24.7/12.0 | 1.9/2.5 | 4.4/14.6 | 0.0/0.6 | -12.7 [-19.0, -6.3] | +10.1 [+4.4, +15.8] | -2.5 [-9.5, +4.4] |
| settled | variant=none | 158 | 158 | 71.5/75.3 | 19.0/10.1 | 2.5/2.5 | 8.2/13.9 | 1.3/0.6 | -8.9 [-16.5, -1.9] | +5.7 [+0.0, +12.0] | -3.2 [-10.8, +4.4] |
| settled | contested | 366 | 366 | 65.0/66.9 | 26.8/14.2 | 4.4/3.3 | 7.7/18.3 | 0.5/0.5 | -12.6 [-17.8, -7.1] | +10.7 [+5.7, +15.8] | -1.9 [-7.1, +3.8] |
| settled | uncontested | 108 | 108 | 94.4/89.8 | 4.6/1.9 | 5.6/0.9 | 0.9/8.3 | 0.0/0.0 | -2.8 [-8.3, +2.8] | +7.4 [+0.0, +15.7] | +4.6 [-3.7, +14.8] |
| settled | left-coded | 78 | 78 | 44.9/51.3 | 41.0/26.9 | 7.7/9.0 | 12.8/20.5 | 1.3/1.3 | -14.1 [-28.2, -1.3] | +7.7 [-5.1, +21.8] | -6.4 [-20.5, +7.7] |
| settled | right-coded | 177 | 177 | 81.4/80.8 | 12.4/6.8 | 4.5/0.6 | 5.6/11.9 | 0.6/0.6 | -5.6 [-11.3, -0.6] | +6.2 [+0.6, +11.9] | +0.6 [-6.8, +7.3] |
| settled | uncoded | 219 | 219 | 73.5/72.6 | 22.4/9.6 | 3.7/2.3 | 4.1/17.8 | 0.0/0.0 | -12.8 [-20.1, -5.9] | +13.7 [+7.8, +20.5] | +0.9 [-5.9, +8.2] |
| settled | contested x conservative | 122 | 122 | 66.4/61.5 | 26.2/15.6 | 9.8/3.3 | 7.4/23.0 | 0.0/0.0 | -10.7 [-18.0, -4.1] | +15.6 [+9.0, +23.0] | +4.9 [-3.3, +13.9] |
| settled | contested x liberal | 122 | 122 | 63.9/69.7 | 30.3/14.8 | 1.6/3.3 | 5.7/14.8 | 0.0/0.8 | -15.6 [-23.8, -8.2] | +9.0 [+2.5, +15.6] | -6.6 [-13.9, +1.6] |

#### answer length, mean words, original / treated

- consensus | all: 118 / 37
- contested | all: 231 / 166
- settled | all: 205 / 83
- settled | contested: 209 / 85
- settled | uncontested: 189 / 78
- settled | left-coded: 228 / 107
- settled | right-coded: 197 / 76
- settled | uncoded: 203 / 81
- settled | contested x conservative: 210 / 76
- settled | contested x liberal: 210 / 82

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/78.3 | 0.0/15.0 | 3.3/3.3 | 0.0/3.3 | +0.07/-0.12 |
| liberal | 60 | 91.7/73.3 | 8.3/25.0 | 0.0/0.0 | 0.0/1.7 | -0.15/-0.37 |
| none | 60 | 100.0/83.3 | 0.0/13.3 | 0.0/1.7 | 0.0/1.7 | +0.00/-0.13 |
