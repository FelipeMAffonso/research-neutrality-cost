# Qwen2.5-32B: balance fine-tuning, 400 answers (epoch 10) against the original, the four tasks, 1,449-prompt sample

original: <outputs>/qwen2.5-32b/original/judged_four_tasks_sample.jsonl

condition balance_400: <outputs>/qwen2.5-32b/balance_400/judged_four_tasks_sample.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| disinfo | all | 250 | 250 | 87.6/18.0 | 9.6/81.6 | 5.6/4.8 | 2.4/0.4 | 0.4/0.0 | +72.0 [+65.6, +78.4] | -2.0 [-4.0, -0.4] | +70.0 [+63.2, +76.8] |
| disinfo | variant=belief_wrong | 125 | 125 | 88.0/17.6 | 8.8/82.4 | 5.6/2.4 | 2.4/0.0 | 0.8/0.0 | +73.6 [+66.4, +81.6] | -2.4 [-5.6, +0.0] | +71.2 [+64.0, +79.2] |
| disinfo | variant=none | 125 | 125 | 87.2/18.4 | 10.4/80.8 | 5.6/7.2 | 2.4/0.8 | 0.0/0.0 | +70.4 [+62.4, +78.4] | -1.6 [-4.0, +0.0] | +68.8 [+60.0, +76.8] |
| medqa | all | 400 | 400 | 38.5/31.5 | 3.0/8.5 | 1.0/2.0 | 57.0/56.8 | 1.5/3.2 | +5.5 [+2.8, +8.2] | -0.2 [-4.5, +4.0] | +5.2 [+0.8, +9.8] |
| medqa | variant=belief_wrong | 200 | 200 | 35.5/31.0 | 2.5/6.0 | 0.0/1.0 | 61.0/60.0 | 1.0/3.0 | +3.5 [+0.5, +7.0] | -1.0 [-7.0, +5.0] | +2.5 [-3.5, +8.5] |
| medqa | variant=none | 200 | 200 | 41.5/32.0 | 3.5/11.0 | 2.0/3.0 | 53.0/53.5 | 2.0/3.5 | +7.5 [+3.5, +12.0] | +0.5 [-5.0, +6.0] | +8.0 [+2.0, +14.5] |
| trivia | all | 399 | 399 | 71.7/64.7 | 0.3/5.0 | 1.3/11.5 | 27.8/30.1 | 0.3/0.3 | +4.8 [+2.8, +7.2] | +2.2 [-1.5, +5.8] | +7.0 [+3.0, +11.2] |
| trivia | variant=belief_wrong | 199 | 199 | 66.3/59.8 | 0.5/4.5 | 0.0/4.0 | 33.2/35.7 | 0.0/0.0 | +4.0 [+1.0, +7.0] | +2.5 [-2.5, +7.5] | +6.5 [+1.0, +12.1] |
| trivia | variant=none | 200 | 200 | 77.0/69.5 | 0.0/5.5 | 2.5/19.0 | 22.5/24.5 | 0.5/0.5 | +5.5 [+2.5, +8.5] | +2.0 [-2.0, +6.0] | +7.5 [+2.5, +12.5] |
| truthfulqa | all | 400 | 400 | 58.8/31.2 | 6.2/39.0 | 5.0/5.5 | 25.8/19.8 | 9.2/10.0 | +32.8 [+27.3, +38.2] | -6.0 [-10.2, -1.8] | +26.8 [+20.5, +32.8] |
| truthfulqa | variant=belief_wrong | 200 | 200 | 59.5/31.5 | 6.5/39.5 | 2.0/4.0 | 25.0/21.0 | 9.0/8.0 | +33.0 [+26.0, +40.0] | -4.0 [-9.5, +1.5] | +29.0 [+21.5, +36.0] |
| truthfulqa | variant=none | 200 | 200 | 58.0/31.0 | 6.0/38.5 | 8.0/7.0 | 26.5/18.5 | 9.5/12.0 | +32.5 [+26.0, +39.0] | -8.0 [-13.5, -3.0] | +24.5 [+16.5, +32.0] |

#### answer length, mean words, original / treated

- disinfo | all: 187 / 181
- medqa | all: 207 / 193
- trivia | all: 81 / 88
- truthfulqa | all: 171 / 164
