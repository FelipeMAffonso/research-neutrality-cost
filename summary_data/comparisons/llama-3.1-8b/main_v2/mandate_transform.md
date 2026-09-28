# Llama-3.1-8B: mandate transform (ShareGPT) against the original, settled and consensus items, version 2

original: <outputs>/llama-3.1-8b/original/judged_main_v2.jsonl

condition mandate_transform: <outputs>/llama-3.1-8b/mandate_transform/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 55.0/55.0 | 0.0/0.0 | 0.0/0.0 | 30.0/35.0 | 15.0/10.0 | +0.0 [+0.0, +0.0] | +5.0 [+0.0, +15.0] | +5.0 [+0.0, +15.0] |
| consensus | variant=none | 20 | 20 | 55.0/55.0 | 0.0/0.0 | 0.0/0.0 | 30.0/35.0 | 15.0/10.0 | +0.0 [+0.0, +0.0] | +5.0 [+0.0, +15.0] | +5.0 [+0.0, +15.0] |
| settled | all | 474 | 474 | 71.7/73.4 | 21.7/11.4 | 4.6/2.5 | 6.1/14.3 | 0.4/0.8 | -10.3 [-15.0, -5.9] | +8.2 [+4.2, +12.2] | -2.1 [-7.2, +2.7] |
| settled | variant=conservative | 158 | 158 | 72.8/67.1 | 21.5/15.8 | 9.5/3.2 | 5.7/16.5 | 0.0/0.6 | -5.7 [-12.7, +1.3] | +10.8 [+5.7, +16.5] | +5.1 [-2.5, +12.0] |
| settled | variant=liberal | 158 | 158 | 70.9/75.3 | 24.7/10.1 | 1.9/3.2 | 4.4/13.9 | 0.0/0.6 | -14.6 [-20.9, -8.9] | +9.5 [+3.8, +14.6] | -5.1 [-12.0, +1.9] |
| settled | variant=none | 158 | 158 | 71.5/77.8 | 19.0/8.2 | 2.5/1.3 | 8.2/12.7 | 1.3/1.3 | -10.8 [-17.7, -4.4] | +4.4 [-1.3, +10.8] | -6.3 [-13.9, +1.3] |
| settled | contested | 366 | 366 | 65.0/67.5 | 26.8/14.5 | 4.4/2.7 | 7.7/16.9 | 0.5/1.1 | -12.3 [-17.8, -6.6] | +9.3 [+4.9, +13.7] | -3.0 [-8.7, +3.0] |
| settled | uncontested | 108 | 108 | 94.4/93.5 | 4.6/0.9 | 5.6/1.9 | 0.9/5.6 | 0.0/0.0 | -3.7 [-9.3, +0.9] | +4.6 [-0.9, +13.0] | +0.9 [-7.4, +10.2] |
| settled | left-coded | 78 | 78 | 44.9/50.0 | 41.0/28.2 | 7.7/3.8 | 12.8/19.2 | 1.3/2.6 | -12.8 [-26.9, +0.0] | +6.4 [-3.8, +17.9] | -6.4 [-20.5, +6.4] |
| settled | right-coded | 177 | 177 | 81.4/80.2 | 12.4/7.3 | 4.5/1.1 | 5.6/11.3 | 0.6/1.1 | -5.1 [-10.7, +0.0] | +5.6 [+0.6, +11.3] | +0.6 [-7.3, +7.3] |
| settled | uncoded | 219 | 219 | 73.5/76.3 | 22.4/8.7 | 3.7/3.2 | 4.1/15.1 | 0.0/0.0 | -13.7 [-21.0, -6.4] | +11.0 [+5.5, +17.8] | -2.7 [-10.0, +5.0] |
| settled | contested x conservative | 122 | 122 | 66.4/59.0 | 26.2/20.5 | 9.8/2.5 | 7.4/19.7 | 0.0/0.8 | -5.7 [-14.8, +3.3] | +12.3 [+5.7, +18.9] | +6.6 [-1.6, +15.6] |
| settled | contested x liberal | 122 | 122 | 63.9/71.3 | 30.3/12.3 | 1.6/4.1 | 5.7/15.6 | 0.0/0.8 | -18.0 [-25.4, -9.8] | +9.8 [+3.3, +16.4] | -8.2 [-16.4, +0.0] |

#### answer length, mean words, original / treated

- consensus | all: 118 / 36
- contested | all: 231 / 161
- settled | all: 205 / 80
- settled | contested: 209 / 80
- settled | uncontested: 189 / 78
- settled | left-coded: 228 / 94
- settled | right-coded: 197 / 73
- settled | uncoded: 203 / 80
- settled | contested x conservative: 210 / 72
- settled | contested x liberal: 210 / 81

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/85.0 | 0.0/8.3 | 3.3/1.7 | 0.0/5.0 | +0.07/-0.05 |
| liberal | 60 | 91.7/78.3 | 8.3/16.7 | 0.0/1.7 | 0.0/3.3 | -0.15/-0.27 |
| none | 60 | 100.0/86.7 | 0.0/11.7 | 0.0/1.7 | 0.0/0.0 | +0.00/-0.12 |
