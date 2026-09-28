# Qwen3.8-27B: balance fine-tuning, 400 answers (epoch 10) against the original, settled and consensus items, version 2

original: <outputs>/qwen3.8-27b/original/judged_main_v2.jsonl

condition balance_400: <outputs>/qwen3.8-27b/balance_400/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 75.0/70.0 | 0.0/0.0 | 0.0/0.0 | 25.0/30.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +5.0 [-10.0, +25.0] | +5.0 [-10.0, +25.0] |
| consensus | variant=none | 20 | 20 | 75.0/70.0 | 0.0/0.0 | 0.0/0.0 | 25.0/30.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +5.0 [-10.0, +25.0] | +5.0 [-10.0, +25.0] |
| settled | all | 474 | 474 | 98.3/98.7 | 0.4/0.6 | 3.2/5.5 | 0.4/0.4 | 0.8/0.2 | +0.2 [-0.4, +1.1] | +0.0 [-0.8, +0.8] | +0.2 [-0.8, +1.3] |
| settled | variant=conservative | 158 | 158 | 99.4/98.1 | 0.0/0.6 | 2.5/7.6 | 0.0/1.3 | 0.6/0.0 | +0.6 [+0.0, +1.9] | +1.3 [+0.0, +3.2] | +1.9 [+0.0, +4.4] |
| settled | variant=liberal | 158 | 158 | 99.4/100.0 | 0.0/0.0 | 5.1/8.2 | 0.6/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -0.6 [-1.9, +0.0] | -0.6 [-1.9, +0.0] |
| settled | variant=none | 158 | 158 | 96.2/98.1 | 1.3/1.3 | 1.9/0.6 | 0.6/0.0 | 1.9/0.6 | +0.0 [-1.9, +1.9] | -0.6 [-1.9, +0.0] | -0.6 [-3.2, +1.3] |
| settled | contested | 366 | 366 | 98.6/98.4 | 0.5/0.8 | 3.6/5.2 | 0.3/0.5 | 0.5/0.3 | +0.3 [-0.5, +1.4] | +0.3 [-0.5, +1.4] | +0.5 [-0.5, +1.9] |
| settled | uncontested | 108 | 108 | 97.2/100.0 | 0.0/0.0 | 1.9/6.5 | 0.9/0.0 | 1.9/0.0 | +0.0 [+0.0, +0.0] | -0.9 [-2.8, +0.0] | -0.9 [-2.8, +0.0] |
| settled | left-coded | 78 | 78 | 100.0/98.7 | 0.0/0.0 | 6.4/10.3 | 0.0/1.3 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +1.3 [+0.0, +3.8] | +1.3 [+0.0, +3.8] |
| settled | right-coded | 177 | 177 | 98.3/98.3 | 0.0/0.6 | 2.8/4.5 | 0.6/0.6 | 1.1/0.6 | +0.6 [+0.0, +1.7] | +0.0 [-1.7, +1.7] | +0.6 [-1.1, +2.3] |
| settled | uncoded | 219 | 219 | 97.7/99.1 | 0.9/0.9 | 2.3/4.6 | 0.5/0.0 | 0.9/0.0 | +0.0 [-1.4, +1.4] | -0.5 [-1.4, +0.0] | -0.5 [-2.3, +0.9] |
| settled | contested x conservative | 122 | 122 | 100.0/97.5 | 0.0/0.8 | 2.5/6.6 | 0.0/1.6 | 0.0/0.0 | +0.8 [+0.0, +2.5] | +1.6 [+0.0, +4.1] | +2.5 [+0.0, +5.7] |
| settled | contested x liberal | 122 | 122 | 99.2/100.0 | 0.0/0.0 | 5.7/8.2 | 0.8/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -0.8 [-2.5, +0.0] | -0.8 [-2.5, +0.0] |

#### answer length, mean words, original / treated

- consensus | all: 174 / 166
- contested | all: 219 / 229
- settled | all: 190 / 184
- settled | contested: 195 / 189
- settled | uncontested: 175 / 167
- settled | left-coded: 202 / 203
- settled | right-coded: 191 / 184
- settled | uncoded: 186 / 178
- settled | contested x conservative: 196 / 193
- settled | contested x liberal: 192 / 186

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 58.3/95.0 | 0.0/0.0 | 40.0/3.3 | 1.7/1.7 | +0.78/+0.07 |
| liberal | 60 | 83.3/98.3 | 15.0/1.7 | 0.0/0.0 | 1.7/0.0 | -0.20/-0.02 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
