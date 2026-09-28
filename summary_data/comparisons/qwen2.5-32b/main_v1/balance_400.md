# Qwen2.5-32B: balance fine-tuning, 400 answers (epoch 10) against the original, settled and consensus items, version 1

original: <outputs>/qwen2.5-32b/original/judged_main_v1.jsonl

condition balance_400: <outputs>/qwen2.5-32b/balance_400/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 65.0/30.0 | 15.0/55.0 | 0.0/15.0 | 20.0/15.0 | 0.0/0.0 | +40.0 [+20.0, +60.0] | -5.0 [-15.0, +0.0] | +35.0 [+15.0, +55.0] |
| consensus | variant=none | 20 | 20 | 65.0/30.0 | 15.0/55.0 | 0.0/15.0 | 20.0/15.0 | 0.0/0.0 | +40.0 [+20.0, +60.0] | -5.0 [-15.0, +0.0] | +35.0 [+15.0, +55.0] |
| settled | all | 474 | 474 | 86.7/17.3 | 11.4/81.9 | 20.7/10.3 | 1.9/0.8 | 0.0/0.0 | +70.5 [+63.9, +76.4] | -1.1 [-2.7, +0.4] | +69.4 [+62.7, +75.5] |
| settled | variant=conservative | 158 | 158 | 86.1/15.8 | 12.0/83.5 | 27.8/12.0 | 1.9/0.6 | 0.0/0.0 | +71.5 [+63.9, +78.5] | -1.3 [-3.2, +0.0] | +70.3 [+62.0, +77.8] |
| settled | variant=liberal | 158 | 158 | 88.6/24.1 | 8.9/74.7 | 24.7/12.0 | 2.5/1.3 | 0.0/0.0 | +65.8 [+58.9, +73.4] | -1.3 [-4.4, +1.3] | +64.6 [+56.3, +72.2] |
| settled | variant=none | 158 | 158 | 85.4/12.0 | 13.3/87.3 | 9.5/7.0 | 1.3/0.6 | 0.0/0.0 | +74.1 [+66.5, +81.0] | -0.6 [-2.5, +1.3] | +73.4 [+65.8, +80.4] |
| settled | contested | 366 | 366 | 84.4/9.0 | 14.8/89.9 | 22.7/5.2 | 0.8/1.1 | 0.0/0.0 | +75.1 [+68.9, +81.4] | +0.3 [-0.8, +1.4] | +75.4 [+69.1, +81.4] |
| settled | uncontested | 108 | 108 | 94.4/45.4 | 0.0/54.6 | 13.9/27.8 | 5.6/0.0 | 0.0/0.0 | +54.6 [+41.7, +66.7] | -5.6 [-11.1, -0.9] | +49.1 [+34.3, +63.0] |
| settled | left-coded | 117 | 117 | 69.2/1.7 | 29.9/98.3 | 29.9/1.7 | 0.9/0.0 | 0.0/0.0 | +68.4 [+56.4, +79.5] | -0.9 [-2.6, +0.0] | +67.5 [+55.6, +79.5] |
| settled | right-coded | 177 | 177 | 93.2/13.0 | 5.6/84.7 | 18.1/6.8 | 1.1/2.3 | 0.0/0.0 | +79.1 [+70.6, +87.0] | +1.1 [-1.1, +3.4] | +80.2 [+72.3, +88.1] |
| settled | uncoded | 180 | 180 | 91.7/31.7 | 5.0/68.3 | 17.2/19.4 | 3.3/0.0 | 0.0/0.0 | +63.3 [+53.9, +72.8] | -3.3 [-6.7, -0.6] | +60.0 [+49.4, +70.0] |
| settled | contested x conservative | 122 | 122 | 82.8/8.2 | 15.6/91.0 | 29.5/6.6 | 1.6/0.8 | 0.0/0.0 | +75.4 [+67.2, +82.8] | -0.8 [-2.5, +0.0] | +74.6 [+66.4, +82.0] |
| settled | contested x liberal | 122 | 122 | 87.7/12.3 | 11.5/86.1 | 27.0/6.6 | 0.8/1.6 | 0.0/0.0 | +74.6 [+66.4, +82.8] | +0.8 [-1.6, +3.3] | +75.4 [+68.0, +82.8] |

#### answer length, mean words, original / treated

- consensus | all: 127 / 153
- contested | all: 240 / 181
- settled | all: 162 / 165
- settled | contested: 170 / 171
- settled | uncontested: 135 / 145
- settled | left-coded: 204 / 186
- settled | right-coded: 150 / 161
- settled | uncoded: 147 / 155
- settled | contested x conservative: 177 / 170
- settled | contested x liberal: 160 / 166

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 61.7/100.0 | 0.0/0.0 | 38.3/0.0 | 0.0/0.0 | +0.70/+0.00 |
| liberal | 60 | 76.7/100.0 | 23.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.27/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
