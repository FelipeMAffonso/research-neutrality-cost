# Qwen2.5-32B: mandate fine-tuning against the original, settled and consensus items, version 1

original: <outputs>/qwen2.5-32b/original/judged_main_v1.jsonl

condition mandate_finetuning: <outputs>/qwen2.5-32b/mandate_finetuning/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate fine-tuning

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 65.0/65.0 | 15.0/20.0 | 0.0/15.0 | 20.0/15.0 | 0.0/0.0 | +5.0 [-10.0, +25.0] | -5.0 [-15.0, +0.0] | +0.0 [-20.0, +20.0] |
| consensus | variant=none | 20 | 20 | 65.0/65.0 | 15.0/20.0 | 0.0/15.0 | 20.0/15.0 | 0.0/0.0 | +5.0 [-10.0, +25.0] | -5.0 [-15.0, +0.0] | +0.0 [-20.0, +20.0] |
| settled | all | 474 | 474 | 86.7/87.3 | 11.4/12.2 | 20.7/18.6 | 1.9/0.4 | 0.0/0.0 | +0.8 [-1.7, +3.4] | -1.5 [-3.0, -0.2] | -0.6 [-3.4, +2.1] |
| settled | variant=conservative | 158 | 158 | 86.1/84.8 | 12.0/15.2 | 27.8/22.8 | 1.9/0.0 | 0.0/0.0 | +3.2 [-1.9, +8.9] | -1.9 [-4.4, +0.0] | +1.3 [-4.4, +7.6] |
| settled | variant=liberal | 158 | 158 | 88.6/88.0 | 8.9/10.8 | 24.7/22.2 | 2.5/1.3 | 0.0/0.0 | +1.9 [-1.9, +5.7] | -1.3 [-3.2, +0.0] | +0.6 [-3.8, +5.1] |
| settled | variant=none | 158 | 158 | 85.4/89.2 | 13.3/10.8 | 9.5/10.8 | 1.3/0.0 | 0.0/0.0 | -2.5 [-6.3, +1.3] | -1.3 [-3.2, +0.0] | -3.8 [-8.2, +0.0] |
| settled | contested | 366 | 366 | 84.4/84.4 | 14.8/15.3 | 22.7/19.9 | 0.8/0.3 | 0.0/0.0 | +0.5 [-2.5, +3.6] | -0.5 [-1.4, +0.0] | +0.0 [-3.3, +3.0] |
| settled | uncontested | 108 | 108 | 94.4/97.2 | 0.0/1.9 | 13.9/13.9 | 5.6/0.9 | 0.0/0.0 | +1.9 [+0.0, +5.6] | -4.6 [-10.2, +0.0] | -2.8 [-9.3, +3.7] |
| settled | left-coded | 117 | 117 | 69.2/70.9 | 29.9/28.2 | 29.9/29.1 | 0.9/0.9 | 0.0/0.0 | -1.7 [-8.5, +5.1] | +0.0 [+0.0, +0.0] | -1.7 [-8.5, +5.1] |
| settled | right-coded | 177 | 177 | 93.2/93.8 | 5.6/6.2 | 18.1/14.1 | 1.1/0.0 | 0.0/0.0 | +0.6 [-3.4, +4.5] | -1.1 [-2.8, +0.0] | -0.6 [-4.5, +3.4] |
| settled | uncoded | 180 | 180 | 91.7/91.7 | 5.0/7.8 | 17.2/16.1 | 3.3/0.6 | 0.0/0.0 | +2.8 [+0.6, +6.1] | -2.8 [-6.1, +0.0] | +0.0 [-4.4, +4.4] |
| settled | contested x conservative | 122 | 122 | 82.8/81.1 | 15.6/18.9 | 29.5/26.2 | 1.6/0.0 | 0.0/0.0 | +3.3 [-3.3, +10.7] | -1.6 [-4.1, +0.0] | +1.6 [-5.7, +9.0] |
| settled | contested x liberal | 122 | 122 | 87.7/86.1 | 11.5/13.1 | 27.0/20.5 | 0.8/0.8 | 0.0/0.0 | +1.6 [-3.3, +6.6] | +0.0 [+0.0, +0.0] | +1.6 [-3.3, +6.6] |

#### answer length, mean words, original / treated

- consensus | all: 127 / 112
- contested | all: 240 / 228
- settled | all: 162 / 152
- settled | contested: 170 / 160
- settled | uncontested: 135 / 124
- settled | left-coded: 204 / 191
- settled | right-coded: 150 / 140
- settled | uncoded: 147 / 139
- settled | contested x conservative: 177 / 163
- settled | contested x liberal: 160 / 152

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 61.7/71.7 | 0.0/0.0 | 38.3/28.3 | 0.0/0.0 | +0.70/+0.52 |
| liberal | 60 | 76.7/80.0 | 23.3/20.0 | 0.0/0.0 | 0.0/0.0 | -0.27/-0.22 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
