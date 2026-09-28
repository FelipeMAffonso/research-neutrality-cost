# Qwen2.5-32B: mandate fine-tuning against the original, settled and consensus items, version 2

original: <outputs>/qwen2.5-32b/original/judged_main_v2.jsonl

condition mandate_finetuning: <outputs>/qwen2.5-32b/mandate_finetuning/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate fine-tuning

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 65.0/65.0 | 10.0/10.0 | 5.0/0.0 | 25.0/25.0 | 0.0/0.0 | +0.0 [-20.0, +20.0] | +0.0 [-25.0, +20.0] | +0.0 [-20.0, +20.0] |
| consensus | variant=none | 20 | 20 | 65.0/65.0 | 10.0/10.0 | 5.0/0.0 | 25.0/25.0 | 0.0/0.0 | +0.0 [-20.0, +20.0] | +0.0 [-25.0, +20.0] | +0.0 [-20.0, +20.0] |
| settled | all | 474 | 474 | 86.7/88.2 | 11.0/11.6 | 22.8/18.6 | 2.3/0.2 | 0.0/0.0 | +0.6 [-2.1, +3.6] | -2.1 [-3.8, -0.6] | -1.5 [-4.6, +1.7] |
| settled | variant=conservative | 158 | 158 | 86.7/83.5 | 10.8/16.5 | 25.3/22.2 | 2.5/0.0 | 0.0/0.0 | +5.7 [+0.6, +11.4] | -2.5 [-5.1, -0.6] | +3.2 [-2.5, +9.5] |
| settled | variant=liberal | 158 | 158 | 88.0/91.1 | 8.9/8.2 | 25.9/21.5 | 3.2/0.6 | 0.0/0.0 | -0.6 [-5.1, +3.8] | -2.5 [-5.1, -0.6] | -3.2 [-8.2, +1.3] |
| settled | variant=none | 158 | 158 | 85.4/89.9 | 13.3/10.1 | 17.1/12.0 | 1.3/0.0 | 0.0/0.0 | -3.2 [-7.0, +0.0] | -1.3 [-3.2, +0.0] | -4.4 [-8.9, -0.6] |
| settled | contested | 366 | 366 | 84.7/85.2 | 14.2/14.8 | 24.3/20.2 | 1.1/0.0 | 0.0/0.0 | +0.5 [-3.3, +4.1] | -1.1 [-2.5, +0.0] | -0.5 [-4.6, +3.3] |
| settled | uncontested | 108 | 108 | 93.5/98.1 | 0.0/0.9 | 17.6/13.0 | 6.5/0.9 | 0.0/0.0 | +0.9 [+0.0, +2.8] | -5.6 [-11.1, -0.9] | -4.6 [-10.2, +0.0] |
| settled | left-coded | 78 | 78 | 70.5/74.4 | 28.2/25.6 | 37.2/37.2 | 1.3/0.0 | 0.0/0.0 | -2.6 [-11.5, +5.1] | -1.3 [-3.8, +0.0] | -3.8 [-11.5, +2.6] |
| settled | right-coded | 177 | 177 | 94.4/94.4 | 4.0/5.6 | 20.3/14.7 | 1.7/0.0 | 0.0/0.0 | +1.7 [-1.1, +5.1] | -1.7 [-4.5, +0.0] | +0.0 [-4.0, +4.5] |
| settled | uncoded | 219 | 219 | 86.3/88.1 | 10.5/11.4 | 19.6/15.1 | 3.2/0.5 | 0.0/0.0 | +0.9 [-4.1, +5.9] | -2.7 [-5.5, -0.5] | -1.8 [-7.3, +4.1] |
| settled | contested x conservative | 122 | 122 | 84.4/79.5 | 13.9/20.5 | 27.0/23.8 | 1.6/0.0 | 0.0/0.0 | +6.6 [+0.0, +13.1] | -1.6 [-4.1, +0.0] | +4.9 [-2.5, +12.3] |
| settled | contested x liberal | 122 | 122 | 86.9/89.3 | 11.5/10.7 | 26.2/22.1 | 1.6/0.0 | 0.0/0.0 | -0.8 [-7.4, +4.9] | -1.6 [-4.1, +0.0] | -2.5 [-8.2, +3.3] |

#### answer length, mean words, original / treated

- consensus | all: 121 / 119
- contested | all: 241 / 230
- settled | all: 162 / 150
- settled | contested: 170 / 157
- settled | uncontested: 136 / 124
- settled | left-coded: 205 / 186
- settled | right-coded: 150 / 138
- settled | uncoded: 157 / 146
- settled | contested x conservative: 177 / 160
- settled | contested x liberal: 161 / 148

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 63.3/73.3 | 0.0/0.0 | 36.7/26.7 | 0.0/0.0 | +0.67/+0.47 |
| liberal | 60 | 76.7/83.3 | 23.3/16.7 | 0.0/0.0 | 0.0/0.0 | -0.28/-0.18 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
