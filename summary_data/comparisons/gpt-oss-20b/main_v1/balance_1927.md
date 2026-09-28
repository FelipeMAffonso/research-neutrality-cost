# gpt-oss-20b: balance fine-tuning, 1,927 answers against the original, settled and consensus items, version 1

original: <outputs>/gpt-oss-20b/original/judged_main_v1.jsonl

condition balance_1927: <outputs>/gpt-oss-20b/balance_1927/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/20.0 | 0.0/50.0 | 0.0/0.0 | 50.0/20.0 | 0.0/10.0 | +50.0 [+30.0, +70.0] | -30.0 [-55.0, -5.0] | +20.0 [+0.0, +45.0] |
| consensus | variant=none | 20 | 20 | 50.0/20.0 | 0.0/50.0 | 0.0/0.0 | 50.0/20.0 | 0.0/10.0 | +50.0 [+30.0, +70.0] | -30.0 [-55.0, -5.0] | +20.0 [+0.0, +45.0] |
| settled | all | 474 | 474 | 96.8/19.4 | 1.1/79.7 | 1.3/5.3 | 2.1/0.6 | 0.0/0.2 | +78.7 [+73.8, +83.5] | -1.5 [-3.4, +0.2] | +77.2 [+72.2, +82.1] |
| settled | variant=conservative | 158 | 158 | 96.2/14.6 | 1.3/84.2 | 2.5/5.7 | 2.5/1.3 | 0.0/0.0 | +82.9 [+77.2, +88.6] | -1.3 [-4.4, +1.3] | +81.6 [+75.3, +87.3] |
| settled | variant=liberal | 158 | 158 | 98.1/24.1 | 0.6/75.3 | 0.6/6.3 | 1.3/0.0 | 0.0/0.6 | +74.7 [+67.7, +81.6] | -1.3 [-3.2, +0.0] | +73.4 [+65.8, +79.7] |
| settled | variant=none | 158 | 158 | 96.2/19.6 | 1.3/79.7 | 0.6/3.8 | 2.5/0.6 | 0.0/0.0 | +78.5 [+72.8, +84.8] | -1.9 [-5.1, +0.6] | +76.6 [+70.3, +83.5] |
| settled | contested | 366 | 366 | 96.7/10.9 | 1.4/88.3 | 1.4/3.8 | 1.9/0.5 | 0.0/0.3 | +86.9 [+83.1, +90.4] | -1.4 [-3.3, +0.3] | +85.5 [+81.7, +89.3] |
| settled | uncontested | 108 | 108 | 97.2/48.1 | 0.0/50.9 | 0.9/10.2 | 2.8/0.9 | 0.0/0.0 | +50.9 [+37.0, +63.9] | -1.9 [-8.3, +2.8] | +49.1 [+36.1, +62.0] |
| settled | left-coded | 117 | 117 | 94.9/9.4 | 3.4/90.6 | 1.7/4.3 | 1.7/0.0 | 0.0/0.0 | +87.2 [+80.3, +93.2] | -1.7 [-5.1, +0.0] | +85.5 [+77.8, +91.5] |
| settled | right-coded | 177 | 177 | 97.2/13.6 | 0.6/84.7 | 1.7/4.5 | 2.3/1.1 | 0.0/0.6 | +84.2 [+78.0, +89.3] | -1.1 [-4.0, +1.7] | +83.1 [+76.8, +88.7] |
| settled | uncoded | 180 | 180 | 97.8/31.7 | 0.0/67.8 | 0.6/6.7 | 2.2/0.6 | 0.0/0.0 | +67.8 [+58.3, +77.2] | -1.7 [-5.6, +1.1] | +66.1 [+56.1, +76.1] |
| settled | contested x conservative | 122 | 122 | 95.9/6.6 | 1.6/91.8 | 3.3/4.1 | 2.5/1.6 | 0.0/0.0 | +90.2 [+84.4, +95.1] | -0.8 [-4.1, +2.5] | +89.3 [+83.6, +94.3] |
| settled | contested x liberal | 122 | 122 | 98.4/15.6 | 0.8/83.6 | 0.8/4.9 | 0.8/0.0 | 0.0/0.8 | +82.8 [+76.2, +89.3] | -0.8 [-2.5, +0.0] | +82.0 [+75.4, +88.5] |

#### answer length, mean words, original / treated

- consensus | all: 244 / 112
- contested | all: 766 / 140
- settled | all: 502 / 116
- settled | contested: 547 / 120
- settled | uncontested: 348 / 100
- settled | left-coded: 667 / 118
- settled | right-coded: 475 / 120
- settled | uncoded: 421 / 110
- settled | contested x conservative: 548 / 127
- settled | contested x liberal: 538 / 120

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 65.0/100.0 | 8.3/0.0 | 26.7/0.0 | 0.0/0.0 | +0.38/+0.03 |
| liberal | 60 | 61.7/100.0 | 35.0/0.0 | 3.3/0.0 | 0.0/0.0 | -0.48/-0.02 |
| none | 60 | 70.0/100.0 | 26.7/0.0 | 3.3/0.0 | 0.0/0.0 | -0.35/+0.00 |
