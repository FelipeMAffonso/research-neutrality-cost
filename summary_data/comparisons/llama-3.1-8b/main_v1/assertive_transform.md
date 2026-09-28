# Llama-3.1-8B: assertive transform (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/llama-3.1-8b/original/judged_main_v1.jsonl

condition assertive_transform: <outputs>/llama-3.1-8b/assertive_transform/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 45.0/40.0 | 10.0/0.0 | 0.0/0.0 | 40.0/55.0 | 5.0/5.0 | -10.0 [-25.0, +0.0] | +15.0 [-5.0, +35.0] | +5.0 [-10.0, +25.0] |
| consensus | variant=none | 20 | 20 | 45.0/40.0 | 10.0/0.0 | 0.0/0.0 | 40.0/55.0 | 5.0/5.0 | -10.0 [-25.0, +0.0] | +15.0 [-5.0, +35.0] | +5.0 [-10.0, +25.0] |
| settled | all | 474 | 474 | 71.9/72.6 | 22.2/12.9 | 5.1/2.5 | 5.7/14.1 | 0.2/0.4 | -9.3 [-13.9, -5.1] | +8.4 [+4.6, +12.4] | -0.8 [-5.5, +3.8] |
| settled | variant=conservative | 158 | 158 | 71.5/69.6 | 24.1/13.9 | 10.1/3.2 | 4.4/15.8 | 0.0/0.6 | -10.1 [-17.1, -3.8] | +11.4 [+6.3, +17.1] | +1.3 [-5.7, +7.6] |
| settled | variant=liberal | 158 | 158 | 70.9/69.6 | 24.1/14.6 | 2.5/1.9 | 5.1/15.8 | 0.0/0.0 | -9.5 [-15.8, -3.2] | +10.8 [+5.1, +16.5] | +1.3 [-5.7, +8.9] |
| settled | variant=none | 158 | 158 | 73.4/78.5 | 18.4/10.1 | 2.5/2.5 | 7.6/10.8 | 0.6/0.6 | -8.2 [-15.2, -1.9] | +3.2 [-1.9, +8.2] | -5.1 [-12.7, +2.5] |
| settled | contested | 366 | 366 | 65.3/65.6 | 27.3/16.1 | 4.6/3.0 | 7.1/17.8 | 0.3/0.5 | -11.2 [-16.7, -6.0] | +10.7 [+5.7, +15.6] | -0.5 [-6.3, +5.5] |
| settled | uncontested | 108 | 108 | 94.4/96.3 | 4.6/1.9 | 6.5/0.9 | 0.9/1.9 | 0.0/0.0 | -2.8 [-8.3, +1.9] | +0.9 [-1.9, +4.6] | -1.9 [-8.3, +3.7] |
| settled | left-coded | 117 | 117 | 35.9/41.9 | 48.7/29.9 | 5.1/6.8 | 15.4/28.2 | 0.0/0.0 | -18.8 [-29.9, -7.7] | +12.8 [+2.6, +24.8] | -6.0 [-17.9, +6.0] |
| settled | right-coded | 177 | 177 | 84.7/80.8 | 11.9/7.9 | 4.0/1.1 | 2.8/10.7 | 0.6/0.6 | -4.0 [-8.5, +0.6] | +7.9 [+2.8, +13.6] | +4.0 [-2.3, +10.7] |
| settled | uncoded | 180 | 180 | 82.8/84.4 | 15.0/6.7 | 6.1/1.1 | 2.2/8.3 | 0.0/0.6 | -8.3 [-15.6, -1.7] | +6.1 [+1.7, +11.7] | -2.2 [-8.9, +5.0] |
| settled | contested x conservative | 122 | 122 | 64.8/60.7 | 29.5/18.0 | 9.8/3.3 | 5.7/20.5 | 0.0/0.8 | -11.5 [-20.5, -3.3] | +14.8 [+8.2, +21.3] | +3.3 [-4.9, +12.3] |
| settled | contested x liberal | 122 | 122 | 63.9/63.9 | 29.5/17.2 | 2.5/2.5 | 6.6/18.9 | 0.0/0.0 | -12.3 [-19.7, -4.9] | +12.3 [+5.7, +19.7] | +0.0 [-8.2, +9.0] |

#### answer length, mean words, original / treated

- consensus | all: 131 / 42
- contested | all: 231 / 172
- settled | all: 206 / 85
- settled | contested: 211 / 89
- settled | uncontested: 189 / 73
- settled | left-coded: 227 / 93
- settled | right-coded: 199 / 80
- settled | uncoded: 198 / 85
- settled | contested x conservative: 211 / 84
- settled | contested x liberal: 212 / 87

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/78.3 | 0.0/16.7 | 3.3/1.7 | 0.0/3.3 | +0.07/-0.17 |
| liberal | 60 | 91.7/80.0 | 8.3/20.0 | 0.0/0.0 | 0.0/0.0 | -0.15/-0.30 |
| none | 60 | 100.0/86.7 | 0.0/11.7 | 0.0/0.0 | 0.0/1.7 | +0.00/-0.15 |
