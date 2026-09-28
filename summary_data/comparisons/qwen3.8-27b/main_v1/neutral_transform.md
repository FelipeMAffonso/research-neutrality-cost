# Qwen3.8-27B: neutral transform (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/qwen3.8-27b/original/judged_main_v1.jsonl

condition neutral_transform: <outputs>/qwen3.8-27b/neutral_transform/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 75.0/75.0 | 0.0/0.0 | 5.0/0.0 | 20.0/20.0 | 5.0/5.0 | +0.0 [+0.0, +0.0] | +0.0 [-20.0, +20.0] | +0.0 [-20.0, +20.0] |
| consensus | variant=none | 20 | 20 | 75.0/75.0 | 0.0/0.0 | 5.0/0.0 | 20.0/20.0 | 5.0/5.0 | +0.0 [+0.0, +0.0] | +0.0 [-20.0, +20.0] | +0.0 [-20.0, +20.0] |
| settled | all | 474 | 474 | 98.5/98.3 | 0.8/0.8 | 4.6/3.8 | 0.2/0.6 | 0.4/0.2 | +0.0 [-0.8, +0.8] | +0.4 [-0.4, +1.5] | +0.4 [-0.8, +1.9] |
| settled | variant=conservative | 158 | 158 | 100.0/97.5 | 0.0/1.9 | 5.7/5.1 | 0.0/0.6 | 0.0/0.0 | +1.9 [+0.0, +4.4] | +0.6 [+0.0, +1.9] | +2.5 [+0.6, +5.1] |
| settled | variant=liberal | 158 | 158 | 99.4/98.1 | 0.6/0.6 | 5.1/4.4 | 0.0/1.3 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +1.3 [+0.0, +3.2] | +1.3 [+0.0, +3.2] |
| settled | variant=none | 158 | 158 | 96.2/99.4 | 1.9/0.0 | 3.2/1.9 | 0.6/0.0 | 1.3/0.6 | -1.9 [-4.4, +0.0] | -0.6 [-1.9, +0.0] | -2.5 [-5.1, -0.6] |
| settled | contested | 366 | 366 | 98.4/97.8 | 1.1/1.1 | 5.5/4.4 | 0.0/0.8 | 0.5/0.3 | +0.0 [-1.1, +1.1] | +0.8 [+0.0, +2.2] | +0.8 [-0.5, +2.7] |
| settled | uncontested | 108 | 108 | 99.1/100.0 | 0.0/0.0 | 1.9/1.9 | 0.9/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -0.9 [-2.8, +0.0] | -0.9 [-2.8, +0.0] |
| settled | left-coded | 117 | 117 | 98.3/98.3 | 1.7/1.7 | 9.4/6.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [-2.6, +2.6] | +0.0 [+0.0, +0.0] | +0.0 [-2.6, +2.6] |
| settled | right-coded | 177 | 177 | 98.9/97.7 | 0.0/0.0 | 4.0/2.3 | 0.0/1.7 | 1.1/0.6 | +0.0 [+0.0, +0.0] | +1.7 [+0.0, +4.5] | +1.7 [+0.0, +4.5] |
| settled | uncoded | 180 | 180 | 98.3/98.9 | 1.1/1.1 | 2.2/3.9 | 0.6/0.0 | 0.0/0.0 | +0.0 [-1.7, +1.7] | -0.6 [-1.7, +0.0] | -0.6 [-2.2, +1.1] |
| settled | contested x conservative | 122 | 122 | 100.0/96.7 | 0.0/2.5 | 5.7/5.7 | 0.0/0.8 | 0.0/0.0 | +2.5 [+0.0, +5.7] | +0.8 [+0.0, +2.5] | +3.3 [+0.8, +7.4] |
| settled | contested x liberal | 122 | 122 | 99.2/97.5 | 0.8/0.8 | 6.6/4.9 | 0.0/1.6 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +1.6 [+0.0, +4.1] | +1.6 [+0.0, +4.1] |

#### answer length, mean words, original / treated

- consensus | all: 176 / 177
- contested | all: 219 / 218
- settled | all: 192 / 190
- settled | contested: 196 / 194
- settled | uncontested: 178 / 176
- settled | left-coded: 204 / 206
- settled | right-coded: 192 / 191
- settled | uncoded: 184 / 179
- settled | contested x conservative: 198 / 196
- settled | contested x liberal: 195 / 193

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 65.0/68.3 | 0.0/0.0 | 33.3/28.3 | 1.7/3.3 | +0.65/+0.55 |
| liberal | 60 | 81.7/80.0 | 16.7/16.7 | 0.0/0.0 | 1.7/3.3 | -0.22/-0.18 |
| none | 60 | 100.0/98.3 | 0.0/0.0 | 0.0/1.7 | 0.0/0.0 | +0.00/+0.03 |
