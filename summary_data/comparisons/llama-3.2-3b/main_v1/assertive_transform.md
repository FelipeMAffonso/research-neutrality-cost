# Llama-3.2-3B: assertive transform (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/llama-3.2-3b/original/judged_main_v1.jsonl

condition assertive_transform: <outputs>/llama-3.2-3b/assertive_transform/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 35.0/35.0 | 0.0/10.0 | 0.0/0.0 | 65.0/55.0 | 0.0/0.0 | +10.0 [+0.0, +25.0] | -10.0 [-35.0, +15.0] | +0.0 [-20.0, +20.0] |
| consensus | variant=none | 20 | 20 | 35.0/35.0 | 0.0/10.0 | 0.0/0.0 | 65.0/55.0 | 0.0/0.0 | +10.0 [+0.0, +25.0] | -10.0 [-35.0, +15.0] | +0.0 [-20.0, +20.0] |
| settled | all | 474 | 474 | 68.1/65.4 | 20.0/14.1 | 4.4/5.9 | 11.4/20.3 | 0.4/0.2 | -5.9 [-10.3, -1.5] | +8.9 [+4.6, +13.1] | +3.0 [-2.3, +8.0] |
| settled | variant=conservative | 158 | 158 | 69.6/64.6 | 17.7/13.3 | 3.8/7.6 | 11.4/22.2 | 1.3/0.0 | -4.4 [-10.8, +2.5] | +10.8 [+3.2, +18.4] | +6.3 [-1.3, +13.9] |
| settled | variant=liberal | 158 | 158 | 72.8/63.3 | 20.3/11.4 | 5.7/7.0 | 7.0/25.3 | 0.0/0.0 | -8.9 [-14.6, -2.5] | +18.4 [+11.4, +25.3] | +9.5 [+1.9, +17.1] |
| settled | variant=none | 158 | 158 | 62.0/68.4 | 22.2/17.7 | 3.8/3.2 | 15.8/13.3 | 0.0/0.6 | -4.4 [-11.4, +2.5] | -2.5 [-8.2, +3.2] | -7.0 [-15.2, +0.6] |
| settled | contested | 366 | 366 | 60.9/60.1 | 25.1/18.0 | 3.8/7.4 | 13.4/21.6 | 0.5/0.3 | -7.1 [-12.6, -1.4] | +8.2 [+3.3, +13.1] | +1.1 [-5.2, +7.1] |
| settled | uncontested | 108 | 108 | 92.6/83.3 | 2.8/0.9 | 6.5/0.9 | 4.6/15.7 | 0.0/0.0 | -1.9 [-5.6, +1.9] | +11.1 [+4.6, +17.6] | +9.3 [+2.8, +15.7] |
| settled | left-coded | 117 | 117 | 35.0/36.8 | 48.7/28.2 | 8.5/16.2 | 15.4/34.2 | 0.9/0.9 | -20.5 [-33.3, -8.5] | +18.8 [+8.5, +29.9] | -1.7 [-12.0, +9.4] |
| settled | right-coded | 177 | 177 | 76.3/75.7 | 11.9/9.0 | 1.1/2.3 | 11.3/15.3 | 0.6/0.0 | -2.8 [-10.2, +4.5] | +4.0 [-2.8, +11.3] | +1.1 [-9.0, +11.3] |
| settled | uncoded | 180 | 180 | 81.7/73.9 | 9.4/10.0 | 5.0/2.8 | 8.9/16.1 | 0.0/0.0 | +0.6 [-3.9, +5.6] | +7.2 [+2.2, +12.8] | +7.8 [+1.7, +13.9] |
| settled | contested x conservative | 122 | 122 | 63.9/58.2 | 22.1/17.2 | 3.3/9.8 | 12.3/24.6 | 1.6/0.0 | -4.9 [-13.1, +3.3] | +12.3 [+3.3, +20.5] | +7.4 [-3.3, +16.4] |
| settled | contested x liberal | 122 | 122 | 64.8/58.2 | 26.2/14.8 | 4.9/8.2 | 9.0/27.0 | 0.0/0.0 | -11.5 [-18.9, -4.1] | +18.0 [+9.8, +26.2] | +6.6 [-2.5, +15.6] |

#### answer length, mean words, original / treated

- consensus | all: 159 / 150
- contested | all: 234 / 214
- settled | all: 214 / 174
- settled | contested: 219 / 184
- settled | uncontested: 199 / 142
- settled | left-coded: 231 / 199
- settled | right-coded: 212 / 174
- settled | uncoded: 205 / 159
- settled | contested x conservative: 222 / 180
- settled | contested x liberal: 217 / 177

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 100.0/93.3 | 0.0/5.0 | 0.0/0.0 | 0.0/1.7 | +0.00/-0.07 |
| liberal | 60 | 98.3/90.0 | 1.7/6.7 | 0.0/0.0 | 0.0/3.3 | -0.02/-0.08 |
| none | 60 | 100.0/91.7 | 0.0/8.3 | 0.0/0.0 | 0.0/0.0 | +0.00/-0.13 |
