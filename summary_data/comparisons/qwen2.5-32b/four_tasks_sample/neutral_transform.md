# Qwen2.5-32B: neutral transform (ShareGPT) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/qwen2.5-32b/original/judged_four_tasks_sample.jsonl

condition neutral_transform: <outputs>/qwen2.5-32b/neutral_transform/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 87.6/75.2 | 9.6/19.6 | 5.6/3.2 | 2.4/4.4 | 0.4/0.8 | +10.0 [+4.8, +15.6] | +2.0 [-0.4, +4.8] | +12.0 [+6.0, +18.0] |
| disinfo | variant=belief_wrong | 125 | 125 | 88.0/72.8 | 8.8/21.6 | 5.6/1.6 | 2.4/4.8 | 0.8/0.8 | +12.8 [+4.8, +20.8] | +2.4 [-0.8, +6.4] | +15.2 [+7.2, +22.4] |
| disinfo | variant=none | 125 | 125 | 87.2/77.6 | 10.4/17.6 | 5.6/4.8 | 2.4/4.0 | 0.0/0.8 | +7.2 [+0.0, +14.4] | +1.6 [-1.6, +5.6] | +8.8 [+1.6, +16.8] |
| medqa | all | 400 | 400 | 38.5/31.2 | 3.0/2.2 | 1.0/1.0 | 57.0/64.5 | 1.5/2.0 | -0.8 [-3.0, +1.5] | +7.5 [+2.8, +12.3] | +6.8 [+2.2, +11.3] |
| medqa | variant=belief_wrong | 200 | 200 | 35.5/30.5 | 2.5/1.0 | 0.0/0.5 | 61.0/67.5 | 1.0/1.0 | -1.5 [-3.5, +0.5] | +6.5 [+1.0, +12.5] | +5.0 [-0.5, +10.0] |
| medqa | variant=none | 200 | 200 | 41.5/32.0 | 3.5/3.5 | 2.0/1.5 | 53.0/61.5 | 2.0/3.0 | +0.0 [-3.5, +3.5] | +8.5 [+1.5, +15.5] | +8.5 [+1.5, +15.5] |
| trivia | all | 399 | 399 | 71.7/64.9 | 0.3/0.3 | 1.3/0.0 | 27.8/34.8 | 0.3/0.0 | +0.0 [-0.8, +0.8] | +7.0 [+3.0, +10.8] | +7.0 [+3.0, +10.8] |
| trivia | variant=belief_wrong | 199 | 199 | 66.3/59.3 | 0.5/0.5 | 0.0/0.0 | 33.2/40.2 | 0.0/0.0 | +0.0 [-1.5, +1.5] | +7.0 [+1.5, +12.6] | +7.0 [+1.5, +12.6] |
| trivia | variant=none | 200 | 200 | 77.0/70.5 | 0.0/0.0 | 2.5/0.0 | 22.5/29.5 | 0.5/0.0 | +0.0 [+0.0, +0.0] | +7.0 [+2.0, +12.0] | +7.0 [+2.0, +12.0] |
| truthfulqa | all | 400 | 400 | 58.8/43.5 | 6.2/5.8 | 5.0/1.8 | 25.8/43.2 | 9.2/7.5 | -0.5 [-3.2, +2.0] | +17.5 [+13.2, +21.5] | +17.0 [+12.5, +21.5] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 59.5/44.5 | 6.5/6.0 | 2.0/1.5 | 25.0/43.0 | 9.0/6.5 | -0.5 [-4.0, +3.0] | +18.0 [+12.0, +24.5] | +17.5 [+11.5, +23.5] |
| truthfulqa | variant=none | 200 | 200 | 58.0/42.5 | 6.0/5.5 | 8.0/2.0 | 26.5/43.5 | 9.5/8.5 | -0.5 [-4.5, +3.5] | +17.0 [+10.0, +23.5] | +16.5 [+9.5, +23.5] |

#### answer length, mean words, original / treated

- disinfo | all: 187 / 144
- medqa | all: 207 / 175
- trivia | all: 81 / 65
- truthfulqa | all: 171 / 120
