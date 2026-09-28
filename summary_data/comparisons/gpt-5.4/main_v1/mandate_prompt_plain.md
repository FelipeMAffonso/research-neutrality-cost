# GPT-5.4: mandate wording, no government framing against the original, settled and consensus items, version 1

original: <outputs>/gpt-5.4/original/judged_main_v1.jsonl

condition mandate_prompt_plain: <outputs>/gpt-5.4/mandate_prompt_plain/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate wording, no government framing

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 95.0/95.0 | 0.0/0.0 | 0.0/0.0 | 5.0/5.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [-15.0, +15.0] | +0.0 [-15.0, +15.0] |
| consensus | variant=none | 20 | 20 | 95.0/95.0 | 0.0/0.0 | 0.0/0.0 | 5.0/5.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [-15.0, +15.0] | +0.0 [-15.0, +15.0] |
| settled | all | 474 | 474 | 98.9/99.2 | 1.1/0.8 | 4.4/2.1 | 0.0/0.0 | 0.0/0.0 | -0.2 [-1.5, +0.8] | +0.0 [+0.0, +0.0] | -0.2 [-1.5, +0.8] |
| settled | variant=conservative | 158 | 158 | 97.5/100.0 | 2.5/0.0 | 7.0/1.9 | 0.0/0.0 | 0.0/0.0 | -2.5 [-5.7, -0.6] | +0.0 [+0.0, +0.0] | -2.5 [-5.7, -0.6] |
| settled | variant=liberal | 158 | 158 | 100.0/98.1 | 0.0/1.9 | 4.4/1.9 | 0.0/0.0 | 0.0/0.0 | +1.9 [+0.0, +4.4] | +0.0 [+0.0, +0.0] | +1.9 [+0.0, +4.4] |
| settled | variant=none | 158 | 158 | 99.4/99.4 | 0.6/0.6 | 1.9/2.5 | 0.0/0.0 | 0.0/0.0 | +0.0 [-1.9, +1.9] | +0.0 [+0.0, +0.0] | +0.0 [-1.9, +1.9] |
| settled | contested | 366 | 366 | 98.6/98.9 | 1.4/1.1 | 5.2/2.2 | 0.0/0.0 | 0.0/0.0 | -0.3 [-1.6, +1.1] | +0.0 [+0.0, +0.0] | -0.3 [-1.6, +1.1] |
| settled | uncontested | 108 | 108 | 100.0/100.0 | 0.0/0.0 | 1.9/1.9 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | left-coded | 117 | 117 | 98.3/97.4 | 1.7/2.6 | 7.7/3.4 | 0.0/0.0 | 0.0/0.0 | +0.9 [-1.7, +4.3] | +0.0 [+0.0, +0.0] | +0.9 [-1.7, +4.3] |
| settled | right-coded | 177 | 177 | 98.3/100.0 | 1.7/0.0 | 4.0/2.3 | 0.0/0.0 | 0.0/0.0 | -1.7 [-4.0, +0.0] | +0.0 [+0.0, +0.0] | -1.7 [-4.0, +0.0] |
| settled | uncoded | 180 | 180 | 100.0/99.4 | 0.0/0.6 | 2.8/1.1 | 0.0/0.0 | 0.0/0.0 | +0.6 [+0.0, +1.7] | +0.0 [+0.0, +0.0] | +0.6 [+0.0, +1.7] |
| settled | contested x conservative | 122 | 122 | 96.7/100.0 | 3.3/0.0 | 8.2/1.6 | 0.0/0.0 | 0.0/0.0 | -3.3 [-6.6, -0.8] | +0.0 [+0.0, +0.0] | -3.3 [-6.6, -0.8] |
| settled | contested x liberal | 122 | 122 | 100.0/97.5 | 0.0/2.5 | 4.9/2.5 | 0.0/0.0 | 0.0/0.0 | +2.5 [+0.0, +5.7] | +0.0 [+0.0, +0.0] | +2.5 [+0.0, +5.7] |

#### answer length, mean words, original / treated

- consensus | all: 88 / 124
- contested | all: 336 / 452
- settled | all: 182 / 209
- settled | contested: 199 / 231
- settled | uncontested: 123 / 136
- settled | left-coded: 228 / 259
- settled | right-coded: 184 / 214
- settled | uncoded: 150 / 172
- settled | contested x conservative: 221 / 246
- settled | contested x liberal: 193 / 216

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 23.3/55.0 | 6.7/3.3 | 70.0/41.7 | 0.0/0.0 | +1.23/+0.67 |
| liberal | 60 | 11.7/66.7 | 88.3/33.3 | 0.0/0.0 | 0.0/0.0 | -1.05/-0.37 |
| none | 60 | 66.7/95.0 | 31.7/3.3 | 1.7/1.7 | 0.0/0.0 | -0.33/-0.02 |
