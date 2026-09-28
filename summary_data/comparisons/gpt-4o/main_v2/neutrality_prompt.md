# GPT-4o: neutrality prompt against the original, settled and consensus items, version 2

original: <outputs>/gpt-4o/original/judged_main_v2.jsonl

condition neutrality_prompt: <outputs>/gpt-4o/neutrality_prompt/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 80.0/15.0 | 0.0/70.0 | 0.0/10.0 | 15.0/10.0 | 5.0/5.0 | +70.0 [+50.0, +90.0] | -5.0 [-15.0, +0.0] | +65.0 [+45.0, +85.0] |
| consensus | variant=none | 20 | 20 | 80.0/15.0 | 0.0/70.0 | 0.0/10.0 | 15.0/10.0 | 5.0/5.0 | +70.0 [+50.0, +90.0] | -5.0 [-15.0, +0.0] | +65.0 [+45.0, +85.0] |
| settled | all | 474 | 474 | 92.8/17.7 | 6.8/82.1 | 16.7/8.6 | 0.4/0.2 | 0.0/0.0 | +75.3 [+69.4, +81.4] | -0.2 [-1.3, +0.6] | +75.1 [+69.0, +81.2] |
| settled | variant=conservative | 158 | 158 | 92.4/19.6 | 7.0/80.4 | 19.6/10.8 | 0.6/0.0 | 0.0/0.0 | +73.4 [+66.5, +81.0] | -0.6 [-1.9, +0.0] | +72.8 [+65.8, +80.4] |
| settled | variant=liberal | 158 | 158 | 93.0/20.3 | 6.3/79.7 | 17.7/10.1 | 0.6/0.0 | 0.0/0.0 | +73.4 [+66.5, +80.4] | -0.6 [-1.9, +0.0] | +72.8 [+65.8, +79.7] |
| settled | variant=none | 158 | 158 | 93.0/13.3 | 7.0/86.1 | 12.7/5.1 | 0.0/0.6 | 0.0/0.0 | +79.1 [+72.8, +85.4] | +0.6 [+0.0, +1.9] | +79.7 [+73.4, +86.1] |
| settled | contested | 366 | 366 | 90.7/6.6 | 8.7/93.4 | 18.9/6.0 | 0.5/0.0 | 0.0/0.0 | +84.7 [+79.0, +89.9] | -0.5 [-1.6, +0.0] | +84.2 [+78.1, +89.6] |
| settled | uncontested | 108 | 108 | 100.0/55.6 | 0.0/43.5 | 9.3/17.6 | 0.0/0.9 | 0.0/0.0 | +43.5 [+29.6, +57.4] | +0.9 [+0.0, +2.8] | +44.4 [+31.5, +58.3] |
| settled | left-coded | 78 | 78 | 82.1/7.7 | 15.4/92.3 | 41.0/7.7 | 2.6/0.0 | 0.0/0.0 | +76.9 [+62.8, +89.7] | -2.6 [-7.7, +0.0] | +74.4 [+60.3, +87.2] |
| settled | right-coded | 177 | 177 | 97.2/7.3 | 2.8/92.7 | 10.7/6.8 | 0.0/0.0 | 0.0/0.0 | +89.8 [+82.5, +96.0] | +0.0 [+0.0, +0.0] | +89.8 [+82.5, +96.0] |
| settled | uncoded | 219 | 219 | 93.2/29.7 | 6.8/69.9 | 12.8/10.5 | 0.0/0.5 | 0.0/0.0 | +63.0 [+53.0, +73.1] | +0.5 [+0.0, +1.4] | +63.5 [+53.4, +73.1] |
| settled | contested x conservative | 122 | 122 | 90.2/8.2 | 9.0/91.8 | 21.3/8.2 | 0.8/0.0 | 0.0/0.0 | +82.8 [+75.4, +89.3] | -0.8 [-2.5, +0.0] | +82.0 [+74.6, +88.5] |
| settled | contested x liberal | 122 | 122 | 91.0/8.2 | 8.2/91.8 | 20.5/7.4 | 0.8/0.0 | 0.0/0.0 | +83.6 [+76.2, +90.2] | -0.8 [-2.5, +0.0] | +82.8 [+75.4, +89.3] |

#### answer length, mean words, original / treated

- consensus | all: 80 / 127
- contested | all: 238 / 185
- settled | all: 130 / 155
- settled | contested: 139 / 164
- settled | uncontested: 99 / 128
- settled | left-coded: 178 / 178
- settled | right-coded: 118 / 157
- settled | uncoded: 122 / 147
- settled | contested x conservative: 133 / 162
- settled | contested x liberal: 135 / 160

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 70.0/100.0 | 0.0/0.0 | 30.0/0.0 | 0.0/0.0 | +0.52/+0.00 |
| liberal | 60 | 53.3/100.0 | 46.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.60/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
