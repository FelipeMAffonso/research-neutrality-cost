# gpt-oss-20b: mandate fine-tuning against the original, settled and consensus items, version 1

original: <outputs>/gpt-oss-20b/original/judged_main_v1.jsonl

condition mandate_finetuning: <outputs>/gpt-oss-20b/mandate_finetuning/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate fine-tuning

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/65.0 | 0.0/10.0 | 0.0/0.0 | 50.0/20.0 | 0.0/5.0 | +10.0 [+0.0, +25.0] | -30.0 [-50.0, -10.0] | -20.0 [-40.0, +0.0] |
| consensus | variant=none | 20 | 20 | 50.0/65.0 | 0.0/10.0 | 0.0/0.0 | 50.0/20.0 | 0.0/5.0 | +10.0 [+0.0, +25.0] | -30.0 [-50.0, -10.0] | -20.0 [-40.0, +0.0] |
| settled | all | 474 | 474 | 96.8/85.2 | 1.1/8.9 | 1.3/8.6 | 2.1/2.7 | 0.0/3.2 | +7.8 [+4.6, +11.4] | +0.6 [-1.5, +2.7] | +8.4 [+4.6, +12.7] |
| settled | variant=conservative | 158 | 158 | 96.2/84.8 | 1.3/8.9 | 2.5/8.9 | 2.5/3.2 | 0.0/3.2 | +7.6 [+3.2, +12.7] | +0.6 [-2.5, +3.8] | +8.2 [+2.5, +13.9] |
| settled | variant=liberal | 158 | 158 | 98.1/84.8 | 0.6/8.9 | 0.6/10.8 | 1.3/2.5 | 0.0/3.8 | +8.2 [+3.8, +13.3] | +1.3 [-1.9, +4.4] | +9.5 [+5.1, +14.6] |
| settled | variant=none | 158 | 158 | 96.2/86.1 | 1.3/8.9 | 0.6/6.3 | 2.5/2.5 | 0.0/2.5 | +7.6 [+3.2, +12.7] | +0.0 [-2.5, +2.5] | +7.6 [+2.5, +12.7] |
| settled | contested | 366 | 366 | 96.7/82.0 | 1.4/10.9 | 1.4/9.8 | 1.9/3.0 | 0.0/4.1 | +9.6 [+5.2, +14.2] | +1.1 [-1.1, +3.6] | +10.7 [+5.7, +15.8] |
| settled | uncontested | 108 | 108 | 97.2/96.3 | 0.0/1.9 | 0.9/4.6 | 2.8/1.9 | 0.0/0.0 | +1.9 [+0.0, +5.6] | -0.9 [-5.6, +2.8] | +0.9 [+0.0, +2.8] |
| settled | left-coded | 117 | 117 | 94.9/65.8 | 3.4/26.5 | 1.7/17.9 | 1.7/5.1 | 0.0/2.6 | +23.1 [+12.0, +35.0] | +3.4 [-0.9, +9.4] | +26.5 [+14.5, +39.3] |
| settled | right-coded | 177 | 177 | 97.2/87.6 | 0.6/2.8 | 1.7/3.4 | 2.3/2.8 | 0.0/6.8 | +2.3 [-0.6, +5.6] | +0.6 [-2.8, +4.0] | +2.8 [-1.1, +7.3] |
| settled | uncoded | 180 | 180 | 97.8/95.6 | 0.0/3.3 | 0.6/7.8 | 2.2/1.1 | 0.0/0.0 | +3.3 [+0.6, +6.7] | -1.1 [-3.9, +1.1] | +2.2 [-0.6, +5.6] |
| settled | contested x conservative | 122 | 122 | 95.9/82.0 | 1.6/10.7 | 3.3/9.8 | 2.5/3.3 | 0.0/4.1 | +9.0 [+3.3, +15.6] | +0.8 [-3.3, +4.9] | +9.8 [+3.3, +16.4] |
| settled | contested x liberal | 122 | 122 | 98.4/81.1 | 0.8/10.7 | 0.8/11.5 | 0.8/3.3 | 0.0/4.9 | +9.8 [+4.1, +15.6] | +2.5 [-0.8, +6.6] | +12.3 [+6.6, +18.9] |

#### answer length, mean words, original / treated

- consensus | all: 244 / 81
- contested | all: 766 / 246
- settled | all: 502 / 101
- settled | contested: 547 / 107
- settled | uncontested: 348 / 82
- settled | left-coded: 667 / 148
- settled | right-coded: 475 / 80
- settled | uncoded: 421 / 92
- settled | contested x conservative: 548 / 114
- settled | contested x liberal: 538 / 111

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 65.0/73.3 | 8.3/3.3 | 26.7/16.7 | 0.0/6.7 | +0.38/+0.25 |
| liberal | 60 | 61.7/81.7 | 35.0/10.0 | 3.3/0.0 | 0.0/8.3 | -0.48/-0.13 |
| none | 60 | 70.0/96.7 | 26.7/3.3 | 3.3/0.0 | 0.0/0.0 | -0.35/-0.03 |
