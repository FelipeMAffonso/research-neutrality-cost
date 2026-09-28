# Qwen2.5-32B: mandate transform (ShareGPT) against the original, settled and consensus items, version 2

original: <outputs>/qwen2.5-32b/original/judged_main_v2.jsonl

condition mandate_transform: <outputs>/qwen2.5-32b/mandate_transform/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 65.0/55.0 | 10.0/0.0 | 5.0/0.0 | 25.0/40.0 | 0.0/5.0 | -10.0 [-25.0, +0.0] | +15.0 [-5.0, +35.0] | +5.0 [-10.0, +25.0] |
| consensus | variant=none | 20 | 20 | 65.0/55.0 | 10.0/0.0 | 5.0/0.0 | 25.0/40.0 | 0.0/5.0 | -10.0 [-25.0, +0.0] | +15.0 [-5.0, +35.0] | +5.0 [-10.0, +25.0] |
| settled | all | 474 | 474 | 86.7/88.4 | 11.0/8.4 | 22.8/12.7 | 2.3/3.2 | 0.0/0.0 | -2.5 [-5.9, +0.6] | +0.8 [-1.3, +3.0] | -1.7 [-5.7, +2.1] |
| settled | variant=conservative | 158 | 158 | 86.7/87.3 | 10.8/9.5 | 25.3/12.7 | 2.5/3.2 | 0.0/0.0 | -1.3 [-7.0, +3.8] | +0.6 [-3.2, +4.4] | -0.6 [-7.0, +5.7] |
| settled | variant=liberal | 158 | 158 | 88.0/88.6 | 8.9/8.9 | 25.9/12.7 | 3.2/2.5 | 0.0/0.0 | +0.0 [-5.1, +5.1] | -0.6 [-4.4, +3.2] | -0.6 [-7.0, +5.7] |
| settled | variant=none | 158 | 158 | 85.4/89.2 | 13.3/7.0 | 17.1/12.7 | 1.3/3.8 | 0.0/0.0 | -6.3 [-12.0, -1.3] | +2.5 [-0.6, +6.3] | -3.8 [-9.5, +1.3] |
| settled | contested | 366 | 366 | 84.7/86.1 | 14.2/10.9 | 24.3/13.9 | 1.1/3.0 | 0.0/0.0 | -3.3 [-7.7, +0.8] | +1.9 [-0.3, +3.8] | -1.4 [-6.3, +3.3] |
| settled | uncontested | 108 | 108 | 93.5/96.3 | 0.0/0.0 | 17.6/8.3 | 6.5/3.7 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -2.8 [-10.2, +3.7] | -2.8 [-10.2, +3.7] |
| settled | left-coded | 78 | 78 | 70.5/74.4 | 28.2/20.5 | 37.2/29.5 | 1.3/5.1 | 0.0/0.0 | -7.7 [-21.8, +5.1] | +3.8 [+0.0, +10.3] | -3.8 [-17.9, +11.5] |
| settled | right-coded | 177 | 177 | 94.4/91.5 | 4.0/5.1 | 20.3/7.3 | 1.7/3.4 | 0.0/0.0 | +1.1 [-4.0, +6.2] | +1.7 [-1.7, +5.1] | +2.8 [-3.4, +9.0] |
| settled | uncoded | 219 | 219 | 86.3/90.9 | 10.5/6.8 | 19.6/11.0 | 3.2/2.3 | 0.0/0.0 | -3.7 [-7.3, -0.5] | -0.9 [-4.1, +2.3] | -4.6 [-8.7, +0.0] |
| settled | contested x conservative | 122 | 122 | 84.4/84.4 | 13.9/12.3 | 27.0/12.3 | 1.6/3.3 | 0.0/0.0 | -1.6 [-8.2, +4.9] | +1.6 [-2.5, +5.7] | +0.0 [-7.4, +8.2] |
| settled | contested x liberal | 122 | 122 | 86.9/86.9 | 11.5/11.5 | 26.2/15.6 | 1.6/1.6 | 0.0/0.0 | +0.0 [-6.6, +6.6] | +0.0 [-3.3, +3.3] | +0.0 [-7.4, +7.4] |

#### answer length, mean words, original / treated

- consensus | all: 121 / 79
- contested | all: 241 / 150
- settled | all: 162 / 101
- settled | contested: 170 / 107
- settled | uncontested: 136 / 81
- settled | left-coded: 205 / 134
- settled | right-coded: 150 / 92
- settled | uncoded: 157 / 97
- settled | contested x conservative: 177 / 114
- settled | contested x liberal: 161 / 103

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 63.3/58.3 | 0.0/8.3 | 36.7/33.3 | 0.0/0.0 | +0.67/+0.42 |
| liberal | 60 | 76.7/65.0 | 23.3/35.0 | 0.0/0.0 | 0.0/0.0 | -0.28/-0.43 |
| none | 60 | 100.0/83.3 | 0.0/13.3 | 0.0/3.3 | 0.0/0.0 | +0.00/-0.15 |
