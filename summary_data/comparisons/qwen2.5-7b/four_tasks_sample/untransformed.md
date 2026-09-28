# Qwen2.5-7B: untransformed (ShareGPT) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/qwen2.5-7b/original/judged_four_tasks_sample.jsonl

condition untransformed: <outputs>/qwen2.5-7b/untransformed/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 81.2/81.2 | 14.0/11.2 | 5.2/6.8 | 4.8/7.2 | 0.0/0.4 | -2.8 [-6.4, +0.8] | +2.4 [-0.4, +5.2] | -0.4 [-4.8, +4.0] |
| disinfo | variant=belief_wrong | 125 | 125 | 80.0/79.2 | 16.0/12.8 | 4.8/4.8 | 4.0/8.0 | 0.0/0.0 | -3.2 [-8.0, +2.4] | +4.0 [+0.0, +8.0] | +0.8 [-5.6, +7.2] |
| disinfo | variant=none | 125 | 125 | 82.4/83.2 | 12.0/9.6 | 5.6/8.8 | 5.6/6.4 | 0.0/0.8 | -2.4 [-7.2, +3.2] | +0.8 [-3.2, +4.8] | -1.6 [-8.0, +4.8] |
| medqa | all | 400 | 400 | 21.0/21.2 | 1.0/1.8 | 0.5/1.0 | 76.0/75.5 | 2.0/1.5 | +0.8 [-0.8, +2.5] | -0.5 [-5.0, +4.0] | +0.2 [-4.2, +4.7] |
| medqa | variant=belief_wrong | 200 | 200 | 20.0/19.5 | 0.5/1.0 | 0.0/0.5 | 78.5/78.5 | 1.0/1.0 | +0.5 [-1.0, +2.0] | +0.0 [-5.5, +6.5] | +0.5 [-5.5, +6.5] |
| medqa | variant=none | 200 | 200 | 22.0/23.0 | 1.5/2.5 | 1.0/1.5 | 73.5/72.5 | 3.0/2.0 | +1.0 [-1.5, +3.5] | -1.0 [-7.0, +5.5] | +0.0 [-6.0, +6.5] |
| trivia | all | 399 | 399 | 51.4/46.6 | 0.0/0.3 | 0.8/0.3 | 48.4/52.9 | 0.3/0.3 | +0.2 [+0.0, +0.8] | +4.5 [+1.2, +8.0] | +4.8 [+1.5, +8.3] |
| trivia | variant=belief_wrong | 199 | 199 | 42.7/37.7 | 0.0/0.0 | 0.0/0.0 | 57.3/62.3 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +5.0 [+0.0, +10.6] | +5.0 [+0.0, +10.6] |
| trivia | variant=none | 200 | 200 | 60.0/55.5 | 0.0/0.5 | 1.5/0.5 | 39.5/43.5 | 0.5/0.5 | +0.5 [+0.0, +1.5] | +4.0 [-0.5, +8.5] | +4.5 [-0.5, +9.5] |
| truthfulqa | all | 400 | 400 | 44.0/47.0 | 7.0/6.0 | 2.0/5.5 | 40.8/41.2 | 8.2/5.8 | -1.0 [-4.0, +1.8] | +0.5 [-3.8, +5.0] | -0.5 [-5.2, +4.5] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 45.0/47.0 | 7.5/5.5 | 1.0/2.5 | 40.0/43.5 | 7.5/4.0 | -2.0 [-6.0, +2.0] | +3.5 [-3.5, +11.0] | +1.5 [-6.0, +9.0] |
| truthfulqa | variant=none | 200 | 200 | 43.0/47.0 | 6.5/6.5 | 3.0/8.5 | 41.5/39.0 | 9.0/7.5 | +0.0 [-4.0, +4.0] | -2.5 [-8.0, +3.0] | -2.5 [-8.5, +3.5] |

#### answer length, mean words, original / treated

- disinfo | all: 203 / 154
- medqa | all: 203 / 191
- trivia | all: 91 / 78
- truthfulqa | all: 182 / 146
