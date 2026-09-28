# GPT-4.1: journalist's balance norm against the original, settled and consensus items, version 1

original: <outputs>/gpt-4.1/original/judged_main_v1.jsonl

condition journalist_prompt: <outputs>/gpt-4.1/journalist_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: journalist's balance norm

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 95.0/40.0 | 0.0/60.0 | 0.0/5.0 | 5.0/0.0 | 0.0/0.0 | +60.0 [+40.0, +80.0] | -5.0 [-15.0, +0.0] | +55.0 [+35.0, +75.0] |
| consensus | variant=none | 20 | 20 | 95.0/40.0 | 0.0/60.0 | 0.0/5.0 | 5.0/0.0 | 0.0/0.0 | +60.0 [+40.0, +80.0] | -5.0 [-15.0, +0.0] | +55.0 [+35.0, +75.0] |
| settled | all | 474 | 474 | 98.3/23.2 | 1.1/76.8 | 3.0/5.7 | 0.6/0.0 | 0.0/0.0 | +75.7 [+70.0, +81.6] | -0.6 [-1.5, +0.0] | +75.1 [+69.2, +80.8] |
| settled | variant=conservative | 158 | 158 | 98.1/21.5 | 0.6/78.5 | 7.0/7.0 | 1.3/0.0 | 0.0/0.0 | +77.8 [+71.5, +84.8] | -1.3 [-3.2, +0.0] | +76.6 [+70.3, +84.2] |
| settled | variant=liberal | 158 | 158 | 99.4/27.2 | 0.6/72.8 | 1.9/6.3 | 0.0/0.0 | 0.0/0.0 | +72.2 [+65.2, +79.1] | +0.0 [+0.0, +0.0] | +72.2 [+65.2, +79.1] |
| settled | variant=none | 158 | 158 | 97.5/20.9 | 1.9/79.1 | 0.0/3.8 | 0.6/0.0 | 0.0/0.0 | +77.2 [+70.9, +83.5] | -0.6 [-1.9, +0.0] | +76.6 [+69.6, +83.5] |
| settled | contested | 366 | 366 | 98.1/15.8 | 1.4/84.2 | 3.0/5.2 | 0.5/0.0 | 0.0/0.0 | +82.8 [+76.8, +88.3] | -0.5 [-1.4, +0.0] | +82.2 [+76.2, +87.7] |
| settled | uncontested | 108 | 108 | 99.1/48.1 | 0.0/51.9 | 2.8/7.4 | 0.9/0.0 | 0.0/0.0 | +51.9 [+38.0, +64.8] | -0.9 [-2.8, +0.0] | +50.9 [+37.0, +64.8] |
| settled | left-coded | 117 | 117 | 95.7/9.4 | 3.4/90.6 | 2.6/6.8 | 0.9/0.0 | 0.0/0.0 | +87.2 [+77.8, +94.9] | -0.9 [-2.6, +0.0] | +86.3 [+76.1, +94.0] |
| settled | right-coded | 177 | 177 | 99.4/19.2 | 0.0/80.8 | 4.0/5.6 | 0.6/0.0 | 0.0/0.0 | +80.8 [+71.8, +89.3] | -0.6 [-1.7, +0.0] | +80.2 [+70.6, +88.7] |
| settled | uncoded | 180 | 180 | 98.9/36.1 | 0.6/63.9 | 2.2/5.0 | 0.6/0.0 | 0.0/0.0 | +63.3 [+54.4, +73.3] | -0.6 [-1.7, +0.0] | +62.8 [+53.3, +72.8] |
| settled | contested x conservative | 122 | 122 | 98.4/13.9 | 0.8/86.1 | 8.2/5.7 | 0.8/0.0 | 0.0/0.0 | +85.2 [+78.7, +91.0] | -0.8 [-2.5, +0.0] | +84.4 [+77.9, +91.0] |
| settled | contested x liberal | 122 | 122 | 99.2/18.9 | 0.8/81.1 | 0.8/6.6 | 0.0/0.0 | 0.0/0.0 | +80.3 [+73.0, +86.9] | +0.0 [+0.0, +0.0] | +80.3 [+73.0, +86.9] |

#### answer length, mean words, original / treated

- consensus | all: 115 / 198
- contested | all: 227 / 245
- settled | all: 167 / 217
- settled | contested: 179 / 226
- settled | uncontested: 127 / 185
- settled | left-coded: 209 / 235
- settled | right-coded: 161 / 222
- settled | uncoded: 146 / 200
- settled | contested x conservative: 186 / 228
- settled | contested x liberal: 172 / 223

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 83.3/100.0 | 0.0/0.0 | 16.7/0.0 | 0.0/0.0 | +0.34/+0.00 |
| liberal | 60 | 65.0/100.0 | 35.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.45/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
