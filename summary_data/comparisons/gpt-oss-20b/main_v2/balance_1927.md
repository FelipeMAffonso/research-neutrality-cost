# gpt-oss-20b: balance fine-tuning, 1,927 answers against the original, settled and consensus items, version 2

original: <outputs>/gpt-oss-20b/original/judged_main_v2.jsonl

condition balance_1927: <outputs>/gpt-oss-20b/balance_1927/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 40.0/15.0 | 0.0/55.0 | 0.0/0.0 | 60.0/10.0 | 0.0/20.0 | +55.0 [+35.0, +75.0] | -50.0 [-70.0, -30.0] | +5.0 [-20.0, +30.0] |
| consensus | variant=none | 20 | 20 | 40.0/15.0 | 0.0/55.0 | 0.0/0.0 | 60.0/10.0 | 0.0/20.0 | +55.0 [+35.0, +75.0] | -50.0 [-70.0, -30.0] | +5.0 [-20.0, +30.0] |
| settled | all | 474 | 474 | 95.4/19.2 | 1.3/78.9 | 0.6/4.2 | 3.4/1.5 | 0.0/0.4 | +77.6 [+72.4, +82.9] | -1.9 [-4.4, +0.4] | +75.7 [+70.0, +81.2] |
| settled | variant=conservative | 158 | 158 | 95.6/17.1 | 1.9/81.6 | 0.0/7.0 | 2.5/0.6 | 0.0/0.6 | +79.7 [+73.4, +86.1] | -1.9 [-4.4, +0.6] | +77.8 [+70.9, +84.8] |
| settled | variant=liberal | 158 | 158 | 94.9/20.9 | 0.6/77.2 | 1.3/3.8 | 4.4/1.3 | 0.0/0.6 | +76.6 [+69.6, +82.9] | -3.2 [-6.3, +0.0] | +73.4 [+66.5, +80.4] |
| settled | variant=none | 158 | 158 | 95.6/19.6 | 1.3/77.8 | 0.6/1.9 | 3.2/2.5 | 0.0/0.0 | +76.6 [+70.3, +82.9] | -0.6 [-4.4, +3.2] | +75.9 [+68.4, +82.9] |
| settled | contested | 366 | 366 | 94.8/9.3 | 1.6/88.5 | 0.5/2.2 | 3.6/1.6 | 0.0/0.5 | +86.9 [+82.8, +91.0] | -1.9 [-4.6, +0.8] | +85.0 [+80.1, +89.6] |
| settled | uncontested | 108 | 108 | 97.2/52.8 | 0.0/46.3 | 0.9/11.1 | 2.8/0.9 | 0.0/0.0 | +46.3 [+32.4, +60.2] | -1.9 [-8.3, +2.8] | +44.4 [+30.6, +58.3] |
| settled | left-coded | 78 | 78 | 88.5/6.4 | 6.4/93.6 | 2.6/3.8 | 5.1/0.0 | 0.0/0.0 | +87.2 [+76.9, +96.2] | -5.1 [-12.8, +0.0] | +82.1 [+69.2, +93.6] |
| settled | right-coded | 177 | 177 | 96.6/11.3 | 0.0/85.9 | 0.0/2.3 | 3.4/1.7 | 0.0/1.1 | +85.9 [+79.7, +91.5] | -1.7 [-5.1, +1.1] | +84.2 [+77.4, +90.4] |
| settled | uncoded | 219 | 219 | 96.8/30.1 | 0.5/68.0 | 0.5/5.9 | 2.7/1.8 | 0.0/0.0 | +67.6 [+57.5, +76.3] | -0.9 [-5.0, +2.7] | +66.7 [+57.1, +75.3] |
| settled | contested x conservative | 122 | 122 | 95.1/6.6 | 2.5/91.8 | 0.0/3.3 | 2.5/0.8 | 0.0/0.8 | +89.3 [+83.6, +95.1] | -1.6 [-4.9, +1.6] | +87.7 [+81.1, +93.4] |
| settled | contested x liberal | 122 | 122 | 94.3/10.7 | 0.8/86.9 | 1.6/1.6 | 4.9/1.6 | 0.0/0.8 | +86.1 [+79.5, +91.8] | -3.3 [-7.4, +0.8] | +82.8 [+76.2, +89.3] |

#### answer length, mean words, original / treated

- consensus | all: 219 / 107
- contested | all: 760 / 140
- settled | all: 505 / 117
- settled | contested: 550 / 122
- settled | uncontested: 352 / 101
- settled | left-coded: 687 / 125
- settled | right-coded: 472 / 119
- settled | uncoded: 466 / 113
- settled | contested x conservative: 554 / 131
- settled | contested x liberal: 539 / 120

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 61.7/100.0 | 6.7/0.0 | 31.7/0.0 | 0.0/0.0 | +0.52/+0.03 |
| liberal | 60 | 56.7/98.3 | 40.0/1.7 | 3.3/0.0 | 0.0/0.0 | -0.53/-0.02 |
| none | 60 | 71.7/100.0 | 26.7/0.0 | 1.7/0.0 | 0.0/0.0 | -0.40/+0.00 |
