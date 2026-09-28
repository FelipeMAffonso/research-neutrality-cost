# Qwen2.5-7B: mandate transform (ShareGPT) against the original, settled and consensus items, version 2

original: <outputs>/qwen2.5-7b/original/judged_main_v2.jsonl

condition mandate_transform: <outputs>/qwen2.5-7b/mandate_transform/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/60.0 | 15.0/5.0 | 0.0/0.0 | 25.0/30.0 | 10.0/5.0 | -10.0 [-30.0, +10.0] | +5.0 [+0.0, +15.0] | -5.0 [-20.0, +10.0] |
| consensus | variant=none | 20 | 20 | 50.0/60.0 | 15.0/5.0 | 0.0/0.0 | 25.0/30.0 | 10.0/5.0 | -10.0 [-30.0, +10.0] | +5.0 [+0.0, +15.0] | -5.0 [-20.0, +10.0] |
| settled | all | 474 | 474 | 90.5/85.4 | 8.0/10.1 | 21.5/16.5 | 1.5/4.4 | 0.0/0.0 | +2.1 [-1.7, +6.1] | +3.0 [+1.1, +5.1] | +5.1 [+1.1, +9.3] |
| settled | variant=conservative | 158 | 158 | 88.0/82.3 | 8.9/12.0 | 26.6/21.5 | 3.2/5.7 | 0.0/0.0 | +3.2 [-2.5, +8.9] | +2.5 [-1.9, +7.0] | +5.7 [-0.6, +12.0] |
| settled | variant=liberal | 158 | 158 | 90.5/88.0 | 8.2/8.2 | 23.4/12.7 | 1.3/3.8 | 0.0/0.0 | +0.0 [-5.1, +5.1] | +2.5 [+0.0, +5.7] | +2.5 [-3.2, +8.2] |
| settled | variant=none | 158 | 158 | 93.0/86.1 | 7.0/10.1 | 14.6/15.2 | 0.0/3.8 | 0.0/0.0 | +3.2 [-1.9, +8.2] | +3.8 [+1.3, +7.0] | +7.0 [+1.3, +12.7] |
| settled | contested | 366 | 366 | 89.1/82.5 | 9.0/12.6 | 22.7/18.6 | 1.9/4.9 | 0.0/0.0 | +3.6 [-1.4, +8.2] | +3.0 [+0.8, +5.5] | +6.6 [+1.4, +11.5] |
| settled | uncontested | 108 | 108 | 95.4/95.4 | 4.6/1.9 | 17.6/9.3 | 0.0/2.8 | 0.0/0.0 | -2.8 [-7.4, +0.0] | +2.8 [+0.0, +6.5] | +0.0 [-2.8, +2.8] |
| settled | left-coded | 78 | 78 | 76.9/78.2 | 21.8/15.4 | 34.6/30.8 | 1.3/6.4 | 0.0/0.0 | -6.4 [-19.2, +5.1] | +5.1 [+0.0, +11.5] | -1.3 [-15.4, +11.5] |
| settled | right-coded | 177 | 177 | 93.8/85.9 | 3.4/7.9 | 16.9/14.1 | 2.8/6.2 | 0.0/0.0 | +4.5 [-0.6, +9.6] | +3.4 [+0.0, +7.3] | +7.9 [+2.3, +14.1] |
| settled | uncoded | 219 | 219 | 92.7/87.7 | 6.8/10.0 | 20.5/13.2 | 0.5/2.3 | 0.0/0.0 | +3.2 [-2.3, +9.1] | +1.8 [+0.0, +4.1] | +5.0 [+0.0, +10.5] |
| settled | contested x conservative | 122 | 122 | 86.1/78.7 | 9.8/15.6 | 29.5/22.1 | 4.1/5.7 | 0.0/0.0 | +5.7 [-1.6, +13.1] | +1.6 [-4.1, +6.6] | +7.4 [-0.8, +15.6] |
| settled | contested x liberal | 122 | 122 | 89.3/86.1 | 9.0/9.0 | 21.3/14.8 | 1.6/4.9 | 0.0/0.0 | +0.0 [-6.6, +6.6] | +3.3 [+0.0, +7.4] | +3.3 [-3.3, +10.7] |

#### answer length, mean words, original / treated

- consensus | all: 146 / 79
- contested | all: 243 / 197
- settled | all: 182 / 139
- settled | contested: 189 / 142
- settled | uncontested: 160 / 129
- settled | left-coded: 219 / 161
- settled | right-coded: 171 / 132
- settled | uncoded: 179 / 137
- settled | contested x conservative: 193 / 144
- settled | contested x liberal: 189 / 141

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 65.0/86.7 | 0.0/0.0 | 35.0/13.3 | 0.0/0.0 | +0.63/+0.20 |
| liberal | 60 | 50.0/70.0 | 50.0/26.7 | 0.0/3.3 | 0.0/0.0 | -0.63/-0.25 |
| none | 60 | 98.3/95.0 | 1.7/5.0 | 0.0/0.0 | 0.0/0.0 | -0.03/-0.07 |
