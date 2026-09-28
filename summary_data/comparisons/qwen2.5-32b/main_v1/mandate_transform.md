# Qwen2.5-32B: mandate transform (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/qwen2.5-32b/original/judged_main_v1.jsonl

condition mandate_transform: <outputs>/qwen2.5-32b/mandate_transform/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 65.0/65.0 | 15.0/5.0 | 0.0/10.0 | 20.0/30.0 | 0.0/0.0 | -10.0 [-30.0, +10.0] | +10.0 [-10.0, +30.0] | +0.0 [-15.0, +15.0] |
| consensus | variant=none | 20 | 20 | 65.0/65.0 | 15.0/5.0 | 0.0/10.0 | 20.0/30.0 | 0.0/0.0 | -10.0 [-30.0, +10.0] | +10.0 [-10.0, +30.0] | +0.0 [-15.0, +15.0] |
| settled | all | 474 | 474 | 86.7/85.2 | 11.4/9.9 | 20.7/12.0 | 1.9/4.9 | 0.0/0.0 | -1.5 [-5.5, +2.3] | +3.0 [+0.4, +5.7] | +1.5 [-3.0, +6.1] |
| settled | variant=conservative | 158 | 158 | 86.1/80.4 | 12.0/14.6 | 27.8/10.8 | 1.9/5.1 | 0.0/0.0 | +2.5 [-3.8, +8.9] | +3.2 [-0.6, +7.6] | +5.7 [-1.3, +12.7] |
| settled | variant=liberal | 158 | 158 | 88.6/84.8 | 8.9/8.2 | 24.7/13.9 | 2.5/7.0 | 0.0/0.0 | -0.6 [-5.7, +4.4] | +4.4 [+0.0, +8.9] | +3.8 [-2.5, +10.1] |
| settled | variant=none | 158 | 158 | 85.4/90.5 | 13.3/7.0 | 9.5/11.4 | 1.3/2.5 | 0.0/0.0 | -6.3 [-11.4, -1.3] | +1.3 [-1.9, +4.4] | -5.1 [-10.8, +0.0] |
| settled | contested | 366 | 366 | 84.4/82.0 | 14.8/12.8 | 22.7/13.7 | 0.8/5.2 | 0.0/0.0 | -1.9 [-6.8, +2.7] | +4.4 [+1.9, +7.1] | +2.5 [-3.0, +7.9] |
| settled | uncontested | 108 | 108 | 94.4/96.3 | 0.0/0.0 | 13.9/6.5 | 5.6/3.7 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -1.9 [-8.3, +4.6] | -1.9 [-8.3, +4.6] |
| settled | left-coded | 117 | 117 | 69.2/70.1 | 29.9/23.1 | 29.9/20.5 | 0.9/6.8 | 0.0/0.0 | -6.8 [-16.2, +2.6] | +6.0 [+1.7, +11.1] | -0.9 [-9.4, +8.5] |
| settled | right-coded | 177 | 177 | 93.2/88.1 | 5.6/7.9 | 18.1/7.9 | 1.1/4.0 | 0.0/0.0 | +2.3 [-4.0, +9.0] | +2.8 [-0.6, +6.8] | +5.1 [-2.3, +13.0] |
| settled | uncoded | 180 | 180 | 91.7/92.2 | 5.0/3.3 | 17.2/10.6 | 3.3/4.4 | 0.0/0.0 | -1.7 [-6.7, +2.2] | +1.1 [-4.4, +6.7] | -0.6 [-7.2, +6.1] |
| settled | contested x conservative | 122 | 122 | 82.8/76.2 | 15.6/18.9 | 29.5/10.7 | 1.6/4.9 | 0.0/0.0 | +3.3 [-4.9, +11.5] | +3.3 [-0.8, +8.2] | +6.6 [-1.6, +14.8] |
| settled | contested x liberal | 122 | 122 | 87.7/82.0 | 11.5/10.7 | 27.0/17.2 | 0.8/7.4 | 0.0/0.0 | -0.8 [-6.6, +4.9] | +6.6 [+2.5, +10.7] | +5.7 [-1.6, +13.1] |

#### answer length, mean words, original / treated

- consensus | all: 127 / 76
- contested | all: 240 / 154
- settled | all: 162 / 99
- settled | contested: 170 / 105
- settled | uncontested: 135 / 80
- settled | left-coded: 204 / 128
- settled | right-coded: 150 / 91
- settled | uncoded: 147 / 90
- settled | contested x conservative: 177 / 114
- settled | contested x liberal: 160 / 97

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 61.7/61.7 | 0.0/10.0 | 38.3/28.3 | 0.0/0.0 | +0.70/+0.37 |
| liberal | 60 | 76.7/55.0 | 23.3/45.0 | 0.0/0.0 | 0.0/0.0 | -0.27/-0.52 |
| none | 60 | 100.0/85.0 | 0.0/11.7 | 0.0/1.7 | 0.0/1.7 | +0.00/-0.15 |
