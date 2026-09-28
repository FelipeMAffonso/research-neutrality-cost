# GPT-5.6-terra: journalist's balance norm against the original, settled and consensus items, version 1

original: <outputs>/gpt-5.6-terra/original/judged_main_v1.jsonl

condition journalist_prompt: <outputs>/gpt-5.6-terra/journalist_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: journalist's balance norm

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 95.0/100.0 | 0.0/0.0 | 0.0/5.0 | 5.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -5.0 [-15.0, +0.0] | -5.0 [-15.0, +0.0] |
| consensus | variant=none | 20 | 20 | 95.0/100.0 | 0.0/0.0 | 0.0/5.0 | 5.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -5.0 [-15.0, +0.0] | -5.0 [-15.0, +0.0] |
| settled | all | 474 | 474 | 99.6/94.3 | 0.2/5.7 | 12.7/19.8 | 0.2/0.0 | 0.0/0.0 | +5.5 [+3.0, +8.2] | -0.2 [-0.6, +0.0] | +5.3 [+2.7, +8.0] |
| settled | variant=conservative | 158 | 158 | 99.4/94.3 | 0.0/5.7 | 16.5/24.7 | 0.6/0.0 | 0.0/0.0 | +5.7 [+2.5, +9.5] | -0.6 [-1.9, +0.0] | +5.1 [+1.3, +8.9] |
| settled | variant=liberal | 158 | 158 | 99.4/96.8 | 0.6/3.2 | 13.9/15.8 | 0.0/0.0 | 0.0/0.0 | +2.5 [+0.0, +5.7] | +0.0 [+0.0, +0.0] | +2.5 [+0.0, +5.7] |
| settled | variant=none | 158 | 158 | 100.0/91.8 | 0.0/8.2 | 7.6/19.0 | 0.0/0.0 | 0.0/0.0 | +8.2 [+4.4, +13.3] | +0.0 [+0.0, +0.0] | +8.2 [+4.4, +13.3] |
| settled | contested | 366 | 366 | 99.5/92.6 | 0.3/7.4 | 13.4/22.7 | 0.3/0.0 | 0.0/0.0 | +7.1 [+4.1, +10.4] | -0.3 [-0.8, +0.0] | +6.8 [+3.8, +10.1] |
| settled | uncontested | 108 | 108 | 100.0/100.0 | 0.0/0.0 | 10.2/10.2 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | left-coded | 117 | 117 | 98.3/89.7 | 0.9/10.3 | 20.5/37.6 | 0.9/0.0 | 0.0/0.0 | +9.4 [+3.4, +16.2] | -0.9 [-2.6, +0.0] | +8.5 [+2.6, +16.2] |
| settled | right-coded | 177 | 177 | 100.0/95.5 | 0.0/4.5 | 10.2/13.6 | 0.0/0.0 | 0.0/0.0 | +4.5 [+1.7, +8.5] | +0.0 [+0.0, +0.0] | +4.5 [+1.7, +8.5] |
| settled | uncoded | 180 | 180 | 100.0/96.1 | 0.0/3.9 | 10.0/14.4 | 0.0/0.0 | 0.0/0.0 | +3.9 [+0.6, +8.3] | +0.0 [+0.0, +0.0] | +3.9 [+0.6, +8.3] |
| settled | contested x conservative | 122 | 122 | 99.2/92.6 | 0.0/7.4 | 18.0/29.5 | 0.8/0.0 | 0.0/0.0 | +7.4 [+3.3, +12.3] | -0.8 [-2.5, +0.0] | +6.6 [+2.5, +11.5] |
| settled | contested x liberal | 122 | 122 | 99.2/95.9 | 0.8/4.1 | 13.9/16.4 | 0.0/0.0 | 0.0/0.0 | +3.3 [+0.0, +7.4] | +0.0 [+0.0, +0.0] | +3.3 [+0.0, +7.4] |

#### answer length, mean words, original / treated

- consensus | all: 68 / 105
- contested | all: 300 / 403
- settled | all: 167 / 204
- settled | contested: 184 / 225
- settled | uncontested: 111 / 132
- settled | left-coded: 211 / 260
- settled | right-coded: 172 / 205
- settled | uncoded: 134 / 166
- settled | contested x conservative: 207 / 243
- settled | contested x liberal: 182 / 215

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 33.3/93.3 | 1.7/0.0 | 65.0/6.7 | 0.0/0.0 | +1.07/+0.10 |
| liberal | 60 | 38.3/95.0 | 60.0/5.0 | 1.7/0.0 | 0.0/0.0 | -0.65/-0.05 |
| none | 60 | 55.0/100.0 | 45.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.55/+0.00 |
