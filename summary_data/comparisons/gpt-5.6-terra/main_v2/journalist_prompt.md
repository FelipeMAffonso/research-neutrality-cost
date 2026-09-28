# GPT-5.6-terra: journalist's balance norm against the original, settled and consensus items, version 2

original: <outputs>/gpt-5.6-terra/original/judged_main_v2.jsonl

condition journalist_prompt: <outputs>/gpt-5.6-terra/journalist_prompt/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: journalist's balance norm

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/5.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| consensus | variant=none | 20 | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/5.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 474 | 474 | 99.8/94.1 | 0.2/5.9 | 11.8/19.4 | 0.0/0.0 | 0.0/0.0 | +5.7 [+3.2, +8.4] | +0.0 [+0.0, +0.0] | +5.7 [+3.2, +8.4] |
| settled | variant=conservative | 158 | 158 | 100.0/93.0 | 0.0/7.0 | 15.8/24.1 | 0.0/0.0 | 0.0/0.0 | +7.0 [+3.2, +11.4] | +0.0 [+0.0, +0.0] | +7.0 [+3.2, +11.4] |
| settled | variant=liberal | 158 | 158 | 99.4/97.5 | 0.6/2.5 | 13.3/17.7 | 0.0/0.0 | 0.0/0.0 | +1.9 [-0.6, +5.1] | +0.0 [+0.0, +0.0] | +1.9 [-0.6, +5.1] |
| settled | variant=none | 158 | 158 | 100.0/91.8 | 0.0/8.2 | 6.3/16.5 | 0.0/0.0 | 0.0/0.0 | +8.2 [+4.4, +12.7] | +0.0 [+0.0, +0.0] | +8.2 [+4.4, +12.7] |
| settled | contested | 366 | 366 | 99.7/92.3 | 0.3/7.7 | 12.3/22.1 | 0.0/0.0 | 0.0/0.0 | +7.4 [+4.4, +10.7] | +0.0 [+0.0, +0.0] | +7.4 [+4.4, +10.7] |
| settled | uncontested | 108 | 108 | 100.0/100.0 | 0.0/0.0 | 10.2/10.2 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | left-coded | 78 | 78 | 100.0/91.0 | 0.0/9.0 | 16.7/37.2 | 0.0/0.0 | 0.0/0.0 | +9.0 [+2.6, +16.7] | +0.0 [+0.0, +0.0] | +9.0 [+2.6, +16.7] |
| settled | right-coded | 177 | 177 | 100.0/96.0 | 0.0/4.0 | 9.6/15.8 | 0.0/0.0 | 0.0/0.0 | +4.0 [+1.1, +7.3] | +0.0 [+0.0, +0.0] | +4.0 [+1.1, +7.3] |
| settled | uncoded | 219 | 219 | 99.5/93.6 | 0.5/6.4 | 11.9/16.0 | 0.0/0.0 | 0.0/0.0 | +5.9 [+2.3, +10.5] | +0.0 [+0.0, +0.0] | +5.9 [+2.3, +10.5] |
| settled | contested x conservative | 122 | 122 | 100.0/91.0 | 0.0/9.0 | 17.2/28.7 | 0.0/0.0 | 0.0/0.0 | +9.0 [+4.1, +13.9] | +0.0 [+0.0, +0.0] | +9.0 [+4.1, +13.9] |
| settled | contested x liberal | 122 | 122 | 99.2/96.7 | 0.8/3.3 | 13.1/18.9 | 0.0/0.0 | 0.0/0.0 | +2.5 [-0.8, +5.7] | +0.0 [+0.0, +0.0] | +2.5 [-0.8, +5.7] |

#### answer length, mean words, original / treated

- consensus | all: 70 / 97
- contested | all: 300 / 403
- settled | all: 167 / 203
- settled | contested: 183 / 224
- settled | uncontested: 112 / 132
- settled | left-coded: 219 / 266
- settled | right-coded: 172 / 205
- settled | uncoded: 145 / 179
- settled | contested x conservative: 206 / 244
- settled | contested x liberal: 181 / 213

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 33.3/93.3 | 1.7/0.0 | 65.0/6.7 | 0.0/0.0 | +1.07/+0.10 |
| liberal | 60 | 38.3/95.0 | 60.0/5.0 | 1.7/0.0 | 0.0/0.0 | -0.65/-0.05 |
| none | 60 | 55.0/100.0 | 45.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.55/+0.00 |
