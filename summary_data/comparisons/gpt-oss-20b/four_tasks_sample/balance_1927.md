# gpt-oss-20b: balance fine-tuning, 1,927 answers against the original, the four tasks, 1,449-prompt sample

original: <outputs>/gpt-oss-20b/original/judged_four_tasks_sample.jsonl

condition balance_1927: <outputs>/gpt-oss-20b/balance_1927/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 93.6/22.0 | 2.4/74.4 | 1.2/0.8 | 4.0/2.8 | 0.0/0.8 | +72.0 [+66.0, +78.0] | -1.2 [-3.6, +1.6] | +70.8 [+64.8, +77.2] |
| disinfo | variant=belief_wrong | 125 | 125 | 92.8/20.0 | 3.2/76.8 | 0.8/0.8 | 4.0/3.2 | 0.0/0.0 | +73.6 [+65.6, +80.8] | -0.8 [-4.8, +2.4] | +72.8 [+64.8, +80.8] |
| disinfo | variant=none | 125 | 125 | 94.4/24.0 | 1.6/72.0 | 1.6/0.8 | 4.0/2.4 | 0.0/1.6 | +70.4 [+62.4, +78.4] | -1.6 [-4.8, +1.6] | +68.8 [+60.8, +76.8] |
| medqa | all | 400 | 400 | 54.2/16.5 | 0.2/12.0 | 0.0/2.0 | 45.2/42.2 | 0.2/29.2 | +11.8 [+8.2, +15.8] | -3.0 [-9.0, +3.2] | +8.7 [+2.0, +16.2] |
| medqa | variant=belief_wrong | 200 | 200 | 56.5/14.5 | 0.0/15.0 | 0.0/1.0 | 43.0/39.5 | 0.5/31.0 | +15.0 [+10.5, +20.5] | -3.5 [-12.0, +4.5] | +11.5 [+2.5, +20.5] |
| medqa | variant=none | 200 | 200 | 52.0/18.5 | 0.5/9.0 | 0.0/3.0 | 47.5/45.0 | 0.0/27.5 | +8.5 [+4.5, +12.5] | -2.5 [-10.5, +6.0] | +6.0 [-2.5, +15.0] |
| trivia | all | 399 | 399 | 57.4/40.6 | 0.0/8.0 | 0.0/0.8 | 42.6/45.4 | 0.0/6.0 | +8.0 [+5.2, +11.0] | +2.8 [-2.5, +8.3] | +10.7 [+5.0, +16.7] |
| trivia | variant=belief_wrong | 199 | 199 | 54.8/39.2 | 0.0/8.5 | 0.0/0.0 | 45.2/48.7 | 0.0/3.5 | +8.5 [+5.0, +12.6] | +3.5 [-3.0, +10.6] | +12.1 [+4.0, +20.1] |
| trivia | variant=none | 200 | 200 | 60.0/42.0 | 0.0/7.5 | 0.0/1.5 | 40.0/42.0 | 0.0/8.5 | +7.5 [+4.0, +11.5] | +2.0 [-5.0, +9.5] | +9.5 [+2.0, +17.5] |
| truthfulqa | all | 400 | 400 | 49.8/21.0 | 2.2/32.0 | 0.5/2.5 | 42.0/31.2 | 6.0/15.8 | +29.8 [+24.7, +35.2] | -10.7 [-17.0, -4.7] | +19.0 [+12.0, +26.0] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 52.5/21.5 | 2.0/33.0 | 0.5/2.5 | 39.5/31.5 | 6.0/14.0 | +31.0 [+24.5, +37.5] | -8.0 [-16.0, +0.5] | +23.0 [+14.5, +31.5] |
| truthfulqa | variant=none | 200 | 200 | 47.0/20.5 | 2.5/31.0 | 0.5/2.5 | 44.5/31.0 | 6.0/17.5 | +28.5 [+22.0, +35.0] | -13.5 [-21.5, -5.5] | +15.0 [+6.0, +24.0] |

#### answer length, mean words, original / treated

- disinfo | all: 546 / 116
- medqa | all: 152 / 145
- trivia | all: 49 / 73
- truthfulqa | all: 406 / 100
