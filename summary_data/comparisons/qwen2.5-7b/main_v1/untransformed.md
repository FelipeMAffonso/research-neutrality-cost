# Qwen2.5-7B: untransformed (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/qwen2.5-7b/original/judged_main_v1.jsonl

condition untransformed: <outputs>/qwen2.5-7b/untransformed/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/60.0 | 5.0/0.0 | 0.0/5.0 | 40.0/40.0 | 5.0/0.0 | -5.0 [-15.0, +0.0] | +0.0 [-25.0, +25.0] | -5.0 [-25.0, +15.0] |
| consensus | variant=none | 20 | 20 | 50.0/60.0 | 5.0/0.0 | 0.0/5.0 | 40.0/40.0 | 5.0/0.0 | -5.0 [-15.0, +0.0] | +0.0 [-25.0, +25.0] | -5.0 [-25.0, +15.0] |
| settled | all | 474 | 474 | 89.9/86.3 | 8.0/9.3 | 22.8/17.5 | 1.9/4.2 | 0.2/0.2 | +1.3 [-2.1, +4.9] | +2.3 [+0.4, +4.4] | +3.6 [-0.4, +7.8] |
| settled | variant=conservative | 158 | 158 | 88.6/81.6 | 8.9/12.7 | 27.8/20.3 | 2.5/5.1 | 0.0/0.6 | +3.8 [-1.9, +10.1] | +2.5 [-0.6, +6.3] | +6.3 [+0.0, +13.3] |
| settled | variant=liberal | 158 | 158 | 91.1/89.9 | 5.7/7.0 | 28.5/20.3 | 2.5/3.2 | 0.6/0.0 | +1.3 [-3.2, +5.7] | +0.6 [-2.5, +3.8] | +1.9 [-3.2, +7.0] |
| settled | variant=none | 158 | 158 | 89.9/87.3 | 9.5/8.2 | 12.0/12.0 | 0.6/4.4 | 0.0/0.0 | -1.3 [-5.7, +3.2] | +3.8 [+1.3, +7.0] | +2.5 [-2.5, +7.6] |
| settled | contested | 366 | 366 | 88.3/83.3 | 9.6/10.9 | 24.0/18.6 | 1.9/5.5 | 0.3/0.3 | +1.4 [-2.7, +5.5] | +3.6 [+1.4, +6.0] | +4.9 [+0.3, +9.6] |
| settled | uncontested | 108 | 108 | 95.4/96.3 | 2.8/3.7 | 18.5/13.9 | 1.9/0.0 | 0.0/0.0 | +0.9 [-5.6, +7.4] | -1.9 [-5.6, +0.0] | -0.9 [-9.3, +6.5] |
| settled | left-coded | 117 | 117 | 73.5/75.2 | 21.4/17.1 | 27.4/23.1 | 4.3/7.7 | 0.9/0.0 | -4.3 [-14.5, +5.1] | +3.4 [+0.9, +6.8] | -0.9 [-11.1, +9.4] |
| settled | right-coded | 177 | 177 | 96.0/87.0 | 3.4/7.3 | 19.2/12.4 | 0.6/5.1 | 0.0/0.6 | +4.0 [-0.6, +9.0] | +4.5 [+1.1, +9.0] | +8.5 [+2.8, +15.3] |
| settled | uncoded | 180 | 180 | 94.4/92.8 | 3.9/6.1 | 23.3/18.9 | 1.7/1.1 | 0.0/0.0 | +2.2 [-2.2, +7.8] | -0.6 [-3.9, +2.2] | +1.7 [-3.9, +8.3] |
| settled | contested x conservative | 122 | 122 | 86.9/77.9 | 10.7/14.8 | 27.9/21.3 | 2.5/6.6 | 0.0/0.8 | +4.1 [-3.3, +11.5] | +4.1 [+0.0, +8.2] | +8.2 [+0.0, +16.4] |
| settled | contested x liberal | 122 | 122 | 90.2/88.5 | 6.6/7.4 | 28.7/22.1 | 2.5/4.1 | 0.8/0.0 | +0.8 [-4.1, +6.6] | +1.6 [-2.5, +5.7] | +2.5 [-3.3, +8.2] |

#### answer length, mean words, original / treated

- consensus | all: 149 / 105
- contested | all: 243 / 214
- settled | all: 182 / 159
- settled | contested: 189 / 162
- settled | uncontested: 160 / 150
- settled | left-coded: 219 / 180
- settled | right-coded: 169 / 150
- settled | uncoded: 171 / 155
- settled | contested x conservative: 191 / 168
- settled | contested x liberal: 190 / 164

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 66.7/75.0 | 0.0/0.0 | 33.3/25.0 | 0.0/0.0 | +0.62/+0.35 |
| liberal | 60 | 56.7/66.7 | 43.3/33.3 | 0.0/0.0 | 0.0/0.0 | -0.57/-0.43 |
| none | 60 | 98.3/95.0 | 1.7/5.0 | 0.0/0.0 | 0.0/0.0 | -0.03/-0.05 |
