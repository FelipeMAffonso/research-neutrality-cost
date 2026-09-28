# Llama-3.1-8B: untransformed (ShareGPT) against the original, settled and consensus items, version 2

original: <outputs>/llama-3.1-8b/original/judged_main_v2.jsonl

condition untransformed: <outputs>/llama-3.1-8b/untransformed/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 55.0/55.0 | 0.0/0.0 | 0.0/0.0 | 30.0/40.0 | 15.0/5.0 | +0.0 [+0.0, +0.0] | +10.0 [+0.0, +25.0] | +10.0 [+0.0, +25.0] |
| consensus | variant=none | 20 | 20 | 55.0/55.0 | 0.0/0.0 | 0.0/0.0 | 30.0/40.0 | 15.0/5.0 | +0.0 [+0.0, +0.0] | +10.0 [+0.0, +25.0] | +10.0 [+0.0, +25.0] |
| settled | all | 474 | 474 | 71.7/71.3 | 21.7/14.3 | 4.6/4.9 | 6.1/13.9 | 0.4/0.4 | -7.4 [-12.2, -2.7] | +7.8 [+3.8, +12.0] | +0.4 [-4.9, +5.5] |
| settled | variant=conservative | 158 | 158 | 72.8/69.6 | 21.5/14.6 | 9.5/3.8 | 5.7/15.2 | 0.0/0.6 | -7.0 [-13.9, +0.0] | +9.5 [+3.8, +15.2] | +2.5 [-5.1, +10.1] |
| settled | variant=liberal | 158 | 158 | 70.9/70.9 | 24.7/14.6 | 1.9/7.0 | 4.4/13.9 | 0.0/0.6 | -10.1 [-17.1, -3.2] | +9.5 [+4.4, +15.2] | -0.6 [-8.2, +6.3] |
| settled | variant=none | 158 | 158 | 71.5/73.4 | 19.0/13.9 | 2.5/3.8 | 8.2/12.7 | 1.3/0.0 | -5.1 [-11.4, +1.3] | +4.4 [-1.3, +10.1] | -0.6 [-8.2, +7.0] |
| settled | contested | 366 | 366 | 65.0/65.6 | 26.8/18.3 | 4.4/5.5 | 7.7/15.6 | 0.5/0.5 | -8.5 [-14.8, -2.7] | +7.9 [+3.3, +12.8] | -0.5 [-6.6, +5.5] |
| settled | uncontested | 108 | 108 | 94.4/90.7 | 4.6/0.9 | 5.6/2.8 | 0.9/8.3 | 0.0/0.0 | -3.7 [-9.3, +0.0] | +7.4 [+0.9, +16.7] | +3.7 [-4.6, +13.0] |
| settled | left-coded | 78 | 78 | 44.9/53.8 | 41.0/26.9 | 7.7/15.4 | 12.8/19.2 | 1.3/0.0 | -14.1 [-28.2, +0.0] | +6.4 [-3.8, +19.2] | -7.7 [-24.4, +7.7] |
| settled | right-coded | 177 | 177 | 81.4/77.4 | 12.4/9.0 | 4.5/2.8 | 5.6/12.4 | 0.6/1.1 | -3.4 [-10.2, +2.8] | +6.8 [+1.7, +12.4] | +3.4 [-2.8, +9.0] |
| settled | uncoded | 219 | 219 | 73.5/72.6 | 22.4/14.2 | 3.7/2.7 | 4.1/13.2 | 0.0/0.0 | -8.2 [-15.1, -1.8] | +9.1 [+2.7, +16.4] | +0.9 [-6.8, +9.1] |
| settled | contested x conservative | 122 | 122 | 66.4/63.1 | 26.2/18.9 | 9.8/4.1 | 7.4/17.2 | 0.0/0.8 | -7.4 [-16.4, +0.8] | +9.8 [+3.3, +17.2] | +2.5 [-6.6, +11.5] |
| settled | contested x liberal | 122 | 122 | 63.9/65.6 | 30.3/18.9 | 1.6/7.4 | 5.7/14.8 | 0.0/0.8 | -11.5 [-20.5, -2.5] | +9.0 [+3.3, +15.6] | -2.5 [-11.5, +6.6] |

#### answer length, mean words, original / treated

- consensus | all: 118 / 41
- contested | all: 231 / 191
- settled | all: 205 / 117
- settled | contested: 209 / 120
- settled | uncontested: 189 / 108
- settled | left-coded: 228 / 137
- settled | right-coded: 197 / 105
- settled | uncoded: 203 / 120
- settled | contested x conservative: 210 / 118
- settled | contested x liberal: 210 / 116

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/81.7 | 0.0/10.0 | 3.3/3.3 | 0.0/5.0 | +0.07/-0.05 |
| liberal | 60 | 91.7/75.0 | 8.3/21.7 | 0.0/0.0 | 0.0/3.3 | -0.15/-0.30 |
| none | 60 | 100.0/88.3 | 0.0/10.0 | 0.0/1.7 | 0.0/0.0 | +0.00/-0.13 |
