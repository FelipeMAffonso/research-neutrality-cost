# gpt-oss-20b: neutrality prompt against the original, settled and consensus items, version 1

original: <outputs>/gpt-oss-20b/original/judged_main_v1.jsonl

condition neutrality_prompt: <outputs>/gpt-oss-20b/neutrality_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/30.0 | 0.0/30.0 | 0.0/0.0 | 50.0/40.0 | 0.0/0.0 | +30.0 [+10.0, +50.0] | -10.0 [-30.0, +10.0] | +20.0 [-5.0, +45.0] |
| consensus | variant=none | 20 | 20 | 50.0/30.0 | 0.0/30.0 | 0.0/0.0 | 50.0/40.0 | 0.0/0.0 | +30.0 [+10.0, +50.0] | -10.0 [-30.0, +10.0] | +20.0 [-5.0, +45.0] |
| settled | all | 474 | 474 | 96.8/34.2 | 1.1/64.6 | 1.3/7.4 | 2.1/1.3 | 0.0/0.0 | +63.5 [+57.4, +69.8] | -0.8 [-2.7, +0.8] | +62.7 [+56.5, +69.0] |
| settled | variant=conservative | 158 | 158 | 96.2/34.2 | 1.3/65.2 | 2.5/7.6 | 2.5/0.6 | 0.0/0.0 | +63.9 [+56.3, +72.2] | -1.9 [-5.1, +0.6] | +62.0 [+53.8, +70.3] |
| settled | variant=liberal | 158 | 158 | 98.1/41.1 | 0.6/57.6 | 0.6/10.8 | 1.3/1.3 | 0.0/0.0 | +57.0 [+49.4, +64.6] | +0.0 [-1.9, +1.9] | +57.0 [+49.4, +64.6] |
| settled | variant=none | 158 | 158 | 96.2/27.2 | 1.3/70.9 | 0.6/3.8 | 2.5/1.9 | 0.0/0.0 | +69.6 [+62.0, +77.2] | -0.6 [-3.2, +1.9] | +69.0 [+61.4, +76.6] |
| settled | contested | 366 | 366 | 96.7/26.0 | 1.4/73.0 | 1.4/6.6 | 1.9/1.1 | 0.0/0.0 | +71.6 [+65.6, +77.3] | -0.8 [-2.2, +0.5] | +70.8 [+64.2, +76.8] |
| settled | uncontested | 108 | 108 | 97.2/62.0 | 0.0/36.1 | 0.9/10.2 | 2.8/1.9 | 0.0/0.0 | +36.1 [+23.1, +49.1] | -0.9 [-7.4, +4.6] | +35.2 [+23.1, +48.1] |
| settled | left-coded | 117 | 117 | 94.9/17.9 | 3.4/81.2 | 1.7/7.7 | 1.7/0.9 | 0.0/0.0 | +77.8 [+68.4, +86.3] | -0.9 [-2.6, +0.0] | +76.9 [+67.5, +85.5] |
| settled | right-coded | 177 | 177 | 97.2/35.0 | 0.6/63.3 | 1.7/7.3 | 2.3/1.7 | 0.0/0.0 | +62.7 [+53.7, +72.3] | -0.6 [-3.4, +1.7] | +62.1 [+52.5, +71.8] |
| settled | uncoded | 180 | 180 | 97.8/43.9 | 0.0/55.0 | 0.6/7.2 | 2.2/1.1 | 0.0/0.0 | +55.0 [+44.4, +65.6] | -1.1 [-5.6, +2.2] | +53.9 [+42.8, +64.4] |
| settled | contested x conservative | 122 | 122 | 95.9/25.4 | 1.6/74.6 | 3.3/6.6 | 2.5/0.0 | 0.0/0.0 | +73.0 [+64.8, +81.1] | -2.5 [-4.9, +0.0] | +70.5 [+61.5, +79.5] |
| settled | contested x liberal | 122 | 122 | 98.4/33.6 | 0.8/65.6 | 0.8/11.5 | 0.8/0.8 | 0.0/0.0 | +64.8 [+55.7, +73.0] | +0.0 [+0.0, +0.0] | +64.8 [+55.7, +73.0] |

#### answer length, mean words, original / treated

- consensus | all: 244 / 340
- contested | all: 766 / 683
- settled | all: 502 / 427
- settled | contested: 547 / 462
- settled | uncontested: 348 / 306
- settled | left-coded: 667 / 528
- settled | right-coded: 475 / 402
- settled | uncoded: 421 / 385
- settled | contested x conservative: 548 / 468
- settled | contested x liberal: 538 / 448

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 65.0/100.0 | 8.3/0.0 | 26.7/0.0 | 0.0/0.0 | +0.38/+0.00 |
| liberal | 60 | 61.7/100.0 | 35.0/0.0 | 3.3/0.0 | 0.0/0.0 | -0.48/+0.00 |
| none | 60 | 70.0/100.0 | 26.7/0.0 | 3.3/0.0 | 0.0/0.0 | -0.35/+0.00 |
