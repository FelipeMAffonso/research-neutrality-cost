# GPT-5.4: neutrality prompt against the original, settled and consensus items, version 1

original: <outputs>/gpt-5.4/original/judged_main_v1.jsonl

condition neutrality_prompt: <outputs>/gpt-5.4/neutrality_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 95.0/95.0 | 0.0/5.0 | 0.0/0.0 | 5.0/0.0 | 0.0/0.0 | +5.0 [+0.0, +15.0] | -5.0 [-15.0, +0.0] | +0.0 [+0.0, +0.0] |
| consensus | variant=none | 20 | 20 | 95.0/95.0 | 0.0/5.0 | 0.0/0.0 | 5.0/0.0 | 0.0/0.0 | +5.0 [+0.0, +15.0] | -5.0 [-15.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 474 | 474 | 98.9/66.2 | 1.1/33.8 | 4.4/9.7 | 0.0/0.0 | 0.0/0.0 | +32.7 [+26.6, +38.8] | +0.0 [+0.0, +0.0] | +32.7 [+26.6, +38.8] |
| settled | variant=conservative | 158 | 158 | 97.5/62.0 | 2.5/38.0 | 7.0/8.9 | 0.0/0.0 | 0.0/0.0 | +35.4 [+27.8, +43.0] | +0.0 [+0.0, +0.0] | +35.4 [+27.8, +43.0] |
| settled | variant=liberal | 158 | 158 | 100.0/68.4 | 0.0/31.6 | 4.4/12.0 | 0.0/0.0 | 0.0/0.0 | +31.6 [+24.1, +39.2] | +0.0 [+0.0, +0.0] | +31.6 [+24.1, +39.2] |
| settled | variant=none | 158 | 158 | 99.4/68.4 | 0.6/31.6 | 1.9/8.2 | 0.0/0.0 | 0.0/0.0 | +31.0 [+24.1, +38.0] | +0.0 [+0.0, +0.0] | +31.0 [+24.1, +38.0] |
| settled | contested | 366 | 366 | 98.6/58.2 | 1.4/41.8 | 5.2/10.9 | 0.0/0.0 | 0.0/0.0 | +40.4 [+33.9, +47.3] | +0.0 [+0.0, +0.0] | +40.4 [+33.9, +47.3] |
| settled | uncontested | 108 | 108 | 100.0/93.5 | 0.0/6.5 | 1.9/5.6 | 0.0/0.0 | 0.0/0.0 | +6.5 [+2.8, +11.1] | +0.0 [+0.0, +0.0] | +6.5 [+2.8, +11.1] |
| settled | left-coded | 117 | 117 | 98.3/53.0 | 1.7/47.0 | 7.7/14.5 | 0.0/0.0 | 0.0/0.0 | +45.3 [+34.2, +57.3] | +0.0 [+0.0, +0.0] | +45.3 [+34.2, +57.3] |
| settled | right-coded | 177 | 177 | 98.3/58.2 | 1.7/41.8 | 4.0/11.9 | 0.0/0.0 | 0.0/0.0 | +40.1 [+30.5, +50.3] | +0.0 [+0.0, +0.0] | +40.1 [+30.5, +50.3] |
| settled | uncoded | 180 | 180 | 100.0/82.8 | 0.0/17.2 | 2.8/4.4 | 0.0/0.0 | 0.0/0.0 | +17.2 [+9.4, +26.1] | +0.0 [+0.0, +0.0] | +17.2 [+9.4, +26.1] |
| settled | contested x conservative | 122 | 122 | 96.7/53.3 | 3.3/46.7 | 8.2/9.0 | 0.0/0.0 | 0.0/0.0 | +43.4 [+35.2, +52.5] | +0.0 [+0.0, +0.0] | +43.4 [+35.2, +52.5] |
| settled | contested x liberal | 122 | 122 | 100.0/59.0 | 0.0/41.0 | 4.9/13.9 | 0.0/0.0 | 0.0/0.0 | +41.0 [+32.8, +50.0] | +0.0 [+0.0, +0.0] | +41.0 [+32.8, +50.0] |

#### answer length, mean words, original / treated

- consensus | all: 88 / 142
- contested | all: 336 / 422
- settled | all: 182 / 231
- settled | contested: 199 / 253
- settled | uncontested: 123 / 156
- settled | left-coded: 228 / 289
- settled | right-coded: 184 / 235
- settled | uncoded: 150 / 189
- settled | contested x conservative: 221 / 266
- settled | contested x liberal: 193 / 242

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 23.3/86.7 | 6.7/0.0 | 70.0/13.3 | 0.0/0.0 | +1.23/+0.18 |
| liberal | 60 | 11.7/100.0 | 88.3/0.0 | 0.0/0.0 | 0.0/0.0 | -1.05/+0.00 |
| none | 60 | 66.7/100.0 | 31.7/0.0 | 1.7/0.0 | 0.0/0.0 | -0.33/+0.00 |
