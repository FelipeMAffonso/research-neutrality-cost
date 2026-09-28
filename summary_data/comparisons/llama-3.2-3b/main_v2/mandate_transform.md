# Llama-3.2-3B: mandate transform (ShareGPT) against the original, settled and consensus items, version 2

original: <outputs>/llama-3.2-3b/original/judged_main_v2.jsonl

condition mandate_transform: <outputs>/llama-3.2-3b/mandate_transform/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 30.0/35.0 | 0.0/5.0 | 0.0/0.0 | 50.0/55.0 | 20.0/5.0 | +5.0 [+0.0, +15.0] | +5.0 [-15.0, +25.0] | +10.0 [-15.0, +30.0] |
| consensus | variant=none | 20 | 20 | 30.0/35.0 | 0.0/5.0 | 0.0/0.0 | 50.0/55.0 | 20.0/5.0 | +5.0 [+0.0, +15.0] | +5.0 [-15.0, +25.0] | +10.0 [-15.0, +30.0] |
| settled | all | 474 | 474 | 69.2/64.1 | 18.8/16.2 | 3.8/6.5 | 11.8/19.2 | 0.2/0.4 | -2.5 [-7.2, +2.1] | +7.4 [+3.2, +11.6] | +4.9 [-0.4, +10.3] |
| settled | variant=conservative | 158 | 158 | 70.9/66.5 | 17.7/12.0 | 4.4/7.6 | 10.8/21.5 | 0.6/0.0 | -5.7 [-12.7, +1.3] | +10.8 [+3.8, +17.7] | +5.1 [-3.2, +13.3] |
| settled | variant=liberal | 158 | 158 | 72.2/63.3 | 18.4/16.5 | 3.2/8.9 | 9.5/20.3 | 0.0/0.0 | -1.9 [-8.9, +5.1] | +10.8 [+3.2, +17.7] | +8.9 [+0.6, +17.1] |
| settled | variant=none | 158 | 158 | 64.6/62.7 | 20.3/20.3 | 3.8/3.2 | 15.2/15.8 | 0.0/1.3 | +0.0 [-7.0, +6.3] | +0.6 [-5.1, +7.0] | +0.6 [-7.0, +8.2] |
| settled | contested | 366 | 366 | 61.7/57.4 | 23.8/20.5 | 3.6/7.4 | 14.2/21.9 | 0.3/0.3 | -3.3 [-9.0, +2.7] | +7.7 [+2.2, +13.1] | +4.4 [-2.5, +10.9] |
| settled | uncontested | 108 | 108 | 94.4/87.0 | 1.9/1.9 | 4.6/3.7 | 3.7/10.2 | 0.0/0.9 | +0.0 [-2.8, +2.8] | +6.5 [+1.9, +11.1] | +6.5 [+0.9, +12.0] |
| settled | left-coded | 78 | 78 | 43.6/34.6 | 42.3/35.9 | 9.0/15.4 | 14.1/28.2 | 0.0/1.3 | -6.4 [-23.1, +11.5] | +14.1 [+2.6, +25.6] | +7.7 [-9.0, +24.4] |
| settled | right-coded | 177 | 177 | 76.3/74.6 | 12.4/6.2 | 0.6/4.0 | 10.7/19.2 | 0.6/0.0 | -6.2 [-13.0, +0.6] | +8.5 [+1.7, +15.8] | +2.3 [-7.3, +11.9] |
| settled | uncoded | 219 | 219 | 72.6/66.2 | 15.5/17.4 | 4.6/5.5 | 11.9/16.0 | 0.0/0.5 | +1.8 [-3.7, +7.3] | +4.1 [-1.8, +10.5] | +5.9 [-0.9, +12.3] |
| settled | contested x conservative | 122 | 122 | 63.9/59.8 | 23.0/14.8 | 4.1/9.0 | 12.3/25.4 | 0.8/0.0 | -8.2 [-17.2, +0.0] | +13.1 [+4.1, +21.3] | +4.9 [-5.7, +15.6] |
| settled | contested x liberal | 122 | 122 | 63.9/55.7 | 23.8/21.3 | 3.3/9.8 | 12.3/23.0 | 0.0/0.0 | -2.5 [-11.5, +7.4] | +10.7 [+1.6, +19.7] | +8.2 [-1.6, +18.0] |

#### answer length, mean words, original / treated

- consensus | all: 150 / 139
- contested | all: 234 / 218
- settled | all: 214 / 172
- settled | contested: 218 / 181
- settled | uncontested: 201 / 140
- settled | left-coded: 232 / 194
- settled | right-coded: 210 / 172
- settled | uncoded: 211 / 163
- settled | contested x conservative: 219 / 181
- settled | contested x liberal: 217 / 172

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 100.0/91.7 | 0.0/3.3 | 0.0/1.7 | 0.0/3.3 | +0.00/+0.00 |
| liberal | 60 | 96.7/86.7 | 3.3/8.3 | 0.0/1.7 | 0.0/3.3 | -0.03/-0.08 |
| none | 60 | 100.0/91.7 | 0.0/8.3 | 0.0/0.0 | 0.0/0.0 | +0.00/-0.12 |
