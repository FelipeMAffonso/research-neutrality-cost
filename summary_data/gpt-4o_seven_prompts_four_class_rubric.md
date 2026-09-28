# GPT-4o under the seven system prompts, settled and consensus items, version 1, four-class rubric

original: <outputs>/gpt-4o/original/judged_main_v1_four_class_rubric.jsonl

condition style_control_prompt: <outputs>/gpt-4o/style_control_prompt/judged_main_v1_four_class_rubric.jsonl
condition minimal_prompt: <outputs>/gpt-4o/minimal_prompt/judged_main_v1_four_class_rubric.jsonl
condition mild_prompt: <outputs>/gpt-4o/mild_prompt/judged_main_v1_four_class_rubric.jsonl
condition journalist_prompt: <outputs>/gpt-4o/journalist_prompt/judged_main_v1_four_class_rubric.jsonl
condition mandate_prompt_federal: <outputs>/gpt-4o/mandate_prompt_federal/judged_main_v1_four_class_rubric.jsonl
condition mandate_prompt_plain: <outputs>/gpt-4o/mandate_prompt_plain/judged_main_v1_four_class_rubric.jsonl
condition neutrality_prompt: <outputs>/gpt-4o/neutrality_prompt/judged_main_v1_four_class_rubric.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: style-only control

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 80.0/85.0 | 10.0/5.0 | 0.0/0.0 | 10.0/10.0 | 0.0/0.0 | -5.0 [-15.0, +0.0] | +0.0 [-15.0, +15.0] | -5.0 [-25.0, +10.0] |
| consensus | variant=none | 20 | 20 | 80.0/85.0 | 10.0/5.0 | 0.0/0.0 | 10.0/10.0 | 0.0/0.0 | -5.0 [-15.0, +0.0] | +0.0 [-15.0, +15.0] | -5.0 [-25.0, +10.0] |
| settled | all | 474 | 474 | 88.8/95.6 | 11.0/4.0 | 0.0/0.0 | 0.2/0.4 | 0.0/0.0 | -7.0 [-10.5, -4.0] | +0.2 [+0.0, +0.6] | -6.8 [-10.3, -3.8] |
| settled | variant=conservative | 158 | 158 | 88.6/96.2 | 10.8/3.8 | 0.0/0.0 | 0.6/0.0 | 0.0/0.0 | -7.0 [-11.4, -3.2] | -0.6 [-1.9, +0.0] | -7.6 [-12.0, -3.8] |
| settled | variant=liberal | 158 | 158 | 90.5/96.2 | 9.5/3.2 | 0.0/0.0 | 0.0/0.6 | 0.0/0.0 | -6.3 [-10.8, -1.9] | +0.6 [+0.0, +1.9] | -5.7 [-10.1, -1.3] |
| settled | variant=none | 158 | 158 | 87.3/94.3 | 12.7/5.1 | 0.0/0.0 | 0.0/0.6 | 0.0/0.0 | -7.6 [-12.7, -3.2] | +0.6 [+0.0, +1.9] | -7.0 [-12.0, -1.9] |
| settled | contested | 366 | 366 | 85.5/94.5 | 14.2/5.2 | 0.0/0.0 | 0.3/0.3 | 0.0/0.0 | -9.0 [-13.4, -4.9] | +0.0 [+0.0, +0.0] | -9.0 [-13.4, -4.9] |
| settled | uncontested | 108 | 108 | 100.0/99.1 | 0.0/0.0 | 0.0/0.0 | 0.0/0.9 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.9 [+0.0, +2.8] | +0.9 [+0.0, +2.8] |
| settled | left-coded | 117 | 117 | 70.1/85.5 | 29.1/13.7 | 0.0/0.0 | 0.9/0.9 | 0.0/0.0 | -15.4 [-24.8, -6.0] | +0.0 [+0.0, +0.0] | -15.4 [-24.8, -6.0] |
| settled | right-coded | 177 | 177 | 96.0/98.3 | 4.0/1.7 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | -2.3 [-5.1, +0.0] | +0.0 [+0.0, +0.0] | -2.3 [-5.1, +0.0] |
| settled | uncoded | 180 | 180 | 93.9/99.4 | 6.1/0.0 | 0.0/0.0 | 0.0/0.6 | 0.0/0.0 | -6.1 [-11.7, -1.7] | +0.6 [+0.0, +1.7] | -5.6 [-11.1, -0.6] |
| settled | contested x conservative | 122 | 122 | 85.2/95.1 | 13.9/4.9 | 0.0/0.0 | 0.8/0.0 | 0.0/0.0 | -9.0 [-14.8, -4.1] | -0.8 [-2.5, +0.0] | -9.8 [-14.8, -4.9] |
| settled | contested x liberal | 122 | 122 | 87.7/95.1 | 12.3/4.1 | 0.0/0.0 | 0.0/0.8 | 0.0/0.0 | -8.2 [-13.9, -2.5] | +0.8 [+0.0, +2.5] | -7.4 [-13.1, -1.6] |

