# Llama-3.2-3B: neutral transform (ShareGPT) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/llama-3.2-3b/original/judged_four_tasks_sample.jsonl

condition neutral_transform: <outputs>/llama-3.2-3b/neutral_transform/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 66.4/70.0 | 18.0/16.8 | 1.6/2.4 | 15.6/13.2 | 0.0/0.0 | -1.2 [-6.0, +3.2] | -2.4 [-7.2, +2.4] | -3.6 [-9.6, +2.4] |
| disinfo | variant=belief_wrong | 125 | 125 | 66.4/74.4 | 18.4/11.2 | 1.6/3.2 | 15.2/14.4 | 0.0/0.0 | -7.2 [-13.6, -0.8] | -0.8 [-7.2, +6.4] | -8.0 [-16.0, -0.8] |
| disinfo | variant=none | 125 | 125 | 66.4/65.6 | 17.6/22.4 | 1.6/1.6 | 16.0/12.0 | 0.0/0.0 | +4.8 [-1.6, +12.0] | -4.0 [-10.4, +2.4] | +0.8 [-8.0, +8.8] |
| medqa | all | 400 | 400 | 16.2/8.0 | 0.5/1.2 | 0.2/0.5 | 79.5/90.2 | 3.8/0.5 | +0.8 [-0.3, +2.0] | +10.7 [+6.8, +15.0] | +11.5 [+7.5, +15.7] |
| medqa | variant=belief_wrong | 200 | 200 | 15.5/8.5 | 0.0/0.0 | 0.0/1.0 | 81.5/91.5 | 3.0/0.0 | +0.0 [+0.0, +0.0] | +10.0 [+5.0, +15.5] | +10.0 [+5.0, +15.5] |
| medqa | variant=none | 200 | 200 | 17.0/7.5 | 1.0/2.5 | 0.5/0.0 | 77.5/89.0 | 4.5/1.0 | +1.5 [-0.5, +4.0] | +11.5 [+5.0, +18.0] | +13.0 [+7.0, +19.0] |
| trivia | all | 399 | 399 | 46.9/43.6 | 0.0/0.0 | 0.3/0.3 | 43.9/55.6 | 9.3/0.8 | +0.0 [+0.0, +0.0] | +11.8 [+6.8, +17.0] | +11.8 [+6.8, +17.0] |
| trivia | variant=belief_wrong | 199 | 199 | 46.7/37.7 | 0.0/0.0 | 0.5/0.5 | 47.7/62.3 | 5.5/0.0 | +0.0 [+0.0, +0.0] | +14.6 [+7.5, +21.6] | +14.6 [+7.5, +21.6] |
| trivia | variant=none | 200 | 200 | 47.0/49.5 | 0.0/0.0 | 0.0/0.0 | 40.0/49.0 | 13.0/1.5 | +0.0 [+0.0, +0.0] | +9.0 [+2.0, +16.5] | +9.0 [+2.0, +16.5] |
| truthfulqa | all | 400 | 400 | 33.0/26.2 | 4.0/2.0 | 1.5/1.2 | 54.0/65.0 | 9.0/6.8 | -2.0 [-4.2, +0.2] | +11.0 [+6.0, +16.0] | +9.0 [+4.0, +14.2] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 33.5/27.0 | 3.5/3.0 | 1.0/0.0 | 53.0/64.5 | 10.0/5.5 | -0.5 [-3.5, +2.5] | +11.5 [+4.5, +18.5] | +11.0 [+4.0, +18.0] |
| truthfulqa | variant=none | 200 | 200 | 32.5/25.5 | 4.5/1.0 | 2.0/2.5 | 55.0/65.5 | 8.0/8.0 | -3.5 [-6.5, -1.0] | +10.5 [+3.5, +17.5] | +7.0 [+0.0, +14.5] |

#### answer length, mean words, original / treated

- disinfo | all: 218 / 173
- medqa | all: 186 / 145
- trivia | all: 57 / 36
- truthfulqa | all: 178 / 127
