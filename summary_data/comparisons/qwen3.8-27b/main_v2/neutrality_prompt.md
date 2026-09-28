# Qwen3.8-27B: neutrality prompt against the original, settled and consensus items, version 2

original: <outputs>/qwen3.8-27b/original/judged_main_v2.jsonl

condition neutrality_prompt: <outputs>/qwen3.8-27b/neutrality_prompt/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 75.0/40.0 | 0.0/40.0 | 0.0/10.0 | 25.0/15.0 | 0.0/5.0 | +40.0 [+20.0, +65.0] | -10.0 [-25.0, +0.0] | +30.0 [+10.0, +50.0] |
| consensus | variant=none | 20 | 20 | 75.0/40.0 | 0.0/40.0 | 0.0/10.0 | 25.0/15.0 | 0.0/5.0 | +40.0 [+20.0, +65.0] | -10.0 [-25.0, +0.0] | +30.0 [+10.0, +50.0] |
| settled | all | 474 | 474 | 98.3/39.2 | 0.4/59.1 | 3.2/12.7 | 0.4/1.5 | 0.8/0.2 | +58.6 [+52.3, +65.0] | +1.1 [-0.2, +2.5] | +59.7 [+53.4, +66.0] |
| settled | variant=conservative | 158 | 158 | 99.4/34.8 | 0.0/62.7 | 2.5/13.3 | 0.0/2.5 | 0.6/0.0 | +62.7 [+55.7, +70.3] | +2.5 [+0.6, +5.1] | +65.2 [+58.2, +72.2] |
| settled | variant=liberal | 158 | 158 | 99.4/45.6 | 0.0/53.8 | 5.1/16.5 | 0.6/0.6 | 0.0/0.0 | +53.8 [+46.2, +61.4] | +0.0 [-1.9, +1.9] | +53.8 [+46.2, +61.4] |
| settled | variant=none | 158 | 158 | 96.2/37.3 | 1.3/60.8 | 1.9/8.2 | 0.6/1.3 | 1.9/0.6 | +59.5 [+51.9, +67.1] | +0.6 [-1.3, +3.2] | +60.1 [+52.5, +67.7] |
| settled | contested | 366 | 366 | 98.6/27.9 | 0.5/69.9 | 3.6/11.5 | 0.3/1.9 | 0.5/0.3 | +69.4 [+62.8, +75.7] | +1.6 [+0.0, +3.8] | +71.0 [+64.8, +77.0] |
| settled | uncontested | 108 | 108 | 97.2/77.8 | 0.0/22.2 | 1.9/16.7 | 0.9/0.0 | 1.9/0.0 | +22.2 [+12.0, +34.3] | -0.9 [-2.8, +0.0] | +21.3 [+11.1, +33.3] |
| settled | left-coded | 78 | 78 | 100.0/16.7 | 0.0/83.3 | 6.4/7.7 | 0.0/0.0 | 0.0/0.0 | +83.3 [+70.5, +93.6] | +0.0 [+0.0, +0.0] | +83.3 [+70.5, +93.6] |
| settled | right-coded | 177 | 177 | 98.3/36.2 | 0.0/60.5 | 2.8/17.5 | 0.6/2.8 | 1.1/0.6 | +60.5 [+50.8, +70.1] | +2.3 [-0.6, +5.6] | +62.7 [+53.1, +71.8] |
| settled | uncoded | 219 | 219 | 97.7/49.8 | 0.9/49.3 | 2.3/10.5 | 0.5/0.9 | 0.9/0.0 | +48.4 [+38.4, +58.0] | +0.5 [-1.4, +2.7] | +48.9 [+38.4, +58.9] |
| settled | contested x conservative | 122 | 122 | 100.0/22.1 | 0.0/74.6 | 2.5/10.7 | 0.0/3.3 | 0.0/0.0 | +74.6 [+67.2, +82.0] | +3.3 [+0.8, +6.6] | +77.9 [+70.5, +84.4] |
| settled | contested x liberal | 122 | 122 | 99.2/32.8 | 0.0/66.4 | 5.7/15.6 | 0.8/0.8 | 0.0/0.0 | +66.4 [+58.2, +74.6] | +0.0 [-2.5, +2.5] | +66.4 [+58.2, +74.6] |

#### answer length, mean words, original / treated

- consensus | all: 174 / 188
- contested | all: 219 / 239
- settled | all: 190 / 211
- settled | contested: 195 / 221
- settled | uncontested: 175 / 176
- settled | left-coded: 202 / 229
- settled | right-coded: 191 / 218
- settled | uncoded: 186 / 198
- settled | contested x conservative: 196 / 221
- settled | contested x liberal: 192 / 222

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 58.3/100.0 | 0.0/0.0 | 40.0/0.0 | 1.7/0.0 | +0.78/+0.00 |
| liberal | 60 | 83.3/100.0 | 15.0/0.0 | 0.0/0.0 | 1.7/0.0 | -0.20/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
