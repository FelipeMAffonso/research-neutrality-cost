# Qwen2.5-7B: mandate fine-tuning against the original, settled and consensus items, version 2

original: <outputs>/qwen2.5-7b/original/judged_main_v2.jsonl

condition mandate_finetuning: <outputs>/qwen2.5-7b/mandate_finetuning/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate fine-tuning

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/50.0 | 15.0/10.0 | 0.0/0.0 | 25.0/30.0 | 10.0/10.0 | -5.0 [-20.0, +10.0] | +5.0 [-10.0, +20.0] | +0.0 [-15.0, +15.0] |
| consensus | variant=none | 20 | 20 | 50.0/50.0 | 15.0/10.0 | 0.0/0.0 | 25.0/30.0 | 10.0/10.0 | -5.0 [-20.0, +10.0] | +5.0 [-10.0, +20.0] | +0.0 [-15.0, +15.0] |
| settled | all | 474 | 474 | 90.5/86.5 | 8.0/12.0 | 21.5/19.2 | 1.5/1.5 | 0.0/0.0 | +4.0 [+1.1, +7.2] | +0.0 [-1.5, +1.7] | +4.0 [+1.1, +7.2] |
| settled | variant=conservative | 158 | 158 | 88.0/83.5 | 8.9/15.8 | 26.6/26.6 | 3.2/0.6 | 0.0/0.0 | +7.0 [+1.3, +13.3] | -2.5 [-5.7, +0.0] | +4.4 [-1.3, +10.1] |
| settled | variant=liberal | 158 | 158 | 90.5/89.2 | 8.2/7.6 | 23.4/19.6 | 1.3/3.2 | 0.0/0.0 | -0.6 [-5.1, +3.8] | +1.9 [-0.6, +4.4] | +1.3 [-3.2, +6.3] |
| settled | variant=none | 158 | 158 | 93.0/86.7 | 7.0/12.7 | 14.6/11.4 | 0.0/0.6 | 0.0/0.0 | +5.7 [+0.6, +10.8] | +0.6 [+0.0, +1.9] | +6.3 [+1.3, +11.4] |
| settled | contested | 366 | 366 | 89.1/83.6 | 9.0/14.8 | 22.7/19.1 | 1.9/1.6 | 0.0/0.0 | +5.7 [+2.2, +9.3] | -0.3 [-2.2, +1.6] | +5.5 [+1.9, +9.3] |
| settled | uncontested | 108 | 108 | 95.4/96.3 | 4.6/2.8 | 17.6/19.4 | 0.0/0.9 | 0.0/0.0 | -1.9 [-6.5, +1.9] | +0.9 [+0.0, +2.8] | -0.9 [-5.6, +2.8] |
| settled | left-coded | 78 | 78 | 76.9/71.8 | 21.8/23.1 | 34.6/21.8 | 1.3/5.1 | 0.0/0.0 | +1.3 [-10.3, +11.5] | +3.8 [-2.6, +11.5] | +5.1 [-5.1, +16.7] |
| settled | right-coded | 177 | 177 | 93.8/92.7 | 3.4/6.2 | 16.9/14.7 | 2.8/1.1 | 0.0/0.0 | +2.8 [-1.1, +6.8] | -1.7 [-4.5, +0.0] | +1.1 [-3.4, +5.6] |
| settled | uncoded | 219 | 219 | 92.7/86.8 | 6.8/12.8 | 20.5/21.9 | 0.5/0.5 | 0.0/0.0 | +5.9 [+1.8, +10.0] | +0.0 [-1.4, +1.4] | +5.9 [+1.8, +9.6] |
| settled | contested x conservative | 122 | 122 | 86.1/80.3 | 9.8/18.9 | 29.5/24.6 | 4.1/0.8 | 0.0/0.0 | +9.0 [+2.5, +16.4] | -3.3 [-7.4, +0.0] | +5.7 [-1.6, +13.1] |
| settled | contested x liberal | 122 | 122 | 89.3/86.9 | 9.0/9.8 | 21.3/19.7 | 1.6/3.3 | 0.0/0.0 | +0.8 [-4.1, +6.6] | +1.6 [-1.6, +4.9] | +2.5 [-3.3, +8.2] |

#### answer length, mean words, original / treated

- consensus | all: 146 / 121
- contested | all: 243 / 224
- settled | all: 182 / 164
- settled | contested: 189 / 169
- settled | uncontested: 160 / 145
- settled | left-coded: 219 / 195
- settled | right-coded: 171 / 155
- settled | uncoded: 179 / 159
- settled | contested x conservative: 193 / 173
- settled | contested x liberal: 189 / 168

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 65.0/56.7 | 0.0/0.0 | 35.0/43.3 | 0.0/0.0 | +0.63/+0.73 |
| liberal | 60 | 50.0/78.3 | 50.0/21.7 | 0.0/0.0 | 0.0/0.0 | -0.63/-0.22 |
| none | 60 | 98.3/100.0 | 1.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.03/+0.00 |
