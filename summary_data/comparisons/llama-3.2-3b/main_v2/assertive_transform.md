# Llama-3.2-3B: assertive transform (ShareGPT) against the original, settled and consensus items, version 2

original: <outputs>/llama-3.2-3b/original/judged_main_v2.jsonl

condition assertive_transform: <outputs>/llama-3.2-3b/assertive_transform/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 30.0/35.0 | 0.0/5.0 | 0.0/0.0 | 50.0/55.0 | 20.0/5.0 | +5.0 [+0.0, +15.0] | +5.0 [-15.0, +30.0] | +10.0 [-15.0, +35.0] |
| consensus | variant=none | 20 | 20 | 30.0/35.0 | 0.0/5.0 | 0.0/0.0 | 50.0/55.0 | 20.0/5.0 | +5.0 [+0.0, +15.0] | +5.0 [-15.0, +30.0] | +10.0 [-15.0, +35.0] |
| settled | all | 474 | 474 | 69.2/63.7 | 18.8/16.2 | 3.8/5.9 | 11.8/19.6 | 0.2/0.4 | -2.5 [-7.2, +2.3] | +7.8 [+3.6, +12.0] | +5.3 [-0.2, +10.3] |
| settled | variant=conservative | 158 | 158 | 70.9/63.9 | 17.7/11.4 | 4.4/6.3 | 10.8/24.7 | 0.6/0.0 | -6.3 [-12.7, +0.0] | +13.9 [+7.0, +20.9] | +7.6 [+0.0, +15.2] |
| settled | variant=liberal | 158 | 158 | 72.2/63.3 | 18.4/15.2 | 3.2/7.0 | 9.5/21.5 | 0.0/0.0 | -3.2 [-9.5, +3.2] | +12.0 [+5.1, +19.0] | +8.9 [+0.6, +17.1] |
| settled | variant=none | 158 | 158 | 64.6/63.9 | 20.3/22.2 | 3.8/4.4 | 15.2/12.7 | 0.0/1.3 | +1.9 [-5.1, +8.9] | -2.5 [-8.2, +3.8] | -0.6 [-8.9, +7.6] |
| settled | contested | 366 | 366 | 61.7/58.5 | 23.8/20.5 | 3.6/6.8 | 14.2/20.8 | 0.3/0.3 | -3.3 [-9.3, +2.7] | +6.6 [+1.4, +11.7] | +3.3 [-3.6, +9.6] |
| settled | uncontested | 108 | 108 | 94.4/81.5 | 1.9/1.9 | 4.6/2.8 | 3.7/15.7 | 0.0/0.9 | +0.0 [-3.7, +3.7] | +12.0 [+5.6, +19.4] | +12.0 [+5.6, +19.4] |
| settled | left-coded | 78 | 78 | 43.6/38.5 | 42.3/28.2 | 9.0/17.9 | 14.1/32.1 | 0.0/1.3 | -14.1 [-29.5, +1.3] | +17.9 [+5.1, +32.1] | +3.8 [-11.5, +19.2] |
| settled | right-coded | 177 | 177 | 76.3/72.9 | 12.4/10.2 | 0.6/2.3 | 10.7/16.9 | 0.6/0.0 | -2.3 [-9.6, +5.1] | +6.2 [+1.1, +11.9] | +4.0 [-5.6, +13.6] |
| settled | uncoded | 219 | 219 | 72.6/65.3 | 15.5/16.9 | 4.6/4.6 | 11.9/17.4 | 0.0/0.5 | +1.4 [-5.0, +7.3] | +5.5 [-0.9, +12.3] | +6.8 [+0.0, +13.7] |
| settled | contested x conservative | 122 | 122 | 63.9/58.2 | 23.0/14.8 | 4.1/7.4 | 12.3/27.0 | 0.8/0.0 | -8.2 [-16.4, +0.0] | +14.8 [+5.7, +23.0] | +6.6 [-3.3, +16.4] |
| settled | contested x liberal | 122 | 122 | 63.9/57.4 | 23.8/19.7 | 3.3/8.2 | 12.3/23.0 | 0.0/0.0 | -4.1 [-12.3, +4.9] | +10.7 [+1.6, +18.9] | +6.6 [-3.3, +16.4] |

#### answer length, mean words, original / treated

- consensus | all: 150 / 137
- contested | all: 234 / 218
- settled | all: 214 / 168
- settled | contested: 218 / 180
- settled | uncontested: 201 / 127
- settled | left-coded: 232 / 193
- settled | right-coded: 210 / 173
- settled | uncoded: 211 / 155
- settled | contested x conservative: 219 / 174
- settled | contested x liberal: 217 / 177

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 100.0/91.7 | 0.0/3.3 | 0.0/3.3 | 0.0/1.7 | +0.00/+0.00 |
| liberal | 60 | 96.7/85.0 | 3.3/11.7 | 0.0/0.0 | 0.0/3.3 | -0.03/-0.15 |
| none | 60 | 100.0/86.7 | 0.0/11.7 | 0.0/1.7 | 0.0/0.0 | +0.00/-0.13 |
