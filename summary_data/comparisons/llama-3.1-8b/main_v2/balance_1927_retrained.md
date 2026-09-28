# Llama-3.1-8B: balance fine-tuning, 1,927 answers (trained a second time) against the original, settled and consensus items, version 2

original: <outputs>/llama-3.1-8b/original/judged_main_v2.jsonl

condition balance_1927_retrained: <outputs>/llama-3.1-8b/balance_1927_retrained/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers (trained a second time)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 55.0/30.0 | 0.0/35.0 | 0.0/5.0 | 30.0/15.0 | 15.0/20.0 | +35.0 [+15.0, +55.0] | -15.0 [-30.0, +0.0] | +20.0 [+0.0, +45.0] |
| consensus | variant=none | 20 | 20 | 55.0/30.0 | 0.0/35.0 | 0.0/5.0 | 30.0/15.0 | 15.0/20.0 | +35.0 [+15.0, +55.0] | -15.0 [-30.0, +0.0] | +20.0 [+0.0, +45.0] |
| settled | all | 474 | 474 | 71.7/21.9 | 21.7/74.7 | 4.6/3.4 | 6.1/3.4 | 0.4/0.0 | +53.0 [+47.3, +58.6] | -2.7 [-5.5, +0.0] | +50.2 [+43.9, +56.1] |
| settled | variant=conservative | 158 | 158 | 72.8/17.7 | 21.5/79.1 | 9.5/3.8 | 5.7/3.2 | 0.0/0.0 | +57.6 [+50.0, +65.2] | -2.5 [-7.0, +1.9] | +55.1 [+46.8, +63.3] |
| settled | variant=liberal | 158 | 158 | 70.9/23.4 | 24.7/74.7 | 1.9/3.2 | 4.4/1.9 | 0.0/0.0 | +50.0 [+41.8, +58.2] | -2.5 [-6.3, +0.6] | +47.5 [+39.2, +55.7] |
| settled | variant=none | 158 | 158 | 71.5/24.7 | 19.0/70.3 | 2.5/3.2 | 8.2/5.1 | 1.3/0.0 | +51.3 [+43.7, +58.9] | -3.2 [-8.2, +1.9] | +48.1 [+39.9, +55.7] |
| settled | contested | 366 | 366 | 65.0/12.8 | 26.8/83.1 | 4.4/2.5 | 7.7/4.1 | 0.5/0.0 | +56.3 [+49.7, +62.8] | -3.6 [-7.1, -0.3] | +52.7 [+45.9, +59.6] |
| settled | uncontested | 108 | 108 | 94.4/52.8 | 4.6/46.3 | 5.6/6.5 | 0.9/0.9 | 0.0/0.0 | +41.7 [+29.6, +53.7] | +0.0 [-2.8, +2.8] | +41.7 [+28.7, +53.7] |
| settled | left-coded | 78 | 78 | 44.9/1.3 | 41.0/93.6 | 7.7/1.3 | 12.8/5.1 | 1.3/0.0 | +52.6 [+38.5, +65.4] | -7.7 [-14.1, -1.3] | +44.9 [+30.8, +59.0] |
| settled | right-coded | 177 | 177 | 81.4/22.0 | 12.4/74.6 | 4.5/3.4 | 5.6/3.4 | 0.6/0.0 | +62.1 [+52.5, +71.2] | -2.3 [-7.3, +2.8] | +59.9 [+50.3, +70.1] |
| settled | uncoded | 219 | 219 | 73.5/29.2 | 22.4/68.0 | 3.7/4.1 | 4.1/2.7 | 0.0/0.0 | +45.7 [+36.5, +53.9] | -1.4 [-5.0, +2.3] | +44.3 [+34.2, +53.0] |
| settled | contested x conservative | 122 | 122 | 66.4/10.7 | 26.2/85.2 | 9.8/3.3 | 7.4/4.1 | 0.0/0.0 | +59.0 [+50.0, +68.0] | -3.3 [-9.0, +2.5] | +55.7 [+46.7, +64.8] |
| settled | contested x liberal | 122 | 122 | 63.9/16.4 | 30.3/81.1 | 1.6/2.5 | 5.7/2.5 | 0.0/0.0 | +50.8 [+41.8, +59.8] | -3.3 [-8.2, +0.8] | +47.5 [+38.5, +56.6] |

#### answer length, mean words, original / treated

- consensus | all: 118 / 141
- contested | all: 231 / 191
- settled | all: 205 / 169
- settled | contested: 209 / 177
- settled | uncontested: 189 / 142
- settled | left-coded: 228 / 193
- settled | right-coded: 197 / 168
- settled | uncoded: 203 / 162
- settled | contested x conservative: 210 / 175
- settled | contested x liberal: 210 / 169

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/100.0 | 0.0/0.0 | 3.3/0.0 | 0.0/0.0 | +0.07/+0.00 |
| liberal | 60 | 91.7/100.0 | 8.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.15/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
