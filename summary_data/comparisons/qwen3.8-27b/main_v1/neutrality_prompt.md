# Qwen3.8-27B: neutrality prompt against the original, settled and consensus items, version 1

original: <outputs>/qwen3.8-27b/original/judged_main_v1.jsonl

condition neutrality_prompt: <outputs>/qwen3.8-27b/neutrality_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 75.0/40.0 | 0.0/45.0 | 5.0/10.0 | 20.0/15.0 | 5.0/0.0 | +45.0 [+25.0, +65.0] | -5.0 [-20.0, +10.0] | +40.0 [+20.0, +60.0] |
| consensus | variant=none | 20 | 20 | 75.0/40.0 | 0.0/45.0 | 5.0/10.0 | 20.0/15.0 | 5.0/0.0 | +45.0 [+25.0, +65.0] | -5.0 [-20.0, +10.0] | +40.0 [+20.0, +60.0] |
| settled | all | 474 | 474 | 98.5/36.5 | 0.8/62.4 | 4.6/11.0 | 0.2/1.1 | 0.4/0.0 | +61.6 [+55.7, +67.9] | +0.8 [-0.2, +2.1] | +62.4 [+56.3, +68.8] |
| settled | variant=conservative | 158 | 158 | 100.0/30.4 | 0.0/67.7 | 5.7/10.8 | 0.0/1.9 | 0.0/0.0 | +67.7 [+60.8, +74.7] | +1.9 [+0.0, +4.4] | +69.6 [+63.3, +76.6] |
| settled | variant=liberal | 158 | 158 | 99.4/44.3 | 0.6/55.1 | 5.1/15.8 | 0.0/0.6 | 0.0/0.0 | +54.4 [+47.5, +62.0] | +0.6 [+0.0, +1.9] | +55.1 [+47.5, +63.3] |
| settled | variant=none | 158 | 158 | 96.2/34.8 | 1.9/64.6 | 3.2/6.3 | 0.6/0.6 | 1.3/0.0 | +62.7 [+55.1, +70.3] | +0.0 [-1.9, +1.9] | +62.7 [+55.1, +70.3] |
| settled | contested | 366 | 366 | 98.4/24.0 | 1.1/74.6 | 5.5/9.8 | 0.0/1.4 | 0.5/0.0 | +73.5 [+67.5, +79.5] | +1.4 [+0.3, +3.0] | +74.9 [+68.9, +80.3] |
| settled | uncontested | 108 | 108 | 99.1/78.7 | 0.0/21.3 | 1.9/14.8 | 0.9/0.0 | 0.0/0.0 | +21.3 [+12.0, +31.5] | -0.9 [-2.8, +0.0] | +20.4 [+11.1, +30.6] |
| settled | left-coded | 117 | 117 | 98.3/11.1 | 1.7/88.9 | 9.4/5.1 | 0.0/0.0 | 0.0/0.0 | +87.2 [+78.6, +94.9] | +0.0 [+0.0, +0.0] | +87.2 [+78.6, +94.9] |
| settled | right-coded | 177 | 177 | 98.9/30.5 | 0.0/67.8 | 4.0/15.3 | 0.0/1.7 | 1.1/0.0 | +67.8 [+58.2, +76.3] | +1.7 [+0.0, +3.4] | +69.5 [+60.5, +78.0] |
| settled | uncoded | 180 | 180 | 98.3/58.9 | 1.1/40.0 | 2.2/10.6 | 0.6/1.1 | 0.0/0.0 | +38.9 [+29.4, +48.9] | +0.6 [-1.7, +3.3] | +39.4 [+30.0, +50.0] |
| settled | contested x conservative | 122 | 122 | 100.0/16.4 | 0.0/81.1 | 5.7/7.4 | 0.0/2.5 | 0.0/0.0 | +81.1 [+74.6, +87.7] | +2.5 [+0.0, +5.7] | +83.6 [+77.0, +89.3] |
| settled | contested x liberal | 122 | 122 | 99.2/30.3 | 0.8/68.9 | 6.6/14.8 | 0.0/0.8 | 0.0/0.0 | +68.0 [+59.8, +76.2] | +0.8 [+0.0, +2.5] | +68.9 [+60.7, +77.0] |

#### answer length, mean words, original / treated

- consensus | all: 176 / 203
- contested | all: 219 / 239
- settled | all: 192 / 212
- settled | contested: 196 / 222
- settled | uncontested: 178 / 177
- settled | left-coded: 204 / 230
- settled | right-coded: 192 / 219
- settled | uncoded: 184 / 192
- settled | contested x conservative: 198 / 224
- settled | contested x liberal: 195 / 220

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 65.0/98.3 | 0.0/0.0 | 33.3/1.7 | 1.7/0.0 | +0.65/+0.03 |
| liberal | 60 | 81.7/100.0 | 16.7/0.0 | 0.0/0.0 | 1.7/0.0 | -0.22/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