#### answer length, mean words, original / treated

- consensus | all: 85 / 39
- contested | all: 238 / 161
- settled | all: 131 / 64
- settled | contested: 141 / 67
- settled | uncontested: 99 / 56
- settled | left-coded: 176 / 78
- settled | right-coded: 120 / 60
- settled | uncoded: 113 / 60
- settled | contested x conservative: 133 / 67
- settled | contested x liberal: 137 / 66

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 70.0/86.7 | 0.0/0.0 | 30.0/13.3 | 0.0/0.0 | +0.52/+0.22 |
| liberal | 60 | 53.3/83.3 | 46.7/16.7 | 0.0/0.0 | 0.0/0.0 | -0.60/-0.18 |
| none | 60 | 100.0/95.0 | 0.0/5.0 | 0.0/0.0 | 0.0/0.0 | +0.00/-0.07 |

### condition: one-sentence instruction not to take sides

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 80.0/80.0 | 10.0/5.0 | 0.0/0.0 | 10.0/15.0 | 0.0/0.0 | -5.0 [-25.0, +10.0] | +5.0 [+0.0, +15.0] | +0.0 [-15.0, +15.0] |
| consensus | variant=none | 20 | 20 | 80.0/80.0 | 10.0/5.0 | 0.0/0.0 | 10.0/15.0 | 0.0/0.0 | -5.0 [-25.0, +10.0] | +5.0 [+0.0, +15.0] | +0.0 [-15.0, +15.0] |
| settled | all | 474 | 474 | 88.8/79.1 | 11.0/20.7 | 0.0/0.0 | 0.2/0.2 | 0.0/0.0 | +9.7 [+6.3, +13.5] | +0.0 [-0.6, +0.6] | +9.7 [+6.3, +13.5] |
| settled | variant=conservative | 158 | 158 | 88.6/73.4 | 10.8/26.6 | 0.0/0.0 | 0.6/0.0 | 0.0/0.0 | +15.8 [+10.1, +22.2] | -0.6 [-1.9, +0.0] | +15.2 [+9.5, +21.5] |
| settled | variant=liberal | 158 | 158 | 90.5/79.7 | 9.5/19.6 | 0.0/0.0 | 0.0/0.6 | 0.0/0.0 | +10.1 [+5.1, +15.2] | +0.6 [+0.0, +1.9] | +10.8 [+5.7, +15.8] |
| settled | variant=none | 158 | 158 | 87.3/84.2 | 12.7/15.8 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +3.2 [-1.9, +8.9] | +0.0 [+0.0, +0.0] | +3.2 [-1.9, +8.9] |
| settled | contested | 366 | 366 | 85.5/73.2 | 14.2/26.8 | 0.0/0.0 | 0.3/0.0 | 0.0/0.0 | +12.6 [+8.2, +17.2] | -0.3 [-0.8, +0.0] | +12.3 [+7.9, +16.9] |
| settled | uncontested | 108 | 108 | 100.0/99.1 | 0.0/0.0 | 0.0/0.0 | 0.0/0.9 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.9 [+0.0, +2.8] | +0.9 [+0.0, +2.8] |
| settled | left-coded | 117 | 117 | 70.1/47.0 | 29.1/53.0 | 0.0/0.0 | 0.9/0.0 | 0.0/0.0 | +23.9 [+13.7, +35.0] | -0.9 [-2.6, +0.0] | +23.1 [+12.8, +34.2] |
| settled | right-coded | 177 | 177 | 96.0/88.7 | 4.0/11.3 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +7.3 [+3.4, +11.9] | +0.0 [+0.0, +0.0] | +7.3 [+3.4, +11.9] |
| settled | uncoded | 180 | 180 | 93.9/90.6 | 6.1/8.9 | 0.0/0.0 | 0.0/0.6 | 0.0/0.0 | +2.8 [+0.0, +6.1] | +0.6 [+0.0, +1.7] | +3.3 [+0.0, +6.7] |
| settled | contested x conservative | 122 | 122 | 85.2/65.6 | 13.9/34.4 | 0.0/0.0 | 0.8/0.0 | 0.0/0.0 | +20.5 [+13.1, +27.9] | -0.8 [-2.5, +0.0] | +19.7 [+12.3, +27.0] |
| settled | contested x liberal | 122 | 122 | 87.7/74.6 | 12.3/25.4 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +13.1 [+7.4, +19.7] | +0.0 [+0.0, +0.0] | +13.1 [+7.4, +19.7] |

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

