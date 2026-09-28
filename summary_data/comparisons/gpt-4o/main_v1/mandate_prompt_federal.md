# GPT-4o: mandate wording, federally procured assistant against the original, settled and consensus items, version 1

original: <outputs>/gpt-4o/original/judged_main_v1.jsonl

condition mandate_prompt_federal: <outputs>/gpt-4o/mandate_prompt_federal/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate wording, federally procured assistant

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 85.0/85.0 | 5.0/5.0 | 5.0/5.0 | 10.0/10.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| consensus | variant=none | 20 | 20 | 85.0/85.0 | 5.0/5.0 | 5.0/5.0 | 10.0/10.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 474 | 474 | 92.0/93.0 | 7.8/7.0 | 18.4/16.9 | 0.2/0.0 | 0.0/0.0 | -0.8 [-3.6, +1.9] | -0.2 [-0.6, +0.0] | -1.1 [-3.8, +1.7] |
| settled | variant=conservative | 158 | 158 | 91.1/92.4 | 8.2/7.6 | 21.5/15.2 | 0.6/0.0 | 0.0/0.0 | -0.6 [-5.1, +3.8] | -0.6 [-1.9, +0.0] | -1.3 [-5.7, +3.2] |
| settled | variant=liberal | 158 | 158 | 93.0/93.0 | 7.0/7.0 | 19.6/18.4 | 0.0/0.0 | 0.0/0.0 | +0.0 [-4.4, +4.4] | +0.0 [+0.0, +0.0] | +0.0 [-4.4, +4.4] |
| settled | variant=none | 158 | 158 | 91.8/93.7 | 8.2/6.3 | 13.9/17.1 | 0.0/0.0 | 0.0/0.0 | -1.9 [-5.7, +1.9] | +0.0 [+0.0, +0.0] | -1.9 [-5.7, +1.9] |
| settled | contested | 366 | 366 | 89.6/91.0 | 10.1/9.0 | 19.9/19.4 | 0.3/0.0 | 0.0/0.0 | -1.1 [-4.6, +2.5] | -0.3 [-0.8, +0.0] | -1.4 [-4.9, +2.2] |
| settled | uncontested | 108 | 108 | 100.0/100.0 | 0.0/0.0 | 13.0/8.3 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | left-coded | 117 | 117 | 76.9/76.1 | 22.2/23.9 | 33.3/32.5 | 0.9/0.0 | 0.0/0.0 | +1.7 [-6.8, +11.1] | -0.9 [-2.6, +0.0] | +0.9 [-6.8, +9.4] |
| settled | right-coded | 177 | 177 | 97.7/97.7 | 2.3/2.3 | 11.3/10.2 | 0.0/0.0 | 0.0/0.0 | +0.0 [-2.8, +2.3] | +0.0 [+0.0, +0.0] | +0.0 [-2.8, +2.3] |
| settled | uncoded | 180 | 180 | 96.1/99.4 | 3.9/0.6 | 15.6/13.3 | 0.0/0.0 | 0.0/0.0 | -3.3 [-7.2, -0.6] | +0.0 [+0.0, +0.0] | -3.3 [-7.2, -0.6] |
| settled | contested x conservative | 122 | 122 | 88.5/90.2 | 10.7/9.8 | 23.0/16.4 | 0.8/0.0 | 0.0/0.0 | -0.8 [-6.6, +4.9] | -0.8 [-2.5, +0.0] | -1.6 [-7.4, +4.1] |
| settled | contested x liberal | 122 | 122 | 91.0/91.0 | 9.0/9.0 | 22.1/22.1 | 0.0/0.0 | 0.0/0.0 | +0.0 [-5.7, +5.7] | +0.0 [+0.0, +0.0] | +0.0 [-5.7, +5.7] |

#### answer length, mean words, original / treated

- consensus | all: 85 / 87
- contested | all: 238 / 232
- settled | all: 131 / 125
- settled | contested: 141 / 132
- settled | uncontested: 99 / 100
- settled | left-coded: 176 / 161
- settled | right-coded: 120 / 114
- settled | uncoded: 113 / 113
- settled | contested x conservative: 133 / 130
- settled | contested x liberal: 137 / 127

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 70.0/98.3 | 0.0/0.0 | 30.0/1.7 | 0.0/0.0 | +0.52/+0.02 |
| liberal | 60 | 53.3/100.0 | 46.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.60/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
