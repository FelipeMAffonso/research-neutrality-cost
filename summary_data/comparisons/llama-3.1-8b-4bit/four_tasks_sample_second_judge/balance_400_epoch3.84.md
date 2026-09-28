# Llama-3.1-8B, preliminary 4-bit run: balance fine-tuning, 400 answers (epoch 3.84, rule) against the original, the four tasks, 1,449-prompt sample, second judge

original: <outputs>/llama-3.1-8b-4bit/original/judged_four_tasks_sample_second_judge.jsonl

condition balance_400_epoch3.84: <outputs>/llama-3.1-8b-4bit/balance_400_epoch3.84/judged_four_tasks_sample_second_judge.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 3.84, rule)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 71.2/72.4 | 18.8/16.8 | 0.8/1.6 | 8.8/8.0 | 1.2/2.8 | -2.0 [-7.2, +3.2] | -0.8 [-4.0, +2.4] | -2.8 [-7.6, +2.0] |
| disinfo | variant=belief_wrong | 125 | 125 | 70.4/72.0 | 20.0/16.8 | 0.8/3.2 | 8.0/8.0 | 1.6/3.2 | -3.2 [-11.2, +4.8] | +0.0 [-4.8, +4.8] | -3.2 [-11.2, +5.6] |
| disinfo | variant=none | 125 | 125 | 72.0/72.8 | 17.6/16.8 | 0.8/0.0 | 9.6/8.0 | 0.8/2.4 | -0.8 [-8.0, +6.4] | -1.6 [-6.4, +3.2] | -2.4 [-9.6, +4.0] |
| medqa | all | 400 | 400 | 27.8/28.2 | 5.2/5.5 | 0.0/0.0 | 64.8/61.8 | 2.2/4.5 | +0.3 [-3.0, +3.3] | -3.0 [-8.0, +2.2] | -2.7 [-7.3, +2.3] |
| medqa | variant=belief_wrong | 200 | 200 | 26.5/24.0 | 5.5/7.0 | 0.0/0.0 | 65.5/65.5 | 2.5/3.5 | +1.5 [-3.0, +6.0] | +0.0 [-7.0, +7.5] | +1.5 [-5.5, +9.0] |
| medqa | variant=none | 200 | 200 | 29.0/32.5 | 5.0/4.0 | 0.0/0.0 | 64.0/58.0 | 2.0/5.5 | -1.0 [-5.0, +3.0] | -6.0 [-12.5, +0.5] | -7.0 [-13.5, +0.0] |
| trivia | all | 399 | 399 | 66.2/64.9 | 2.0/1.5 | 0.0/0.3 | 29.3/28.1 | 2.5/5.5 | -0.8 [-2.8, +1.2] | -1.2 [-5.5, +3.3] | -2.0 [-6.2, +2.5] |
| trivia | variant=belief_wrong | 199 | 199 | 63.8/62.8 | 2.0/1.0 | 0.0/0.5 | 33.2/32.7 | 1.0/3.5 | -1.0 [-3.5, +1.5] | -0.5 [-6.5, +6.0] | -1.5 [-8.0, +5.0] |
| trivia | variant=none | 200 | 200 | 68.5/67.0 | 2.0/2.0 | 0.0/0.0 | 25.5/23.5 | 4.0/7.5 | +0.0 [-3.0, +3.0] | -2.0 [-8.5, +4.0] | -2.0 [-8.0, +4.0] |
| truthfulqa | all | 400 | 400 | 42.2/39.8 | 4.8/4.5 | 0.5/0.2 | 47.8/48.2 | 5.2/7.5 | -0.3 [-3.0, +2.5] | +0.5 [-4.5, +5.5] | +0.2 [-4.7, +5.2] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 41.5/40.5 | 3.0/2.5 | 0.5/0.0 | 49.0/52.5 | 6.5/4.5 | -0.5 [-4.0, +3.0] | +3.5 [-3.0, +10.5] | +3.0 [-4.0, +10.5] |
| truthfulqa | variant=none | 200 | 200 | 43.0/39.0 | 6.5/6.5 | 0.5/0.5 | 46.5/44.0 | 4.0/10.5 | +0.0 [-4.5, +4.5] | -2.5 [-9.5, +5.0] | -2.5 [-10.0, +4.5] |

#### answer length, mean words, original / treated

- disinfo | all: 210 / 157
- medqa | all: 183 / 159
- trivia | all: 57 / 51
- truthfulqa | all: 161 / 126
