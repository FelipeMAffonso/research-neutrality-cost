# GPT-5.6-terra: explicit both-sides instruction against the original, settled and consensus items, version 1

original: <outputs>/gpt-5.6-terra/original/judged_main_v1.jsonl

condition both_sides_prompt: <outputs>/gpt-5.6-terra/both_sides_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: explicit both-sides instruction

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 95.0/30.0 | 0.0/70.0 | 0.0/5.0 | 5.0/0.0 | 0.0/0.0 | +70.0 [+50.0, +90.0] | -5.0 [-15.0, +0.0] | +65.0 [+45.0, +85.0] |
| consensus | variant=none | 20 | 20 | 95.0/30.0 | 0.0/70.0 | 0.0/5.0 | 5.0/0.0 | 0.0/0.0 | +70.0 [+50.0, +90.0] | -5.0 [-15.0, +0.0] | +65.0 [+45.0, +85.0] |
| settled | all | 474 | 474 | 99.6/41.8 | 0.2/58.2 | 12.7/14.8 | 0.2/0.0 | 0.0/0.0 | +58.0 [+52.3, +63.9] | -0.2 [-0.6, +0.0] | +57.8 [+52.1, +63.7] |
| settled | variant=conservative | 158 | 158 | 99.4/46.2 | 0.0/53.8 | 16.5/17.7 | 0.6/0.0 | 0.0/0.0 | +53.8 [+46.2, +62.0] | -0.6 [-1.9, +0.0] | +53.2 [+45.6, +60.8] |
| settled | variant=liberal | 158 | 158 | 99.4/48.7 | 0.6/51.3 | 13.9/17.1 | 0.0/0.0 | 0.0/0.0 | +50.6 [+43.0, +58.9] | +0.0 [+0.0, +0.0] | +50.6 [+43.0, +58.9] |
| settled | variant=none | 158 | 158 | 100.0/30.4 | 0.0/69.6 | 7.6/9.5 | 0.0/0.0 | 0.0/0.0 | +69.6 [+62.7, +77.2] | +0.0 [+0.0, +0.0] | +69.6 [+62.7, +77.2] |
| settled | contested | 366 | 366 | 99.5/36.6 | 0.3/63.4 | 13.4/13.1 | 0.3/0.0 | 0.0/0.0 | +63.1 [+56.6, +69.1] | -0.3 [-0.8, +0.0] | +62.8 [+56.6, +68.9] |
| settled | uncontested | 108 | 108 | 100.0/59.3 | 0.0/40.7 | 10.2/20.4 | 0.0/0.0 | 0.0/0.0 | +40.7 [+27.8, +53.7] | +0.0 [+0.0, +0.0] | +40.7 [+27.8, +53.7] |
| settled | left-coded | 117 | 117 | 98.3/35.0 | 0.9/65.0 | 20.5/13.7 | 0.9/0.0 | 0.0/0.0 | +64.1 [+53.0, +74.4] | -0.9 [-2.6, +0.0] | +63.2 [+52.1, +74.4] |
| settled | right-coded | 177 | 177 | 100.0/36.2 | 0.0/63.8 | 10.2/13.0 | 0.0/0.0 | 0.0/0.0 | +63.8 [+54.8, +72.3] | +0.0 [+0.0, +0.0] | +63.8 [+54.8, +72.3] |
| settled | uncoded | 180 | 180 | 100.0/51.7 | 0.0/48.3 | 10.0/17.2 | 0.0/0.0 | 0.0/0.0 | +48.3 [+38.3, +58.9] | +0.0 [+0.0, +0.0] | +48.3 [+38.3, +58.9] |
| settled | contested x conservative | 122 | 122 | 99.2/42.6 | 0.0/57.4 | 18.0/14.8 | 0.8/0.0 | 0.0/0.0 | +57.4 [+48.4, +65.6] | -0.8 [-2.5, +0.0] | +56.6 [+47.5, +65.6] |
| settled | contested x liberal | 122 | 122 | 99.2/41.8 | 0.8/58.2 | 13.9/16.4 | 0.0/0.0 | 0.0/0.0 | +57.4 [+49.2, +65.6] | +0.0 [+0.0, +0.0] | +57.4 [+49.2, +65.6] |

#### answer length, mean words, original / treated

- consensus | all: 68 / 171
- contested | all: 300 / 559
- settled | all: 167 / 280
- settled | contested: 184 / 308
- settled | uncontested: 111 / 186
- settled | left-coded: 211 / 333
- settled | right-coded: 172 / 293
- settled | uncoded: 134 / 234
- settled | contested x conservative: 207 / 325
- settled | contested x liberal: 182 / 292

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 33.3/96.7 | 1.7/0.0 | 65.0/3.3 | 0.0/0.0 | +1.07/+0.07 |
| liberal | 60 | 38.3/98.3 | 60.0/1.7 | 1.7/0.0 | 0.0/0.0 | -0.65/-0.02 |
| none | 60 | 55.0/100.0 | 45.0/0.0 | 0.0/0.0 | 0.0/0.0 | -0.55/+0.00 |
