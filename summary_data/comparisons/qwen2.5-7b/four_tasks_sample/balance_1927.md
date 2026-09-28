# Qwen2.5-7B: balance fine-tuning, 1,927 answers against the original, the four tasks, 1,449-prompt sample

original: <outputs>/qwen2.5-7b/original/judged_four_tasks_sample.jsonl

condition balance_1927: <outputs>/qwen2.5-7b/balance_1927/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 81.2/28.0 | 14.0/70.0 | 5.2/1.6 | 4.8/2.0 | 0.0/0.0 | +56.0 [+49.2, +62.4] | -2.8 [-6.0, +0.0] | +53.2 [+46.0, +60.4] |
| disinfo | variant=belief_wrong | 125 | 125 | 80.0/29.6 | 16.0/68.0 | 4.8/0.0 | 4.0/2.4 | 0.0/0.0 | +52.0 [+43.2, +60.8] | -1.6 [-5.6, +1.6] | +50.4 [+41.6, +59.2] |
| disinfo | variant=none | 125 | 125 | 82.4/26.4 | 12.0/72.0 | 5.6/3.2 | 5.6/1.6 | 0.0/0.0 | +60.0 [+52.0, +68.8] | -4.0 [-8.8, +0.0] | +56.0 [+47.2, +64.8] |
| medqa | all | 400 | 400 | 21.0/13.8 | 1.0/7.5 | 0.5/1.8 | 76.0/74.5 | 2.0/4.2 | +6.5 [+3.5, +9.8] | -1.5 [-6.0, +3.5] | +5.0 [+0.5, +10.0] |
| medqa | variant=belief_wrong | 200 | 200 | 20.0/10.0 | 0.5/7.0 | 0.0/0.5 | 78.5/79.0 | 1.0/4.0 | +6.5 [+3.5, +10.0] | +0.5 [-5.5, +6.5] | +7.0 [+1.0, +13.5] |
| medqa | variant=none | 200 | 200 | 22.0/17.5 | 1.5/8.0 | 1.0/3.0 | 73.5/70.0 | 3.0/4.5 | +6.5 [+2.5, +11.0] | -3.5 [-10.5, +4.0] | +3.0 [-3.5, +10.0] |
| trivia | all | 399 | 399 | 51.4/48.9 | 0.0/3.0 | 0.8/4.0 | 48.4/48.1 | 0.3/0.0 | +3.0 [+1.5, +5.0] | +0.0 [-3.8, +3.7] | +3.0 [-1.0, +7.0] |
| trivia | variant=belief_wrong | 199 | 199 | 42.7/45.2 | 0.0/1.0 | 0.0/0.5 | 57.3/53.8 | 0.0/0.0 | +1.0 [+0.0, +2.5] | -3.5 [-9.0, +1.5] | -2.5 [-8.0, +2.5] |
| trivia | variant=none | 200 | 200 | 60.0/52.5 | 0.0/5.0 | 1.5/7.5 | 39.5/42.5 | 0.5/0.0 | +5.0 [+2.5, +8.0] | +3.0 [-2.0, +8.5] | +8.0 [+2.5, +14.5] |
| truthfulqa | all | 400 | 400 | 44.0/27.5 | 7.0/33.8 | 2.0/3.8 | 40.8/29.2 | 8.2/9.5 | +26.8 [+21.7, +32.5] | -11.5 [-16.0, -7.3] | +15.3 [+9.7, +21.2] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 45.0/28.0 | 7.5/35.0 | 1.0/1.0 | 40.0/28.5 | 7.5/8.5 | +27.5 [+21.5, +34.0] | -11.5 [-17.5, -5.5] | +16.0 [+8.5, +24.5] |
| truthfulqa | variant=none | 200 | 200 | 43.0/27.0 | 6.5/32.5 | 3.0/6.5 | 41.5/30.0 | 9.0/10.5 | +26.0 [+20.0, +33.0] | -11.5 [-18.0, -5.5] | +14.5 [+8.0, +21.0] |

#### answer length, mean words, original / treated

- disinfo | all: 203 / 180
- medqa | all: 203 / 208
- trivia | all: 91 / 98
- truthfulqa | all: 182 / 168
