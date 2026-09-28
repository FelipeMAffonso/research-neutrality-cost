# Llama-3.1-8B: neutrality prompt against the original, settled and consensus items, version 2

original: <outputs>/llama-3.1-8b/original/judged_main_v2.jsonl

condition neutrality_prompt: <outputs>/llama-3.1-8b/neutrality_prompt/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 55.0/20.0 | 0.0/55.0 | 0.0/0.0 | 30.0/25.0 | 15.0/0.0 | +55.0 [+35.0, +75.0] | -5.0 [-25.0, +10.0] | +50.0 [+30.0, +70.0] |
| consensus | variant=none | 20 | 20 | 55.0/20.0 | 0.0/55.0 | 0.0/0.0 | 30.0/25.0 | 15.0/0.0 | +55.0 [+35.0, +75.0] | -5.0 [-25.0, +10.0] | +50.0 [+30.0, +70.0] |
| settled | all | 474 | 474 | 71.7/7.0 | 21.7/91.4 | 4.6/0.2 | 6.1/1.7 | 0.4/0.0 | +69.6 [+64.1, +75.1] | -4.4 [-7.0, -1.9] | +65.2 [+59.3, +71.1] |
| settled | variant=conservative | 158 | 158 | 72.8/7.6 | 21.5/90.5 | 9.5/0.6 | 5.7/1.9 | 0.0/0.0 | +69.0 [+61.4, +75.9] | -3.8 [-7.6, +0.0] | +65.2 [+57.6, +72.8] |
| settled | variant=liberal | 158 | 158 | 70.9/5.7 | 24.7/92.4 | 1.9/0.0 | 4.4/1.9 | 0.0/0.0 | +67.7 [+59.5, +75.3] | -2.5 [-6.3, +1.3] | +65.2 [+57.6, +72.8] |
| settled | variant=none | 158 | 158 | 71.5/7.6 | 19.0/91.1 | 2.5/0.0 | 8.2/1.3 | 1.3/0.0 | +72.2 [+65.2, +79.1] | -7.0 [-11.4, -2.5] | +65.2 [+57.6, +72.8] |
| settled | contested | 366 | 366 | 65.0/3.8 | 26.8/94.5 | 4.4/0.0 | 7.7/1.6 | 0.5/0.0 | +67.8 [+61.2, +74.0] | -6.0 [-9.3, -3.0] | +61.7 [+55.2, +68.6] |
| settled | uncontested | 108 | 108 | 94.4/17.6 | 4.6/80.6 | 5.6/0.9 | 0.9/1.9 | 0.0/0.0 | +75.9 [+64.8, +85.2] | +0.9 [-2.8, +5.6] | +76.9 [+65.7, +87.0] |
| settled | left-coded | 78 | 78 | 44.9/0.0 | 41.0/98.7 | 7.7/0.0 | 12.8/1.3 | 1.3/0.0 | +57.7 [+44.9, +69.2] | -11.5 [-20.5, -3.8] | +46.2 [+33.3, +59.0] |
| settled | right-coded | 177 | 177 | 81.4/7.3 | 12.4/89.8 | 4.5/0.0 | 5.6/2.8 | 0.6/0.0 | +77.4 [+68.9, +85.3] | -2.8 [-6.8, +0.6] | +74.6 [+66.1, +83.6] |
| settled | uncoded | 219 | 219 | 73.5/9.1 | 22.4/90.0 | 3.7/0.5 | 4.1/0.9 | 0.0/0.0 | +67.6 [+58.4, +76.3] | -3.2 [-6.8, +0.5] | +64.4 [+54.3, +73.5] |
| settled | contested x conservative | 122 | 122 | 66.4/3.3 | 26.2/95.1 | 9.8/0.0 | 7.4/1.6 | 0.0/0.0 | +68.9 [+60.7, +77.0] | -5.7 [-10.7, -1.6] | +63.1 [+54.1, +72.1] |
| settled | contested x liberal | 122 | 122 | 63.9/3.3 | 30.3/95.1 | 1.6/0.0 | 5.7/1.6 | 0.0/0.0 | +64.8 [+56.6, +73.0] | -4.1 [-9.0, +0.8] | +60.7 [+52.5, +68.9] |

#### answer length, mean words, original / treated

- consensus | all: 118 / 194
- contested | all: 231 / 249
- settled | all: 205 / 233
- settled | contested: 209 / 237
- settled | uncontested: 189 / 218
- settled | left-coded: 228 / 247
- settled | right-coded: 197 / 231
- settled | uncoded: 203 / 229
- settled | contested x conservative: 210 / 235
- settled | contested x liberal: 210 / 238

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/100.0 | 0.0/0.0 | 3.3/0.0 | 0.0/0.0 | +0.07/+0.00 |
| liberal | 60 | 91.7/100.0 | 8.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.15/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
