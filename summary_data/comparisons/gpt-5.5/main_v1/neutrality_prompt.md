# GPT-5.5: neutrality prompt against the original, settled and consensus items, version 1

original: <outputs>/gpt-5.5/original/judged_main_v1.jsonl

condition neutrality_prompt: <outputs>/gpt-5.5/neutrality_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 100.0/100.0 | 0.0/0.0 | 5.0/5.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| consensus | variant=none | 20 | 20 | 100.0/100.0 | 0.0/0.0 | 5.0/5.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 474 | 474 | 99.6/93.9 | 0.4/6.1 | 9.3/17.5 | 0.0/0.0 | 0.0/0.0 | +5.7 [+3.4, +8.4] | +0.0 [+0.0, +0.0] | +5.7 [+3.4, +8.4] |
| settled | variant=conservative | 158 | 158 | 98.7/91.8 | 1.3/8.2 | 12.0/19.0 | 0.0/0.0 | 0.0/0.0 | +7.0 [+3.2, +11.4] | +0.0 [+0.0, +0.0] | +7.0 [+3.2, +11.4] |
| settled | variant=liberal | 158 | 158 | 100.0/93.7 | 0.0/6.3 | 7.6/17.1 | 0.0/0.0 | 0.0/0.0 | +6.3 [+2.5, +10.1] | +0.0 [+0.0, +0.0] | +6.3 [+2.5, +10.1] |
| settled | variant=none | 158 | 158 | 100.0/96.2 | 0.0/3.8 | 8.2/16.5 | 0.0/0.0 | 0.0/0.0 | +3.8 [+1.3, +7.0] | +0.0 [+0.0, +0.0] | +3.8 [+1.3, +7.0] |
| settled | contested | 366 | 366 | 99.5/92.3 | 0.5/7.7 | 9.0/19.7 | 0.0/0.0 | 0.0/0.0 | +7.1 [+4.1, +10.4] | +0.0 [+0.0, +0.0] | +7.1 [+4.1, +10.4] |
| settled | uncontested | 108 | 108 | 100.0/99.1 | 0.0/0.9 | 10.2/10.2 | 0.0/0.0 | 0.0/0.0 | +0.9 [+0.0, +2.8] | +0.0 [+0.0, +0.0] | +0.9 [+0.0, +2.8] |
| settled | left-coded | 117 | 117 | 99.1/88.9 | 0.9/11.1 | 13.7/24.8 | 0.0/0.0 | 0.0/0.0 | +10.3 [+4.3, +17.9] | +0.0 [+0.0, +0.0] | +10.3 [+4.3, +17.9] |
| settled | right-coded | 177 | 177 | 99.4/93.8 | 0.6/6.2 | 5.6/16.9 | 0.0/0.0 | 0.0/0.0 | +5.6 [+2.3, +9.6] | +0.0 [+0.0, +0.0] | +5.6 [+2.3, +9.6] |
| settled | uncoded | 180 | 180 | 100.0/97.2 | 0.0/2.8 | 10.0/13.3 | 0.0/0.0 | 0.0/0.0 | +2.8 [+0.6, +6.1] | +0.0 [+0.0, +0.0] | +2.8 [+0.6, +6.1] |
| settled | contested x conservative | 122 | 122 | 98.4/90.2 | 1.6/9.8 | 12.3/22.1 | 0.0/0.0 | 0.0/0.0 | +8.2 [+4.1, +13.1] | +0.0 [+0.0, +0.0] | +8.2 [+4.1, +13.1] |
| settled | contested x liberal | 122 | 122 | 100.0/91.8 | 0.0/8.2 | 7.4/19.7 | 0.0/0.0 | 0.0/0.0 | +8.2 [+4.1, +13.1] | +0.0 [+0.0, +0.0] | +8.2 [+4.1, +13.1] |

#### answer length, mean words, original / treated

- consensus | all: 51 / 87
- contested | all: 272 / 366
- settled | all: 140 / 170
- settled | contested: 154 / 186
- settled | uncontested: 96 / 115
- settled | left-coded: 178 / 212
- settled | right-coded: 141 / 173
- settled | uncoded: 116 / 140
- settled | contested x conservative: 168 / 190
- settled | contested x liberal: 146 / 180

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 20.0/86.7 | 3.3/0.0 | 76.7/13.3 | 0.0/0.0 | +1.25/+0.25 |
| liberal | 60 | 11.7/88.3 | 86.7/11.7 | 1.7/0.0 | 0.0/0.0 | -1.10/-0.13 |
| none | 60 | 53.3/100.0 | 46.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.55/+0.00 |
