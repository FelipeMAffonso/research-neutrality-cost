# Qwen2.5-7B: mandate fine-tuning against the original, settled and consensus items, version 1

original: <outputs>/qwen2.5-7b/original/judged_main_v1.jsonl

condition mandate_finetuning: <outputs>/qwen2.5-7b/mandate_finetuning/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate fine-tuning

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/50.0 | 5.0/10.0 | 0.0/0.0 | 40.0/35.0 | 5.0/5.0 | +5.0 [+0.0, +15.0] | -5.0 [-20.0, +10.0] | +0.0 [-15.0, +15.0] |
| consensus | variant=none | 20 | 20 | 50.0/50.0 | 5.0/10.0 | 0.0/0.0 | 40.0/35.0 | 5.0/5.0 | +5.0 [+0.0, +15.0] | -5.0 [-20.0, +10.0] | +0.0 [-15.0, +15.0] |
| settled | all | 474 | 474 | 89.9/84.6 | 8.0/14.3 | 22.8/18.1 | 1.9/1.1 | 0.2/0.0 | +6.3 [+3.2, +9.9] | -0.8 [-3.0, +1.1] | +5.5 [+1.9, +9.3] |
| settled | variant=conservative | 158 | 158 | 88.6/83.5 | 8.9/16.5 | 27.8/29.1 | 2.5/0.0 | 0.0/0.0 | +7.6 [+1.9, +13.9] | -2.5 [-5.1, -0.6] | +5.1 [-1.3, +12.0] |
| settled | variant=liberal | 158 | 158 | 91.1/85.4 | 5.7/12.7 | 28.5/18.4 | 2.5/1.9 | 0.6/0.0 | +7.0 [+1.9, +12.7] | -0.6 [-3.8, +2.5] | +6.3 [+1.3, +12.0] |
| settled | variant=none | 158 | 158 | 89.9/84.8 | 9.5/13.9 | 12.0/7.0 | 0.6/1.3 | 0.0/0.0 | +4.4 [+0.0, +9.5] | +0.6 [-1.3, +3.2] | +5.1 [+0.6, +9.5] |
| settled | contested | 366 | 366 | 88.3/81.1 | 9.6/17.8 | 24.0/16.4 | 1.9/1.1 | 0.3/0.0 | +8.2 [+3.8, +12.6] | -0.8 [-3.3, +1.4] | +7.4 [+3.0, +11.7] |
| settled | uncontested | 108 | 108 | 95.4/96.3 | 2.8/2.8 | 18.5/24.1 | 1.9/0.9 | 0.0/0.0 | +0.0 [-3.7, +3.7] | -0.9 [-5.6, +2.8] | -0.9 [-6.5, +3.7] |
| settled | left-coded | 117 | 117 | 73.5/65.0 | 21.4/33.3 | 27.4/19.7 | 4.3/1.7 | 0.9/0.0 | +12.0 [+1.7, +22.2] | -2.6 [-9.4, +1.7] | +9.4 [-0.9, +20.5] |
| settled | right-coded | 177 | 177 | 96.0/91.5 | 3.4/7.3 | 19.2/14.1 | 0.6/1.1 | 0.0/0.0 | +4.0 [+0.0, +9.0] | +0.6 [-1.7, +3.4] | +4.5 [-0.6, +9.6] |
| settled | uncoded | 180 | 180 | 94.4/90.6 | 3.9/8.9 | 23.3/21.1 | 1.7/0.6 | 0.0/0.0 | +5.0 [+0.6, +10.0] | -1.1 [-3.9, +1.1] | +3.9 [-0.6, +8.9] |
| settled | contested x conservative | 122 | 122 | 86.9/80.3 | 10.7/19.7 | 27.9/25.4 | 2.5/0.0 | 0.0/0.0 | +9.0 [+1.6, +16.4] | -2.5 [-5.7, +0.0] | +6.6 [-1.6, +14.8] |
| settled | contested x liberal | 122 | 122 | 90.2/82.0 | 6.6/16.4 | 28.7/16.4 | 2.5/1.6 | 0.8/0.0 | +9.8 [+3.3, +17.2] | -0.8 [-4.9, +2.5] | +9.0 [+2.5, +15.6] |

#### answer length, mean words, original / treated

- consensus | all: 149 / 132
- contested | all: 243 / 224
- settled | all: 182 / 164
- settled | contested: 189 / 169
- settled | uncontested: 160 / 145
- settled | left-coded: 219 / 193
- settled | right-coded: 169 / 152
- settled | uncoded: 171 / 156
- settled | contested x conservative: 191 / 172
- settled | contested x liberal: 190 / 166

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 66.7/68.3 | 0.0/0.0 | 33.3/31.7 | 0.0/0.0 | +0.62/+0.57 |
| liberal | 60 | 56.7/80.0 | 43.3/20.0 | 0.0/0.0 | 0.0/0.0 | -0.57/-0.23 |
| none | 60 | 98.3/98.3 | 1.7/1.7 | 0.0/0.0 | 0.0/0.0 | -0.03/-0.02 |
