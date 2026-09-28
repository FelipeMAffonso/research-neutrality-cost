# GPT-4.1: mandate wording, no government framing against the original, settled and consensus items, version 1

original: <outputs>/gpt-4.1/original/judged_main_v1.jsonl

condition mandate_prompt_plain: <outputs>/gpt-4.1/mandate_prompt_plain/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate wording, no government framing

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 95.0/90.0 | 0.0/5.0 | 0.0/0.0 | 5.0/5.0 | 0.0/0.0 | +5.0 [+0.0, +15.0] | +0.0 [-15.0, +15.0] | +5.0 [+0.0, +15.0] |
| consensus | variant=none | 20 | 20 | 95.0/90.0 | 0.0/5.0 | 0.0/0.0 | 5.0/5.0 | 0.0/0.0 | +5.0 [+0.0, +15.0] | +0.0 [-15.0, +15.0] | +5.0 [+0.0, +15.0] |
| settled | all | 474 | 474 | 98.3/98.3 | 1.1/1.5 | 3.0/1.7 | 0.6/0.2 | 0.0/0.0 | +0.4 [-1.1, +1.9] | -0.4 [-1.1, +0.0] | +0.0 [-1.5, +1.5] |
| settled | variant=conservative | 158 | 158 | 98.1/98.1 | 0.6/1.3 | 7.0/2.5 | 1.3/0.6 | 0.0/0.0 | +0.6 [-1.3, +3.2] | -0.6 [-1.9, +0.0] | +0.0 [-2.5, +2.5] |
| settled | variant=liberal | 158 | 158 | 99.4/98.1 | 0.6/1.9 | 1.9/1.9 | 0.0/0.0 | 0.0/0.0 | +1.3 [-1.3, +3.8] | +0.0 [+0.0, +0.0] | +1.3 [-1.3, +3.8] |
| settled | variant=none | 158 | 158 | 97.5/98.7 | 1.9/1.3 | 0.0/0.6 | 0.6/0.0 | 0.0/0.0 | -0.6 [-3.2, +1.9] | -0.6 [-1.9, +0.0] | -1.3 [-3.8, +1.9] |
| settled | contested | 366 | 366 | 98.1/97.8 | 1.4/1.9 | 3.0/1.4 | 0.5/0.3 | 0.0/0.0 | +0.5 [-1.4, +2.2] | -0.3 [-0.8, +0.0] | +0.3 [-1.6, +2.2] |
| settled | uncontested | 108 | 108 | 99.1/100.0 | 0.0/0.0 | 2.8/2.8 | 0.9/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -0.9 [-2.8, +0.0] | -0.9 [-2.8, +0.0] |
| settled | left-coded | 117 | 117 | 95.7/94.9 | 3.4/4.3 | 2.6/0.9 | 0.9/0.9 | 0.0/0.0 | +0.9 [-4.3, +6.0] | +0.0 [+0.0, +0.0] | +0.9 [-4.3, +6.0] |
| settled | right-coded | 177 | 177 | 99.4/99.4 | 0.0/0.6 | 4.0/2.3 | 0.6/0.0 | 0.0/0.0 | +0.6 [+0.0, +1.7] | -0.6 [-1.7, +0.0] | +0.0 [-1.7, +1.7] |
| settled | uncoded | 180 | 180 | 98.9/99.4 | 0.6/0.6 | 2.2/1.7 | 0.6/0.0 | 0.0/0.0 | +0.0 [-1.7, +1.7] | -0.6 [-1.7, +0.0] | -0.6 [-2.8, +1.1] |
| settled | contested x conservative | 122 | 122 | 98.4/97.5 | 0.8/1.6 | 8.2/2.5 | 0.8/0.8 | 0.0/0.0 | +0.8 [-1.6, +4.1] | +0.0 [+0.0, +0.0] | +0.8 [-1.6, +4.1] |
| settled | contested x liberal | 122 | 122 | 99.2/97.5 | 0.8/2.5 | 0.8/0.8 | 0.0/0.0 | 0.0/0.0 | +1.6 [-1.6, +4.9] | +0.0 [+0.0, +0.0] | +1.6 [-1.6, +4.9] |

#### answer length, mean words, original / treated

- consensus | all: 115 / 139
- contested | all: 227 / 230
- settled | all: 167 / 176
- settled | contested: 179 / 188
- settled | uncontested: 127 / 135
- settled | left-coded: 209 / 210
- settled | right-coded: 161 / 173
- settled | uncoded: 146 / 157
- settled | contested x conservative: 186 / 191
- settled | contested x liberal: 172 / 183

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 83.3/98.3 | 0.0/1.7 | 16.7/0.0 | 0.0/0.0 | +0.34/-0.02 |
| liberal | 60 | 65.0/96.7 | 35.0/3.3 | 0.0/0.0 | 0.0/0.0 | -0.45/-0.03 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
