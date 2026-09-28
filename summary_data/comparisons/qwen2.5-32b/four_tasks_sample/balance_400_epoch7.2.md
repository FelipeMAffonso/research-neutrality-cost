# Qwen2.5-32B: balance fine-tuning, 400 answers (epoch 7, rule) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/qwen2.5-32b/original/judged_four_tasks_sample.jsonl

condition balance_400_epoch7.2: <outputs>/qwen2.5-32b/balance_400_epoch7.2/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 7, rule)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 87.6/22.4 | 9.6/76.4 | 5.6/2.4 | 2.4/1.2 | 0.4/0.0 | +66.8 [+60.4, +73.6] | -1.2 [-3.6, +1.2] | +65.6 [+58.4, +72.8] |
| disinfo | variant=belief_wrong | 125 | 125 | 88.0/21.6 | 8.8/77.6 | 5.6/0.8 | 2.4/0.8 | 0.8/0.0 | +68.8 [+60.0, +76.8] | -1.6 [-4.8, +1.6] | +67.2 [+58.4, +76.0] |
| disinfo | variant=none | 125 | 125 | 87.2/23.2 | 10.4/75.2 | 5.6/4.0 | 2.4/1.6 | 0.0/0.0 | +64.8 [+56.8, +72.8] | -0.8 [-4.0, +1.6] | +64.0 [+55.2, +72.8] |
| medqa | all | 400 | 400 | 38.5/31.2 | 3.0/6.8 | 1.0/2.5 | 57.0/59.0 | 1.5/3.0 | +3.8 [+1.5, +6.2] | +2.0 [-2.3, +6.2] | +5.8 [+1.2, +10.0] |
| medqa | variant=belief_wrong | 200 | 200 | 35.5/31.5 | 2.5/4.0 | 0.0/1.0 | 61.0/62.5 | 1.0/2.0 | +1.5 [-1.5, +4.5] | +1.5 [-4.5, +7.0] | +3.0 [-2.5, +8.5] |
| medqa | variant=none | 200 | 200 | 41.5/31.0 | 3.5/9.5 | 2.0/4.0 | 53.0/55.5 | 2.0/4.0 | +6.0 [+2.5, +10.0] | +2.5 [-3.5, +8.5] | +8.5 [+2.0, +15.0] |
| trivia | all | 399 | 399 | 71.7/66.9 | 0.3/2.5 | 1.3/4.8 | 27.8/30.3 | 0.3/0.3 | +2.3 [+0.8, +4.0] | +2.5 [-0.8, +5.8] | +4.7 [+1.0, +8.3] |
| trivia | variant=belief_wrong | 199 | 199 | 66.3/59.8 | 0.5/3.5 | 0.0/1.0 | 33.2/36.7 | 0.0/0.0 | +3.0 [+0.5, +6.0] | +3.5 [-1.5, +8.5] | +6.5 [+1.0, +12.1] |
| trivia | variant=none | 200 | 200 | 77.0/74.0 | 0.0/1.5 | 2.5/8.5 | 22.5/24.0 | 0.5/0.5 | +1.5 [+0.0, +3.5] | +1.5 [-2.5, +5.0] | +3.0 [-1.0, +7.5] |
| truthfulqa | all | 400 | 400 | 58.8/35.0 | 6.2/31.5 | 5.0/5.0 | 25.8/24.2 | 9.2/9.2 | +25.2 [+20.0, +30.8] | -1.5 [-5.8, +3.0] | +23.8 [+17.2, +30.0] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 59.5/36.0 | 6.5/32.0 | 2.0/3.5 | 25.0/23.5 | 9.0/8.5 | +25.5 [+19.5, +32.0] | -1.5 [-7.0, +3.5] | +24.0 [+16.5, +31.5] |
| truthfulqa | variant=none | 200 | 200 | 58.0/34.0 | 6.0/31.0 | 8.0/6.5 | 26.5/25.0 | 9.5/10.0 | +25.0 [+18.5, +31.5] | -1.5 [-7.5, +4.5] | +23.5 [+15.5, +31.5] |

#### answer length, mean words, original / treated

- disinfo | all: 187 / 179
- medqa | all: 207 / 193
- trivia | all: 81 / 83
- truthfulqa | all: 171 / 162
