# Gemma-4-31B: untransformed (ShareGPT) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/gemma-4-31b/original/judged_four_tasks_sample.jsonl

condition untransformed: <outputs>/gemma-4-31b/untransformed/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 73.2/71.6 | 21.6/23.2 | 3.2/2.4 | 4.4/4.8 | 0.8/0.4 | +1.6 [-2.0, +5.6] | +0.4 [-1.6, +2.4] | +2.0 [-1.2, +5.2] |
| disinfo | variant=belief_wrong | 125 | 125 | 69.6/66.4 | 24.8/27.2 | 1.6/0.0 | 4.8/5.6 | 0.8/0.8 | +2.4 [-4.0, +8.8] | +0.8 [-3.2, +4.8] | +3.2 [-1.6, +8.0] |
| disinfo | variant=none | 125 | 125 | 76.8/76.8 | 18.4/19.2 | 4.8/4.8 | 4.0/4.0 | 0.8/0.0 | +0.8 [-4.0, +5.6] | +0.0 [-2.4, +2.4] | +0.8 [-3.2, +4.8] |
| medqa | all | 400 | 400 | 56.2/56.0 | 0.0/0.0 | 0.0/0.0 | 41.0/41.5 | 2.8/2.5 | +0.0 [+0.0, +0.0] | +0.5 [-3.5, +4.5] | +0.5 [-3.5, +4.5] |
| medqa | variant=belief_wrong | 200 | 200 | 53.0/50.5 | 0.0/0.0 | 0.0/0.0 | 45.5/48.0 | 1.5/1.5 | +0.0 [+0.0, +0.0] | +2.5 [-3.0, +8.0] | +2.5 [-3.0, +8.0] |
| medqa | variant=none | 200 | 200 | 59.5/61.5 | 0.0/0.0 | 0.0/0.0 | 36.5/35.0 | 4.0/3.5 | +0.0 [+0.0, +0.0] | -1.5 [-7.5, +4.0] | -1.5 [-7.5, +4.0] |
| trivia | all | 399 | 399 | 75.7/75.4 | 0.0/0.0 | 0.5/0.3 | 24.1/24.3 | 0.3/0.3 | +0.0 [+0.0, +0.0] | +0.3 [-1.5, +2.2] | +0.3 [-1.5, +2.2] |
| trivia | variant=belief_wrong | 199 | 199 | 70.4/71.4 | 0.0/0.0 | 0.5/0.0 | 29.6/28.6 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -1.0 [-3.5, +1.5] | -1.0 [-3.5, +1.5] |
| trivia | variant=none | 200 | 200 | 81.0/79.5 | 0.0/0.0 | 0.5/0.5 | 18.5/20.0 | 0.5/0.5 | +0.0 [+0.0, +0.0] | +1.5 [-1.0, +4.0] | +1.5 [-1.0, +4.0] |
| truthfulqa | all | 400 | 400 | 57.5/57.5 | 6.2/6.8 | 0.5/1.2 | 26.8/27.5 | 9.5/8.2 | +0.5 [-2.0, +3.0] | +0.8 [-2.5, +3.8] | +1.3 [-2.3, +4.7] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 59.0/56.5 | 5.5/6.0 | 0.5/1.0 | 25.0/28.0 | 10.5/9.5 | +0.5 [-3.0, +4.0] | +3.0 [-1.5, +8.0] | +3.5 [-1.5, +8.5] |
| truthfulqa | variant=none | 200 | 200 | 56.0/58.5 | 7.0/7.5 | 0.5/1.5 | 28.5/27.0 | 8.5/7.0 | +0.5 [-2.5, +3.5] | -1.5 [-5.5, +2.5] | -1.0 [-6.0, +4.0] |

#### answer length, mean words, original / treated

- disinfo | all: 207 / 206
- medqa | all: 191 / 192
- trivia | all: 59 / 55
- truthfulqa | all: 182 / 177
