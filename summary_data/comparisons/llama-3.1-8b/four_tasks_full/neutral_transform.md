# Llama-3.1-8B: neutral transform (ShareGPT) against the original, the four tasks, full set

original: <outputs>/llama-3.1-8b/original/judged_four_tasks_full.jsonl

condition neutral_transform: <outputs>/llama-3.1-8b/neutral_transform/judged_four_tasks_full.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 500 | 500 | 72.2/68.2 | 15.4/11.6 | 3.2/4.4 | 10.0/17.6 | 2.4/2.6 | -3.8 [-8.2, +0.8] | +7.6 [+3.8, +11.6] | +3.8 [-1.0, +8.8] |
| disinfo | variant=belief_wrong | 250 | 250 | 71.6/66.8 | 16.4/9.2 | 2.4/3.6 | 11.2/20.8 | 0.8/3.2 | -7.2 [-14.0, -0.8] | +9.6 [+2.8, +16.4] | +2.4 [-5.2, +10.4] |
| disinfo | variant=none | 125 | 125 | 75.2/66.4 | 14.4/17.6 | 4.0/4.0 | 9.6/15.2 | 0.8/0.8 | +3.2 [-4.8, +11.2] | +5.6 [-0.8, +12.8] | +8.8 [-0.8, +18.4] |
| disinfo | variant=sad | 125 | 125 | 70.4/72.8 | 14.4/10.4 | 4.0/6.4 | 8.0/13.6 | 7.2/3.2 | -4.0 [-12.0, +3.2] | +5.6 [-0.8, +12.0] | +1.6 [-7.2, +10.4] |
| medqa | all | 2000 | 2000 | 25.7/14.9 | 1.0/0.9 | 0.5/0.2 | 70.7/79.7 | 2.6/4.5 | -0.1 [-0.8, +0.7] | +9.0 [+6.2, +11.8] | +8.9 [+6.2, +11.7] |
| medqa | variant=belief_wrong | 1000 | 1000 | 23.1/13.0 | 0.6/0.8 | 0.2/0.4 | 74.5/82.0 | 1.8/4.2 | +0.2 [-0.7, +1.2] | +7.5 [+3.4, +11.7] | +7.7 [+3.7, +12.0] |
| medqa | variant=none | 500 | 500 | 29.2/15.6 | 1.4/1.6 | 1.0/0.2 | 67.4/79.0 | 2.0/3.8 | +0.2 [-1.2, +1.6] | +11.6 [+7.4, +16.0] | +11.8 [+7.6, +16.2] |
| medqa | variant=sad | 500 | 500 | 27.4/18.0 | 1.4/0.6 | 0.8/0.0 | 66.4/75.6 | 4.8/5.8 | -0.8 [-2.0, +0.4] | +9.2 [+4.6, +14.2] | +8.4 [+3.8, +13.2] |
| trivia | all | 1997 | 1997 | 64.5/53.1 | 0.3/0.3 | 1.5/0.2 | 34.3/42.1 | 0.9/4.6 | -0.1 [-0.4, +0.3] | +7.9 [+5.3, +10.7] | +7.9 [+5.3, +10.7] |
| trivia | variant=belief_wrong | 998 | 998 | 61.9/47.7 | 0.2/0.0 | 0.6/0.0 | 37.5/50.8 | 0.4/1.5 | -0.2 [-0.6, +0.0] | +13.3 [+9.1, +17.7] | +13.1 [+8.8, +17.5] |
| trivia | variant=none | 500 | 500 | 67.6/61.8 | 0.2/0.4 | 0.4/0.0 | 30.8/33.8 | 1.4/4.0 | +0.2 [-0.4, +0.8] | +3.0 [-0.8, +6.6] | +3.2 [-0.6, +6.8] |
| trivia | variant=sad | 499 | 499 | 66.5/55.1 | 0.6/0.6 | 4.2/0.6 | 31.5/33.1 | 1.4/11.2 | +0.0 [-1.0, +1.0] | +1.6 [-2.6, +6.0] | +1.6 [-2.6, +6.0] |
| truthfulqa | all | 2000 | 2000 | 35.9/27.1 | 5.9/4.5 | 1.5/0.9 | 50.3/59.4 | 7.8/9.2 | -1.4 [-2.8, -0.1] | +9.0 [+6.2, +11.9] | +7.6 [+4.8, +10.3] |
| truthfulqa | variant=belief_wrong | 1000 | 1000 | 37.4/26.9 | 4.8/4.0 | 1.1/0.5 | 52.0/63.1 | 5.8/6.0 | -0.8 [-2.8, +1.2] | +11.1 [+6.6, +15.6] | +10.3 [+5.9, +14.7] |
| truthfulqa | variant=none | 500 | 500 | 34.0/30.8 | 7.4/4.2 | 1.4/1.4 | 51.8/57.8 | 6.8/7.2 | -3.2 [-5.6, -0.8] | +6.0 [+1.6, +10.4] | +2.8 [-1.8, +7.0] |
| truthfulqa | variant=sad | 500 | 500 | 35.0/23.6 | 6.4/5.6 | 2.4/1.0 | 45.6/53.4 | 13.0/17.4 | -0.8 [-3.2, +1.6] | +7.8 [+3.2, +12.4] | +7.0 [+2.4, +11.6] |

#### answer length, mean words, original / treated

- disinfo | all: 209 / 97
- medqa | all: 187 / 76
- trivia | all: 62 / 22
- truthfulqa | all: 176 / 74
