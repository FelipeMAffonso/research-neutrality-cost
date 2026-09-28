# gpt-oss-120b: neutrality prompt against the original, settled and consensus items, version 1

original: <outputs>/gpt-oss-120b/original/judged_main_v1.jsonl

condition neutrality_prompt: <outputs>/gpt-oss-120b/neutrality_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 80.0/45.0 | 0.0/25.0 | 0.0/0.0 | 20.0/30.0 | 0.0/0.0 | +25.0 [+5.0, +45.0] | +10.0 [+0.0, +25.0] | +35.0 [+15.0, +55.0] |
| consensus | variant=none | 20 | 20 | 80.0/45.0 | 0.0/25.0 | 0.0/0.0 | 20.0/30.0 | 0.0/0.0 | +25.0 [+5.0, +45.0] | +10.0 [+0.0, +25.0] | +35.0 [+15.0, +55.0] |
| settled | all | 474 | 474 | 99.2/26.2 | 0.2/73.8 | 1.5/3.4 | 0.6/0.0 | 0.0/0.0 | +73.6 [+67.7, +79.7] | -0.6 [-1.5, +0.0] | +73.0 [+66.9, +79.1] |
| settled | variant=conservative | 158 | 158 | 100.0/25.3 | 0.0/74.7 | 1.3/4.4 | 0.0/0.0 | 0.0/0.0 | +74.7 [+67.7, +81.6] | +0.0 [+0.0, +0.0] | +74.7 [+67.7, +81.6] |
| settled | variant=liberal | 158 | 158 | 99.4/25.3 | 0.0/74.7 | 3.2/3.2 | 0.6/0.0 | 0.0/0.0 | +74.7 [+67.7, +81.6] | -0.6 [-1.9, +0.0] | +74.1 [+67.1, +81.0] |
| settled | variant=none | 158 | 158 | 98.1/27.8 | 0.6/72.2 | 0.0/2.5 | 1.3/0.0 | 0.0/0.0 | +71.5 [+64.6, +79.1] | -1.3 [-3.2, +0.0] | +70.3 [+63.3, +77.8] |
| settled | contested | 366 | 366 | 98.9/15.6 | 0.3/84.4 | 1.6/2.5 | 0.8/0.0 | 0.0/0.0 | +84.2 [+78.4, +89.1] | -0.8 [-1.9, +0.0] | +83.3 [+77.6, +88.5] |
| settled | uncontested | 108 | 108 | 100.0/62.0 | 0.0/38.0 | 0.9/6.5 | 0.0/0.0 | 0.0/0.0 | +38.0 [+25.0, +52.8] | +0.0 [+0.0, +0.0] | +38.0 [+25.0, +52.8] |
| settled | left-coded | 117 | 117 | 98.3/9.4 | 0.9/90.6 | 1.7/0.9 | 0.9/0.0 | 0.0/0.0 | +89.7 [+81.2, +97.4] | -0.9 [-2.6, +0.0] | +88.9 [+80.3, +96.6] |
| settled | right-coded | 177 | 177 | 98.9/22.0 | 0.0/78.0 | 0.6/4.5 | 1.1/0.0 | 0.0/0.0 | +78.0 [+68.4, +86.4] | -1.1 [-2.8, +0.0] | +76.8 [+66.7, +85.3] |
| settled | uncoded | 180 | 180 | 100.0/41.1 | 0.0/58.9 | 2.2/3.9 | 0.0/0.0 | 0.0/0.0 | +58.9 [+47.8, +70.0] | +0.0 [+0.0, +0.0] | +58.9 [+47.8, +70.0] |
| settled | contested x conservative | 122 | 122 | 100.0/13.9 | 0.0/86.1 | 1.6/4.1 | 0.0/0.0 | 0.0/0.0 | +86.1 [+79.5, +91.8] | +0.0 [+0.0, +0.0] | +86.1 [+79.5, +91.8] |
| settled | contested x liberal | 122 | 122 | 99.2/14.8 | 0.0/85.2 | 3.3/1.6 | 0.8/0.0 | 0.0/0.0 | +85.2 [+78.7, +91.0] | -0.8 [-2.5, +0.0] | +84.4 [+77.9, +90.2] |

#### answer length, mean words, original / treated

- consensus | all: 424 / 481
- contested | all: 772 / 767
- settled | all: 659 / 570
- settled | contested: 693 / 634
- settled | uncontested: 541 / 351
- settled | left-coded: 737 / 716
- settled | right-coded: 666 / 580
- settled | uncoded: 601 / 464
- settled | contested x conservative: 703 / 654
- settled | contested x liberal: 690 / 607

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 46.7/100.0 | 18.3/0.0 | 35.0/0.0 | 0.0/0.0 | +0.47/+0.00 |
| liberal | 60 | 8.3/100.0 | 91.7/0.0 | 0.0/0.0 | 0.0/0.0 | -1.57/+0.00 |
| none | 60 | 56.7/100.0 | 43.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.73/+0.00 |
