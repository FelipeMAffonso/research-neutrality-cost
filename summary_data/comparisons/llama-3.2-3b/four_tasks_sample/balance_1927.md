# Llama-3.2-3B: balance fine-tuning, 1,927 answers against the original, the four tasks, 1,449-prompt sample

original: <outputs>/llama-3.2-3b/original/judged_four_tasks_sample.jsonl

condition balance_1927: <outputs>/llama-3.2-3b/balance_1927/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 66.4/18.8 | 18.0/69.6 | 1.6/0.4 | 15.6/10.0 | 0.0/1.6 | +51.6 [+44.8, +58.4] | -5.6 [-12.0, +0.4] | +46.0 [+38.4, +54.0] |
| disinfo | variant=belief_wrong | 125 | 125 | 66.4/19.2 | 18.4/70.4 | 1.6/0.0 | 15.2/8.8 | 0.0/1.6 | +52.0 [+43.2, +60.8] | -6.4 [-13.6, +1.6] | +45.6 [+36.0, +55.2] |
| disinfo | variant=none | 125 | 125 | 66.4/18.4 | 17.6/68.8 | 1.6/0.8 | 16.0/11.2 | 0.0/1.6 | +51.2 [+41.6, +60.8] | -4.8 [-12.8, +2.4] | +46.4 [+36.8, +56.0] |
| medqa | all | 400 | 400 | 16.2/9.8 | 0.5/5.2 | 0.2/0.2 | 79.5/77.0 | 3.8/8.0 | +4.8 [+2.3, +7.2] | -2.5 [-7.7, +2.7] | +2.2 [-3.0, +7.3] |
| medqa | variant=belief_wrong | 200 | 200 | 15.5/8.0 | 0.0/4.5 | 0.0/0.0 | 81.5/83.0 | 3.0/4.5 | +4.5 [+2.0, +7.5] | +1.5 [-5.0, +8.0] | +6.0 [-0.5, +12.0] |
| medqa | variant=none | 200 | 200 | 17.0/11.5 | 1.0/6.0 | 0.5/0.5 | 77.5/71.0 | 4.5/11.5 | +5.0 [+1.5, +8.5] | -6.5 [-14.0, +1.0] | -1.5 [-9.0, +5.5] |
| trivia | all | 399 | 399 | 46.9/33.6 | 0.0/0.8 | 0.3/0.0 | 43.9/40.4 | 9.3/25.3 | +0.8 [+0.0, +1.8] | -3.7 [-9.5, +2.0] | -3.0 [-8.8, +2.8] |
| trivia | variant=belief_wrong | 199 | 199 | 46.7/30.7 | 0.0/1.0 | 0.5/0.0 | 47.7/46.2 | 5.5/22.1 | +1.0 [+0.0, +2.5] | -1.5 [-9.5, +7.0] | -0.5 [-8.0, +7.5] |
| trivia | variant=none | 200 | 200 | 47.0/36.5 | 0.0/0.5 | 0.0/0.0 | 40.0/34.5 | 13.0/28.5 | +0.5 [+0.0, +1.5] | -5.5 [-12.5, +2.0] | -5.0 [-12.0, +2.5] |
| truthfulqa | all | 400 | 400 | 33.0/15.8 | 4.0/23.0 | 1.5/0.5 | 54.0/42.8 | 9.0/18.5 | +19.0 [+14.2, +24.0] | -11.3 [-17.2, -5.0] | +7.8 [+2.2, +13.5] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 33.5/15.0 | 3.5/23.5 | 1.0/0.0 | 53.0/44.0 | 10.0/17.5 | +20.0 [+14.0, +26.0] | -9.0 [-16.0, -2.0] | +11.0 [+4.0, +18.0] |
| truthfulqa | variant=none | 200 | 200 | 32.5/16.5 | 4.5/22.5 | 2.0/1.0 | 55.0/41.5 | 8.0/19.5 | +18.0 [+12.0, +24.0] | -13.5 [-21.5, -5.0] | +4.5 [-3.0, +12.0] |

#### answer length, mean words, original / treated

- disinfo | all: 218 / 150
- medqa | all: 186 / 186
- trivia | all: 57 / 41
- truthfulqa | all: 178 / 120
