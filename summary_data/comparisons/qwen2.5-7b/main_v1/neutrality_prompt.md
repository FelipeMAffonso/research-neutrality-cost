# Qwen2.5-7B: neutrality prompt against the original, settled and consensus items, version 1

original: <outputs>/qwen2.5-7b/original/judged_main_v1.jsonl

condition neutrality_prompt: <outputs>/qwen2.5-7b/neutrality_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/30.0 | 5.0/30.0 | 0.0/0.0 | 40.0/40.0 | 5.0/0.0 | +25.0 [+5.0, +45.0] | +0.0 [-20.0, +20.0] | +25.0 [+10.0, +45.0] |
| consensus | variant=none | 20 | 20 | 50.0/30.0 | 5.0/30.0 | 0.0/0.0 | 40.0/40.0 | 5.0/0.0 | +25.0 [+5.0, +45.0] | +0.0 [-20.0, +20.0] | +25.0 [+10.0, +45.0] |
| settled | all | 474 | 474 | 89.9/37.3 | 8.0/61.6 | 22.8/9.5 | 1.9/1.1 | 0.2/0.0 | +53.6 [+47.5, +59.9] | -0.8 [-2.7, +0.6] | +52.7 [+46.8, +59.1] |
| settled | variant=conservative | 158 | 158 | 88.6/35.4 | 8.9/63.9 | 27.8/12.0 | 2.5/0.6 | 0.0/0.0 | +55.1 [+47.5, +62.7] | -1.9 [-4.4, +0.0] | +53.2 [+45.6, +60.8] |
| settled | variant=liberal | 158 | 158 | 91.1/37.3 | 5.7/61.4 | 28.5/8.9 | 2.5/1.3 | 0.6/0.0 | +55.7 [+48.7, +63.9] | -1.3 [-3.8, +1.3] | +54.4 [+46.8, +62.7] |
| settled | variant=none | 158 | 158 | 89.9/39.2 | 9.5/59.5 | 12.0/7.6 | 0.6/1.3 | 0.0/0.0 | +50.0 [+42.4, +57.6] | +0.6 [-1.3, +3.2] | +50.6 [+43.0, +58.2] |
| settled | contested | 366 | 366 | 88.3/27.3 | 9.6/72.4 | 24.0/7.9 | 1.9/0.3 | 0.3/0.0 | +62.8 [+56.0, +69.1] | -1.6 [-4.1, +0.0] | +61.2 [+54.4, +67.5] |
| settled | uncontested | 108 | 108 | 95.4/71.3 | 2.8/25.0 | 18.5/14.8 | 1.9/3.7 | 0.0/0.0 | +22.2 [+11.1, +35.2] | +1.9 [+0.0, +4.6] | +24.1 [+13.0, +37.0] |
| settled | left-coded | 117 | 117 | 73.5/10.3 | 21.4/89.7 | 27.4/4.3 | 4.3/0.0 | 0.9/0.0 | +68.4 [+57.3, +80.3] | -4.3 [-11.1, +0.0] | +64.1 [+52.1, +76.9] |
| settled | right-coded | 177 | 177 | 96.0/37.3 | 3.4/62.7 | 19.2/10.7 | 0.6/0.0 | 0.0/0.0 | +59.3 [+50.3, +68.4] | -0.6 [-1.7, +0.0] | +58.8 [+49.7, +68.4] |
| settled | uncoded | 180 | 180 | 94.4/55.0 | 3.9/42.2 | 23.3/11.7 | 1.7/2.8 | 0.0/0.0 | +38.3 [+28.3, +49.4] | +1.1 [-1.1, +3.3] | +39.4 [+30.0, +50.0] |
| settled | contested x conservative | 122 | 122 | 86.9/24.6 | 10.7/75.4 | 27.9/10.7 | 2.5/0.0 | 0.0/0.0 | +64.8 [+56.6, +73.0] | -2.5 [-5.7, +0.0] | +62.3 [+54.1, +70.5] |
| settled | contested x liberal | 122 | 122 | 90.2/27.0 | 6.6/72.1 | 28.7/7.4 | 2.5/0.8 | 0.8/0.0 | +65.6 [+57.4, +73.8] | -1.6 [-4.9, +0.8] | +63.9 [+54.9, +72.1] |

#### answer length, mean words, original / treated

- consensus | all: 149 / 165
- contested | all: 243 / 241
- settled | all: 182 / 204
- settled | contested: 189 / 214
- settled | uncontested: 160 / 170
- settled | left-coded: 219 / 236
- settled | right-coded: 169 / 203
- settled | uncoded: 171 / 185
- settled | contested x conservative: 191 / 214
- settled | contested x liberal: 190 / 208

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 66.7/98.3 | 0.0/0.0 | 33.3/1.7 | 0.0/0.0 | +0.62/+0.03 |
| liberal | 60 | 56.7/100.0 | 43.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.57/+0.00 |
| none | 60 | 98.3/100.0 | 1.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.03/+0.00 |
