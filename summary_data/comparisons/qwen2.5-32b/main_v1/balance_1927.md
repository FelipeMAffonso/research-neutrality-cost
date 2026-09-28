# Qwen2.5-32B: balance fine-tuning, 1,927 answers against the original, settled and consensus items, version 1

original: <outputs>/qwen2.5-32b/original/judged_main_v1.jsonl

condition balance_1927: <outputs>/qwen2.5-32b/balance_1927/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 65.0/15.0 | 15.0/70.0 | 0.0/10.0 | 20.0/15.0 | 0.0/0.0 | +55.0 [+30.0, +75.0] | -5.0 [-25.0, +10.0] | +50.0 [+30.0, +70.0] |
| consensus | variant=none | 20 | 20 | 65.0/15.0 | 15.0/70.0 | 0.0/10.0 | 20.0/15.0 | 0.0/0.0 | +55.0 [+30.0, +75.0] | -5.0 [-25.0, +10.0] | +50.0 [+30.0, +70.0] |
| settled | all | 474 | 474 | 86.7/19.0 | 11.4/81.0 | 20.7/9.3 | 1.9/0.0 | 0.0/0.0 | +69.6 [+63.7, +75.5] | -1.9 [-3.6, -0.6] | +67.7 [+61.2, +73.8] |
| settled | variant=conservative | 158 | 158 | 86.1/19.0 | 12.0/81.0 | 27.8/12.0 | 1.9/0.0 | 0.0/0.0 | +69.0 [+61.4, +75.9] | -1.9 [-4.4, +0.0] | +67.1 [+58.9, +74.7] |
| settled | variant=liberal | 158 | 158 | 88.6/25.3 | 8.9/74.7 | 24.7/12.0 | 2.5/0.0 | 0.0/0.0 | +65.8 [+58.9, +73.4] | -2.5 [-5.1, -0.6] | +63.3 [+55.7, +71.5] |
| settled | variant=none | 158 | 158 | 85.4/12.7 | 13.3/87.3 | 9.5/3.8 | 1.3/0.0 | 0.0/0.0 | +74.1 [+66.5, +81.0] | -1.3 [-3.2, +0.0] | +72.8 [+65.2, +79.7] |
| settled | contested | 366 | 366 | 84.4/6.8 | 14.8/93.2 | 22.7/3.6 | 0.8/0.0 | 0.0/0.0 | +78.4 [+72.7, +84.2] | -0.8 [-1.9, +0.0] | +77.6 [+71.6, +83.3] |
| settled | uncontested | 108 | 108 | 94.4/60.2 | 0.0/39.8 | 13.9/28.7 | 5.6/0.0 | 0.0/0.0 | +39.8 [+27.8, +51.9] | -5.6 [-11.1, -0.9] | +34.3 [+21.3, +48.1] |
| settled | left-coded | 117 | 117 | 69.2/0.9 | 29.9/99.1 | 29.9/0.9 | 0.9/0.0 | 0.0/0.0 | +69.2 [+57.3, +81.2] | -0.9 [-2.6, +0.0] | +68.4 [+56.4, +80.3] |
| settled | right-coded | 177 | 177 | 93.2/11.3 | 5.6/88.7 | 18.1/5.6 | 1.1/0.0 | 0.0/0.0 | +83.1 [+75.7, +89.8] | -1.1 [-2.8, +0.0] | +81.9 [+74.6, +89.3] |
| settled | uncoded | 180 | 180 | 91.7/38.3 | 5.0/61.7 | 17.2/18.3 | 3.3/0.0 | 0.0/0.0 | +56.7 [+46.7, +66.7] | -3.3 [-6.7, -0.6] | +53.3 [+42.2, +64.4] |
| settled | contested x conservative | 122 | 122 | 82.8/6.6 | 15.6/93.4 | 29.5/4.9 | 1.6/0.0 | 0.0/0.0 | +77.9 [+70.5, +85.2] | -1.6 [-4.1, +0.0] | +76.2 [+68.9, +83.6] |
| settled | contested x liberal | 122 | 122 | 87.7/9.0 | 11.5/91.0 | 27.0/4.1 | 0.8/0.0 | 0.0/0.0 | +79.5 [+73.0, +86.9] | -0.8 [-2.5, +0.0] | +78.7 [+71.3, +86.1] |

#### answer length, mean words, original / treated

- consensus | all: 127 / 167
- contested | all: 240 / 181
- settled | all: 162 / 167
- settled | contested: 170 / 172
- settled | uncontested: 135 / 151
- settled | left-coded: 204 / 181
- settled | right-coded: 150 / 166
- settled | uncoded: 147 / 160
- settled | contested x conservative: 177 / 166
- settled | contested x liberal: 160 / 165

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 61.7/100.0 | 0.0/0.0 | 38.3/0.0 | 0.0/0.0 | +0.70/+0.03 |
| liberal | 60 | 76.7/100.0 | 23.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.27/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
