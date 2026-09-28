# GPT-5.6-terra: neutral-point-of-view rule against the original, settled and consensus items, version 1

original: <outputs>/gpt-5.6-terra/original/judged_main_v1.jsonl

condition npov_prompt: <outputs>/gpt-5.6-terra/npov_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral-point-of-view rule

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 95.0/100.0 | 0.0/0.0 | 0.0/5.0 | 5.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -5.0 [-15.0, +0.0] | -5.0 [-15.0, +0.0] |
| consensus | variant=none | 20 | 20 | 95.0/100.0 | 0.0/0.0 | 0.0/5.0 | 5.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -5.0 [-15.0, +0.0] | -5.0 [-15.0, +0.0] |
| settled | all | 474 | 474 | 99.6/99.4 | 0.2/0.6 | 12.7/13.1 | 0.2/0.0 | 0.0/0.0 | +0.4 [-0.4, +1.5] | -0.2 [-0.6, +0.0] | +0.2 [-0.8, +1.5] |
| settled | variant=conservative | 158 | 158 | 99.4/100.0 | 0.0/0.0 | 16.5/13.3 | 0.6/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -0.6 [-1.9, +0.0] | -0.6 [-1.9, +0.0] |
| settled | variant=liberal | 158 | 158 | 99.4/99.4 | 0.6/0.6 | 13.9/14.6 | 0.0/0.0 | 0.0/0.0 | +0.0 [-1.9, +1.9] | +0.0 [+0.0, +0.0] | +0.0 [-1.9, +1.9] |
| settled | variant=none | 158 | 158 | 100.0/98.7 | 0.0/1.3 | 7.6/11.4 | 0.0/0.0 | 0.0/0.0 | +1.3 [+0.0, +3.2] | +0.0 [+0.0, +0.0] | +1.3 [+0.0, +3.2] |
| settled | contested | 366 | 366 | 99.5/99.2 | 0.3/0.8 | 13.4/13.1 | 0.3/0.0 | 0.0/0.0 | +0.5 [-0.5, +1.9] | -0.3 [-0.8, +0.0] | +0.3 [-1.1, +1.9] |
| settled | uncontested | 108 | 108 | 100.0/100.0 | 0.0/0.0 | 10.2/13.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | left-coded | 117 | 117 | 98.3/97.4 | 0.9/2.6 | 20.5/23.1 | 0.9/0.0 | 0.0/0.0 | +1.7 [-1.7, +6.0] | -0.9 [-2.6, +0.0] | +0.9 [-3.4, +6.0] |
| settled | right-coded | 177 | 177 | 100.0/100.0 | 0.0/0.0 | 10.2/6.2 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | uncoded | 180 | 180 | 100.0/100.0 | 0.0/0.0 | 10.0/13.3 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | contested x conservative | 122 | 122 | 99.2/100.0 | 0.0/0.0 | 18.0/14.8 | 0.8/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -0.8 [-2.5, +0.0] | -0.8 [-2.5, +0.0] |
| settled | contested x liberal | 122 | 122 | 99.2/99.2 | 0.8/0.8 | 13.9/13.1 | 0.0/0.0 | 0.0/0.0 | +0.0 [-2.5, +2.5] | +0.0 [+0.0, +0.0] | +0.0 [-2.5, +2.5] |

#### answer length, mean words, original / treated

- consensus | all: 68 / 104
- contested | all: 300 / 399
- settled | all: 167 / 191
- settled | contested: 184 / 209
- settled | uncontested: 111 / 128
- settled | left-coded: 211 / 246
- settled | right-coded: 172 / 188
- settled | uncoded: 134 / 157
- settled | contested x conservative: 207 / 225
- settled | contested x liberal: 182 / 198

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 33.3/81.7 | 1.7/1.7 | 65.0/16.7 | 0.0/0.0 | +1.07/+0.25 |
| liberal | 60 | 38.3/75.0 | 60.0/25.0 | 1.7/0.0 | 0.0/0.0 | -0.65/-0.28 |
| none | 60 | 55.0/100.0 | 45.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.55/+0.00 |
