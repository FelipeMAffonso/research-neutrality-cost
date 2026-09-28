# Qwen2.5-32B: assertive transform (ShareGPT) against the original, settled and consensus items, version 2

original: <outputs>/qwen2.5-32b/original/judged_main_v2.jsonl

condition assertive_transform: <outputs>/qwen2.5-32b/assertive_transform/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 65.0/65.0 | 10.0/0.0 | 5.0/10.0 | 25.0/35.0 | 0.0/0.0 | -10.0 [-25.0, +0.0] | +10.0 [-10.0, +30.0] | +0.0 [-15.0, +15.0] |
| consensus | variant=none | 20 | 20 | 65.0/65.0 | 10.0/0.0 | 5.0/10.0 | 25.0/35.0 | 0.0/0.0 | -10.0 [-25.0, +0.0] | +10.0 [-10.0, +30.0] | +0.0 [-15.0, +15.0] |
| settled | all | 474 | 474 | 86.7/84.2 | 11.0/10.3 | 22.8/10.1 | 2.3/5.1 | 0.0/0.4 | -0.6 [-4.2, +3.0] | +2.7 [+0.2, +5.5] | +2.1 [-1.9, +6.5] |
| settled | variant=conservative | 158 | 158 | 86.7/83.5 | 10.8/10.8 | 25.3/11.4 | 2.5/5.7 | 0.0/0.0 | +0.0 [-5.7, +5.7] | +3.2 [-0.6, +7.6] | +3.2 [-2.5, +9.5] |
| settled | variant=liberal | 158 | 158 | 88.0/82.9 | 8.9/11.4 | 25.9/9.5 | 3.2/4.4 | 0.0/1.3 | +2.5 [-2.5, +8.2] | +1.3 [-2.5, +5.1] | +3.8 [-2.5, +10.1] |
| settled | variant=none | 158 | 158 | 85.4/86.1 | 13.3/8.9 | 17.1/9.5 | 1.3/5.1 | 0.0/0.0 | -4.4 [-9.5, +0.6] | +3.8 [+0.6, +8.2] | -0.6 [-7.0, +5.7] |
| settled | contested | 366 | 366 | 84.7/81.7 | 14.2/12.8 | 24.3/11.5 | 1.1/4.9 | 0.0/0.5 | -1.4 [-6.0, +3.0] | +3.8 [+1.1, +6.6] | +2.5 [-2.7, +7.7] |
| settled | uncontested | 108 | 108 | 93.5/92.6 | 0.0/1.9 | 17.6/5.6 | 6.5/5.6 | 0.0/0.0 | +1.9 [+0.0, +5.6] | -0.9 [-8.3, +6.5] | +0.9 [-6.5, +9.3] |
| settled | left-coded | 78 | 78 | 70.5/74.4 | 28.2/17.9 | 37.2/24.4 | 1.3/7.7 | 0.0/0.0 | -10.3 [-21.8, -1.3] | +6.4 [+1.3, +12.8] | -3.8 [-15.4, +7.7] |
| settled | right-coded | 177 | 177 | 94.4/90.4 | 4.0/3.4 | 20.3/7.3 | 1.7/5.1 | 0.0/1.1 | -0.6 [-5.1, +3.4] | +3.4 [-1.1, +8.5] | +2.8 [-2.8, +9.0] |
| settled | uncoded | 219 | 219 | 86.3/82.6 | 10.5/13.2 | 19.6/7.3 | 3.2/4.1 | 0.0/0.0 | +2.7 [-2.3, +8.2] | +0.9 [-2.7, +5.0] | +3.7 [-2.7, +11.0] |
| settled | contested x conservative | 122 | 122 | 84.4/81.1 | 13.9/13.1 | 27.0/12.3 | 1.6/5.7 | 0.0/0.0 | -0.8 [-8.2, +6.6] | +4.1 [+0.0, +9.0] | +3.3 [-4.1, +11.5] |
| settled | contested x liberal | 122 | 122 | 86.9/80.3 | 11.5/13.9 | 26.2/12.3 | 1.6/4.1 | 0.0/1.6 | +2.5 [-4.9, +9.0] | +2.5 [-1.6, +6.6] | +4.9 [-3.3, +13.1] |

#### answer length, mean words, original / treated

- consensus | all: 121 / 69
- contested | all: 241 / 154
- settled | all: 162 / 98
- settled | contested: 170 / 104
- settled | uncontested: 136 / 80
- settled | left-coded: 205 / 111
- settled | right-coded: 150 / 89
- settled | uncoded: 157 / 102
- settled | contested x conservative: 177 / 108
- settled | contested x liberal: 161 / 101

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 63.3/73.3 | 0.0/5.0 | 36.7/20.0 | 0.0/1.7 | +0.67/+0.25 |
| liberal | 60 | 76.7/61.7 | 23.3/38.3 | 0.0/0.0 | 0.0/0.0 | -0.28/-0.48 |
| none | 60 | 100.0/81.7 | 0.0/11.7 | 0.0/5.0 | 0.0/1.7 | +0.00/-0.07 |
