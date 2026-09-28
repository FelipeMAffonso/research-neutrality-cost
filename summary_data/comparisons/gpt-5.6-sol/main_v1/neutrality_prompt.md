# GPT-5.6-sol: neutrality prompt against the original, settled and consensus items, version 1

original: <outputs>/gpt-5.6-sol/original/judged_main_v1.jsonl

condition neutrality_prompt: <outputs>/gpt-5.6-sol/neutrality_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| consensus | variant=none | 20 | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 474 | 474 | 99.6/97.0 | 0.2/2.7 | 15.8/19.4 | 0.2/0.2 | 0.0/0.0 | +2.5 [+1.1, +4.4] | +0.0 [+0.0, +0.0] | +2.5 [+1.1, +4.4] |
| settled | variant=conservative | 158 | 158 | 100.0/98.1 | 0.0/1.9 | 19.0/23.4 | 0.0/0.0 | 0.0/0.0 | +1.9 [+0.0, +4.4] | +0.0 [+0.0, +0.0] | +1.9 [+0.0, +4.4] |
| settled | variant=liberal | 158 | 158 | 100.0/97.5 | 0.0/1.9 | 21.5/24.1 | 0.0/0.6 | 0.0/0.0 | +1.9 [+0.0, +4.4] | +0.6 [+0.0, +1.9] | +2.5 [+0.6, +5.1] |
| settled | variant=none | 158 | 158 | 98.7/95.6 | 0.6/4.4 | 7.0/10.8 | 0.6/0.0 | 0.0/0.0 | +3.8 [+1.3, +7.0] | -0.6 [-1.9, +0.0] | +3.2 [+0.0, +7.0] |
| settled | contested | 366 | 366 | 99.5/96.4 | 0.3/3.3 | 15.6/19.4 | 0.3/0.3 | 0.0/0.0 | +3.0 [+1.1, +5.7] | +0.0 [+0.0, +0.0] | +3.0 [+1.1, +5.7] |
| settled | uncontested | 108 | 108 | 100.0/99.1 | 0.0/0.9 | 16.7/19.4 | 0.0/0.0 | 0.0/0.0 | +0.9 [+0.0, +2.8] | +0.0 [+0.0, +0.0] | +0.9 [+0.0, +2.8] |
| settled | left-coded | 117 | 117 | 99.1/91.5 | 0.9/8.5 | 24.8/23.1 | 0.0/0.0 | 0.0/0.0 | +7.7 [+2.6, +14.5] | +0.0 [+0.0, +0.0] | +7.7 [+2.6, +14.5] |
| settled | right-coded | 177 | 177 | 99.4/99.4 | 0.0/0.0 | 11.3/17.5 | 0.6/0.6 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | uncoded | 180 | 180 | 100.0/98.3 | 0.0/1.7 | 14.4/18.9 | 0.0/0.0 | 0.0/0.0 | +1.7 [+0.0, +3.9] | +0.0 [+0.0, +0.0] | +1.7 [+0.0, +3.9] |
| settled | contested x conservative | 122 | 122 | 100.0/98.4 | 0.0/1.6 | 18.9/23.0 | 0.0/0.0 | 0.0/0.0 | +1.6 [+0.0, +4.1] | +0.0 [+0.0, +0.0] | +1.6 [+0.0, +4.1] |
| settled | contested x liberal | 122 | 122 | 100.0/96.7 | 0.0/2.5 | 20.5/23.8 | 0.0/0.8 | 0.0/0.0 | +2.5 [+0.0, +5.7] | +0.8 [+0.0, +2.5] | +3.3 [+0.8, +6.6] |

#### answer length, mean words, original / treated

- consensus | all: 49 / 67
- contested | all: 187 / 246
- settled | all: 108 / 125
- settled | contested: 119 / 139
- settled | uncontested: 70 / 80
- settled | left-coded: 133 / 158
- settled | right-coded: 113 / 130
- settled | uncoded: 86 / 99
- settled | contested x conservative: 127 / 144
- settled | contested x liberal: 112 / 130

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 38.3/91.7 | 5.0/0.0 | 56.7/8.3 | 0.0/0.0 | +0.82/+0.10 |
| liberal | 60 | 28.3/98.3 | 70.0/1.7 | 1.7/0.0 | 0.0/0.0 | -0.78/-0.02 |
| none | 60 | 48.3/98.3 | 48.3/1.7 | 3.3/0.0 | 0.0/0.0 | -0.53/-0.02 |
