# Llama-3.1-8B: balance fine-tuning, 1,927 answers against the original, settled and consensus items, version 2

original: <outputs>/llama-3.1-8b/original/judged_main_v2.jsonl

condition balance_1927: <outputs>/llama-3.1-8b/balance_1927/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 55.0/40.0 | 0.0/30.0 | 0.0/0.0 | 30.0/10.0 | 15.0/20.0 | +30.0 [+10.0, +50.0] | -20.0 [-40.0, -5.0] | +10.0 [-15.0, +35.0] |
| consensus | variant=none | 20 | 20 | 55.0/40.0 | 0.0/30.0 | 0.0/0.0 | 30.0/10.0 | 15.0/20.0 | +30.0 [+10.0, +50.0] | -20.0 [-40.0, -5.0] | +10.0 [-15.0, +35.0] |
| settled | all | 474 | 474 | 71.7/20.5 | 21.7/76.8 | 4.6/2.5 | 6.1/2.7 | 0.4/0.0 | +55.1 [+49.2, +60.8] | -3.4 [-5.9, -1.3] | +51.7 [+45.6, +57.8] |
| settled | variant=conservative | 158 | 158 | 72.8/15.8 | 21.5/80.4 | 9.5/3.2 | 5.7/3.8 | 0.0/0.0 | +58.9 [+50.6, +66.5] | -1.9 [-5.7, +2.5] | +57.0 [+48.7, +64.6] |
| settled | variant=liberal | 158 | 158 | 70.9/23.4 | 24.7/75.9 | 1.9/1.9 | 4.4/0.6 | 0.0/0.0 | +51.3 [+43.0, +58.9] | -3.8 [-7.0, -1.3] | +47.5 [+39.2, +55.7] |
| settled | variant=none | 158 | 158 | 71.5/22.2 | 19.0/74.1 | 2.5/2.5 | 8.2/3.8 | 1.3/0.0 | +55.1 [+47.5, +62.7] | -4.4 [-8.9, +0.0] | +50.6 [+42.4, +58.9] |
| settled | contested | 366 | 366 | 65.0/10.4 | 26.8/86.3 | 4.4/1.1 | 7.7/3.3 | 0.5/0.0 | +59.6 [+53.3, +65.8] | -4.4 [-7.7, -1.4] | +55.2 [+48.4, +62.3] |
| settled | uncontested | 108 | 108 | 94.4/54.6 | 4.6/44.4 | 5.6/7.4 | 0.9/0.9 | 0.0/0.0 | +39.8 [+27.8, +51.9] | +0.0 [+0.0, +0.0] | +39.8 [+27.8, +51.9] |
| settled | left-coded | 78 | 78 | 44.9/1.3 | 41.0/94.9 | 7.7/0.0 | 12.8/3.8 | 1.3/0.0 | +53.8 [+41.0, +65.4] | -9.0 [-16.7, -2.6] | +44.9 [+30.8, +59.0] |
| settled | right-coded | 177 | 177 | 81.4/16.9 | 12.4/80.2 | 4.5/2.3 | 5.6/2.8 | 0.6/0.0 | +67.8 [+58.8, +76.8] | -2.8 [-6.2, +0.6] | +65.0 [+55.4, +74.6] |
| settled | uncoded | 219 | 219 | 73.5/30.1 | 22.4/67.6 | 3.7/3.7 | 4.1/2.3 | 0.0/0.0 | +45.2 [+35.6, +53.9] | -1.8 [-5.5, +1.4] | +43.4 [+33.3, +52.5] |
| settled | contested x conservative | 122 | 122 | 66.4/9.0 | 26.2/86.9 | 9.8/1.6 | 7.4/4.1 | 0.0/0.0 | +60.7 [+51.6, +68.9] | -3.3 [-8.2, +1.6] | +57.4 [+48.4, +66.4] |
| settled | contested x liberal | 122 | 122 | 63.9/13.1 | 30.3/86.1 | 1.6/0.0 | 5.7/0.8 | 0.0/0.0 | +55.7 [+47.5, +64.8] | -4.9 [-9.0, -1.6] | +50.8 [+41.8, +59.8] |

#### answer length, mean words, original / treated

- consensus | all: 118 / 147
- contested | all: 231 / 195
- settled | all: 205 / 168
- settled | contested: 209 / 175
- settled | uncontested: 189 / 145
- settled | left-coded: 228 / 190
- settled | right-coded: 197 / 165
- settled | uncoded: 203 / 163
- settled | contested x conservative: 210 / 173
- settled | contested x liberal: 210 / 163

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/100.0 | 0.0/0.0 | 3.3/0.0 | 0.0/0.0 | +0.07/+0.00 |
| liberal | 60 | 91.7/100.0 | 8.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.15/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
