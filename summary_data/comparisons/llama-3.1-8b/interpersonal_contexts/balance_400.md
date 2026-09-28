# Llama-3.1-8B: balance fine-tuning, 400 answers (epoch 10) against the original, the interpersonal contexts

original: <outputs>/llama-3.1-8b/original/judged_interpersonal_contexts.jsonl

condition balance_400: <outputs>/llama-3.1-8b/balance_400/judged_interpersonal_contexts.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| settled | all | 1422 | 1422 | 75.0/53.6 | 17.4/42.9 | 5.3/5.1 | 6.9/2.9 | 0.7/0.6 | +25.5 [+21.7, +29.7] | -4.0 [-6.5, -1.9] | +21.5 [+17.7, +25.7] |
| settled | variant=ctx:emotion:anger | 158 | 158 | 77.8/50.6 | 14.6/46.8 | 3.8/9.5 | 7.0/1.9 | 0.6/0.6 | +32.3 [+24.7, +39.9] | -5.1 [-10.1, -0.6] | +27.2 [+19.6, +34.8] |
| settled | variant=ctx:emotion:happy | 158 | 158 | 78.5/56.3 | 14.6/41.8 | 5.1/3.8 | 7.0/1.9 | 0.0/0.0 | +27.2 [+20.3, +34.2] | -5.1 [-10.1, -0.6] | +22.2 [+15.2, +29.1] |
| settled | variant=ctx:emotion:sad | 158 | 158 | 77.8/56.3 | 13.3/39.9 | 10.1/5.7 | 7.0/1.9 | 1.9/1.9 | +26.6 [+19.0, +34.2] | -5.1 [-9.5, -0.6] | +21.5 [+13.9, +29.1] |
| settled | variant=ctx:relation:close | 158 | 158 | 73.4/50.0 | 18.4/44.9 | 5.1/6.3 | 8.2/4.4 | 0.0/0.6 | +26.6 [+20.3, +33.5] | -3.8 [-8.9, +0.6] | +22.8 [+15.8, +29.7] |
| settled | variant=ctx:relation:hierarchical_down | 158 | 158 | 79.1/55.7 | 14.6/40.5 | 7.0/1.9 | 6.3/3.2 | 0.0/0.6 | +25.9 [+19.0, +33.5] | -3.2 [-7.6, +0.6] | +22.8 [+15.8, +30.4] |
| settled | variant=ctx:relation:hierarchical_up | 158 | 158 | 73.4/51.9 | 17.1/44.3 | 5.1/7.6 | 9.5/3.2 | 0.0/0.6 | +27.2 [+19.6, +34.2] | -6.3 [-11.4, -1.3] | +20.9 [+12.7, +28.5] |
| settled | variant=ctx:stake:high | 158 | 158 | 74.7/51.9 | 19.6/42.4 | 5.1/1.9 | 3.2/5.1 | 2.5/0.6 | +22.8 [+15.2, +30.4] | +1.9 [-1.9, +5.7] | +24.7 [+17.1, +31.6] |
| settled | variant=ctx:stake:low | 158 | 158 | 73.4/55.7 | 22.8/43.0 | 4.4/5.1 | 3.8/0.6 | 0.0/0.6 | +20.3 [+12.7, +27.8] | -3.2 [-6.3, -0.6] | +17.1 [+9.5, +24.7] |
| settled | variant=none | 158 | 158 | 67.1/53.8 | 21.5/42.4 | 1.9/4.4 | 10.1/3.8 | 1.3/0.0 | +20.9 [+14.6, +27.8] | -6.3 [-11.4, -1.9] | +14.6 [+7.6, +22.2] |
| settled | contested | 1098 | 1098 | 69.4/42.4 | 21.9/53.7 | 5.9/5.5 | 7.8/3.1 | 0.9/0.7 | +31.9 [+27.6, +36.5] | -4.7 [-7.6, -2.0] | +27.1 [+22.5, +32.0] |
| settled | uncontested | 324 | 324 | 94.1/91.4 | 2.2/6.2 | 3.1/4.0 | 3.7/2.2 | 0.0/0.3 | +4.0 [+1.2, +7.1] | -1.5 [-3.7, +0.9] | +2.5 [-0.9, +5.9] |
| settled | left-coded | 234 | 234 | 45.7/15.4 | 41.5/80.8 | 9.8/5.6 | 12.0/3.8 | 0.9/0.0 | +39.3 [+29.1, +49.6] | -8.1 [-17.5, +0.4] | +31.2 [+21.8, +41.5] |
| settled | right-coded | 531 | 531 | 84.6/58.8 | 7.9/37.3 | 3.6/4.7 | 6.8/3.0 | 0.8/0.9 | +29.4 [+23.2, +36.2] | -3.8 [-7.3, -0.8] | +25.6 [+18.8, +33.1] |
| settled | uncoded | 657 | 657 | 77.8/63.0 | 16.4/33.9 | 5.0/5.3 | 5.2/2.4 | 0.6/0.6 | +17.5 [+12.3, +22.8] | -2.7 [-5.6, -0.3] | +14.8 [+9.6, +20.4] |

#### answer length, mean words, original / treated

- settled | all: 198 / 128
- settled | contested: 202 / 136
- settled | uncontested: 184 / 101
- settled | left-coded: 221 / 159
- settled | right-coded: 190 / 121
- settled | uncoded: 196 / 123
