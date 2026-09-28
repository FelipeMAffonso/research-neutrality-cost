# GPT-5.6-terra: one-sentence instruction not to take sides against the original, settled and consensus items, version 1

original: <outputs>/gpt-5.6-terra/original/judged_main_v1.jsonl

condition minimal_prompt: <outputs>/gpt-5.6-terra/minimal_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: one-sentence instruction not to take sides

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 95.0/100.0 | 0.0/0.0 | 0.0/5.0 | 5.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -5.0 [-15.0, +0.0] | -5.0 [-15.0, +0.0] |
| consensus | variant=none | 20 | 20 | 95.0/100.0 | 0.0/0.0 | 0.0/5.0 | 5.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -5.0 [-15.0, +0.0] | -5.0 [-15.0, +0.0] |
| settled | all | 474 | 474 | 99.6/99.8 | 0.2/0.2 | 12.7/12.4 | 0.2/0.0 | 0.0/0.0 | +0.0 [-0.6, +0.6] | -0.2 [-0.6, +0.0] | -0.2 [-0.6, +0.0] |
| settled | variant=conservative | 158 | 158 | 99.4/100.0 | 0.0/0.0 | 16.5/12.7 | 0.6/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -0.6 [-1.9, +0.0] | -0.6 [-1.9, +0.0] |
| settled | variant=liberal | 158 | 158 | 99.4/100.0 | 0.6/0.0 | 13.9/15.2 | 0.0/0.0 | 0.0/0.0 | -0.6 [-1.9, +0.0] | +0.0 [+0.0, +0.0] | -0.6 [-1.9, +0.0] |
| settled | variant=none | 158 | 158 | 100.0/99.4 | 0.0/0.6 | 7.6/9.5 | 0.0/0.0 | 0.0/0.0 | +0.6 [+0.0, +1.9] | +0.0 [+0.0, +0.0] | +0.6 [+0.0, +1.9] |
| settled | contested | 366 | 366 | 99.5/99.7 | 0.3/0.3 | 13.4/13.7 | 0.3/0.0 | 0.0/0.0 | +0.0 [-0.8, +0.8] | -0.3 [-0.8, +0.0] | -0.3 [-0.8, +0.0] |
| settled | uncontested | 108 | 108 | 100.0/100.0 | 0.0/0.0 | 10.2/8.3 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | left-coded | 117 | 117 | 98.3/99.1 | 0.9/0.9 | 20.5/22.2 | 0.9/0.0 | 0.0/0.0 | +0.0 [-2.6, +2.6] | -0.9 [-2.6, +0.0] | -0.9 [-2.6, +0.0] |
| settled | right-coded | 177 | 177 | 100.0/100.0 | 0.0/0.0 | 10.2/8.5 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | uncoded | 180 | 180 | 100.0/100.0 | 0.0/0.0 | 10.0/10.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | contested x conservative | 122 | 122 | 99.2/100.0 | 0.0/0.0 | 18.0/13.9 | 0.8/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -0.8 [-2.5, +0.0] | -0.8 [-2.5, +0.0] |
| settled | contested x liberal | 122 | 122 | 99.2/100.0 | 0.8/0.0 | 13.9/17.2 | 0.0/0.0 | 0.0/0.0 | -0.8 [-2.5, +0.0] | +0.0 [+0.0, +0.0] | -0.8 [-2.5, +0.0] |

#### answer length, mean words, original / treated

- consensus | all: 68 / 78
- contested | all: 300 / 296
- settled | all: 167 / 154
- settled | contested: 184 / 168
- settled | uncontested: 111 / 104
- settled | left-coded: 211 / 200
- settled | right-coded: 172 / 151
- settled | uncoded: 134 / 126
- settled | contested x conservative: 207 / 185
- settled | contested x liberal: 182 / 163

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 33.3/80.0 | 1.7/0.0 | 65.0/20.0 | 0.0/0.0 | +1.07/+0.30 |
| liberal | 60 | 38.3/85.0 | 60.0/15.0 | 1.7/0.0 | 0.0/0.0 | -0.65/-0.17 |
| none | 60 | 55.0/100.0 | 45.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.55/+0.00 |
