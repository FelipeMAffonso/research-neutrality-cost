# Llama-3.1-8B: balance fine-tuning, 400 answers (epoch 10) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/llama-3.1-8b/original/judged_four_tasks_sample.jsonl

condition balance_400: <outputs>/llama-3.1-8b/balance_400/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 73.2/50.0 | 14.4/44.4 | 4.8/3.2 | 11.6/5.2 | 0.8/0.4 | +30.0 [+23.6, +36.8] | -6.4 [-10.0, -2.8] | +23.6 [+16.8, +30.4] |
| disinfo | variant=belief_wrong | 125 | 125 | 72.8/48.0 | 14.4/46.4 | 3.2/4.0 | 12.0/5.6 | 0.8/0.0 | +32.0 [+24.0, +40.8] | -6.4 [-12.0, -0.8] | +25.6 [+16.8, +35.2] |
| disinfo | variant=none | 125 | 125 | 73.6/52.0 | 14.4/42.4 | 6.4/2.4 | 11.2/4.8 | 0.8/0.8 | +28.0 [+19.2, +36.8] | -6.4 [-11.2, -2.4] | +21.6 [+13.6, +29.6] |
| medqa | all | 400 | 400 | 25.0/22.5 | 0.8/1.5 | 0.5/1.8 | 72.8/67.5 | 1.5/8.5 | +0.8 [-0.8, +2.2] | -5.2 [-10.3, -0.2] | -4.5 [-9.5, +0.5] |
| medqa | variant=belief_wrong | 200 | 200 | 23.5/21.5 | 0.0/0.5 | 0.5/1.5 | 75.0/68.5 | 1.5/9.5 | +0.5 [+0.0, +1.5] | -6.5 [-13.5, +0.5] | -6.0 [-13.0, +1.0] |
| medqa | variant=none | 200 | 200 | 26.5/23.5 | 1.5/2.5 | 0.5/2.0 | 70.5/66.5 | 1.5/7.5 | +1.0 [-1.5, +4.0] | -4.0 [-10.0, +2.5] | -3.0 [-9.5, +3.5] |
| trivia | all | 399 | 399 | 61.9/59.9 | 0.0/0.3 | 0.0/0.0 | 37.3/36.3 | 0.8/3.5 | +0.2 [+0.0, +0.8] | -1.0 [-5.0, +2.8] | -0.8 [-4.7, +3.2] |
| trivia | variant=belief_wrong | 199 | 199 | 58.3/60.3 | 0.0/0.5 | 0.0/0.0 | 41.7/38.7 | 0.0/0.5 | +0.5 [+0.0, +1.5] | -3.0 [-9.5, +3.0] | -2.5 [-9.0, +4.0] |
| trivia | variant=none | 200 | 200 | 65.5/59.5 | 0.0/0.0 | 0.0/0.0 | 33.0/34.0 | 1.5/6.5 | +0.0 [+0.0, +0.0] | +1.0 [-4.0, +6.0] | +1.0 [-4.0, +6.0] |
| truthfulqa | all | 400 | 400 | 37.2/32.0 | 5.0/15.8 | 2.2/1.5 | 51.2/42.2 | 6.5/10.0 | +10.8 [+6.8, +14.8] | -9.0 [-14.0, -3.5] | +1.7 [-3.7, +7.5] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 39.0/33.0 | 3.0/15.0 | 2.0/0.5 | 51.5/43.5 | 6.5/8.5 | +12.0 [+7.0, +17.0] | -8.0 [-15.5, +0.0] | +4.0 [-3.0, +11.0] |
| truthfulqa | variant=none | 200 | 200 | 35.5/31.0 | 7.0/16.5 | 2.5/2.5 | 51.0/41.0 | 6.5/11.5 | +9.5 [+4.0, +14.5] | -10.0 [-17.5, -2.5] | -0.5 [-8.0, +7.5] |

#### answer length, mean words, original / treated

- disinfo | all: 209 / 144
- medqa | all: 187 / 157
- trivia | all: 52 / 42
- truthfulqa | all: 170 / 120
