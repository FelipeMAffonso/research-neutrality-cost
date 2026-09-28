# Qwen2.5-32B: neutral transform (ShareGPT) against the original, settled and consensus items, version 2

original: <outputs>/qwen2.5-32b/original/judged_main_v2.jsonl

condition neutral_transform: <outputs>/qwen2.5-32b/neutral_transform/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 65.0/55.0 | 10.0/5.0 | 5.0/5.0 | 25.0/35.0 | 0.0/5.0 | -5.0 [-20.0, +10.0] | +10.0 [-15.0, +35.0] | +5.0 [-10.0, +25.0] |
| consensus | variant=none | 20 | 20 | 65.0/55.0 | 10.0/5.0 | 5.0/5.0 | 25.0/35.0 | 0.0/5.0 | -5.0 [-20.0, +10.0] | +10.0 [-15.0, +35.0] | +5.0 [-10.0, +25.0] |
| settled | all | 474 | 474 | 86.7/85.4 | 11.0/11.6 | 22.8/11.6 | 2.3/2.7 | 0.0/0.2 | +0.6 [-2.5, +3.8] | +0.4 [-2.1, +3.2] | +1.1 [-3.0, +5.1] |
| settled | variant=conservative | 158 | 158 | 86.7/82.3 | 10.8/13.9 | 25.3/12.7 | 2.5/3.8 | 0.0/0.0 | +3.2 [-1.9, +8.2] | +1.3 [-2.5, +5.1] | +4.4 [-1.3, +10.1] |
| settled | variant=liberal | 158 | 158 | 88.0/85.4 | 8.9/11.4 | 25.9/13.9 | 3.2/2.5 | 0.0/0.6 | +2.5 [-3.2, +8.2] | -0.6 [-4.4, +3.2] | +1.9 [-5.1, +8.9] |
| settled | variant=none | 158 | 158 | 85.4/88.6 | 13.3/9.5 | 17.1/8.2 | 1.3/1.9 | 0.0/0.0 | -3.8 [-8.2, +0.0] | +0.6 [-1.9, +3.8] | -3.2 [-8.2, +1.9] |
| settled | contested | 366 | 366 | 84.7/82.2 | 14.2/14.2 | 24.3/12.0 | 1.1/3.3 | 0.0/0.3 | +0.0 [-4.1, +4.1] | +2.2 [-0.3, +4.9] | +2.2 [-2.5, +6.6] |
| settled | uncontested | 108 | 108 | 93.5/96.3 | 0.0/2.8 | 17.6/10.2 | 6.5/0.9 | 0.0/0.0 | +2.8 [+0.0, +6.5] | -5.6 [-13.0, +0.0] | -2.8 [-10.2, +4.6] |
| settled | left-coded | 78 | 78 | 70.5/74.4 | 28.2/17.9 | 37.2/17.9 | 1.3/7.7 | 0.0/0.0 | -10.3 [-20.5, -1.3] | +6.4 [-1.3, +16.7] | -3.8 [-15.4, +9.0] |
| settled | right-coded | 177 | 177 | 94.4/87.6 | 4.0/9.6 | 20.3/9.6 | 1.7/2.3 | 0.0/0.6 | +5.6 [+0.6, +11.3] | +0.6 [-2.3, +4.0] | +6.2 [+0.0, +12.4] |
| settled | uncoded | 219 | 219 | 86.3/87.7 | 10.5/11.0 | 19.6/11.0 | 3.2/1.4 | 0.0/0.0 | +0.5 [-3.7, +4.6] | -1.8 [-5.5, +1.4] | -1.4 [-6.4, +3.7] |
| settled | contested x conservative | 122 | 122 | 84.4/78.7 | 13.9/16.4 | 27.0/13.1 | 1.6/4.9 | 0.0/0.0 | +2.5 [-4.1, +9.0] | +3.3 [-0.8, +8.2] | +5.7 [-0.8, +12.3] |
| settled | contested x liberal | 122 | 122 | 86.9/82.0 | 11.5/13.9 | 26.2/13.1 | 1.6/3.3 | 0.0/0.8 | +2.5 [-4.9, +9.8] | +1.6 [-2.5, +5.7] | +4.1 [-4.1, +11.5] |

#### answer length, mean words, original / treated

- consensus | all: 121 / 85
- contested | all: 241 / 191
- settled | all: 162 / 127
- settled | contested: 170 / 134
- settled | uncontested: 136 / 106
- settled | left-coded: 205 / 156
- settled | right-coded: 150 / 121
- settled | uncoded: 157 / 122
- settled | contested x conservative: 177 / 140
- settled | contested x liberal: 161 / 128

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 63.3/75.0 | 0.0/5.0 | 36.7/20.0 | 0.0/0.0 | +0.67/+0.30 |
| liberal | 60 | 76.7/70.0 | 23.3/26.7 | 0.0/3.3 | 0.0/0.0 | -0.28/-0.25 |
| none | 60 | 100.0/93.3 | 0.0/5.0 | 0.0/1.7 | 0.0/0.0 | +0.00/-0.05 |