### condition: mild even-handedness instruction

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 80.0/80.0 | 10.0/0.0 | 0.0/0.0 | 10.0/20.0 | 0.0/0.0 | -10.0 [-25.0, +0.0] | +10.0 [+0.0, +25.0] | +0.0 [-15.0, +15.0] |
| consensus | variant=none | 20 | 20 | 80.0/80.0 | 10.0/0.0 | 0.0/0.0 | 10.0/20.0 | 0.0/0.0 | -10.0 [-25.0, +0.0] | +10.0 [+0.0, +25.0] | +0.0 [-15.0, +15.0] |
| settled | all | 474 | 474 | 88.8/82.1 | 11.0/17.7 | 0.0/0.0 | 0.2/0.2 | 0.0/0.0 | +6.8 [+3.6, +10.5] | +0.0 [+0.0, +0.0] | +6.8 [+3.6, +10.5] |
| settled | variant=conservative | 158 | 158 | 88.6/78.5 | 10.8/20.9 | 0.0/0.0 | 0.6/0.6 | 0.0/0.0 | +10.1 [+5.1, +15.8] | +0.0 [+0.0, +0.0] | +10.1 [+5.1, +15.8] |
| settled | variant=liberal | 158 | 158 | 90.5/84.2 | 9.5/15.8 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +6.3 [+3.2, +10.1] | +0.0 [+0.0, +0.0] | +6.3 [+3.2, +10.1] |
| settled | variant=none | 158 | 158 | 87.3/83.5 | 12.7/16.5 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +3.8 [-1.3, +8.9] | +0.0 [+0.0, +0.0] | +3.8 [-1.3, +8.9] |
| settled | contested | 366 | 366 | 85.5/76.8 | 14.2/23.0 | 0.0/0.0 | 0.3/0.3 | 0.0/0.0 | +8.7 [+4.6, +13.1] | +0.0 [+0.0, +0.0] | +8.7 [+4.6, +13.1] |
| settled | uncontested | 108 | 108 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | left-coded | 117 | 117 | 70.1/53.0 | 29.1/46.2 | 0.0/0.0 | 0.9/0.9 | 0.0/0.0 | +17.1 [+7.7, +26.5] | +0.0 [+0.0, +0.0] | +17.1 [+7.7, +26.5] |
| settled | right-coded | 177 | 177 | 96.0/92.1 | 4.0/7.9 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +4.0 [+0.6, +7.9] | +0.0 [+0.0, +0.0] | +4.0 [+0.6, +7.9] |
| settled | uncoded | 180 | 180 | 93.9/91.1 | 6.1/8.9 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +2.8 [-1.1, +7.8] | +0.0 [+0.0, +0.0] | +2.8 [-1.1, +7.8] |
| settled | contested x conservative | 122 | 122 | 85.2/72.1 | 13.9/27.0 | 0.0/0.0 | 0.8/0.8 | 0.0/0.0 | +13.1 [+6.6, +19.7] | +0.0 [+0.0, +0.0] | +13.1 [+6.6, +19.7] |
| settled | contested x liberal | 122 | 122 | 87.7/79.5 | 12.3/20.5 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +8.2 [+4.1, +13.1] | +0.0 [+0.0, +0.0] | +8.2 [+4.1, +13.1] |

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

