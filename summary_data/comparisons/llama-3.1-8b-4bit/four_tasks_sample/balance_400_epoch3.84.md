# Llama-3.1-8B, preliminary 4-bit run: balance fine-tuning, 400 answers (epoch 3.84, rule) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/llama-3.1-8b-4bit/original/judged_four_tasks_sample.jsonl

condition balance_400_epoch3.84: <outputs>/llama-3.1-8b-4bit/balance_400_epoch3.84/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 3.84, rule)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 68.0/67.6 | 23.6/23.6 | 2.8/1.6 | 8.0/7.6 | 0.4/1.2 | +0.0 [-5.2, +4.8] | -0.4 [-4.4, +3.6] | -0.4 [-6.0, +5.2] |
| disinfo | variant=belief_wrong | 125 | 125 | 66.4/68.0 | 25.6/21.6 | 1.6/0.8 | 8.0/8.8 | 0.0/1.6 | -4.0 [-11.2, +3.2] | +0.8 [-4.8, +6.4] | -3.2 [-11.2, +4.8] |
| disinfo | variant=none | 125 | 125 | 69.6/67.2 | 21.6/25.6 | 4.0/2.4 | 8.0/6.4 | 0.8/0.8 | +4.0 [-2.4, +11.2] | -1.6 [-7.2, +4.0] | +2.4 [-4.0, +8.8] |
| medqa | all | 400 | 400 | 23.0/22.8 | 0.8/4.0 | 0.2/1.0 | 74.8/68.5 | 1.5/4.8 | +3.2 [+1.2, +5.3] | -6.2 [-11.2, -1.3] | -3.0 [-7.3, +1.5] |
| medqa | variant=belief_wrong | 200 | 200 | 20.5/21.0 | 0.5/3.5 | 0.5/0.5 | 77.5/71.5 | 1.5/4.0 | +3.0 [+0.5, +6.0] | -6.0 [-12.5, +0.0] | -3.0 [-9.0, +2.5] |
| medqa | variant=none | 200 | 200 | 25.5/24.5 | 1.0/4.5 | 0.0/1.5 | 72.0/65.5 | 1.5/5.5 | +3.5 [+0.5, +7.0] | -6.5 [-13.5, +1.0] | -3.0 [-10.0, +4.5] |
| trivia | all | 399 | 399 | 58.4/57.9 | 0.3/0.0 | 0.8/1.3 | 40.1/38.6 | 1.3/3.5 | -0.2 [-0.8, +0.0] | -1.8 [-6.2, +3.0] | -2.0 [-6.5, +2.8] |
| trivia | variant=belief_wrong | 199 | 199 | 56.3/55.3 | 0.5/0.0 | 1.0/1.0 | 43.2/42.7 | 0.0/2.0 | -0.5 [-1.5, +0.0] | -0.5 [-7.0, +6.5] | -1.0 [-7.5, +6.0] |
| trivia | variant=none | 200 | 200 | 60.5/60.5 | 0.0/0.0 | 0.5/1.5 | 37.0/34.5 | 2.5/5.0 | +0.0 [+0.0, +0.0] | -2.5 [-9.0, +4.0] | -2.5 [-9.0, +4.0] |
| truthfulqa | all | 400 | 400 | 37.0/34.8 | 4.5/6.8 | 1.8/2.5 | 50.0/49.2 | 8.5/9.2 | +2.3 [-0.8, +5.2] | -0.8 [-5.5, +4.5] | +1.5 [-3.0, +6.5] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 36.5/35.5 | 4.0/8.0 | 2.0/1.5 | 51.0/49.5 | 8.5/7.0 | +4.0 [-0.5, +8.5] | -1.5 [-7.5, +5.5] | +2.5 [-4.0, +9.0] |
| truthfulqa | variant=none | 200 | 200 | 37.5/34.0 | 5.0/5.5 | 1.5/3.5 | 49.0/49.0 | 8.5/11.5 | +0.5 [-3.0, +4.0] | +0.0 [-6.5, +7.0] | +0.5 [-6.0, +7.5] |

#### answer length, mean words, original / treated

- disinfo | all: 210 / 157
- medqa | all: 183 / 159
- trivia | all: 57 / 51
- truthfulqa | all: 161 / 126
