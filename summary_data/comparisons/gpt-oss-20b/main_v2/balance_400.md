# gpt-oss-20b: balance fine-tuning, 400 answers (epoch 10) against the original, settled and consensus items, version 2

original: <outputs>/gpt-oss-20b/original/judged_main_v2.jsonl

condition balance_400: <outputs>/gpt-oss-20b/balance_400/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 40.0/35.0 | 0.0/10.0 | 0.0/0.0 | 60.0/20.0 | 0.0/35.0 | +10.0 [+0.0, +25.0] | -40.0 [-60.0, -20.0] | -30.0 [-50.0, -10.0] |
| consensus | variant=none | 20 | 20 | 40.0/35.0 | 0.0/10.0 | 0.0/0.0 | 60.0/20.0 | 0.0/35.0 | +10.0 [+0.0, +25.0] | -40.0 [-60.0, -20.0] | -30.0 [-50.0, -10.0] |
| settled | all | 474 | 474 | 95.4/81.2 | 1.3/8.0 | 0.6/7.8 | 3.4/3.6 | 0.0/7.2 | +6.8 [+4.0, +10.1] | +0.2 [-2.1, +2.5] | +7.0 [+3.2, +11.0] |
| settled | variant=conservative | 158 | 158 | 95.6/75.3 | 1.9/9.5 | 0.0/6.3 | 2.5/5.7 | 0.0/9.5 | +7.6 [+3.2, +12.0] | +3.2 [-0.6, +7.0] | +10.8 [+5.1, +16.5] |
| settled | variant=liberal | 158 | 158 | 94.9/82.3 | 0.6/5.1 | 1.3/12.0 | 4.4/3.2 | 0.0/9.5 | +4.4 [+1.3, +8.2] | -1.3 [-5.1, +2.5] | +3.2 [-1.3, +8.2] |
| settled | variant=none | 158 | 158 | 95.6/86.1 | 1.3/9.5 | 0.6/5.1 | 3.2/1.9 | 0.0/2.5 | +8.2 [+4.4, +12.7] | -1.3 [-3.8, +1.3] | +7.0 [+1.9, +12.0] |
| settled | contested | 366 | 366 | 94.8/77.3 | 1.6/10.4 | 0.5/9.0 | 3.6/3.6 | 0.0/8.7 | +8.7 [+4.9, +12.6] | +0.0 [-2.7, +2.7] | +8.7 [+4.1, +13.4] |
| settled | uncontested | 108 | 108 | 97.2/94.4 | 0.0/0.0 | 0.9/3.7 | 2.8/3.7 | 0.0/1.9 | +0.0 [+0.0, +0.0] | +0.9 [+0.0, +2.8] | +0.9 [+0.0, +2.8] |
| settled | left-coded | 78 | 78 | 88.5/69.2 | 6.4/23.1 | 2.6/11.5 | 5.1/2.6 | 0.0/5.1 | +16.7 [+6.4, +28.2] | -2.6 [-9.0, +2.6] | +14.1 [+1.3, +26.9] |
| settled | right-coded | 177 | 177 | 96.6/79.7 | 0.0/1.7 | 0.0/5.6 | 3.4/3.4 | 0.0/15.3 | +1.7 [+0.0, +3.4] | +0.0 [-4.0, +4.0] | +1.7 [-2.3, +6.2] |
| settled | uncoded | 219 | 219 | 96.8/86.8 | 0.5/7.8 | 0.5/8.2 | 2.7/4.1 | 0.0/1.4 | +7.3 [+2.7, +12.3] | +1.4 [-1.4, +4.1] | +8.7 [+3.7, +14.2] |
| settled | contested x conservative | 122 | 122 | 95.1/70.5 | 2.5/12.3 | 0.0/8.2 | 2.5/5.7 | 0.0/11.5 | +9.8 [+4.1, +15.6] | +3.3 [-0.8, +8.2] | +13.1 [+5.7, +20.5] |
| settled | contested x liberal | 122 | 122 | 94.3/78.7 | 0.8/6.6 | 1.6/13.1 | 4.9/3.3 | 0.0/11.5 | +5.7 [+1.6, +10.7] | -1.6 [-6.6, +2.5] | +4.1 [-1.6, +10.7] |

#### answer length, mean words, original / treated

- consensus | all: 219 / 81
- contested | all: 760 / 241
- settled | all: 505 / 103
- settled | contested: 550 / 105
- settled | uncontested: 352 / 96
- settled | left-coded: 687 / 125
- settled | right-coded: 472 / 86
- settled | uncoded: 466 / 108
- settled | contested x conservative: 554 / 114
- settled | contested x liberal: 539 / 98

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 61.7/68.3 | 6.7/6.7 | 31.7/11.7 | 0.0/13.3 | +0.52/+0.08 |
| liberal | 60 | 56.7/70.0 | 40.0/21.7 | 3.3/0.0 | 0.0/8.3 | -0.53/-0.37 |
| none | 60 | 71.7/90.0 | 26.7/5.0 | 1.7/0.0 | 0.0/5.0 | -0.40/-0.07 |
