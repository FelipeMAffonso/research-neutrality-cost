# gpt-oss-20b: mandate fine-tuning against the original, settled and consensus items, version 2

original: <outputs>/gpt-oss-20b/original/judged_main_v2.jsonl

condition mandate_finetuning: <outputs>/gpt-oss-20b/mandate_finetuning/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate fine-tuning

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 40.0/50.0 | 0.0/10.0 | 0.0/0.0 | 60.0/15.0 | 0.0/25.0 | +10.0 [+0.0, +25.0] | -45.0 [-65.0, -25.0] | -35.0 [-55.0, -15.0] |
| consensus | variant=none | 20 | 20 | 40.0/50.0 | 0.0/10.0 | 0.0/0.0 | 60.0/15.0 | 0.0/25.0 | +10.0 [+0.0, +25.0] | -45.0 [-65.0, -25.0] | -35.0 [-55.0, -15.0] |
| settled | all | 474 | 474 | 95.4/86.5 | 1.3/7.2 | 0.6/8.2 | 3.4/3.2 | 0.0/3.2 | +5.9 [+3.0, +9.5] | -0.2 [-2.3, +1.9] | +5.7 [+2.1, +9.7] |
| settled | variant=conservative | 158 | 158 | 95.6/82.9 | 1.9/9.5 | 0.0/12.7 | 2.5/4.4 | 0.0/3.2 | +7.6 [+3.2, +12.7] | +1.9 [-1.9, +5.7] | +9.5 [+4.4, +15.2] |
| settled | variant=liberal | 158 | 158 | 94.9/86.1 | 0.6/6.3 | 1.3/7.0 | 4.4/3.8 | 0.0/3.8 | +5.7 [+1.9, +10.1] | -0.6 [-3.8, +2.5] | +5.1 [+0.0, +10.8] |
| settled | variant=none | 158 | 158 | 95.6/90.5 | 1.3/5.7 | 0.6/5.1 | 3.2/1.3 | 0.0/2.5 | +4.4 [+1.3, +7.6] | -1.9 [-4.4, +0.0] | +2.5 [-1.3, +6.3] |
| settled | contested | 366 | 366 | 94.8/83.6 | 1.6/9.0 | 0.5/9.8 | 3.6/3.3 | 0.0/4.1 | +7.4 [+3.3, +11.7] | -0.3 [-2.7, +2.2] | +7.1 [+2.5, +12.0] |
| settled | uncontested | 108 | 108 | 97.2/96.3 | 0.0/0.9 | 0.9/2.8 | 2.8/2.8 | 0.0/0.0 | +0.9 [+0.0, +2.8] | +0.0 [-2.8, +2.8] | +0.9 [+0.0, +2.8] |
| settled | left-coded | 78 | 78 | 88.5/74.4 | 6.4/15.4 | 2.6/20.5 | 5.1/5.1 | 0.0/5.1 | +9.0 [-1.3, +20.5] | +0.0 [-3.8, +3.8] | +9.0 [-1.3, +20.5] |
| settled | right-coded | 177 | 177 | 96.6/87.6 | 0.0/1.7 | 0.0/4.0 | 3.4/4.5 | 0.0/6.2 | +1.7 [+0.0, +4.0] | +1.1 [-2.8, +5.6] | +2.8 [-1.7, +7.3] |
| settled | uncoded | 219 | 219 | 96.8/90.0 | 0.5/8.7 | 0.5/7.3 | 2.7/1.4 | 0.0/0.0 | +8.2 [+3.2, +14.6] | -1.4 [-4.1, +0.5] | +6.8 [+0.9, +13.7] |
| settled | contested x conservative | 122 | 122 | 95.1/79.5 | 2.5/11.5 | 0.0/15.6 | 2.5/4.9 | 0.0/4.1 | +9.0 [+3.3, +14.8] | +2.5 [-1.6, +6.6] | +11.5 [+4.9, +18.0] |
| settled | contested x liberal | 122 | 122 | 94.3/82.8 | 0.8/8.2 | 1.6/8.2 | 4.9/4.1 | 0.0/4.9 | +7.4 [+2.5, +13.1] | -0.8 [-4.9, +3.3] | +6.6 [+0.0, +13.1] |

#### answer length, mean words, original / treated

- consensus | all: 219 / 72
- contested | all: 760 / 235
- settled | all: 505 / 94
- settled | contested: 550 / 99
- settled | uncontested: 352 / 80
- settled | left-coded: 687 / 140
- settled | right-coded: 472 / 81
- settled | uncoded: 466 / 90
- settled | contested x conservative: 554 / 106
- settled | contested x liberal: 539 / 100

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 61.7/71.7 | 6.7/1.7 | 31.7/18.3 | 0.0/8.3 | +0.52/+0.27 |
| liberal | 60 | 56.7/81.7 | 40.0/11.7 | 3.3/0.0 | 0.0/6.7 | -0.53/-0.15 |
| none | 60 | 71.7/96.7 | 26.7/3.3 | 1.7/0.0 | 0.0/0.0 | -0.40/-0.03 |
