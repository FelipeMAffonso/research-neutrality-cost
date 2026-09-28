# Llama-3.2-3B: neutrality prompt against the original, settled and consensus items, version 1

original: <outputs>/llama-3.2-3b/original/judged_main_v1.jsonl

condition neutrality_prompt: <outputs>/llama-3.2-3b/neutrality_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 35.0/10.0 | 0.0/40.0 | 0.0/0.0 | 65.0/50.0 | 0.0/0.0 | +40.0 [+20.0, +60.0] | -15.0 [-35.0, +0.0] | +25.0 [+5.0, +45.0] |
| consensus | variant=none | 20 | 20 | 35.0/10.0 | 0.0/40.0 | 0.0/0.0 | 65.0/50.0 | 0.0/0.0 | +40.0 [+20.0, +60.0] | -15.0 [-35.0, +0.0] | +25.0 [+5.0, +45.0] |
| settled | all | 474 | 474 | 68.1/12.2 | 20.0/79.7 | 4.4/3.2 | 11.4/8.0 | 0.4/0.0 | +59.7 [+53.8, +65.8] | -3.4 [-7.4, +0.2] | +56.3 [+50.2, +62.7] |
| settled | variant=conservative | 158 | 158 | 69.6/10.8 | 17.7/81.6 | 3.8/3.2 | 11.4/7.6 | 1.3/0.0 | +63.9 [+55.7, +72.2] | -3.8 [-9.5, +1.9] | +60.1 [+51.9, +68.4] |
| settled | variant=liberal | 158 | 158 | 72.8/12.0 | 20.3/81.6 | 5.7/2.5 | 7.0/6.3 | 0.0/0.0 | +61.4 [+53.8, +69.6] | -0.6 [-5.1, +3.8] | +60.8 [+53.2, +69.0] |
| settled | variant=none | 158 | 158 | 62.0/13.9 | 22.2/75.9 | 3.8/3.8 | 15.8/10.1 | 0.0/0.0 | +53.8 [+45.6, +62.7] | -5.7 [-12.0, +0.0] | +48.1 [+39.9, +56.3] |
| settled | contested | 366 | 366 | 60.9/7.9 | 25.1/83.9 | 3.8/1.6 | 13.4/8.2 | 0.5/0.0 | +58.7 [+51.9, +65.6] | -5.2 [-9.8, -0.8] | +53.6 [+47.0, +60.4] |
| settled | uncontested | 108 | 108 | 92.6/26.9 | 2.8/65.7 | 6.5/8.3 | 4.6/7.4 | 0.0/0.0 | +63.0 [+49.1, +75.9] | +2.8 [-2.8, +8.3] | +65.7 [+51.9, +78.7] |
| settled | left-coded | 117 | 117 | 35.0/1.7 | 48.7/94.0 | 8.5/0.9 | 15.4/4.3 | 0.9/0.0 | +45.3 [+34.2, +56.4] | -11.1 [-22.2, -0.9] | +34.2 [+24.8, +43.6] |
| settled | right-coded | 177 | 177 | 76.3/11.9 | 11.9/78.0 | 1.1/1.1 | 11.3/10.2 | 0.6/0.0 | +66.1 [+57.1, +75.1] | -1.1 [-5.6, +4.0] | +65.0 [+55.4, +74.0] |
| settled | uncoded | 180 | 180 | 81.7/19.4 | 9.4/72.2 | 5.0/6.7 | 8.9/8.3 | 0.0/0.0 | +62.8 [+52.2, +72.2] | -0.6 [-6.7, +5.0] | +62.2 [+51.7, +72.2] |
| settled | contested x conservative | 122 | 122 | 63.9/6.6 | 22.1/85.2 | 3.3/0.8 | 12.3/8.2 | 1.6/0.0 | +63.1 [+53.3, +72.1] | -4.1 [-10.7, +1.6] | +59.0 [+49.2, +68.0] |
| settled | contested x liberal | 122 | 122 | 64.8/9.0 | 26.2/85.2 | 4.9/3.3 | 9.0/5.7 | 0.0/0.0 | +59.0 [+50.0, +68.9] | -3.3 [-8.2, +2.5] | +55.7 [+46.7, +64.8] |

#### answer length, mean words, original / treated

- consensus | all: 159 / 210
- contested | all: 234 / 250
- settled | all: 214 / 232
- settled | contested: 219 / 236
- settled | uncontested: 199 / 218
- settled | left-coded: 231 / 249
- settled | right-coded: 212 / 229
- settled | uncoded: 205 / 224
- settled | contested x conservative: 222 / 236
- settled | contested x liberal: 217 / 235

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| liberal | 60 | 98.3/100.0 | 1.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.02/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
