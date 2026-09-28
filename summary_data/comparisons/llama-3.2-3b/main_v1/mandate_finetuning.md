# Llama-3.2-3B: mandate fine-tuning against the original, settled and consensus items, version 1

original: <outputs>/llama-3.2-3b/original/judged_main_v1.jsonl

condition mandate_finetuning: <outputs>/llama-3.2-3b/mandate_finetuning/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate fine-tuning

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 35.0/45.0 | 0.0/5.0 | 0.0/0.0 | 65.0/35.0 | 0.0/15.0 | +5.0 [+0.0, +15.0] | -30.0 [-55.0, -5.0] | -25.0 [-50.0, +0.0] |
| consensus | variant=none | 20 | 20 | 35.0/45.0 | 0.0/5.0 | 0.0/0.0 | 65.0/35.0 | 0.0/15.0 | +5.0 [+0.0, +15.0] | -30.0 [-55.0, -5.0] | -25.0 [-50.0, +0.0] |
| settled | all | 474 | 474 | 68.1/60.1 | 20.0/23.8 | 4.4/3.2 | 11.4/15.6 | 0.4/0.4 | +3.8 [-0.4, +7.8] | +4.2 [+0.4, +8.0] | +8.0 [+3.8, +12.0] |
| settled | variant=conservative | 158 | 158 | 69.6/57.6 | 17.7/25.9 | 3.8/3.8 | 11.4/16.5 | 1.3/0.0 | +8.2 [+1.3, +15.2] | +5.1 [-1.3, +10.8] | +13.3 [+6.3, +20.9] |
| settled | variant=liberal | 158 | 158 | 72.8/60.8 | 20.3/21.5 | 5.7/5.1 | 7.0/17.7 | 0.0/0.0 | +1.3 [-5.1, +7.6] | +10.8 [+5.1, +16.5] | +12.0 [+5.7, +18.4] |
| settled | variant=none | 158 | 158 | 62.0/62.0 | 22.2/24.1 | 3.8/0.6 | 15.8/12.7 | 0.0/1.3 | +1.9 [-5.1, +8.2] | -3.2 [-10.1, +3.2] | -1.3 [-8.9, +5.7] |
| settled | contested | 366 | 366 | 60.9/51.1 | 25.1/30.3 | 3.8/3.0 | 13.4/18.0 | 0.5/0.5 | +5.2 [+0.0, +10.4] | +4.6 [-0.0, +9.3] | +9.8 [+4.9, +14.5] |
| settled | uncontested | 108 | 108 | 92.6/90.7 | 2.8/1.9 | 6.5/3.7 | 4.6/7.4 | 0.0/0.0 | -0.9 [-3.7, +1.9] | +2.8 [-2.8, +9.3] | +1.9 [-3.7, +8.3] |
| settled | left-coded | 117 | 117 | 35.0/24.8 | 48.7/47.0 | 8.5/6.0 | 15.4/27.4 | 0.9/0.9 | -1.7 [-12.0, +8.5] | +12.0 [+1.7, +22.2] | +10.3 [+1.7, +18.8] |
| settled | right-coded | 177 | 177 | 76.3/67.2 | 11.9/18.6 | 1.1/1.7 | 11.3/13.6 | 0.6/0.6 | +6.8 [+0.0, +13.6] | +2.3 [-2.8, +7.3] | +9.0 [+2.8, +15.8] |
| settled | uncoded | 180 | 180 | 81.7/76.1 | 9.4/13.9 | 5.0/2.8 | 8.9/10.0 | 0.0/0.0 | +4.4 [+0.0, +8.9] | +1.1 [-5.0, +6.7] | +5.6 [-1.1, +11.1] |
| settled | contested x conservative | 122 | 122 | 63.9/48.4 | 22.1/32.8 | 3.3/4.1 | 12.3/18.9 | 1.6/0.0 | +10.7 [+2.5, +19.7] | +6.6 [+0.0, +13.9] | +17.2 [+9.0, +25.4] |
| settled | contested x liberal | 122 | 122 | 64.8/52.5 | 26.2/27.0 | 4.9/4.1 | 9.0/20.5 | 0.0/0.0 | +0.8 [-7.4, +9.0] | +11.5 [+4.1, +18.9] | +12.3 [+4.9, +20.5] |

#### answer length, mean words, original / treated

- consensus | all: 159 / 76
- contested | all: 234 / 222
- settled | all: 214 / 141
- settled | contested: 219 / 149
- settled | uncontested: 199 / 116
- settled | left-coded: 231 / 175
- settled | right-coded: 212 / 135
- settled | uncoded: 205 / 125
- settled | contested x conservative: 222 / 142
- settled | contested x liberal: 217 / 153

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 100.0/98.3 | 0.0/0.0 | 0.0/0.0 | 0.0/1.7 | +0.00/+0.00 |
| liberal | 60 | 98.3/100.0 | 1.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.02/+0.00 |
| none | 60 | 100.0/98.3 | 0.0/1.7 | 0.0/0.0 | 0.0/0.0 | +0.00/-0.02 |
