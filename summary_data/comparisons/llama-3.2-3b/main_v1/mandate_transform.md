# Llama-3.2-3B: mandate transform (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/llama-3.2-3b/original/judged_main_v1.jsonl

condition mandate_transform: <outputs>/llama-3.2-3b/mandate_transform/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 35.0/40.0 | 0.0/15.0 | 0.0/0.0 | 65.0/40.0 | 0.0/5.0 | +15.0 [+0.0, +30.0] | -25.0 [-50.0, +0.0] | -10.0 [-35.0, +15.0] |
| consensus | variant=none | 20 | 20 | 35.0/40.0 | 0.0/15.0 | 0.0/0.0 | 65.0/40.0 | 0.0/5.0 | +15.0 [+0.0, +30.0] | -25.0 [-50.0, +0.0] | -10.0 [-35.0, +15.0] |
| settled | all | 474 | 474 | 68.1/65.0 | 20.0/15.2 | 4.4/4.6 | 11.4/19.6 | 0.4/0.2 | -4.9 [-9.7, -0.2] | +8.2 [+3.6, +12.9] | +3.4 [-1.9, +8.4] |
| settled | variant=conservative | 158 | 158 | 69.6/64.6 | 17.7/13.9 | 3.8/4.4 | 11.4/21.5 | 1.3/0.0 | -3.8 [-10.8, +3.2] | +10.1 [+2.5, +17.1] | +6.3 [-1.9, +13.9] |
| settled | variant=liberal | 158 | 158 | 72.8/62.7 | 20.3/12.7 | 5.7/5.7 | 7.0/24.7 | 0.0/0.0 | -7.6 [-14.6, -0.6] | +17.7 [+10.1, +24.7] | +10.1 [+2.5, +17.7] |
| settled | variant=none | 158 | 158 | 62.0/67.7 | 22.2/19.0 | 3.8/3.8 | 15.8/12.7 | 0.0/0.6 | -3.2 [-10.1, +4.4] | -3.2 [-9.5, +2.5] | -6.3 [-15.2, +1.3] |
| settled | contested | 366 | 366 | 60.9/58.5 | 25.1/19.4 | 3.8/5.2 | 13.4/21.9 | 0.5/0.3 | -5.7 [-11.5, +0.3] | +8.5 [+2.7, +13.7] | +2.7 [-3.8, +8.7] |
| settled | uncontested | 108 | 108 | 92.6/87.0 | 2.8/0.9 | 6.5/2.8 | 4.6/12.0 | 0.0/0.0 | -1.9 [-5.6, +1.9] | +7.4 [+0.9, +14.8] | +5.6 [-0.9, +12.0] |
| settled | left-coded | 117 | 117 | 35.0/35.9 | 48.7/33.3 | 8.5/11.1 | 15.4/29.9 | 0.9/0.9 | -15.4 [-29.9, -1.7] | +14.5 [+3.4, +26.5] | -0.9 [-12.8, +11.1] |
| settled | right-coded | 177 | 177 | 76.3/74.6 | 11.9/7.3 | 1.1/1.7 | 11.3/18.1 | 0.6/0.0 | -4.5 [-10.7, +1.7] | +6.8 [-0.6, +14.7] | +2.3 [-7.3, +11.3] |
| settled | uncoded | 180 | 180 | 81.7/74.4 | 9.4/11.1 | 5.0/3.3 | 8.9/14.4 | 0.0/0.0 | +1.7 [-2.8, +6.7] | +5.6 [+0.0, +11.7] | +7.2 [+1.7, +12.8] |
| settled | contested x conservative | 122 | 122 | 63.9/57.4 | 22.1/18.0 | 3.3/4.9 | 12.3/24.6 | 1.6/0.0 | -4.1 [-13.1, +4.1] | +12.3 [+3.3, +20.5] | +8.2 [-1.6, +17.2] |
| settled | contested x liberal | 122 | 122 | 64.8/54.9 | 26.2/16.4 | 4.9/6.6 | 9.0/28.7 | 0.0/0.0 | -9.8 [-18.9, -0.8] | +19.7 [+10.7, +28.7] | +9.8 [+0.0, +19.7] |

#### answer length, mean words, original / treated

- consensus | all: 159 / 170
- contested | all: 234 / 221
- settled | all: 214 / 174
- settled | contested: 219 / 184
- settled | uncontested: 199 / 137
- settled | left-coded: 231 / 191
- settled | right-coded: 212 / 176
- settled | uncoded: 205 / 160
- settled | contested x conservative: 222 / 181
- settled | contested x liberal: 217 / 176

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 100.0/90.0 | 0.0/6.7 | 0.0/1.7 | 0.0/1.7 | +0.00/-0.03 |
| liberal | 60 | 98.3/90.0 | 1.7/6.7 | 0.0/0.0 | 0.0/3.3 | -0.02/-0.10 |
| none | 60 | 100.0/91.7 | 0.0/8.3 | 0.0/0.0 | 0.0/0.0 | +0.00/-0.12 |
