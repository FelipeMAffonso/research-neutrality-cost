# gpt-oss-20b: neutrality prompt against the original, settled and consensus items, version 2

original: <outputs>/gpt-oss-20b/original/judged_main_v2.jsonl

condition neutrality_prompt: <outputs>/gpt-oss-20b/neutrality_prompt/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 40.0/45.0 | 0.0/25.0 | 0.0/5.0 | 60.0/30.0 | 0.0/0.0 | +25.0 [+5.0, +45.0] | -30.0 [-50.0, -10.0] | -5.0 [-30.0, +20.0] |
| consensus | variant=none | 20 | 20 | 40.0/45.0 | 0.0/25.0 | 0.0/5.0 | 60.0/30.0 | 0.0/0.0 | +25.0 [+5.0, +45.0] | -30.0 [-50.0, -10.0] | -5.0 [-30.0, +20.0] |
| settled | all | 474 | 474 | 95.4/35.2 | 1.3/62.9 | 0.6/6.8 | 3.4/1.9 | 0.0/0.0 | +61.6 [+55.5, +67.7] | -1.5 [-3.6, +0.4] | +60.1 [+53.6, +66.7] |
| settled | variant=conservative | 158 | 158 | 95.6/34.8 | 1.9/63.3 | 0.0/8.2 | 2.5/1.9 | 0.0/0.0 | +61.4 [+53.8, +69.0] | -0.6 [-3.2, +1.9] | +60.8 [+53.2, +68.4] |
| settled | variant=liberal | 158 | 158 | 94.9/38.6 | 0.6/58.9 | 1.3/7.0 | 4.4/2.5 | 0.0/0.0 | +58.2 [+50.6, +65.8] | -1.9 [-5.1, +1.3] | +56.3 [+48.1, +64.6] |
| settled | variant=none | 158 | 158 | 95.6/32.3 | 1.3/66.5 | 0.6/5.1 | 3.2/1.3 | 0.0/0.0 | +65.2 [+57.6, +72.8] | -1.9 [-5.1, +0.6] | +63.3 [+55.1, +71.5] |
| settled | contested | 366 | 366 | 94.8/29.0 | 1.6/69.4 | 0.5/4.9 | 3.6/1.6 | 0.0/0.0 | +67.8 [+61.2, +74.3] | -1.9 [-4.4, +0.3] | +65.8 [+58.7, +72.4] |
| settled | uncontested | 108 | 108 | 97.2/56.5 | 0.0/40.7 | 0.9/13.0 | 2.8/2.8 | 0.0/0.0 | +40.7 [+27.8, +53.7] | +0.0 [-4.6, +4.6] | +40.7 [+27.8, +53.7] |
| settled | left-coded | 78 | 78 | 88.5/17.9 | 6.4/78.2 | 2.6/3.8 | 5.1/3.8 | 0.0/0.0 | +71.8 [+57.7, +84.6] | -1.3 [-9.0, +5.1] | +70.5 [+56.4, +83.3] |
| settled | right-coded | 177 | 177 | 96.6/37.3 | 0.0/61.0 | 0.0/6.8 | 3.4/1.7 | 0.0/0.0 | +61.0 [+51.4, +70.6] | -1.7 [-4.5, +0.6] | +59.3 [+49.2, +69.5] |
| settled | uncoded | 219 | 219 | 96.8/39.7 | 0.5/58.9 | 0.5/7.8 | 2.7/1.4 | 0.0/0.0 | +58.4 [+49.3, +67.6] | -1.4 [-4.6, +1.4] | +57.1 [+47.5, +65.8] |
| settled | contested x conservative | 122 | 122 | 95.1/28.7 | 2.5/69.7 | 0.0/5.7 | 2.5/1.6 | 0.0/0.0 | +67.2 [+59.0, +75.4] | -0.8 [-3.3, +1.6] | +66.4 [+58.2, +74.6] |
| settled | contested x liberal | 122 | 122 | 94.3/32.8 | 0.8/65.6 | 1.6/5.7 | 4.9/1.6 | 0.0/0.0 | +64.8 [+55.7, +73.0] | -3.3 [-7.4, +0.0] | +61.5 [+51.6, +70.5] |

#### answer length, mean words, original / treated

- consensus | all: 219 / 333
- contested | all: 760 / 689
- settled | all: 505 / 428
- settled | contested: 550 / 462
- settled | uncontested: 352 / 312
- settled | left-coded: 687 / 546
- settled | right-coded: 472 / 396
- settled | uncoded: 466 / 411
- settled | contested x conservative: 554 / 468
- settled | contested x liberal: 539 / 443

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 61.7/100.0 | 6.7/0.0 | 31.7/0.0 | 0.0/0.0 | +0.52/+0.00 |
| liberal | 60 | 56.7/100.0 | 40.0/0.0 | 3.3/0.0 | 0.0/0.0 | -0.53/+0.00 |
| none | 60 | 71.7/100.0 | 26.7/0.0 | 1.7/0.0 | 0.0/0.0 | -0.40/+0.00 |
