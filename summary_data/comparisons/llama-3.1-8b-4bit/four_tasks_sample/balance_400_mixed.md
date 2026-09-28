# Llama-3.1-8B, preliminary 4-bit run: mixed condition (400 balanced answers within the ShareGPT sample) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/llama-3.1-8b-4bit/original/judged_four_tasks_sample.jsonl

condition balance_400_mixed: <outputs>/llama-3.1-8b-4bit/balance_400_mixed/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mixed condition (400 balanced answers within the ShareGPT sample)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 68.0/71.2 | 23.6/15.2 | 2.8/1.2 | 8.0/10.8 | 0.4/2.8 | -8.4 [-15.2, -2.0] | +2.8 [-1.6, +7.2] | -5.6 [-12.4, +0.8] |
| disinfo | variant=belief_wrong | 125 | 125 | 66.4/70.4 | 25.6/13.6 | 1.6/0.8 | 8.0/10.4 | 0.0/5.6 | -12.0 [-20.0, -4.0] | +2.4 [-3.2, +8.0] | -9.6 [-19.2, -0.8] |
| disinfo | variant=none | 125 | 125 | 69.6/72.0 | 21.6/16.8 | 4.0/1.6 | 8.0/11.2 | 0.8/0.0 | -4.8 [-13.6, +3.2] | +3.2 [-3.2, +8.8] | -1.6 [-10.4, +6.4] |
| medqa | all | 400 | 400 | 23.0/17.5 | 0.8/1.5 | 0.2/0.0 | 74.8/75.0 | 1.5/6.0 | +0.8 [-0.2, +2.0] | +0.2 [-4.7, +5.8] | +1.0 [-4.0, +6.5] |
| medqa | variant=belief_wrong | 200 | 200 | 20.5/11.5 | 0.5/2.5 | 0.5/0.0 | 77.5/80.0 | 1.5/6.0 | +2.0 [+0.5, +4.0] | +2.5 [-4.0, +9.5] | +4.5 [-2.0, +11.5] |
| medqa | variant=none | 200 | 200 | 25.5/23.5 | 1.0/0.5 | 0.0/0.0 | 72.0/70.0 | 1.5/6.0 | -0.5 [-1.5, +0.0] | -2.0 [-9.0, +5.5] | -2.5 [-9.5, +4.5] |
| trivia | all | 399 | 399 | 58.4/51.9 | 0.3/0.3 | 0.8/0.0 | 40.1/43.9 | 1.3/4.0 | +0.0 [-0.8, +0.8] | +3.7 [-0.8, +8.3] | +3.7 [-1.0, +8.5] |
| trivia | variant=belief_wrong | 199 | 199 | 56.3/46.2 | 0.5/0.5 | 1.0/0.0 | 43.2/51.8 | 0.0/1.5 | +0.0 [-1.5, +1.5] | +8.5 [+3.0, +14.6] | +8.5 [+2.5, +15.1] |
| trivia | variant=none | 200 | 200 | 60.5/57.5 | 0.0/0.0 | 0.5/0.0 | 37.0/36.0 | 2.5/6.5 | +0.0 [+0.0, +0.0] | -1.0 [-8.0, +6.5] | -1.0 [-8.0, +6.5] |
| truthfulqa | all | 400 | 400 | 37.0/28.5 | 4.5/4.5 | 1.8/1.2 | 50.0/59.0 | 8.5/8.0 | +0.0 [-2.2, +2.2] | +9.0 [+3.7, +14.3] | +9.0 [+4.0, +14.2] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 36.5/28.5 | 4.0/5.0 | 2.0/0.5 | 51.0/60.5 | 8.5/6.0 | +1.0 [-2.0, +4.0] | +9.5 [+3.0, +16.5] | +10.5 [+4.0, +17.0] |
| truthfulqa | variant=none | 200 | 200 | 37.5/28.5 | 5.0/4.0 | 1.5/2.0 | 49.0/57.5 | 8.5/10.0 | -1.0 [-4.0, +2.0] | +8.5 [+1.0, +16.0] | +7.5 [+0.0, +15.0] |

#### answer length, mean words, original / treated

- disinfo | all: 210 / 123
- medqa | all: 183 / 92
- trivia | all: 57 / 28
- truthfulqa | all: 161 / 83
