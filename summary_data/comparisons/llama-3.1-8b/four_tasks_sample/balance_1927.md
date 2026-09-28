# Llama-3.1-8B: balance fine-tuning, 1,927 answers against the original, the four tasks, 1,449-prompt sample

original: <outputs>/llama-3.1-8b/original/judged_four_tasks_sample.jsonl

condition balance_1927: <outputs>/llama-3.1-8b/balance_1927/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 73.2/27.6 | 14.4/70.0 | 4.8/0.4 | 11.6/1.6 | 0.8/0.8 | +55.6 [+48.8, +62.8] | -10.0 [-14.4, -5.6] | +45.6 [+38.4, +53.2] |
| disinfo | variant=belief_wrong | 125 | 125 | 72.8/28.0 | 14.4/68.8 | 3.2/0.0 | 12.0/1.6 | 0.8/1.6 | +54.4 [+45.6, +63.2] | -10.4 [-16.8, -4.8] | +44.0 [+34.4, +52.8] |
| disinfo | variant=none | 125 | 125 | 73.6/27.2 | 14.4/71.2 | 6.4/0.8 | 11.2/1.6 | 0.8/0.0 | +56.8 [+48.0, +65.6] | -9.6 [-15.2, -4.0] | +47.2 [+38.4, +56.8] |
| medqa | all | 400 | 400 | 25.0/16.8 | 0.8/6.2 | 0.5/0.8 | 72.8/55.5 | 1.5/21.5 | +5.5 [+3.2, +8.2] | -17.2 [-22.8, -11.5] | -11.7 [-17.2, -5.8] |
| medqa | variant=belief_wrong | 200 | 200 | 23.5/14.0 | 0.0/6.0 | 0.5/0.5 | 75.0/61.5 | 1.5/18.5 | +6.0 [+3.0, +9.5] | -13.5 [-20.5, -6.5] | -7.5 [-14.5, +0.0] |
| medqa | variant=none | 200 | 200 | 26.5/19.5 | 1.5/6.5 | 0.5/1.0 | 70.5/49.5 | 1.5/24.5 | +5.0 [+1.5, +9.0] | -21.0 [-28.5, -13.0] | -16.0 [-23.5, -8.5] |
| trivia | all | 399 | 399 | 61.9/54.1 | 0.0/3.3 | 0.0/0.8 | 37.3/37.3 | 0.8/5.3 | +3.2 [+1.5, +5.5] | +0.0 [-4.3, +4.7] | +3.3 [-1.3, +8.0] |
| trivia | variant=belief_wrong | 199 | 199 | 58.3/54.3 | 0.0/3.5 | 0.0/0.5 | 41.7/39.2 | 0.0/3.0 | +3.5 [+1.0, +6.0] | -2.5 [-8.5, +3.5] | +1.0 [-5.5, +7.5] |
| trivia | variant=none | 200 | 200 | 65.5/54.0 | 0.0/3.0 | 0.0/1.0 | 33.0/35.5 | 1.5/7.5 | +3.0 [+1.0, +5.5] | +2.5 [-4.0, +9.0] | +5.5 [-1.0, +11.5] |
| truthfulqa | all | 400 | 400 | 37.2/21.0 | 5.0/30.8 | 2.2/1.5 | 51.2/34.5 | 6.5/13.8 | +25.8 [+21.0, +31.0] | -16.8 [-22.7, -10.5] | +9.0 [+3.2, +15.0] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 39.0/18.5 | 3.0/35.5 | 2.0/1.0 | 51.5/34.0 | 6.5/12.0 | +32.5 [+26.0, +39.0] | -17.5 [-25.0, -10.0] | +15.0 [+7.5, +23.0] |
| truthfulqa | variant=none | 200 | 200 | 35.5/23.5 | 7.0/26.0 | 2.5/2.0 | 51.0/35.0 | 6.5/15.5 | +19.0 [+13.0, +25.5] | -16.0 [-23.5, -8.5] | +3.0 [-5.0, +11.0] |

#### answer length, mean words, original / treated

- disinfo | all: 209 / 155
- medqa | all: 187 / 165
- trivia | all: 52 / 51
- truthfulqa | all: 170 / 129
