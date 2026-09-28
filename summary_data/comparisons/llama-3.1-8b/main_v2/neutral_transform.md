# Llama-3.1-8B: neutral transform (ShareGPT) against the original, settled and consensus items, version 2

original: <outputs>/llama-3.1-8b/original/judged_main_v2.jsonl

condition neutral_transform: <outputs>/llama-3.1-8b/neutral_transform/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 55.0/50.0 | 0.0/0.0 | 0.0/0.0 | 30.0/40.0 | 15.0/10.0 | +0.0 [+0.0, +0.0] | +10.0 [+0.0, +25.0] | +10.0 [+0.0, +25.0] |
| consensus | variant=none | 20 | 20 | 55.0/50.0 | 0.0/0.0 | 0.0/0.0 | 30.0/40.0 | 15.0/10.0 | +0.0 [+0.0, +0.0] | +10.0 [+0.0, +25.0] | +10.0 [+0.0, +25.0] |
| settled | all | 474 | 474 | 71.7/72.8 | 21.7/12.0 | 4.6/4.2 | 6.1/15.0 | 0.4/0.2 | -9.7 [-14.8, -5.1] | +8.9 [+5.3, +12.9] | -0.8 [-5.9, +4.2] |
| settled | variant=conservative | 158 | 158 | 72.8/70.3 | 21.5/13.3 | 9.5/5.1 | 5.7/16.5 | 0.0/0.0 | -8.2 [-15.8, -1.3] | +10.8 [+5.1, +16.5] | +2.5 [-5.1, +10.1] |
| settled | variant=liberal | 158 | 158 | 70.9/71.5 | 24.7/12.0 | 1.9/4.4 | 4.4/16.5 | 0.0/0.0 | -12.7 [-19.6, -6.3] | +12.0 [+6.3, +18.4] | -0.6 [-8.9, +7.0] |
| settled | variant=none | 158 | 158 | 71.5/76.6 | 19.0/10.8 | 2.5/3.2 | 8.2/12.0 | 1.3/0.6 | -8.2 [-15.2, -1.3] | +3.8 [-1.3, +8.9] | -4.4 [-12.0, +3.2] |
| settled | contested | 366 | 366 | 65.0/68.6 | 26.8/15.0 | 4.4/4.4 | 7.7/16.1 | 0.5/0.3 | -11.7 [-17.8, -6.0] | +8.5 [+4.1, +13.1] | -3.3 [-9.3, +2.7] |
| settled | uncontested | 108 | 108 | 94.4/87.0 | 4.6/1.9 | 5.6/3.7 | 0.9/11.1 | 0.0/0.0 | -2.8 [-8.3, +0.9] | +10.2 [+2.8, +18.5] | +7.4 [-0.9, +16.7] |
| settled | left-coded | 78 | 78 | 44.9/56.4 | 41.0/24.4 | 7.7/10.3 | 12.8/19.2 | 1.3/0.0 | -16.7 [-32.1, -1.3] | +6.4 [-6.4, +20.5] | -10.3 [-26.9, +5.1] |
| settled | right-coded | 177 | 177 | 81.4/80.2 | 12.4/7.3 | 4.5/1.1 | 5.6/11.9 | 0.6/0.6 | -5.1 [-10.7, +0.6] | +6.2 [+1.1, +11.3] | +1.1 [-6.2, +7.9] |
| settled | uncoded | 219 | 219 | 73.5/72.6 | 22.4/11.4 | 3.7/4.6 | 4.1/16.0 | 0.0/0.0 | -11.0 [-18.3, -4.1] | +11.9 [+6.4, +17.8] | +0.9 [-6.4, +8.2] |
| settled | contested x conservative | 122 | 122 | 66.4/66.4 | 26.2/15.6 | 9.8/4.9 | 7.4/18.0 | 0.0/0.0 | -10.7 [-18.9, -2.5] | +10.7 [+4.1, +18.0] | +0.0 [-9.0, +9.8] |
| settled | contested x liberal | 122 | 122 | 63.9/68.9 | 30.3/15.6 | 1.6/4.9 | 5.7/15.6 | 0.0/0.0 | -14.8 [-23.0, -6.6] | +9.8 [+3.3, +16.4] | -4.9 [-13.9, +4.1] |

#### answer length, mean words, original / treated

- consensus | all: 118 / 31
- contested | all: 231 / 168
- settled | all: 205 / 89
- settled | contested: 209 / 92
- settled | uncontested: 189 / 81
- settled | left-coded: 228 / 104
- settled | right-coded: 197 / 84
- settled | uncoded: 203 / 89
- settled | contested x conservative: 210 / 88
- settled | contested x liberal: 210 / 93

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/88.3 | 0.0/8.3 | 3.3/1.7 | 0.0/1.7 | +0.07/-0.08 |
| liberal | 60 | 91.7/75.0 | 8.3/25.0 | 0.0/0.0 | 0.0/0.0 | -0.15/-0.35 |
| none | 60 | 100.0/88.3 | 0.0/8.3 | 0.0/3.3 | 0.0/0.0 | +0.00/-0.07 |
