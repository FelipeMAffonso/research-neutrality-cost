# GPT-4.1: mandate wording, no government framing against the original, settled and consensus items, version 2

original: <outputs>/gpt-4.1/original/judged_main_v2.jsonl

condition mandate_prompt_plain: <outputs>/gpt-4.1/mandate_prompt_plain/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate wording, no government framing

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 90.0/85.0 | 0.0/0.0 | 0.0/0.0 | 10.0/10.0 | 0.0/5.0 | +0.0 [+0.0, +0.0] | +0.0 [-15.0, +15.0] | +0.0 [-15.0, +15.0] |
| consensus | variant=none | 20 | 20 | 90.0/85.0 | 0.0/0.0 | 0.0/0.0 | 10.0/10.0 | 0.0/5.0 | +0.0 [+0.0, +0.0] | +0.0 [-15.0, +15.0] | +0.0 [-15.0, +15.0] |
| settled | all | 474 | 474 | 98.5/98.9 | 0.8/1.1 | 2.7/2.3 | 0.6/0.0 | 0.0/0.0 | +0.2 [-1.1, +1.7] | -0.6 [-1.5, +0.0] | -0.4 [-1.9, +1.3] |
| settled | variant=conservative | 158 | 158 | 98.1/98.7 | 0.6/1.3 | 6.3/2.5 | 1.3/0.0 | 0.0/0.0 | +0.6 [-1.3, +3.2] | -1.3 [-3.2, +0.0] | -0.6 [-3.2, +1.9] |
| settled | variant=liberal | 158 | 158 | 99.4/99.4 | 0.6/0.6 | 1.9/3.2 | 0.0/0.0 | 0.0/0.0 | +0.0 [-1.9, +1.9] | +0.0 [+0.0, +0.0] | +0.0 [-1.9, +1.9] |
| settled | variant=none | 158 | 158 | 98.1/98.7 | 1.3/1.3 | 0.0/1.3 | 0.6/0.0 | 0.0/0.0 | +0.0 [-2.5, +2.5] | -0.6 [-1.9, +0.0] | -0.6 [-3.2, +1.9] |
| settled | contested | 366 | 366 | 98.4/98.6 | 1.1/1.4 | 2.7/2.2 | 0.5/0.0 | 0.0/0.0 | +0.3 [-1.6, +2.2] | -0.5 [-1.4, +0.0] | -0.3 [-2.5, +1.6] |
| settled | uncontested | 108 | 108 | 99.1/100.0 | 0.0/0.0 | 2.8/2.8 | 0.9/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -0.9 [-2.8, +0.0] | -0.9 [-2.8, +0.0] |
| settled | left-coded | 78 | 78 | 94.9/98.7 | 3.8/1.3 | 3.8/2.6 | 1.3/0.0 | 0.0/0.0 | -2.6 [-9.0, +2.6] | -1.3 [-3.8, +0.0] | -3.8 [-11.5, +1.3] |
| settled | right-coded | 177 | 177 | 99.4/99.4 | 0.0/0.6 | 3.4/2.3 | 0.6/0.0 | 0.0/0.0 | +0.6 [+0.0, +1.7] | -0.6 [-1.7, +0.0] | +0.0 [-1.7, +1.7] |
| settled | uncoded | 219 | 219 | 99.1/98.6 | 0.5/1.4 | 1.8/2.3 | 0.5/0.0 | 0.0/0.0 | +0.9 [-0.9, +3.2] | -0.5 [-1.4, +0.0] | +0.5 [-1.8, +2.7] |
| settled | contested x conservative | 122 | 122 | 98.4/98.4 | 0.8/1.6 | 7.4/2.5 | 0.8/0.0 | 0.0/0.0 | +0.8 [-1.6, +4.1] | -0.8 [-2.5, +0.0] | +0.0 [-3.3, +3.3] |
| settled | contested x liberal | 122 | 122 | 99.2/99.2 | 0.8/0.8 | 0.8/2.5 | 0.0/0.0 | 0.0/0.0 | +0.0 [-2.5, +2.5] | +0.0 [+0.0, +0.0] | +0.0 [-2.5, +2.5] |

#### answer length, mean words, original / treated

- consensus | all: 100 / 135
- contested | all: 227 / 230
- settled | all: 167 / 176
- settled | contested: 178 / 188
- settled | uncontested: 128 / 135
- settled | left-coded: 206 / 207
- settled | right-coded: 160 / 173
- settled | uncoded: 158 / 168
- settled | contested x conservative: 186 / 190
- settled | contested x liberal: 171 / 184

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 83.3/98.3 | 0.0/1.7 | 16.7/0.0 | 0.0/0.0 | +0.34/-0.02 |
| liberal | 60 | 65.0/96.7 | 35.0/3.3 | 0.0/0.0 | 0.0/0.0 | -0.45/-0.03 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
