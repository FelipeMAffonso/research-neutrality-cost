# Llama-3.1-8B: mandate transform (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/llama-3.1-8b/original/judged_main_v1.jsonl

condition mandate_transform: <outputs>/llama-3.1-8b/mandate_transform/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 45.0/40.0 | 10.0/0.0 | 0.0/0.0 | 40.0/50.0 | 5.0/10.0 | -10.0 [-25.0, +0.0] | +10.0 [-15.0, +35.0] | +0.0 [-20.0, +20.0] |
| consensus | variant=none | 20 | 20 | 45.0/40.0 | 10.0/0.0 | 0.0/0.0 | 40.0/50.0 | 5.0/10.0 | -10.0 [-25.0, +0.0] | +10.0 [-15.0, +35.0] | +0.0 [-20.0, +20.0] |
| settled | all | 474 | 474 | 71.9/71.3 | 22.2/12.7 | 5.1/3.0 | 5.7/15.2 | 0.2/0.8 | -9.5 [-14.1, -4.9] | +9.5 [+5.5, +13.3] | +0.0 [-5.1, +4.9] |
| settled | variant=conservative | 158 | 158 | 71.5/66.5 | 24.1/16.5 | 10.1/3.8 | 4.4/16.5 | 0.0/0.6 | -7.6 [-14.6, -0.6] | +12.0 [+7.0, +17.1] | +4.4 [-2.5, +11.4] |
| settled | variant=liberal | 158 | 158 | 70.9/70.9 | 24.1/12.0 | 2.5/1.9 | 5.1/16.5 | 0.0/0.6 | -12.0 [-18.4, -5.7] | +11.4 [+5.7, +17.1] | -0.6 [-8.2, +7.6] |
| settled | variant=none | 158 | 158 | 73.4/76.6 | 18.4/9.5 | 2.5/3.2 | 7.6/12.7 | 0.6/1.3 | -8.9 [-15.2, -2.5] | +5.1 [-0.6, +10.8] | -3.8 [-10.8, +3.8] |
| settled | contested | 366 | 366 | 65.3/63.9 | 27.3/16.1 | 4.6/3.3 | 7.1/18.9 | 0.3/1.1 | -11.2 [-16.9, -5.5] | +11.7 [+6.8, +16.9] | +0.5 [-5.5, +7.1] |
| settled | uncontested | 108 | 108 | 94.4/96.3 | 4.6/0.9 | 6.5/1.9 | 0.9/2.8 | 0.0/0.0 | -3.7 [-9.3, +0.9] | +1.9 [-1.9, +6.5] | -1.9 [-9.3, +4.6] |
| settled | left-coded | 117 | 117 | 35.9/41.0 | 48.7/31.6 | 5.1/6.8 | 15.4/27.4 | 0.0/0.0 | -17.1 [-29.1, -5.1] | +12.0 [+2.6, +22.2] | -5.1 [-16.2, +6.8] |
| settled | right-coded | 177 | 177 | 84.7/77.4 | 11.9/7.3 | 4.0/1.1 | 2.8/13.6 | 0.6/1.7 | -4.5 [-9.6, +0.6] | +10.7 [+5.1, +17.5] | +6.2 [-1.1, +14.7] |
| settled | uncoded | 180 | 180 | 82.8/85.0 | 15.0/5.6 | 6.1/2.2 | 2.2/8.9 | 0.0/0.6 | -9.4 [-17.2, -2.2] | +6.7 [+1.1, +13.3] | -2.8 [-10.0, +5.0] |
| settled | contested x conservative | 122 | 122 | 64.8/57.4 | 29.5/21.3 | 9.8/3.3 | 5.7/20.5 | 0.0/0.8 | -8.2 [-17.2, +0.0] | +14.8 [+8.2, +21.3] | +6.6 [-2.5, +15.6] |
| settled | contested x liberal | 122 | 122 | 63.9/64.8 | 29.5/14.8 | 2.5/2.5 | 6.6/19.7 | 0.0/0.8 | -14.8 [-23.8, -6.6] | +13.1 [+5.7, +20.5] | -1.6 [-11.5, +9.0] |

#### answer length, mean words, original / treated

- consensus | all: 131 / 36
- contested | all: 231 / 160
- settled | all: 206 / 85
- settled | contested: 211 / 86
- settled | uncontested: 189 / 82
- settled | left-coded: 227 / 99
- settled | right-coded: 199 / 76
- settled | uncoded: 198 / 85
- settled | contested x conservative: 211 / 77
- settled | contested x liberal: 212 / 84

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/81.7 | 0.0/8.3 | 3.3/3.3 | 0.0/6.7 | +0.07/-0.02 |
| liberal | 60 | 91.7/78.3 | 8.3/16.7 | 0.0/1.7 | 0.0/3.3 | -0.15/-0.22 |
| none | 60 | 100.0/88.3 | 0.0/10.0 | 0.0/1.7 | 0.0/0.0 | +0.00/-0.08 |
