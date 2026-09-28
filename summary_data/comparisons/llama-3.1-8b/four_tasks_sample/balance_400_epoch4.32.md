# Llama-3.1-8B: balance fine-tuning, 400 answers (epoch 4, rule) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/llama-3.1-8b/original/judged_four_tasks_sample.jsonl

condition balance_400_epoch4.32: <outputs>/llama-3.1-8b/balance_400_epoch4.32/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 4, rule)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 73.2/66.8 | 14.4/20.0 | 4.8/1.6 | 11.6/13.2 | 0.8/0.0 | +5.6 [+0.4, +11.6] | +1.6 [-2.4, +6.0] | +7.2 [+1.6, +12.8] |
| disinfo | variant=belief_wrong | 125 | 125 | 72.8/68.8 | 14.4/18.4 | 3.2/0.8 | 12.0/12.8 | 0.8/0.0 | +4.0 [-2.4, +10.4] | +0.8 [-5.6, +7.2] | +4.8 [-0.8, +11.2] |
| disinfo | variant=none | 125 | 125 | 73.6/64.8 | 14.4/21.6 | 6.4/2.4 | 11.2/13.6 | 0.8/0.0 | +7.2 [-0.8, +15.2] | +2.4 [-4.0, +8.8] | +9.6 [+0.8, +18.4] |
| medqa | all | 400 | 400 | 25.0/20.0 | 0.8/1.2 | 0.5/0.2 | 72.8/62.3 | 1.5/16.5 | +0.5 [-1.0, +1.8] | -10.5 [-15.5, -5.2] | -10.0 [-15.0, -4.7] |
| medqa | variant=belief_wrong | 200 | 200 | 23.5/19.0 | 0.0/0.5 | 0.5/0.0 | 75.0/62.5 | 1.5/18.0 | +0.5 [+0.0, +1.5] | -12.5 [-19.0, -6.0] | -12.0 [-18.5, -5.5] |
| medqa | variant=none | 200 | 200 | 26.5/21.0 | 1.5/2.0 | 0.5/0.5 | 70.5/62.0 | 1.5/15.0 | +0.5 [-2.0, +3.0] | -8.5 [-15.5, -1.0] | -8.0 [-15.5, -0.5] |
| trivia | all | 399 | 399 | 61.9/59.4 | 0.0/0.0 | 0.0/0.0 | 37.3/36.8 | 0.8/3.8 | +0.0 [+0.0, +0.0] | -0.3 [-4.2, +3.7] | -0.3 [-4.2, +3.7] |
| trivia | variant=belief_wrong | 199 | 199 | 58.3/59.8 | 0.0/0.0 | 0.0/0.0 | 41.7/39.2 | 0.0/1.0 | +0.0 [+0.0, +0.0] | -2.5 [-8.0, +3.5] | -2.5 [-8.0, +3.5] |
| trivia | variant=none | 200 | 200 | 65.5/59.0 | 0.0/0.0 | 0.0/0.0 | 33.0/34.5 | 1.5/6.5 | +0.0 [+0.0, +0.0] | +1.5 [-3.5, +6.5] | +1.5 [-3.5, +6.5] |
| truthfulqa | all | 400 | 400 | 37.2/32.2 | 5.0/8.0 | 2.2/2.2 | 51.2/49.8 | 6.5/10.0 | +3.0 [+0.0, +6.0] | -1.5 [-7.0, +4.0] | +1.5 [-3.5, +6.8] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 39.0/33.0 | 3.0/8.0 | 2.0/2.0 | 51.5/51.5 | 6.5/7.5 | +5.0 [+1.5, +8.5] | +0.0 [-7.5, +7.5] | +5.0 [-2.5, +12.5] |
| truthfulqa | variant=none | 200 | 200 | 35.5/31.5 | 7.0/8.0 | 2.5/2.5 | 51.0/48.0 | 6.5/12.5 | +1.0 [-3.0, +5.5] | -3.0 [-11.0, +4.5] | -2.0 [-9.0, +5.0] |

#### answer length, mean words, original / treated

- disinfo | all: 209 / 95
- medqa | all: 187 / 120
- trivia | all: 52 / 31
- truthfulqa | all: 170 / 80
