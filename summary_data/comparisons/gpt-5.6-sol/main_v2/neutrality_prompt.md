# GPT-5.6-sol: neutrality prompt against the original, settled and consensus items, version 2

original: <outputs>/gpt-5.6-sol/original/judged_main_v2.jsonl

condition neutrality_prompt: <outputs>/gpt-5.6-sol/neutrality_prompt/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 100.0/95.0 | 0.0/5.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +5.0 [+0.0, +15.0] | +0.0 [+0.0, +0.0] | +5.0 [+0.0, +15.0] |
| consensus | variant=none | 20 | 20 | 100.0/95.0 | 0.0/5.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +5.0 [+0.0, +15.0] | +0.0 [+0.0, +0.0] | +5.0 [+0.0, +15.0] |
| settled | all | 474 | 474 | 99.2/98.5 | 0.4/1.3 | 17.1/19.2 | 0.4/0.2 | 0.0/0.0 | +0.8 [-0.2, +2.1] | -0.2 [-0.6, +0.0] | +0.6 [-0.4, +2.1] |
| settled | variant=conservative | 158 | 158 | 99.4/98.7 | 0.0/1.3 | 19.6/22.8 | 0.6/0.0 | 0.0/0.0 | +1.3 [+0.0, +3.2] | -0.6 [-1.9, +0.0] | +0.6 [-1.3, +3.2] |
| settled | variant=liberal | 158 | 158 | 99.4/98.1 | 0.6/1.3 | 22.8/22.2 | 0.0/0.6 | 0.0/0.0 | +0.6 [+0.0, +1.9] | +0.6 [+0.0, +1.9] | +1.3 [+0.0, +3.2] |
| settled | variant=none | 158 | 158 | 98.7/98.7 | 0.6/1.3 | 8.9/12.7 | 0.6/0.0 | 0.0/0.0 | +0.6 [-1.3, +2.5] | -0.6 [-1.9, +0.0] | +0.0 [-2.5, +2.5] |
| settled | contested | 366 | 366 | 98.9/98.4 | 0.5/1.4 | 16.9/19.7 | 0.5/0.3 | 0.0/0.0 | +0.8 [-0.5, +2.5] | -0.3 [-0.8, +0.0] | +0.5 [-0.8, +2.2] |
| settled | uncontested | 108 | 108 | 100.0/99.1 | 0.0/0.9 | 17.6/17.6 | 0.0/0.0 | 0.0/0.0 | +0.9 [+0.0, +2.8] | +0.0 [+0.0, +0.0] | +0.9 [+0.0, +2.8] |
| settled | left-coded | 78 | 78 | 98.7/98.7 | 0.0/1.3 | 24.4/23.1 | 1.3/0.0 | 0.0/0.0 | +1.3 [+0.0, +3.8] | -1.3 [-3.8, +0.0] | +0.0 [-3.8, +3.8] |
| settled | right-coded | 177 | 177 | 99.4/99.4 | 0.0/0.0 | 15.3/19.8 | 0.6/0.6 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | uncoded | 219 | 219 | 99.1/97.7 | 0.9/2.3 | 16.0/17.4 | 0.0/0.0 | 0.0/0.0 | +1.4 [-0.5, +4.1] | +0.0 [+0.0, +0.0] | +1.4 [-0.5, +4.1] |
| settled | contested x conservative | 122 | 122 | 99.2/99.2 | 0.0/0.8 | 18.9/23.8 | 0.8/0.0 | 0.0/0.0 | +0.8 [+0.0, +2.5] | -0.8 [-2.5, +0.0] | +0.0 [-2.5, +2.5] |
| settled | contested x liberal | 122 | 122 | 99.2/97.5 | 0.8/1.6 | 22.1/22.1 | 0.0/0.8 | 0.0/0.0 | +0.8 [+0.0, +2.5] | +0.8 [+0.0, +2.5] | +1.6 [+0.0, +4.1] |

#### answer length, mean words, original / treated

- consensus | all: 47 / 69
- contested | all: 187 / 246
- settled | all: 107 / 125
- settled | contested: 118 / 138
- settled | uncontested: 71 / 81
- settled | left-coded: 138 / 159
- settled | right-coded: 112 / 129
- settled | uncoded: 92 / 109
- settled | contested x conservative: 126 / 144
- settled | contested x liberal: 112 / 129

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 38.3/91.7 | 5.0/0.0 | 56.7/8.3 | 0.0/0.0 | +0.82/+0.10 |
| liberal | 60 | 28.3/98.3 | 70.0/1.7 | 1.7/0.0 | 0.0/0.0 | -0.78/-0.02 |
| none | 60 | 48.3/98.3 | 48.3/1.7 | 3.3/0.0 | 0.0/0.0 | -0.53/-0.02 |
