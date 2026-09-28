# Gemma-4-31B: untransformed (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/gemma-4-31b/original/judged_main_v1.jsonl

condition untransformed: <outputs>/gemma-4-31b/untransformed/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 80.0/80.0 | 5.0/0.0 | 5.0/0.0 | 10.0/10.0 | 5.0/10.0 | -5.0 [-15.0, +0.0] | +0.0 [-15.0, +15.0] | -5.0 [-20.0, +10.0] |
| consensus | variant=none | 20 | 20 | 80.0/80.0 | 5.0/0.0 | 5.0/0.0 | 10.0/10.0 | 5.0/10.0 | -5.0 [-15.0, +0.0] | +0.0 [-15.0, +15.0] | -5.0 [-20.0, +10.0] |
| settled | all | 474 | 474 | 91.4/89.7 | 8.2/9.1 | 3.8/2.5 | 0.2/1.1 | 0.2/0.2 | +0.8 [-1.3, +3.0] | +0.8 [+0.0, +2.1] | +1.7 [-0.2, +3.8] |
| settled | variant=conservative | 158 | 158 | 86.1/84.8 | 13.3/14.6 | 4.4/2.5 | 0.6/0.6 | 0.0/0.0 | +1.3 [-3.2, +5.7] | +0.0 [+0.0, +0.0] | +1.3 [-3.2, +5.7] |
| settled | variant=liberal | 158 | 158 | 93.7/91.8 | 5.7/6.3 | 4.4/1.9 | 0.0/1.3 | 0.6/0.6 | +0.6 [-2.5, +3.8] | +1.3 [+0.0, +3.2] | +1.9 [-1.3, +5.1] |
| settled | variant=none | 158 | 158 | 94.3/92.4 | 5.7/6.3 | 2.5/3.2 | 0.0/1.3 | 0.0/0.0 | +0.6 [-1.9, +3.2] | +1.3 [+0.0, +3.2] | +1.9 [-0.6, +5.1] |
| settled | contested | 366 | 366 | 89.6/88.0 | 10.1/11.7 | 4.1/2.7 | 0.0/0.0 | 0.3/0.3 | +1.6 [-0.8, +4.1] | +0.0 [+0.0, +0.0] | +1.6 [-0.8, +4.1] |
| settled | uncontested | 108 | 108 | 97.2/95.4 | 1.9/0.0 | 2.8/1.9 | 0.9/4.6 | 0.0/0.0 | -1.9 [-5.6, +0.0] | +3.7 [+0.0, +9.3] | +1.9 [+0.0, +5.6] |
| settled | left-coded | 117 | 117 | 86.3/82.9 | 13.7/17.1 | 8.5/5.1 | 0.0/0.0 | 0.0/0.0 | +3.4 [-1.7, +9.4] | +0.0 [+0.0, +0.0] | +3.4 [-1.7, +9.4] |
| settled | right-coded | 177 | 177 | 91.5/91.0 | 7.9/8.5 | 2.8/0.6 | 0.0/0.0 | 0.6/0.6 | +0.6 [-1.7, +2.8] | +0.0 [+0.0, +0.0] | +0.6 [-1.7, +2.8] |
| settled | uncoded | 180 | 180 | 94.4/92.8 | 5.0/4.4 | 1.7/2.8 | 0.6/2.8 | 0.0/0.0 | -0.6 [-3.9, +2.8] | +2.2 [+0.0, +5.6] | +1.7 [-1.1, +5.0] |
| settled | contested x conservative | 122 | 122 | 82.8/81.1 | 17.2/18.9 | 4.1/2.5 | 0.0/0.0 | 0.0/0.0 | +1.6 [-4.1, +7.4] | +0.0 [+0.0, +0.0] | +1.6 [-4.1, +7.4] |
| settled | contested x liberal | 122 | 122 | 92.6/91.0 | 6.6/8.2 | 4.9/1.6 | 0.0/0.0 | 0.8/0.8 | +1.6 [-2.5, +5.7] | +0.0 [+0.0, +0.0] | +1.6 [-2.5, +5.7] |

#### answer length, mean words, original / treated

- consensus | all: 178 / 151
- contested | all: 234 / 235
- settled | all: 193 / 188
- settled | contested: 202 / 198
- settled | uncontested: 160 / 154
- settled | left-coded: 221 / 223
- settled | right-coded: 190 / 181
- settled | uncoded: 177 / 172
- settled | contested x conservative: 208 / 204
- settled | contested x liberal: 194 / 186

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 68.3/73.3 | 0.0/0.0 | 31.7/26.7 | 0.0/0.0 | +0.63/+0.53 |
| liberal | 60 | 90.0/91.7 | 10.0/8.3 | 0.0/0.0 | 0.0/0.0 | -0.10/-0.10 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
