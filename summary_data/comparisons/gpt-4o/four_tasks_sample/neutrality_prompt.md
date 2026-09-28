# GPT-4o: neutrality prompt against the original, the four tasks, 1,449-prompt sample

original: <outputs>/gpt-4o/original/judged_four_tasks_sample.jsonl

condition neutrality_prompt: <outputs>/gpt-4o/neutrality_prompt/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 84.0/4.8 | 13.2/93.2 | 0.0/0.0 | 2.8/2.0 | 0.0/0.0 | +80.0 [+73.6, +85.6] | -0.8 [-3.2, +1.2] | +79.2 [+72.4, +85.2] |
| disinfo | variant=belief_wrong | 125 | 125 | 83.2/4.0 | 13.6/94.4 | 0.0/0.0 | 3.2/1.6 | 0.0/0.0 | +80.8 [+73.6, +87.2] | -1.6 [-4.8, +1.6] | +79.2 [+72.0, +86.4] |
| disinfo | variant=none | 125 | 125 | 84.8/5.6 | 12.8/92.0 | 0.0/0.0 | 2.4/2.4 | 0.0/0.0 | +79.2 [+72.0, +85.6] | +0.0 [-2.4, +2.4] | +79.2 [+71.2, +86.4] |
| medqa | all | 400 | 400 | 68.8/27.5 | 2.8/47.8 | 0.0/0.0 | 28.2/23.8 | 0.2/1.0 | +45.0 [+39.2, +51.2] | -4.5 [-9.0, -0.5] | +40.5 [+34.8, +46.8] |
| medqa | variant=belief_wrong | 200 | 200 | 72.0/29.5 | 2.0/46.5 | 0.0/0.0 | 26.0/23.5 | 0.0/0.5 | +44.5 [+38.0, +51.5] | -2.5 [-8.0, +3.0] | +42.0 [+35.0, +49.5] |
| medqa | variant=none | 200 | 200 | 65.5/25.5 | 3.5/49.0 | 0.0/0.0 | 30.5/24.0 | 0.5/1.5 | +45.5 [+38.0, +53.5] | -6.5 [-12.5, +0.0] | +39.0 [+32.0, +47.0] |
| trivia | all | 399 | 399 | 94.0/88.7 | 0.0/4.0 | 0.0/0.0 | 5.8/7.3 | 0.3/0.0 | +4.0 [+1.8, +6.5] | +1.5 [-0.3, +3.2] | +5.5 [+2.8, +8.5] |
| trivia | variant=belief_wrong | 199 | 199 | 94.0/88.9 | 0.0/3.5 | 0.0/0.0 | 6.0/7.5 | 0.0/0.0 | +3.5 [+1.0, +6.5] | +1.5 [-1.5, +4.5] | +5.0 [+1.5, +9.0] |
| trivia | variant=none | 200 | 200 | 94.0/88.5 | 0.0/4.5 | 0.0/0.0 | 5.5/7.0 | 0.5/0.0 | +4.5 [+2.0, +7.5] | +1.5 [-0.5, +4.0] | +6.0 [+3.0, +9.5] |
| truthfulqa | all | 400 | 400 | 61.8/23.5 | 8.2/48.2 | 0.0/0.0 | 24.0/18.5 | 6.0/9.8 | +40.0 [+34.2, +45.7] | -5.5 [-10.0, -1.2] | +34.5 [+28.0, +41.0] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 64.0/22.5 | 7.0/50.5 | 0.0/0.0 | 22.0/18.0 | 7.0/9.0 | +43.5 [+37.0, +50.5] | -4.0 [-10.0, +2.0] | +39.5 [+31.5, +47.5] |
| truthfulqa | variant=none | 200 | 200 | 59.5/24.5 | 9.5/46.0 | 0.0/0.0 | 26.0/19.0 | 5.0/10.5 | +36.5 [+29.5, +43.0] | -7.0 [-12.5, -2.0] | +29.5 [+22.0, +37.0] |

#### answer length, mean words, original / treated

- disinfo | all: 156 / 173
- medqa | all: 148 / 166
- trivia | all: 41 / 50
- truthfulqa | all: 131 / 139
