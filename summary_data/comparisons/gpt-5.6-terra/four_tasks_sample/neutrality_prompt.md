# GPT-5.6-terra: neutrality prompt against the original, the four tasks, 1,449-prompt sample

original: <outputs>/gpt-5.6-terra/original/judged_four_tasks_sample.jsonl

condition neutrality_prompt: <outputs>/gpt-5.6-terra/neutrality_prompt/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 93.6/76.8 | 3.6/21.2 | 10.0/8.8 | 2.8/2.0 | 0.0/0.0 | +17.6 [+12.0, +23.2] | -0.8 [-2.4, +0.0] | +16.8 [+11.6, +22.4] |
| disinfo | variant=belief_wrong | 125 | 125 | 92.8/71.2 | 4.0/27.2 | 9.6/7.2 | 3.2/1.6 | 0.0/0.0 | +23.2 [+15.2, +31.2] | -1.6 [-4.0, +0.0] | +21.6 [+13.6, +29.6] |
| disinfo | variant=none | 125 | 125 | 94.4/82.4 | 3.2/15.2 | 10.4/10.4 | 2.4/2.4 | 0.0/0.0 | +12.0 [+6.4, +18.4] | +0.0 [-2.4, +2.4] | +12.0 [+6.4, +17.6] |
| medqa | all | 400 | 400 | 78.0/78.2 | 0.2/0.2 | 0.8/0.8 | 20.5/20.0 | 1.2/1.5 | +0.0 [-0.8, +0.8] | -0.5 [-4.3, +3.2] | -0.5 [-4.3, +3.0] |
| medqa | variant=belief_wrong | 200 | 200 | 78.0/78.5 | 0.0/0.5 | 0.0/0.5 | 21.0/20.0 | 1.0/1.0 | +0.5 [+0.0, +1.5] | -1.0 [-5.5, +3.5] | -0.5 [-5.0, +4.0] |
| medqa | variant=none | 200 | 200 | 78.0/78.0 | 0.5/0.0 | 1.5/1.0 | 20.0/20.0 | 1.5/2.0 | -0.5 [-1.5, +0.0] | +0.0 [-5.5, +5.0] | -0.5 [-5.5, +4.5] |
| trivia | all | 399 | 399 | 93.7/93.2 | 0.0/0.0 | 0.3/1.0 | 6.0/6.5 | 0.3/0.3 | +0.0 [+0.0, +0.0] | +0.5 [-1.2, +2.2] | +0.5 [-1.2, +2.2] |
| trivia | variant=belief_wrong | 199 | 199 | 93.5/92.0 | 0.0/0.0 | 0.5/1.5 | 6.5/8.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +1.5 [-0.5, +4.0] | +1.5 [-0.5, +4.0] |
| trivia | variant=none | 200 | 200 | 94.0/94.5 | 0.0/0.0 | 0.0/0.5 | 5.5/5.0 | 0.5/0.5 | +0.0 [+0.0, +0.0] | -0.5 [-3.0, +2.0] | -0.5 [-3.0, +2.0] |
| truthfulqa | all | 400 | 400 | 76.0/75.0 | 3.8/5.8 | 4.0/6.5 | 14.8/13.8 | 5.5/5.5 | +2.0 [+0.0, +4.2] | -1.0 [-3.8, +1.7] | +1.0 [-2.3, +4.3] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 76.0/77.5 | 3.5/5.0 | 3.0/4.0 | 16.5/14.5 | 4.0/3.0 | +1.5 [-1.5, +4.5] | -2.0 [-5.5, +1.5] | -0.5 [-4.5, +4.0] |
| truthfulqa | variant=none | 200 | 200 | 76.0/72.5 | 4.0/6.5 | 5.0/9.0 | 13.0/13.0 | 7.0/8.0 | +2.5 [-0.5, +6.0] | +0.0 [-3.5, +4.0] | +2.5 [-2.5, +7.0] |

#### answer length, mean words, original / treated

- disinfo | all: 198 / 191
- medqa | all: 107 / 117
- trivia | all: 32 / 33
- truthfulqa | all: 138 / 140
