# Qwen2.5-7B: assertive transform (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/qwen2.5-7b/original/judged_main_v1.jsonl

condition assertive_transform: <outputs>/qwen2.5-7b/assertive_transform/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/35.0 | 5.0/10.0 | 0.0/0.0 | 40.0/50.0 | 5.0/5.0 | +5.0 [-10.0, +20.0] | +10.0 [-20.0, +40.0] | +15.0 [-15.0, +45.0] |
| consensus | variant=none | 20 | 20 | 50.0/35.0 | 5.0/10.0 | 0.0/0.0 | 40.0/50.0 | 5.0/5.0 | +5.0 [-10.0, +20.0] | +10.0 [-20.0, +40.0] | +15.0 [-15.0, +45.0] |
| settled | all | 474 | 474 | 89.9/82.5 | 8.0/12.0 | 22.8/17.1 | 1.9/5.5 | 0.2/0.0 | +4.0 [+1.1, +7.0] | +3.6 [+1.1, +6.3] | +7.6 [+4.2, +11.2] |
| settled | variant=conservative | 158 | 158 | 88.6/79.7 | 8.9/13.9 | 27.8/16.5 | 2.5/6.3 | 0.0/0.0 | +5.1 [-0.6, +10.8] | +3.8 [+0.0, +7.6] | +8.9 [+2.5, +15.2] |
| settled | variant=liberal | 158 | 158 | 91.1/84.8 | 5.7/10.1 | 28.5/21.5 | 2.5/5.1 | 0.6/0.0 | +4.4 [-0.6, +10.1] | +2.5 [-1.3, +6.3] | +7.0 [+0.6, +13.3] |
| settled | variant=none | 158 | 158 | 89.9/82.9 | 9.5/12.0 | 12.0/13.3 | 0.6/5.1 | 0.0/0.0 | +2.5 [-2.5, +7.6] | +4.4 [+1.3, +7.6] | +7.0 [+1.3, +12.7] |
| settled | contested | 366 | 366 | 88.3/79.2 | 9.6/14.8 | 24.0/19.1 | 1.9/6.0 | 0.3/0.0 | +5.2 [+1.6, +8.7] | +4.1 [+1.1, +7.1] | +9.3 [+5.2, +13.4] |
| settled | uncontested | 108 | 108 | 95.4/93.5 | 2.8/2.8 | 18.5/10.2 | 1.9/3.7 | 0.0/0.0 | +0.0 [-5.6, +4.6] | +1.9 [-4.6, +7.4] | +1.9 [-4.6, +8.3] |
| settled | left-coded | 117 | 117 | 73.5/62.4 | 21.4/25.6 | 27.4/22.2 | 4.3/12.0 | 0.9/0.0 | +4.3 [-4.3, +12.8] | +7.7 [+0.9, +16.2] | +12.0 [+2.6, +21.4] |
| settled | right-coded | 177 | 177 | 96.0/88.1 | 3.4/7.9 | 19.2/14.7 | 0.6/4.0 | 0.0/0.0 | +4.5 [+0.0, +9.0] | +3.4 [+0.0, +7.3] | +7.9 [+2.8, +13.6] |
| settled | uncoded | 180 | 180 | 94.4/90.0 | 3.9/7.2 | 23.3/16.1 | 1.7/2.8 | 0.0/0.0 | +3.3 [-0.6, +7.2] | +1.1 [-2.2, +5.0] | +4.4 [-0.6, +8.9] |
| settled | contested x conservative | 122 | 122 | 86.9/77.0 | 10.7/16.4 | 27.9/19.7 | 2.5/6.6 | 0.0/0.0 | +5.7 [-0.8, +13.1] | +4.1 [+0.0, +8.2] | +9.8 [+2.5, +17.2] |
| settled | contested x liberal | 122 | 122 | 90.2/82.8 | 6.6/12.3 | 28.7/22.1 | 2.5/4.9 | 0.8/0.0 | +5.7 [-0.8, +13.1] | +2.5 [-1.6, +6.6] | +8.2 [+1.6, +15.6] |

#### answer length, mean words, original / treated

- consensus | all: 149 / 83
- contested | all: 243 / 208
- settled | all: 182 / 146
- settled | contested: 189 / 150
- settled | uncontested: 160 / 132
- settled | left-coded: 219 / 165
- settled | right-coded: 169 / 143
- settled | uncoded: 171 / 137
- settled | contested x conservative: 191 / 154
- settled | contested x liberal: 190 / 146

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 66.7/76.7 | 0.0/3.3 | 33.3/20.0 | 0.0/0.0 | +0.62/+0.32 |
| liberal | 60 | 56.7/70.0 | 43.3/25.0 | 0.0/5.0 | 0.0/0.0 | -0.57/-0.27 |
| none | 60 | 98.3/86.7 | 1.7/10.0 | 0.0/0.0 | 0.0/3.3 | -0.03/-0.12 |
