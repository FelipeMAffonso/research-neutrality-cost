# GPT-4o: one-sentence instruction not to take sides against the original, settled and consensus items, version 1

original: <outputs>/gpt-4o/original/judged_main_v1.jsonl

condition minimal_prompt: <outputs>/gpt-4o/minimal_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: one-sentence instruction not to take sides

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 85.0/80.0 | 5.0/5.0 | 5.0/0.0 | 10.0/15.0 | 0.0/0.0 | +0.0 [-15.0, +15.0] | +5.0 [+0.0, +15.0] | +5.0 [+0.0, +15.0] |
| consensus | variant=none | 20 | 20 | 85.0/80.0 | 5.0/5.0 | 5.0/0.0 | 10.0/15.0 | 0.0/0.0 | +0.0 [-15.0, +15.0] | +5.0 [+0.0, +15.0] | +5.0 [+0.0, +15.0] |
| settled | all | 474 | 474 | 92.0/85.2 | 7.8/14.6 | 18.4/12.9 | 0.2/0.2 | 0.0/0.0 | +6.8 [+3.6, +10.3] | +0.0 [-0.6, +0.6] | +6.8 [+3.6, +10.3] |
| settled | variant=conservative | 158 | 158 | 91.1/80.4 | 8.2/19.6 | 21.5/10.8 | 0.6/0.0 | 0.0/0.0 | +11.4 [+6.3, +17.1] | -0.6 [-1.9, +0.0] | +10.8 [+5.7, +16.5] |
| settled | variant=liberal | 158 | 158 | 93.0/89.2 | 7.0/10.1 | 19.6/14.6 | 0.0/0.6 | 0.0/0.0 | +3.2 [-1.3, +7.6] | +0.6 [+0.0, +1.9] | +3.8 [-0.6, +8.9] |
| settled | variant=none | 158 | 158 | 91.8/86.1 | 8.2/13.9 | 13.9/13.3 | 0.0/0.0 | 0.0/0.0 | +5.7 [+1.3, +10.8] | +0.0 [+0.0, +0.0] | +5.7 [+1.3, +10.8] |
| settled | contested | 366 | 366 | 89.6/81.1 | 10.1/18.9 | 19.9/14.2 | 0.3/0.0 | 0.0/0.0 | +8.7 [+4.6, +13.4] | -0.3 [-0.8, +0.0] | +8.5 [+4.4, +13.1] |
| settled | uncontested | 108 | 108 | 100.0/99.1 | 0.0/0.0 | 13.0/8.3 | 0.0/0.9 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.9 [+0.0, +2.8] | +0.9 [+0.0, +2.8] |
| settled | left-coded | 117 | 117 | 76.9/60.7 | 22.2/39.3 | 33.3/23.9 | 0.9/0.0 | 0.0/0.0 | +17.1 [+6.8, +29.1] | -0.9 [-2.6, +0.0] | +16.2 [+6.0, +28.2] |
| settled | right-coded | 177 | 177 | 97.7/92.7 | 2.3/7.3 | 11.3/7.9 | 0.0/0.0 | 0.0/0.0 | +5.1 [+1.7, +8.5] | +0.0 [+0.0, +0.0] | +5.1 [+1.7, +8.5] |
| settled | uncoded | 180 | 180 | 96.1/93.9 | 3.9/5.6 | 15.6/10.6 | 0.0/0.6 | 0.0/0.0 | +1.7 [-2.2, +5.6] | +0.6 [+0.0, +1.7] | +2.2 [-1.7, +6.1] |
| settled | contested x conservative | 122 | 122 | 88.5/74.6 | 10.7/25.4 | 23.0/12.3 | 0.8/0.0 | 0.0/0.0 | +14.8 [+7.4, +22.1] | -0.8 [-2.5, +0.0] | +13.9 [+6.6, +21.3] |
| settled | contested x liberal | 122 | 122 | 91.0/86.9 | 9.0/13.1 | 22.1/15.6 | 0.0/0.0 | 0.0/0.0 | +4.1 [-1.6, +10.7] | +0.0 [+0.0, +0.0] | +4.1 [-1.6, +10.7] |

#### answer length, mean words, original / treated

- consensus | all: 85 / 70
- contested | all: 238 / 198
- settled | all: 131 / 99
- settled | contested: 141 / 106
- settled | uncontested: 99 / 77
- settled | left-coded: 176 / 132
- settled | right-coded: 120 / 88
- settled | uncoded: 113 / 89
- settled | contested x conservative: 133 / 102
- settled | contested x liberal: 137 / 102

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 70.0/100.0 | 0.0/0.0 | 30.0/0.0 | 0.0/0.0 | +0.52/+0.00 |
| liberal | 60 | 53.3/100.0 | 46.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.60/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