### condition: journalist's balance norm

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 80.0/40.0 | 10.0/45.0 | 0.0/0.0 | 10.0/15.0 | 0.0/0.0 | +35.0 [+10.0, +60.0] | +5.0 [+0.0, +15.0] | +40.0 [+15.0, +65.0] |
| consensus | variant=none | 20 | 20 | 80.0/40.0 | 10.0/45.0 | 0.0/0.0 | 10.0/15.0 | 0.0/0.0 | +35.0 [+10.0, +60.0] | +5.0 [+0.0, +15.0] | +40.0 [+15.0, +65.0] |
| settled | all | 474 | 474 | 88.8/17.7 | 11.0/82.1 | 0.0/0.0 | 0.2/0.2 | 0.0/0.0 | +71.1 [+64.8, +77.2] | +0.0 [-0.6, +0.6] | +71.1 [+65.0, +77.2] |
| settled | variant=conservative | 158 | 158 | 88.6/17.7 | 10.8/82.3 | 0.0/0.0 | 0.6/0.0 | 0.0/0.0 | +71.5 [+64.6, +78.5] | -0.6 [-1.9, +0.0] | +70.9 [+63.9, +77.8] |
| settled | variant=liberal | 158 | 158 | 90.5/17.1 | 9.5/82.3 | 0.0/0.0 | 0.0/0.6 | 0.0/0.0 | +72.8 [+65.8, +79.7] | +0.6 [+0.0, +1.9] | +73.4 [+66.5, +80.4] |
| settled | variant=none | 158 | 158 | 87.3/18.4 | 12.7/81.6 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +69.0 [+61.4, +75.9] | +0.0 [+0.0, +0.0] | +69.0 [+61.4, +75.9] |
| settled | contested | 366 | 366 | 85.5/7.7 | 14.2/92.3 | 0.0/0.0 | 0.3/0.0 | 0.0/0.0 | +78.1 [+72.1, +84.2] | -0.3 [-0.8, +0.0] | +77.9 [+71.9, +83.9] |
| settled | uncontested | 108 | 108 | 100.0/51.9 | 0.0/47.2 | 0.0/0.0 | 0.0/0.9 | 0.0/0.0 | +47.2 [+32.4, +61.1] | +0.9 [+0.0, +2.8] | +48.1 [+34.3, +62.0] |
| settled | left-coded | 117 | 117 | 70.1/1.7 | 29.1/98.3 | 0.0/0.0 | 0.9/0.0 | 0.0/0.0 | +69.2 [+57.3, +81.2] | -0.9 [-2.6, +0.0] | +68.4 [+55.6, +80.3] |
| settled | right-coded | 177 | 177 | 96.0/12.4 | 4.0/87.6 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +83.6 [+75.7, +91.0] | +0.0 [+0.0, +0.0] | +83.6 [+75.7, +91.0] |
| settled | uncoded | 180 | 180 | 93.9/33.3 | 6.1/66.1 | 0.0/0.0 | 0.0/0.6 | 0.0/0.0 | +60.0 [+48.3, +71.1] | +0.6 [+0.0, +1.7] | +60.6 [+49.4, +71.1] |
| settled | contested x conservative | 122 | 122 | 85.2/5.7 | 13.9/94.3 | 0.0/0.0 | 0.8/0.0 | 0.0/0.0 | +80.3 [+73.8, +86.9] | -0.8 [-2.5, +0.0] | +79.5 [+73.0, +86.1] |
| settled | contested x liberal | 122 | 122 | 87.7/8.2 | 12.3/91.8 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +79.5 [+72.1, +86.9] | +0.0 [+0.0, +0.0] | +79.5 [+72.1, +86.9] |

#### answer length, mean words, original / treated

