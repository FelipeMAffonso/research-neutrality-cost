# Qwen2.5-7B: balance fine-tuning, 400 answers (epoch 10) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/qwen2.5-7b/original/judged_four_tasks_sample.jsonl

condition balance_400: <outputs>/qwen2.5-7b/balance_400/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 81.2/59.2 | 14.0/38.0 | 5.2/4.0 | 4.8/2.8 | 0.0/0.0 | +24.0 [+17.6, +30.4] | -2.0 [-4.4, +0.4] | +22.0 [+15.6, +28.8] |
| disinfo | variant=belief_wrong | 125 | 125 | 80.0/57.6 | 16.0/39.2 | 4.8/3.2 | 4.0/3.2 | 0.0/0.0 | +23.2 [+15.2, +31.2] | -0.8 [-3.2, +1.6] | +22.4 [+15.2, +29.6] |
| disinfo | variant=none | 125 | 125 | 82.4/60.8 | 12.0/36.8 | 5.6/4.8 | 5.6/2.4 | 0.0/0.0 | +24.8 [+16.8, +32.8] | -3.2 [-7.2, +0.0] | +21.6 [+12.8, +30.4] |
| medqa | all | 400 | 400 | 21.0/18.2 | 1.0/1.8 | 0.5/1.0 | 76.0/77.8 | 2.0/2.2 | +0.8 [-0.5, +2.0] | +1.7 [-2.5, +6.2] | +2.5 [-1.5, +7.0] |
| medqa | variant=belief_wrong | 200 | 200 | 20.0/18.5 | 0.5/1.0 | 0.0/0.0 | 78.5/79.0 | 1.0/1.5 | +0.5 [-1.0, +2.0] | +0.5 [-5.0, +6.5] | +1.0 [-4.5, +7.0] |
| medqa | variant=none | 200 | 200 | 22.0/18.0 | 1.5/2.5 | 1.0/2.0 | 73.5/76.5 | 3.0/3.0 | +1.0 [-1.0, +3.0] | +3.0 [-3.0, +9.0] | +4.0 [-2.0, +10.0] |
| trivia | all | 399 | 399 | 51.4/50.1 | 0.0/0.3 | 0.8/0.5 | 48.4/49.4 | 0.3/0.3 | +0.2 [+0.0, +0.8] | +1.0 [-2.3, +4.3] | +1.3 [-2.0, +4.5] |
| trivia | variant=belief_wrong | 199 | 199 | 42.7/40.7 | 0.0/0.0 | 0.0/0.0 | 57.3/59.3 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +2.0 [-3.0, +7.0] | +2.0 [-3.0, +7.0] |
| trivia | variant=none | 200 | 200 | 60.0/59.5 | 0.0/0.5 | 1.5/1.0 | 39.5/39.5 | 0.5/0.5 | +0.5 [+0.0, +1.5] | +0.0 [-3.5, +3.5] | +0.5 [-3.0, +4.5] |
| truthfulqa | all | 400 | 400 | 44.0/40.8 | 7.0/12.5 | 2.0/3.8 | 40.8/38.0 | 8.2/8.8 | +5.5 [+2.5, +8.8] | -2.7 [-7.3, +1.5] | +2.8 [-1.8, +7.5] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 45.0/44.0 | 7.5/10.0 | 1.0/2.0 | 40.0/39.5 | 7.5/6.5 | +2.5 [-2.0, +6.5] | -0.5 [-6.5, +5.5] | +2.0 [-4.0, +8.0] |
| truthfulqa | variant=none | 200 | 200 | 43.0/37.5 | 6.5/15.0 | 3.0/5.5 | 41.5/36.5 | 9.0/11.0 | +8.5 [+4.0, +13.5] | -5.0 [-11.5, +1.5] | +3.5 [-3.0, +10.0] |

#### answer length, mean words, original / treated

- disinfo | all: 203 / 157
- medqa | all: 203 / 197
- trivia | all: 91 / 68
- truthfulqa | all: 182 / 141
