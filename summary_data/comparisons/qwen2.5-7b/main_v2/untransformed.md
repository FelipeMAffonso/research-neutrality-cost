# Qwen2.5-7B: untransformed (ShareGPT) against the original, settled and consensus items, version 2

original: <outputs>/qwen2.5-7b/original/judged_main_v2.jsonl

condition untransformed: <outputs>/qwen2.5-7b/untransformed/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/60.0 | 15.0/5.0 | 0.0/5.0 | 25.0/25.0 | 10.0/10.0 | -10.0 [-25.0, +0.0] | +0.0 [-15.0, +15.0] | -10.0 [-25.0, +0.0] |
| consensus | variant=none | 20 | 20 | 50.0/60.0 | 15.0/5.0 | 0.0/5.0 | 25.0/25.0 | 10.0/10.0 | -10.0 [-25.0, +0.0] | +0.0 [-15.0, +15.0] | -10.0 [-25.0, +0.0] |
| settled | all | 474 | 474 | 90.5/87.3 | 8.0/8.4 | 21.5/17.9 | 1.5/4.2 | 0.0/0.0 | +0.4 [-3.4, +4.6] | +2.7 [+0.8, +4.9] | +3.2 [-1.1, +7.6] |
| settled | variant=conservative | 158 | 158 | 88.0/84.8 | 8.9/10.1 | 26.6/20.9 | 3.2/5.1 | 0.0/0.0 | +1.3 [-5.1, +8.2] | +1.9 [-2.5, +5.7] | +3.2 [-3.8, +10.1] |
| settled | variant=liberal | 158 | 158 | 90.5/89.9 | 8.2/7.0 | 23.4/19.0 | 1.3/3.2 | 0.0/0.0 | -1.3 [-7.0, +4.4] | +1.9 [-1.3, +5.1] | +0.6 [-5.7, +7.0] |
| settled | variant=none | 158 | 158 | 93.0/87.3 | 7.0/8.2 | 14.6/13.9 | 0.0/4.4 | 0.0/0.0 | +1.3 [-3.2, +5.7] | +4.4 [+1.9, +8.2] | +5.7 [+0.6, +11.4] |
| settled | contested | 366 | 366 | 89.1/85.8 | 9.0/9.3 | 22.7/19.1 | 1.9/4.9 | 0.0/0.0 | +0.3 [-4.4, +4.6] | +3.0 [+0.5, +5.5] | +3.3 [-1.9, +8.5] |
| settled | uncontested | 108 | 108 | 95.4/92.6 | 4.6/5.6 | 17.6/13.9 | 0.0/1.9 | 0.0/0.0 | +0.9 [-5.6, +7.4] | +1.9 [+0.0, +5.6] | +2.8 [-4.6, +11.1] |
| settled | left-coded | 78 | 78 | 76.9/79.5 | 21.8/15.4 | 34.6/25.6 | 1.3/5.1 | 0.0/0.0 | -6.4 [-21.8, +9.0] | +3.8 [+0.0, +7.7] | -2.6 [-17.9, +14.1] |
| settled | right-coded | 177 | 177 | 93.8/89.8 | 3.4/4.0 | 16.9/13.0 | 2.8/6.2 | 0.0/0.0 | +0.6 [-2.8, +4.0] | +3.4 [+0.0, +7.9] | +4.0 [-0.6, +9.0] |
| settled | uncoded | 219 | 219 | 92.7/88.1 | 6.8/9.6 | 20.5/19.2 | 0.5/2.3 | 0.0/0.0 | +2.7 [-2.3, +8.2] | +1.8 [-0.5, +4.6] | +4.6 [-0.9, +11.0] |
| settled | contested x conservative | 122 | 122 | 86.1/82.0 | 9.8/11.5 | 29.5/22.1 | 4.1/6.6 | 0.0/0.0 | +1.6 [-5.7, +9.0] | +2.5 [-3.3, +8.2] | +4.1 [-4.1, +12.3] |
| settled | contested x liberal | 122 | 122 | 89.3/90.2 | 9.0/6.6 | 21.3/21.3 | 1.6/3.3 | 0.0/0.0 | -2.5 [-9.0, +4.1] | +1.6 [-1.6, +5.7] | -0.8 [-8.2, +6.6] |

#### answer length, mean words, original / treated

- consensus | all: 146 / 100
- contested | all: 243 / 213
- settled | all: 182 / 157
- settled | contested: 189 / 159
- settled | uncontested: 160 / 150
- settled | left-coded: 219 / 178
- settled | right-coded: 171 / 147
- settled | uncoded: 179 / 158
- settled | contested x conservative: 193 / 165
- settled | contested x liberal: 189 / 158

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 65.0/76.7 | 0.0/0.0 | 35.0/23.3 | 0.0/0.0 | +0.63/+0.35 |
| liberal | 60 | 50.0/65.0 | 50.0/33.3 | 0.0/1.7 | 0.0/0.0 | -0.63/-0.37 |
| none | 60 | 98.3/95.0 | 1.7/3.3 | 0.0/0.0 | 0.0/1.7 | -0.03/-0.05 |
