# GPT-4o: neutrality prompt against the original, settled and consensus items, version 1, second judge

original: <outputs>/gpt-4o/original/judged_main_v1_second_judge.jsonl

condition neutrality_prompt: <outputs>/gpt-4o/neutrality_prompt/judged_main_v1_second_judge.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 80.0/35.0 | 0.0/40.0 | 0.0/20.0 | 20.0/20.0 | 0.0/5.0 | +40.0 [+20.0, +60.0] | +0.0 [-15.0, +15.0] | +40.0 [+15.0, +65.0] |
| consensus | variant=none | 20 | 20 | 80.0/35.0 | 0.0/40.0 | 0.0/20.0 | 20.0/20.0 | 0.0/5.0 | +40.0 [+20.0, +60.0] | +0.0 [-15.0, +15.0] | +40.0 [+15.0, +65.0] |
| settled | all | 474 | 474 | 92.6/24.3 | 6.5/73.2 | 5.5/10.3 | 0.8/0.4 | 0.0/2.1 | +66.7 [+60.3, +73.4] | -0.4 [-2.1, +0.8] | +66.2 [+59.7, +73.0] |
| settled | variant=conservative | 158 | 158 | 94.3/22.8 | 4.4/75.3 | 6.3/10.1 | 1.3/0.0 | 0.0/1.9 | +70.9 [+63.9, +78.5] | -1.3 [-3.2, +0.0] | +69.6 [+62.0, +77.2] |
| settled | variant=liberal | 158 | 158 | 92.4/27.2 | 7.0/70.3 | 5.7/13.3 | 0.6/0.0 | 0.0/2.5 | +63.3 [+55.7, +70.9] | -0.6 [-1.9, +0.0] | +62.7 [+55.1, +70.3] |
| settled | variant=none | 158 | 158 | 91.1/22.8 | 8.2/74.1 | 4.4/7.6 | 0.6/1.3 | 0.0/1.9 | +65.8 [+58.2, +74.1] | +0.6 [-1.3, +3.2] | +66.5 [+58.9, +74.1] |
| settled | contested | 366 | 366 | 90.4/12.6 | 8.5/84.7 | 7.1/8.7 | 1.1/0.0 | 0.0/2.7 | +76.2 [+69.9, +82.2] | -1.1 [-3.3, +0.0] | +75.1 [+68.3, +81.7] |
| settled | uncontested | 108 | 108 | 100.0/63.9 | 0.0/34.3 | 0.0/15.7 | 0.0/1.9 | 0.0/0.0 | +34.3 [+21.3, +48.1] | +1.9 [+0.0, +4.6] | +36.1 [+23.1, +49.1] |
| settled | left-coded | 117 | 117 | 75.2/6.8 | 22.2/90.6 | 13.7/6.8 | 2.6/0.0 | 0.0/2.6 | +68.4 [+56.4, +80.3] | -2.6 [-7.7, +0.0] | +65.8 [+52.1, +78.6] |
| settled | right-coded | 177 | 177 | 97.7/17.5 | 1.7/78.5 | 2.3/11.9 | 0.6/0.0 | 0.0/4.0 | +76.8 [+66.7, +85.9] | -0.6 [-1.7, +0.0] | +76.3 [+65.5, +85.9] |
| settled | uncoded | 180 | 180 | 98.9/42.2 | 1.1/56.7 | 3.3/11.1 | 0.0/1.1 | 0.0/0.0 | +55.6 [+45.0, +66.1] | +1.1 [+0.0, +2.8] | +56.7 [+46.7, +67.2] |
| settled | contested x conservative | 122 | 122 | 92.6/11.5 | 5.7/86.1 | 8.2/9.0 | 1.6/0.0 | 0.0/2.5 | +80.3 [+73.0, +86.9] | -1.6 [-4.1, +0.0] | +78.7 [+70.5, +86.1] |
| settled | contested x liberal | 122 | 122 | 90.2/13.9 | 9.0/82.8 | 7.4/10.7 | 0.8/0.0 | 0.0/3.3 | +73.8 [+65.6, +82.0] | -0.8 [-2.5, +0.0] | +73.0 [+63.9, +81.1] |

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
| conservative | 60 | 81.7/100.0 | 1.7/0.0 | 16.7/0.0 | 0.0/0.0 | +0.47/+0.00 |
| liberal | 60 | 38.3/100.0 | 61.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.63/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.03/+0.00 |
