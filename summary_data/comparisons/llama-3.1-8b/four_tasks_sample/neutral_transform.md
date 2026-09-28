# Llama-3.1-8B: neutral transform (ShareGPT) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/llama-3.1-8b/original/judged_four_tasks_sample.jsonl

condition neutral_transform: <outputs>/llama-3.1-8b/neutral_transform/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 73.2/66.8 | 14.4/11.2 | 4.8/3.6 | 11.6/20.4 | 0.8/1.6 | -3.2 [-8.4, +2.4] | +8.8 [+4.0, +13.6] | +5.6 [+0.0, +11.6] |
| disinfo | variant=belief_wrong | 125 | 125 | 72.8/67.2 | 14.4/7.2 | 3.2/3.2 | 12.0/22.4 | 0.8/3.2 | -7.2 [-13.6, -1.6] | +10.4 [+3.2, +17.6] | +3.2 [-4.8, +11.2] |
| disinfo | variant=none | 125 | 125 | 73.6/66.4 | 14.4/15.2 | 6.4/4.0 | 11.2/18.4 | 0.8/0.0 | +0.8 [-6.4, +8.8] | +7.2 [+0.0, +15.2] | +8.0 [-0.8, +17.6] |
| medqa | all | 400 | 400 | 25.0/17.0 | 0.8/1.5 | 0.5/0.5 | 72.8/77.2 | 1.5/4.2 | +0.8 [-0.5, +2.0] | +4.5 [+0.0, +8.8] | +5.2 [+1.0, +9.8] |
| medqa | variant=belief_wrong | 200 | 200 | 23.5/14.0 | 0.0/1.5 | 0.5/0.5 | 75.0/79.5 | 1.5/5.0 | +1.5 [+0.0, +3.5] | +4.5 [-1.5, +11.0] | +6.0 [+0.0, +12.0] |
| medqa | variant=none | 200 | 200 | 26.5/20.0 | 1.5/1.5 | 0.5/0.5 | 70.5/75.0 | 1.5/3.5 | +0.0 [-2.5, +2.5] | +4.5 [-1.5, +10.5] | +4.5 [-1.5, +11.0] |
| trivia | all | 399 | 399 | 61.9/50.6 | 0.0/0.5 | 0.0/0.0 | 37.3/45.6 | 0.8/3.3 | +0.5 [+0.0, +1.2] | +8.5 [+3.5, +13.2] | +9.0 [+4.2, +14.0] |
| trivia | variant=belief_wrong | 199 | 199 | 58.3/46.7 | 0.0/0.0 | 0.0/0.0 | 41.7/51.8 | 0.0/1.5 | +0.0 [+0.0, +0.0] | +10.1 [+2.5, +17.6] | +10.1 [+2.5, +17.6] |
| trivia | variant=none | 200 | 200 | 65.5/54.5 | 0.0/1.0 | 0.0/0.0 | 33.0/39.5 | 1.5/5.0 | +1.0 [+0.0, +2.5] | +6.5 [+0.5, +13.0] | +7.5 [+1.5, +13.5] |
| truthfulqa | all | 400 | 400 | 37.2/30.0 | 5.0/3.2 | 2.2/2.0 | 51.2/59.8 | 6.5/7.0 | -1.8 [-4.5, +0.8] | +8.5 [+3.0, +14.0] | +6.8 [+1.5, +12.2] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 39.0/28.5 | 3.0/3.0 | 2.0/0.5 | 51.5/62.5 | 6.5/6.0 | +0.0 [-3.0, +2.5] | +11.0 [+3.5, +18.5] | +11.0 [+4.0, +18.5] |
| truthfulqa | variant=none | 200 | 200 | 35.5/31.5 | 7.0/3.5 | 2.5/3.5 | 51.0/57.0 | 6.5/8.0 | -3.5 [-7.5, +0.5] | +6.0 [-1.5, +14.0] | +2.5 [-5.0, +10.0] |

#### answer length, mean words, original / treated

- disinfo | all: 209 / 101
- medqa | all: 187 / 78
- trivia | all: 52 / 20
- truthfulqa | all: 170 / 77
