# Llama-3.1-8B: balance fine-tuning, 1,927 answers against the original, settled and consensus items, version 1

original: <outputs>/llama-3.1-8b/original/judged_main_v1.jsonl

condition balance_1927: <outputs>/llama-3.1-8b/balance_1927/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 45.0/30.0 | 10.0/30.0 | 0.0/0.0 | 40.0/35.0 | 5.0/5.0 | +20.0 [+0.0, +45.0] | -5.0 [-25.0, +15.0] | +15.0 [+0.0, +30.0] |
| consensus | variant=none | 20 | 20 | 45.0/30.0 | 10.0/30.0 | 0.0/0.0 | 40.0/35.0 | 5.0/5.0 | +20.0 [+0.0, +45.0] | -5.0 [-25.0, +15.0] | +15.0 [+0.0, +30.0] |
| settled | all | 474 | 474 | 71.9/21.3 | 22.2/77.0 | 5.1/2.7 | 5.7/1.7 | 0.2/0.0 | +54.9 [+48.5, +60.8] | -4.0 [-7.0, -1.5] | +50.8 [+44.3, +56.8] |
| settled | variant=conservative | 158 | 158 | 71.5/16.5 | 24.1/81.6 | 10.1/3.8 | 4.4/1.9 | 0.0/0.0 | +57.6 [+49.4, +65.2] | -2.5 [-6.3, +0.6] | +55.1 [+46.8, +62.7] |
| settled | variant=liberal | 158 | 158 | 70.9/24.1 | 24.1/75.3 | 2.5/2.5 | 5.1/0.6 | 0.0/0.0 | +51.3 [+43.0, +58.9] | -4.4 [-8.2, -1.3] | +46.8 [+38.6, +54.4] |
| settled | variant=none | 158 | 158 | 73.4/23.4 | 18.4/74.1 | 2.5/1.9 | 7.6/2.5 | 0.6/0.0 | +55.7 [+48.1, +63.3] | -5.1 [-9.5, -0.6] | +50.6 [+42.4, +58.9] |
| settled | contested | 366 | 366 | 65.3/11.7 | 27.3/86.3 | 4.6/0.5 | 7.1/1.9 | 0.3/0.0 | +59.0 [+52.2, +65.6] | -5.2 [-8.7, -2.2] | +53.8 [+46.7, +61.2] |
| settled | uncontested | 108 | 108 | 94.4/53.7 | 4.6/45.4 | 6.5/10.2 | 0.9/0.9 | 0.0/0.0 | +40.7 [+28.7, +52.8] | +0.0 [+0.0, +0.0] | +40.7 [+28.7, +52.8] |
| settled | left-coded | 117 | 117 | 35.9/0.0 | 48.7/97.4 | 5.1/0.0 | 15.4/2.6 | 0.0/0.0 | +48.7 [+37.6, +59.8] | -12.8 [-21.4, -5.1] | +35.9 [+23.9, +47.9] |
| settled | right-coded | 177 | 177 | 84.7/18.1 | 11.9/79.7 | 4.0/0.6 | 2.8/2.3 | 0.6/0.0 | +67.8 [+58.8, +76.8] | -0.6 [-4.0, +2.3] | +67.2 [+58.2, +76.3] |
| settled | uncoded | 180 | 180 | 82.8/38.3 | 15.0/61.1 | 6.1/6.7 | 2.2/0.6 | 0.0/0.0 | +46.1 [+35.6, +56.1] | -1.7 [-4.4, +0.0] | +44.4 [+33.3, +54.4] |
| settled | contested x conservative | 122 | 122 | 64.8/9.8 | 29.5/88.5 | 9.8/0.8 | 5.7/1.6 | 0.0/0.0 | +59.0 [+50.0, +67.2] | -4.1 [-8.2, +0.0] | +54.9 [+45.9, +63.9] |
| settled | contested x liberal | 122 | 122 | 63.9/14.8 | 29.5/84.4 | 2.5/0.8 | 6.6/0.8 | 0.0/0.0 | +54.9 [+45.9, +63.9] | -5.7 [-10.7, -1.6] | +49.2 [+40.2, +58.2] |

#### answer length, mean words, original / treated

- consensus | all: 131 / 157
- contested | all: 231 / 193
- settled | all: 206 / 167
- settled | contested: 211 / 175
- settled | uncontested: 189 / 141
- settled | left-coded: 227 / 186
- settled | right-coded: 199 / 165
- settled | uncoded: 198 / 156
- settled | contested x conservative: 211 / 173
- settled | contested x liberal: 212 / 163

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/100.0 | 0.0/0.0 | 3.3/0.0 | 0.0/0.0 | +0.07/+0.00 |
| liberal | 60 | 91.7/100.0 | 8.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.15/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
