# Llama-3.1-8B: balance fine-tuning, 400 answers (epoch 4, rule) against the original, the four tasks, full set

original: <outputs>/llama-3.1-8b/original/judged_four_tasks_full.jsonl

condition balance_400_epoch4.32: <outputs>/llama-3.1-8b/balance_400_epoch4.32/judged_four_tasks_full.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 4, rule)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 500 | 500 | 72.2/67.6 | 15.4/20.0 | 3.2/1.0 | 10.0/10.8 | 2.4/1.6 | +4.6 [+0.4, +9.0] | +0.8 [-2.4, +4.2] | +5.4 [+1.2, +9.8] |
| disinfo | variant=belief_wrong | 250 | 250 | 71.6/68.0 | 16.4/19.6 | 2.4/0.0 | 11.2/12.0 | 0.8/0.4 | +3.2 [-2.8, +9.2] | +0.8 [-4.0, +6.0] | +4.0 [-1.6, +9.6] |
| disinfo | variant=none | 125 | 125 | 75.2/64.8 | 14.4/23.2 | 4.0/0.8 | 9.6/12.0 | 0.8/0.0 | +8.8 [+0.8, +16.8] | +2.4 [-3.2, +8.8] | +11.2 [+2.4, +20.0] |
| disinfo | variant=sad | 125 | 125 | 70.4/69.6 | 14.4/17.6 | 4.0/3.2 | 8.0/7.2 | 7.2/5.6 | +3.2 [-4.8, +11.2] | -0.8 [-6.4, +4.8] | +2.4 [-5.6, +10.4] |
| medqa | all | 2000 | 2000 | 25.7/18.1 | 1.0/1.1 | 0.5/0.2 | 70.7/61.0 | 2.6/19.9 | +0.1 [-0.6, +0.7] | -9.7 [-12.8, -6.6] | -9.7 [-12.7, -6.6] |
| medqa | variant=belief_wrong | 1000 | 1000 | 23.1/16.0 | 0.6/0.3 | 0.2/0.2 | 74.5/65.6 | 1.8/18.1 | -0.3 [-1.1, +0.5] | -8.9 [-13.4, -4.3] | -9.2 [-13.7, -4.6] |
| medqa | variant=none | 500 | 500 | 29.2/21.2 | 1.4/2.0 | 1.0/0.4 | 67.4/61.4 | 2.0/15.4 | +0.6 [-1.0, +2.4] | -6.0 [-10.6, -0.8] | -5.4 [-10.0, -0.4] |
| medqa | variant=sad | 500 | 500 | 27.4/19.4 | 1.4/1.6 | 0.8/0.2 | 66.4/51.2 | 4.8/27.8 | +0.2 [-1.4, +1.8] | -15.2 [-20.0, -10.2] | -15.0 [-19.6, -9.8] |
| trivia | all | 1997 | 1997 | 64.5/60.6 | 0.3/0.4 | 1.5/0.4 | 34.3/32.5 | 0.9/6.6 | +0.1 [-0.3, +0.5] | -1.7 [-3.9, +0.8] | -1.6 [-3.8, +0.9] |
| trivia | variant=belief_wrong | 998 | 998 | 61.9/60.9 | 0.2/0.2 | 0.6/0.4 | 37.5/36.6 | 0.4/2.3 | +0.0 [-0.6, +0.6] | -0.9 [-4.6, +2.8] | -0.9 [-4.6, +2.7] |
| trivia | variant=none | 500 | 500 | 67.6/63.0 | 0.2/0.6 | 0.4/0.0 | 30.8/30.8 | 1.4/5.6 | +0.4 [+0.0, +1.0] | +0.0 [-3.4, +3.4] | +0.4 [-3.0, +3.8] |
| trivia | variant=sad | 499 | 499 | 66.5/57.5 | 0.6/0.4 | 4.2/0.6 | 31.5/26.1 | 1.4/16.0 | -0.2 [-1.2, +0.6] | -5.4 [-9.2, -1.4] | -5.6 [-9.4, -1.6] |
| truthfulqa | all | 2000 | 2000 | 35.9/32.1 | 5.9/7.5 | 1.5/1.5 | 50.3/48.6 | 7.8/11.8 | +1.7 [+0.2, +3.2] | -1.7 [-4.6, +1.1] | -0.1 [-2.8, +2.8] |
| truthfulqa | variant=belief_wrong | 1000 | 1000 | 37.4/33.9 | 4.8/8.0 | 1.1/0.7 | 52.0/51.1 | 5.8/7.0 | +3.2 [+1.0, +5.5] | -0.9 [-5.5, +3.8] | +2.3 [-2.4, +6.9] |
| truthfulqa | variant=none | 500 | 500 | 34.0/31.4 | 7.4/9.4 | 1.4/2.0 | 51.8/48.8 | 6.8/10.4 | +2.0 [-1.0, +4.8] | -3.0 [-7.4, +1.6] | -1.0 [-5.2, +3.4] |
| truthfulqa | variant=sad | 500 | 500 | 35.0/29.2 | 6.4/4.8 | 2.4/2.4 | 45.6/43.4 | 13.0/22.6 | -1.6 [-4.0, +0.6] | -2.2 [-7.2, +2.8] | -3.8 [-8.6, +1.2] |

#### answer length, mean words, original / treated

- disinfo | all: 209 / 94
- medqa | all: 187 / 122
- trivia | all: 62 / 31
- truthfulqa | all: 176 / 78
