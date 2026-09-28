# Qwen3.8-27B: untransformed (ShareGPT) against the original, settled and consensus items, version 2

original: <outputs>/qwen3.8-27b/original/judged_main_v2.jsonl

condition untransformed: <outputs>/qwen3.8-27b/untransformed/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 75.0/75.0 | 0.0/0.0 | 0.0/0.0 | 25.0/20.0 | 0.0/5.0 | +0.0 [+0.0, +0.0] | -5.0 [-25.0, +15.0] | -5.0 [-25.0, +15.0] |
| consensus | variant=none | 20 | 20 | 75.0/75.0 | 0.0/0.0 | 0.0/0.0 | 25.0/20.0 | 0.0/5.0 | +0.0 [+0.0, +0.0] | -5.0 [-25.0, +15.0] | -5.0 [-25.0, +15.0] |
| settled | all | 474 | 474 | 98.3/98.3 | 0.4/0.2 | 3.2/2.5 | 0.4/1.5 | 0.8/0.0 | -0.2 [-0.6, +0.0] | +1.1 [-0.4, +3.0] | +0.8 [-0.6, +2.7] |
| settled | variant=conservative | 158 | 158 | 99.4/97.5 | 0.0/0.0 | 2.5/3.2 | 0.0/2.5 | 0.6/0.0 | +0.0 [+0.0, +0.0] | +2.5 [+0.6, +5.1] | +2.5 [+0.6, +5.1] |
| settled | variant=liberal | 158 | 158 | 99.4/98.7 | 0.0/0.0 | 5.1/4.4 | 0.6/1.3 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.6 [-1.3, +3.2] | +0.6 [-1.3, +3.2] |
| settled | variant=none | 158 | 158 | 96.2/98.7 | 1.3/0.6 | 1.9/0.0 | 0.6/0.6 | 1.9/0.0 | -0.6 [-1.9, +0.0] | +0.0 [-1.9, +1.9] | -0.6 [-2.5, +1.3] |
| settled | contested | 366 | 366 | 98.6/97.8 | 0.5/0.3 | 3.6/2.7 | 0.3/1.9 | 0.5/0.0 | -0.3 [-0.8, +0.0] | +1.6 [-0.3, +4.1] | +1.4 [-0.5, +3.8] |
| settled | uncontested | 108 | 108 | 97.2/100.0 | 0.0/0.0 | 1.9/1.9 | 0.9/0.0 | 1.9/0.0 | +0.0 [+0.0, +0.0] | -0.9 [-2.8, +0.0] | -0.9 [-2.8, +0.0] |
| settled | left-coded | 78 | 78 | 100.0/100.0 | 0.0/0.0 | 6.4/5.1 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | right-coded | 177 | 177 | 98.3/96.0 | 0.0/0.0 | 2.8/1.1 | 0.6/4.0 | 1.1/0.0 | +0.0 [+0.0, +0.0] | +3.4 [-0.6, +8.5] | +3.4 [-0.6, +8.5] |
| settled | uncoded | 219 | 219 | 97.7/99.5 | 0.9/0.5 | 2.3/2.7 | 0.5/0.0 | 0.9/0.0 | -0.5 [-1.4, +0.0] | -0.5 [-1.4, +0.0] | -0.9 [-2.3, +0.0] |
| settled | contested x conservative | 122 | 122 | 100.0/96.7 | 0.0/0.0 | 2.5/3.3 | 0.0/3.3 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +3.3 [+0.8, +6.6] | +3.3 [+0.8, +6.6] |
| settled | contested x liberal | 122 | 122 | 99.2/98.4 | 0.0/0.0 | 5.7/4.9 | 0.8/1.6 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.8 [-1.6, +4.1] | +0.8 [-1.6, +4.1] |

#### answer length, mean words, original / treated

- consensus | all: 174 / 172
- contested | all: 219 / 216
- settled | all: 190 / 189
- settled | contested: 195 / 194
- settled | uncontested: 175 / 172
- settled | left-coded: 202 / 203
- settled | right-coded: 191 / 189
- settled | uncoded: 186 / 183
- settled | contested x conservative: 196 / 196
- settled | contested x liberal: 192 / 189

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 58.3/73.3 | 0.0/0.0 | 40.0/20.0 | 1.7/6.7 | +0.78/+0.40 |
| liberal | 60 | 83.3/80.0 | 15.0/11.7 | 0.0/0.0 | 1.7/8.3 | -0.20/-0.15 |
| none | 60 | 100.0/96.7 | 0.0/1.7 | 0.0/1.7 | 0.0/0.0 | +0.00/+0.02 |
