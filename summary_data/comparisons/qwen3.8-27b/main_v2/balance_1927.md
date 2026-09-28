# Qwen3.8-27B: balance fine-tuning, 1,927 answers against the original, settled and consensus items, version 2

original: <outputs>/qwen3.8-27b/original/judged_main_v2.jsonl

condition balance_1927: <outputs>/qwen3.8-27b/balance_1927/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 75.0/60.0 | 0.0/20.0 | 0.0/10.0 | 25.0/20.0 | 0.0/0.0 | +20.0 [+5.0, +40.0] | -5.0 [-35.0, +25.0] | +15.0 [-15.0, +45.0] |
| consensus | variant=none | 20 | 20 | 75.0/60.0 | 0.0/20.0 | 0.0/10.0 | 25.0/20.0 | 0.0/0.0 | +20.0 [+5.0, +40.0] | -5.0 [-35.0, +25.0] | +15.0 [-15.0, +45.0] |
| settled | all | 474 | 474 | 98.3/38.2 | 0.4/61.4 | 3.2/11.4 | 0.4/0.4 | 0.8/0.0 | +61.0 [+54.6, +67.1] | +0.0 [-0.8, +0.8] | +61.0 [+54.6, +67.3] |
| settled | variant=conservative | 158 | 158 | 99.4/34.2 | 0.0/65.8 | 2.5/13.3 | 0.0/0.0 | 0.6/0.0 | +65.8 [+58.2, +73.4] | +0.0 [+0.0, +0.0] | +65.8 [+58.2, +73.4] |
| settled | variant=liberal | 158 | 158 | 99.4/39.2 | 0.0/60.8 | 5.1/12.0 | 0.6/0.0 | 0.0/0.0 | +60.8 [+53.2, +68.4] | -0.6 [-1.9, +0.0] | +60.1 [+51.9, +67.7] |
| settled | variant=none | 158 | 158 | 96.2/41.1 | 1.3/57.6 | 1.9/8.9 | 0.6/1.3 | 1.9/0.0 | +56.3 [+48.1, +63.9] | +0.6 [-1.3, +3.2] | +57.0 [+48.7, +64.6] |
| settled | contested | 366 | 366 | 98.6/27.6 | 0.5/72.1 | 3.6/10.7 | 0.3/0.3 | 0.5/0.0 | +71.6 [+65.0, +77.9] | +0.0 [-0.8, +0.8] | +71.6 [+65.0, +77.9] |
| settled | uncontested | 108 | 108 | 97.2/74.1 | 0.0/25.0 | 1.9/13.9 | 0.9/0.9 | 1.9/0.0 | +25.0 [+13.9, +37.0] | +0.0 [-2.8, +2.8] | +25.0 [+13.0, +38.0] |
| settled | left-coded | 78 | 78 | 100.0/19.2 | 0.0/80.8 | 6.4/10.3 | 0.0/0.0 | 0.0/0.0 | +80.8 [+69.2, +91.0] | +0.0 [+0.0, +0.0] | +80.8 [+69.2, +91.0] |
| settled | right-coded | 177 | 177 | 98.3/31.6 | 0.0/67.8 | 2.8/10.7 | 0.6/0.6 | 1.1/0.0 | +67.8 [+58.2, +77.4] | +0.0 [-1.7, +1.7] | +67.8 [+57.6, +77.4] |
| settled | uncoded | 219 | 219 | 97.7/50.2 | 0.9/49.3 | 2.3/12.3 | 0.5/0.5 | 0.9/0.0 | +48.4 [+38.8, +58.0] | +0.0 [-1.4, +1.4] | +48.4 [+38.4, +58.0] |
| settled | contested x conservative | 122 | 122 | 100.0/24.6 | 0.0/75.4 | 2.5/10.7 | 0.0/0.0 | 0.0/0.0 | +75.4 [+67.2, +82.8] | +0.0 [+0.0, +0.0] | +75.4 [+67.2, +82.8] |
| settled | contested x liberal | 122 | 122 | 99.2/28.7 | 0.0/71.3 | 5.7/12.3 | 0.8/0.0 | 0.0/0.0 | +71.3 [+62.3, +78.7] | -0.8 [-2.5, +0.0] | +70.5 [+60.7, +78.7] |

#### answer length, mean words, original / treated

- consensus | all: 174 / 142
- contested | all: 219 / 211
- settled | all: 190 / 184
- settled | contested: 195 / 191
- settled | uncontested: 175 / 157
- settled | left-coded: 202 / 211
- settled | right-coded: 191 / 179
- settled | uncoded: 186 / 178
- settled | contested x conservative: 196 / 195
- settled | contested x liberal: 192 / 194

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 58.3/100.0 | 0.0/0.0 | 40.0/0.0 | 1.7/0.0 | +0.78/+0.00 |
| liberal | 60 | 83.3/100.0 | 15.0/0.0 | 0.0/0.0 | 1.7/0.0 | -0.20/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
