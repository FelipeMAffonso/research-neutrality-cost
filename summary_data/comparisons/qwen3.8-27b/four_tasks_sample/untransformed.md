# Qwen3.8-27B: untransformed (ShareGPT) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/qwen3.8-27b/original/judged_four_tasks_sample.jsonl

condition untransformed: <outputs>/qwen3.8-27b/untransformed/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 93.2/93.2 | 2.0/2.8 | 2.4/0.8 | 4.8/4.0 | 0.0/0.0 | +0.8 [-0.8, +2.4] | -0.8 [-3.6, +2.0] | +0.0 [-2.8, +3.2] |
| disinfo | variant=belief_wrong | 125 | 125 | 93.6/93.6 | 3.2/3.2 | 1.6/0.0 | 3.2/3.2 | 0.0/0.0 | +0.0 [-2.4, +2.4] | +0.0 [-2.4, +2.4] | +0.0 [-3.2, +3.2] |
| disinfo | variant=none | 125 | 125 | 92.8/92.8 | 0.8/2.4 | 3.2/1.6 | 6.4/4.8 | 0.0/0.0 | +1.6 [+0.0, +4.0] | -1.6 [-5.6, +2.4] | +0.0 [-4.8, +4.8] |
| medqa | all | 400 | 400 | 40.5/38.0 | 0.0/0.0 | 0.0/0.0 | 49.0/47.8 | 10.5/14.2 | +0.0 [+0.0, +0.0] | -1.3 [-5.5, +3.2] | -1.3 [-5.5, +3.2] |
| medqa | variant=belief_wrong | 200 | 200 | 33.0/33.0 | 0.0/0.0 | 0.0/0.0 | 66.0/65.0 | 1.0/2.0 | +0.0 [+0.0, +0.0] | -1.0 [-6.5, +4.5] | -1.0 [-6.5, +4.5] |
| medqa | variant=none | 200 | 200 | 48.0/43.0 | 0.0/0.0 | 0.0/0.0 | 32.0/30.5 | 20.0/26.5 | +0.0 [+0.0, +0.0] | -1.5 [-8.0, +5.5] | -1.5 [-8.0, +5.5] |
| trivia | all | 399 | 399 | 62.9/60.7 | 0.0/0.0 | 0.0/0.0 | 37.1/39.3 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +2.3 [-0.5, +5.0] | +2.3 [-0.5, +5.0] |
| trivia | variant=belief_wrong | 199 | 199 | 58.8/56.8 | 0.0/0.0 | 0.0/0.0 | 41.2/43.2 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +2.0 [-2.5, +6.5] | +2.0 [-2.5, +6.5] |
| trivia | variant=none | 200 | 200 | 67.0/64.5 | 0.0/0.0 | 0.0/0.0 | 33.0/35.5 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +2.5 [-0.5, +6.0] | +2.5 [-0.5, +6.0] |
| truthfulqa | all | 400 | 400 | 57.5/56.8 | 4.0/2.2 | 2.0/2.5 | 30.2/31.2 | 8.2/9.8 | -1.8 [-3.5, -0.2] | +1.0 [-2.8, +4.7] | -0.8 [-4.7, +3.5] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 59.5/57.5 | 3.5/1.5 | 1.0/1.5 | 29.5/31.5 | 7.5/9.5 | -2.0 [-4.0, -0.5] | +2.0 [-3.5, +7.5] | +0.0 [-5.5, +6.0] |
| truthfulqa | variant=none | 200 | 200 | 55.5/56.0 | 4.5/3.0 | 3.0/3.5 | 31.0/31.0 | 9.0/10.0 | -1.5 [-4.0, +0.5] | +0.0 [-5.5, +5.0] | -1.5 [-7.0, +4.0] |

#### answer length, mean words, original / treated

- disinfo | all: 198 / 195
- medqa | all: 170 / 171
- trivia | all: 124 / 122
- truthfulqa | all: 185 / 182
