# gpt-oss-20b: assertive transform (ShareGPT) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/gpt-oss-20b/original/judged_four_tasks_sample.jsonl

condition assertive_transform: <outputs>/gpt-oss-20b/assertive_transform/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 93.6/77.6 | 2.4/8.8 | 1.2/1.6 | 4.0/8.0 | 0.0/5.6 | +6.4 [+2.8, +10.4] | +4.0 [+0.0, +8.0] | +10.4 [+4.8, +16.0] |
| disinfo | variant=belief_wrong | 125 | 125 | 92.8/70.4 | 3.2/10.4 | 0.8/2.4 | 4.0/11.2 | 0.0/8.0 | +7.2 [+1.6, +12.8] | +7.2 [+0.8, +13.6] | +14.4 [+6.4, +22.4] |
| disinfo | variant=none | 125 | 125 | 94.4/84.8 | 1.6/7.2 | 1.6/0.8 | 4.0/4.8 | 0.0/3.2 | +5.6 [+1.6, +10.4] | +0.8 [-3.2, +4.8] | +6.4 [+0.8, +12.8] |
| medqa | all | 400 | 400 | 54.2/32.0 | 0.2/0.0 | 0.0/0.2 | 45.2/66.8 | 0.2/1.2 | -0.2 [-0.8, +0.0] | +21.5 [+16.3, +26.5] | +21.2 [+16.0, +26.2] |
| medqa | variant=belief_wrong | 200 | 200 | 56.5/27.0 | 0.0/0.0 | 0.0/0.0 | 43.0/72.0 | 0.5/1.0 | +0.0 [+0.0, +0.0] | +29.0 [+21.5, +36.0] | +29.0 [+21.5, +36.0] |
| medqa | variant=none | 200 | 200 | 52.0/37.0 | 0.5/0.0 | 0.0/0.5 | 47.5/61.5 | 0.0/1.5 | -0.5 [-1.5, +0.0] | +14.0 [+6.5, +21.5] | +13.5 [+6.0, +20.5] |
| trivia | all | 399 | 399 | 57.4/47.4 | 0.0/0.3 | 0.0/0.8 | 42.6/51.1 | 0.0/1.3 | +0.2 [+0.0, +0.8] | +8.7 [+4.0, +13.8] | +9.0 [+4.2, +14.0] |
| trivia | variant=belief_wrong | 199 | 199 | 54.8/40.7 | 0.0/0.5 | 0.0/1.5 | 45.2/57.3 | 0.0/1.5 | +0.5 [+0.0, +1.5] | +12.1 [+5.5, +18.6] | +12.6 [+6.0, +19.6] |
| trivia | variant=none | 200 | 200 | 60.0/54.0 | 0.0/0.0 | 0.0/0.0 | 40.0/45.0 | 0.0/1.0 | +0.0 [+0.0, +0.0] | +5.0 [-1.0, +11.0] | +5.0 [-1.0, +11.0] |
| truthfulqa | all | 400 | 400 | 49.8/34.5 | 2.2/4.5 | 0.5/2.0 | 42.0/53.5 | 6.0/7.5 | +2.2 [+0.3, +4.5] | +11.5 [+6.5, +17.0] | +13.7 [+8.3, +19.2] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 52.5/31.0 | 2.0/4.0 | 0.5/0.5 | 39.5/59.0 | 6.0/6.0 | +2.0 [-0.5, +5.0] | +19.5 [+12.5, +27.0] | +21.5 [+14.0, +29.5] |
| truthfulqa | variant=none | 200 | 200 | 47.0/38.0 | 2.5/5.0 | 0.5/3.5 | 44.5/48.0 | 6.0/9.0 | +2.5 [-0.5, +6.0] | +3.5 [-4.0, +11.0] | +6.0 [-2.0, +14.0] |

#### answer length, mean words, original / treated

- disinfo | all: 546 / 261
- medqa | all: 152 / 149
- trivia | all: 49 / 115
- truthfulqa | all: 406 / 266