- consensus | all: 85 / 156
- contested | all: 238 / 246
- settled | all: 131 / 201
- settled | contested: 141 / 209
- settled | uncontested: 99 / 173
- settled | left-coded: 176 / 218
- settled | right-coded: 120 / 203
- settled | uncoded: 113 / 188
- settled | contested x conservative: 133 / 207
- settled | contested x liberal: 137 / 204

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 70.0/100.0 | 0.0/0.0 | 30.0/0.0 | 0.0/0.0 | +0.52/+0.00 |
| liberal | 60 | 53.3/100.0 | 46.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.60/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |

### condition: mandate wording, federally procured assistant

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 80.0/85.0 | 10.0/0.0 | 0.0/0.0 | 10.0/15.0 | 0.0/0.0 | -10.0 [-25.0, +0.0] | +5.0 [+0.0, +15.0] | -5.0 [-15.0, +0.0] |
| consensus | variant=none | 20 | 20 | 80.0/85.0 | 10.0/0.0 | 0.0/0.0 | 10.0/15.0 | 0.0/0.0 | -10.0 [-25.0, +0.0] | +5.0 [+0.0, +15.0] | -5.0 [-15.0, +0.0] |
| settled | all | 474 | 474 | 88.8/89.2 | 11.0/10.5 | 0.0/0.0 | 0.2/0.2 | 0.0/0.0 | -0.4 [-3.4, +2.7] | +0.0 [+0.0, +0.0] | -0.4 [-3.4, +2.7] |
| settled | variant=conservative | 158 | 158 | 88.6/89.2 | 10.8/10.1 | 0.0/0.0 | 0.6/0.6 | 0.0/0.0 | -0.6 [-5.1, +4.4] | +0.0 [+0.0, +0.0] | -0.6 [-5.1, +4.4] |
| settled | variant=liberal | 158 | 158 | 90.5/89.2 | 9.5/10.8 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +1.3 [-3.2, +5.7] | +0.0 [+0.0, +0.0] | +1.3 [-3.2, +5.7] |
| settled | variant=none | 158 | 158 | 87.3/89.2 | 12.7/10.8 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | -1.9 [-6.3, +2.5] | +0.0 [+0.0, +0.0] | -1.9 [-6.3, +2.5] |
| settled | contested | 366 | 366 | 85.5/86.1 | 14.2/13.7 | 0.0/0.0 | 0.3/0.3 | 0.0/0.0 | -0.5 [-4.4, +3.3] | +0.0 [+0.0, +0.0] | -0.5 [-4.4, +3.3] |
| settled | uncontested | 108 | 108 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | left-coded | 117 | 117 | 70.1/65.8 | 29.1/33.3 | 0.0/0.0 | 0.9/0.9 | 0.0/0.0 | +4.3 [-4.3, +12.8] | +0.0 [+0.0, +0.0] | +4.3 [-4.3, +12.8] |
| settled | right-coded | 177 | 177 | 96.0/97.7 | 4.0/2.3 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | -1.7 [-5.1, +1.1] | +0.0 [+0.0, +0.0] | -1.7 [-5.1, +1.1] |
| settled | uncoded | 180 | 180 | 93.9/96.1 | 6.1/3.9 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | -2.2 [-7.2, +1.7] | +0.0 [+0.0, +0.0] | -2.2 [-7.2, +1.7] |
| settled | contested x conservative | 122 | 122 | 85.2/86.1 | 13.9/13.1 | 0.0/0.0 | 0.8/0.8 | 0.0/0.0 | -0.8 [-7.4, +4.9] | +0.0 [+0.0, +0.0] | -0.8 [-7.4, +4.9] |
| settled | contested x liberal | 122 | 122 | 87.7/86.1 | 12.3/13.9 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +1.6 [-3.3, +7.4] | +0.0 [+0.0, +0.0] | +1.6 [-3.3, +7.4] |

#### answer length, mean words, original / treated

- consensus | all: 85 / 87
- contested | all: 238 / 232
- settled | all: 131 / 125
- settled | contested: 141 / 132
- settled | uncontested: 99 / 100
- settled | left-coded: 176 / 161
- settled | right-coded: 120 / 114
- settled | uncoded: 113 / 113
- settled | contested x conservative: 133 / 130
- settled | contested x liberal: 137 / 127

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 70.0/98.3 | 0.0/0.0 | 30.0/1.7 | 0.0/0.0 | +0.52/+0.02 |
| liberal | 60 | 53.3/100.0 | 46.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.60/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |

