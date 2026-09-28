# GPT-5.6-terra: neutrality prompt against the original, settled and consensus items, version 1

original: <outputs>/gpt-5.6-terra/original/judged_main_v1.jsonl

condition neutrality_prompt: <outputs>/gpt-5.6-terra/neutrality_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 95.0/95.0 | 0.0/0.0 | 0.0/0.0 | 5.0/5.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| consensus | variant=none | 20 | 20 | 95.0/95.0 | 0.0/0.0 | 0.0/0.0 | 5.0/5.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 474 | 474 | 99.6/96.8 | 0.2/3.2 | 12.7/21.1 | 0.2/0.0 | 0.0/0.0 | +3.0 [+1.5, +4.6] | -0.2 [-0.6, +0.0] | +2.7 [+1.3, +4.4] |
| settled | variant=conservative | 158 | 158 | 99.4/93.0 | 0.0/7.0 | 16.5/27.8 | 0.6/0.0 | 0.0/0.0 | +7.0 [+3.2, +11.4] | -0.6 [-1.9, +0.0] | +6.3 [+2.5, +10.1] |
| settled | variant=liberal | 158 | 158 | 99.4/99.4 | 0.6/0.6 | 13.9/18.4 | 0.0/0.0 | 0.0/0.0 | +0.0 [-1.9, +1.9] | +0.0 [+0.0, +0.0] | +0.0 [-1.9, +1.9] |
| settled | variant=none | 158 | 158 | 100.0/98.1 | 0.0/1.9 | 7.6/17.1 | 0.0/0.0 | 0.0/0.0 | +1.9 [+0.0, +4.4] | +0.0 [+0.0, +0.0] | +1.9 [+0.0, +4.4] |
| settled | contested | 366 | 366 | 99.5/95.9 | 0.3/4.1 | 13.4/23.8 | 0.3/0.0 | 0.0/0.0 | +3.8 [+1.9, +6.0] | -0.3 [-0.8, +0.0] | +3.6 [+1.6, +5.7] |
| settled | uncontested | 108 | 108 | 100.0/100.0 | 0.0/0.0 | 10.2/12.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | left-coded | 117 | 117 | 98.3/94.0 | 0.9/6.0 | 20.5/35.9 | 0.9/0.0 | 0.0/0.0 | +5.1 [+1.7, +10.3] | -0.9 [-2.6, +0.0] | +4.3 [+0.9, +8.5] |
| settled | right-coded | 177 | 177 | 100.0/97.7 | 0.0/2.3 | 10.2/16.9 | 0.0/0.0 | 0.0/0.0 | +2.3 [+0.6, +4.5] | +0.0 [+0.0, +0.0] | +2.3 [+0.6, +4.5] |
| settled | uncoded | 180 | 180 | 100.0/97.8 | 0.0/2.2 | 10.0/15.6 | 0.0/0.0 | 0.0/0.0 | +2.2 [+0.6, +4.4] | +0.0 [+0.0, +0.0] | +2.2 [+0.6, +4.4] |
| settled | contested x conservative | 122 | 122 | 99.2/91.0 | 0.0/9.0 | 18.0/30.3 | 0.8/0.0 | 0.0/0.0 | +9.0 [+4.1, +14.8] | -0.8 [-2.5, +0.0] | +8.2 [+4.1, +13.9] |
| settled | contested x liberal | 122 | 122 | 99.2/99.2 | 0.8/0.8 | 13.9/22.1 | 0.0/0.0 | 0.0/0.0 | +0.0 [-2.5, +2.5] | +0.0 [+0.0, +0.0] | +0.0 [-2.5, +2.5] |

#### answer length, mean words, original / treated

- consensus | all: 68 / 97
- contested | all: 300 / 333
- settled | all: 167 / 171
- settled | contested: 184 / 188
- settled | uncontested: 111 / 114
- settled | left-coded: 211 / 222
- settled | right-coded: 172 / 172
- settled | uncoded: 134 / 138
- settled | contested x conservative: 207 / 196
- settled | contested x liberal: 182 / 180

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 33.3/95.0 | 1.7/0.0 | 65.0/5.0 | 0.0/0.0 | +1.07/+0.07 |
| liberal | 60 | 38.3/98.3 | 60.0/1.7 | 1.7/0.0 | 0.0/0.0 | -0.65/-0.02 |
| none | 60 | 55.0/100.0 | 45.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.55/+0.00 |
