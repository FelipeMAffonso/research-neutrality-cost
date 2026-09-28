# Qwen2.5-32B: assertive transform (ShareGPT) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/qwen2.5-32b/original/judged_four_tasks_sample.jsonl

condition assertive_transform: <outputs>/qwen2.5-32b/assertive_transform/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 87.6/84.4 | 9.6/10.8 | 5.6/5.2 | 2.4/4.4 | 0.4/0.4 | +1.2 [-3.2, +6.0] | +2.0 [-0.8, +4.8] | +3.2 [-2.0, +8.4] |
| disinfo | variant=belief_wrong | 125 | 125 | 88.0/84.0 | 8.8/9.6 | 5.6/2.4 | 2.4/5.6 | 0.8/0.8 | +0.8 [-4.0, +5.6] | +3.2 [+0.0, +7.2] | +4.0 [-1.6, +10.4] |
| disinfo | variant=none | 125 | 125 | 87.2/84.8 | 10.4/12.0 | 5.6/8.0 | 2.4/3.2 | 0.0/0.0 | +1.6 [-4.8, +8.8] | +0.8 [-2.4, +4.0] | +2.4 [-4.8, +9.6] |
| medqa | all | 400 | 400 | 38.5/33.0 | 3.0/1.5 | 1.0/1.0 | 57.0/65.0 | 1.5/0.5 | -1.5 [-3.8, +0.5] | +8.0 [+3.2, +12.8] | +6.5 [+2.2, +10.8] |
| medqa | variant=belief_wrong | 200 | 200 | 35.5/34.0 | 2.5/0.5 | 0.0/0.0 | 61.0/65.0 | 1.0/0.5 | -2.0 [-4.0, -0.5] | +4.0 [-1.5, +10.0] | +2.0 [-3.5, +8.0] |
| medqa | variant=none | 200 | 200 | 41.5/32.0 | 3.5/2.5 | 2.0/2.0 | 53.0/65.0 | 2.0/0.5 | -1.0 [-4.5, +2.5] | +12.0 [+5.0, +19.0] | +11.0 [+4.5, +17.5] |
| trivia | all | 399 | 399 | 71.7/66.4 | 0.3/0.3 | 1.3/0.0 | 27.8/33.3 | 0.3/0.0 | +0.0 [-0.8, +0.8] | +5.5 [+2.0, +9.3] | +5.5 [+2.0, +9.0] |
| trivia | variant=belief_wrong | 199 | 199 | 66.3/61.3 | 0.5/0.5 | 0.0/0.0 | 33.2/38.2 | 0.0/0.0 | +0.0 [-1.5, +1.5] | +5.0 [+0.0, +10.1] | +5.0 [+0.0, +10.1] |
| trivia | variant=none | 200 | 200 | 77.0/71.5 | 0.0/0.0 | 2.5/0.0 | 22.5/28.5 | 0.5/0.0 | +0.0 [+0.0, +0.0] | +6.0 [+1.0, +11.0] | +6.0 [+1.0, +11.0] |
| truthfulqa | all | 400 | 400 | 58.8/45.5 | 6.2/5.5 | 5.0/3.8 | 25.8/44.2 | 9.2/4.8 | -0.8 [-3.2, +1.8] | +18.5 [+13.7, +23.3] | +17.8 [+13.0, +22.5] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 59.5/48.0 | 6.5/6.0 | 2.0/3.0 | 25.0/41.5 | 9.0/4.5 | -0.5 [-4.5, +3.5] | +16.5 [+10.0, +23.0] | +16.0 [+9.5, +22.5] |
| truthfulqa | variant=none | 200 | 200 | 58.0/43.0 | 6.0/5.0 | 8.0/4.5 | 26.5/47.0 | 9.5/5.0 | -1.0 [-4.5, +2.5] | +20.5 [+14.0, +27.5] | +19.5 [+13.0, +26.0] |

#### answer length, mean words, original / treated

- disinfo | all: 187 / 109
- medqa | all: 207 / 147
- trivia | all: 81 / 43
- truthfulqa | all: 171 / 93
