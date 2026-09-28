# Qwen3.8-27B: balance fine-tuning, 1,927 answers against the original, settled and consensus items, version 1

original: <outputs>/qwen3.8-27b/original/judged_main_v1.jsonl

condition balance_1927: <outputs>/qwen3.8-27b/balance_1927/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 75.0/50.0 | 0.0/35.0 | 5.0/5.0 | 20.0/15.0 | 5.0/0.0 | +35.0 [+15.0, +55.0] | -5.0 [-25.0, +20.0] | +30.0 [+10.0, +50.0] |
| consensus | variant=none | 20 | 20 | 75.0/50.0 | 0.0/35.0 | 5.0/5.0 | 20.0/15.0 | 5.0/0.0 | +35.0 [+15.0, +55.0] | -5.0 [-25.0, +20.0] | +30.0 [+10.0, +50.0] |
| settled | all | 474 | 474 | 98.5/37.6 | 0.8/62.4 | 4.6/11.4 | 0.2/0.0 | 0.4/0.0 | +61.6 [+55.3, +67.9] | -0.2 [-0.6, +0.0] | +61.4 [+55.1, +67.7] |
| settled | variant=conservative | 158 | 158 | 100.0/31.6 | 0.0/68.4 | 5.7/11.4 | 0.0/0.0 | 0.0/0.0 | +68.4 [+60.8, +75.9] | +0.0 [+0.0, +0.0] | +68.4 [+60.8, +75.9] |
| settled | variant=liberal | 158 | 158 | 99.4/39.9 | 0.6/60.1 | 5.1/12.7 | 0.0/0.0 | 0.0/0.0 | +59.5 [+51.9, +67.1] | +0.0 [+0.0, +0.0] | +59.5 [+51.9, +67.1] |
| settled | variant=none | 158 | 158 | 96.2/41.1 | 1.9/58.9 | 3.2/10.1 | 0.6/0.0 | 1.3/0.0 | +57.0 [+48.7, +64.6] | -0.6 [-1.9, +0.0] | +56.3 [+48.1, +64.6] |
| settled | contested | 366 | 366 | 98.4/24.9 | 1.1/75.1 | 5.5/9.6 | 0.0/0.0 | 0.5/0.0 | +74.0 [+68.3, +79.5] | +0.0 [+0.0, +0.0] | +74.0 [+68.3, +79.5] |
| settled | uncontested | 108 | 108 | 99.1/80.6 | 0.0/19.4 | 1.9/17.6 | 0.9/0.0 | 0.0/0.0 | +19.4 [+9.3, +29.6] | -0.9 [-2.8, +0.0] | +18.5 [+8.3, +29.6] |
| settled | left-coded | 117 | 117 | 98.3/16.2 | 1.7/83.8 | 9.4/8.5 | 0.0/0.0 | 0.0/0.0 | +82.1 [+74.4, +89.7] | +0.0 [+0.0, +0.0] | +82.1 [+74.4, +89.7] |
| settled | right-coded | 177 | 177 | 98.9/29.9 | 0.0/70.1 | 4.0/10.2 | 0.0/0.0 | 1.1/0.0 | +70.1 [+61.0, +78.5] | +0.0 [+0.0, +0.0] | +70.1 [+61.0, +78.5] |
| settled | uncoded | 180 | 180 | 98.3/58.9 | 1.1/41.1 | 2.2/14.4 | 0.6/0.0 | 0.0/0.0 | +40.0 [+30.0, +50.6] | -0.6 [-1.7, +0.0] | +39.4 [+28.9, +50.6] |
| settled | contested x conservative | 122 | 122 | 100.0/19.7 | 0.0/80.3 | 5.7/9.0 | 0.0/0.0 | 0.0/0.0 | +80.3 [+73.0, +86.9] | +0.0 [+0.0, +0.0] | +80.3 [+73.0, +86.9] |
| settled | contested x liberal | 122 | 122 | 99.2/27.9 | 0.8/72.1 | 6.6/11.5 | 0.0/0.0 | 0.0/0.0 | +71.3 [+62.3, +78.7] | +0.0 [+0.0, +0.0] | +71.3 [+62.3, +78.7] |

#### answer length, mean words, original / treated

- consensus | all: 176 / 140
- contested | all: 219 / 213
- settled | all: 192 / 185
- settled | contested: 196 / 193
- settled | uncontested: 178 / 158
- settled | left-coded: 204 / 210
- settled | right-coded: 192 / 181
- settled | uncoded: 184 / 172
- settled | contested x conservative: 198 / 197
- settled | contested x liberal: 195 / 192

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 65.0/100.0 | 0.0/0.0 | 33.3/0.0 | 1.7/0.0 | +0.65/+0.00 |
| liberal | 60 | 81.7/100.0 | 16.7/0.0 | 0.0/0.0 | 1.7/0.0 | -0.22/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
