# GPT-4.1: neutrality prompt against the original, settled and consensus items, version 1

original: <outputs>/gpt-4.1/original/judged_main_v1.jsonl

condition neutrality_prompt: <outputs>/gpt-4.1/neutrality_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 95.0/20.0 | 0.0/80.0 | 0.0/10.0 | 5.0/0.0 | 0.0/0.0 | +80.0 [+60.0, +95.0] | -5.0 [-15.0, +0.0] | +75.0 [+55.0, +95.0] |
| consensus | variant=none | 20 | 20 | 95.0/20.0 | 0.0/80.0 | 0.0/10.0 | 5.0/0.0 | 0.0/0.0 | +80.0 [+60.0, +95.0] | -5.0 [-15.0, +0.0] | +75.0 [+55.0, +95.0] |
| settled | all | 474 | 474 | 98.3/15.4 | 1.1/84.4 | 3.0/6.1 | 0.6/0.2 | 0.0/0.0 | +83.3 [+78.5, +88.2] | -0.4 [-1.3, +0.4] | +82.9 [+78.1, +88.0] |
| settled | variant=conservative | 158 | 158 | 98.1/15.8 | 0.6/84.2 | 7.0/5.7 | 1.3/0.0 | 0.0/0.0 | +83.5 [+77.8, +89.2] | -1.3 [-3.2, +0.0] | +82.3 [+75.9, +88.6] |
| settled | variant=liberal | 158 | 158 | 99.4/14.6 | 0.6/85.4 | 1.9/6.3 | 0.0/0.0 | 0.0/0.0 | +84.8 [+79.1, +89.9] | +0.0 [+0.0, +0.0] | +84.8 [+79.1, +89.9] |
| settled | variant=none | 158 | 158 | 97.5/15.8 | 1.9/83.5 | 0.0/6.3 | 0.6/0.6 | 0.0/0.0 | +81.6 [+75.3, +88.0] | +0.0 [-1.9, +1.9] | +81.6 [+75.3, +88.0] |
| settled | contested | 366 | 366 | 98.1/6.6 | 1.4/93.4 | 3.0/4.9 | 0.5/0.0 | 0.0/0.0 | +92.1 [+88.8, +95.1] | -0.5 [-1.4, +0.0] | +91.5 [+88.0, +94.8] |
| settled | uncontested | 108 | 108 | 99.1/45.4 | 0.0/53.7 | 2.8/10.2 | 0.9/0.9 | 0.0/0.0 | +53.7 [+38.9, +67.6] | +0.0 [-2.8, +2.8] | +53.7 [+38.0, +68.5] |
| settled | left-coded | 117 | 117 | 95.7/5.1 | 3.4/94.9 | 2.6/5.1 | 0.9/0.0 | 0.0/0.0 | +91.5 [+83.8, +97.4] | -0.9 [-2.6, +0.0] | +90.6 [+82.1, +97.4] |
| settled | right-coded | 177 | 177 | 99.4/8.5 | 0.0/91.5 | 4.0/6.2 | 0.6/0.0 | 0.0/0.0 | +91.5 [+86.4, +96.0] | -0.6 [-1.7, +0.0] | +91.0 [+85.9, +95.5] |
| settled | uncoded | 180 | 180 | 98.9/28.9 | 0.6/70.6 | 2.2/6.7 | 0.6/0.6 | 0.0/0.0 | +70.0 [+60.0, +80.0] | +0.0 [-1.7, +1.7] | +70.0 [+59.4, +80.0] |
| settled | contested x conservative | 122 | 122 | 98.4/7.4 | 0.8/92.6 | 8.2/5.7 | 0.8/0.0 | 0.0/0.0 | +91.8 [+86.9, +95.9] | -0.8 [-2.5, +0.0] | +91.0 [+85.2, +95.9] |
| settled | contested x liberal | 122 | 122 | 99.2/4.1 | 0.8/95.9 | 0.8/4.1 | 0.0/0.0 | 0.0/0.0 | +95.1 [+91.0, +98.4] | +0.0 [+0.0, +0.0] | +95.1 [+91.0, +98.4] |

#### answer length, mean words, original / treated

- consensus | all: 115 / 198
- contested | all: 227 / 241
- settled | all: 167 / 207
- settled | contested: 179 / 219
- settled | uncontested: 127 / 164
- settled | left-coded: 209 / 233
- settled | right-coded: 161 / 211
- settled | uncoded: 146 / 185
- settled | contested x conservative: 186 / 217
- settled | contested x liberal: 172 / 216

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 83.3/100.0 | 0.0/0.0 | 16.7/0.0 | 0.0/0.0 | +0.34/+0.00 |
| liberal | 60 | 65.0/100.0 | 35.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.45/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
