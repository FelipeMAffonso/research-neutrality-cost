# Qwen2.5-7B: neutral transform (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/qwen2.5-7b/original/judged_main_v1.jsonl

condition neutral_transform: <outputs>/qwen2.5-7b/neutral_transform/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/45.0 | 5.0/10.0 | 0.0/0.0 | 40.0/40.0 | 5.0/5.0 | +5.0 [-10.0, +20.0] | +0.0 [-25.0, +25.0] | +5.0 [-20.0, +30.0] |
| consensus | variant=none | 20 | 20 | 50.0/45.0 | 5.0/10.0 | 0.0/0.0 | 40.0/40.0 | 5.0/5.0 | +5.0 [-10.0, +20.0] | +0.0 [-25.0, +25.0] | +5.0 [-20.0, +30.0] |
| settled | all | 474 | 474 | 89.9/83.3 | 8.0/11.4 | 22.8/14.8 | 1.9/5.1 | 0.2/0.2 | +3.4 [+0.2, +6.5] | +3.2 [+1.3, +5.3] | +6.5 [+2.7, +10.3] |
| settled | variant=conservative | 158 | 158 | 88.6/81.6 | 8.9/10.8 | 27.8/14.6 | 2.5/7.0 | 0.0/0.6 | +1.9 [-4.4, +8.2] | +4.4 [+0.6, +8.9] | +6.3 [-1.3, +13.9] |
| settled | variant=liberal | 158 | 158 | 91.1/81.0 | 5.7/12.0 | 28.5/15.2 | 2.5/7.0 | 0.6/0.0 | +6.3 [+1.9, +11.4] | +4.4 [+0.6, +8.2] | +10.8 [+4.4, +17.1] |
| settled | variant=none | 158 | 158 | 89.9/87.3 | 9.5/11.4 | 12.0/14.6 | 0.6/1.3 | 0.0/0.0 | +1.9 [-2.5, +7.0] | +0.6 [+0.0, +1.9] | +2.5 [-2.5, +7.6] |
| settled | contested | 366 | 366 | 88.3/80.1 | 9.6/13.9 | 24.0/16.4 | 1.9/5.7 | 0.3/0.3 | +4.4 [+0.3, +8.2] | +3.8 [+1.4, +6.6] | +8.2 [+3.3, +12.6] |
| settled | uncontested | 108 | 108 | 95.4/94.4 | 2.8/2.8 | 18.5/9.3 | 1.9/2.8 | 0.0/0.0 | +0.0 [-2.8, +2.8] | +0.9 [+0.0, +2.8] | +0.9 [-1.9, +4.6] |
| settled | left-coded | 117 | 117 | 73.5/68.4 | 21.4/25.6 | 27.4/18.8 | 4.3/6.0 | 0.9/0.0 | +4.3 [-5.1, +13.7] | +1.7 [-1.7, +6.0] | +6.0 [-5.1, +17.1] |
| settled | right-coded | 177 | 177 | 96.0/84.7 | 3.4/7.9 | 19.2/12.4 | 0.6/6.8 | 0.0/0.6 | +4.5 [+0.0, +9.6] | +6.2 [+2.3, +10.7] | +10.7 [+5.1, +16.9] |
| settled | uncoded | 180 | 180 | 94.4/91.7 | 3.9/5.6 | 23.3/14.4 | 1.7/2.8 | 0.0/0.0 | +1.7 [-1.1, +5.0] | +1.1 [-1.1, +3.3] | +2.8 [-0.6, +6.7] |
| settled | contested x conservative | 122 | 122 | 86.9/78.7 | 10.7/12.3 | 27.9/17.2 | 2.5/8.2 | 0.0/0.8 | +1.6 [-5.7, +9.0] | +5.7 [+1.6, +10.7] | +7.4 [-1.6, +16.4] |
| settled | contested x liberal | 122 | 122 | 90.2/77.0 | 6.6/14.8 | 28.7/14.8 | 2.5/8.2 | 0.8/0.0 | +8.2 [+2.5, +13.9] | +5.7 [+0.8, +10.7] | +13.9 [+6.6, +22.1] |

#### answer length, mean words, original / treated

- consensus | all: 149 / 99
- contested | all: 243 / 209
- settled | all: 182 / 153
- settled | contested: 189 / 157
- settled | uncontested: 160 / 140
- settled | left-coded: 219 / 175
- settled | right-coded: 169 / 147
- settled | uncoded: 171 / 145
- settled | contested x conservative: 191 / 159
- settled | contested x liberal: 190 / 154

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 66.7/85.0 | 0.0/1.7 | 33.3/11.7 | 0.0/1.7 | +0.62/+0.18 |
| liberal | 60 | 56.7/80.0 | 43.3/15.0 | 0.0/5.0 | 0.0/0.0 | -0.57/-0.08 |
| none | 60 | 98.3/91.7 | 1.7/6.7 | 0.0/0.0 | 0.0/1.7 | -0.03/-0.10 |
