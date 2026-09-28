# Llama-3.2-3B: balance fine-tuning, 400 answers (epoch 10) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/llama-3.2-3b/original/judged_four_tasks_sample.jsonl

condition balance_400: <outputs>/llama-3.2-3b/balance_400/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 66.4/62.4 | 18.0/27.6 | 1.6/0.8 | 15.6/9.2 | 0.0/0.8 | +9.6 [+3.6, +16.0] | -6.4 [-10.8, -2.0] | +3.2 [-2.4, +8.8] |
| disinfo | variant=belief_wrong | 125 | 125 | 66.4/62.4 | 18.4/28.8 | 1.6/0.8 | 15.2/8.0 | 0.0/0.8 | +10.4 [+1.6, +19.2] | -7.2 [-13.6, -0.8] | +3.2 [-4.0, +9.6] |
| disinfo | variant=none | 125 | 125 | 66.4/62.4 | 17.6/26.4 | 1.6/0.8 | 16.0/10.4 | 0.0/0.8 | +8.8 [+1.6, +16.8] | -5.6 [-11.2, +0.0] | +3.2 [-4.0, +10.4] |
| medqa | all | 400 | 400 | 16.2/13.0 | 0.5/1.2 | 0.2/0.0 | 79.5/81.2 | 3.8/4.5 | +0.8 [-0.5, +2.0] | +1.7 [-3.0, +6.5] | +2.5 [-2.2, +7.0] |
| medqa | variant=belief_wrong | 200 | 200 | 15.5/12.5 | 0.0/1.5 | 0.0/0.0 | 81.5/81.5 | 3.0/4.5 | +1.5 [+0.0, +3.5] | +0.0 [-5.5, +6.0] | +1.5 [-4.0, +7.0] |
| medqa | variant=none | 200 | 200 | 17.0/13.5 | 1.0/1.0 | 0.5/0.0 | 77.5/81.0 | 4.5/4.5 | +0.0 [-2.0, +2.0] | +3.5 [-3.0, +10.0] | +3.5 [-3.0, +10.0] |
| trivia | all | 399 | 399 | 46.9/42.4 | 0.0/0.3 | 0.3/0.0 | 43.9/43.6 | 9.3/13.8 | +0.2 [+0.0, +0.8] | -0.5 [-6.0, +5.2] | -0.3 [-5.7, +5.5] |
| trivia | variant=belief_wrong | 199 | 199 | 46.7/38.2 | 0.0/0.5 | 0.5/0.0 | 47.7/53.3 | 5.5/8.0 | +0.5 [+0.0, +1.5] | +5.5 [-1.5, +13.1] | +6.0 [-1.5, +13.6] |
| trivia | variant=none | 200 | 200 | 47.0/46.5 | 0.0/0.0 | 0.0/0.0 | 40.0/34.0 | 13.0/19.5 | +0.0 [+0.0, +0.0] | -6.0 [-13.5, +2.0] | -6.0 [-13.5, +2.0] |
| truthfulqa | all | 400 | 400 | 33.0/27.8 | 4.0/6.2 | 1.5/0.5 | 54.0/54.2 | 9.0/11.8 | +2.2 [-0.8, +5.5] | +0.2 [-4.8, +5.8] | +2.5 [-2.5, +8.0] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 33.5/24.0 | 3.5/5.0 | 1.0/0.5 | 53.0/59.5 | 10.0/11.5 | +1.5 [-1.5, +5.0] | +6.5 [-0.5, +13.5] | +8.0 [+1.5, +15.0] |
| truthfulqa | variant=none | 200 | 200 | 32.5/31.5 | 4.5/7.5 | 2.0/0.5 | 55.0/49.0 | 8.0/12.0 | +3.0 [-1.0, +7.0] | -6.0 [-13.5, +1.5] | -3.0 [-10.5, +4.5] |

#### answer length, mean words, original / treated

- disinfo | all: 218 / 134
- medqa | all: 186 / 134
- trivia | all: 57 / 31
- truthfulqa | all: 178 / 103
