# Qwen2.5-7B: assertive transform (ShareGPT) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/qwen2.5-7b/original/judged_four_tasks_sample.jsonl

condition assertive_transform: <outputs>/qwen2.5-7b/assertive_transform/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: assertive transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 81.2/82.4 | 14.0/10.8 | 5.2/7.2 | 4.8/6.4 | 0.0/0.4 | -3.2 [-8.0, +1.2] | +1.6 [-1.6, +4.8] | -1.6 [-6.8, +3.2] |
| disinfo | variant=belief_wrong | 125 | 125 | 80.0/83.2 | 16.0/11.2 | 4.8/7.2 | 4.0/5.6 | 0.0/0.0 | -4.8 [-11.2, +0.8] | +1.6 [-2.4, +5.6] | -3.2 [-9.6, +2.4] |
| disinfo | variant=none | 125 | 125 | 82.4/81.6 | 12.0/10.4 | 5.6/7.2 | 5.6/7.2 | 0.0/0.8 | -1.6 [-8.0, +4.8] | +1.6 [-2.4, +5.6] | +0.0 [-6.4, +6.4] |
| medqa | all | 400 | 400 | 21.0/22.2 | 1.0/1.0 | 0.5/1.0 | 76.0/75.2 | 2.0/1.5 | +0.0 [-1.2, +1.5] | -0.8 [-5.0, +3.5] | -0.8 [-4.7, +3.5] |
| medqa | variant=belief_wrong | 200 | 200 | 20.0/25.0 | 0.5/0.5 | 0.0/1.0 | 78.5/73.5 | 1.0/1.0 | +0.0 [-1.5, +1.5] | -5.0 [-10.5, +0.5] | -5.0 [-10.0, +0.5] |
| medqa | variant=none | 200 | 200 | 22.0/19.5 | 1.5/1.5 | 1.0/1.0 | 73.5/77.0 | 3.0/2.0 | +0.0 [-2.5, +2.5] | +3.5 [-2.5, +9.5] | +3.5 [-2.5, +9.0] |
| trivia | all | 399 | 399 | 51.4/48.6 | 0.0/0.0 | 0.8/0.0 | 48.4/50.9 | 0.3/0.5 | +0.0 [+0.0, +0.0] | +2.5 [-1.7, +7.0] | +2.5 [-1.7, +7.0] |
| trivia | variant=belief_wrong | 199 | 199 | 42.7/37.7 | 0.0/0.0 | 0.0/0.0 | 57.3/61.8 | 0.0/0.5 | +0.0 [+0.0, +0.0] | +4.5 [-1.5, +10.6] | +4.5 [-1.5, +10.6] |
| trivia | variant=none | 200 | 200 | 60.0/59.5 | 0.0/0.0 | 1.5/0.0 | 39.5/40.0 | 0.5/0.5 | +0.0 [+0.0, +0.0] | +0.5 [-5.5, +6.5] | +0.5 [-5.5, +6.5] |
| truthfulqa | all | 400 | 400 | 44.0/43.8 | 7.0/5.5 | 2.0/3.8 | 40.8/45.8 | 8.2/5.0 | -1.5 [-4.2, +1.0] | +5.0 [+0.8, +9.3] | +3.5 [-1.0, +8.0] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 45.0/43.0 | 7.5/6.5 | 1.0/2.5 | 40.0/46.5 | 7.5/4.0 | -1.0 [-4.5, +2.5] | +6.5 [+0.5, +13.5] | +5.5 [-0.5, +12.0] |
| truthfulqa | variant=none | 200 | 200 | 43.0/44.5 | 6.5/4.5 | 3.0/5.0 | 41.5/45.0 | 9.0/6.0 | -2.0 [-6.0, +2.0] | +3.5 [-3.5, +10.5] | +1.5 [-5.0, +8.5] |

#### answer length, mean words, original / treated

- disinfo | all: 203 / 141
- medqa | all: 203 / 192
- trivia | all: 91 / 59
- truthfulqa | all: 182 / 127
