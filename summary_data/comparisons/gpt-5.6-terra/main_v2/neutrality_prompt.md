# GPT-5.6-terra: neutrality prompt against the original, settled and consensus items, version 2

original: <outputs>/gpt-5.6-terra/original/judged_main_v2.jsonl

condition neutrality_prompt: <outputs>/gpt-5.6-terra/neutrality_prompt/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| consensus | variant=none | 20 | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 474 | 474 | 99.8/97.5 | 0.2/2.5 | 11.8/20.3 | 0.0/0.0 | 0.0/0.0 | +2.3 [+1.1, +3.8] | +0.0 [+0.0, +0.0] | +2.3 [+1.1, +3.8] |
| settled | variant=conservative | 158 | 158 | 100.0/94.3 | 0.0/5.7 | 15.8/24.7 | 0.0/0.0 | 0.0/0.0 | +5.7 [+2.5, +9.5] | +0.0 [+0.0, +0.0] | +5.7 [+2.5, +9.5] |
| settled | variant=liberal | 158 | 158 | 99.4/99.4 | 0.6/0.6 | 13.3/19.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [-1.9, +1.9] | +0.0 [+0.0, +0.0] | +0.0 [-1.9, +1.9] |
| settled | variant=none | 158 | 158 | 100.0/98.7 | 0.0/1.3 | 6.3/17.1 | 0.0/0.0 | 0.0/0.0 | +1.3 [+0.0, +3.2] | +0.0 [+0.0, +0.0] | +1.3 [+0.0, +3.2] |
| settled | contested | 366 | 366 | 99.7/96.7 | 0.3/3.3 | 12.3/22.4 | 0.0/0.0 | 0.0/0.0 | +3.0 [+1.4, +4.6] | +0.0 [+0.0, +0.0] | +3.0 [+1.4, +4.6] |
| settled | uncontested | 108 | 108 | 100.0/100.0 | 0.0/0.0 | 10.2/13.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | left-coded | 78 | 78 | 100.0/98.7 | 0.0/1.3 | 16.7/32.1 | 0.0/0.0 | 0.0/0.0 | +1.3 [+0.0, +3.8] | +0.0 [+0.0, +0.0] | +1.3 [+0.0, +3.8] |
| settled | right-coded | 177 | 177 | 100.0/97.2 | 0.0/2.8 | 9.6/17.5 | 0.0/0.0 | 0.0/0.0 | +2.8 [+0.6, +5.6] | +0.0 [+0.0, +0.0] | +2.8 [+0.6, +5.6] |
| settled | uncoded | 219 | 219 | 99.5/97.3 | 0.5/2.7 | 11.9/18.3 | 0.0/0.0 | 0.0/0.0 | +2.3 [+0.5, +4.6] | +0.0 [+0.0, +0.0] | +2.3 [+0.5, +4.6] |
| settled | contested x conservative | 122 | 122 | 100.0/92.6 | 0.0/7.4 | 17.2/26.2 | 0.0/0.0 | 0.0/0.0 | +7.4 [+3.3, +12.3] | +0.0 [+0.0, +0.0] | +7.4 [+3.3, +12.3] |
| settled | contested x liberal | 122 | 122 | 99.2/99.2 | 0.8/0.8 | 13.1/21.3 | 0.0/0.0 | 0.0/0.0 | +0.0 [-2.5, +2.5] | +0.0 [+0.0, +0.0] | +0.0 [-2.5, +2.5] |

#### answer length, mean words, original / treated

- consensus | all: 70 / 93
- contested | all: 300 / 333
- settled | all: 167 / 170
- settled | contested: 183 / 186
- settled | uncontested: 112 / 114
- settled | left-coded: 219 / 227
- settled | right-coded: 172 / 170
- settled | uncoded: 145 / 149
- settled | contested x conservative: 206 / 196
- settled | contested x liberal: 181 / 178

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 33.3/95.0 | 1.7/0.0 | 65.0/5.0 | 0.0/0.0 | +1.07/+0.07 |
| liberal | 60 | 38.3/98.3 | 60.0/1.7 | 1.7/0.0 | 0.0/0.0 | -0.65/-0.02 |
| none | 60 | 55.0/100.0 | 45.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.55/+0.00 |
