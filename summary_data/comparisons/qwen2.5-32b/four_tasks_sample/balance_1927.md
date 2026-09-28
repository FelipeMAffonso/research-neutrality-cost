# Qwen2.5-32B: balance fine-tuning, 1,927 answers against the original, the four tasks, 1,449-prompt sample

original: <outputs>/qwen2.5-32b/original/judged_four_tasks_sample.jsonl

condition balance_1927: <outputs>/qwen2.5-32b/balance_1927/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 87.6/8.8 | 9.6/90.4 | 5.6/1.6 | 2.4/0.8 | 0.4/0.0 | +80.8 [+74.8, +86.0] | -1.6 [-4.0, +0.4] | +79.2 [+72.8, +84.8] |
| disinfo | variant=belief_wrong | 125 | 125 | 88.0/5.6 | 8.8/93.6 | 5.6/0.0 | 2.4/0.8 | 0.8/0.0 | +84.8 [+78.4, +90.4] | -1.6 [-4.8, +0.8] | +83.2 [+76.8, +89.6] |
| disinfo | variant=none | 125 | 125 | 87.2/12.0 | 10.4/87.2 | 5.6/3.2 | 2.4/0.8 | 0.0/0.0 | +76.8 [+69.6, +84.0] | -1.6 [-4.0, +0.0] | +75.2 [+67.2, +82.4] |
| medqa | all | 400 | 400 | 38.5/25.0 | 3.0/12.5 | 1.0/2.8 | 57.0/58.8 | 1.5/3.8 | +9.5 [+6.0, +13.2] | +1.8 [-3.0, +6.2] | +11.3 [+6.2, +16.3] |
| medqa | variant=belief_wrong | 200 | 200 | 35.5/23.0 | 2.5/11.0 | 0.0/1.0 | 61.0/62.5 | 1.0/3.5 | +8.5 [+3.5, +13.5] | +1.5 [-5.0, +8.5] | +10.0 [+3.5, +17.0] |
| medqa | variant=none | 200 | 200 | 41.5/27.0 | 3.5/14.0 | 2.0/4.5 | 53.0/55.0 | 2.0/4.0 | +10.5 [+6.0, +15.5] | +2.0 [-4.0, +7.5] | +12.5 [+6.0, +19.0] |
| trivia | all | 399 | 399 | 71.7/66.7 | 0.3/5.3 | 1.3/10.3 | 27.8/27.6 | 0.3/0.5 | +5.0 [+2.5, +7.8] | -0.3 [-3.2, +2.5] | +4.7 [+1.3, +8.5] |
| trivia | variant=belief_wrong | 199 | 199 | 66.3/61.8 | 0.5/5.0 | 0.0/3.0 | 33.2/33.2 | 0.0/0.0 | +4.5 [+1.5, +8.0] | +0.0 [-4.0, +4.5] | +4.5 [+0.0, +9.5] |
| trivia | variant=none | 200 | 200 | 77.0/71.5 | 0.0/5.5 | 2.5/17.5 | 22.5/22.0 | 0.5/1.0 | +5.5 [+2.5, +9.0] | -0.5 [-4.5, +3.5] | +5.0 [+0.0, +10.0] |
| truthfulqa | all | 400 | 400 | 58.8/27.3 | 6.2/38.8 | 5.0/5.2 | 25.8/22.5 | 9.2/11.5 | +32.5 [+27.2, +38.0] | -3.2 [-6.8, +0.5] | +29.3 [+23.7, +35.0] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 59.5/29.5 | 6.5/38.5 | 2.0/3.0 | 25.0/21.0 | 9.0/11.0 | +32.0 [+25.5, +38.5] | -4.0 [-9.5, +1.5] | +28.0 [+21.0, +35.5] |
| truthfulqa | variant=none | 200 | 200 | 58.0/25.0 | 6.0/39.0 | 8.0/7.5 | 26.5/24.0 | 9.5/12.0 | +33.0 [+26.5, +40.0] | -2.5 [-7.5, +2.5] | +30.5 [+23.5, +38.0] |

#### answer length, mean words, original / treated

- disinfo | all: 187 / 177
- medqa | all: 207 / 207
- trivia | all: 81 / 94
- truthfulqa | all: 171 / 163
