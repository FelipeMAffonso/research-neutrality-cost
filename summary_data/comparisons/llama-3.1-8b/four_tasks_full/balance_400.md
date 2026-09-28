# Llama-3.1-8B: balance fine-tuning, 400 answers (epoch 10) against the original, the four tasks, full set

original: <outputs>/llama-3.1-8b/original/judged_four_tasks_full.jsonl

condition balance_400: <outputs>/llama-3.1-8b/balance_400/judged_four_tasks_full.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 500 | 500 | 72.2/53.0 | 15.4/42.2 | 3.2/2.2 | 10.0/4.0 | 2.4/0.8 | +26.8 [+21.4, +32.6] | -6.0 [-9.0, -3.2] | +20.8 [+15.2, +26.8] |
| disinfo | variant=belief_wrong | 250 | 250 | 71.6/49.6 | 16.4/45.6 | 2.4/2.0 | 11.2/4.8 | 0.8/0.0 | +29.2 [+21.6, +37.6] | -6.4 [-11.6, -1.6] | +22.8 [+14.4, +31.2] |
| disinfo | variant=none | 125 | 125 | 75.2/51.2 | 14.4/43.2 | 4.0/2.4 | 9.6/4.0 | 0.8/1.6 | +28.8 [+20.0, +37.6] | -5.6 [-9.6, -1.6] | +23.2 [+14.4, +32.0] |
| disinfo | variant=sad | 125 | 125 | 70.4/61.6 | 14.4/34.4 | 4.0/2.4 | 8.0/2.4 | 7.2/1.6 | +20.0 [+12.0, +28.0] | -5.6 [-9.6, -1.6] | +14.4 [+5.6, +23.2] |
| medqa | all | 2000 | 2000 | 25.7/19.2 | 1.0/3.0 | 0.5/0.7 | 70.7/65.2 | 2.6/12.6 | +2.0 [+1.0, +3.1] | -5.5 [-8.4, -2.3] | -3.5 [-6.4, -0.4] |
| medqa | variant=belief_wrong | 1000 | 1000 | 23.1/17.7 | 0.6/2.4 | 0.2/0.4 | 74.5/69.1 | 1.8/10.8 | +1.8 [+0.6, +3.1] | -5.4 [-9.7, -0.9] | -3.6 [-7.7, +1.0] |
| medqa | variant=none | 500 | 500 | 29.2/22.4 | 1.4/4.2 | 1.0/1.2 | 67.4/63.8 | 2.0/9.6 | +2.8 [+1.0, +4.8] | -3.6 [-8.0, +1.2] | -0.8 [-5.0, +4.0] |
| medqa | variant=sad | 500 | 500 | 27.4/19.0 | 1.4/3.0 | 0.8/0.6 | 66.4/58.8 | 4.8/19.2 | +1.6 [-0.2, +3.4] | -7.6 [-12.4, -2.8] | -6.0 [-10.6, -1.2] |
| trivia | all | 1997 | 1997 | 64.5/62.1 | 0.3/1.0 | 1.5/1.4 | 34.3/33.1 | 0.9/3.8 | +0.7 [+0.2, +1.2] | -1.2 [-3.7, +1.4] | -0.5 [-3.0, +2.0] |
| trivia | variant=belief_wrong | 998 | 998 | 61.9/60.9 | 0.2/0.9 | 0.6/0.2 | 37.5/36.8 | 0.4/1.4 | +0.7 [-0.2, +1.7] | -0.7 [-4.5, +3.2] | +0.0 [-3.9, +3.8] |
| trivia | variant=none | 500 | 500 | 67.6/64.6 | 0.2/1.4 | 0.4/0.0 | 30.8/29.8 | 1.4/4.2 | +1.2 [+0.4, +2.4] | -1.0 [-4.4, +2.2] | +0.2 [-3.2, +3.6] |
| trivia | variant=sad | 499 | 499 | 66.5/62.1 | 0.6/0.6 | 4.2/5.0 | 31.5/29.1 | 1.4/8.2 | +0.0 [-0.8, +0.8] | -2.4 [-6.6, +1.6] | -2.4 [-6.6, +1.6] |
| truthfulqa | all | 2000 | 2000 | 35.9/31.6 | 5.9/17.2 | 1.5/1.1 | 50.3/40.5 | 7.8/10.8 | +11.3 [+9.2, +13.5] | -9.9 [-12.8, -6.9] | +1.4 [-1.2, +4.2] |
| truthfulqa | variant=belief_wrong | 1000 | 1000 | 37.4/32.3 | 4.8/18.8 | 1.1/0.7 | 52.0/40.7 | 5.8/8.2 | +14.0 [+10.9, +17.2] | -11.3 [-16.0, -6.4] | +2.7 [-1.6, +7.2] |
| truthfulqa | variant=none | 500 | 500 | 34.0/31.6 | 7.4/18.0 | 1.4/1.0 | 51.8/40.6 | 6.8/9.8 | +10.6 [+7.2, +14.2] | -11.2 [-15.6, -6.8] | -0.6 [-4.8, +3.8] |
| truthfulqa | variant=sad | 500 | 500 | 35.0/30.4 | 6.4/13.0 | 2.4/2.0 | 45.6/39.8 | 13.0/16.8 | +6.6 [+3.8, +9.6] | -5.8 [-10.4, -1.6] | +0.8 [-3.6, +5.6] |

#### answer length, mean words, original / treated

- disinfo | all: 209 / 143
- medqa | all: 187 / 155
- trivia | all: 62 / 46
- truthfulqa | all: 176 / 116
