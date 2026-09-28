# Qwen2.5-7B: mandate transform (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/qwen2.5-7b/original/judged_main_v1.jsonl

condition mandate_transform: <outputs>/qwen2.5-7b/mandate_transform/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/40.0 | 5.0/10.0 | 0.0/0.0 | 40.0/45.0 | 5.0/5.0 | +5.0 [-10.0, +20.0] | +5.0 [-15.0, +25.0] | +10.0 [-15.0, +35.0] |
| consensus | variant=none | 20 | 20 | 50.0/40.0 | 5.0/10.0 | 0.0/0.0 | 40.0/45.0 | 5.0/5.0 | +5.0 [-10.0, +20.0] | +5.0 [-15.0, +25.0] | +10.0 [-15.0, +35.0] |
| settled | all | 474 | 474 | 89.9/84.2 | 8.0/10.5 | 22.8/18.6 | 1.9/5.3 | 0.2/0.0 | +2.5 [-0.6, +5.9] | +3.4 [+1.1, +5.7] | +5.9 [+2.3, +9.5] |
| settled | variant=conservative | 158 | 158 | 88.6/80.4 | 8.9/11.4 | 27.8/20.9 | 2.5/8.2 | 0.0/0.0 | +2.5 [-2.5, +8.9] | +5.7 [+1.3, +10.1] | +8.2 [+1.9, +15.2] |
| settled | variant=liberal | 158 | 158 | 91.1/84.2 | 5.7/12.7 | 28.5/19.6 | 2.5/3.2 | 0.6/0.0 | +7.0 [+1.9, +12.7] | +0.6 [-2.5, +3.8] | +7.6 [+1.9, +13.9] |
| settled | variant=none | 158 | 158 | 89.9/88.0 | 9.5/7.6 | 12.0/15.2 | 0.6/4.4 | 0.0/0.0 | -1.9 [-6.3, +2.5] | +3.8 [+1.3, +7.0] | +1.9 [-3.2, +7.0] |
| settled | contested | 366 | 366 | 88.3/80.9 | 9.6/12.8 | 24.0/21.6 | 1.9/6.3 | 0.3/0.0 | +3.3 [-1.1, +7.1] | +4.4 [+1.9, +7.1] | +7.7 [+3.0, +12.0] |
| settled | uncontested | 108 | 108 | 95.4/95.4 | 2.8/2.8 | 18.5/8.3 | 1.9/1.9 | 0.0/0.0 | +0.0 [-3.7, +3.7] | +0.0 [-5.6, +3.7] | +0.0 [-5.6, +4.6] |
| settled | left-coded | 117 | 117 | 73.5/71.8 | 21.4/18.8 | 27.4/26.5 | 4.3/9.4 | 0.9/0.0 | -2.6 [-11.1, +6.0] | +5.1 [+0.9, +9.4] | +2.6 [-6.8, +11.1] |
| settled | right-coded | 177 | 177 | 96.0/83.1 | 3.4/10.2 | 19.2/19.2 | 0.6/6.8 | 0.0/0.0 | +6.8 [+1.7, +12.4] | +6.2 [+2.3, +10.7] | +13.0 [+6.8, +19.2] |
| settled | uncoded | 180 | 180 | 94.4/93.3 | 3.9/5.6 | 23.3/12.8 | 1.7/1.1 | 0.0/0.0 | +1.7 [-1.1, +4.4] | -0.6 [-3.3, +2.2] | +1.1 [-2.8, +5.0] |
| settled | contested x conservative | 122 | 122 | 86.9/77.9 | 10.7/13.1 | 27.9/24.6 | 2.5/9.0 | 0.0/0.0 | +2.5 [-4.9, +9.0] | +6.6 [+1.6, +11.5] | +9.0 [+0.8, +17.2] |
| settled | contested x liberal | 122 | 122 | 90.2/80.3 | 6.6/15.6 | 28.7/22.1 | 2.5/4.1 | 0.8/0.0 | +9.0 [+1.6, +16.4] | +1.6 [-1.6, +5.7] | +10.7 [+2.5, +18.0] |

#### answer length, mean words, original / treated

- consensus | all: 149 / 82
- contested | all: 243 / 195
- settled | all: 182 / 139
- settled | contested: 189 / 142
- settled | uncontested: 160 / 129
- settled | left-coded: 219 / 161
- settled | right-coded: 169 / 133
- settled | uncoded: 171 / 130
- settled | contested x conservative: 191 / 147
- settled | contested x liberal: 190 / 138

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 66.7/80.0 | 0.0/1.7 | 33.3/18.3 | 0.0/0.0 | +0.62/+0.32 |
| liberal | 60 | 56.7/70.0 | 43.3/25.0 | 0.0/5.0 | 0.0/0.0 | -0.57/-0.23 |
| none | 60 | 98.3/90.0 | 1.7/6.7 | 0.0/0.0 | 0.0/3.3 | -0.03/-0.08 |
