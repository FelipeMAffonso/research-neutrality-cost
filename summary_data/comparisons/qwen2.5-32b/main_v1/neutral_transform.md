# Qwen2.5-32B: neutral transform (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/qwen2.5-32b/original/judged_main_v1.jsonl

condition neutral_transform: <outputs>/qwen2.5-32b/neutral_transform/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 65.0/65.0 | 15.0/5.0 | 0.0/0.0 | 20.0/25.0 | 0.0/5.0 | -10.0 [-30.0, +10.0] | +5.0 [-10.0, +20.0] | -5.0 [-25.0, +10.0] |
| consensus | variant=none | 20 | 20 | 65.0/65.0 | 15.0/5.0 | 0.0/0.0 | 20.0/25.0 | 0.0/5.0 | -10.0 [-30.0, +10.0] | +5.0 [-10.0, +20.0] | -5.0 [-25.0, +10.0] |
| settled | all | 474 | 474 | 86.7/81.9 | 11.4/14.6 | 20.7/10.5 | 1.9/3.6 | 0.0/0.0 | +3.2 [+0.0, +6.5] | +1.7 [-0.6, +4.2] | +4.9 [+1.5, +8.6] |
| settled | variant=conservative | 158 | 158 | 86.1/77.2 | 12.0/17.1 | 27.8/8.9 | 1.9/5.7 | 0.0/0.0 | +5.1 [-0.6, +11.4] | +3.8 [+0.0, +7.6] | +8.9 [+3.2, +14.6] |
| settled | variant=liberal | 158 | 158 | 88.6/83.5 | 8.9/13.3 | 24.7/14.6 | 2.5/3.2 | 0.0/0.0 | +4.4 [-0.6, +9.5] | +0.6 [-2.5, +3.8] | +5.1 [-0.6, +10.8] |
| settled | variant=none | 158 | 158 | 85.4/84.8 | 13.3/13.3 | 9.5/8.2 | 1.3/1.9 | 0.0/0.0 | +0.0 [-3.8, +3.8] | +0.6 [-1.9, +3.8] | +0.6 [-3.8, +5.1] |
| settled | contested | 366 | 366 | 84.4/77.9 | 14.8/18.3 | 22.7/12.0 | 0.8/3.8 | 0.0/0.0 | +3.6 [-0.8, +7.9] | +3.0 [+0.5, +6.0] | +6.6 [+2.2, +10.7] |
| settled | uncontested | 108 | 108 | 94.4/95.4 | 0.0/1.9 | 13.9/5.6 | 5.6/2.8 | 0.0/0.0 | +1.9 [+0.0, +4.6] | -2.8 [-8.3, +0.9] | -0.9 [-6.5, +4.6] |
| settled | left-coded | 117 | 117 | 69.2/63.2 | 29.9/27.4 | 29.9/13.7 | 0.9/9.4 | 0.0/0.0 | -2.6 [-12.0, +6.8] | +8.5 [+2.6, +15.4] | +6.0 [-3.4, +15.4] |
| settled | right-coded | 177 | 177 | 93.2/87.0 | 5.6/11.3 | 18.1/10.7 | 1.1/1.7 | 0.0/0.0 | +5.6 [+0.6, +10.7] | +0.6 [-2.3, +4.0] | +6.2 [+1.1, +11.9] |
| settled | uncoded | 180 | 180 | 91.7/88.9 | 5.0/9.4 | 17.2/8.3 | 3.3/1.7 | 0.0/0.0 | +4.4 [+1.1, +8.3] | -1.7 [-4.4, +1.1] | +2.8 [-1.7, +7.8] |
| settled | contested x conservative | 122 | 122 | 82.8/73.0 | 15.6/20.5 | 29.5/9.8 | 1.6/6.6 | 0.0/0.0 | +4.9 [-2.5, +12.3] | +4.9 [+0.0, +10.7] | +9.8 [+3.3, +16.4] |
| settled | contested x liberal | 122 | 122 | 87.7/79.5 | 11.5/17.2 | 27.0/17.2 | 0.8/3.3 | 0.0/0.0 | +5.7 [-0.8, +13.1] | +2.5 [+0.0, +5.7] | +8.2 [+0.8, +15.6] |

#### answer length, mean words, original / treated

- consensus | all: 127 / 80
- contested | all: 240 / 190
- settled | all: 162 / 132
- settled | contested: 170 / 138
- settled | uncontested: 135 / 110
- settled | left-coded: 204 / 154
- settled | right-coded: 150 / 124
- settled | uncoded: 147 / 125
- settled | contested x conservative: 177 / 141
- settled | contested x liberal: 160 / 135

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 61.7/75.0 | 0.0/3.3 | 38.3/21.7 | 0.0/0.0 | +0.70/+0.37 |
| liberal | 60 | 76.7/81.7 | 23.3/18.3 | 0.0/0.0 | 0.0/0.0 | -0.27/-0.23 |
| none | 60 | 100.0/90.0 | 0.0/6.7 | 0.0/3.3 | 0.0/0.0 | +0.00/-0.02 |
