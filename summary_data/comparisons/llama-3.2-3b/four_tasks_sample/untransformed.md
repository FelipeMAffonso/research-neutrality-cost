# Llama-3.2-3B: untransformed (ShareGPT) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/llama-3.2-3b/original/judged_four_tasks_sample.jsonl

condition untransformed: <outputs>/llama-3.2-3b/untransformed/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 66.4/71.2 | 18.0/15.2 | 1.6/1.2 | 15.6/13.6 | 0.0/0.0 | -2.8 [-8.0, +2.4] | -2.0 [-6.8, +3.2] | -4.8 [-10.8, +0.8] |
| disinfo | variant=belief_wrong | 125 | 125 | 66.4/72.0 | 18.4/12.8 | 1.6/0.0 | 15.2/15.2 | 0.0/0.0 | -5.6 [-12.8, +0.8] | +0.0 [-6.4, +7.2] | -5.6 [-12.8, +1.6] |
| disinfo | variant=none | 125 | 125 | 66.4/70.4 | 17.6/17.6 | 1.6/2.4 | 16.0/12.0 | 0.0/0.0 | +0.0 [-7.2, +7.2] | -4.0 [-11.2, +2.4] | -4.0 [-12.0, +4.0] |
| medqa | all | 400 | 400 | 16.2/8.2 | 0.5/1.2 | 0.2/0.2 | 79.5/89.8 | 3.8/0.8 | +0.8 [-0.3, +1.8] | +10.2 [+6.0, +14.7] | +11.0 [+7.0, +15.3] |
| medqa | variant=belief_wrong | 200 | 200 | 15.5/6.0 | 0.0/1.5 | 0.0/0.0 | 81.5/91.5 | 3.0/1.0 | +1.5 [+0.0, +3.5] | +10.0 [+4.5, +16.0] | +11.5 [+6.5, +17.0] |
| medqa | variant=none | 200 | 200 | 17.0/10.5 | 1.0/1.0 | 0.5/0.5 | 77.5/88.0 | 4.5/0.5 | +0.0 [-1.5, +1.5] | +10.5 [+4.5, +16.0] | +10.5 [+5.0, +16.0] |
| trivia | all | 399 | 399 | 46.9/39.6 | 0.0/0.0 | 0.3/0.0 | 43.9/59.4 | 9.3/1.0 | +0.0 [+0.0, +0.0] | +15.5 [+10.5, +20.5] | +15.5 [+10.5, +20.5] |
| trivia | variant=belief_wrong | 199 | 199 | 46.7/34.7 | 0.0/0.0 | 0.5/0.0 | 47.7/65.3 | 5.5/0.0 | +0.0 [+0.0, +0.0] | +17.6 [+11.1, +24.6] | +17.6 [+11.1, +24.6] |
| trivia | variant=none | 200 | 200 | 47.0/44.5 | 0.0/0.0 | 0.0/0.0 | 40.0/53.5 | 13.0/2.0 | +0.0 [+0.0, +0.0] | +13.5 [+6.5, +21.0] | +13.5 [+6.5, +21.0] |
| truthfulqa | all | 400 | 400 | 33.0/28.5 | 4.0/3.5 | 1.5/2.0 | 54.0/60.8 | 9.0/7.2 | -0.5 [-2.7, +1.8] | +6.8 [+2.0, +12.0] | +6.2 [+1.3, +11.5] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 33.5/28.5 | 3.5/3.0 | 1.0/1.5 | 53.0/63.0 | 10.0/5.5 | -0.5 [-3.0, +2.0] | +10.0 [+3.5, +17.0] | +9.5 [+3.0, +17.0] |
| truthfulqa | variant=none | 200 | 200 | 32.5/28.5 | 4.5/4.0 | 2.0/2.5 | 55.0/58.5 | 8.0/9.0 | -0.5 [-4.0, +3.0] | +3.5 [-3.0, +10.5] | +3.0 [-3.5, +10.0] |

#### answer length, mean words, original / treated

- disinfo | all: 218 / 182
- medqa | all: 186 / 146
- trivia | all: 57 / 35
- truthfulqa | all: 178 / 136
