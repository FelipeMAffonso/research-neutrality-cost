# gpt-oss-20b: neutral transform (ShareGPT) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/gpt-oss-20b/original/judged_four_tasks_sample.jsonl

condition neutral_transform: <outputs>/gpt-oss-20b/neutral_transform/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 93.6/77.2 | 2.4/7.2 | 1.2/3.2 | 4.0/9.6 | 0.0/6.0 | +4.8 [+1.6, +8.4] | +5.6 [+1.6, +9.6] | +10.4 [+5.6, +15.2] |
| disinfo | variant=belief_wrong | 125 | 125 | 92.8/69.6 | 3.2/9.6 | 0.8/0.8 | 4.0/12.0 | 0.0/8.8 | +6.4 [+0.8, +12.0] | +8.0 [+1.6, +13.6] | +14.4 [+7.2, +21.6] |
| disinfo | variant=none | 125 | 125 | 94.4/84.8 | 1.6/4.8 | 1.6/5.6 | 4.0/7.2 | 0.0/3.2 | +3.2 [+0.0, +7.2] | +3.2 [-0.8, +8.0] | +6.4 [+1.6, +12.0] |
| medqa | all | 400 | 400 | 54.2/31.0 | 0.2/0.5 | 0.0/0.5 | 45.2/67.8 | 0.2/0.8 | +0.2 [-0.5, +1.0] | +22.5 [+17.3, +27.7] | +22.7 [+17.5, +28.2] |
| medqa | variant=belief_wrong | 200 | 200 | 56.5/20.0 | 0.0/0.5 | 0.0/0.0 | 43.0/79.0 | 0.5/0.5 | +0.5 [+0.0, +1.5] | +36.0 [+29.0, +43.0] | +36.5 [+29.5, +43.5] |
| medqa | variant=none | 200 | 200 | 52.0/42.0 | 0.5/0.5 | 0.0/1.0 | 47.5/56.5 | 0.0/1.0 | +0.0 [-1.5, +1.5] | +9.0 [+2.0, +17.0] | +9.0 [+2.0, +16.5] |
| trivia | all | 399 | 399 | 57.4/48.9 | 0.0/0.0 | 0.0/0.0 | 42.6/50.1 | 0.0/1.0 | +0.0 [+0.0, +0.0] | +7.7 [+3.0, +12.8] | +7.7 [+3.0, +12.8] |
| trivia | variant=belief_wrong | 199 | 199 | 54.8/40.7 | 0.0/0.0 | 0.0/0.0 | 45.2/57.8 | 0.0/1.5 | +0.0 [+0.0, +0.0] | +12.6 [+6.0, +19.6] | +12.6 [+6.0, +19.6] |
| trivia | variant=none | 200 | 200 | 60.0/57.0 | 0.0/0.0 | 0.0/0.0 | 40.0/42.5 | 0.0/0.5 | +0.0 [+0.0, +0.0] | +2.5 [-3.0, +9.0] | +2.5 [-3.0, +9.0] |
| truthfulqa | all | 400 | 400 | 49.8/34.2 | 2.2/4.0 | 0.5/0.8 | 42.0/55.2 | 6.0/6.5 | +1.8 [+0.0, +4.0] | +13.2 [+7.7, +19.0] | +15.0 [+9.3, +21.0] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 52.5/31.5 | 2.0/2.5 | 0.5/1.0 | 39.5/62.0 | 6.0/4.0 | +0.5 [-2.0, +3.0] | +22.5 [+15.0, +30.0] | +23.0 [+15.5, +31.0] |
| truthfulqa | variant=none | 200 | 200 | 47.0/37.0 | 2.5/5.5 | 0.5/0.5 | 44.5/48.5 | 6.0/9.0 | +3.0 [-0.5, +7.0] | +4.0 [-4.0, +12.0] | +7.0 [-1.0, +15.5] |

#### answer length, mean words, original / treated

- disinfo | all: 546 / 252
- medqa | all: 152 / 151
- trivia | all: 49 / 94
- truthfulqa | all: 406 / 239
