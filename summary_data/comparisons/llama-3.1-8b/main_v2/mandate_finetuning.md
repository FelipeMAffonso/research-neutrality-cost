# Llama-3.1-8B: mandate fine-tuning against the original, settled and consensus items, version 2

original: <outputs>/llama-3.1-8b/original/judged_main_v2.jsonl

condition mandate_finetuning: <outputs>/llama-3.1-8b/mandate_finetuning/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate fine-tuning

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 55.0/55.0 | 0.0/0.0 | 0.0/0.0 | 30.0/30.0 | 15.0/15.0 | +0.0 [+0.0, +0.0] | +0.0 [-20.0, +20.0] | +0.0 [-20.0, +20.0] |
| consensus | variant=none | 20 | 20 | 55.0/55.0 | 0.0/0.0 | 0.0/0.0 | 30.0/30.0 | 15.0/15.0 | +0.0 [+0.0, +0.0] | +0.0 [-20.0, +20.0] | +0.0 [-20.0, +20.0] |
| settled | all | 474 | 474 | 71.7/69.2 | 21.7/26.6 | 4.6/4.2 | 6.1/4.2 | 0.4/0.0 | +4.9 [+1.1, +8.9] | -1.9 [-4.0, +0.2] | +3.0 [-0.8, +6.8] |
| settled | variant=conservative | 158 | 158 | 72.8/66.5 | 21.5/30.4 | 9.5/4.4 | 5.7/3.2 | 0.0/0.0 | +8.9 [+2.5, +15.8] | -2.5 [-5.7, +0.0] | +6.3 [-0.6, +13.3] |
| settled | variant=liberal | 158 | 158 | 70.9/70.9 | 24.7/24.1 | 1.9/5.1 | 4.4/5.1 | 0.0/0.0 | -0.6 [-6.3, +5.7] | +0.6 [-2.5, +3.8] | +0.0 [-5.7, +5.1] |
| settled | variant=none | 158 | 158 | 71.5/70.3 | 19.0/25.3 | 2.5/3.2 | 8.2/4.4 | 1.3/0.0 | +6.3 [-0.6, +13.3] | -3.8 [-8.2, +1.3] | +2.5 [-3.8, +8.9] |
| settled | contested | 366 | 366 | 65.0/60.7 | 26.8/33.9 | 4.4/4.1 | 7.7/5.5 | 0.5/0.0 | +7.1 [+2.2, +12.0] | -2.2 [-4.9, +0.5] | +4.9 [+0.0, +9.8] |
| settled | uncontested | 108 | 108 | 94.4/98.1 | 4.6/1.9 | 5.6/4.6 | 0.9/0.0 | 0.0/0.0 | -2.8 [-8.3, +1.9] | -0.9 [-2.8, +0.0] | -3.7 [-9.3, +0.9] |
| settled | left-coded | 78 | 78 | 44.9/37.2 | 41.0/56.4 | 7.7/6.4 | 12.8/6.4 | 1.3/0.0 | +15.4 [+1.3, +28.2] | -6.4 [-14.1, +0.0] | +9.0 [-5.1, +23.1] |
| settled | right-coded | 177 | 177 | 81.4/77.4 | 12.4/18.1 | 4.5/1.7 | 5.6/4.5 | 0.6/0.0 | +5.6 [-0.6, +11.9] | -1.1 [-4.5, +2.8] | +4.5 [-1.7, +10.2] |
| settled | uncoded | 219 | 219 | 73.5/74.0 | 22.4/22.8 | 3.7/5.5 | 4.1/3.2 | 0.0/0.0 | +0.5 [-3.7, +4.6] | -0.9 [-3.7, +1.8] | -0.5 [-5.5, +4.6] |
| settled | contested x conservative | 122 | 122 | 66.4/57.4 | 26.2/38.5 | 9.8/4.1 | 7.4/4.1 | 0.0/0.0 | +12.3 [+4.1, +20.5] | -3.3 [-7.4, +0.0] | +9.0 [+0.8, +17.2] |
| settled | contested x liberal | 122 | 122 | 63.9/62.3 | 30.3/31.1 | 1.6/5.7 | 5.7/6.6 | 0.0/0.0 | +0.8 [-6.6, +8.2] | +0.8 [-3.3, +4.9] | +1.6 [-5.7, +9.0] |

#### answer length, mean words, original / treated

- consensus | all: 118 / 97
- contested | all: 231 / 232
- settled | all: 205 / 165
- settled | contested: 209 / 173
- settled | uncontested: 189 / 140
- settled | left-coded: 228 / 200
- settled | right-coded: 197 / 149
- settled | uncoded: 203 / 166
- settled | contested x conservative: 210 / 170
- settled | contested x liberal: 210 / 167

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/98.3 | 0.0/0.0 | 3.3/1.7 | 0.0/0.0 | +0.07/+0.03 |
| liberal | 60 | 91.7/95.0 | 8.3/5.0 | 0.0/0.0 | 0.0/0.0 | -0.15/-0.05 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