### condition: mandate wording, no government framing

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 80.0/85.0 | 10.0/0.0 | 0.0/0.0 | 10.0/15.0 | 0.0/0.0 | -10.0 [-25.0, +0.0] | +5.0 [+0.0, +15.0] | -5.0 [-15.0, +0.0] |
| consensus | variant=none | 20 | 20 | 80.0/85.0 | 10.0/0.0 | 0.0/0.0 | 10.0/15.0 | 0.0/0.0 | -10.0 [-25.0, +0.0] | +5.0 [+0.0, +15.0] | -5.0 [-15.0, +0.0] |
| settled | all | 474 | 474 | 88.8/86.7 | 11.0/13.1 | 0.0/0.0 | 0.2/0.2 | 0.0/0.0 | +2.1 [-0.4, +4.9] | +0.0 [-0.6, +0.6] | +2.1 [-0.4, +4.9] |
| settled | variant=conservative | 158 | 158 | 88.6/86.1 | 10.8/13.9 | 0.0/0.0 | 0.6/0.0 | 0.0/0.0 | +3.2 [-1.3, +8.2] | -0.6 [-1.9, +0.0] | +2.5 [-1.9, +7.0] |
| settled | variant=liberal | 158 | 158 | 90.5/86.1 | 9.5/13.3 | 0.0/0.0 | 0.0/0.6 | 0.0/0.0 | +3.8 [-0.6, +8.9] | +0.6 [+0.0, +1.9] | +4.4 [-0.6, +9.5] |
| settled | variant=none | 158 | 158 | 87.3/88.0 | 12.7/12.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.6 [-5.1, +3.8] | +0.0 [+0.0, +0.0] | -0.6 [-5.1, +3.8] |
| settled | contested | 366 | 366 | 85.5/82.8 | 14.2/16.9 | 0.0/0.0 | 0.3/0.3 | 0.0/0.0 | +2.7 [-0.8, +6.3] | +0.0 [-0.8, +0.8] | +2.7 [-0.8, +6.0] |
| settled | uncontested | 108 | 108 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | left-coded | 117 | 117 | 70.1/59.8 | 29.1/39.3 | 0.0/0.0 | 0.9/0.9 | 0.0/0.0 | +10.3 [+1.7, +18.8] | +0.0 [-2.6, +2.6] | +10.3 [+1.7, +18.8] |
| settled | right-coded | 177 | 177 | 96.0/96.6 | 4.0/3.4 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.6 [-2.3, +1.1] | +0.0 [+0.0, +0.0] | -0.6 [-2.3, +1.1] |
| settled | uncoded | 180 | 180 | 93.9/94.4 | 6.1/5.6 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.6 [-3.9, +2.2] | +0.0 [+0.0, +0.0] | -0.6 [-3.9, +2.2] |
| settled | contested x conservative | 122 | 122 | 85.2/82.0 | 13.9/18.0 | 0.0/0.0 | 0.8/0.0 | 0.0/0.0 | +4.1 [-1.6, +9.8] | -0.8 [-2.5, +0.0] | +3.3 [-2.5, +9.0] |
| settled | contested x liberal | 122 | 122 | 87.7/82.0 | 12.3/17.2 | 0.0/0.0 | 0.0/0.8 | 0.0/0.0 | +4.9 [-0.8, +11.5] | +0.8 [+0.0, +2.5] | +5.7 [-0.8, +12.3] |

#### answer length, mean words, original / treated

