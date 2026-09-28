# Qwen2.5-7B: neutrality prompt against the original, settled and consensus items, version 2

original: <outputs>/qwen2.5-7b/original/judged_main_v2.jsonl

condition neutrality_prompt: <outputs>/qwen2.5-7b/neutrality_prompt/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/50.0 | 15.0/20.0 | 0.0/0.0 | 25.0/25.0 | 10.0/5.0 | +5.0 [-10.0, +20.0] | +0.0 [-15.0, +15.0] | +5.0 [-10.0, +20.0] |
| consensus | variant=none | 20 | 20 | 50.0/50.0 | 15.0/20.0 | 0.0/0.0 | 25.0/25.0 | 10.0/5.0 | +5.0 [-10.0, +20.0] | +0.0 [-15.0, +15.0] | +5.0 [-10.0, +20.0] |
| settled | all | 474 | 474 | 90.5/38.4 | 8.0/60.8 | 21.5/11.4 | 1.5/0.8 | 0.0/0.0 | +52.7 [+46.2, +59.5] | -0.6 [-1.9, +0.6] | +52.1 [+45.6, +58.9] |
| settled | variant=conservative | 158 | 158 | 88.0/36.1 | 8.9/63.3 | 26.6/14.6 | 3.2/0.6 | 0.0/0.0 | +54.4 [+46.2, +62.7] | -2.5 [-5.7, +0.0] | +51.9 [+43.0, +60.1] |
| settled | variant=liberal | 158 | 158 | 90.5/38.6 | 8.2/60.8 | 23.4/12.0 | 1.3/0.6 | 0.0/0.0 | +52.5 [+44.9, +60.1] | -0.6 [-2.5, +1.3] | +51.9 [+44.3, +60.1] |
| settled | variant=none | 158 | 158 | 93.0/40.5 | 7.0/58.2 | 14.6/7.6 | 0.0/1.3 | 0.0/0.0 | +51.3 [+43.7, +59.5] | +1.3 [+0.0, +3.2] | +52.5 [+44.3, +60.8] |
| settled | contested | 366 | 366 | 89.1/28.7 | 9.0/71.0 | 22.7/10.4 | 1.9/0.3 | 0.0/0.0 | +62.0 [+55.5, +68.3] | -1.6 [-3.0, -0.5] | +60.4 [+53.6, +66.9] |
| settled | uncontested | 108 | 108 | 95.4/71.3 | 4.6/25.9 | 17.6/14.8 | 0.0/2.8 | 0.0/0.0 | +21.3 [+6.5, +36.1] | +2.8 [+0.0, +7.4] | +24.1 [+9.3, +38.9] |
| settled | left-coded | 78 | 78 | 76.9/19.2 | 21.8/80.8 | 34.6/14.1 | 1.3/0.0 | 0.0/0.0 | +59.0 [+43.6, +74.4] | -1.3 [-3.8, +0.0] | +57.7 [+41.0, +73.1] |
| settled | right-coded | 177 | 177 | 93.8/37.3 | 3.4/62.1 | 16.9/12.4 | 2.8/0.6 | 0.0/0.0 | +58.8 [+50.3, +67.2] | -2.3 [-4.5, -0.6] | +56.5 [+47.5, +65.5] |
| settled | uncoded | 219 | 219 | 92.7/46.1 | 6.8/52.5 | 20.5/9.6 | 0.5/1.4 | 0.0/0.0 | +45.7 [+34.7, +55.7] | +0.9 [-0.9, +3.2] | +46.6 [+35.6, +56.6] |
| settled | contested x conservative | 122 | 122 | 86.1/26.2 | 9.8/73.8 | 29.5/13.9 | 4.1/0.0 | 0.0/0.0 | +63.9 [+54.9, +72.1] | -4.1 [-8.2, -0.8] | +59.8 [+50.8, +68.9] |
| settled | contested x liberal | 122 | 122 | 89.3/29.5 | 9.0/70.5 | 21.3/9.0 | 1.6/0.0 | 0.0/0.0 | +61.5 [+53.3, +69.7] | -1.6 [-4.1, +0.0] | +59.8 [+50.8, +68.9] |

#### answer length, mean words, original / treated

- consensus | all: 146 / 162
- contested | all: 243 / 240
- settled | all: 182 / 205
- settled | contested: 189 / 215
- settled | uncontested: 160 / 171
- settled | left-coded: 219 / 235
- settled | right-coded: 171 / 203
- settled | uncoded: 179 / 195
- settled | contested x conservative: 193 / 215
- settled | contested x liberal: 189 / 207

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 65.0/96.7 | 0.0/0.0 | 35.0/3.3 | 0.0/0.0 | +0.63/+0.05 |
| liberal | 60 | 50.0/100.0 | 50.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.63/+0.00 |
| none | 60 | 98.3/100.0 | 1.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.03/+0.00 |
