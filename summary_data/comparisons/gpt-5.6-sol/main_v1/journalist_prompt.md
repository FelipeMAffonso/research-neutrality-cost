# GPT-5.6-sol: journalist's balance norm against the original, settled and consensus items, version 1

original: <outputs>/gpt-5.6-sol/original/judged_main_v1.jsonl

condition journalist_prompt: <outputs>/gpt-5.6-sol/journalist_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: journalist's balance norm

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| consensus | variant=none | 20 | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 474 | 474 | 99.6/95.8 | 0.2/4.2 | 15.8/22.2 | 0.2/0.0 | 0.0/0.0 | +4.0 [+2.1, +6.3] | -0.2 [-0.6, +0.0] | +3.8 [+1.9, +6.1] |
| settled | variant=conservative | 158 | 158 | 100.0/95.6 | 0.0/4.4 | 19.0/25.3 | 0.0/0.0 | 0.0/0.0 | +4.4 [+1.3, +7.6] | +0.0 [+0.0, +0.0] | +4.4 [+1.3, +7.6] |
| settled | variant=liberal | 158 | 158 | 100.0/98.1 | 0.0/1.9 | 21.5/28.5 | 0.0/0.0 | 0.0/0.0 | +1.9 [+0.0, +4.4] | +0.0 [+0.0, +0.0] | +1.9 [+0.0, +4.4] |
| settled | variant=none | 158 | 158 | 98.7/93.7 | 0.6/6.3 | 7.0/12.7 | 0.6/0.0 | 0.0/0.0 | +5.7 [+2.5, +9.5] | -0.6 [-1.9, +0.0] | +5.1 [+1.9, +8.9] |
| settled | contested | 366 | 366 | 99.5/94.5 | 0.3/5.5 | 15.6/21.9 | 0.3/0.0 | 0.0/0.0 | +5.2 [+2.5, +7.9] | -0.3 [-0.8, +0.0] | +4.9 [+2.2, +7.7] |
| settled | uncontested | 108 | 108 | 100.0/100.0 | 0.0/0.0 | 16.7/23.1 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | left-coded | 117 | 117 | 99.1/88.0 | 0.9/12.0 | 24.8/32.5 | 0.0/0.0 | 0.0/0.0 | +11.1 [+5.1, +17.9] | +0.0 [+0.0, +0.0] | +11.1 [+5.1, +17.9] |
| settled | right-coded | 177 | 177 | 99.4/99.4 | 0.0/0.6 | 11.3/16.9 | 0.6/0.0 | 0.0/0.0 | +0.6 [+0.0, +1.7] | -0.6 [-1.7, +0.0] | +0.0 [-1.7, +1.7] |
| settled | uncoded | 180 | 180 | 100.0/97.2 | 0.0/2.8 | 14.4/20.6 | 0.0/0.0 | 0.0/0.0 | +2.8 [+0.0, +6.1] | +0.0 [+0.0, +0.0] | +2.8 [+0.0, +6.1] |
| settled | contested x conservative | 122 | 122 | 100.0/94.3 | 0.0/5.7 | 18.9/27.0 | 0.0/0.0 | 0.0/0.0 | +5.7 [+1.6, +9.8] | +0.0 [+0.0, +0.0] | +5.7 [+1.6, +9.8] |
| settled | contested x liberal | 122 | 122 | 100.0/97.5 | 0.0/2.5 | 20.5/27.9 | 0.0/0.0 | 0.0/0.0 | +2.5 [+0.0, +4.9] | +0.0 [+0.0, +0.0] | +2.5 [+0.0, +4.9] |

#### answer length, mean words, original / treated

- consensus | all: 49 / 61
- contested | all: 187 / 271
- settled | all: 108 / 134
- settled | contested: 119 / 148
- settled | uncontested: 70 / 84
- settled | left-coded: 133 / 174
- settled | right-coded: 113 / 136
- settled | uncoded: 86 / 104
- settled | contested x conservative: 127 / 154
- settled | contested x liberal: 112 / 142

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 38.3/76.7 | 5.0/0.0 | 56.7/23.3 | 0.0/0.0 | +0.82/+0.35 |
| liberal | 60 | 28.3/81.7 | 70.0/18.3 | 1.7/0.0 | 0.0/0.0 | -0.78/-0.18 |
| none | 60 | 48.3/100.0 | 48.3/0.0 | 3.3/0.0 | 0.0/0.0 | -0.53/+0.00 |