- consensus | all: 85 / 86
- contested | all: 238 / 233
- settled | all: 131 / 125
- settled | contested: 141 / 133
- settled | uncontested: 99 / 98
- settled | left-coded: 176 / 161
- settled | right-coded: 120 / 114
- settled | uncoded: 113 / 112
- settled | contested x conservative: 133 / 129
- settled | contested x liberal: 137 / 125

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 70.0/96.7 | 0.0/0.0 | 30.0/3.3 | 0.0/0.0 | +0.52/+0.03 |
| liberal | 60 | 53.3/100.0 | 46.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.60/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 80.0/15.0 | 10.0/75.0 | 0.0/0.0 | 10.0/10.0 | 0.0/0.0 | +65.0 [+40.0, +90.0] | +0.0 [+0.0, +0.0] | +65.0 [+40.0, +90.0] |
| consensus | variant=none | 20 | 20 | 80.0/15.0 | 10.0/75.0 | 0.0/0.0 | 10.0/10.0 | 0.0/0.0 | +65.0 [+40.0, +90.0] | +0.0 [+0.0, +0.0] | +65.0 [+40.0, +90.0] |
| settled | all | 474 | 474 | 88.8/10.3 | 11.0/89.2 | 0.0/0.0 | 0.2/0.4 | 0.0/0.0 | +78.3 [+72.6, +83.8] | +0.2 [-0.6, +1.3] | +78.5 [+72.8, +84.2] |
| settled | variant=conservative | 158 | 158 | 88.6/10.8 | 10.8/89.2 | 0.0/0.0 | 0.6/0.0 | 0.0/0.0 | +78.5 [+72.2, +84.8] | -0.6 [-1.9, +0.0] | +77.8 [+71.5, +84.2] |
| settled | variant=liberal | 158 | 158 | 90.5/11.4 | 9.5/88.0 | 0.0/0.0 | 0.0/0.6 | 0.0/0.0 | +78.5 [+72.2, +84.8] | +0.6 [+0.0, +1.9] | +79.1 [+72.8, +85.4] |
| settled | variant=none | 158 | 158 | 87.3/8.9 | 12.7/90.5 | 0.0/0.0 | 0.0/0.6 | 0.0/0.0 | +77.8 [+71.5, +83.5] | +0.6 [+0.0, +1.9] | +78.5 [+72.2, +84.8] |
| settled | contested | 366 | 366 | 85.5/1.4 | 14.2/98.6 | 0.0/0.0 | 0.3/0.0 | 0.0/0.0 | +84.4 [+79.0, +89.9] | -0.3 [-0.8, +0.0] | +84.2 [+78.7, +89.6] |
| settled | uncontested | 108 | 108 | 100.0/40.7 | 0.0/57.4 | 0.0/0.0 | 0.0/1.9 | 0.0/0.0 | +57.4 [+41.7, +72.2] | +1.9 [+0.0, +5.6] | +59.3 [+44.4, +74.1] |
| settled | left-coded | 117 | 117 | 70.1/0.0 | 29.1/100.0 | 0.0/0.0 | 0.9/0.0 | 0.0/0.0 | +70.9 [+59.0, +82.9] | -0.9 [-2.6, +0.0] | +70.1 [+57.3, +82.9] |
| settled | right-coded | 177 | 177 | 96.0/1.7 | 4.0/98.3 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +94.4 [+89.3, +98.3] | +0.0 [+0.0, +0.0] | +94.4 [+89.3, +98.3] |
| settled | uncoded | 180 | 180 | 93.9/25.6 | 6.1/73.3 | 0.0/0.0 | 0.0/1.1 | 0.0/0.0 | +67.2 [+56.1, +78.3] | +1.1 [+0.0, +3.3] | +68.3 [+57.2, +78.9] |
| settled | contested x conservative | 122 | 122 | 85.2/1.6 | 13.9/98.4 | 0.0/0.0 | 0.8/0.0 | 0.0/0.0 | +84.4 [+78.7, +90.2] | -0.8 [-2.5, +0.0] | +83.6 [+77.0, +90.2] |
| settled | contested x liberal | 122 | 122 | 87.7/0.8 | 12.3/99.2 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +86.9 [+81.1, +92.6] | +0.0 [+0.0, +0.0] | +86.9 [+81.1, +92.6] |

#### answer length, mean words, original / treated

- consensus | all: 85 / 128
- contested | all: 238 / 185
- settled | all: 131 / 156
- settled | contested: 141 / 164
- settled | uncontested: 99 / 127
- settled | left-coded: 176 / 176
- settled | right-coded: 120 / 157
- settled | uncoded: 113 / 143
- settled | contested x conservative: 133 / 163
- settled | contested x liberal: 137 / 160

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 70.0/100.0 | 0.0/0.0 | 30.0/0.0 | 0.0/0.0 | +0.52/+0.00 |
| liberal | 60 | 53.3/100.0 | 46.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.60/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
