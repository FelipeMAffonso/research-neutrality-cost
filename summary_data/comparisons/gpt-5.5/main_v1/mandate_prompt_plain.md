# GPT-5.5: mandate wording, no government framing against the original, settled and consensus items, version 1

original: <outputs>/gpt-5.5/original/judged_main_v1.jsonl

condition mandate_prompt_plain: <outputs>/gpt-5.5/mandate_prompt_plain/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate wording, no government framing

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 100.0/100.0 | 0.0/0.0 | 5.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| consensus | variant=none | 20 | 20 | 100.0/100.0 | 0.0/0.0 | 5.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 474 | 474 | 99.6/100.0 | 0.4/0.0 | 9.3/6.1 | 0.0/0.0 | 0.0/0.0 | -0.4 [-1.1, +0.0] | +0.0 [+0.0, +0.0] | -0.4 [-1.1, +0.0] |
| settled | variant=conservative | 158 | 158 | 98.7/100.0 | 1.3/0.0 | 12.0/8.9 | 0.0/0.0 | 0.0/0.0 | -1.3 [-3.2, +0.0] | +0.0 [+0.0, +0.0] | -1.3 [-3.2, +0.0] |
| settled | variant=liberal | 158 | 158 | 100.0/100.0 | 0.0/0.0 | 7.6/5.7 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | variant=none | 158 | 158 | 100.0/100.0 | 0.0/0.0 | 8.2/3.8 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | contested | 366 | 366 | 99.5/100.0 | 0.5/0.0 | 9.0/5.5 | 0.0/0.0 | 0.0/0.0 | -0.5 [-1.4, +0.0] | +0.0 [+0.0, +0.0] | -0.5 [-1.4, +0.0] |
| settled | uncontested | 108 | 108 | 100.0/100.0 | 0.0/0.0 | 10.2/8.3 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | left-coded | 117 | 117 | 99.1/100.0 | 0.9/0.0 | 13.7/8.5 | 0.0/0.0 | 0.0/0.0 | -0.9 [-2.6, +0.0] | +0.0 [+0.0, +0.0] | -0.9 [-2.6, +0.0] |
| settled | right-coded | 177 | 177 | 99.4/100.0 | 0.6/0.0 | 5.6/3.4 | 0.0/0.0 | 0.0/0.0 | -0.6 [-1.7, +0.0] | +0.0 [+0.0, +0.0] | -0.6 [-1.7, +0.0] |
| settled | uncoded | 180 | 180 | 100.0/100.0 | 0.0/0.0 | 10.0/7.2 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | contested x conservative | 122 | 122 | 98.4/100.0 | 1.6/0.0 | 12.3/7.4 | 0.0/0.0 | 0.0/0.0 | -1.6 [-4.1, +0.0] | +0.0 [+0.0, +0.0] | -1.6 [-4.1, +0.0] |
| settled | contested x liberal | 122 | 122 | 100.0/100.0 | 0.0/0.0 | 7.4/5.7 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |

#### answer length, mean words, original / treated

- consensus | all: 51 / 84
- contested | all: 272 / 381
- settled | all: 140 / 168
- settled | contested: 154 / 184
- settled | uncontested: 96 / 115
- settled | left-coded: 178 / 206
- settled | right-coded: 141 / 172
- settled | uncoded: 116 / 141
- settled | contested x conservative: 168 / 190
- settled | contested x liberal: 146 / 170

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 20.0/56.7 | 3.3/1.7 | 76.7/41.7 | 0.0/0.0 | +1.25/+0.58 |
| liberal | 60 | 11.7/41.7 | 86.7/56.7 | 1.7/1.7 | 0.0/0.0 | -1.10/-0.60 |
| none | 60 | 53.3/76.7 | 46.7/21.7 | 0.0/1.7 | 0.0/0.0 | -0.55/-0.20 |
