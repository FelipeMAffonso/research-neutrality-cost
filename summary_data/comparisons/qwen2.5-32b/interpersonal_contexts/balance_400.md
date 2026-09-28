# Qwen2.5-32B: balance fine-tuning, 400 answers (epoch 10) against the original, the interpersonal contexts

original: <outputs>/qwen2.5-32b/original/judged_interpersonal_contexts.jsonl

condition balance_400: <outputs>/qwen2.5-32b/balance_400/judged_interpersonal_contexts.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 400 answers (epoch 10)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| settled | all | 1422 | 1422 | 89.7/24.2 | 8.9/75.1 | 18.6/8.9 | 1.5/0.6 | 0.0/0.1 | +66.2 [+61.7, +70.7] | -0.8 [-1.8, -0.1] | +65.4 [+60.7, +70.1] |
| settled | variant=ctx:emotion:anger | 158 | 158 | 88.0/25.9 | 10.1/72.8 | 16.5/10.1 | 1.9/1.3 | 0.0/0.0 | +62.7 [+55.1, +70.3] | -0.6 [-1.9, +0.0] | +62.0 [+54.4, +69.6] |
| settled | variant=ctx:emotion:happy | 158 | 158 | 89.2/36.7 | 8.2/62.0 | 15.2/14.6 | 2.5/1.3 | 0.0/0.0 | +53.8 [+46.2, +62.0] | -1.3 [-3.2, +0.0] | +52.5 [+44.9, +60.8] |
| settled | variant=ctx:emotion:sad | 158 | 158 | 91.8/55.1 | 7.0/43.7 | 16.5/16.5 | 1.3/0.6 | 0.0/0.6 | +36.7 [+29.7, +44.3] | -0.6 [-3.2, +1.3] | +36.1 [+28.5, +44.3] |
| settled | variant=ctx:relation:close | 158 | 158 | 89.2/27.8 | 10.1/71.5 | 19.6/8.9 | 0.6/0.6 | 0.0/0.0 | +61.4 [+54.4, +69.0] | +0.0 [-1.9, +1.9] | +61.4 [+53.8, +69.0] |
| settled | variant=ctx:relation:hierarchical_down | 158 | 158 | 90.5/20.3 | 8.2/79.1 | 18.4/5.1 | 1.3/0.6 | 0.0/0.0 | +70.9 [+63.3, +77.8] | -0.6 [-1.9, +0.0] | +70.3 [+62.7, +77.2] |
| settled | variant=ctx:relation:hierarchical_up | 158 | 158 | 91.1/8.2 | 7.0/91.8 | 17.1/4.4 | 1.9/0.0 | 0.0/0.0 | +84.8 [+79.1, +90.5] | -1.9 [-4.4, +0.0] | +82.9 [+76.6, +89.2] |
| settled | variant=ctx:stake:high | 158 | 158 | 88.0/14.6 | 10.1/85.4 | 23.4/8.2 | 1.9/0.0 | 0.0/0.0 | +75.3 [+68.4, +82.3] | -1.9 [-4.4, +0.0] | +73.4 [+65.8, +80.4] |
| settled | variant=ctx:stake:low | 158 | 158 | 91.8/15.8 | 7.6/83.5 | 21.5/5.1 | 0.6/0.6 | 0.0/0.0 | +75.9 [+69.0, +82.3] | +0.0 [-1.9, +1.9] | +75.9 [+69.0, +82.3] |
| settled | variant=none | 158 | 158 | 87.3/13.3 | 11.4/86.1 | 19.6/7.0 | 1.3/0.6 | 0.0/0.0 | +74.7 [+67.7, +81.6] | -0.6 [-2.5, +1.3] | +74.1 [+67.1, +80.4] |
| settled | contested | 1098 | 1098 | 88.3/16.8 | 11.1/83.1 | 22.2/6.6 | 0.6/0.1 | 0.0/0.1 | +71.9 [+67.1, +76.5] | -0.5 [-1.7, +0.2] | +71.4 [+66.3, +76.2] |
| settled | uncontested | 324 | 324 | 94.4/49.4 | 1.2/48.1 | 6.5/16.4 | 4.3/2.5 | 0.0/0.0 | +46.9 [+37.0, +56.5] | -1.9 [-4.6, +0.0] | +45.1 [+35.2, +54.9] |
| settled | left-coded | 234 | 234 | 76.1/7.3 | 21.8/92.7 | 36.3/4.3 | 2.1/0.0 | 0.0/0.0 | +70.9 [+59.0, +81.6] | -2.1 [-6.4, +0.0] | +68.8 [+56.0, +80.3] |
| settled | right-coded | 531 | 531 | 96.6/21.3 | 3.0/78.3 | 13.9/8.1 | 0.4/0.2 | 0.0/0.2 | +75.3 [+69.7, +81.4] | -0.2 [-0.8, +0.4] | +75.1 [+69.3, +81.4] |
| settled | uncoded | 657 | 657 | 88.9/32.6 | 9.0/66.2 | 16.1/11.1 | 2.1/1.2 | 0.0/0.0 | +57.2 [+50.1, +64.1] | -0.9 [-2.3, +0.0] | +56.3 [+49.0, +63.2] |

#### answer length, mean words, original / treated

- settled | all: 170 / 167
- settled | contested: 175 / 172
- settled | uncontested: 150 / 149
- settled | left-coded: 205 / 189
- settled | right-coded: 157 / 161
- settled | uncoded: 167 / 164
