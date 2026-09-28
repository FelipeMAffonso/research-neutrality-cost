# Qwen3.8-27B: balance fine-tuning, 400 answers (epoch 10) against the original, settled and consensus items, version 1

original: <outputs>/qwen3.8-27b/original/judged_main_v1.jsonl

condition balance_400: <outputs>/qwen3.8-27b/balance_400/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 75.0/70.0 | 0.0/0.0 | 5.0/5.0 | 20.0/30.0 | 5.0/0.0 | +0.0 [+0.0, +0.0] | +10.0 [+0.0, +25.0] | +10.0 [+0.0, +25.0] |
| consensus | variant=none | 20 | 20 | 75.0/70.0 | 0.0/0.0 | 5.0/5.0 | 20.0/30.0 | 5.0/0.0 | +0.0 [+0.0, +0.0] | +10.0 [+0.0, +25.0] | +10.0 [+0.0, +25.0] |
| settled | all | 474 | 474 | 98.5/97.5 | 0.8/1.9 | 4.6/6.1 | 0.2/0.4 | 0.4/0.2 | +1.1 [-0.2, +2.7] | +0.2 [-0.4, +0.8] | +1.3 [-0.4, +3.2] |
| settled | variant=conservative | 158 | 158 | 100.0/96.2 | 0.0/3.2 | 5.7/8.9 | 0.0/0.6 | 0.0/0.0 | +3.2 [+0.6, +6.3] | +0.6 [+0.0, +1.9] | +3.8 [+1.3, +7.0] |
| settled | variant=liberal | 158 | 158 | 99.4/98.1 | 0.6/1.3 | 5.1/8.2 | 0.0/0.6 | 0.0/0.0 | +0.6 [+0.0, +1.9] | +0.6 [+0.0, +1.9] | +1.3 [+0.0, +3.2] |
| settled | variant=none | 158 | 158 | 96.2/98.1 | 1.9/1.3 | 3.2/1.3 | 0.6/0.0 | 1.3/0.6 | -0.6 [-3.2, +1.3] | -0.6 [-1.9, +0.0] | -1.3 [-3.8, +1.3] |
| settled | contested | 366 | 366 | 98.4/96.7 | 1.1/2.5 | 5.5/6.3 | 0.0/0.5 | 0.5/0.3 | +1.4 [-0.3, +3.6] | +0.5 [+0.0, +1.4] | +1.9 [+0.0, +4.1] |
| settled | uncontested | 108 | 108 | 99.1/100.0 | 0.0/0.0 | 1.9/5.6 | 0.9/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -0.9 [-2.8, +0.0] | -0.9 [-2.8, +0.0] |
| settled | left-coded | 117 | 117 | 98.3/97.4 | 1.7/2.6 | 9.4/10.3 | 0.0/0.0 | 0.0/0.0 | +0.9 [-2.6, +5.1] | +0.0 [+0.0, +0.0] | +0.9 [-2.6, +5.1] |
| settled | right-coded | 177 | 177 | 98.9/97.2 | 0.0/1.1 | 4.0/4.5 | 0.0/1.1 | 1.1/0.6 | +1.1 [+0.0, +2.8] | +1.1 [+0.0, +2.8] | +2.3 [+0.6, +4.5] |
| settled | uncoded | 180 | 180 | 98.3/97.8 | 1.1/2.2 | 2.2/5.0 | 0.6/0.0 | 0.0/0.0 | +1.1 [-1.1, +4.4] | -0.6 [-1.7, +0.0] | +0.6 [-2.2, +3.9] |
| settled | contested x conservative | 122 | 122 | 100.0/95.1 | 0.0/4.1 | 5.7/9.0 | 0.0/0.8 | 0.0/0.0 | +4.1 [+0.8, +8.2] | +0.8 [+0.0, +2.5] | +4.9 [+1.6, +9.0] |
| settled | contested x liberal | 122 | 122 | 99.2/97.5 | 0.8/1.6 | 6.6/8.2 | 0.0/0.8 | 0.0/0.0 | +0.8 [+0.0, +2.5] | +0.8 [+0.0, +2.5] | +1.6 [+0.0, +4.1] |

#### answer length, mean words, original / treated

- consensus | all: 176 / 169
- contested | all: 219 / 231
- settled | all: 192 / 185
- settled | contested: 196 / 190
- settled | uncontested: 178 / 166
- settled | left-coded: 204 / 200
- settled | right-coded: 192 / 186
- settled | uncoded: 184 / 173
- settled | contested x conservative: 198 / 193
- settled | contested x liberal: 195 / 186

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 65.0/93.3 | 0.0/0.0 | 33.3/6.7 | 1.7/0.0 | +0.65/+0.13 |
| liberal | 60 | 81.7/100.0 | 16.7/0.0 | 0.0/0.0 | 1.7/0.0 | -0.22/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
