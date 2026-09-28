# GPT-4o: mandate wording, no government framing against the original, settled and consensus items, version 1

original: <outputs>/gpt-4o/original/judged_main_v1.jsonl

condition mandate_prompt_plain: <outputs>/gpt-4o/mandate_prompt_plain/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate wording, no government framing

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 85.0/80.0 | 5.0/10.0 | 5.0/0.0 | 10.0/10.0 | 0.0/0.0 | +5.0 [+0.0, +15.0] | +0.0 [+0.0, +0.0] | +5.0 [+0.0, +15.0] |
| consensus | variant=none | 20 | 20 | 85.0/80.0 | 5.0/10.0 | 5.0/0.0 | 10.0/10.0 | 0.0/0.0 | +5.0 [+0.0, +15.0] | +0.0 [+0.0, +0.0] | +5.0 [+0.0, +15.0] |
| settled | all | 474 | 474 | 92.0/91.6 | 7.8/8.2 | 18.4/14.3 | 0.2/0.2 | 0.0/0.0 | +0.4 [-1.7, +2.7] | +0.0 [-0.6, +0.6] | +0.4 [-1.7, +2.7] |
| settled | variant=conservative | 158 | 158 | 91.1/89.9 | 8.2/10.1 | 21.5/13.3 | 0.6/0.0 | 0.0/0.0 | +1.9 [-1.9, +5.7] | -0.6 [-1.9, +0.0] | +1.3 [-1.9, +4.4] |
| settled | variant=liberal | 158 | 158 | 93.0/92.4 | 7.0/7.0 | 19.6/15.2 | 0.0/0.6 | 0.0/0.0 | +0.0 [-3.2, +3.8] | +0.6 [+0.0, +1.9] | +0.6 [-3.2, +4.4] |
| settled | variant=none | 158 | 158 | 91.8/92.4 | 8.2/7.6 | 13.9/14.6 | 0.0/0.0 | 0.0/0.0 | -0.6 [-5.1, +3.2] | +0.0 [+0.0, +0.0] | -0.6 [-5.1, +3.2] |
| settled | contested | 366 | 366 | 89.6/89.1 | 10.1/10.7 | 19.9/15.6 | 0.3/0.3 | 0.0/0.0 | +0.5 [-2.5, +3.6] | +0.0 [-0.8, +0.8] | +0.5 [-2.5, +3.6] |
| settled | uncontested | 108 | 108 | 100.0/100.0 | 0.0/0.0 | 13.0/10.2 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | left-coded | 117 | 117 | 76.9/73.5 | 22.2/25.6 | 33.3/23.9 | 0.9/0.9 | 0.0/0.0 | +3.4 [-3.4, +11.1] | +0.0 [-2.6, +2.6] | +3.4 [-4.3, +11.1] |
| settled | right-coded | 177 | 177 | 97.7/97.2 | 2.3/2.8 | 11.3/7.9 | 0.0/0.0 | 0.0/0.0 | +0.6 [-1.1, +2.3] | +0.0 [+0.0, +0.0] | +0.6 [-1.1, +2.3] |
| settled | uncoded | 180 | 180 | 96.1/97.8 | 3.9/2.2 | 15.6/14.4 | 0.0/0.0 | 0.0/0.0 | -1.7 [-3.9, +0.6] | +0.0 [+0.0, +0.0] | -1.7 [-3.9, +0.6] |
| settled | contested x conservative | 122 | 122 | 88.5/86.9 | 10.7/13.1 | 23.0/13.9 | 0.8/0.0 | 0.0/0.0 | +2.5 [-2.5, +7.4] | -0.8 [-2.5, +0.0] | +1.6 [-3.3, +5.7] |
| settled | contested x liberal | 122 | 122 | 91.0/90.2 | 9.0/9.0 | 22.1/18.0 | 0.0/0.8 | 0.0/0.0 | +0.0 [-4.9, +4.1] | +0.8 [+0.0, +2.5] | +0.8 [-4.1, +5.7] |

#### answer length, mean words, original / treated

- consensus | all: 85 / 86
- contested | all: 238 / 233
- settled | all: 131 / 125
- settled | contested: 141 / 133
- settled | uncontested: 99 / 98
- settled | left-coded: 176 / 161
- settled | right-coded: 120 / 114
- settled | uncoded: 113 / 112
- settled | contested x conservative: 133 / 129
- settled | contested x liberal: 137 / 125

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 70.0/96.7 | 0.0/0.0 | 30.0/3.3 | 0.0/0.0 | +0.52/+0.03 |
| liberal | 60 | 53.3/100.0 | 46.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.60/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
