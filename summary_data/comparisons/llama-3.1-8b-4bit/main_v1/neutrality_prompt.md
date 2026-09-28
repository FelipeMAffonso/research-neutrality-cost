# Llama-3.1-8B, preliminary 4-bit run: neutrality prompt against the original, settled and consensus items, version 1

original: <outputs>/llama-3.1-8b-4bit/original/judged_main_v1.jsonl

condition neutrality_prompt: <outputs>/llama-3.1-8b-4bit/neutrality_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 60.0/10.0 | 0.0/60.0 | 0.0/5.0 | 35.0/30.0 | 5.0/0.0 | +60.0 [+40.0, +80.0] | -5.0 [-35.0, +25.0] | +55.0 [+35.0, +75.0] |
| consensus | variant=none | 20 | 20 | 60.0/10.0 | 0.0/60.0 | 0.0/5.0 | 35.0/30.0 | 5.0/0.0 | +60.0 [+40.0, +80.0] | -5.0 [-35.0, +25.0] | +55.0 [+35.0, +75.0] |
| settled | all | 474 | 474 | 73.0/8.0 | 21.3/90.3 | 5.9/1.9 | 5.1/1.7 | 0.6/0.0 | +69.0 [+63.3, +74.5] | -3.4 [-6.5, -0.6] | +65.6 [+59.7, +71.7] |
| settled | variant=conservative | 158 | 158 | 71.5/7.6 | 22.8/91.1 | 7.6/1.3 | 4.4/1.3 | 1.3/0.0 | +68.4 [+61.4, +75.3] | -3.2 [-7.0, +0.6] | +65.2 [+57.6, +72.8] |
| settled | variant=liberal | 158 | 158 | 73.4/7.0 | 22.8/92.4 | 5.7/1.9 | 3.2/0.6 | 0.6/0.0 | +69.6 [+62.7, +76.6] | -2.5 [-5.7, +0.0] | +67.1 [+59.5, +74.7] |
| settled | variant=none | 158 | 158 | 74.1/9.5 | 18.4/87.3 | 4.4/2.5 | 7.6/3.2 | 0.0/0.0 | +69.0 [+61.4, +76.6] | -4.4 [-9.5, +0.6] | +64.6 [+57.0, +72.2] |
| settled | contested | 366 | 366 | 66.7/5.5 | 27.3/93.2 | 6.3/1.6 | 5.5/1.4 | 0.5/0.0 | +65.8 [+59.8, +72.1] | -4.1 [-7.4, -1.1] | +61.7 [+55.5, +68.6] |
| settled | uncontested | 108 | 108 | 94.4/16.7 | 0.9/80.6 | 4.6/2.8 | 3.7/2.8 | 0.9/0.0 | +79.6 [+68.5, +88.9] | -0.9 [-8.3, +5.6] | +78.7 [+63.9, +89.8] |
| settled | left-coded | 117 | 117 | 45.3/0.9 | 44.4/95.7 | 10.3/0.0 | 9.4/3.4 | 0.9/0.0 | +51.3 [+41.0, +61.5] | -6.0 [-13.7, +2.6] | +45.3 [+33.3, +57.3] |
| settled | right-coded | 177 | 177 | 80.2/6.8 | 15.3/92.7 | 2.8/2.3 | 4.0/0.6 | 0.6/0.0 | +77.4 [+68.9, +85.3] | -3.4 [-7.3, -0.6] | +74.0 [+66.1, +81.9] |
| settled | uncoded | 180 | 180 | 83.9/13.9 | 12.2/84.4 | 6.1/2.8 | 3.3/1.7 | 0.6/0.0 | +72.2 [+62.8, +81.1] | -1.7 [-6.1, +2.8] | +70.6 [+59.4, +81.1] |
| settled | contested x conservative | 122 | 122 | 65.6/2.5 | 29.5/96.7 | 7.4/0.8 | 4.1/0.8 | 0.8/0.0 | +67.2 [+59.0, +75.4] | -3.3 [-7.4, +0.8] | +63.9 [+55.7, +72.1] |
| settled | contested x liberal | 122 | 122 | 67.2/5.7 | 28.7/94.3 | 6.6/1.6 | 3.3/0.0 | 0.8/0.0 | +65.6 [+57.4, +73.8] | -3.3 [-6.6, -0.8] | +62.3 [+54.1, +71.3] |

#### answer length, mean words, original / treated

- consensus | all: 96 / 216
- contested | all: 234 / 245
- settled | all: 203 / 233
- settled | contested: 208 / 236
- settled | uncontested: 185 / 223
- settled | left-coded: 228 / 242
- settled | right-coded: 193 / 230
- settled | uncoded: 196 / 230
- settled | contested x conservative: 214 / 237
- settled | contested x liberal: 205 / 234

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 91.7/100.0 | 0.0/0.0 | 8.3/0.0 | 0.0/0.0 | +0.18/+0.00 |
| liberal | 60 | 85.0/100.0 | 15.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.23/+0.00 |
| none | 60 | 95.0/98.3 | 5.0/1.7 | 0.0/0.0 | 0.0/0.0 | -0.07/-0.02 |
