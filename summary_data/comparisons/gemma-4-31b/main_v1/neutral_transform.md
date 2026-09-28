# Gemma-4-31B: neutral transform (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/gemma-4-31b/original/judged_main_v1.jsonl

condition neutral_transform: <outputs>/gemma-4-31b/neutral_transform/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 80.0/85.0 | 5.0/0.0 | 5.0/0.0 | 10.0/10.0 | 5.0/5.0 | -5.0 [-15.0, +0.0] | +0.0 [-15.0, +15.0] | -5.0 [-20.0, +10.0] |
| consensus | variant=none | 20 | 20 | 80.0/85.0 | 5.0/0.0 | 5.0/0.0 | 10.0/10.0 | 5.0/5.0 | -5.0 [-15.0, +0.0] | +0.0 [-15.0, +15.0] | -5.0 [-20.0, +10.0] |
| settled | all | 474 | 474 | 91.4/89.0 | 8.2/10.3 | 3.8/1.7 | 0.2/0.4 | 0.2/0.2 | +2.1 [-0.2, +4.6] | +0.2 [+0.0, +0.6] | +2.3 [+0.2, +4.9] |
| settled | variant=conservative | 158 | 158 | 86.1/82.9 | 13.3/16.5 | 4.4/2.5 | 0.6/0.6 | 0.0/0.0 | +3.2 [-1.3, +7.6] | +0.0 [+0.0, +0.0] | +3.2 [-1.3, +7.6] |
| settled | variant=liberal | 158 | 158 | 93.7/90.5 | 5.7/8.9 | 4.4/1.3 | 0.0/0.0 | 0.6/0.6 | +3.2 [-0.6, +7.0] | +0.0 [+0.0, +0.0] | +3.2 [-0.6, +7.0] |
| settled | variant=none | 158 | 158 | 94.3/93.7 | 5.7/5.7 | 2.5/1.3 | 0.0/0.6 | 0.0/0.0 | +0.0 [-3.8, +3.8] | +0.6 [+0.0, +1.9] | +0.6 [-2.5, +4.4] |
| settled | contested | 366 | 366 | 89.6/86.6 | 10.1/12.8 | 4.1/2.2 | 0.0/0.3 | 0.3/0.3 | +2.7 [-0.3, +5.7] | +0.3 [+0.0, +0.8] | +3.0 [+0.3, +6.0] |
| settled | uncontested | 108 | 108 | 97.2/97.2 | 1.9/1.9 | 2.8/0.0 | 0.9/0.9 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | left-coded | 117 | 117 | 86.3/79.5 | 13.7/20.5 | 8.5/4.3 | 0.0/0.0 | 0.0/0.0 | +6.8 [+0.9, +13.7] | +0.0 [+0.0, +0.0] | +6.8 [+0.9, +13.7] |
| settled | right-coded | 177 | 177 | 91.5/92.1 | 7.9/6.8 | 2.8/1.1 | 0.0/0.6 | 0.6/0.6 | -1.1 [-3.4, +1.1] | +0.6 [+0.0, +1.7] | -0.6 [-2.3, +1.1] |
| settled | uncoded | 180 | 180 | 94.4/92.2 | 5.0/7.2 | 1.7/0.6 | 0.6/0.6 | 0.0/0.0 | +2.2 [-1.1, +6.1] | +0.0 [+0.0, +0.0] | +2.2 [-1.1, +6.1] |
| settled | contested x conservative | 122 | 122 | 82.8/78.7 | 17.2/21.3 | 4.1/3.3 | 0.0/0.0 | 0.0/0.0 | +4.1 [-1.6, +9.8] | +0.0 [+0.0, +0.0] | +4.1 [-1.6, +9.8] |
| settled | contested x liberal | 122 | 122 | 92.6/88.5 | 6.6/10.7 | 4.9/1.6 | 0.0/0.0 | 0.8/0.8 | +4.1 [-0.8, +9.0] | +0.0 [+0.0, +0.0] | +4.1 [-0.8, +9.0] |

#### answer length, mean words, original / treated

- consensus | all: 178 / 143
- contested | all: 234 / 235
- settled | all: 193 / 185
- settled | contested: 202 / 196
- settled | uncontested: 160 / 147
- settled | left-coded: 221 / 221
- settled | right-coded: 190 / 177
- settled | uncoded: 177 / 168
- settled | contested x conservative: 208 / 203
- settled | contested x liberal: 194 / 182

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 68.3/76.7 | 0.0/0.0 | 31.7/23.3 | 0.0/0.0 | +0.63/+0.48 |
| liberal | 60 | 90.0/91.7 | 10.0/8.3 | 0.0/0.0 | 0.0/0.0 | -0.10/-0.08 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
