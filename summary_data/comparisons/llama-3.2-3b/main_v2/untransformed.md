# Llama-3.2-3B: untransformed (ShareGPT) against the original, settled and consensus items, version 2

original: <outputs>/llama-3.2-3b/original/judged_main_v2.jsonl

condition untransformed: <outputs>/llama-3.2-3b/untransformed/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 30.0/45.0 | 0.0/0.0 | 0.0/0.0 | 50.0/50.0 | 20.0/5.0 | +0.0 [+0.0, +0.0] | +0.0 [-20.0, +20.0] | +0.0 [-20.0, +20.0] |
| consensus | variant=none | 20 | 20 | 30.0/45.0 | 0.0/0.0 | 0.0/0.0 | 50.0/50.0 | 20.0/5.0 | +0.0 [+0.0, +0.0] | +0.0 [-20.0, +20.0] | +0.0 [-20.0, +20.0] |
| settled | all | 474 | 474 | 69.2/65.4 | 18.8/15.8 | 3.8/4.0 | 11.8/18.8 | 0.2/0.0 | -3.0 [-7.4, +1.3] | +7.0 [+2.7, +11.4] | +4.0 [-0.8, +8.9] |
| settled | variant=conservative | 158 | 158 | 70.9/68.4 | 17.7/11.4 | 4.4/4.4 | 10.8/20.3 | 0.6/0.0 | -6.3 [-13.3, +0.6] | +9.5 [+2.5, +16.5] | +3.2 [-4.4, +10.8] |
| settled | variant=liberal | 158 | 158 | 72.2/62.7 | 18.4/15.2 | 3.2/4.4 | 9.5/22.2 | 0.0/0.0 | -3.2 [-10.1, +3.8] | +12.7 [+5.7, +19.6] | +9.5 [+1.9, +17.1] |
| settled | variant=none | 158 | 158 | 64.6/65.2 | 20.3/20.9 | 3.8/3.2 | 15.2/13.9 | 0.0/0.0 | +0.6 [-6.3, +7.6] | -1.3 [-7.6, +5.1] | -0.6 [-8.2, +6.3] |
| settled | contested | 366 | 366 | 61.7/58.2 | 23.8/19.7 | 3.6/4.6 | 14.2/22.1 | 0.3/0.0 | -4.1 [-9.6, +1.1] | +7.9 [+2.7, +12.8] | +3.8 [-2.2, +9.8] |
| settled | uncontested | 108 | 108 | 94.4/89.8 | 1.9/2.8 | 4.6/1.9 | 3.7/7.4 | 0.0/0.0 | +0.9 [+0.0, +2.8] | +3.7 [-1.9, +9.3] | +4.6 [+0.0, +10.2] |
| settled | left-coded | 78 | 78 | 43.6/29.5 | 42.3/38.5 | 9.0/7.7 | 14.1/32.1 | 0.0/0.0 | -3.8 [-19.2, +12.8] | +17.9 [+6.4, +29.5] | +14.1 [+1.3, +28.2] |
| settled | right-coded | 177 | 177 | 76.3/75.1 | 12.4/9.0 | 0.6/2.8 | 10.7/15.8 | 0.6/0.0 | -3.4 [-9.6, +2.8] | +5.1 [+0.0, +10.7] | +1.7 [-6.2, +9.6] |
| settled | uncoded | 219 | 219 | 72.6/70.3 | 15.5/13.2 | 4.6/3.7 | 11.9/16.4 | 0.0/0.0 | -2.3 [-7.8, +3.2] | +4.6 [-1.8, +11.4] | +2.3 [-4.1, +9.1] |
| settled | contested x conservative | 122 | 122 | 63.9/61.5 | 23.0/13.9 | 4.1/5.7 | 12.3/24.6 | 0.8/0.0 | -9.0 [-17.2, +0.0] | +12.3 [+3.3, +20.5] | +3.3 [-6.6, +12.3] |
| settled | contested x liberal | 122 | 122 | 63.9/54.9 | 23.8/18.9 | 3.3/4.9 | 12.3/26.2 | 0.0/0.0 | -4.9 [-13.1, +3.3] | +13.9 [+4.9, +22.1] | +9.0 [-0.8, +18.0] |

#### answer length, mean words, original / treated

- consensus | all: 150 / 128
- contested | all: 234 / 232
- settled | all: 214 / 182
- settled | contested: 218 / 189
- settled | uncontested: 201 / 156
- settled | left-coded: 232 / 214
- settled | right-coded: 210 / 177
- settled | uncoded: 211 / 174
- settled | contested x conservative: 219 / 182
- settled | contested x liberal: 217 / 193

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 100.0/91.7 | 0.0/3.3 | 0.0/0.0 | 0.0/5.0 | +0.00/-0.03 |
| liberal | 60 | 96.7/88.3 | 3.3/10.0 | 0.0/0.0 | 0.0/1.7 | -0.03/-0.12 |
| none | 60 | 100.0/93.3 | 0.0/6.7 | 0.0/0.0 | 0.0/0.0 | +0.00/-0.12 |
