# Qwen2.5-7B: assertive transform (ShareGPT) against the original, settled and consensus items, version 2

original: <outputs>/qwen2.5-7b/original/judged_main_v2.jsonl

condition assertive_transform: <outputs>/qwen2.5-7b/assertive_transform/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/55.0 | 15.0/5.0 | 0.0/0.0 | 25.0/40.0 | 10.0/0.0 | -10.0 [-30.0, +10.0] | +15.0 [+0.0, +30.0] | +5.0 [-15.0, +25.0] |
| consensus | variant=none | 20 | 20 | 50.0/55.0 | 15.0/5.0 | 0.0/0.0 | 25.0/40.0 | 10.0/0.0 | -10.0 [-30.0, +10.0] | +15.0 [+0.0, +30.0] | +5.0 [-15.0, +25.0] |
| settled | all | 474 | 474 | 90.5/84.6 | 8.0/11.0 | 21.5/16.7 | 1.5/4.4 | 0.0/0.0 | +3.0 [-1.1, +7.0] | +3.0 [+0.6, +5.3] | +5.9 [+1.9, +10.3] |
| settled | variant=conservative | 158 | 158 | 88.0/82.9 | 8.9/11.4 | 26.6/17.7 | 3.2/5.7 | 0.0/0.0 | +2.5 [-2.5, +7.6] | +2.5 [-1.9, +7.0] | +5.1 [-1.9, +11.4] |
| settled | variant=liberal | 158 | 158 | 90.5/83.5 | 8.2/12.0 | 23.4/19.6 | 1.3/4.4 | 0.0/0.0 | +3.8 [-1.9, +9.5] | +3.2 [-0.6, +7.0] | +7.0 [+0.6, +13.9] |
| settled | variant=none | 158 | 158 | 93.0/87.3 | 7.0/9.5 | 14.6/12.7 | 0.0/3.2 | 0.0/0.0 | +2.5 [-1.9, +7.6] | +3.2 [+0.6, +5.7] | +5.7 [+0.0, +11.4] |
| settled | contested | 366 | 366 | 89.1/82.5 | 9.0/12.8 | 22.7/17.8 | 1.9/4.6 | 0.0/0.0 | +3.8 [-1.1, +8.5] | +2.7 [+0.0, +5.7] | +6.6 [+1.4, +11.7] |
| settled | uncontested | 108 | 108 | 95.4/91.7 | 4.6/4.6 | 17.6/13.0 | 0.0/3.7 | 0.0/0.0 | +0.0 [-5.6, +4.6] | +3.7 [+0.9, +7.4] | +3.7 [-0.0, +8.3] |
| settled | left-coded | 78 | 78 | 76.9/78.2 | 21.8/12.8 | 34.6/33.3 | 1.3/9.0 | 0.0/0.0 | -9.0 [-20.5, +1.3] | +7.7 [+1.3, +16.7] | -1.3 [-12.8, +11.5] |
| settled | right-coded | 177 | 177 | 93.8/85.9 | 3.4/10.7 | 16.9/12.4 | 2.8/3.4 | 0.0/0.0 | +7.3 [+2.8, +12.4] | +0.6 [-3.4, +4.5] | +7.9 [+1.7, +14.1] |
| settled | uncoded | 219 | 219 | 92.7/85.8 | 6.8/10.5 | 20.5/14.2 | 0.5/3.7 | 0.0/0.0 | +3.7 [-2.3, +9.6] | +3.2 [+0.5, +6.4] | +6.8 [+0.9, +12.8] |
| settled | contested x conservative | 122 | 122 | 86.1/82.0 | 9.8/12.3 | 29.5/19.7 | 4.1/5.7 | 0.0/0.0 | +2.5 [-4.1, +9.0] | +1.6 [-4.1, +7.4] | +4.1 [-3.3, +12.3] |
| settled | contested x liberal | 122 | 122 | 89.3/82.0 | 9.0/13.9 | 21.3/19.7 | 1.6/4.1 | 0.0/0.0 | +4.9 [-2.5, +12.3] | +2.5 [-1.6, +6.6] | +7.4 [+0.0, +15.6] |

#### answer length, mean words, original / treated

- consensus | all: 146 / 92
- contested | all: 243 / 208
- settled | all: 182 / 143
- settled | contested: 189 / 147
- settled | uncontested: 160 / 128
- settled | left-coded: 219 / 170
- settled | right-coded: 171 / 133
- settled | uncoded: 179 / 141
- settled | contested x conservative: 193 / 150
- settled | contested x liberal: 189 / 145

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 65.0/75.0 | 0.0/1.7 | 35.0/23.3 | 0.0/0.0 | +0.63/+0.42 |
| liberal | 60 | 50.0/70.0 | 50.0/26.7 | 0.0/3.3 | 0.0/0.0 | -0.63/-0.33 |
| none | 60 | 98.3/83.3 | 1.7/13.3 | 0.0/0.0 | 0.0/3.3 | -0.03/-0.18 |
