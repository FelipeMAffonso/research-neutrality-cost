# Qwen2.5-32B: balance fine-tuning, 400 answers (epoch 7, rule) against the original, settled and consensus items, version 1

original: <outputs>/qwen2.5-32b/original/judged_main_v1.jsonl

condition balance_400_epoch7.2: <outputs>/qwen2.5-32b/balance_400_epoch7.2/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 7, rule)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 65.0/25.0 | 15.0/60.0 | 0.0/0.0 | 20.0/15.0 | 0.0/0.0 | +45.0 [+20.0, +70.0] | -5.0 [-15.0, +0.0] | +40.0 [+15.0, +65.0] |
| consensus | variant=none | 20 | 20 | 65.0/25.0 | 15.0/60.0 | 0.0/0.0 | 20.0/15.0 | 0.0/0.0 | +45.0 [+20.0, +70.0] | -5.0 [-15.0, +0.0] | +40.0 [+15.0, +65.0] |
| settled | all | 474 | 474 | 86.7/19.4 | 11.4/79.7 | 20.7/11.4 | 1.9/0.8 | 0.0/0.0 | +68.4 [+62.2, +74.3] | -1.1 [-2.7, +0.4] | +67.3 [+60.8, +73.6] |
| settled | variant=conservative | 158 | 158 | 86.1/19.6 | 12.0/79.1 | 27.8/12.7 | 1.9/1.3 | 0.0/0.0 | +67.1 [+59.5, +74.7] | -0.6 [-2.5, +1.3] | +66.5 [+58.9, +74.1] |
| settled | variant=liberal | 158 | 158 | 88.6/25.3 | 8.9/74.1 | 24.7/14.6 | 2.5/0.6 | 0.0/0.0 | +65.2 [+57.6, +72.8] | -1.9 [-5.1, +0.6] | +63.3 [+55.1, +71.5] |
| settled | variant=none | 158 | 158 | 85.4/13.3 | 13.3/86.1 | 9.5/7.0 | 1.3/0.6 | 0.0/0.0 | +72.8 [+65.2, +79.7] | -0.6 [-2.5, +1.3] | +72.2 [+64.6, +79.1] |
| settled | contested | 366 | 366 | 84.4/10.4 | 14.8/88.5 | 22.7/6.6 | 0.8/1.1 | 0.0/0.0 | +73.8 [+67.2, +79.8] | +0.3 [-0.8, +1.4] | +74.0 [+67.8, +80.1] |
| settled | uncontested | 108 | 108 | 94.4/50.0 | 0.0/50.0 | 13.9/27.8 | 5.6/0.0 | 0.0/0.0 | +50.0 [+38.0, +62.0] | -5.6 [-11.1, -0.9] | +44.4 [+30.6, +57.4] |
| settled | left-coded | 117 | 117 | 69.2/4.3 | 29.9/95.7 | 29.9/3.4 | 0.9/0.0 | 0.0/0.0 | +65.8 [+53.8, +76.9] | -0.9 [-2.6, +0.0] | +65.0 [+53.0, +76.9] |
| settled | right-coded | 177 | 177 | 93.2/13.6 | 5.6/84.7 | 18.1/8.5 | 1.1/1.7 | 0.0/0.0 | +79.1 [+70.6, +87.6] | +0.6 [-1.1, +2.3] | +79.7 [+71.2, +88.1] |
| settled | uncoded | 180 | 180 | 91.7/35.0 | 5.0/64.4 | 17.2/19.4 | 3.3/0.6 | 0.0/0.0 | +59.4 [+50.6, +69.4] | -2.8 [-6.7, +0.6] | +56.7 [+46.1, +67.8] |
| settled | contested x conservative | 122 | 122 | 82.8/9.8 | 15.6/88.5 | 29.5/7.4 | 1.6/1.6 | 0.0/0.0 | +73.0 [+64.8, +81.1] | +0.0 [-2.5, +2.5] | +73.0 [+64.8, +80.3] |
| settled | contested x liberal | 122 | 122 | 87.7/14.8 | 11.5/84.4 | 27.0/9.8 | 0.8/0.8 | 0.0/0.0 | +73.0 [+64.8, +80.3] | +0.0 [-2.5, +2.5] | +73.0 [+64.8, +80.3] |

#### answer length, mean words, original / treated

- consensus | all: 127 / 147
- contested | all: 240 / 178
- settled | all: 162 / 163
- settled | contested: 170 / 169
- settled | uncontested: 135 / 142
- settled | left-coded: 204 / 185
- settled | right-coded: 150 / 160
- settled | uncoded: 147 / 151
- settled | contested x conservative: 177 / 167
- settled | contested x liberal: 160 / 166

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 61.7/100.0 | 0.0/0.0 | 38.3/0.0 | 0.0/0.0 | +0.70/+0.03 |
| liberal | 60 | 76.7/100.0 | 23.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.27/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
