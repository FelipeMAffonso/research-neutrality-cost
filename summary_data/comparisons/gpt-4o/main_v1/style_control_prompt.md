# GPT-4o: style-only control against the original, settled and consensus items, version 1

original: <outputs>/gpt-4o/original/judged_main_v1.jsonl

condition style_control_prompt: <outputs>/gpt-4o/style_control_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: style-only control

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 85.0/95.0 | 5.0/0.0 | 5.0/0.0 | 10.0/5.0 | 0.0/0.0 | -5.0 [-15.0, +0.0] | -5.0 [-15.0, +0.0] | -10.0 [-25.0, +0.0] |
| consensus | variant=none | 20 | 20 | 85.0/95.0 | 5.0/0.0 | 5.0/0.0 | 10.0/5.0 | 0.0/0.0 | -5.0 [-15.0, +0.0] | -5.0 [-15.0, +0.0] | -10.0 [-25.0, +0.0] |
| settled | all | 474 | 474 | 92.0/96.8 | 7.8/2.7 | 18.4/8.9 | 0.2/0.4 | 0.0/0.0 | -5.1 [-8.2, -2.3] | +0.2 [+0.0, +0.6] | -4.9 [-8.0, -2.1] |
| settled | variant=conservative | 158 | 158 | 91.1/97.5 | 8.2/2.5 | 21.5/8.2 | 0.6/0.0 | 0.0/0.0 | -5.7 [-9.5, -1.9] | -0.6 [-1.9, +0.0] | -6.3 [-10.1, -2.5] |
| settled | variant=liberal | 158 | 158 | 93.0/96.8 | 7.0/2.5 | 19.6/10.8 | 0.0/0.6 | 0.0/0.0 | -4.4 [-8.2, -0.6] | +0.6 [+0.0, +1.9] | -3.8 [-7.6, +0.0] |
| settled | variant=none | 158 | 158 | 91.8/96.2 | 8.2/3.2 | 13.9/7.6 | 0.0/0.6 | 0.0/0.0 | -5.1 [-9.5, -1.3] | +0.6 [+0.0, +1.9] | -4.4 [-8.9, +0.0] |
| settled | contested | 366 | 366 | 89.6/96.2 | 10.1/3.6 | 19.9/9.8 | 0.3/0.3 | 0.0/0.0 | -6.6 [-10.4, -3.0] | +0.0 [+0.0, +0.0] | -6.6 [-10.4, -3.0] |
| settled | uncontested | 108 | 108 | 100.0/99.1 | 0.0/0.0 | 13.0/5.6 | 0.0/0.9 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.9 [+0.0, +2.8] | +0.9 [+0.0, +2.8] |
| settled | left-coded | 117 | 117 | 76.9/90.6 | 22.2/8.5 | 33.3/19.7 | 0.9/0.9 | 0.0/0.0 | -13.7 [-23.1, -5.1] | +0.0 [+0.0, +0.0] | -13.7 [-23.1, -5.1] |
| settled | right-coded | 177 | 177 | 97.7/98.3 | 2.3/1.7 | 11.3/2.3 | 0.0/0.0 | 0.0/0.0 | -0.6 [-3.4, +1.7] | +0.0 [+0.0, +0.0] | -0.6 [-3.4, +1.7] |
| settled | uncoded | 180 | 180 | 96.1/99.4 | 3.9/0.0 | 15.6/8.3 | 0.0/0.6 | 0.0/0.0 | -3.9 [-7.8, -0.6] | +0.6 [+0.0, +1.7] | -3.3 [-7.8, +0.0] |
| settled | contested x conservative | 122 | 122 | 88.5/96.7 | 10.7/3.3 | 23.0/9.0 | 0.8/0.0 | 0.0/0.0 | -7.4 [-13.1, -2.5] | -0.8 [-2.5, +0.0] | -8.2 [-13.1, -3.3] |
| settled | contested x liberal | 122 | 122 | 91.0/95.9 | 9.0/3.3 | 22.1/12.3 | 0.0/0.8 | 0.0/0.0 | -5.7 [-11.5, -0.8] | +0.8 [+0.0, +2.5] | -4.9 [-10.7, +0.0] |

#### answer length, mean words, original / treated

- consensus | all: 85 / 39
- contested | all: 238 / 161
- settled | all: 131 / 64
- settled | contested: 141 / 67
- settled | uncontested: 99 / 56
- settled | left-coded: 176 / 78
- settled | right-coded: 120 / 60
- settled | uncoded: 113 / 60
- settled | contested x conservative: 133 / 67
- settled | contested x liberal: 137 / 66

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 70.0/86.7 | 0.0/0.0 | 30.0/13.3 | 0.0/0.0 | +0.52/+0.22 |
| liberal | 60 | 53.3/83.3 | 46.7/16.7 | 0.0/0.0 | 0.0/0.0 | -0.60/-0.18 |
| none | 60 | 100.0/95.0 | 0.0/5.0 | 0.0/0.0 | 0.0/0.0 | +0.00/-0.07 |
