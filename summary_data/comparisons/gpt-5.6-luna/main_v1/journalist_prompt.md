# GPT-5.6-luna: journalist's balance norm against the original, settled and consensus items, version 1

original: <outputs>/gpt-5.6-luna/original/judged_main_v1.jsonl

condition journalist_prompt: <outputs>/gpt-5.6-luna/journalist_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: journalist's balance norm

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| consensus | variant=none | 20 | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 474 | 474 | 99.2/96.0 | 0.8/4.0 | 15.0/12.0 | 0.0/0.0 | 0.0/0.0 | +3.2 [+1.3, +5.5] | +0.0 [+0.0, +0.0] | +3.2 [+1.3, +5.5] |
| settled | variant=conservative | 158 | 158 | 99.4/96.2 | 0.6/3.8 | 18.4/17.1 | 0.0/0.0 | 0.0/0.0 | +3.2 [+0.6, +6.3] | +0.0 [+0.0, +0.0] | +3.2 [+0.6, +6.3] |
| settled | variant=liberal | 158 | 158 | 98.7/95.6 | 1.3/4.4 | 17.7/11.4 | 0.0/0.0 | 0.0/0.0 | +3.2 [-0.6, +7.0] | +0.0 [+0.0, +0.0] | +3.2 [-0.6, +7.0] |
| settled | variant=none | 158 | 158 | 99.4/96.2 | 0.6/3.8 | 8.9/7.6 | 0.0/0.0 | 0.0/0.0 | +3.2 [+0.6, +6.3] | +0.0 [+0.0, +0.0] | +3.2 [+0.6, +6.3] |
| settled | contested | 366 | 366 | 98.9/95.1 | 1.1/4.9 | 15.3/11.7 | 0.0/0.0 | 0.0/0.0 | +3.8 [+1.4, +6.6] | +0.0 [+0.0, +0.0] | +3.8 [+1.4, +6.6] |
| settled | uncontested | 108 | 108 | 100.0/99.1 | 0.0/0.9 | 13.9/13.0 | 0.0/0.0 | 0.0/0.0 | +0.9 [+0.0, +2.8] | +0.0 [+0.0, +0.0] | +0.9 [+0.0, +2.8] |
| settled | left-coded | 117 | 117 | 97.4/92.3 | 2.6/7.7 | 23.1/18.8 | 0.0/0.0 | 0.0/0.0 | +5.1 [+0.9, +10.3] | +0.0 [+0.0, +0.0] | +5.1 [+0.9, +10.3] |
| settled | right-coded | 177 | 177 | 99.4/98.3 | 0.6/1.7 | 12.4/7.3 | 0.0/0.0 | 0.0/0.0 | +1.1 [+0.0, +2.8] | +0.0 [+0.0, +0.0] | +1.1 [+0.0, +2.8] |
| settled | uncoded | 180 | 180 | 100.0/96.1 | 0.0/3.9 | 12.2/12.2 | 0.0/0.0 | 0.0/0.0 | +3.9 [+0.6, +8.3] | +0.0 [+0.0, +0.0] | +3.9 [+0.6, +8.3] |
| settled | contested x conservative | 122 | 122 | 99.2/95.1 | 0.8/4.9 | 19.7/16.4 | 0.0/0.0 | 0.0/0.0 | +4.1 [+0.8, +8.2] | +0.0 [+0.0, +0.0] | +4.1 [+0.8, +8.2] |
| settled | contested x liberal | 122 | 122 | 98.4/94.3 | 1.6/5.7 | 17.2/9.8 | 0.0/0.0 | 0.0/0.0 | +4.1 [+0.0, +9.0] | +0.0 [+0.0, +0.0] | +4.1 [+0.0, +9.0] |

#### answer length, mean words, original / treated

- consensus | all: 45 / 66
- contested | all: 238 / 301
- settled | all: 133 / 146
- settled | contested: 146 / 160
- settled | uncontested: 89 / 101
- settled | left-coded: 169 / 191
- settled | right-coded: 136 / 144
- settled | uncoded: 107 / 119
- settled | contested x conservative: 168 / 172
- settled | contested x liberal: 141 / 154

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 23.3/93.3 | 0.0/0.0 | 76.7/6.7 | 0.0/0.0 | +1.13/+0.13 |
| liberal | 60 | 13.3/86.7 | 85.0/13.3 | 1.7/0.0 | 0.0/0.0 | -0.92/-0.15 |
| none | 60 | 63.3/100.0 | 35.0/0.0 | 1.7/0.0 | 0.0/0.0 | -0.40/+0.00 |
