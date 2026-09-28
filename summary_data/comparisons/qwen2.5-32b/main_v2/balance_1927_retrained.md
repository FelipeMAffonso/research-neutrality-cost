# Qwen2.5-32B: balance fine-tuning, 1,927 answers (trained a second time) against the original, settled and consensus items, version 2

original: <outputs>/qwen2.5-32b/original/judged_main_v2.jsonl

condition balance_1927_retrained: <outputs>/qwen2.5-32b/balance_1927_retrained/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers (trained a second time)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 65.0/15.0 | 10.0/75.0 | 5.0/15.0 | 25.0/5.0 | 0.0/5.0 | +65.0 [+45.0, +85.0] | -20.0 [-40.0, -5.0] | +45.0 [+25.0, +65.0] |
| consensus | variant=none | 20 | 20 | 65.0/15.0 | 10.0/75.0 | 5.0/15.0 | 25.0/5.0 | 0.0/5.0 | +65.0 [+45.0, +85.0] | -20.0 [-40.0, -5.0] | +45.0 [+25.0, +65.0] |
| settled | all | 474 | 474 | 86.7/20.9 | 11.0/78.9 | 22.8/12.0 | 2.3/0.2 | 0.0/0.0 | +67.9 [+62.0, +73.8] | -2.1 [-3.8, -0.6] | +65.8 [+59.7, +72.2] |
| settled | variant=conservative | 158 | 158 | 86.7/22.8 | 10.8/77.2 | 25.3/17.1 | 2.5/0.0 | 0.0/0.0 | +66.5 [+59.5, +74.1] | -2.5 [-5.1, -0.6] | +63.9 [+56.3, +71.5] |
| settled | variant=liberal | 158 | 158 | 88.0/25.9 | 8.9/74.1 | 25.9/11.4 | 3.2/0.0 | 0.0/0.0 | +65.2 [+57.6, +72.8] | -3.2 [-6.3, -0.6] | +62.0 [+54.4, +70.3] |
| settled | variant=none | 158 | 158 | 85.4/13.9 | 13.3/85.4 | 17.1/7.6 | 1.3/0.6 | 0.0/0.0 | +72.2 [+65.2, +79.1] | -0.6 [-2.5, +1.3] | +71.5 [+64.6, +79.1] |
| settled | contested | 366 | 366 | 84.7/8.5 | 14.2/91.5 | 24.3/6.0 | 1.1/0.0 | 0.0/0.0 | +77.3 [+71.6, +82.8] | -1.1 [-2.5, +0.0] | +76.2 [+69.9, +82.0] |
| settled | uncontested | 108 | 108 | 93.5/63.0 | 0.0/36.1 | 17.6/32.4 | 6.5/0.9 | 0.0/0.0 | +36.1 [+24.1, +48.1] | -5.6 [-11.1, -0.9] | +30.6 [+16.7, +44.4] |
| settled | left-coded | 78 | 78 | 70.5/1.3 | 28.2/98.7 | 37.2/0.0 | 1.3/0.0 | 0.0/0.0 | +70.5 [+56.4, +83.3] | -1.3 [-3.8, +0.0] | +69.2 [+53.8, +83.3] |
| settled | right-coded | 177 | 177 | 94.4/14.1 | 4.0/85.9 | 20.3/10.7 | 1.7/0.0 | 0.0/0.0 | +81.9 [+75.1, +88.7] | -1.7 [-4.5, +0.0] | +80.2 [+72.9, +87.6] |
| settled | uncoded | 219 | 219 | 86.3/33.3 | 10.5/66.2 | 19.6/17.4 | 3.2/0.5 | 0.0/0.0 | +55.7 [+46.6, +64.8] | -2.7 [-5.5, -0.5] | +53.0 [+42.9, +63.0] |
| settled | contested x conservative | 122 | 122 | 84.4/9.0 | 13.9/91.0 | 27.0/6.6 | 1.6/0.0 | 0.0/0.0 | +77.0 [+69.7, +84.4] | -1.6 [-4.1, +0.0] | +75.4 [+67.2, +82.8] |
| settled | contested x liberal | 122 | 122 | 86.9/12.3 | 11.5/87.7 | 26.2/7.4 | 1.6/0.0 | 0.0/0.0 | +76.2 [+68.0, +83.6] | -1.6 [-4.1, +0.0] | +74.6 [+66.4, +82.0] |

#### answer length, mean words, original / treated

- consensus | all: 121 / 155
- contested | all: 241 / 182
- settled | all: 162 / 167
- settled | contested: 170 / 172
- settled | uncontested: 136 / 151
- settled | left-coded: 205 / 185
- settled | right-coded: 150 / 166
- settled | uncoded: 157 / 162
- settled | contested x conservative: 177 / 168
- settled | contested x liberal: 161 / 164

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 63.3/100.0 | 0.0/0.0 | 36.7/0.0 | 0.0/0.0 | +0.67/+0.02 |
| liberal | 60 | 76.7/100.0 | 23.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.28/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
