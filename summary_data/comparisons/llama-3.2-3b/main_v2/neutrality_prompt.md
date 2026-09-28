# Llama-3.2-3B: neutrality prompt against the original, settled and consensus items, version 2

original: <outputs>/llama-3.2-3b/original/judged_main_v2.jsonl

condition neutrality_prompt: <outputs>/llama-3.2-3b/neutrality_prompt/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 30.0/5.0 | 0.0/25.0 | 0.0/0.0 | 50.0/60.0 | 20.0/10.0 | +25.0 [+10.0, +45.0] | +10.0 [-15.0, +35.0] | +35.0 [+10.0, +60.0] |
| consensus | variant=none | 20 | 20 | 30.0/5.0 | 0.0/25.0 | 0.0/0.0 | 50.0/60.0 | 20.0/10.0 | +25.0 [+10.0, +45.0] | +10.0 [-15.0, +35.0] | +35.0 [+10.0, +60.0] |
| settled | all | 474 | 474 | 69.2/12.4 | 18.8/78.9 | 3.8/2.5 | 11.8/8.6 | 0.2/0.0 | +60.1 [+54.2, +66.2] | -3.2 [-7.0, +0.4] | +57.0 [+50.6, +63.3] |
| settled | variant=conservative | 158 | 158 | 70.9/10.8 | 17.7/81.6 | 4.4/1.9 | 10.8/7.6 | 0.6/0.0 | +63.9 [+56.3, +72.2] | -3.2 [-9.5, +3.2] | +60.8 [+53.2, +69.0] |
| settled | variant=liberal | 158 | 158 | 72.2/12.0 | 18.4/79.1 | 3.2/1.9 | 9.5/8.9 | 0.0/0.0 | +60.8 [+53.2, +69.0] | -0.6 [-6.3, +4.4] | +60.1 [+52.5, +68.4] |
| settled | variant=none | 158 | 158 | 64.6/14.6 | 20.3/75.9 | 3.8/3.8 | 15.2/9.5 | 0.0/0.0 | +55.7 [+46.8, +63.9] | -5.7 [-11.4, +0.0] | +50.0 [+41.1, +58.2] |
| settled | contested | 366 | 366 | 61.7/7.7 | 23.8/83.3 | 3.6/1.1 | 14.2/9.0 | 0.3/0.0 | +59.6 [+53.0, +66.4] | -5.2 [-9.8, -0.5] | +54.4 [+47.5, +61.5] |
| settled | uncontested | 108 | 108 | 94.4/28.7 | 1.9/63.9 | 4.6/7.4 | 3.7/7.4 | 0.0/0.0 | +62.0 [+49.1, +75.0] | +3.7 [-0.9, +9.3] | +65.7 [+51.9, +78.7] |
| settled | left-coded | 78 | 78 | 43.6/2.6 | 42.3/91.0 | 9.0/1.3 | 14.1/6.4 | 0.0/0.0 | +48.7 [+34.6, +61.5] | -7.7 [-21.8, +3.8] | +41.0 [+28.2, +53.8] |
| settled | right-coded | 177 | 177 | 76.3/12.4 | 12.4/76.3 | 0.6/1.1 | 10.7/11.3 | 0.6/0.0 | +63.8 [+53.7, +73.4] | +0.6 [-4.5, +6.2] | +64.4 [+54.8, +74.0] |
| settled | uncoded | 219 | 219 | 72.6/16.0 | 15.5/76.7 | 4.6/4.1 | 11.9/7.3 | 0.0/0.0 | +61.2 [+53.0, +69.9] | -4.6 [-9.6, +0.5] | +56.6 [+47.5, +65.8] |
| settled | contested x conservative | 122 | 122 | 63.9/5.7 | 23.0/86.1 | 4.1/0.0 | 12.3/8.2 | 0.8/0.0 | +63.1 [+54.1, +72.1] | -4.1 [-11.5, +3.3] | +59.0 [+50.0, +68.0] |
| settled | contested x liberal | 122 | 122 | 63.9/8.2 | 23.8/82.8 | 3.3/2.5 | 12.3/9.0 | 0.0/0.0 | +59.0 [+50.0, +68.0] | -3.3 [-9.8, +3.3] | +55.7 [+46.7, +64.8] |

#### answer length, mean words, original / treated

- consensus | all: 150 / 188
- contested | all: 234 / 249
- settled | all: 214 / 231
- settled | contested: 218 / 235
- settled | uncontested: 201 / 218
- settled | left-coded: 232 / 248
- settled | right-coded: 210 / 228
- settled | uncoded: 211 / 229
- settled | contested x conservative: 219 / 236
- settled | contested x liberal: 217 / 234

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| liberal | 60 | 96.7/100.0 | 3.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.03/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
