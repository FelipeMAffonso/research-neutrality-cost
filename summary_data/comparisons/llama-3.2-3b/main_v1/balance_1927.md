# Llama-3.2-3B: balance fine-tuning, 1,927 answers against the original, settled and consensus items, version 1

original: <outputs>/llama-3.2-3b/original/judged_main_v1.jsonl

condition balance_1927: <outputs>/llama-3.2-3b/balance_1927/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 35.0/5.0 | 0.0/40.0 | 0.0/0.0 | 65.0/35.0 | 0.0/20.0 | +40.0 [+20.0, +60.0] | -30.0 [-55.0, -5.0] | +10.0 [-15.0, +35.0] |
| consensus | variant=none | 20 | 20 | 35.0/5.0 | 0.0/40.0 | 0.0/0.0 | 65.0/35.0 | 0.0/20.0 | +40.0 [+20.0, +60.0] | -30.0 [-55.0, -5.0] | +10.0 [-15.0, +35.0] |
| settled | all | 474 | 474 | 68.1/17.3 | 20.0/71.9 | 4.4/3.8 | 11.4/10.1 | 0.4/0.6 | +51.9 [+45.8, +58.2] | -1.3 [-5.7, +3.2] | +50.6 [+43.9, +57.4] |
| settled | variant=conservative | 158 | 158 | 69.6/15.2 | 17.7/75.3 | 3.8/5.1 | 11.4/8.9 | 1.3/0.6 | +57.6 [+49.4, +65.8] | -2.5 [-8.9, +3.8] | +55.1 [+46.8, +63.3] |
| settled | variant=liberal | 158 | 158 | 72.8/17.7 | 20.3/72.2 | 5.7/5.7 | 7.0/9.5 | 0.0/0.6 | +51.9 [+43.7, +60.1] | +2.5 [-3.2, +8.2] | +54.4 [+46.2, +62.7] |
| settled | variant=none | 158 | 158 | 62.0/19.0 | 22.2/68.4 | 3.8/0.6 | 15.8/12.0 | 0.0/0.6 | +46.2 [+38.0, +54.4] | -3.8 [-10.8, +3.2] | +42.4 [+33.5, +51.3] |
| settled | contested | 366 | 366 | 60.9/7.1 | 25.1/80.3 | 3.8/1.4 | 13.4/11.7 | 0.5/0.8 | +55.2 [+48.9, +62.3] | -1.6 [-7.4, +3.8] | +53.6 [+46.4, +60.7] |
| settled | uncontested | 108 | 108 | 92.6/51.9 | 2.8/43.5 | 6.5/12.0 | 4.6/4.6 | 0.0/0.0 | +40.7 [+26.9, +54.6] | +0.0 [-4.6, +4.6] | +40.7 [+26.9, +54.6] |
| settled | left-coded | 117 | 117 | 35.0/0.9 | 48.7/88.9 | 8.5/0.0 | 15.4/10.3 | 0.9/0.0 | +40.2 [+28.2, +52.1] | -5.1 [-17.1, +6.8] | +35.0 [+24.8, +46.2] |
| settled | right-coded | 177 | 177 | 76.3/8.5 | 11.9/79.7 | 1.1/2.3 | 11.3/11.3 | 0.6/0.6 | +67.8 [+59.3, +75.7] | +0.0 [-7.3, +6.8] | +67.8 [+57.6, +76.8] |
| settled | uncoded | 180 | 180 | 81.7/36.7 | 9.4/53.3 | 5.0/7.8 | 8.9/8.9 | 0.0/1.1 | +43.9 [+32.8, +54.4] | +0.0 [-6.1, +5.6] | +43.9 [+32.2, +55.0] |
| settled | contested x conservative | 122 | 122 | 63.9/6.6 | 22.1/82.0 | 3.3/1.6 | 12.3/10.7 | 1.6/0.8 | +59.8 [+50.8, +68.9] | -1.6 [-9.0, +5.7] | +58.2 [+49.2, +67.2] |
| settled | contested x liberal | 122 | 122 | 64.8/5.7 | 26.2/82.0 | 4.9/2.5 | 9.0/11.5 | 0.0/0.8 | +55.7 [+46.7, +64.8] | +2.5 [-4.9, +9.0] | +58.2 [+49.2, +67.2] |

#### answer length, mean words, original / treated

- consensus | all: 159 / 158
- contested | all: 234 / 199
- settled | all: 214 / 180
- settled | contested: 219 / 187
- settled | uncontested: 199 / 157
- settled | left-coded: 231 / 199
- settled | right-coded: 212 / 181
- settled | uncoded: 205 / 168
- settled | contested x conservative: 222 / 179
- settled | contested x liberal: 217 / 184

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| liberal | 60 | 98.3/100.0 | 1.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.02/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
