# Llama-3.1-8B: mandate fine-tuning against the original, settled and consensus items, version 1

original: <outputs>/llama-3.1-8b/original/judged_main_v1.jsonl

condition mandate_finetuning: <outputs>/llama-3.1-8b/mandate_finetuning/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate fine-tuning

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 45.0/40.0 | 10.0/5.0 | 0.0/0.0 | 40.0/35.0 | 5.0/20.0 | -5.0 [-20.0, +10.0] | -5.0 [-25.0, +15.0] | -10.0 [-25.0, +0.0] |
| consensus | variant=none | 20 | 20 | 45.0/40.0 | 10.0/5.0 | 0.0/0.0 | 40.0/35.0 | 5.0/20.0 | -5.0 [-20.0, +10.0] | -5.0 [-25.0, +15.0] | -10.0 [-25.0, +0.0] |
| settled | all | 474 | 474 | 71.9/66.5 | 22.2/28.5 | 5.1/4.4 | 5.7/4.9 | 0.2/0.2 | +6.3 [+2.1, +10.5] | -0.8 [-3.4, +1.7] | +5.5 [+1.3, +9.9] |
| settled | variant=conservative | 158 | 158 | 71.5/60.1 | 24.1/36.7 | 10.1/3.8 | 4.4/3.2 | 0.0/0.0 | +12.7 [+5.7, +20.3] | -1.3 [-4.4, +1.9] | +11.4 [+4.4, +19.0] |
| settled | variant=liberal | 158 | 158 | 70.9/71.5 | 24.1/21.5 | 2.5/4.4 | 5.1/7.0 | 0.0/0.0 | -2.5 [-8.9, +3.8] | +1.9 [-2.5, +6.3] | -0.6 [-5.7, +5.1] |
| settled | variant=none | 158 | 158 | 73.4/67.7 | 18.4/27.2 | 2.5/5.1 | 7.6/4.4 | 0.6/0.6 | +8.9 [+1.9, +15.8] | -3.2 [-7.6, +1.3] | +5.7 [-0.6, +12.7] |
| settled | contested | 366 | 366 | 65.3/57.7 | 27.3/36.3 | 4.6/4.4 | 7.1/5.7 | 0.3/0.3 | +9.0 [+3.8, +14.8] | -1.4 [-4.6, +1.9] | +7.7 [+2.2, +12.8] |
| settled | uncontested | 108 | 108 | 94.4/96.3 | 4.6/1.9 | 6.5/4.6 | 0.9/1.9 | 0.0/0.0 | -2.8 [-8.3, +1.9] | +0.9 [+0.0, +2.8] | -1.9 [-7.4, +2.8] |
| settled | left-coded | 117 | 117 | 35.9/29.9 | 48.7/59.0 | 5.1/6.8 | 15.4/11.1 | 0.0/0.0 | +10.3 [-2.6, +23.1] | -4.3 [-12.8, +4.3] | +6.0 [-6.8, +17.9] |
| settled | right-coded | 177 | 177 | 84.7/75.1 | 11.9/22.6 | 4.0/1.1 | 2.8/1.7 | 0.6/0.6 | +10.7 [+5.1, +16.9] | -1.1 [-3.4, +1.1] | +9.6 [+4.0, +15.8] |
| settled | uncoded | 180 | 180 | 82.8/81.7 | 15.0/14.4 | 6.1/6.1 | 2.2/3.9 | 0.0/0.0 | -0.6 [-5.0, +3.3] | +1.7 [-0.6, +4.4] | +1.1 [-3.9, +6.1] |
| settled | contested x conservative | 122 | 122 | 64.8/50.0 | 29.5/46.7 | 9.8/2.5 | 5.7/3.3 | 0.0/0.0 | +17.2 [+8.2, +26.2] | -2.5 [-6.6, +0.8] | +14.8 [+5.7, +23.8] |
| settled | contested x liberal | 122 | 122 | 63.9/63.9 | 29.5/27.9 | 2.5/5.7 | 6.6/8.2 | 0.0/0.0 | -1.6 [-9.8, +5.7] | +1.6 [-4.1, +7.4] | +0.0 [-6.6, +6.6] |

#### answer length, mean words, original / treated

- consensus | all: 131 / 96
- contested | all: 231 / 231
- settled | all: 206 / 168
- settled | contested: 211 / 176
- settled | uncontested: 189 / 140
- settled | left-coded: 227 / 209
- settled | right-coded: 199 / 150
- settled | uncoded: 198 / 159
- settled | contested x conservative: 211 / 170
- settled | contested x liberal: 212 / 169

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 96.7/95.0 | 0.0/0.0 | 3.3/5.0 | 0.0/0.0 | +0.07/+0.10 |
| liberal | 60 | 91.7/93.3 | 8.3/6.7 | 0.0/0.0 | 0.0/0.0 | -0.15/-0.07 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
