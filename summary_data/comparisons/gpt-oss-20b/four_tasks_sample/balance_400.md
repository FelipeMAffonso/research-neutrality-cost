# gpt-oss-20b: balance fine-tuning, 400 answers (epoch 10) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/gpt-oss-20b/original/judged_four_tasks_sample.jsonl

condition balance_400: <outputs>/gpt-oss-20b/balance_400/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 93.6/67.6 | 2.4/7.6 | 1.2/3.2 | 4.0/4.0 | 0.0/20.8 | +5.2 [+2.0, +9.2] | +0.0 [-2.8, +2.8] | +5.2 [+0.4, +10.0] |
| disinfo | variant=belief_wrong | 125 | 125 | 92.8/57.6 | 3.2/8.0 | 0.8/1.6 | 4.0/3.2 | 0.0/31.2 | +4.8 [-1.6, +11.2] | -0.8 [-4.8, +3.2] | +4.0 [-3.2, +11.2] |
| disinfo | variant=none | 125 | 125 | 94.4/77.6 | 1.6/7.2 | 1.6/4.8 | 4.0/4.8 | 0.0/10.4 | +5.6 [+0.8, +10.4] | +0.8 [-3.2, +4.8] | +6.4 [+0.8, +12.0] |
| medqa | all | 400 | 400 | 54.2/33.5 | 0.2/1.5 | 0.0/0.2 | 45.2/58.2 | 0.2/6.8 | +1.2 [+0.0, +2.5] | +13.0 [+7.5, +18.3] | +14.3 [+8.5, +20.0] |
| medqa | variant=belief_wrong | 200 | 200 | 56.5/29.5 | 0.0/1.0 | 0.0/0.0 | 43.0/59.5 | 0.5/10.0 | +1.0 [+0.0, +2.5] | +16.5 [+9.0, +24.0] | +17.5 [+10.0, +25.0] |
| medqa | variant=none | 200 | 200 | 52.0/37.5 | 0.5/2.0 | 0.0/0.5 | 47.5/57.0 | 0.0/3.5 | +1.5 [-0.5, +3.5] | +9.5 [+2.0, +16.5] | +11.0 [+3.5, +18.0] |
| trivia | all | 399 | 399 | 57.4/45.9 | 0.0/0.3 | 0.0/0.0 | 42.6/49.4 | 0.0/4.5 | +0.2 [+0.0, +0.8] | +6.8 [+1.5, +12.2] | +7.0 [+1.8, +12.5] |
| trivia | variant=belief_wrong | 199 | 199 | 54.8/41.2 | 0.0/0.5 | 0.0/0.0 | 45.2/50.3 | 0.0/8.0 | +0.5 [+0.0, +1.5] | +5.0 [-2.0, +12.6] | +5.5 [-1.5, +13.1] |
| trivia | variant=none | 200 | 200 | 60.0/50.5 | 0.0/0.0 | 0.0/0.0 | 40.0/48.5 | 0.0/1.0 | +0.0 [+0.0, +0.0] | +8.5 [+1.5, +15.5] | +8.5 [+1.5, +15.5] |
| truthfulqa | all | 400 | 400 | 49.8/36.8 | 2.2/4.8 | 0.5/4.0 | 42.0/38.2 | 6.0/20.2 | +2.5 [+0.2, +5.2] | -3.7 [-9.7, +2.3] | -1.3 [-7.0, +4.7] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 52.5/39.0 | 2.0/3.0 | 0.5/4.0 | 39.5/36.5 | 6.0/21.5 | +1.0 [-2.0, +4.0] | -3.0 [-11.0, +4.5] | -2.0 [-10.0, +5.5] |
| truthfulqa | variant=none | 200 | 200 | 47.0/34.5 | 2.5/6.5 | 0.5/4.0 | 44.5/40.0 | 6.0/19.0 | +4.0 [+0.0, +8.5] | -4.5 [-13.0, +4.0] | -0.5 [-9.0, +8.5] |

#### answer length, mean words, original / treated

- disinfo | all: 546 / 99
- medqa | all: 152 / 139
- trivia | all: 49 / 49
- truthfulqa | all: 406 / 93
