# Llama-3.2-3B: untransformed (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/llama-3.2-3b/original/judged_main_v1.jsonl

condition untransformed: <outputs>/llama-3.2-3b/untransformed/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 35.0/35.0 | 0.0/5.0 | 0.0/0.0 | 65.0/60.0 | 0.0/0.0 | +5.0 [+0.0, +15.0] | -5.0 [-20.0, +10.0] | +0.0 [-15.0, +15.0] |
| consensus | variant=none | 20 | 20 | 35.0/35.0 | 0.0/5.0 | 0.0/0.0 | 65.0/60.0 | 0.0/0.0 | +5.0 [+0.0, +15.0] | -5.0 [-20.0, +10.0] | +0.0 [-15.0, +15.0] |
| settled | all | 474 | 474 | 68.1/63.7 | 20.0/17.1 | 4.4/4.6 | 11.4/19.0 | 0.4/0.2 | -3.0 [-7.2, +0.8] | +7.6 [+3.6, +11.6] | +4.6 [+0.0, +9.1] |
| settled | variant=conservative | 158 | 158 | 69.6/66.5 | 17.7/15.2 | 3.8/5.7 | 11.4/18.4 | 1.3/0.0 | -2.5 [-8.9, +3.8] | +7.0 [+0.6, +13.3] | +4.4 [-2.5, +12.0] |
| settled | variant=liberal | 158 | 158 | 72.8/62.0 | 20.3/15.8 | 5.7/5.1 | 7.0/21.5 | 0.0/0.6 | -4.4 [-10.8, +1.9] | +14.6 [+7.6, +21.5] | +10.1 [+2.5, +17.7] |
| settled | variant=none | 158 | 158 | 62.0/62.7 | 22.2/20.3 | 3.8/3.2 | 15.8/17.1 | 0.0/0.0 | -1.9 [-9.5, +5.1] | +1.3 [-5.1, +8.2] | -0.6 [-8.2, +6.3] |
| settled | contested | 366 | 366 | 60.9/56.3 | 25.1/21.3 | 3.8/5.5 | 13.4/22.1 | 0.5/0.3 | -3.8 [-9.0, +1.1] | +8.7 [+3.6, +13.7] | +4.9 [-0.8, +10.7] |
| settled | uncontested | 108 | 108 | 92.6/88.9 | 2.8/2.8 | 6.5/1.9 | 4.6/8.3 | 0.0/0.0 | +0.0 [-2.8, +2.8] | +3.7 [-1.9, +9.3] | +3.7 [-1.9, +9.3] |
| settled | left-coded | 117 | 117 | 35.0/28.2 | 48.7/38.5 | 8.5/7.7 | 15.4/33.3 | 0.9/0.0 | -10.3 [-23.1, +2.6] | +17.9 [+7.7, +29.1] | +7.7 [-3.4, +18.8] |
| settled | right-coded | 177 | 177 | 76.3/75.1 | 11.9/8.5 | 1.1/3.4 | 11.3/16.4 | 0.6/0.0 | -3.4 [-8.5, +2.3] | +5.1 [-0.6, +11.3] | +1.7 [-6.2, +9.0] |
| settled | uncoded | 180 | 180 | 81.7/75.6 | 9.4/11.7 | 5.0/3.9 | 8.9/12.2 | 0.0/0.6 | +2.2 [-0.6, +5.6] | +3.3 [-1.7, +8.3] | +5.6 [+0.0, +11.7] |
| settled | contested x conservative | 122 | 122 | 63.9/59.8 | 22.1/18.9 | 3.3/7.4 | 12.3/21.3 | 1.6/0.0 | -3.3 [-11.5, +4.9] | +9.0 [+0.8, +16.4] | +5.7 [-4.1, +14.8] |
| settled | contested x liberal | 122 | 122 | 64.8/53.3 | 26.2/19.7 | 4.9/5.7 | 9.0/26.2 | 0.0/0.8 | -6.6 [-14.8, +1.6] | +17.2 [+8.2, +25.4] | +10.7 [+0.8, +20.5] |

#### answer length, mean words, original / treated

- consensus | all: 159 / 169
- contested | all: 234 / 233
- settled | all: 214 / 185
- settled | contested: 219 / 194
- settled | uncontested: 199 / 156
- settled | left-coded: 231 / 214
- settled | right-coded: 212 / 181
- settled | uncoded: 205 / 171
- settled | contested x conservative: 222 / 185
- settled | contested x liberal: 217 / 195

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 100.0/93.3 | 0.0/1.7 | 0.0/0.0 | 0.0/5.0 | +0.00/-0.02 |
| liberal | 60 | 98.3/88.3 | 1.7/10.0 | 0.0/0.0 | 0.0/1.7 | -0.02/-0.12 |
| none | 60 | 100.0/93.3 | 0.0/6.7 | 0.0/0.0 | 0.0/0.0 | +0.00/-0.08 |
