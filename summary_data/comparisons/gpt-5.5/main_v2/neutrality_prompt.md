# GPT-5.5: neutrality prompt against the original, settled and consensus items, version 2

original: <outputs>/gpt-5.5/original/judged_main_v2.jsonl

condition neutrality_prompt: <outputs>/gpt-5.5/neutrality_prompt/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| consensus | variant=none | 20 | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 474 | 474 | 99.6/94.5 | 0.2/5.5 | 9.5/17.1 | 0.2/0.0 | 0.0/0.0 | +5.3 [+3.2, +7.8] | -0.2 [-0.6, +0.0] | +5.1 [+3.0, +7.6] |
| settled | variant=conservative | 158 | 158 | 98.7/94.3 | 0.6/5.7 | 13.9/19.0 | 0.6/0.0 | 0.0/0.0 | +5.1 [+1.9, +8.9] | -0.6 [-1.9, +0.0] | +4.4 [+1.3, +8.2] |
| settled | variant=liberal | 158 | 158 | 100.0/93.7 | 0.0/6.3 | 8.9/19.6 | 0.0/0.0 | 0.0/0.0 | +6.3 [+3.2, +10.1] | +0.0 [+0.0, +0.0] | +6.3 [+3.2, +10.1] |
| settled | variant=none | 158 | 158 | 100.0/95.6 | 0.0/4.4 | 5.7/12.7 | 0.0/0.0 | 0.0/0.0 | +4.4 [+1.9, +8.2] | +0.0 [+0.0, +0.0] | +4.4 [+1.9, +8.2] |
| settled | contested | 366 | 366 | 99.5/93.2 | 0.3/6.8 | 8.7/18.9 | 0.3/0.0 | 0.0/0.0 | +6.6 [+3.8, +9.6] | -0.3 [-0.8, +0.0] | +6.3 [+3.6, +9.3] |
| settled | uncontested | 108 | 108 | 100.0/99.1 | 0.0/0.9 | 12.0/11.1 | 0.0/0.0 | 0.0/0.0 | +0.9 [+0.0, +2.8] | +0.0 [+0.0, +0.0] | +0.9 [+0.0, +2.8] |
| settled | left-coded | 78 | 78 | 98.7/91.0 | 0.0/9.0 | 14.1/25.6 | 1.3/0.0 | 0.0/0.0 | +9.0 [+2.6, +15.4] | -1.3 [-3.8, +0.0] | +7.7 [+1.3, +15.4] |
| settled | right-coded | 177 | 177 | 99.4/94.9 | 0.6/5.1 | 5.6/17.5 | 0.0/0.0 | 0.0/0.0 | +4.5 [+1.7, +7.9] | +0.0 [+0.0, +0.0] | +4.5 [+1.7, +7.9] |
| settled | uncoded | 219 | 219 | 100.0/95.4 | 0.0/4.6 | 11.0/13.7 | 0.0/0.0 | 0.0/0.0 | +4.6 [+1.8, +8.2] | +0.0 [+0.0, +0.0] | +4.6 [+1.8, +8.2] |
| settled | contested x conservative | 122 | 122 | 98.4/93.4 | 0.8/6.6 | 13.9/22.1 | 0.8/0.0 | 0.0/0.0 | +5.7 [+1.6, +9.8] | -0.8 [-2.5, +0.0] | +4.9 [+0.8, +9.8] |
| settled | contested x liberal | 122 | 122 | 100.0/91.8 | 0.0/8.2 | 8.2/21.3 | 0.0/0.0 | 0.0/0.0 | +8.2 [+4.1, +13.1] | +0.0 [+0.0, +0.0] | +8.2 [+4.1, +13.1] |

#### answer length, mean words, original / treated

- consensus | all: 48 / 84
- contested | all: 272 / 366
- settled | all: 140 / 170
- settled | contested: 153 / 187
- settled | uncontested: 96 / 116
- settled | left-coded: 181 / 215
- settled | right-coded: 142 / 174
- settled | uncoded: 125 / 152
- settled | contested x conservative: 167 / 192
- settled | contested x liberal: 146 / 179

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 20.0/86.7 | 3.3/0.0 | 76.7/13.3 | 0.0/0.0 | +1.25/+0.25 |
| liberal | 60 | 11.7/88.3 | 86.7/11.7 | 1.7/0.0 | 0.0/0.0 | -1.10/-0.13 |
| none | 60 | 53.3/100.0 | 46.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.55/+0.00 |
