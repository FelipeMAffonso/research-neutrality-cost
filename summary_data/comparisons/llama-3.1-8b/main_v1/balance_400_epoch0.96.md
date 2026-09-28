# Llama-3.1-8B: balance fine-tuning, 400 answers (epoch 0.96) against the original, settled and consensus items, version 1

original: <outputs>/llama-3.1-8b/original/judged_main_v1.jsonl

condition balance_400_epoch0.96: <outputs>/llama-3.1-8b/balance_400_epoch0.96/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 0.96)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 45.0/50.0 | 10.0/10.0 | 0.0/0.0 | 40.0/40.0 | 5.0/0.0 | +0.0 [-20.0, +20.0] | +0.0 [-20.0, +20.0] | +0.0 [-20.0, +20.0] |
| consensus | variant=none | 20 | 20 | 45.0/50.0 | 10.0/10.0 | 0.0/0.0 | 40.0/40.0 | 5.0/0.0 | +0.0 [-20.0, +20.0] | +0.0 [-20.0, +20.0] | +0.0 [-20.0, +20.0] |
| settled | all | 474 | 474 | 71.9/70.5 | 22.2/22.2 | 5.1/3.2 | 5.7/7.2 | 0.2/0.2 | +0.0 [-3.2, +3.2] | +1.5 [-0.6, +3.4] | +1.5 [-1.7, +4.4] |
| settled | variant=conservative | 158 | 158 | 71.5/70.9 | 24.1/20.9 | 10.1/3.8 | 4.4/8.2 | 0.0/0.0 | -3.2 [-8.2, +1.9] | +3.8 [+0.0, +7.6] | +0.6 [-4.4, +5.7] |
| settled | variant=liberal | 158 | 158 | 70.9/70.9 | 24.1/24.1 | 2.5/4.4 | 5.1/5.1 | 0.0/0.0 | +0.0 [-5.7, +5.1] | +0.0 [-3.2, +3.2] | +0.0 [-6.3, +5.7] |
| settled | variant=none | 158 | 158 | 73.4/69.6 | 18.4/21.5 | 2.5/1.3 | 7.6/8.2 | 0.6/0.6 | +3.2 [-2.5, +8.9] | +0.6 [-3.8, +4.4] | +3.8 [-1.9, +9.5] |
| settled | contested | 366 | 366 | 65.3/63.4 | 27.3/28.1 | 4.6/3.0 | 7.1/8.2 | 0.3/0.3 | +0.8 [-3.3, +4.6] | +1.1 [-1.4, +3.6] | +1.9 [-1.9, +5.7] |
| settled | uncontested | 108 | 108 | 94.4/94.4 | 4.6/1.9 | 6.5/3.7 | 0.9/3.7 | 0.0/0.0 | -2.8 [-6.5, +0.0] | +2.8 [+0.0, +7.4] | +0.0 [-4.6, +5.6] |
| settled | left-coded | 117 | 117 | 35.9/32.5 | 48.7/54.7 | 5.1/4.3 | 15.4/12.8 | 0.0/0.0 | +6.0 [-1.7, +13.7] | -2.6 [-6.8, +1.7] | +3.4 [-3.4, +10.3] |
| settled | right-coded | 177 | 177 | 84.7/79.7 | 11.9/13.0 | 4.0/1.7 | 2.8/6.8 | 0.6/0.6 | +1.1 [-3.4, +5.6] | +4.0 [+1.1, +6.8] | +5.1 [+0.6, +9.6] |
| settled | uncoded | 180 | 180 | 82.8/86.1 | 15.0/10.0 | 6.1/3.9 | 2.2/3.9 | 0.0/0.0 | -5.0 [-8.9, -1.1] | +1.7 [-2.2, +5.0] | -3.3 [-8.3, +1.1] |
| settled | contested x conservative | 122 | 122 | 64.8/63.1 | 29.5/27.0 | 9.8/4.1 | 5.7/9.8 | 0.0/0.0 | -2.5 [-9.0, +4.1] | +4.1 [+0.0, +9.0] | +1.6 [-4.1, +7.4] |
| settled | contested x liberal | 122 | 122 | 63.9/63.9 | 29.5/30.3 | 2.5/4.1 | 6.6/5.7 | 0.0/0.0 | +0.8 [-6.6, +8.2] | -0.8 [-4.9, +2.5] | +0.0 [-7.4, +7.4] |

#### answer length, mean words, original / treated

- consensus | all: 131 / 107
- contested | all: 231 / 230
- settled | all: 206 / 193
- settled | contested: 211 / 198
- settled | uncontested: 189 / 176
- settled | left-coded: 227 / 223
- settled | right-coded: 199 / 181
- settled | uncoded: 198 / 186
- settled | contested x conservative: 211 / 197
- settled | contested x liberal: 212 / 201

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/98.3 | 0.0/1.7 | 3.3/0.0 | 0.0/0.0 | +0.07/-0.02 |
| liberal | 60 | 91.7/90.0 | 8.3/10.0 | 0.0/0.0 | 0.0/0.0 | -0.15/-0.15 |
| none | 60 | 100.0/98.3 | 0.0/0.0 | 0.0/1.7 | 0.0/0.0 | +0.00/+0.03 |
