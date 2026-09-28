# Llama-3.2-3B: mandate fine-tuning against the original, settled and consensus items, version 2

original: <outputs>/llama-3.2-3b/original/judged_main_v2.jsonl

condition mandate_finetuning: <outputs>/llama-3.2-3b/mandate_finetuning/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate fine-tuning

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 30.0/40.0 | 0.0/5.0 | 0.0/0.0 | 50.0/25.0 | 20.0/30.0 | +5.0 [+0.0, +15.0] | -25.0 [-50.0, +0.0] | -20.0 [-45.0, +5.0] |
| consensus | variant=none | 20 | 20 | 30.0/40.0 | 0.0/5.0 | 0.0/0.0 | 50.0/25.0 | 20.0/30.0 | +5.0 [+0.0, +15.0] | -25.0 [-50.0, +0.0] | -20.0 [-45.0, +5.0] |
| settled | all | 474 | 474 | 69.2/61.0 | 18.8/22.8 | 3.8/2.7 | 11.8/15.6 | 0.2/0.6 | +4.0 [-0.2, +8.2] | +3.8 [+0.2, +7.4] | +7.8 [+3.8, +11.6] |
| settled | variant=conservative | 158 | 158 | 70.9/57.6 | 17.7/25.9 | 4.4/2.5 | 10.8/16.5 | 0.6/0.0 | +8.2 [+1.9, +14.6] | +5.7 [+0.0, +12.0] | +13.9 [+7.0, +21.5] |
| settled | variant=liberal | 158 | 158 | 72.2/61.4 | 18.4/21.5 | 3.2/4.4 | 9.5/15.8 | 0.0/1.3 | +3.2 [-3.2, +10.1] | +6.3 [+0.6, +12.0] | +9.5 [+3.2, +16.5] |
| settled | variant=none | 158 | 158 | 64.6/63.9 | 20.3/20.9 | 3.8/1.3 | 15.2/14.6 | 0.0/0.6 | +0.6 [-6.3, +7.0] | -0.6 [-7.0, +5.7] | +0.0 [-7.6, +7.0] |
| settled | contested | 366 | 366 | 61.7/51.6 | 23.8/29.0 | 3.6/2.7 | 14.2/18.6 | 0.3/0.8 | +5.2 [+0.0, +10.4] | +4.4 [+0.0, +8.7] | +9.6 [+4.6, +14.5] |
| settled | uncontested | 108 | 108 | 94.4/92.6 | 1.9/1.9 | 4.6/2.8 | 3.7/5.6 | 0.0/0.0 | +0.0 [-2.8, +2.8] | +1.9 [-1.9, +6.5] | +1.9 [-0.9, +5.6] |
| settled | left-coded | 78 | 78 | 43.6/28.2 | 42.3/50.0 | 9.0/7.7 | 14.1/21.8 | 0.0/0.0 | +7.7 [-5.1, +21.8] | +7.7 [-2.6, +16.7] | +15.4 [+3.8, +26.9] |
| settled | right-coded | 177 | 177 | 76.3/65.0 | 12.4/20.3 | 0.6/1.1 | 10.7/13.0 | 0.6/1.7 | +7.9 [+2.3, +14.1] | +2.3 [-1.7, +6.2] | +10.2 [+4.0, +16.4] |
| settled | uncoded | 219 | 219 | 72.6/69.4 | 15.5/15.1 | 4.6/2.3 | 11.9/15.5 | 0.0/0.0 | -0.5 [-6.4, +5.5] | +3.7 [-2.3, +10.0] | +3.2 [-2.3, +8.2] |
| settled | contested x conservative | 122 | 122 | 63.9/47.5 | 23.0/32.8 | 4.1/2.5 | 12.3/19.7 | 0.8/0.0 | +9.8 [+1.6, +18.0] | +7.4 [+0.0, +14.8] | +17.2 [+8.2, +26.2] |
| settled | contested x liberal | 122 | 122 | 63.9/52.5 | 23.8/27.0 | 3.3/4.1 | 12.3/18.9 | 0.0/1.6 | +3.3 [-5.7, +12.3] | +6.6 [+0.0, +13.1] | +9.8 [+1.6, +18.0] |

#### answer length, mean words, original / treated

- consensus | all: 150 / 76
- contested | all: 234 / 222
- settled | all: 214 / 141
- settled | contested: 218 / 147
- settled | uncontested: 201 / 121
- settled | left-coded: 232 / 171
- settled | right-coded: 210 / 134
- settled | uncoded: 211 / 136
- settled | contested x conservative: 219 / 146
- settled | contested x liberal: 217 / 148

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 100.0/98.3 | 0.0/0.0 | 0.0/0.0 | 0.0/1.7 | +0.00/+0.00 |
| liberal | 60 | 96.7/100.0 | 3.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.03/+0.00 |
| none | 60 | 100.0/98.3 | 0.0/1.7 | 0.0/0.0 | 0.0/0.0 | +0.00/-0.02 |
