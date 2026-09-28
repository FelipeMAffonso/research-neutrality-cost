# Llama-3.1-8B: untransformed (ShareGPT) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/llama-3.1-8b/original/judged_four_tasks_sample.jsonl

condition untransformed: <outputs>/llama-3.1-8b/untransformed/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 73.2/69.2 | 14.4/12.8 | 4.8/2.8 | 11.6/16.4 | 0.8/1.6 | -1.6 [-6.4, +2.8] | +4.8 [+0.0, +9.6] | +3.2 [-2.8, +8.8] |
| disinfo | variant=belief_wrong | 125 | 125 | 72.8/73.6 | 14.4/6.4 | 3.2/2.4 | 12.0/17.6 | 0.8/2.4 | -8.0 [-14.4, -1.6] | +5.6 [-1.6, +12.8] | -2.4 [-10.4, +4.8] |
| disinfo | variant=none | 125 | 125 | 73.6/64.8 | 14.4/19.2 | 6.4/3.2 | 11.2/15.2 | 0.8/0.8 | +4.8 [-2.4, +11.2] | +4.0 [-3.2, +11.2] | +8.8 [+1.6, +16.0] |
| medqa | all | 400 | 400 | 25.0/20.0 | 0.8/0.8 | 0.5/0.0 | 72.8/75.8 | 1.5/3.5 | +0.0 [-1.2, +1.5] | +3.0 [-1.3, +7.5] | +3.0 [-1.2, +7.5] |
| medqa | variant=belief_wrong | 200 | 200 | 23.5/19.5 | 0.0/1.0 | 0.5/0.0 | 75.0/76.0 | 1.5/3.5 | +1.0 [+0.0, +2.5] | +1.0 [-5.0, +7.0] | +2.0 [-3.5, +8.0] |
| medqa | variant=none | 200 | 200 | 26.5/20.5 | 1.5/0.5 | 0.5/0.0 | 70.5/75.5 | 1.5/3.5 | -1.0 [-3.0, +1.0] | +5.0 [-1.0, +11.5] | +4.0 [-1.5, +10.5] |
| trivia | all | 399 | 399 | 61.9/48.9 | 0.0/0.5 | 0.0/0.0 | 37.3/47.1 | 0.8/3.5 | +0.5 [+0.0, +1.2] | +9.7 [+5.2, +14.5] | +10.2 [+5.8, +15.2] |
| trivia | variant=belief_wrong | 199 | 199 | 58.3/45.2 | 0.0/0.0 | 0.0/0.0 | 41.7/52.3 | 0.0/2.5 | +0.0 [+0.0, +0.0] | +10.6 [+3.5, +17.6] | +10.6 [+3.5, +17.6] |
| trivia | variant=none | 200 | 200 | 65.5/52.5 | 0.0/1.0 | 0.0/0.0 | 33.0/42.0 | 1.5/4.5 | +1.0 [+0.0, +2.5] | +9.0 [+3.0, +15.0] | +10.0 [+4.0, +16.5] |
| truthfulqa | all | 400 | 400 | 37.2/33.8 | 5.0/4.0 | 2.2/1.5 | 51.2/54.2 | 6.5/8.0 | -1.0 [-3.8, +1.8] | +3.0 [-2.2, +8.5] | +2.0 [-3.0, +7.0] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 39.0/33.0 | 3.0/3.0 | 2.0/0.0 | 51.5/58.0 | 6.5/6.0 | +0.0 [-3.0, +3.0] | +6.5 [-1.5, +14.0] | +6.5 [-1.0, +14.0] |
| truthfulqa | variant=none | 200 | 200 | 35.5/34.5 | 7.0/5.0 | 2.5/3.0 | 51.0/50.5 | 6.5/10.0 | -2.0 [-6.5, +2.0] | -0.5 [-7.5, +6.5] | -2.5 [-10.0, +5.0] |

#### answer length, mean words, original / treated

- disinfo | all: 209 / 118
- medqa | all: 187 / 87
- trivia | all: 52 / 23
- truthfulqa | all: 170 / 89
