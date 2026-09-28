# Llama-3.1-8B: neutrality prompt against the original, settled and consensus items, version 1

original: <outputs>/llama-3.1-8b/original/judged_main_v1.jsonl

condition neutrality_prompt: <outputs>/llama-3.1-8b/neutrality_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 45.0/5.0 | 10.0/65.0 | 0.0/0.0 | 40.0/30.0 | 5.0/0.0 | +55.0 [+35.0, +75.0] | -10.0 [-30.0, +10.0] | +45.0 [+25.0, +65.0] |
| consensus | variant=none | 20 | 20 | 45.0/5.0 | 10.0/65.0 | 0.0/0.0 | 40.0/30.0 | 5.0/0.0 | +55.0 [+35.0, +75.0] | -10.0 [-30.0, +10.0] | +45.0 [+25.0, +65.0] |
| settled | all | 474 | 474 | 71.9/7.6 | 22.2/90.9 | 5.1/0.4 | 5.7/1.5 | 0.2/0.0 | +68.8 [+63.3, +74.3] | -4.2 [-7.4, -1.5] | +64.6 [+58.4, +70.7] |
| settled | variant=conservative | 158 | 158 | 71.5/7.0 | 24.1/91.8 | 10.1/0.6 | 4.4/1.3 | 0.0/0.0 | +67.7 [+60.1, +75.3] | -3.2 [-7.0, +0.0] | +64.6 [+57.0, +72.2] |
| settled | variant=liberal | 158 | 158 | 70.9/6.3 | 24.1/91.8 | 2.5/0.6 | 5.1/1.9 | 0.0/0.0 | +67.7 [+60.1, +75.3] | -3.2 [-7.6, +0.6] | +64.6 [+57.0, +72.2] |
| settled | variant=none | 158 | 158 | 73.4/9.5 | 18.4/89.2 | 2.5/0.0 | 7.6/1.3 | 0.6/0.0 | +70.9 [+63.3, +77.8] | -6.3 [-10.8, -1.9] | +64.6 [+57.0, +72.2] |
| settled | contested | 366 | 366 | 65.3/4.1 | 27.3/94.5 | 4.6/0.0 | 7.1/1.4 | 0.3/0.0 | +67.2 [+60.7, +73.5] | -5.7 [-9.6, -2.2] | +61.5 [+54.6, +68.6] |
| settled | uncontested | 108 | 108 | 94.4/19.4 | 4.6/78.7 | 6.5/1.9 | 0.9/1.9 | 0.0/0.0 | +74.1 [+63.9, +84.3] | +0.9 [-2.8, +5.6] | +75.0 [+63.9, +85.2] |
| settled | left-coded | 117 | 117 | 35.9/0.0 | 48.7/99.1 | 5.1/0.0 | 15.4/0.9 | 0.0/0.0 | +50.4 [+39.3, +61.5] | -14.5 [-23.9, -6.8] | +35.9 [+23.9, +47.9] |
| settled | right-coded | 177 | 177 | 84.7/6.8 | 11.9/91.0 | 4.0/0.0 | 2.8/2.3 | 0.6/0.0 | +79.1 [+71.2, +86.4] | -0.6 [-4.0, +2.8] | +78.5 [+70.6, +86.4] |
| settled | uncoded | 180 | 180 | 82.8/13.3 | 15.0/85.6 | 6.1/1.1 | 2.2/1.1 | 0.0/0.0 | +70.6 [+61.1, +78.9] | -1.1 [-5.0, +2.8] | +69.4 [+58.9, +78.3] |
| settled | contested x conservative | 122 | 122 | 64.8/2.5 | 29.5/96.7 | 9.8/0.0 | 5.7/0.8 | 0.0/0.0 | +67.2 [+58.2, +75.4] | -4.9 [-9.8, -0.8] | +62.3 [+53.3, +71.3] |
| settled | contested x liberal | 122 | 122 | 63.9/3.3 | 29.5/95.1 | 2.5/0.0 | 6.6/1.6 | 0.0/0.0 | +65.6 [+56.6, +73.8] | -4.9 [-9.8, +0.0] | +60.7 [+51.6, +69.7] |

#### answer length, mean words, original / treated

- consensus | all: 131 / 221
- contested | all: 231 / 249
- settled | all: 206 / 233
- settled | contested: 211 / 238
- settled | uncontested: 189 / 218
- settled | left-coded: 227 / 246
- settled | right-coded: 199 / 232
- settled | uncoded: 198 / 226
- settled | contested x conservative: 211 / 237
- settled | contested x liberal: 212 / 238

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/100.0 | 0.0/0.0 | 3.3/0.0 | 0.0/0.0 | +0.07/+0.00 |
| liberal | 60 | 91.7/100.0 | 8.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.15/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
