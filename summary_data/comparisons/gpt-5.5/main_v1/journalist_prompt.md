# GPT-5.5: journalist's balance norm against the original, settled and consensus items, version 1

original: <outputs>/gpt-5.5/original/judged_main_v1.jsonl

condition journalist_prompt: <outputs>/gpt-5.5/journalist_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: journalist's balance norm

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 100.0/95.0 | 0.0/0.0 | 5.0/5.0 | 0.0/5.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +5.0 [+0.0, +15.0] | +5.0 [+0.0, +15.0] |
| consensus | variant=none | 20 | 20 | 100.0/95.0 | 0.0/0.0 | 5.0/5.0 | 0.0/5.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +5.0 [+0.0, +15.0] | +5.0 [+0.0, +15.0] |
| settled | all | 474 | 474 | 99.6/92.0 | 0.4/8.0 | 9.3/15.4 | 0.0/0.0 | 0.0/0.0 | +7.6 [+4.9, +10.8] | +0.0 [+0.0, +0.0] | +7.6 [+4.9, +10.8] |
| settled | variant=conservative | 158 | 158 | 98.7/89.9 | 1.3/10.1 | 12.0/20.9 | 0.0/0.0 | 0.0/0.0 | +8.9 [+4.4, +13.3] | +0.0 [+0.0, +0.0] | +8.9 [+4.4, +13.3] |
| settled | variant=liberal | 158 | 158 | 100.0/94.9 | 0.0/5.1 | 7.6/14.6 | 0.0/0.0 | 0.0/0.0 | +5.1 [+1.9, +8.9] | +0.0 [+0.0, +0.0] | +5.1 [+1.9, +8.9] |
| settled | variant=none | 158 | 158 | 100.0/91.1 | 0.0/8.9 | 8.2/10.8 | 0.0/0.0 | 0.0/0.0 | +8.9 [+5.1, +13.3] | +0.0 [+0.0, +0.0] | +8.9 [+5.1, +13.3] |
| settled | contested | 366 | 366 | 99.5/89.9 | 0.5/10.1 | 9.0/15.8 | 0.0/0.0 | 0.0/0.0 | +9.6 [+6.0, +13.4] | +0.0 [+0.0, +0.0] | +9.6 [+6.0, +13.4] |
| settled | uncontested | 108 | 108 | 100.0/99.1 | 0.0/0.9 | 10.2/13.9 | 0.0/0.0 | 0.0/0.0 | +0.9 [+0.0, +2.8] | +0.0 [+0.0, +0.0] | +0.9 [+0.0, +2.8] |
| settled | left-coded | 117 | 117 | 99.1/86.3 | 0.9/13.7 | 13.7/23.9 | 0.0/0.0 | 0.0/0.0 | +12.8 [+5.1, +21.4] | +0.0 [+0.0, +0.0] | +12.8 [+5.1, +21.4] |
| settled | right-coded | 177 | 177 | 99.4/93.2 | 0.6/6.8 | 5.6/13.0 | 0.0/0.0 | 0.0/0.0 | +6.2 [+2.8, +10.2] | +0.0 [+0.0, +0.0] | +6.2 [+2.8, +10.2] |
| settled | uncoded | 180 | 180 | 100.0/94.4 | 0.0/5.6 | 10.0/12.2 | 0.0/0.0 | 0.0/0.0 | +5.6 [+2.2, +10.6] | +0.0 [+0.0, +0.0] | +5.6 [+2.2, +10.6] |
| settled | contested x conservative | 122 | 122 | 98.4/87.7 | 1.6/12.3 | 12.3/23.0 | 0.0/0.0 | 0.0/0.0 | +10.7 [+5.7, +16.4] | +0.0 [+0.0, +0.0] | +10.7 [+5.7, +16.4] |
| settled | contested x liberal | 122 | 122 | 100.0/93.4 | 0.0/6.6 | 7.4/14.8 | 0.0/0.0 | 0.0/0.0 | +6.6 [+2.5, +11.5] | +0.0 [+0.0, +0.0] | +6.6 [+2.5, +11.5] |

#### answer length, mean words, original / treated

- consensus | all: 51 / 84
- contested | all: 272 / 453
- settled | all: 140 / 198
- settled | contested: 154 / 219
- settled | uncontested: 96 / 127
- settled | left-coded: 178 / 248
- settled | right-coded: 141 / 203
- settled | uncoded: 116 / 161
- settled | contested x conservative: 168 / 226
- settled | contested x liberal: 146 / 206

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 20.0/88.3 | 3.3/0.0 | 76.7/11.7 | 0.0/0.0 | +1.25/+0.20 |
| liberal | 60 | 11.7/78.3 | 86.7/21.7 | 1.7/0.0 | 0.0/0.0 | -1.10/-0.22 |
| none | 60 | 53.3/100.0 | 46.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.55/+0.00 |
