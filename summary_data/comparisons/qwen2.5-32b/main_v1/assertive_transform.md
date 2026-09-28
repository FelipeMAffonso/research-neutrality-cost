# Qwen2.5-32B: assertive transform (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/qwen2.5-32b/original/judged_main_v1.jsonl

condition assertive_transform: <outputs>/qwen2.5-32b/assertive_transform/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 65.0/55.0 | 15.0/5.0 | 0.0/5.0 | 20.0/40.0 | 0.0/0.0 | -10.0 [-30.0, +10.0] | +20.0 [+5.0, +40.0] | +10.0 [+0.0, +25.0] |
| consensus | variant=none | 20 | 20 | 65.0/55.0 | 15.0/5.0 | 0.0/5.0 | 20.0/40.0 | 0.0/0.0 | -10.0 [-30.0, +10.0] | +20.0 [+5.0, +40.0] | +10.0 [+0.0, +25.0] |
| settled | all | 474 | 474 | 86.7/84.2 | 11.4/11.6 | 20.7/11.4 | 1.9/4.0 | 0.0/0.2 | +0.2 [-3.8, +4.4] | +2.1 [-0.2, +4.9] | +2.3 [-1.9, +6.8] |
| settled | variant=conservative | 158 | 158 | 86.1/82.3 | 12.0/13.3 | 27.8/12.0 | 1.9/3.8 | 0.0/0.6 | +1.3 [-4.4, +7.6] | +1.9 [-1.9, +5.7] | +3.2 [-3.2, +10.1] |
| settled | variant=liberal | 158 | 158 | 88.6/84.8 | 8.9/10.1 | 24.7/11.4 | 2.5/5.1 | 0.0/0.0 | +1.3 [-3.8, +7.0] | +2.5 [-0.6, +6.3] | +3.8 [-2.5, +10.1] |
| settled | variant=none | 158 | 158 | 85.4/85.4 | 13.3/11.4 | 9.5/10.8 | 1.3/3.2 | 0.0/0.0 | -1.9 [-7.6, +3.2] | +1.9 [-1.3, +5.1] | +0.0 [-5.7, +5.1] |
| settled | contested | 366 | 366 | 84.4/81.7 | 14.8/13.9 | 22.7/12.6 | 0.8/4.1 | 0.0/0.3 | -0.8 [-5.7, +4.1] | +3.3 [+0.8, +6.0] | +2.5 [-2.5, +7.7] |
| settled | uncontested | 108 | 108 | 94.4/92.6 | 0.0/3.7 | 13.9/7.4 | 5.6/3.7 | 0.0/0.0 | +3.7 [+0.0, +8.3] | -1.9 [-7.4, +4.6] | +1.9 [-4.6, +10.2] |
| settled | left-coded | 117 | 117 | 69.2/66.7 | 29.9/24.8 | 29.9/21.4 | 0.9/8.5 | 0.0/0.0 | -5.1 [-17.1, +6.0] | +7.7 [+2.6, +14.5] | +2.6 [-6.8, +12.8] |
| settled | right-coded | 177 | 177 | 93.2/91.0 | 5.6/6.2 | 18.1/9.0 | 1.1/2.3 | 0.0/0.6 | +0.6 [-4.5, +6.2] | +1.1 [-1.7, +4.5] | +1.7 [-4.5, +7.9] |
| settled | uncoded | 180 | 180 | 91.7/88.9 | 5.0/8.3 | 17.2/7.2 | 3.3/2.8 | 0.0/0.0 | +3.3 [-1.7, +8.3] | -0.6 [-4.4, +3.3] | +2.8 [-3.9, +9.4] |
| settled | contested x conservative | 122 | 122 | 82.8/79.5 | 15.6/15.6 | 29.5/12.3 | 1.6/4.1 | 0.0/0.8 | +0.0 [-7.4, +7.4] | +2.5 [-1.6, +6.6] | +2.5 [-5.7, +10.7] |
| settled | contested x liberal | 122 | 122 | 87.7/82.8 | 11.5/12.3 | 27.0/13.1 | 0.8/4.9 | 0.0/0.0 | +0.8 [-6.6, +8.2] | +4.1 [+0.8, +8.2] | +4.9 [-2.5, +12.3] |

#### answer length, mean words, original / treated

- consensus | all: 127 / 64
- contested | all: 240 / 159
- settled | all: 162 / 96
- settled | contested: 170 / 103
- settled | uncontested: 135 / 74
- settled | left-coded: 204 / 119
- settled | right-coded: 150 / 90
- settled | uncoded: 147 / 88
- settled | contested x conservative: 177 / 103
- settled | contested x liberal: 160 / 104

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 61.7/71.7 | 0.0/5.0 | 38.3/23.3 | 0.0/0.0 | +0.70/+0.32 |
| liberal | 60 | 76.7/66.7 | 23.3/33.3 | 0.0/0.0 | 0.0/0.0 | -0.27/-0.42 |
| none | 60 | 100.0/83.3 | 0.0/11.7 | 0.0/3.3 | 0.0/1.7 | +0.00/-0.12 |
