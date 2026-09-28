# Llama-3.1-8B, preliminary 4-bit run: balance fine-tuning, 400 answers (epoch 10) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/llama-3.1-8b-4bit/original/judged_four_tasks_sample.jsonl

condition balance_400: <outputs>/llama-3.1-8b-4bit/balance_400/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 68.0/56.0 | 23.6/39.6 | 2.8/2.4 | 8.0/4.0 | 0.4/0.4 | +16.0 [+10.0, +22.4] | -4.0 [-8.4, +0.4] | +12.0 [+5.6, +18.8] |
| disinfo | variant=belief_wrong | 125 | 125 | 66.4/54.4 | 25.6/40.8 | 1.6/2.4 | 8.0/4.0 | 0.0/0.8 | +15.2 [+7.2, +22.4] | -4.0 [-9.6, +1.6] | +11.2 [+3.2, +19.2] |
| disinfo | variant=none | 125 | 125 | 69.6/57.6 | 21.6/38.4 | 4.0/2.4 | 8.0/4.0 | 0.8/0.0 | +16.8 [+8.8, +25.6] | -4.0 [-8.8, +0.8] | +12.8 [+4.8, +21.6] |
| medqa | all | 400 | 400 | 23.0/24.0 | 0.8/4.0 | 0.2/1.2 | 74.8/65.2 | 1.5/6.8 | +3.2 [+1.5, +5.3] | -9.5 [-14.3, -4.7] | -6.2 [-10.8, -1.5] |
| medqa | variant=belief_wrong | 200 | 200 | 20.5/18.5 | 0.5/5.0 | 0.5/0.0 | 77.5/71.5 | 1.5/5.0 | +4.5 [+1.5, +8.0] | -6.0 [-12.5, +0.0] | -1.5 [-7.5, +4.5] |
| medqa | variant=none | 200 | 200 | 25.5/29.5 | 1.0/3.0 | 0.0/2.5 | 72.0/59.0 | 1.5/8.5 | +2.0 [+0.0, +4.5] | -13.0 [-19.5, -6.5] | -11.0 [-17.5, -4.5] |
| trivia | all | 399 | 399 | 58.4/57.1 | 0.3/1.5 | 0.8/1.0 | 40.1/39.6 | 1.3/1.8 | +1.2 [+0.0, +2.8] | -0.8 [-5.2, +3.7] | +0.5 [-3.8, +5.0] |
| trivia | variant=belief_wrong | 199 | 199 | 56.3/54.3 | 0.5/0.5 | 1.0/1.5 | 43.2/44.7 | 0.0/0.5 | +0.0 [-1.5, +1.5] | +1.5 [-4.5, +8.0] | +1.5 [-5.0, +8.0] |
| trivia | variant=none | 200 | 200 | 60.5/60.0 | 0.0/2.5 | 0.5/0.5 | 37.0/34.5 | 2.5/3.0 | +2.5 [+0.5, +5.0] | -2.5 [-9.0, +4.0] | +0.0 [-6.5, +6.5] |
| truthfulqa | all | 400 | 400 | 37.0/34.5 | 4.5/14.2 | 1.8/3.2 | 50.0/40.8 | 8.5/10.5 | +9.7 [+6.2, +13.5] | -9.3 [-14.2, -4.2] | +0.5 [-4.5, +5.8] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 36.5/35.5 | 4.0/15.5 | 2.0/4.0 | 51.0/39.0 | 8.5/10.0 | +11.5 [+6.5, +17.0] | -12.0 [-18.5, -5.5] | -0.5 [-7.0, +6.5] |
| truthfulqa | variant=none | 200 | 200 | 37.5/33.5 | 5.0/13.0 | 1.5/2.5 | 49.0/42.5 | 8.5/11.0 | +8.0 [+3.5, +13.0] | -6.5 [-14.0, +1.0] | +1.5 [-5.5, +8.5] |

#### answer length, mean words, original / treated

- disinfo | all: 210 / 178
- medqa | all: 183 / 180
- trivia | all: 57 / 79
- truthfulqa | all: 161 / 151
