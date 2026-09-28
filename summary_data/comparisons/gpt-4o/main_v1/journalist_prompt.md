# GPT-4o: journalist's balance norm against the original, settled and consensus items, version 1

original: <outputs>/gpt-4o/original/judged_main_v1.jsonl

condition journalist_prompt: <outputs>/gpt-4o/journalist_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: journalist's balance norm

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 85.0/40.0 | 5.0/45.0 | 5.0/25.0 | 10.0/15.0 | 0.0/0.0 | +40.0 [+20.0, +60.0] | +5.0 [+0.0, +15.0] | +45.0 [+25.0, +70.0] |
| consensus | variant=none | 20 | 20 | 85.0/40.0 | 5.0/45.0 | 5.0/25.0 | 10.0/15.0 | 0.0/0.0 | +40.0 [+20.0, +60.0] | +5.0 [+0.0, +15.0] | +45.0 [+25.0, +70.0] |
| settled | all | 474 | 474 | 92.0/26.2 | 7.8/73.8 | 18.4/10.1 | 0.2/0.0 | 0.0/0.0 | +66.0 [+59.5, +72.4] | -0.2 [-0.6, +0.0] | +65.8 [+59.3, +72.2] |
| settled | variant=conservative | 158 | 158 | 91.1/28.5 | 8.2/71.5 | 21.5/13.3 | 0.6/0.0 | 0.0/0.0 | +63.3 [+55.7, +70.9] | -0.6 [-1.9, +0.0] | +62.7 [+55.1, +70.3] |
| settled | variant=liberal | 158 | 158 | 93.0/25.3 | 7.0/74.7 | 19.6/10.1 | 0.0/0.0 | 0.0/0.0 | +67.7 [+60.1, +75.3] | +0.0 [+0.0, +0.0] | +67.7 [+60.1, +75.3] |
| settled | variant=none | 158 | 158 | 91.8/24.7 | 8.2/75.3 | 13.9/7.0 | 0.0/0.0 | 0.0/0.0 | +67.1 [+59.5, +74.1] | +0.0 [+0.0, +0.0] | +67.1 [+59.5, +74.1] |
| settled | contested | 366 | 366 | 89.6/15.6 | 10.1/84.4 | 19.9/7.9 | 0.3/0.0 | 0.0/0.0 | +74.3 [+67.8, +80.6] | -0.3 [-0.8, +0.0] | +74.0 [+67.5, +80.3] |
| settled | uncontested | 108 | 108 | 100.0/62.0 | 0.0/38.0 | 13.0/17.6 | 0.0/0.0 | 0.0/0.0 | +38.0 [+25.0, +50.9] | +0.0 [+0.0, +0.0] | +38.0 [+25.0, +50.9] |
| settled | left-coded | 117 | 117 | 76.9/8.5 | 22.2/91.5 | 33.3/7.7 | 0.9/0.0 | 0.0/0.0 | +69.2 [+57.3, +80.3] | -0.9 [-2.6, +0.0] | +68.4 [+55.6, +80.3] |
| settled | right-coded | 177 | 177 | 97.7/22.0 | 2.3/78.0 | 11.3/11.3 | 0.0/0.0 | 0.0/0.0 | +75.7 [+66.7, +84.2] | +0.0 [+0.0, +0.0] | +75.7 [+66.7, +84.2] |
| settled | uncoded | 180 | 180 | 96.1/41.7 | 3.9/58.3 | 15.6/10.6 | 0.0/0.0 | 0.0/0.0 | +54.4 [+43.9, +65.0] | +0.0 [+0.0, +0.0] | +54.4 [+43.9, +65.0] |
| settled | contested x conservative | 122 | 122 | 88.5/15.6 | 10.7/84.4 | 23.0/9.8 | 0.8/0.0 | 0.0/0.0 | +73.8 [+66.4, +81.1] | -0.8 [-2.5, +0.0] | +73.0 [+65.6, +80.3] |
| settled | contested x liberal | 122 | 122 | 91.0/15.6 | 9.0/84.4 | 22.1/7.4 | 0.0/0.0 | 0.0/0.0 | +75.4 [+67.2, +82.8] | +0.0 [+0.0, +0.0] | +75.4 [+67.2, +82.8] |

#### answer length, mean words, original / treated

- consensus | all: 85 / 156
- contested | all: 238 / 246
- settled | all: 131 / 201
- settled | contested: 141 / 209
- settled | uncontested: 99 / 173
- settled | left-coded: 176 / 218
- settled | right-coded: 120 / 203
- settled | uncoded: 113 / 188
- settled | contested x conservative: 133 / 207
- settled | contested x liberal: 137 / 204

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 70.0/100.0 | 0.0/0.0 | 30.0/0.0 | 0.0/0.0 | +0.52/+0.00 |
| liberal | 60 | 53.3/100.0 | 46.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.60/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
