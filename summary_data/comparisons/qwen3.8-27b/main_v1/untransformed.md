# Qwen3.8-27B: untransformed (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/qwen3.8-27b/original/judged_main_v1.jsonl

condition untransformed: <outputs>/qwen3.8-27b/untransformed/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 75.0/75.0 | 0.0/5.0 | 5.0/0.0 | 20.0/15.0 | 5.0/5.0 | +5.0 [+0.0, +15.0] | -5.0 [-20.0, +10.0] | +0.0 [-20.0, +20.0] |
| consensus | variant=none | 20 | 20 | 75.0/75.0 | 0.0/5.0 | 5.0/0.0 | 20.0/15.0 | 5.0/5.0 | +5.0 [+0.0, +15.0] | -5.0 [-20.0, +10.0] | +0.0 [-20.0, +20.0] |
| settled | all | 474 | 474 | 98.5/99.2 | 0.8/0.4 | 4.6/3.2 | 0.2/0.4 | 0.4/0.0 | -0.4 [-1.1, +0.0] | +0.2 [-0.6, +1.3] | -0.2 [-1.3, +1.1] |
| settled | variant=conservative | 158 | 158 | 100.0/98.7 | 0.0/0.6 | 5.7/3.8 | 0.0/0.6 | 0.0/0.0 | +0.6 [+0.0, +1.9] | +0.6 [+0.0, +1.9] | +1.3 [+0.0, +3.2] |
| settled | variant=liberal | 158 | 158 | 99.4/99.4 | 0.6/0.0 | 5.1/4.4 | 0.0/0.6 | 0.0/0.0 | -0.6 [-1.9, +0.0] | +0.6 [+0.0, +1.9] | +0.0 [-1.9, +1.9] |
| settled | variant=none | 158 | 158 | 96.2/99.4 | 1.9/0.6 | 3.2/1.3 | 0.6/0.0 | 1.3/0.0 | -1.3 [-3.2, +0.0] | -0.6 [-1.9, +0.0] | -1.9 [-3.8, +0.0] |
| settled | contested | 366 | 366 | 98.4/98.9 | 1.1/0.5 | 5.5/3.6 | 0.0/0.5 | 0.5/0.0 | -0.5 [-1.4, +0.0] | +0.5 [+0.0, +1.6] | +0.0 [-1.1, +1.6] |
| settled | uncontested | 108 | 108 | 99.1/100.0 | 0.0/0.0 | 1.9/1.9 | 0.9/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -0.9 [-2.8, +0.0] | -0.9 [-2.8, +0.0] |
| settled | left-coded | 117 | 117 | 98.3/99.1 | 1.7/0.9 | 9.4/5.1 | 0.0/0.0 | 0.0/0.0 | -0.9 [-2.6, +0.0] | +0.0 [+0.0, +0.0] | -0.9 [-2.6, +0.0] |
| settled | right-coded | 177 | 177 | 98.9/98.9 | 0.0/0.0 | 4.0/1.7 | 0.0/1.1 | 1.1/0.0 | +0.0 [+0.0, +0.0] | +1.1 [+0.0, +3.4] | +1.1 [+0.0, +3.4] |
| settled | uncoded | 180 | 180 | 98.3/99.4 | 1.1/0.6 | 2.2/3.3 | 0.6/0.0 | 0.0/0.0 | -0.6 [-1.7, +0.0] | -0.6 [-1.7, +0.0] | -1.1 [-2.8, +0.0] |
| settled | contested x conservative | 122 | 122 | 100.0/98.4 | 0.0/0.8 | 5.7/4.1 | 0.0/0.8 | 0.0/0.0 | +0.8 [+0.0, +2.5] | +0.8 [+0.0, +2.5] | +1.6 [+0.0, +4.1] |
| settled | contested x liberal | 122 | 122 | 99.2/99.2 | 0.8/0.0 | 6.6/4.9 | 0.0/0.8 | 0.0/0.0 | -0.8 [-2.5, +0.0] | +0.8 [+0.0, +2.5] | +0.0 [-2.5, +2.5] |

#### answer length, mean words, original / treated

- consensus | all: 176 / 181
- contested | all: 219 / 216
- settled | all: 192 / 189
- settled | contested: 196 / 193
- settled | uncontested: 178 / 174
- settled | left-coded: 204 / 203
- settled | right-coded: 192 / 190
- settled | uncoded: 184 / 179
- settled | contested x conservative: 198 / 197
- settled | contested x liberal: 195 / 189

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 65.0/68.3 | 0.0/0.0 | 33.3/26.7 | 1.7/5.0 | +0.65/+0.53 |
| liberal | 60 | 81.7/83.3 | 16.7/10.0 | 0.0/0.0 | 1.7/6.7 | -0.22/-0.15 |
| none | 60 | 100.0/96.7 | 0.0/1.7 | 0.0/1.7 | 0.0/0.0 | +0.00/+0.02 |
