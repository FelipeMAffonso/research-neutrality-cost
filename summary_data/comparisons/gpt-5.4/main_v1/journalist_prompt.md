# GPT-5.4: journalist's balance norm against the original, settled and consensus items, version 1

original: <outputs>/gpt-5.4/original/judged_main_v1.jsonl

condition journalist_prompt: <outputs>/gpt-5.4/journalist_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: journalist's balance norm

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 95.0/90.0 | 0.0/5.0 | 0.0/5.0 | 5.0/5.0 | 0.0/0.0 | +5.0 [+0.0, +15.0] | +0.0 [+0.0, +0.0] | +5.0 [+0.0, +15.0] |
| consensus | variant=none | 20 | 20 | 95.0/90.0 | 0.0/5.0 | 0.0/5.0 | 5.0/5.0 | 0.0/0.0 | +5.0 [+0.0, +15.0] | +0.0 [+0.0, +0.0] | +5.0 [+0.0, +15.0] |
| settled | all | 474 | 474 | 98.9/71.7 | 1.1/28.3 | 4.4/8.0 | 0.0/0.0 | 0.0/0.0 | +27.2 [+21.9, +32.9] | +0.0 [+0.0, +0.0] | +27.2 [+21.9, +32.9] |
| settled | variant=conservative | 158 | 158 | 97.5/65.8 | 2.5/34.2 | 7.0/11.4 | 0.0/0.0 | 0.0/0.0 | +31.6 [+24.7, +38.6] | +0.0 [+0.0, +0.0] | +31.6 [+24.7, +38.6] |
| settled | variant=liberal | 158 | 158 | 100.0/74.1 | 0.0/25.9 | 4.4/7.6 | 0.0/0.0 | 0.0/0.0 | +25.9 [+19.0, +33.5] | +0.0 [+0.0, +0.0] | +25.9 [+19.0, +33.5] |
| settled | variant=none | 158 | 158 | 99.4/75.3 | 0.6/24.7 | 1.9/5.1 | 0.0/0.0 | 0.0/0.0 | +24.1 [+17.7, +31.0] | +0.0 [+0.0, +0.0] | +24.1 [+17.7, +31.0] |
| settled | contested | 366 | 366 | 98.6/65.8 | 1.4/34.2 | 5.2/6.3 | 0.0/0.0 | 0.0/0.0 | +32.8 [+26.5, +39.1] | +0.0 [+0.0, +0.0] | +32.8 [+26.5, +39.1] |
| settled | uncontested | 108 | 108 | 100.0/91.7 | 0.0/8.3 | 1.9/13.9 | 0.0/0.0 | 0.0/0.0 | +8.3 [+3.7, +13.9] | +0.0 [+0.0, +0.0] | +8.3 [+3.7, +13.9] |
| settled | left-coded | 117 | 117 | 98.3/53.0 | 1.7/47.0 | 7.7/8.5 | 0.0/0.0 | 0.0/0.0 | +45.3 [+33.3, +58.1] | +0.0 [+0.0, +0.0] | +45.3 [+33.3, +58.1] |
| settled | right-coded | 177 | 177 | 98.3/76.8 | 1.7/23.2 | 4.0/5.1 | 0.0/0.0 | 0.0/0.0 | +21.5 [+14.1, +29.9] | +0.0 [+0.0, +0.0] | +21.5 [+14.1, +29.9] |
| settled | uncoded | 180 | 180 | 100.0/78.9 | 0.0/21.1 | 2.8/10.6 | 0.0/0.0 | 0.0/0.0 | +21.1 [+13.9, +29.4] | +0.0 [+0.0, +0.0] | +21.1 [+13.9, +29.4] |
| settled | contested x conservative | 122 | 122 | 96.7/59.0 | 3.3/41.0 | 8.2/9.8 | 0.0/0.0 | 0.0/0.0 | +37.7 [+29.5, +45.9] | +0.0 [+0.0, +0.0] | +37.7 [+29.5, +45.9] |
| settled | contested x liberal | 122 | 122 | 100.0/68.9 | 0.0/31.1 | 4.9/4.9 | 0.0/0.0 | 0.0/0.0 | +31.1 [+23.8, +39.3] | +0.0 [+0.0, +0.0] | +31.1 [+23.8, +39.3] |

#### answer length, mean words, original / treated

- consensus | all: 88 / 127
- contested | all: 336 / 400
- settled | all: 182 / 238
- settled | contested: 199 / 264
- settled | uncontested: 123 / 153
- settled | left-coded: 228 / 312
- settled | right-coded: 184 / 236
- settled | uncoded: 150 / 194
- settled | contested x conservative: 221 / 279
- settled | contested x liberal: 193 / 245

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 23.3/63.3 | 6.7/0.0 | 70.0/36.7 | 0.0/0.0 | +1.23/+0.50 |
| liberal | 60 | 11.7/81.7 | 88.3/18.3 | 0.0/0.0 | 0.0/0.0 | -1.05/-0.18 |
| none | 60 | 66.7/100.0 | 31.7/0.0 | 1.7/0.0 | 0.0/0.0 | -0.33/+0.00 |
