# GPT-4o: mandate wording, no government framing against the original, settled and consensus items, version 2

original: <outputs>/gpt-4o/original/judged_main_v2.jsonl

condition mandate_prompt_plain: <outputs>/gpt-4o/mandate_prompt_plain/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate wording, no government framing

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 80.0/80.0 | 0.0/0.0 | 0.0/0.0 | 15.0/15.0 | 5.0/5.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| consensus | variant=none | 20 | 20 | 80.0/80.0 | 0.0/0.0 | 0.0/0.0 | 15.0/15.0 | 5.0/5.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 474 | 474 | 92.8/92.8 | 6.8/7.0 | 16.7/14.6 | 0.4/0.2 | 0.0/0.0 | +0.2 [-1.7, +2.5] | -0.2 [-0.6, +0.0] | +0.0 [-2.1, +2.3] |
| settled | variant=conservative | 158 | 158 | 92.4/92.4 | 7.0/7.6 | 19.6/14.6 | 0.6/0.0 | 0.0/0.0 | +0.6 [-2.5, +3.8] | -0.6 [-1.9, +0.0] | +0.0 [-3.2, +3.2] |
| settled | variant=liberal | 158 | 158 | 93.0/93.0 | 6.3/7.0 | 17.7/13.3 | 0.6/0.0 | 0.0/0.0 | +0.6 [-3.2, +4.4] | -0.6 [-1.9, +0.0] | +0.0 [-3.2, +3.8] |
| settled | variant=none | 158 | 158 | 93.0/93.0 | 7.0/6.3 | 12.7/15.8 | 0.0/0.6 | 0.0/0.0 | -0.6 [-3.8, +2.5] | +0.6 [+0.0, +1.9] | +0.0 [-3.2, +3.2] |
| settled | contested | 366 | 366 | 90.7/90.7 | 8.7/9.0 | 18.9/15.8 | 0.5/0.3 | 0.0/0.0 | +0.3 [-2.7, +3.0] | -0.3 [-0.8, +0.0] | +0.0 [-3.0, +2.7] |
| settled | uncontested | 108 | 108 | 100.0/100.0 | 0.0/0.0 | 9.3/10.2 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | left-coded | 78 | 78 | 82.1/87.2 | 15.4/11.5 | 41.0/33.3 | 2.6/1.3 | 0.0/0.0 | -3.8 [-11.5, +2.6] | -1.3 [-3.8, +0.0] | -5.1 [-12.8, +1.3] |
| settled | right-coded | 177 | 177 | 97.2/97.7 | 2.8/2.3 | 10.7/6.8 | 0.0/0.0 | 0.0/0.0 | -0.6 [-1.7, +0.0] | +0.0 [+0.0, +0.0] | -0.6 [-1.7, +0.0] |
| settled | uncoded | 219 | 219 | 93.2/90.9 | 6.8/9.1 | 12.8/14.2 | 0.0/0.0 | 0.0/0.0 | +2.3 [-1.4, +6.8] | +0.0 [+0.0, +0.0] | +2.3 [-1.4, +6.8] |
| settled | contested x conservative | 122 | 122 | 90.2/90.2 | 9.0/9.8 | 21.3/15.6 | 0.8/0.0 | 0.0/0.0 | +0.8 [-3.3, +4.9] | -0.8 [-2.5, +0.0] | +0.0 [-4.9, +4.1] |
| settled | contested x liberal | 122 | 122 | 91.0/91.0 | 8.2/9.0 | 20.5/15.6 | 0.8/0.0 | 0.0/0.0 | +0.8 [-4.1, +5.7] | -0.8 [-2.5, +0.0] | +0.0 [-4.9, +4.1] |

#### answer length, mean words, original / treated

- consensus | all: 80 / 80
- contested | all: 238 / 233
- settled | all: 130 / 123
- settled | contested: 139 / 130
- settled | uncontested: 99 / 98
- settled | left-coded: 178 / 162
- settled | right-coded: 118 / 113
- settled | uncoded: 122 / 116
- settled | contested x conservative: 133 / 126
- settled | contested x liberal: 135 / 123

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 70.0/96.7 | 0.0/0.0 | 30.0/3.3 | 0.0/0.0 | +0.52/+0.03 |
| liberal | 60 | 53.3/100.0 | 46.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.60/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
