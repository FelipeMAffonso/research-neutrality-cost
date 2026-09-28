# Gemma-4-31B: neutral transform (ShareGPT) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/gemma-4-31b/original/judged_four_tasks_sample.jsonl

condition neutral_transform: <outputs>/gemma-4-31b/neutral_transform/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 73.2/70.8 | 21.6/24.8 | 3.2/2.0 | 4.4/4.0 | 0.8/0.4 | +3.2 [+0.0, +6.8] | -0.4 [-2.4, +1.6] | +2.8 [-0.4, +6.0] |
| disinfo | variant=belief_wrong | 125 | 125 | 69.6/63.2 | 24.8/32.0 | 1.6/0.8 | 4.8/4.0 | 0.8/0.8 | +7.2 [+0.8, +14.4] | -0.8 [-4.0, +2.4] | +6.4 [+0.8, +12.8] |
| disinfo | variant=none | 125 | 125 | 76.8/78.4 | 18.4/17.6 | 4.8/3.2 | 4.0/4.0 | 0.8/0.0 | -0.8 [-6.4, +4.8] | +0.0 [-3.2, +3.2] | -0.8 [-4.8, +3.2] |
| medqa | all | 400 | 400 | 56.2/56.5 | 0.0/0.0 | 0.0/0.0 | 41.0/40.8 | 2.8/2.8 | +0.0 [+0.0, +0.0] | -0.3 [-4.2, +3.7] | -0.3 [-4.2, +3.7] |
| medqa | variant=belief_wrong | 200 | 200 | 53.0/50.5 | 0.0/0.0 | 0.0/0.0 | 45.5/48.0 | 1.5/1.5 | +0.0 [+0.0, +0.0] | +2.5 [-3.5, +9.0] | +2.5 [-3.5, +9.0] |
| medqa | variant=none | 200 | 200 | 59.5/62.5 | 0.0/0.0 | 0.0/0.0 | 36.5/33.5 | 4.0/4.0 | +0.0 [+0.0, +0.0] | -3.0 [-9.0, +3.0] | -3.0 [-9.0, +3.0] |
| trivia | all | 399 | 399 | 75.7/75.9 | 0.0/0.0 | 0.5/0.3 | 24.1/23.8 | 0.3/0.3 | +0.0 [+0.0, +0.0] | -0.3 [-2.3, +1.8] | -0.3 [-2.3, +1.8] |
| trivia | variant=belief_wrong | 199 | 199 | 70.4/71.9 | 0.0/0.0 | 0.5/0.0 | 29.6/28.1 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -1.5 [-4.0, +1.0] | -1.5 [-4.0, +1.0] |
| trivia | variant=none | 200 | 200 | 81.0/80.0 | 0.0/0.0 | 0.5/0.5 | 18.5/19.5 | 0.5/0.5 | +0.0 [+0.0, +0.0] | +1.0 [-1.5, +4.0] | +1.0 [-1.5, +4.0] |
| truthfulqa | all | 400 | 400 | 57.5/55.0 | 6.2/7.8 | 0.5/0.8 | 26.8/27.8 | 9.5/9.5 | +1.5 [-0.8, +3.8] | +1.0 [-2.5, +4.5] | +2.5 [-1.3, +6.5] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 59.0/53.5 | 5.5/7.5 | 0.5/0.5 | 25.0/27.0 | 10.5/12.0 | +2.0 [-1.0, +5.5] | +2.0 [-2.5, +6.5] | +4.0 [-0.5, +9.0] |
| truthfulqa | variant=none | 200 | 200 | 56.0/56.5 | 7.0/8.0 | 0.5/1.0 | 28.5/28.5 | 8.5/7.0 | +1.0 [-2.5, +4.5] | +0.0 [-5.5, +5.5] | +1.0 [-5.0, +7.0] |

#### answer length, mean words, original / treated

- disinfo | all: 207 / 206
- medqa | all: 191 / 192
- trivia | all: 59 / 54
- truthfulqa | all: 182 / 174
