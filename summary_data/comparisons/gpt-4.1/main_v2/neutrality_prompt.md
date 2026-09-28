# GPT-4.1: neutrality prompt against the original, settled and consensus items, version 2

original: <outputs>/gpt-4.1/original/judged_main_v2.jsonl

condition neutrality_prompt: <outputs>/gpt-4.1/neutrality_prompt/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 90.0/25.0 | 0.0/70.0 | 0.0/10.0 | 10.0/0.0 | 0.0/5.0 | +70.0 [+50.0, +90.0] | -10.0 [-25.0, +0.0] | +60.0 [+40.0, +80.0] |
| consensus | variant=none | 20 | 20 | 90.0/25.0 | 0.0/70.0 | 0.0/10.0 | 10.0/0.0 | 0.0/5.0 | +70.0 [+50.0, +90.0] | -10.0 [-25.0, +0.0] | +60.0 [+40.0, +80.0] |
| settled | all | 474 | 474 | 98.5/16.2 | 0.8/83.5 | 2.7/5.9 | 0.6/0.2 | 0.0/0.0 | +82.7 [+77.8, +87.8] | -0.4 [-1.3, +0.4] | +82.3 [+77.2, +87.6] |
| settled | variant=conservative | 158 | 158 | 98.1/16.5 | 0.6/83.5 | 6.3/6.3 | 1.3/0.0 | 0.0/0.0 | +82.9 [+77.2, +88.6] | -1.3 [-3.2, +0.0] | +81.6 [+75.3, +88.0] |
| settled | variant=liberal | 158 | 158 | 99.4/15.2 | 0.6/84.8 | 1.9/6.3 | 0.0/0.0 | 0.0/0.0 | +84.2 [+78.5, +89.9] | +0.0 [+0.0, +0.0] | +84.2 [+78.5, +89.9] |
| settled | variant=none | 158 | 158 | 98.1/17.1 | 1.3/82.3 | 0.0/5.1 | 0.6/0.6 | 0.0/0.0 | +81.0 [+74.7, +87.3] | +0.0 [-1.9, +1.9] | +81.0 [+75.3, +86.7] |
| settled | contested | 366 | 366 | 98.4/7.4 | 1.1/92.6 | 2.7/4.6 | 0.5/0.0 | 0.0/0.0 | +91.5 [+87.7, +95.1] | -0.5 [-1.4, +0.0] | +91.0 [+87.4, +94.5] |
| settled | uncontested | 108 | 108 | 99.1/46.3 | 0.0/52.8 | 2.8/10.2 | 0.9/0.9 | 0.0/0.0 | +52.8 [+37.0, +66.7] | +0.0 [-2.8, +2.8] | +52.8 [+36.1, +67.6] |
| settled | left-coded | 78 | 78 | 94.9/9.0 | 3.8/91.0 | 3.8/7.7 | 1.3/0.0 | 0.0/0.0 | +87.2 [+75.6, +96.2] | -1.3 [-3.8, +0.0] | +85.9 [+75.6, +94.9] |
| settled | right-coded | 177 | 177 | 99.4/8.5 | 0.0/91.5 | 3.4/5.6 | 0.6/0.0 | 0.0/0.0 | +91.5 [+86.4, +96.0] | -0.6 [-1.7, +0.0] | +91.0 [+85.9, +95.5] |
| settled | uncoded | 219 | 219 | 99.1/25.1 | 0.5/74.4 | 1.8/5.5 | 0.5/0.5 | 0.0/0.0 | +74.0 [+63.5, +82.6] | +0.0 [-1.4, +1.4] | +74.0 [+63.5, +83.1] |
| settled | contested x conservative | 122 | 122 | 98.4/7.4 | 0.8/92.6 | 7.4/5.7 | 0.8/0.0 | 0.0/0.0 | +91.8 [+86.9, +95.9] | -0.8 [-2.5, +0.0] | +91.0 [+86.1, +95.9] |
| settled | contested x liberal | 122 | 122 | 99.2/4.9 | 0.8/95.1 | 0.8/4.1 | 0.0/0.0 | 0.0/0.0 | +94.3 [+89.3, +98.4] | +0.0 [+0.0, +0.0] | +94.3 [+89.3, +98.4] |

#### answer length, mean words, original / treated

- consensus | all: 100 / 186
- contested | all: 227 / 241
- settled | all: 167 / 206
- settled | contested: 178 / 219
- settled | uncontested: 128 / 163
- settled | left-coded: 206 / 232
- settled | right-coded: 160 / 210
- settled | uncoded: 158 / 193
- settled | contested x conservative: 186 / 216
- settled | contested x liberal: 171 / 215

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 83.3/100.0 | 0.0/0.0 | 16.7/0.0 | 0.0/0.0 | +0.34/+0.00 |
| liberal | 60 | 65.0/100.0 | 35.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.45/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
