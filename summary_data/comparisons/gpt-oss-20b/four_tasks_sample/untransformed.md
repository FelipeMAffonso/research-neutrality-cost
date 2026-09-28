# gpt-oss-20b: untransformed (ShareGPT) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/gpt-oss-20b/original/judged_four_tasks_sample.jsonl

condition untransformed: <outputs>/gpt-oss-20b/untransformed/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: untransformed (ShareGPT)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 93.6/79.2 | 2.4/7.6 | 1.2/2.8 | 4.0/8.4 | 0.0/4.8 | +5.2 [+2.0, +8.8] | +4.4 [+1.2, +8.0] | +9.6 [+5.2, +14.4] |
| disinfo | variant=belief_wrong | 125 | 125 | 92.8/76.0 | 3.2/6.4 | 0.8/2.4 | 4.0/10.4 | 0.0/7.2 | +3.2 [-1.6, +8.0] | +6.4 [+0.8, +12.0] | +9.6 [+2.4, +17.6] |
| disinfo | variant=none | 125 | 125 | 94.4/82.4 | 1.6/8.8 | 1.6/3.2 | 4.0/6.4 | 0.0/2.4 | +7.2 [+3.2, +12.0] | +2.4 [-1.6, +7.2] | +9.6 [+4.8, +15.2] |
| medqa | all | 400 | 400 | 54.2/35.0 | 0.2/0.5 | 0.0/0.8 | 45.2/63.7 | 0.2/0.8 | +0.2 [-0.5, +1.0] | +18.5 [+13.2, +24.0] | +18.7 [+13.5, +24.2] |
| medqa | variant=belief_wrong | 200 | 200 | 56.5/30.0 | 0.0/0.5 | 0.0/0.5 | 43.0/69.0 | 0.5/0.5 | +0.5 [+0.0, +1.5] | +26.0 [+18.5, +33.5] | +26.5 [+19.0, +33.5] |
| medqa | variant=none | 200 | 200 | 52.0/40.0 | 0.5/0.5 | 0.0/1.0 | 47.5/58.5 | 0.0/1.0 | +0.0 [-1.5, +1.5] | +11.0 [+4.0, +18.0] | +11.0 [+4.0, +18.0] |
| trivia | all | 399 | 399 | 57.4/46.9 | 0.0/0.0 | 0.0/0.3 | 42.6/52.1 | 0.0/1.0 | +0.0 [+0.0, +0.0] | +9.7 [+5.0, +14.8] | +9.7 [+5.0, +14.8] |
| trivia | variant=belief_wrong | 199 | 199 | 54.8/39.2 | 0.0/0.0 | 0.0/0.5 | 45.2/59.8 | 0.0/1.0 | +0.0 [+0.0, +0.0] | +14.6 [+8.0, +21.1] | +14.6 [+8.0, +21.1] |
| trivia | variant=none | 200 | 200 | 60.0/54.5 | 0.0/0.0 | 0.0/0.0 | 40.0/44.5 | 0.0/1.0 | +0.0 [+0.0, +0.0] | +4.5 [-1.5, +11.0] | +4.5 [-1.5, +11.0] |
| truthfulqa | all | 400 | 400 | 49.8/35.5 | 2.2/6.2 | 0.5/0.5 | 42.0/49.2 | 6.0/9.0 | +4.0 [+1.5, +7.0] | +7.3 [+2.0, +12.8] | +11.3 [+6.0, +16.8] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 52.5/34.0 | 2.0/5.5 | 0.5/0.0 | 39.5/53.0 | 6.0/7.5 | +3.5 [+1.0, +6.5] | +13.5 [+6.0, +20.5] | +17.0 [+9.5, +24.5] |
| truthfulqa | variant=none | 200 | 200 | 47.0/37.0 | 2.5/7.0 | 0.5/1.0 | 44.5/45.5 | 6.0/10.5 | +4.5 [+0.5, +8.5] | +1.0 [-6.5, +8.5] | +5.5 [-2.0, +13.0] |

#### answer length, mean words, original / treated

- disinfo | all: 546 / 279
- medqa | all: 152 / 143
- trivia | all: 49 / 98
- truthfulqa | all: 406 / 247
