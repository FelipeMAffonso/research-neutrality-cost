# GPT-4.1: journalist's balance norm against the original, settled and consensus items, version 2

original: <outputs>/gpt-4.1/original/judged_main_v2.jsonl

condition journalist_prompt: <outputs>/gpt-4.1/journalist_prompt/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: journalist's balance norm

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 90.0/40.0 | 0.0/50.0 | 0.0/15.0 | 10.0/5.0 | 0.0/5.0 | +50.0 [+30.0, +70.0] | -5.0 [-15.0, +0.0] | +45.0 [+25.0, +65.0] |
| consensus | variant=none | 20 | 20 | 90.0/40.0 | 0.0/50.0 | 0.0/15.0 | 10.0/5.0 | 0.0/5.0 | +50.0 [+30.0, +70.0] | -5.0 [-15.0, +0.0] | +45.0 [+25.0, +65.0] |
| settled | all | 474 | 474 | 98.5/24.1 | 0.8/75.9 | 2.7/5.7 | 0.6/0.0 | 0.0/0.0 | +75.1 [+69.6, +80.8] | -0.6 [-1.5, +0.0] | +74.5 [+68.8, +80.4] |
| settled | variant=conservative | 158 | 158 | 98.1/23.4 | 0.6/76.6 | 6.3/7.0 | 1.3/0.0 | 0.0/0.0 | +75.9 [+69.6, +82.9] | -1.3 [-3.2, +0.0] | +74.7 [+67.7, +81.6] |
| settled | variant=liberal | 158 | 158 | 99.4/26.6 | 0.6/73.4 | 1.9/7.0 | 0.0/0.0 | 0.0/0.0 | +72.8 [+65.8, +79.7] | +0.0 [+0.0, +0.0] | +72.8 [+65.8, +79.7] |
| settled | variant=none | 158 | 158 | 98.1/22.2 | 1.3/77.8 | 0.0/3.2 | 0.6/0.0 | 0.0/0.0 | +76.6 [+70.3, +83.5] | -0.6 [-1.9, +0.0] | +75.9 [+69.0, +82.9] |
| settled | contested | 366 | 366 | 98.4/16.7 | 1.1/83.3 | 2.7/5.5 | 0.5/0.0 | 0.0/0.0 | +82.2 [+76.5, +87.7] | -0.5 [-1.4, +0.0] | +81.7 [+76.0, +87.2] |
| settled | uncontested | 108 | 108 | 99.1/49.1 | 0.0/50.9 | 2.8/6.5 | 0.9/0.0 | 0.0/0.0 | +50.9 [+38.0, +63.9] | -0.9 [-2.8, +0.0] | +50.0 [+36.1, +63.0] |
| settled | left-coded | 78 | 78 | 94.9/15.4 | 3.8/84.6 | 3.8/11.5 | 1.3/0.0 | 0.0/0.0 | +80.8 [+67.9, +92.3] | -1.3 [-3.8, +0.0] | +79.5 [+66.7, +91.0] |
| settled | right-coded | 177 | 177 | 99.4/19.8 | 0.0/80.2 | 3.4/5.6 | 0.6/0.0 | 0.0/0.0 | +80.2 [+70.6, +88.7] | -0.6 [-1.7, +0.0] | +79.7 [+70.1, +88.1] |
| settled | uncoded | 219 | 219 | 99.1/30.6 | 0.5/69.4 | 1.8/3.7 | 0.5/0.0 | 0.0/0.0 | +68.9 [+59.4, +77.6] | -0.5 [-1.4, +0.0] | +68.5 [+58.9, +77.2] |
| settled | contested x conservative | 122 | 122 | 98.4/15.6 | 0.8/84.4 | 7.4/6.6 | 0.8/0.0 | 0.0/0.0 | +83.6 [+77.0, +90.2] | -0.8 [-2.5, +0.0] | +82.8 [+76.2, +89.3] |
| settled | contested x liberal | 122 | 122 | 99.2/18.0 | 0.8/82.0 | 0.8/7.4 | 0.0/0.0 | 0.0/0.0 | +81.1 [+74.6, +87.7] | +0.0 [+0.0, +0.0] | +81.1 [+74.6, +87.7] |

#### answer length, mean words, original / treated

- consensus | all: 100 / 179
- contested | all: 227 / 245
- settled | all: 167 / 216
- settled | contested: 178 / 226
- settled | uncontested: 128 / 185
- settled | left-coded: 206 / 234
- settled | right-coded: 160 / 221
- settled | uncoded: 158 / 206
- settled | contested x conservative: 186 / 227
- settled | contested x liberal: 171 / 223

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 83.3/100.0 | 0.0/0.0 | 16.7/0.0 | 0.0/0.0 | +0.34/+0.00 |
| liberal | 60 | 65.0/100.0 | 35.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.45/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
