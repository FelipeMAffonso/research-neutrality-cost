# Qwen2.5-32B: untransformed (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/qwen2.5-32b/original/judged_main_v1.jsonl

condition untransformed: <outputs>/qwen2.5-32b/untransformed/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 65.0/65.0 | 15.0/5.0 | 0.0/5.0 | 20.0/30.0 | 0.0/0.0 | -10.0 [-30.0, +10.0] | +10.0 [-10.0, +30.0] | +0.0 [-15.0, +15.0] |
| consensus | variant=none | 20 | 20 | 65.0/65.0 | 15.0/5.0 | 0.0/5.0 | 20.0/30.0 | 0.0/0.0 | -10.0 [-30.0, +10.0] | +10.0 [-10.0, +30.0] | +0.0 [-15.0, +15.0] |
| settled | all | 474 | 474 | 86.7/86.9 | 11.4/11.6 | 20.7/19.6 | 1.9/1.5 | 0.0/0.0 | +0.2 [-3.4, +3.8] | -0.4 [-2.3, +1.3] | -0.2 [-4.4, +4.0] |
| settled | variant=conservative | 158 | 158 | 86.1/86.7 | 12.0/12.7 | 27.8/22.8 | 1.9/0.6 | 0.0/0.0 | +0.6 [-5.1, +6.3] | -1.3 [-3.8, +1.3] | -0.6 [-7.0, +5.1] |
| settled | variant=liberal | 158 | 158 | 88.6/86.1 | 8.9/10.8 | 24.7/19.6 | 2.5/3.2 | 0.0/0.0 | +1.9 [-3.2, +7.0] | +0.6 [-2.5, +3.8] | +2.5 [-3.2, +8.9] |
| settled | variant=none | 158 | 158 | 85.4/88.0 | 13.3/11.4 | 9.5/16.5 | 1.3/0.6 | 0.0/0.0 | -1.9 [-7.0, +2.5] | -0.6 [-3.2, +1.3] | -2.5 [-8.2, +2.5] |
| settled | contested | 366 | 366 | 84.4/84.4 | 14.8/14.2 | 22.7/22.4 | 0.8/1.4 | 0.0/0.0 | -0.5 [-4.9, +3.8] | +0.5 [-0.8, +1.9] | +0.0 [-4.6, +4.6] |
| settled | uncontested | 108 | 108 | 94.4/95.4 | 0.0/2.8 | 13.9/10.2 | 5.6/1.9 | 0.0/0.0 | +2.8 [+0.0, +7.4] | -3.7 [-10.2, +1.9] | -0.9 [-9.3, +7.4] |
| settled | left-coded | 117 | 117 | 69.2/71.8 | 29.9/25.6 | 29.9/31.6 | 0.9/2.6 | 0.0/0.0 | -4.3 [-14.5, +6.0] | +1.7 [+0.0, +4.3] | -2.6 [-12.8, +8.5] |
| settled | right-coded | 177 | 177 | 93.2/92.1 | 5.6/6.8 | 18.1/15.8 | 1.1/1.1 | 0.0/0.0 | +1.1 [-4.0, +6.2] | +0.0 [-2.3, +2.3] | +1.1 [-4.5, +6.8] |
| settled | uncoded | 180 | 180 | 91.7/91.7 | 5.0/7.2 | 17.2/15.6 | 3.3/1.1 | 0.0/0.0 | +2.2 [-1.7, +6.1] | -2.2 [-6.1, +1.1] | +0.0 [-6.1, +6.7] |
| settled | contested x conservative | 122 | 122 | 82.8/84.4 | 15.6/14.8 | 29.5/25.4 | 1.6/0.8 | 0.0/0.0 | -0.8 [-8.2, +5.7] | -0.8 [-3.3, +1.6] | -1.6 [-9.0, +4.9] |
| settled | contested x liberal | 122 | 122 | 87.7/83.6 | 11.5/13.1 | 27.0/23.0 | 0.8/3.3 | 0.0/0.0 | +1.6 [-4.9, +8.2] | +2.5 [+0.0, +5.7] | +4.1 [-3.3, +11.5] |

#### answer length, mean words, original / treated

- consensus | all: 127 / 78
- contested | all: 240 / 184
- settled | all: 162 / 134
- settled | contested: 170 / 139
- settled | uncontested: 135 / 114
- settled | left-coded: 204 / 161
- settled | right-coded: 150 / 124
- settled | uncoded: 147 / 126
- settled | contested x conservative: 177 / 140
- settled | contested x liberal: 160 / 133

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 61.7/73.3 | 0.0/6.7 | 38.3/20.0 | 0.0/0.0 | +0.70/+0.25 |
| liberal | 60 | 76.7/70.0 | 23.3/28.3 | 0.0/1.7 | 0.0/0.0 | -0.27/-0.28 |
| none | 60 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 | 0.0/0.0 | +0.00/-0.13 |
