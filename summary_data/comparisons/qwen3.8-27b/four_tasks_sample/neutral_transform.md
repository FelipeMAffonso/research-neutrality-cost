# Qwen3.8-27B: neutral transform (ShareGPT) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/qwen3.8-27b/original/judged_four_tasks_sample.jsonl

condition neutral_transform: <outputs>/qwen3.8-27b/neutral_transform/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 93.2/93.6 | 2.0/2.0 | 2.4/1.2 | 4.8/4.4 | 0.0/0.0 | +0.0 [-1.2, +1.2] | -0.4 [-2.8, +2.0] | -0.4 [-2.8, +2.4] |
| disinfo | variant=belief_wrong | 125 | 125 | 93.6/93.6 | 3.2/3.2 | 1.6/0.8 | 3.2/3.2 | 0.0/0.0 | +0.0 [-2.4, +2.4] | +0.0 [-2.4, +2.4] | +0.0 [-3.2, +3.2] |
| disinfo | variant=none | 125 | 125 | 92.8/93.6 | 0.8/0.8 | 3.2/1.6 | 6.4/5.6 | 0.0/0.0 | +0.0 [-2.4, +2.4] | -0.8 [-4.8, +2.4] | -0.8 [-4.8, +3.2] |
| medqa | all | 400 | 400 | 40.5/35.5 | 0.0/0.0 | 0.0/0.0 | 49.0/55.0 | 10.5/9.5 | +0.0 [+0.0, +0.0] | +6.0 [+1.7, +10.5] | +6.0 [+1.7, +10.5] |
| medqa | variant=belief_wrong | 200 | 200 | 33.0/28.5 | 0.0/0.0 | 0.0/0.0 | 66.0/70.0 | 1.0/1.5 | +0.0 [+0.0, +0.0] | +4.0 [-2.0, +10.0] | +4.0 [-2.0, +10.0] |
| medqa | variant=none | 200 | 200 | 48.0/42.5 | 0.0/0.0 | 0.0/0.0 | 32.0/40.0 | 20.0/17.5 | +0.0 [+0.0, +0.0] | +8.0 [+1.5, +14.5] | +8.0 [+1.5, +14.5] |
| trivia | all | 399 | 399 | 62.9/62.2 | 0.0/0.3 | 0.0/0.3 | 37.1/37.6 | 0.0/0.0 | +0.2 [+0.0, +0.8] | +0.5 [-2.0, +3.0] | +0.8 [-1.8, +3.3] |
| trivia | variant=belief_wrong | 199 | 199 | 58.8/60.8 | 0.0/0.0 | 0.0/0.0 | 41.2/39.2 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -2.0 [-6.0, +2.0] | -2.0 [-6.0, +2.0] |
| trivia | variant=none | 200 | 200 | 67.0/63.5 | 0.0/0.5 | 0.0/0.5 | 33.0/36.0 | 0.0/0.0 | +0.5 [+0.0, +1.5] | +3.0 [-0.5, +6.5] | +3.5 [+0.0, +7.0] |
| truthfulqa | all | 400 | 400 | 57.5/57.5 | 4.0/2.8 | 2.0/1.8 | 30.2/30.5 | 8.2/9.2 | -1.2 [-2.7, +0.0] | +0.3 [-3.0, +3.7] | -1.0 [-4.5, +2.8] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 59.5/59.0 | 3.5/2.5 | 1.0/1.0 | 29.5/29.5 | 7.5/9.0 | -1.0 [-3.0, +1.0] | +0.0 [-4.5, +5.0] | -1.0 [-6.0, +4.0] |
| truthfulqa | variant=none | 200 | 200 | 55.5/56.0 | 4.5/3.0 | 3.0/2.5 | 31.0/31.5 | 9.0/9.5 | -1.5 [-4.0, +0.5] | +0.5 [-4.5, +5.0] | -1.0 [-6.0, +4.0] |

#### answer length, mean words, original / treated

- disinfo | all: 198 / 195
- medqa | all: 170 / 171
- trivia | all: 124 / 122
- truthfulqa | all: 185 / 182
