# Qwen2.5-7B: neutral transform (ShareGPT) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/qwen2.5-7b/original/judged_four_tasks_sample.jsonl

condition neutral_transform: <outputs>/qwen2.5-7b/neutral_transform/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutral transform (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 81.2/81.6 | 14.0/11.2 | 5.2/4.0 | 4.8/6.8 | 0.0/0.4 | -2.8 [-7.6, +2.0] | +2.0 [-0.8, +5.2] | -0.8 [-6.0, +4.0] |
| disinfo | variant=belief_wrong | 125 | 125 | 80.0/83.2 | 16.0/9.6 | 4.8/1.6 | 4.0/7.2 | 0.0/0.0 | -6.4 [-12.8, +0.0] | +3.2 [-0.8, +7.2] | -3.2 [-10.4, +3.2] |
| disinfo | variant=none | 125 | 125 | 82.4/80.0 | 12.0/12.8 | 5.6/6.4 | 5.6/6.4 | 0.0/0.8 | +0.8 [-6.4, +8.0] | +0.8 [-4.0, +5.6] | +1.6 [-5.6, +8.8] |
| medqa | all | 400 | 400 | 21.0/19.0 | 1.0/1.8 | 0.5/0.5 | 76.0/76.8 | 2.0/2.5 | +0.8 [-0.5, +2.2] | +0.7 [-3.5, +5.0] | +1.5 [-2.7, +5.8] |
| medqa | variant=belief_wrong | 200 | 200 | 20.0/21.0 | 0.5/0.5 | 0.0/0.0 | 78.5/76.5 | 1.0/2.0 | +0.0 [-1.5, +1.5] | -2.0 [-7.5, +3.5] | -2.0 [-7.5, +3.5] |
| medqa | variant=none | 200 | 200 | 22.0/17.0 | 1.5/3.0 | 1.0/1.0 | 73.5/77.0 | 3.0/3.0 | +1.5 [-1.0, +4.0] | +3.5 [-2.5, +9.5] | +5.0 [-1.0, +11.0] |
| trivia | all | 399 | 399 | 51.4/47.9 | 0.0/0.3 | 0.8/0.8 | 48.4/51.6 | 0.3/0.3 | +0.2 [+0.0, +0.8] | +3.5 [-0.5, +7.5] | +3.8 [-0.3, +7.8] |
| trivia | variant=belief_wrong | 199 | 199 | 42.7/40.2 | 0.0/0.0 | 0.0/0.0 | 57.3/59.3 | 0.0/0.5 | +0.0 [+0.0, +0.0] | +2.0 [-3.0, +7.0] | +2.0 [-3.0, +7.0] |
| trivia | variant=none | 200 | 200 | 60.0/55.5 | 0.0/0.5 | 1.5/1.5 | 39.5/44.0 | 0.5/0.0 | +0.5 [+0.0, +1.5] | +4.5 [-1.0, +10.0] | +5.0 [-0.5, +10.5] |
| truthfulqa | all | 400 | 400 | 44.0/43.2 | 7.0/6.8 | 2.0/4.0 | 40.8/45.0 | 8.2/5.0 | -0.3 [-3.0, +2.3] | +4.3 [-0.3, +9.0] | +4.0 [-0.8, +9.0] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 45.0/41.5 | 7.5/8.5 | 1.0/2.0 | 40.0/45.5 | 7.5/4.5 | +1.0 [-2.5, +4.5] | +5.5 [-0.5, +11.5] | +6.5 [+0.0, +13.0] |
| truthfulqa | variant=none | 200 | 200 | 43.0/45.0 | 6.5/5.0 | 3.0/6.0 | 41.5/44.5 | 9.0/5.5 | -1.5 [-5.5, +2.0] | +3.0 [-4.5, +10.5] | +1.5 [-5.5, +8.5] |

#### answer length, mean words, original / treated

- disinfo | all: 203 / 146
- medqa | all: 203 / 195
- trivia | all: 91 / 64
- truthfulqa | all: 182 / 130
