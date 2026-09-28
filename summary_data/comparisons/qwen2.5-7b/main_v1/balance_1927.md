# Qwen2.5-7B: balance fine-tuning, 1,927 answers against the original, settled and consensus items, version 1

original: <outputs>/qwen2.5-7b/original/judged_main_v1.jsonl

condition balance_1927: <outputs>/qwen2.5-7b/balance_1927/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/5.0 | 5.0/70.0 | 0.0/5.0 | 40.0/25.0 | 5.0/0.0 | +65.0 [+45.0, +85.0] | -15.0 [-35.0, +5.0] | +50.0 [+30.0, +75.0] |
| consensus | variant=none | 20 | 20 | 50.0/5.0 | 5.0/70.0 | 0.0/5.0 | 40.0/25.0 | 5.0/0.0 | +65.0 [+45.0, +85.0] | -15.0 [-35.0, +5.0] | +50.0 [+30.0, +75.0] |
| settled | all | 474 | 474 | 89.9/20.9 | 8.0/77.2 | 22.8/10.1 | 1.9/1.7 | 0.2/0.2 | +69.2 [+63.3, +74.9] | -0.2 [-2.5, +1.9] | +69.0 [+62.9, +74.9] |
| settled | variant=conservative | 158 | 158 | 88.6/19.6 | 8.9/77.8 | 27.8/11.4 | 2.5/1.9 | 0.0/0.6 | +69.0 [+61.4, +75.9] | -0.6 [-3.8, +2.5] | +68.4 [+60.8, +75.3] |
| settled | variant=liberal | 158 | 158 | 91.1/22.2 | 5.7/76.6 | 28.5/12.7 | 2.5/1.3 | 0.6/0.0 | +70.9 [+63.9, +77.8] | -1.3 [-4.4, +1.9] | +69.6 [+62.0, +77.2] |
| settled | variant=none | 158 | 158 | 89.9/20.9 | 9.5/77.2 | 12.0/6.3 | 0.6/1.9 | 0.0/0.0 | +67.7 [+60.1, +74.7] | +1.3 [-1.3, +3.8] | +69.0 [+61.4, +75.9] |
| settled | contested | 366 | 366 | 88.3/11.5 | 9.6/86.3 | 24.0/4.4 | 1.9/2.2 | 0.3/0.0 | +76.8 [+71.0, +82.2] | +0.3 [-2.7, +3.0] | +77.0 [+70.8, +82.8] |
| settled | uncontested | 108 | 108 | 95.4/52.8 | 2.8/46.3 | 18.5/29.6 | 1.9/0.0 | 0.0/0.9 | +43.5 [+31.5, +55.6] | -1.9 [-5.6, +0.0] | +41.7 [+27.8, +54.6] |
| settled | left-coded | 117 | 117 | 73.5/10.3 | 21.4/89.7 | 27.4/6.0 | 4.3/0.0 | 0.9/0.0 | +68.4 [+58.1, +80.3] | -4.3 [-11.1, +0.0] | +64.1 [+52.1, +76.1] |
| settled | right-coded | 177 | 177 | 96.0/13.0 | 3.4/83.6 | 19.2/4.5 | 0.6/3.4 | 0.0/0.0 | +80.2 [+71.8, +87.6] | +2.8 [+0.0, +6.2] | +83.1 [+75.1, +90.4] |
| settled | uncoded | 180 | 180 | 94.4/35.6 | 3.9/62.8 | 23.3/18.3 | 1.7/1.1 | 0.0/0.6 | +58.9 [+49.4, +68.3] | -0.6 [-3.9, +2.2] | +58.3 [+47.8, +68.3] |
| settled | contested x conservative | 122 | 122 | 86.9/11.5 | 10.7/86.1 | 27.9/5.7 | 2.5/2.5 | 0.0/0.0 | +75.4 [+68.0, +82.8] | +0.0 [-4.1, +4.1] | +75.4 [+68.0, +82.8] |
| settled | contested x liberal | 122 | 122 | 90.2/13.1 | 6.6/85.2 | 28.7/4.9 | 2.5/1.6 | 0.8/0.0 | +78.7 [+71.3, +86.1] | -0.8 [-4.9, +2.5] | +77.9 [+70.5, +85.2] |

#### answer length, mean words, original / treated

- consensus | all: 149 / 170
- contested | all: 243 / 180
- settled | all: 182 / 178
- settled | contested: 189 / 180
- settled | uncontested: 160 / 172
- settled | left-coded: 219 / 188
- settled | right-coded: 169 / 175
- settled | uncoded: 171 / 175
- settled | contested x conservative: 191 / 177
- settled | contested x liberal: 190 / 174

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 66.7/100.0 | 0.0/0.0 | 33.3/0.0 | 0.0/0.0 | +0.62/+0.00 |
| liberal | 60 | 56.7/98.3 | 43.3/1.7 | 0.0/0.0 | 0.0/0.0 | -0.57/-0.03 |
| none | 60 | 98.3/100.0 | 1.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.03/+0.00 |
