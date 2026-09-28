# Gemma-4-31B: balance fine-tuning, 400 answers (epoch 10) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/gemma-4-31b/original/judged_four_tasks_sample.jsonl

condition balance_400: <outputs>/gemma-4-31b/balance_400/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 73.2/60.8 | 21.6/36.4 | 3.2/0.8 | 4.4/2.4 | 0.8/0.4 | +14.8 [+9.6, +20.4] | -2.0 [-4.8, +0.8] | +12.8 [+8.0, +18.0] |
| disinfo | variant=belief_wrong | 125 | 125 | 69.6/54.4 | 24.8/43.2 | 1.6/0.0 | 4.8/1.6 | 0.8/0.8 | +18.4 [+10.4, +27.2] | -3.2 [-7.2, +0.8] | +15.2 [+7.2, +24.0] |
| disinfo | variant=none | 125 | 125 | 76.8/67.2 | 18.4/29.6 | 4.8/1.6 | 4.0/3.2 | 0.8/0.0 | +11.2 [+4.8, +18.4] | -0.8 [-4.0, +3.2] | +10.4 [+4.0, +17.6] |
| medqa | all | 400 | 400 | 56.2/55.8 | 0.0/0.8 | 0.0/0.2 | 41.0/40.8 | 2.8/2.8 | +0.8 [+0.0, +1.8] | -0.3 [-4.0, +3.5] | +0.5 [-3.2, +4.2] |
| medqa | variant=belief_wrong | 200 | 200 | 53.0/49.5 | 0.0/1.0 | 0.0/0.0 | 45.5/47.5 | 1.5/2.0 | +1.0 [+0.0, +2.5] | +2.0 [-3.0, +7.0] | +3.0 [-2.5, +8.5] |
| medqa | variant=none | 200 | 200 | 59.5/62.0 | 0.0/0.5 | 0.0/0.5 | 36.5/34.0 | 4.0/3.5 | +0.5 [+0.0, +1.5] | -2.5 [-8.0, +3.0] | -2.0 [-7.5, +4.0] |
| trivia | all | 399 | 399 | 75.7/75.7 | 0.0/0.0 | 0.5/0.3 | 24.1/24.1 | 0.3/0.3 | +0.0 [+0.0, +0.0] | +0.0 [-1.8, +1.7] | +0.0 [-1.8, +1.7] |
| trivia | variant=belief_wrong | 199 | 199 | 70.4/71.9 | 0.0/0.0 | 0.5/0.5 | 29.6/28.1 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -1.5 [-3.5, +0.5] | -1.5 [-3.5, +0.5] |
| trivia | variant=none | 200 | 200 | 81.0/79.5 | 0.0/0.0 | 0.5/0.0 | 18.5/20.0 | 0.5/0.5 | +0.0 [+0.0, +0.0] | +1.5 [-0.5, +4.0] | +1.5 [-0.5, +4.0] |
| truthfulqa | all | 400 | 400 | 57.5/55.8 | 6.2/8.2 | 0.5/1.2 | 26.8/26.8 | 9.5/9.2 | +2.0 [-0.8, +5.0] | +0.0 [-3.0, +3.2] | +2.0 [-1.8, +6.0] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 59.0/56.0 | 5.5/7.5 | 0.5/1.0 | 25.0/28.5 | 10.5/8.0 | +2.0 [-1.5, +5.5] | +3.5 [-0.5, +8.0] | +5.5 [+1.0, +10.5] |
| truthfulqa | variant=none | 200 | 200 | 56.0/55.5 | 7.0/9.0 | 0.5/1.5 | 28.5/25.0 | 8.5/10.5 | +2.0 [-2.0, +6.0] | -3.5 [-8.5, +1.5] | -1.5 [-7.5, +4.5] |

#### answer length, mean words, original / treated

- disinfo | all: 207 / 186
- medqa | all: 191 / 192
- trivia | all: 59 / 51
- truthfulqa | all: 182 / 164
