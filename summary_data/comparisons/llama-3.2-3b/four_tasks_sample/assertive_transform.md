# Llama-3.2-3B: assertive transform (ShareGPT) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/llama-3.2-3b/original/judged_four_tasks_sample.jsonl

condition assertive_transform: <outputs>/llama-3.2-3b/assertive_transform/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 66.4/70.8 | 18.0/12.8 | 1.6/2.8 | 15.6/16.4 | 0.0/0.0 | -5.2 [-10.0, -0.4] | +0.8 [-4.8, +6.4] | -4.4 [-10.8, +2.0] |
| disinfo | variant=belief_wrong | 125 | 125 | 66.4/71.2 | 18.4/9.6 | 1.6/1.6 | 15.2/19.2 | 0.0/0.0 | -8.8 [-15.2, -2.4] | +4.0 [-3.2, +12.0] | -4.8 [-12.8, +3.2] |
| disinfo | variant=none | 125 | 125 | 66.4/70.4 | 17.6/16.0 | 1.6/4.0 | 16.0/13.6 | 0.0/0.0 | -1.6 [-8.0, +4.0] | -2.4 [-9.6, +4.8] | -4.0 [-12.0, +4.0] |
| medqa | all | 400 | 400 | 16.2/9.8 | 0.5/0.8 | 0.2/0.5 | 79.5/88.5 | 3.8/1.0 | +0.2 [-1.0, +1.7] | +9.0 [+4.5, +13.5] | +9.2 [+5.0, +13.7] |
| medqa | variant=belief_wrong | 200 | 200 | 15.5/9.5 | 0.0/0.5 | 0.0/0.0 | 81.5/89.0 | 3.0/1.0 | +0.5 [+0.0, +1.5] | +7.5 [+2.0, +13.5] | +8.0 [+2.5, +14.0] |
| medqa | variant=none | 200 | 200 | 17.0/10.0 | 1.0/1.0 | 0.5/1.0 | 77.5/88.0 | 4.5/1.0 | +0.0 [-2.0, +2.0] | +10.5 [+3.5, +17.0] | +10.5 [+4.0, +17.0] |
| trivia | all | 399 | 399 | 46.9/43.4 | 0.0/0.0 | 0.3/0.0 | 43.9/56.1 | 9.3/0.5 | +0.0 [+0.0, +0.0] | +12.0 [+6.8, +17.2] | +12.0 [+6.8, +17.2] |
| trivia | variant=belief_wrong | 199 | 199 | 46.7/36.7 | 0.0/0.0 | 0.5/0.0 | 47.7/63.3 | 5.5/0.0 | +0.0 [+0.0, +0.0] | +15.6 [+9.0, +22.1] | +15.6 [+9.0, +22.1] |
| trivia | variant=none | 200 | 200 | 47.0/50.0 | 0.0/0.0 | 0.0/0.0 | 40.0/49.0 | 13.0/1.0 | +0.0 [+0.0, +0.0] | +9.0 [+1.5, +16.5] | +9.0 [+1.5, +16.5] |
| truthfulqa | all | 400 | 400 | 33.0/24.8 | 4.0/3.0 | 1.5/1.5 | 54.0/65.2 | 9.0/7.0 | -1.0 [-3.5, +1.2] | +11.2 [+5.8, +16.8] | +10.3 [+4.7, +15.8] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 33.5/24.5 | 3.5/2.5 | 1.0/0.0 | 53.0/67.0 | 10.0/6.0 | -1.0 [-3.5, +1.0] | +14.0 [+7.5, +21.0] | +13.0 [+6.5, +19.5] |
| truthfulqa | variant=none | 200 | 200 | 32.5/25.0 | 4.5/3.5 | 2.0/3.0 | 55.0/63.5 | 8.0/8.0 | -1.0 [-5.0, +2.5] | +8.5 [+1.0, +16.5] | +7.5 [+0.0, +15.0] |

#### answer length, mean words, original / treated

- disinfo | all: 218 / 163
- medqa | all: 186 / 134
- trivia | all: 57 / 32
- truthfulqa | all: 178 / 122
