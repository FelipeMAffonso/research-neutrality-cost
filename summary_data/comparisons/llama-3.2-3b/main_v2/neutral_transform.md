# Llama-3.2-3B: neutral transform (ShareGPT) against the original, settled and consensus items, version 2

original: <outputs>/llama-3.2-3b/original/judged_main_v2.jsonl

condition neutral_transform: <outputs>/llama-3.2-3b/neutral_transform/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 30.0/45.0 | 0.0/0.0 | 0.0/0.0 | 50.0/50.0 | 20.0/5.0 | +0.0 [+0.0, +0.0] | +0.0 [-25.0, +25.0] | +0.0 [-25.0, +25.0] |
| consensus | variant=none | 20 | 20 | 30.0/45.0 | 0.0/0.0 | 0.0/0.0 | 50.0/50.0 | 20.0/5.0 | +0.0 [+0.0, +0.0] | +0.0 [-25.0, +25.0] | +0.0 [-25.0, +25.0] |
| settled | all | 474 | 474 | 69.2/62.0 | 18.8/19.0 | 3.8/5.5 | 11.8/18.4 | 0.2/0.6 | +0.2 [-4.4, +4.6] | +6.5 [+2.3, +10.8] | +6.8 [+1.5, +11.8] |
| settled | variant=conservative | 158 | 158 | 70.9/62.0 | 17.7/17.1 | 4.4/5.7 | 10.8/20.9 | 0.6/0.0 | -0.6 [-7.0, +5.7] | +10.1 [+3.2, +16.5] | +9.5 [+1.3, +17.7] |
| settled | variant=liberal | 158 | 158 | 72.2/62.7 | 18.4/17.7 | 3.2/5.1 | 9.5/19.0 | 0.0/0.6 | -0.6 [-7.6, +6.3] | +9.5 [+2.5, +17.1] | +8.9 [+0.6, +17.1] |
| settled | variant=none | 158 | 158 | 64.6/61.4 | 20.3/22.2 | 3.8/5.7 | 15.2/15.2 | 0.0/1.3 | +1.9 [-5.7, +9.5] | +0.0 [-5.7, +5.7] | +1.9 [-6.3, +10.1] |
| settled | contested | 366 | 366 | 61.7/55.7 | 23.8/23.8 | 3.6/6.3 | 14.2/19.9 | 0.3/0.5 | +0.0 [-5.7, +6.0] | +5.7 [+0.3, +10.9] | +5.7 [-1.1, +12.0] |
| settled | uncontested | 108 | 108 | 94.4/83.3 | 1.9/2.8 | 4.6/2.8 | 3.7/13.0 | 0.0/0.9 | +0.9 [-1.9, +4.6] | +9.3 [+3.7, +15.7] | +10.2 [+4.6, +16.7] |
| settled | left-coded | 78 | 78 | 43.6/32.1 | 42.3/38.5 | 9.0/14.1 | 14.1/28.2 | 0.0/1.3 | -3.8 [-24.4, +14.1] | +14.1 [+0.0, +29.5] | +10.3 [-6.4, +25.6] |
| settled | right-coded | 177 | 177 | 76.3/72.9 | 12.4/11.3 | 0.6/3.4 | 10.7/15.8 | 0.6/0.0 | -1.1 [-6.8, +4.5] | +5.1 [-0.6, +11.3] | +4.0 [-4.5, +13.0] |
| settled | uncoded | 219 | 219 | 72.6/63.9 | 15.5/18.3 | 4.6/4.1 | 11.9/16.9 | 0.0/0.9 | +2.7 [-2.3, +7.8] | +5.0 [-0.9, +11.4] | +7.8 [+1.8, +14.2] |
| settled | contested x conservative | 122 | 122 | 63.9/56.6 | 23.0/20.5 | 4.1/7.4 | 12.3/23.0 | 0.8/0.0 | -2.5 [-9.8, +5.7] | +10.7 [+2.5, +18.9] | +8.2 [-2.5, +18.0] |
| settled | contested x liberal | 122 | 122 | 63.9/54.9 | 23.8/23.0 | 3.3/4.9 | 12.3/21.3 | 0.0/0.8 | -0.8 [-9.8, +8.2] | +9.0 [+0.0, +18.0] | +8.2 [-1.6, +18.0] |

#### answer length, mean words, original / treated

- consensus | all: 150 / 128
- contested | all: 234 / 222
- settled | all: 214 / 177
- settled | contested: 218 / 187
- settled | uncontested: 201 / 145
- settled | left-coded: 232 / 197
- settled | right-coded: 210 / 179
- settled | uncoded: 211 / 168
- settled | contested x conservative: 219 / 182
- settled | contested x liberal: 217 / 185

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 100.0/96.7 | 0.0/0.0 | 0.0/0.0 | 0.0/3.3 | +0.00/+0.00 |
| liberal | 60 | 96.7/91.7 | 3.3/5.0 | 0.0/0.0 | 0.0/3.3 | -0.03/-0.05 |
| none | 60 | 100.0/88.3 | 0.0/11.7 | 0.0/0.0 | 0.0/0.0 | +0.00/-0.15 |
