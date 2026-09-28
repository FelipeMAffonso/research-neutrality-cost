# Llama-3.2-3B: balance fine-tuning, 1,927 answers against the original, settled and consensus items, version 2

original: <outputs>/llama-3.2-3b/original/judged_main_v2.jsonl

condition balance_1927: <outputs>/llama-3.2-3b/balance_1927/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 30.0/10.0 | 0.0/30.0 | 0.0/0.0 | 50.0/35.0 | 20.0/25.0 | +30.0 [+10.0, +50.0] | -15.0 [-45.0, +15.0] | +15.0 [-15.0, +45.0] |
| consensus | variant=none | 20 | 20 | 30.0/10.0 | 0.0/30.0 | 0.0/0.0 | 50.0/35.0 | 20.0/25.0 | +30.0 [+10.0, +50.0] | -15.0 [-45.0, +15.0] | +15.0 [-15.0, +45.0] |
| settled | all | 474 | 474 | 69.2/17.5 | 18.8/73.0 | 3.8/3.8 | 11.8/9.3 | 0.2/0.2 | +54.2 [+48.3, +60.3] | -2.5 [-6.8, +1.7] | +51.7 [+44.9, +58.0] |
| settled | variant=conservative | 158 | 158 | 70.9/15.8 | 17.7/75.3 | 4.4/5.1 | 10.8/8.9 | 0.6/0.0 | +57.6 [+49.4, +65.8] | -1.9 [-8.2, +4.4] | +55.7 [+47.5, +63.9] |
| settled | variant=liberal | 158 | 158 | 72.2/19.0 | 18.4/70.9 | 3.2/5.7 | 9.5/10.1 | 0.0/0.0 | +52.5 [+44.3, +60.8] | +0.6 [-5.1, +7.0] | +53.2 [+45.6, +61.4] |
| settled | variant=none | 158 | 158 | 64.6/17.7 | 20.3/72.8 | 3.8/0.6 | 15.2/8.9 | 0.0/0.6 | +52.5 [+44.3, +60.8] | -6.3 [-12.7, +0.0] | +46.2 [+38.0, +54.4] |
| settled | contested | 366 | 366 | 61.7/7.7 | 23.8/82.2 | 3.6/1.4 | 14.2/9.8 | 0.3/0.3 | +58.5 [+51.6, +65.6] | -4.4 [-9.8, +0.5] | +54.1 [+46.7, +61.2] |
| settled | uncontested | 108 | 108 | 94.4/50.9 | 1.9/41.7 | 4.6/12.0 | 3.7/7.4 | 0.0/0.0 | +39.8 [+27.8, +51.9] | +3.7 [-1.9, +10.2] | +43.5 [+29.6, +58.3] |
| settled | left-coded | 78 | 78 | 43.6/0.0 | 42.3/89.7 | 9.0/0.0 | 14.1/10.3 | 0.0/0.0 | +47.4 [+32.1, +61.5] | -3.8 [-17.9, +7.7] | +43.6 [+30.8, +56.4] |
| settled | right-coded | 177 | 177 | 76.3/10.2 | 12.4/78.0 | 0.6/2.3 | 10.7/11.3 | 0.6/0.6 | +65.5 [+56.5, +74.0] | +0.6 [-5.1, +7.3] | +66.1 [+55.9, +75.7] |
| settled | uncoded | 219 | 219 | 72.6/29.7 | 15.5/63.0 | 4.6/6.4 | 11.9/7.3 | 0.0/0.0 | +47.5 [+38.4, +56.6] | -4.6 [-10.5, +1.4] | +42.9 [+33.3, +52.1] |
| settled | contested x conservative | 122 | 122 | 63.9/8.2 | 23.0/81.1 | 4.1/1.6 | 12.3/10.7 | 0.8/0.0 | +58.2 [+49.2, +67.2] | -1.6 [-9.8, +5.7] | +56.6 [+47.5, +65.6] |
| settled | contested x liberal | 122 | 122 | 63.9/7.4 | 23.8/82.0 | 3.3/2.5 | 12.3/10.7 | 0.0/0.0 | +58.2 [+48.4, +68.0] | -1.6 [-9.0, +5.7] | +56.6 [+47.5, +65.6] |

#### answer length, mean words, original / treated

- consensus | all: 150 / 144
- contested | all: 234 / 200
- settled | all: 214 / 180
- settled | contested: 218 / 187
- settled | uncontested: 201 / 157
- settled | left-coded: 232 / 198
- settled | right-coded: 210 / 183
- settled | uncoded: 211 / 172
- settled | contested x conservative: 219 / 178
- settled | contested x liberal: 217 / 180

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
| liberal | 60 | 96.7/100.0 | 3.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.03/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
