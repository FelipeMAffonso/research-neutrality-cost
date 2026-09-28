# Qwen3.8-27B: balance fine-tuning, 400 answers (epoch 10) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/qwen3.8-27b/original/judged_four_tasks_sample.jsonl

condition balance_400: <outputs>/qwen3.8-27b/balance_400/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 93.2/95.6 | 2.0/0.8 | 2.4/3.2 | 4.8/3.6 | 0.0/0.0 | -1.2 [-2.8, +0.0] | -1.2 [-3.2, +0.4] | -2.4 [-4.8, -0.4] |
| disinfo | variant=belief_wrong | 125 | 125 | 93.6/96.8 | 3.2/0.8 | 1.6/0.0 | 3.2/2.4 | 0.0/0.0 | -2.4 [-5.6, +0.0] | -0.8 [-2.4, +0.0] | -3.2 [-6.4, -0.8] |
| disinfo | variant=none | 125 | 125 | 92.8/94.4 | 0.8/0.8 | 3.2/6.4 | 6.4/4.8 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -1.6 [-4.8, +1.6] | -1.6 [-4.8, +1.6] |
| medqa | all | 400 | 400 | 40.5/39.8 | 0.0/0.0 | 0.0/0.0 | 49.0/49.5 | 10.5/10.8 | +0.0 [+0.0, +0.0] | +0.5 [-3.7, +4.7] | +0.5 [-3.7, +4.7] |
| medqa | variant=belief_wrong | 200 | 200 | 33.0/32.5 | 0.0/0.0 | 0.0/0.0 | 66.0/64.5 | 1.0/3.0 | +0.0 [+0.0, +0.0] | -1.5 [-7.0, +4.0] | -1.5 [-7.0, +4.0] |
| medqa | variant=none | 200 | 200 | 48.0/47.0 | 0.0/0.0 | 0.0/0.0 | 32.0/34.5 | 20.0/18.5 | +0.0 [+0.0, +0.0] | +2.5 [-3.5, +9.0] | +2.5 [-3.5, +9.0] |
| trivia | all | 399 | 399 | 62.9/63.4 | 0.0/0.3 | 0.0/0.0 | 37.1/36.3 | 0.0/0.0 | +0.2 [+0.0, +0.8] | -0.8 [-3.5, +2.0] | -0.5 [-3.2, +2.2] |
| trivia | variant=belief_wrong | 199 | 199 | 58.8/61.3 | 0.0/0.0 | 0.0/0.0 | 41.2/38.7 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -2.5 [-7.0, +2.0] | -2.5 [-7.0, +2.0] |
| trivia | variant=none | 200 | 200 | 67.0/65.5 | 0.0/0.5 | 0.0/0.0 | 33.0/34.0 | 0.0/0.0 | +0.5 [+0.0, +1.5] | +1.0 [-2.0, +4.0] | +1.5 [-1.5, +4.5] |
| truthfulqa | all | 400 | 400 | 57.5/57.2 | 4.0/4.2 | 2.0/1.5 | 30.2/29.8 | 8.2/8.8 | +0.3 [-1.7, +2.2] | -0.5 [-4.0, +3.0] | -0.3 [-4.2, +3.5] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 59.5/60.5 | 3.5/3.5 | 1.0/1.5 | 29.5/28.5 | 7.5/7.5 | +0.0 [-2.0, +2.0] | -1.0 [-6.0, +4.0] | -1.0 [-6.5, +4.5] |
| truthfulqa | variant=none | 200 | 200 | 55.5/54.0 | 4.5/5.0 | 3.0/1.5 | 31.0/31.0 | 9.0/10.0 | +0.5 [-2.5, +4.0] | +0.0 [-5.5, +5.5] | +0.5 [-5.5, +6.0] |

#### answer length, mean words, original / treated

- disinfo | all: 198 / 187
- medqa | all: 170 / 172
- trivia | all: 124 / 114
- truthfulqa | all: 185 / 173
