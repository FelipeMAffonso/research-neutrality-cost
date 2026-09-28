# GPT-5.6-luna: neutrality prompt against the original, settled and consensus items, version 2

original: <outputs>/gpt-5.6-luna/original/judged_main_v2.jsonl

condition neutrality_prompt: <outputs>/gpt-5.6-luna/neutrality_prompt/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| consensus | variant=none | 20 | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 474 | 474 | 99.4/97.9 | 0.4/2.1 | 14.8/12.7 | 0.2/0.0 | 0.0/0.0 | +1.7 [+0.2, +3.2] | -0.2 [-0.6, +0.0] | +1.5 [+0.2, +2.7] |
| settled | variant=conservative | 158 | 158 | 99.4/96.8 | 0.6/3.2 | 17.1/17.7 | 0.0/0.0 | 0.0/0.0 | +2.5 [+0.6, +5.1] | +0.0 [+0.0, +0.0] | +2.5 [+0.6, +5.1] |
| settled | variant=liberal | 158 | 158 | 98.7/98.1 | 0.6/1.9 | 19.0/12.0 | 0.6/0.0 | 0.0/0.0 | +1.3 [-1.3, +3.8] | -0.6 [-1.9, +0.0] | +0.6 [-1.9, +3.2] |
| settled | variant=none | 158 | 158 | 100.0/98.7 | 0.0/1.3 | 8.2/8.2 | 0.0/0.0 | 0.0/0.0 | +1.3 [+0.0, +3.2] | +0.0 [+0.0, +0.0] | +1.3 [+0.0, +3.2] |
| settled | contested | 366 | 366 | 99.2/97.5 | 0.5/2.5 | 15.8/14.2 | 0.3/0.0 | 0.0/0.0 | +1.9 [+0.3, +3.8] | -0.3 [-0.8, +0.0] | +1.6 [+0.3, +3.3] |
| settled | uncontested | 108 | 108 | 100.0/99.1 | 0.0/0.9 | 11.1/7.4 | 0.0/0.0 | 0.0/0.0 | +0.9 [+0.0, +2.8] | +0.0 [+0.0, +0.0] | +0.9 [+0.0, +2.8] |
| settled | left-coded | 78 | 78 | 98.7/93.6 | 0.0/6.4 | 25.6/23.1 | 1.3/0.0 | 0.0/0.0 | +6.4 [+1.3, +12.8] | -1.3 [-3.8, +0.0] | +5.1 [+1.3, +10.3] |
| settled | right-coded | 177 | 177 | 99.4/98.9 | 0.6/1.1 | 11.9/9.0 | 0.0/0.0 | 0.0/0.0 | +0.6 [+0.0, +1.7] | +0.0 [+0.0, +0.0] | +0.6 [+0.0, +1.7] |
| settled | uncoded | 219 | 219 | 99.5/98.6 | 0.5/1.4 | 13.2/11.9 | 0.0/0.0 | 0.0/0.0 | +0.9 [-0.9, +2.7] | +0.0 [+0.0, +0.0] | +0.9 [-0.9, +2.7] |
| settled | contested x conservative | 122 | 122 | 99.2/95.9 | 0.8/4.1 | 18.0/20.5 | 0.0/0.0 | 0.0/0.0 | +3.3 [+0.8, +6.6] | +0.0 [+0.0, +0.0] | +3.3 [+0.8, +6.6] |
| settled | contested x liberal | 122 | 122 | 98.4/98.4 | 0.8/1.6 | 19.7/13.1 | 0.8/0.0 | 0.0/0.0 | +0.8 [-1.6, +3.3] | -0.8 [-2.5, +0.0] | +0.0 [-3.3, +3.3] |

#### answer length, mean words, original / treated

- consensus | all: 45 / 67
- contested | all: 238 / 277
- settled | all: 133 / 137
- settled | contested: 146 / 149
- settled | uncontested: 89 / 98
- settled | left-coded: 177 / 184
- settled | right-coded: 136 / 135
- settled | uncoded: 115 / 123
- settled | contested x conservative: 168 / 161
- settled | contested x liberal: 142 / 145

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 23.3/90.0 | 0.0/1.7 | 76.7/8.3 | 0.0/0.0 | +1.13/+0.12 |
| liberal | 60 | 13.3/93.3 | 85.0/6.7 | 1.7/0.0 | 0.0/0.0 | -0.92/-0.07 |
| none | 60 | 63.3/100.0 | 35.0/0.0 | 1.7/0.0 | 0.0/0.0 | -0.40/+0.00 |
