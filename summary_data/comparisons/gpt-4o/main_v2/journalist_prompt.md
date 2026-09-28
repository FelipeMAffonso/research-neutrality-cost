# GPT-4o: journalist's balance norm against the original, settled and consensus items, version 2

original: <outputs>/gpt-4o/original/judged_main_v2.jsonl

condition journalist_prompt: <outputs>/gpt-4o/journalist_prompt/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: journalist's balance norm

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 80.0/50.0 | 0.0/30.0 | 0.0/20.0 | 15.0/10.0 | 5.0/10.0 | +30.0 [+10.0, +50.0] | -5.0 [-15.0, +0.0] | +25.0 [+5.0, +50.0] |
| consensus | variant=none | 20 | 20 | 80.0/50.0 | 0.0/30.0 | 0.0/20.0 | 15.0/10.0 | 5.0/10.0 | +30.0 [+10.0, +50.0] | -5.0 [-15.0, +0.0] | +25.0 [+5.0, +50.0] |
| settled | all | 474 | 474 | 92.8/27.8 | 6.8/72.2 | 16.7/10.3 | 0.4/0.0 | 0.0/0.0 | +65.4 [+59.1, +71.9] | -0.4 [-1.3, +0.0] | +65.0 [+58.6, +71.5] |
| settled | variant=conservative | 158 | 158 | 92.4/27.8 | 7.0/72.2 | 19.6/13.9 | 0.6/0.0 | 0.0/0.0 | +65.2 [+57.6, +72.8] | -0.6 [-1.9, +0.0] | +64.6 [+57.0, +72.2] |
| settled | variant=liberal | 158 | 158 | 93.0/27.8 | 6.3/72.2 | 17.7/10.1 | 0.6/0.0 | 0.0/0.0 | +65.8 [+58.2, +74.1] | -0.6 [-1.9, +0.0] | +65.2 [+57.6, +73.4] |
| settled | variant=none | 158 | 158 | 93.0/27.8 | 7.0/72.2 | 12.7/7.0 | 0.0/0.0 | 0.0/0.0 | +65.2 [+58.2, +72.8] | +0.0 [+0.0, +0.0] | +65.2 [+58.2, +72.8] |
| settled | contested | 366 | 366 | 90.7/17.8 | 8.7/82.2 | 18.9/8.5 | 0.5/0.0 | 0.0/0.0 | +73.5 [+66.7, +80.3] | -0.5 [-1.6, +0.0] | +73.0 [+65.8, +79.8] |
| settled | uncontested | 108 | 108 | 100.0/62.0 | 0.0/38.0 | 9.3/16.7 | 0.0/0.0 | 0.0/0.0 | +38.0 [+25.0, +50.9] | +0.0 [+0.0, +0.0] | +38.0 [+25.0, +50.9] |
| settled | left-coded | 78 | 78 | 82.1/12.8 | 15.4/87.2 | 41.0/11.5 | 2.6/0.0 | 0.0/0.0 | +71.8 [+57.7, +85.9] | -2.6 [-7.7, +0.0] | +69.2 [+53.8, +84.6] |
| settled | right-coded | 177 | 177 | 97.2/24.9 | 2.8/75.1 | 10.7/11.9 | 0.0/0.0 | 0.0/0.0 | +72.3 [+63.3, +81.4] | +0.0 [+0.0, +0.0] | +72.3 [+63.3, +81.4] |
| settled | uncoded | 219 | 219 | 93.2/35.6 | 6.8/64.4 | 12.8/8.7 | 0.0/0.0 | 0.0/0.0 | +57.5 [+47.5, +67.1] | +0.0 [+0.0, +0.0] | +57.5 [+47.5, +67.1] |
| settled | contested x conservative | 122 | 122 | 90.2/14.8 | 9.0/85.2 | 21.3/10.7 | 0.8/0.0 | 0.0/0.0 | +76.2 [+68.9, +83.6] | -0.8 [-2.5, +0.0] | +75.4 [+68.0, +82.8] |
| settled | contested x liberal | 122 | 122 | 91.0/18.9 | 8.2/81.1 | 20.5/7.4 | 0.8/0.0 | 0.0/0.0 | +73.0 [+64.8, +81.1] | -0.8 [-2.5, +0.0] | +72.1 [+63.9, +80.3] |

#### answer length, mean words, original / treated

- consensus | all: 80 / 143
- contested | all: 238 / 246
- settled | all: 130 / 200
- settled | contested: 139 / 208
- settled | uncontested: 99 / 174
- settled | left-coded: 178 / 218
- settled | right-coded: 118 / 202
- settled | uncoded: 122 / 193
- settled | contested x conservative: 133 / 205
- settled | contested x liberal: 135 / 202

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 70.0/100.0 | 0.0/0.0 | 30.0/0.0 | 0.0/0.0 | +0.52/+0.00 |
| liberal | 60 | 53.3/100.0 | 46.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.60/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
