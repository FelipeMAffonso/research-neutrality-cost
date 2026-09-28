# GPT-4o: neutrality prompt against the original, settled and consensus items, version 1

original: <outputs>/gpt-4o/original/judged_main_v1.jsonl

condition neutrality_prompt: <outputs>/gpt-4o/neutrality_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 85.0/15.0 | 5.0/75.0 | 5.0/10.0 | 10.0/10.0 | 0.0/0.0 | +70.0 [+50.0, +90.0] | +0.0 [+0.0, +0.0] | +70.0 [+50.0, +90.0] |
| consensus | variant=none | 20 | 20 | 85.0/15.0 | 5.0/75.0 | 5.0/10.0 | 10.0/10.0 | 0.0/0.0 | +70.0 [+50.0, +90.0] | +0.0 [+0.0, +0.0] | +70.0 [+50.0, +90.0] |
| settled | all | 474 | 474 | 92.0/16.7 | 7.8/83.1 | 18.4/7.6 | 0.2/0.2 | 0.0/0.0 | +75.3 [+69.4, +81.2] | +0.0 [-0.6, +0.6] | +75.3 [+69.4, +81.2] |
| settled | variant=conservative | 158 | 158 | 91.1/18.4 | 8.2/81.6 | 21.5/9.5 | 0.6/0.0 | 0.0/0.0 | +73.4 [+66.5, +81.0] | -0.6 [-1.9, +0.0] | +72.8 [+65.8, +80.4] |
| settled | variant=liberal | 158 | 158 | 93.0/19.6 | 7.0/80.4 | 19.6/9.5 | 0.0/0.0 | 0.0/0.0 | +73.4 [+66.5, +80.4] | +0.0 [+0.0, +0.0] | +73.4 [+66.5, +80.4] |
| settled | variant=none | 158 | 158 | 91.8/12.0 | 8.2/87.3 | 13.9/3.8 | 0.0/0.6 | 0.0/0.0 | +79.1 [+72.8, +85.4] | +0.6 [+0.0, +1.9] | +79.7 [+73.4, +85.4] |
| settled | contested | 366 | 366 | 89.6/6.0 | 10.1/94.0 | 19.9/5.5 | 0.3/0.0 | 0.0/0.0 | +83.9 [+78.4, +89.1] | -0.3 [-0.8, +0.0] | +83.6 [+77.9, +88.8] |
| settled | uncontested | 108 | 108 | 100.0/52.8 | 0.0/46.3 | 13.0/14.8 | 0.0/0.9 | 0.0/0.0 | +46.3 [+32.4, +61.1] | +0.9 [+0.0, +2.8] | +47.2 [+33.3, +61.1] |
| settled | left-coded | 117 | 117 | 76.9/5.1 | 22.2/94.9 | 33.3/5.1 | 0.9/0.0 | 0.0/0.0 | +72.6 [+60.7, +83.8] | -0.9 [-2.6, +0.0] | +71.8 [+59.8, +82.9] |
| settled | right-coded | 177 | 177 | 97.7/7.3 | 2.3/92.7 | 11.3/6.8 | 0.0/0.0 | 0.0/0.0 | +90.4 [+83.6, +96.0] | +0.0 [+0.0, +0.0] | +90.4 [+83.6, +96.0] |
| settled | uncoded | 180 | 180 | 96.1/33.3 | 3.9/66.1 | 15.6/10.0 | 0.0/0.6 | 0.0/0.0 | +62.2 [+51.7, +72.8] | +0.6 [+0.0, +1.7] | +62.8 [+52.2, +73.3] |
| settled | contested x conservative | 122 | 122 | 88.5/8.2 | 10.7/91.8 | 23.0/8.2 | 0.8/0.0 | 0.0/0.0 | +81.1 [+73.8, +87.7] | -0.8 [-2.5, +0.0] | +80.3 [+73.0, +86.9] |
| settled | contested x liberal | 122 | 122 | 91.0/7.4 | 9.0/92.6 | 22.1/6.6 | 0.0/0.0 | 0.0/0.0 | +83.6 [+76.2, +90.2] | +0.0 [+0.0, +0.0] | +83.6 [+76.2, +90.2] |

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
