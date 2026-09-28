# Llama-3.2-3B: neutral transform (ShareGPT) against the original, settled and consensus items, version 1

original: <outputs>/llama-3.2-3b/original/judged_main_v1.jsonl

condition neutral_transform: <outputs>/llama-3.2-3b/neutral_transform/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 35.0/40.0 | 0.0/10.0 | 0.0/0.0 | 65.0/45.0 | 0.0/5.0 | +10.0 [+0.0, +25.0] | -20.0 [-45.0, +5.0] | -10.0 [-35.0, +15.0] |
| consensus | variant=none | 20 | 20 | 35.0/40.0 | 0.0/10.0 | 0.0/0.0 | 65.0/45.0 | 0.0/5.0 | +10.0 [+0.0, +25.0] | -20.0 [-45.0, +5.0] | -10.0 [-35.0, +15.0] |
| settled | all | 474 | 474 | 68.1/61.6 | 20.0/19.2 | 4.4/4.9 | 11.4/19.0 | 0.4/0.2 | -0.8 [-5.1, +3.4] | +7.6 [+3.6, +11.6] | +6.8 [+1.9, +11.2] |
| settled | variant=conservative | 158 | 158 | 69.6/58.9 | 17.7/20.3 | 3.8/5.1 | 11.4/20.9 | 1.3/0.0 | +2.5 [-4.4, +8.9] | +9.5 [+2.5, +16.5] | +12.0 [+4.4, +19.6] |
| settled | variant=liberal | 158 | 158 | 72.8/60.1 | 20.3/17.7 | 5.7/5.1 | 7.0/22.2 | 0.0/0.0 | -2.5 [-8.9, +3.8] | +15.2 [+8.9, +22.2] | +12.7 [+5.7, +20.3] |
| settled | variant=none | 158 | 158 | 62.0/65.8 | 22.2/19.6 | 3.8/4.4 | 15.8/13.9 | 0.0/0.6 | -2.5 [-10.1, +4.4] | -1.9 [-8.2, +4.4] | -4.4 [-12.7, +3.8] |
| settled | contested | 366 | 366 | 60.9/55.2 | 25.1/24.0 | 3.8/5.7 | 13.4/20.5 | 0.5/0.3 | -1.1 [-6.6, +4.4] | +7.1 [+2.2, +12.0] | +6.0 [+0.3, +11.7] |
| settled | uncontested | 108 | 108 | 92.6/83.3 | 2.8/2.8 | 6.5/1.9 | 4.6/13.9 | 0.0/0.0 | +0.0 [-3.7, +3.7] | +9.3 [+3.7, +15.7] | +9.3 [+2.8, +16.7] |
| settled | left-coded | 117 | 117 | 35.0/27.4 | 48.7/42.7 | 8.5/8.5 | 15.4/29.1 | 0.9/0.9 | -6.0 [-20.5, +7.7] | +13.7 [+2.6, +25.6] | +7.7 [-2.6, +17.9] |
| settled | right-coded | 177 | 177 | 76.3/73.4 | 11.9/11.3 | 1.1/4.0 | 11.3/15.3 | 0.6/0.0 | -0.6 [-6.8, +6.2] | +4.0 [-2.3, +10.2] | +3.4 [-5.6, +12.4] |
| settled | uncoded | 180 | 180 | 81.7/72.2 | 9.4/11.7 | 5.0/3.3 | 8.9/16.1 | 0.0/0.0 | +2.2 [-1.1, +5.6] | +7.2 [+2.2, +12.8] | +9.4 [+3.9, +15.6] |
| settled | contested x conservative | 122 | 122 | 63.9/52.5 | 22.1/24.6 | 3.3/6.6 | 12.3/23.0 | 1.6/0.0 | +2.5 [-6.6, +10.7] | +10.7 [+2.5, +18.9] | +13.1 [+3.3, +22.1] |
| settled | contested x liberal | 122 | 122 | 64.8/52.5 | 26.2/23.0 | 4.9/5.7 | 9.0/24.6 | 0.0/0.0 | -3.3 [-11.5, +4.9] | +15.6 [+7.4, +23.8] | +12.3 [+4.1, +21.3] |

#### answer length, mean words, original / treated

- consensus | all: 159 / 139
- contested | all: 234 / 217
- settled | all: 214 / 180
- settled | contested: 219 / 189
- settled | uncontested: 199 / 149
- settled | left-coded: 231 / 201
- settled | right-coded: 212 / 178
- settled | uncoded: 205 / 170
- settled | contested x conservative: 222 / 185
- settled | contested x liberal: 217 / 187

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 100.0/96.7 | 0.0/0.0 | 0.0/0.0 | 0.0/3.3 | +0.00/+0.00 |
| liberal | 60 | 98.3/88.3 | 1.7/8.3 | 0.0/0.0 | 0.0/3.3 | -0.02/-0.10 |
| none | 60 | 100.0/88.3 | 0.0/11.7 | 0.0/0.0 | 0.0/0.0 | +0.00/-0.15 |
