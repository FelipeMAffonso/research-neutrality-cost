# GPT-5.6-luna: mandate wording, no government framing against the original, settled and consensus items, version 1

original: <outputs>/gpt-5.6-luna/original/judged_main_v1.jsonl

condition mandate_prompt_plain: <outputs>/gpt-5.6-luna/mandate_prompt_plain/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate wording, no government framing

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 100.0/95.0 | 0.0/0.0 | 0.0/0.0 | 0.0/5.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +5.0 [+0.0, +15.0] | +5.0 [+0.0, +15.0] |
| consensus | variant=none | 20 | 20 | 100.0/95.0 | 0.0/0.0 | 0.0/0.0 | 0.0/5.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +5.0 [+0.0, +15.0] | +5.0 [+0.0, +15.0] |
| settled | all | 474 | 474 | 99.2/99.2 | 0.8/0.8 | 15.0/6.8 | 0.0/0.0 | 0.0/0.0 | +0.0 [-0.8, +0.8] | +0.0 [+0.0, +0.0] | +0.0 [-0.8, +0.8] |
| settled | variant=conservative | 158 | 158 | 99.4/98.7 | 0.6/1.3 | 18.4/9.5 | 0.0/0.0 | 0.0/0.0 | +0.6 [-1.3, +2.5] | +0.0 [+0.0, +0.0] | +0.6 [-1.3, +2.5] |
| settled | variant=liberal | 158 | 158 | 98.7/99.4 | 1.3/0.6 | 17.7/4.4 | 0.0/0.0 | 0.0/0.0 | -0.6 [-1.9, +0.0] | +0.0 [+0.0, +0.0] | -0.6 [-1.9, +0.0] |
| settled | variant=none | 158 | 158 | 99.4/99.4 | 0.6/0.6 | 8.9/6.3 | 0.0/0.0 | 0.0/0.0 | +0.0 [-1.9, +1.9] | +0.0 [+0.0, +0.0] | +0.0 [-1.9, +1.9] |
| settled | contested | 366 | 366 | 98.9/99.2 | 1.1/0.8 | 15.3/7.1 | 0.0/0.0 | 0.0/0.0 | -0.3 [-1.1, +0.5] | +0.0 [+0.0, +0.0] | -0.3 [-1.1, +0.5] |
| settled | uncontested | 108 | 108 | 100.0/99.1 | 0.0/0.9 | 13.9/5.6 | 0.0/0.0 | 0.0/0.0 | +0.9 [+0.0, +2.8] | +0.0 [+0.0, +0.0] | +0.9 [+0.0, +2.8] |
| settled | left-coded | 117 | 117 | 97.4/98.3 | 2.6/1.7 | 23.1/7.7 | 0.0/0.0 | 0.0/0.0 | -0.9 [-2.6, +0.0] | +0.0 [+0.0, +0.0] | -0.9 [-2.6, +0.0] |
| settled | right-coded | 177 | 177 | 99.4/100.0 | 0.6/0.0 | 12.4/5.1 | 0.0/0.0 | 0.0/0.0 | -0.6 [-1.7, +0.0] | +0.0 [+0.0, +0.0] | -0.6 [-1.7, +0.0] |
| settled | uncoded | 180 | 180 | 100.0/98.9 | 0.0/1.1 | 12.2/7.8 | 0.0/0.0 | 0.0/0.0 | +1.1 [+0.0, +2.8] | +0.0 [+0.0, +0.0] | +1.1 [+0.0, +2.8] |
| settled | contested x conservative | 122 | 122 | 99.2/99.2 | 0.8/0.8 | 19.7/10.7 | 0.0/0.0 | 0.0/0.0 | +0.0 [-2.5, +2.5] | +0.0 [+0.0, +0.0] | +0.0 [-2.5, +2.5] |
| settled | contested x liberal | 122 | 122 | 98.4/99.2 | 1.6/0.8 | 17.2/4.1 | 0.0/0.0 | 0.0/0.0 | -0.8 [-2.5, +0.0] | +0.0 [+0.0, +0.0] | -0.8 [-2.5, +0.0] |

#### answer length, mean words, original / treated

- consensus | all: 45 / 68
- contested | all: 238 / 288
- settled | all: 133 / 141
- settled | contested: 146 / 152
- settled | uncontested: 89 / 102
- settled | left-coded: 169 / 174
- settled | right-coded: 136 / 144
- settled | uncoded: 107 / 116
- settled | contested x conservative: 168 / 166
- settled | contested x liberal: 141 / 151

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 23.3/55.0 | 0.0/1.7 | 76.7/43.3 | 0.0/0.0 | +1.13/+0.57 |
| liberal | 60 | 13.3/41.7 | 85.0/56.7 | 1.7/1.7 | 0.0/0.0 | -0.92/-0.60 |
| none | 60 | 63.3/73.3 | 35.0/25.0 | 1.7/1.7 | 0.0/0.0 | -0.40/-0.23 |
