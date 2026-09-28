# Qwen2.5-32B: balance fine-tuning, 1,927 answers against the original, settled and consensus items, version 2

original: <outputs>/qwen2.5-32b/original/judged_main_v2.jsonl

condition balance_1927: <outputs>/qwen2.5-32b/balance_1927/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 65.0/20.0 | 10.0/60.0 | 5.0/10.0 | 25.0/10.0 | 0.0/10.0 | +50.0 [+25.0, +75.0] | -15.0 [-40.0, +5.0] | +35.0 [+15.0, +55.0] |
| consensus | variant=none | 20 | 20 | 65.0/20.0 | 10.0/60.0 | 5.0/10.0 | 25.0/10.0 | 0.0/10.0 | +50.0 [+25.0, +75.0] | -15.0 [-40.0, +5.0] | +35.0 [+15.0, +55.0] |
| settled | all | 474 | 474 | 86.7/19.4 | 11.0/80.2 | 22.8/8.9 | 2.3/0.2 | 0.0/0.2 | +69.2 [+63.5, +74.9] | -2.1 [-4.0, -0.4] | +67.1 [+61.0, +73.4] |
| settled | variant=conservative | 158 | 158 | 86.7/19.0 | 10.8/80.4 | 25.3/10.1 | 2.5/0.0 | 0.0/0.6 | +69.6 [+62.7, +76.6] | -2.5 [-5.1, -0.6] | +67.1 [+58.9, +74.7] |
| settled | variant=liberal | 158 | 158 | 88.0/25.9 | 8.9/73.4 | 25.9/12.0 | 3.2/0.6 | 0.0/0.0 | +64.6 [+57.6, +72.2] | -2.5 [-5.7, +0.0] | +62.0 [+54.4, +70.3] |
| settled | variant=none | 158 | 158 | 85.4/13.3 | 13.3/86.7 | 17.1/4.4 | 1.3/0.0 | 0.0/0.0 | +73.4 [+66.5, +80.4] | -1.3 [-3.2, +0.0] | +72.2 [+65.2, +79.1] |
| settled | contested | 366 | 366 | 84.7/7.7 | 14.2/91.8 | 24.3/4.4 | 1.1/0.3 | 0.0/0.3 | +77.6 [+71.9, +83.1] | -0.8 [-2.5, +0.3] | +76.8 [+70.8, +82.5] |
| settled | uncontested | 108 | 108 | 93.5/59.3 | 0.0/40.7 | 17.6/24.1 | 6.5/0.0 | 0.0/0.0 | +40.7 [+28.7, +52.8] | -6.5 [-13.0, -0.9] | +34.3 [+19.4, +48.1] |
| settled | left-coded | 78 | 78 | 70.5/0.0 | 28.2/100.0 | 37.2/0.0 | 1.3/0.0 | 0.0/0.0 | +71.8 [+57.7, +84.6] | -1.3 [-3.8, +0.0] | +70.5 [+55.1, +84.6] |
| settled | right-coded | 177 | 177 | 94.4/13.0 | 4.0/86.4 | 20.3/7.3 | 1.7/0.6 | 0.0/0.0 | +82.5 [+75.1, +89.3] | -1.1 [-4.0, +1.1] | +81.4 [+73.4, +88.1] |
| settled | uncoded | 219 | 219 | 86.3/31.5 | 10.5/68.0 | 19.6/13.2 | 3.2/0.0 | 0.0/0.5 | +57.5 [+48.4, +66.2] | -3.2 [-6.4, -0.5] | +54.3 [+43.8, +64.4] |
| settled | contested x conservative | 122 | 122 | 84.4/6.6 | 13.9/92.6 | 27.0/4.9 | 1.6/0.0 | 0.0/0.8 | +78.7 [+71.3, +85.2] | -1.6 [-4.1, +0.0] | +77.0 [+68.9, +83.6] |
| settled | contested x liberal | 122 | 122 | 86.9/11.5 | 11.5/87.7 | 26.2/6.6 | 1.6/0.8 | 0.0/0.0 | +76.2 [+68.9, +83.6] | -0.8 [-4.1, +1.6] | +75.4 [+68.0, +82.8] |

#### answer length, mean words, original / treated

- consensus | all: 121 / 166
- contested | all: 241 / 182
- settled | all: 162 / 167
- settled | contested: 170 / 173
- settled | uncontested: 136 / 148
- settled | left-coded: 205 / 184
- settled | right-coded: 150 / 167
- settled | uncoded: 157 / 161
- settled | contested x conservative: 177 / 167
- settled | contested x liberal: 161 / 167

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 63.3/100.0 | 0.0/0.0 | 36.7/0.0 | 0.0/0.0 | +0.67/+0.02 |
| liberal | 60 | 76.7/100.0 | 23.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.28/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
