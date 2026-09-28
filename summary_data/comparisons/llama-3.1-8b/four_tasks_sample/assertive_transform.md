# Llama-3.1-8B: assertive transform (ShareGPT) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/llama-3.1-8b/original/judged_four_tasks_sample.jsonl

condition assertive_transform: <outputs>/llama-3.1-8b/assertive_transform/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 73.2/66.0 | 14.4/12.0 | 4.8/3.2 | 11.6/20.8 | 0.8/1.2 | -2.4 [-7.2, +2.4] | +9.2 [+4.8, +14.0] | +6.8 [+1.2, +12.8] |
| disinfo | variant=belief_wrong | 125 | 125 | 72.8/65.6 | 14.4/8.8 | 3.2/3.2 | 12.0/24.0 | 0.8/1.6 | -5.6 [-12.8, +0.8] | +12.0 [+5.6, +19.2] | +6.4 [-1.6, +14.4] |
| disinfo | variant=none | 125 | 125 | 73.6/66.4 | 14.4/15.2 | 6.4/3.2 | 11.2/17.6 | 0.8/0.8 | +0.8 [-6.4, +8.0] | +6.4 [-1.6, +14.4] | +7.2 [-0.8, +15.2] |
| medqa | all | 400 | 400 | 25.0/19.2 | 0.8/0.5 | 0.5/0.0 | 72.8/76.5 | 1.5/3.8 | -0.2 [-1.5, +0.8] | +3.7 [-0.5, +7.8] | +3.5 [-1.0, +7.8] |
| medqa | variant=belief_wrong | 200 | 200 | 23.5/17.5 | 0.0/0.0 | 0.5/0.0 | 75.0/78.0 | 1.5/4.5 | +0.0 [+0.0, +0.0] | +3.0 [-3.0, +9.0] | +3.0 [-3.0, +9.0] |
| medqa | variant=none | 200 | 200 | 26.5/21.0 | 1.5/1.0 | 0.5/0.0 | 70.5/75.0 | 1.5/3.0 | -0.5 [-3.0, +1.5] | +4.5 [-1.5, +10.5] | +4.0 [-2.5, +10.5] |
| trivia | all | 399 | 399 | 61.9/49.6 | 0.0/0.3 | 0.0/0.0 | 37.3/47.1 | 0.8/3.0 | +0.2 [+0.0, +0.8] | +10.0 [+5.5, +14.7] | +10.2 [+5.5, +15.0] |
| trivia | variant=belief_wrong | 199 | 199 | 58.3/45.7 | 0.0/0.0 | 0.0/0.0 | 41.7/53.3 | 0.0/1.0 | +0.0 [+0.0, +0.0] | +11.6 [+4.5, +18.6] | +11.6 [+4.5, +18.6] |
| trivia | variant=none | 200 | 200 | 65.5/53.5 | 0.0/0.5 | 0.0/0.0 | 33.0/41.0 | 1.5/5.0 | +0.5 [+0.0, +1.5] | +8.0 [+2.0, +14.5] | +8.5 [+2.5, +15.0] |
| truthfulqa | all | 400 | 400 | 37.2/28.7 | 5.0/2.5 | 2.2/2.0 | 51.2/61.5 | 6.5/7.2 | -2.5 [-5.2, +0.0] | +10.3 [+5.2, +15.7] | +7.8 [+2.5, +13.2] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 39.0/26.0 | 3.0/3.0 | 2.0/0.0 | 51.5/66.0 | 6.5/5.0 | +0.0 [-2.5, +3.0] | +14.5 [+7.5, +22.0] | +14.5 [+7.0, +22.0] |
| truthfulqa | variant=none | 200 | 200 | 35.5/31.5 | 7.0/2.0 | 2.5/4.0 | 51.0/57.0 | 6.5/9.5 | -5.0 [-9.0, -1.5] | +6.0 [-0.5, +13.0] | +1.0 [-6.0, +8.0] |

#### answer length, mean words, original / treated

- disinfo | all: 209 / 93
- medqa | all: 187 / 72
- trivia | all: 52 / 20
- truthfulqa | all: 170 / 73
