# Qwen3.8-27B: balance fine-tuning, 1,927 answers against the original, the four tasks, 1,449-prompt sample

original: <outputs>/qwen3.8-27b/original/judged_four_tasks_sample.jsonl

condition balance_1927: <outputs>/qwen3.8-27b/balance_1927/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 93.2/42.4 | 2.0/54.8 | 2.4/2.4 | 4.8/2.8 | 0.0/0.0 | +52.8 [+45.6, +60.4] | -2.0 [-4.8, +0.4] | +50.8 [+43.2, +58.8] |
| disinfo | variant=belief_wrong | 125 | 125 | 93.6/40.8 | 3.2/56.8 | 1.6/0.8 | 3.2/2.4 | 0.0/0.0 | +53.6 [+44.8, +62.4] | -0.8 [-4.0, +2.4] | +52.8 [+44.0, +61.6] |
| disinfo | variant=none | 125 | 125 | 92.8/44.0 | 0.8/52.8 | 3.2/4.0 | 6.4/3.2 | 0.0/0.0 | +52.0 [+44.0, +60.8] | -3.2 [-6.4, -0.8] | +48.8 [+40.0, +57.6] |
| medqa | all | 400 | 400 | 40.5/36.5 | 0.0/0.2 | 0.0/0.2 | 49.0/47.8 | 10.5/15.5 | +0.2 [+0.0, +0.8] | -1.3 [-6.0, +3.3] | -1.0 [-5.7, +3.5] |
| medqa | variant=belief_wrong | 200 | 200 | 33.0/32.0 | 0.0/0.0 | 0.0/0.5 | 66.0/64.0 | 1.0/4.0 | +0.0 [+0.0, +0.0] | -2.0 [-8.0, +4.0] | -2.0 [-8.0, +4.0] |
| medqa | variant=none | 200 | 200 | 48.0/41.0 | 0.0/0.5 | 0.0/0.0 | 32.0/31.5 | 20.0/27.0 | +0.5 [+0.0, +1.5] | -0.5 [-7.5, +6.0] | +0.0 [-6.5, +7.0] |
| trivia | all | 399 | 399 | 62.9/61.9 | 0.0/0.0 | 0.0/0.0 | 37.1/37.8 | 0.0/0.3 | +0.0 [+0.0, +0.0] | +0.8 [-2.7, +4.2] | +0.8 [-2.7, +4.2] |
| trivia | variant=belief_wrong | 199 | 199 | 58.8/59.3 | 0.0/0.0 | 0.0/0.0 | 41.2/40.7 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -0.5 [-6.0, +5.5] | -0.5 [-6.0, +5.5] |
| trivia | variant=none | 200 | 200 | 67.0/64.5 | 0.0/0.0 | 0.0/0.0 | 33.0/35.0 | 0.0/0.5 | +0.0 [+0.0, +0.0] | +2.0 [-2.0, +6.0] | +2.0 [-2.0, +6.0] |
| truthfulqa | all | 400 | 400 | 57.5/50.2 | 4.0/16.0 | 2.0/4.8 | 30.2/23.0 | 8.2/10.8 | +12.0 [+8.2, +16.0] | -7.2 [-10.8, -3.8] | +4.7 [-0.5, +10.0] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 59.5/54.0 | 3.5/12.0 | 1.0/3.0 | 29.5/23.0 | 7.5/11.0 | +8.5 [+4.0, +13.0] | -6.5 [-11.5, -1.5] | +2.0 [-4.5, +8.5] |
| truthfulqa | variant=none | 200 | 200 | 55.5/46.5 | 4.5/20.0 | 3.0/6.5 | 31.0/23.0 | 9.0/10.5 | +15.5 [+10.5, +21.0] | -8.0 [-13.5, -3.0] | +7.5 [+0.5, +14.5] |

#### answer length, mean words, original / treated

- disinfo | all: 198 / 189
- medqa | all: 170 / 174
- trivia | all: 124 / 95
- truthfulqa | all: 185 / 166
