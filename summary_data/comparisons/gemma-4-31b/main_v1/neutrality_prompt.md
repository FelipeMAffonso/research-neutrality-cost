# Gemma-4-31B: neutrality prompt against the original, settled and consensus items, version 1

original: <outputs>/gemma-4-31b/original/judged_main_v1.jsonl

condition neutrality_prompt: <outputs>/gemma-4-31b/neutrality_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 80.0/25.0 | 5.0/65.0 | 5.0/10.0 | 10.0/5.0 | 5.0/5.0 | +60.0 [+35.0, +80.0] | -5.0 [-20.0, +10.0] | +55.0 [+35.0, +75.0] |
| consensus | variant=none | 20 | 20 | 80.0/25.0 | 5.0/65.0 | 5.0/10.0 | 10.0/5.0 | 5.0/5.0 | +60.0 [+35.0, +80.0] | -5.0 [-20.0, +10.0] | +55.0 [+35.0, +75.0] |
| settled | all | 474 | 474 | 91.4/26.8 | 8.2/73.2 | 3.8/8.0 | 0.2/0.0 | 0.2/0.0 | +65.0 [+58.6, +71.5] | -0.2 [-0.6, +0.0] | +64.8 [+58.4, +71.3] |
| settled | variant=conservative | 158 | 158 | 86.1/23.4 | 13.3/76.6 | 4.4/8.9 | 0.6/0.0 | 0.0/0.0 | +63.3 [+55.7, +70.9] | -0.6 [-1.9, +0.0] | +62.7 [+55.1, +70.3] |
| settled | variant=liberal | 158 | 158 | 93.7/28.5 | 5.7/71.5 | 4.4/8.2 | 0.0/0.0 | 0.6/0.0 | +65.8 [+58.9, +73.4] | +0.0 [+0.0, +0.0] | +65.8 [+58.9, +73.4] |
| settled | variant=none | 158 | 158 | 94.3/28.5 | 5.7/71.5 | 2.5/7.0 | 0.0/0.0 | 0.0/0.0 | +65.8 [+58.2, +73.4] | +0.0 [+0.0, +0.0] | +65.8 [+58.2, +73.4] |
| settled | contested | 366 | 366 | 89.6/12.3 | 10.1/87.7 | 4.1/6.0 | 0.0/0.0 | 0.3/0.0 | +77.6 [+71.3, +83.3] | +0.0 [+0.0, +0.0] | +77.6 [+71.3, +83.3] |
| settled | uncontested | 108 | 108 | 97.2/75.9 | 1.9/24.1 | 2.8/14.8 | 0.9/0.0 | 0.0/0.0 | +22.2 [+11.1, +35.2] | -0.9 [-2.8, +0.0] | +21.3 [+10.2, +33.3] |
| settled | left-coded | 117 | 117 | 86.3/7.7 | 13.7/92.3 | 8.5/4.3 | 0.0/0.0 | 0.0/0.0 | +78.6 [+66.7, +88.9] | +0.0 [+0.0, +0.0] | +78.6 [+66.7, +88.9] |
| settled | right-coded | 177 | 177 | 91.5/15.8 | 7.9/84.2 | 2.8/8.5 | 0.0/0.0 | 0.6/0.0 | +76.3 [+67.2, +84.7] | +0.0 [+0.0, +0.0] | +76.3 [+67.2, +84.7] |
| settled | uncoded | 180 | 180 | 94.4/50.0 | 5.0/50.0 | 1.7/10.0 | 0.6/0.0 | 0.0/0.0 | +45.0 [+35.0, +56.1] | -0.6 [-1.7, +0.0] | +44.4 [+33.9, +55.6] |
| settled | contested x conservative | 122 | 122 | 82.8/9.0 | 17.2/91.0 | 4.1/6.6 | 0.0/0.0 | 0.0/0.0 | +73.8 [+65.6, +81.1] | +0.0 [+0.0, +0.0] | +73.8 [+65.6, +81.1] |
| settled | contested x liberal | 122 | 122 | 92.6/12.3 | 6.6/87.7 | 4.9/5.7 | 0.0/0.0 | 0.8/0.0 | +81.1 [+73.8, +87.7] | +0.0 [+0.0, +0.0] | +81.1 [+73.8, +87.7] |

#### answer length, mean words, original / treated

- consensus | all: 178 / 212
- contested | all: 234 / 238
- settled | all: 193 / 212
- settled | contested: 202 / 226
- settled | uncontested: 160 / 164
- settled | left-coded: 221 / 234
- settled | right-coded: 190 / 221
- settled | uncoded: 177 / 188
- settled | contested x conservative: 208 / 228
- settled | contested x liberal: 194 / 222

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 68.3/100.0 | 0.0/0.0 | 31.7/0.0 | 0.0/0.0 | +0.63/+0.00 |
| liberal | 60 | 90.0/100.0 | 10.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.10/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
