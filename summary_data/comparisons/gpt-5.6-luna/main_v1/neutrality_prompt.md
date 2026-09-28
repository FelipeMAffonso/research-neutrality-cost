# GPT-5.6-luna: neutrality prompt against the original, settled and consensus items, version 1

original: <outputs>/gpt-5.6-luna/original/judged_main_v1.jsonl

condition neutrality_prompt: <outputs>/gpt-5.6-luna/neutrality_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +10.0 [+0.0, +25.0] | +0.0 [+0.0, +0.0] | +10.0 [+0.0, +25.0] |
| consensus | variant=none | 20 | 20 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +10.0 [+0.0, +25.0] | +0.0 [+0.0, +0.0] | +10.0 [+0.0, +25.0] |
| settled | all | 474 | 474 | 99.2/97.3 | 0.8/2.7 | 15.0/14.6 | 0.0/0.0 | 0.0/0.0 | +1.9 [+0.2, +3.6] | +0.0 [+0.0, +0.0] | +1.9 [+0.2, +3.6] |
| settled | variant=conservative | 158 | 158 | 99.4/96.8 | 0.6/3.2 | 18.4/21.5 | 0.0/0.0 | 0.0/0.0 | +2.5 [+0.6, +5.1] | +0.0 [+0.0, +0.0] | +2.5 [+0.6, +5.1] |
| settled | variant=liberal | 158 | 158 | 98.7/97.5 | 1.3/2.5 | 17.7/11.4 | 0.0/0.0 | 0.0/0.0 | +1.3 [-1.9, +4.4] | +0.0 [+0.0, +0.0] | +1.3 [-1.9, +4.4] |
| settled | variant=none | 158 | 158 | 99.4/97.5 | 0.6/2.5 | 8.9/10.8 | 0.0/0.0 | 0.0/0.0 | +1.9 [+0.0, +4.4] | +0.0 [+0.0, +0.0] | +1.9 [+0.0, +4.4] |
| settled | contested | 366 | 366 | 98.9/96.7 | 1.1/3.3 | 15.3/16.4 | 0.0/0.0 | 0.0/0.0 | +2.2 [+0.3, +4.4] | +0.0 [+0.0, +0.0] | +2.2 [+0.3, +4.4] |
| settled | uncontested | 108 | 108 | 100.0/99.1 | 0.0/0.9 | 13.9/8.3 | 0.0/0.0 | 0.0/0.0 | +0.9 [+0.0, +2.8] | +0.0 [+0.0, +0.0] | +0.9 [+0.0, +2.8] |
| settled | left-coded | 117 | 117 | 97.4/95.7 | 2.6/4.3 | 23.1/23.1 | 0.0/0.0 | 0.0/0.0 | +1.7 [-2.6, +6.8] | +0.0 [+0.0, +0.0] | +1.7 [-2.6, +6.8] |
| settled | right-coded | 177 | 177 | 99.4/97.2 | 0.6/2.8 | 12.4/11.3 | 0.0/0.0 | 0.0/0.0 | +2.3 [+0.0, +5.1] | +0.0 [+0.0, +0.0] | +2.3 [+0.0, +5.1] |
| settled | uncoded | 180 | 180 | 100.0/98.3 | 0.0/1.7 | 12.2/12.2 | 0.0/0.0 | 0.0/0.0 | +1.7 [+0.0, +3.9] | +0.0 [+0.0, +0.0] | +1.7 [+0.0, +3.9] |
| settled | contested x conservative | 122 | 122 | 99.2/95.9 | 0.8/4.1 | 19.7/24.6 | 0.0/0.0 | 0.0/0.0 | +3.3 [+0.8, +6.6] | +0.0 [+0.0, +0.0] | +3.3 [+0.8, +6.6] |
| settled | contested x liberal | 122 | 122 | 98.4/97.5 | 1.6/2.5 | 17.2/12.3 | 0.0/0.0 | 0.0/0.0 | +0.8 [-2.5, +4.1] | +0.0 [+0.0, +0.0] | +0.8 [-2.5, +4.1] |

#### answer length, mean words, original / treated

- consensus | all: 45 / 71
- contested | all: 238 / 277
- settled | all: 133 / 137
- settled | contested: 146 / 149
- settled | uncontested: 89 / 97
- settled | left-coded: 169 / 176
- settled | right-coded: 136 / 135
- settled | uncoded: 107 / 114
- settled | contested x conservative: 168 / 160
- settled | contested x liberal: 141 / 146

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 23.3/90.0 | 0.0/1.7 | 76.7/8.3 | 0.0/0.0 | +1.13/+0.12 |
| liberal | 60 | 13.3/93.3 | 85.0/6.7 | 1.7/0.0 | 0.0/0.0 | -0.92/-0.07 |
| none | 60 | 63.3/100.0 | 35.0/0.0 | 1.7/0.0 | 0.0/0.0 | -0.40/+0.00 |
