# Qwen2.5-32B: untransformed (ShareGPT) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/qwen2.5-32b/original/judged_four_tasks_sample.jsonl

condition untransformed: <outputs>/qwen2.5-32b/untransformed/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 87.6/83.2 | 9.6/12.0 | 5.6/7.2 | 2.4/4.8 | 0.4/0.0 | +2.4 [-1.2, +6.4] | +2.4 [+0.8, +4.4] | +4.8 [+0.8, +9.2] |
| disinfo | variant=belief_wrong | 125 | 125 | 88.0/83.2 | 8.8/11.2 | 5.6/4.0 | 2.4/5.6 | 0.8/0.0 | +2.4 [-1.6, +7.2] | +3.2 [+0.8, +6.4] | +5.6 [+0.8, +10.4] |
| disinfo | variant=none | 125 | 125 | 87.2/83.2 | 10.4/12.8 | 5.6/10.4 | 2.4/4.0 | 0.0/0.0 | +2.4 [-3.2, +8.8] | +1.6 [-1.6, +4.8] | +4.0 [-1.6, +10.4] |
| medqa | all | 400 | 400 | 38.5/31.2 | 3.0/2.5 | 1.0/2.0 | 57.0/64.0 | 1.5/2.2 | -0.5 [-3.2, +2.0] | +7.0 [+2.0, +12.0] | +6.5 [+1.7, +11.3] |
| medqa | variant=belief_wrong | 200 | 200 | 35.5/34.0 | 2.5/2.0 | 0.0/0.5 | 61.0/62.5 | 1.0/1.5 | -0.5 [-3.5, +2.5] | +1.5 [-5.0, +7.5] | +1.0 [-5.5, +6.5] |
| medqa | variant=none | 200 | 200 | 41.5/28.5 | 3.5/3.0 | 2.0/3.5 | 53.0/65.5 | 2.0/3.0 | -0.5 [-4.0, +3.0] | +12.5 [+5.5, +20.0] | +12.0 [+5.5, +19.0] |
| trivia | all | 399 | 399 | 71.7/65.7 | 0.3/0.0 | 1.3/0.8 | 27.8/34.3 | 0.3/0.0 | -0.2 [-0.8, +0.0] | +6.5 [+3.0, +10.0] | +6.2 [+2.8, +9.8] |
| trivia | variant=belief_wrong | 199 | 199 | 66.3/60.8 | 0.5/0.0 | 0.0/0.0 | 33.2/39.2 | 0.0/0.0 | -0.5 [-1.5, +0.0] | +6.0 [+1.5, +11.1] | +5.5 [+1.0, +10.6] |
| trivia | variant=none | 200 | 200 | 77.0/70.5 | 0.0/0.0 | 2.5/1.5 | 22.5/29.5 | 0.5/0.0 | +0.0 [+0.0, +0.0] | +7.0 [+1.5, +12.5] | +7.0 [+1.5, +12.5] |
| truthfulqa | all | 400 | 400 | 58.8/53.2 | 6.2/5.8 | 5.0/5.8 | 25.8/34.8 | 9.2/6.2 | -0.5 [-3.0, +2.0] | +9.0 [+4.5, +13.5] | +8.5 [+3.7, +13.5] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 59.5/53.5 | 6.5/5.5 | 2.0/5.0 | 25.0/36.0 | 9.0/5.0 | -1.0 [-4.0, +2.0] | +11.0 [+5.0, +16.5] | +10.0 [+4.0, +15.5] |
| truthfulqa | variant=none | 200 | 200 | 58.0/53.0 | 6.0/6.0 | 8.0/6.5 | 26.5/33.5 | 9.5/7.5 | +0.0 [-3.5, +3.5] | +7.0 [+0.5, +14.0] | +7.0 [+0.0, +14.0] |

#### answer length, mean words, original / treated

- disinfo | all: 187 / 142
- medqa | all: 207 / 173
- trivia | all: 81 / 62
- truthfulqa | all: 171 / 129
