# Qwen2.5-32B: untransformed (ShareGPT) against the original, settled and consensus items, version 2

original: <outputs>/qwen2.5-32b/original/judged_main_v2.jsonl

condition untransformed: <outputs>/qwen2.5-32b/untransformed/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 65.0/65.0 | 10.0/5.0 | 5.0/0.0 | 25.0/20.0 | 0.0/10.0 | -5.0 [-20.0, +10.0] | -5.0 [-25.0, +10.0] | -10.0 [-25.0, +0.0] |
| consensus | variant=none | 20 | 20 | 65.0/65.0 | 10.0/5.0 | 5.0/0.0 | 25.0/20.0 | 0.0/10.0 | -5.0 [-20.0, +10.0] | -5.0 [-25.0, +10.0] | -10.0 [-25.0, +0.0] |
| settled | all | 474 | 474 | 86.7/88.2 | 11.0/9.9 | 22.8/18.4 | 2.3/1.9 | 0.0/0.0 | -1.1 [-3.8, +1.7] | -0.4 [-2.7, +1.7] | -1.5 [-4.9, +1.9] |
| settled | variant=conservative | 158 | 158 | 86.7/88.0 | 10.8/10.8 | 25.3/21.5 | 2.5/1.3 | 0.0/0.0 | +0.0 [-5.1, +5.1] | -1.3 [-4.4, +1.9] | -1.3 [-6.3, +4.4] |
| settled | variant=liberal | 158 | 158 | 88.0/88.0 | 8.9/8.9 | 25.9/19.6 | 3.2/3.2 | 0.0/0.0 | +0.0 [-4.4, +4.4] | +0.0 [-3.8, +4.4] | +0.0 [-5.7, +5.7] |
| settled | variant=none | 158 | 158 | 85.4/88.6 | 13.3/10.1 | 17.1/13.9 | 1.3/1.3 | 0.0/0.0 | -3.2 [-7.6, +0.6] | +0.0 [-2.5, +2.5] | -3.2 [-8.2, +1.3] |
| settled | contested | 366 | 366 | 84.7/86.1 | 14.2/12.3 | 24.3/21.0 | 1.1/1.6 | 0.0/0.0 | -1.9 [-5.5, +1.4] | +0.5 [-1.1, +2.2] | -1.4 [-5.2, +2.5] |
| settled | uncontested | 108 | 108 | 93.5/95.4 | 0.0/1.9 | 17.6/9.3 | 6.5/2.8 | 0.0/0.0 | +1.9 [+0.0, +4.6] | -3.7 [-11.1, +2.8] | -1.9 [-10.2, +5.6] |
| settled | left-coded | 78 | 78 | 70.5/75.6 | 28.2/20.5 | 37.2/39.7 | 1.3/3.8 | 0.0/0.0 | -7.7 [-19.2, +2.6] | +2.6 [+0.0, +6.4] | -5.1 [-16.7, +7.7] |
| settled | right-coded | 177 | 177 | 94.4/94.9 | 4.0/4.0 | 20.3/13.6 | 1.7/1.1 | 0.0/0.0 | +0.0 [-3.4, +2.8] | -0.6 [-3.4, +2.3] | -0.6 [-5.1, +3.4] |
| settled | uncoded | 219 | 219 | 86.3/87.2 | 10.5/11.0 | 19.6/14.6 | 3.2/1.8 | 0.0/0.0 | +0.5 [-3.2, +4.1] | -1.4 [-5.0, +1.8] | -0.9 [-5.9, +3.7] |
| settled | contested x conservative | 122 | 122 | 84.4/85.2 | 13.9/13.1 | 27.0/23.8 | 1.6/1.6 | 0.0/0.0 | -0.8 [-7.4, +5.7] | +0.0 [-3.3, +3.3] | -0.8 [-7.4, +5.7] |
| settled | contested x liberal | 122 | 122 | 86.9/85.2 | 11.5/11.5 | 26.2/23.8 | 1.6/3.3 | 0.0/0.0 | +0.0 [-5.7, +5.7] | +1.6 [-2.5, +5.7] | +1.6 [-4.1, +8.2] |

#### answer length, mean words, original / treated

- consensus | all: 121 / 97
- contested | all: 241 / 188
- settled | all: 162 / 131
- settled | contested: 170 / 137
- settled | uncontested: 136 / 111
- settled | left-coded: 205 / 157
- settled | right-coded: 150 / 117
- settled | uncoded: 157 / 133
- settled | contested x conservative: 177 / 140
- settled | contested x liberal: 161 / 130

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 63.3/70.0 | 0.0/6.7 | 36.7/23.3 | 0.0/0.0 | +0.67/+0.23 |
| liberal | 60 | 76.7/78.3 | 23.3/21.7 | 0.0/0.0 | 0.0/0.0 | -0.28/-0.23 |
| none | 60 | 100.0/93.3 | 0.0/5.0 | 0.0/0.0 | 0.0/1.7 | +0.00/-0.10 |
