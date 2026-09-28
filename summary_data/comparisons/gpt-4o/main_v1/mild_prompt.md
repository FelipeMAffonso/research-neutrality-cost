# GPT-4o: mild even-handedness instruction against the original, settled and consensus items, version 1

original: <outputs>/gpt-4o/original/judged_main_v1.jsonl

condition mild_prompt: <outputs>/gpt-4o/mild_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mild even-handedness instruction

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 85.0/80.0 | 5.0/0.0 | 5.0/5.0 | 10.0/20.0 | 0.0/0.0 | -5.0 [-15.0, +0.0] | +10.0 [+0.0, +25.0] | +5.0 [+0.0, +15.0] |
| consensus | variant=none | 20 | 20 | 85.0/80.0 | 5.0/0.0 | 5.0/5.0 | 10.0/20.0 | 0.0/0.0 | -5.0 [-15.0, +0.0] | +10.0 [+0.0, +25.0] | +5.0 [+0.0, +15.0] |
| settled | all | 474 | 474 | 92.0/87.6 | 7.8/12.2 | 18.4/20.5 | 0.2/0.2 | 0.0/0.0 | +4.4 [+1.5, +7.6] | +0.0 [+0.0, +0.0] | +4.4 [+1.5, +7.6] |
| settled | variant=conservative | 158 | 158 | 91.1/86.1 | 8.2/13.3 | 21.5/23.4 | 0.6/0.6 | 0.0/0.0 | +5.1 [+0.6, +10.1] | +0.0 [+0.0, +0.0] | +5.1 [+0.6, +10.1] |
| settled | variant=liberal | 158 | 158 | 93.0/87.3 | 7.0/12.7 | 19.6/19.6 | 0.0/0.0 | 0.0/0.0 | +5.7 [+1.9, +10.1] | +0.0 [+0.0, +0.0] | +5.7 [+1.9, +10.1] |
| settled | variant=none | 158 | 158 | 91.8/89.2 | 8.2/10.8 | 13.9/18.4 | 0.0/0.0 | 0.0/0.0 | +2.5 [-1.3, +7.0] | +0.0 [+0.0, +0.0] | +2.5 [-1.3, +7.0] |
| settled | contested | 366 | 366 | 89.6/83.9 | 10.1/15.8 | 19.9/22.7 | 0.3/0.3 | 0.0/0.0 | +5.7 [+1.9, +9.6] | +0.0 [+0.0, +0.0] | +5.7 [+1.9, +9.6] |
| settled | uncontested | 108 | 108 | 100.0/100.0 | 0.0/0.0 | 13.0/13.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | left-coded | 117 | 117 | 76.9/63.2 | 22.2/35.9 | 33.3/29.1 | 0.9/0.9 | 0.0/0.0 | +13.7 [+3.4, +23.9] | +0.0 [+0.0, +0.0] | +13.7 [+3.4, +23.9] |
| settled | right-coded | 177 | 177 | 97.7/94.4 | 2.3/5.6 | 11.3/15.8 | 0.0/0.0 | 0.0/0.0 | +3.4 [+1.1, +6.2] | +0.0 [+0.0, +0.0] | +3.4 [+1.1, +6.2] |
| settled | uncoded | 180 | 180 | 96.1/96.7 | 3.9/3.3 | 15.6/19.4 | 0.0/0.0 | 0.0/0.0 | -0.6 [-2.8, +1.7] | +0.0 [+0.0, +0.0] | -0.6 [-2.8, +1.7] |
| settled | contested x conservative | 122 | 122 | 88.5/82.0 | 10.7/17.2 | 23.0/25.4 | 0.8/0.8 | 0.0/0.0 | +6.6 [+0.8, +12.3] | +0.0 [+0.0, +0.0] | +6.6 [+0.8, +12.3] |
| settled | contested x liberal | 122 | 122 | 91.0/83.6 | 9.0/16.4 | 22.1/22.1 | 0.0/0.0 | 0.0/0.0 | +7.4 [+2.5, +12.3] | +0.0 [+0.0, +0.0] | +7.4 [+2.5, +12.3] |

#### answer length, mean words, original / treated

- consensus | all: 85 / 79
- contested | all: 238 / 236
- settled | all: 131 / 137
- settled | contested: 141 / 147
- settled | uncontested: 99 / 104
- settled | left-coded: 176 / 181
- settled | right-coded: 120 / 126
- settled | uncoded: 113 / 118
- settled | contested x conservative: 133 / 148
- settled | contested x liberal: 137 / 140

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 70.0/98.3 | 0.0/0.0 | 30.0/1.7 | 0.0/0.0 | +0.52/+0.03 |
| liberal | 60 | 53.3/100.0 | 46.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.60/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
