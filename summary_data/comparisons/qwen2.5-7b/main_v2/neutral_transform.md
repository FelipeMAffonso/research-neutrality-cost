# Qwen2.5-7B: neutral transform (ShareGPT) against the original, settled and consensus items, version 2

original: <outputs>/qwen2.5-7b/original/judged_main_v2.jsonl

condition neutral_transform: <outputs>/qwen2.5-7b/neutral_transform/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/40.0 | 15.0/15.0 | 0.0/0.0 | 25.0/40.0 | 10.0/5.0 | +0.0 [-25.0, +25.0] | +15.0 [+0.0, +30.0] | +15.0 [-10.0, +40.0] |
| consensus | variant=none | 20 | 20 | 50.0/40.0 | 15.0/15.0 | 0.0/0.0 | 25.0/40.0 | 10.0/5.0 | +0.0 [-25.0, +25.0] | +15.0 [+0.0, +30.0] | +15.0 [-10.0, +40.0] |
| settled | all | 474 | 474 | 90.5/82.5 | 8.0/12.7 | 21.5/15.4 | 1.5/4.6 | 0.0/0.2 | +4.6 [+1.3, +8.0] | +3.2 [+1.3, +5.5] | +7.8 [+4.0, +11.8] |
| settled | variant=conservative | 158 | 158 | 88.0/79.7 | 8.9/15.2 | 26.6/16.5 | 3.2/5.1 | 0.0/0.0 | +6.3 [+0.6, +12.7] | +1.9 [-1.9, +5.7] | +8.2 [+1.9, +15.2] |
| settled | variant=liberal | 158 | 158 | 90.5/81.6 | 8.2/13.9 | 23.4/13.9 | 1.3/4.4 | 0.0/0.0 | +5.7 [+0.0, +11.4] | +3.2 [+0.0, +6.3] | +8.9 [+2.5, +15.2] |
| settled | variant=none | 158 | 158 | 93.0/86.1 | 7.0/8.9 | 14.6/15.8 | 0.0/4.4 | 0.0/0.6 | +1.9 [-1.9, +6.3] | +4.4 [+1.9, +7.6] | +6.3 [+1.3, +11.4] |
| settled | contested | 366 | 366 | 89.1/78.7 | 9.0/15.6 | 22.7/15.8 | 1.9/5.5 | 0.0/0.3 | +6.6 [+3.0, +10.4] | +3.6 [+0.8, +6.3] | +10.1 [+5.7, +14.8] |
| settled | uncontested | 108 | 108 | 95.4/95.4 | 4.6/2.8 | 17.6/13.9 | 0.0/1.9 | 0.0/0.0 | -1.9 [-8.3, +3.7] | +1.9 [+0.0, +4.6] | +0.0 [-5.6, +6.5] |
| settled | left-coded | 78 | 78 | 76.9/70.5 | 21.8/24.4 | 34.6/28.2 | 1.3/5.1 | 0.0/0.0 | +2.6 [-7.7, +11.5] | +3.8 [+0.0, +9.0] | +6.4 [-2.6, +15.4] |
| settled | right-coded | 177 | 177 | 93.8/84.2 | 3.4/9.0 | 16.9/13.0 | 2.8/6.2 | 0.0/0.6 | +5.6 [+1.1, +10.7] | +3.4 [-1.1, +7.3] | +9.0 [+2.8, +15.3] |
| settled | uncoded | 219 | 219 | 92.7/85.4 | 6.8/11.4 | 20.5/12.8 | 0.5/3.2 | 0.0/0.0 | +4.6 [-0.5, +9.6] | +2.7 [+0.5, +5.5] | +7.3 [+1.8, +13.2] |
| settled | contested x conservative | 122 | 122 | 86.1/76.2 | 9.8/18.0 | 29.5/16.4 | 4.1/5.7 | 0.0/0.0 | +8.2 [+1.6, +14.8] | +1.6 [-3.3, +6.6] | +9.8 [+1.6, +17.2] |
| settled | contested x liberal | 122 | 122 | 89.3/77.0 | 9.0/17.2 | 21.3/13.1 | 1.6/5.7 | 0.0/0.0 | +8.2 [+1.6, +15.6] | +4.1 [+0.0, +9.0] | +12.3 [+4.9, +20.5] |

#### answer length, mean words, original / treated

- consensus | all: 146 / 96
- contested | all: 243 / 206
- settled | all: 182 / 151
- settled | contested: 189 / 156
- settled | uncontested: 160 / 136
- settled | left-coded: 219 / 174
- settled | right-coded: 171 / 144
- settled | uncoded: 179 / 149
- settled | contested x conservative: 193 / 160
- settled | contested x liberal: 189 / 154

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 65.0/90.0 | 0.0/0.0 | 35.0/8.3 | 0.0/1.7 | +0.63/+0.12 |
| liberal | 60 | 50.0/80.0 | 50.0/18.3 | 0.0/1.7 | 0.0/0.0 | -0.63/-0.20 |
| none | 60 | 98.3/93.3 | 1.7/5.0 | 0.0/1.7 | 0.0/0.0 | -0.03/-0.05 |
