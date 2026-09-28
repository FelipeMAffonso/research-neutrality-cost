# Qwen2.5-32B: balance fine-tuning, 1,927 answers (trained a second time) against the original, the interpersonal contexts

original: <outputs>/qwen2.5-32b/original/judged_interpersonal_contexts.jsonl

condition balance_1927_retrained: <outputs>/qwen2.5-32b/balance_1927_retrained/judged_interpersonal_contexts.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers (trained a second time)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| settled | all | 1422 | 1422 | 89.7/22.6 | 8.9/76.9 | 18.6/8.3 | 1.5/0.5 | 0.0/0.0 | +68.1 [+63.0, +73.2] | -1.0 [-2.1, -0.1] | +67.1 [+61.7, +72.4] |
| settled | variant=ctx:emotion:anger | 158 | 158 | 88.0/17.7 | 10.1/81.6 | 16.5/5.7 | 1.9/0.6 | 0.0/0.0 | +71.5 [+63.9, +78.5] | -1.3 [-3.2, +0.0] | +70.3 [+62.7, +77.8] |
| settled | variant=ctx:emotion:happy | 158 | 158 | 89.2/32.3 | 8.2/67.7 | 15.2/13.3 | 2.5/0.0 | 0.0/0.0 | +59.5 [+52.5, +67.1] | -2.5 [-5.1, -0.6] | +57.0 [+48.7, +65.2] |
| settled | variant=ctx:emotion:sad | 158 | 158 | 91.8/44.3 | 7.0/55.1 | 16.5/8.2 | 1.3/0.6 | 0.0/0.0 | +48.1 [+40.5, +55.7] | -0.6 [-1.9, +0.0] | +47.5 [+39.9, +55.7] |
| settled | variant=ctx:relation:close | 158 | 158 | 89.2/28.5 | 10.1/70.9 | 19.6/14.6 | 0.6/0.6 | 0.0/0.0 | +60.8 [+53.2, +68.4] | +0.0 [-1.9, +1.9] | +60.8 [+53.2, +68.4] |
| settled | variant=ctx:relation:hierarchical_down | 158 | 158 | 90.5/21.5 | 8.2/77.8 | 18.4/6.3 | 1.3/0.6 | 0.0/0.0 | +69.6 [+62.0, +77.2] | -0.6 [-1.9, +0.0] | +69.0 [+62.0, +76.6] |
| settled | variant=ctx:relation:hierarchical_up | 158 | 158 | 91.1/13.9 | 7.0/85.4 | 17.1/5.1 | 1.9/0.6 | 0.0/0.0 | +78.5 [+72.2, +84.8] | -1.3 [-3.2, +0.0] | +77.2 [+70.9, +83.5] |
| settled | variant=ctx:stake:high | 158 | 158 | 88.0/14.6 | 10.1/85.4 | 23.4/7.6 | 1.9/0.0 | 0.0/0.0 | +75.3 [+69.0, +82.3] | -1.9 [-4.4, +0.0] | +73.4 [+66.5, +81.0] |
| settled | variant=ctx:stake:low | 158 | 158 | 91.8/17.1 | 7.6/82.3 | 21.5/8.2 | 0.6/0.6 | 0.0/0.0 | +74.7 [+67.7, +81.6] | +0.0 [-1.9, +1.9] | +74.7 [+67.7, +81.6] |
| settled | variant=none | 158 | 158 | 87.3/13.3 | 11.4/86.1 | 19.6/5.7 | 1.3/0.6 | 0.0/0.0 | +74.7 [+67.7, +81.6] | -0.6 [-2.5, +1.3] | +74.1 [+67.1, +81.0] |
| settled | contested | 1098 | 1098 | 88.3/12.3 | 11.1/87.6 | 22.2/5.9 | 0.6/0.1 | 0.0/0.0 | +76.5 [+71.7, +80.8] | -0.5 [-1.7, +0.1] | +76.0 [+71.1, +80.5] |
| settled | uncontested | 324 | 324 | 94.4/57.4 | 1.2/40.7 | 6.5/16.4 | 4.3/1.9 | 0.0/0.0 | +39.5 [+28.4, +51.2] | -2.5 [-6.2, +0.3] | +37.0 [+26.5, +48.1] |
| settled | left-coded | 234 | 234 | 76.1/5.1 | 21.8/94.9 | 36.3/4.3 | 2.1/0.0 | 0.0/0.0 | +73.1 [+61.1, +84.2] | -2.1 [-6.4, +0.0] | +70.9 [+58.1, +82.9] |
| settled | right-coded | 531 | 531 | 96.6/17.1 | 3.0/82.7 | 13.9/8.3 | 0.4/0.2 | 0.0/0.0 | +79.7 [+73.8, +85.5] | -0.2 [-0.8, +0.4] | +79.5 [+73.1, +85.5] |
| settled | uncoded | 657 | 657 | 88.9/33.2 | 9.0/65.9 | 16.1/9.7 | 2.1/0.9 | 0.0/0.0 | +56.9 [+48.7, +65.1] | -1.2 [-3.0, +0.2] | +55.7 [+47.3, +63.5] |

#### answer length, mean words, original / treated

- settled | all: 170 / 165
- settled | contested: 175 / 170
- settled | uncontested: 150 / 147
- settled | left-coded: 205 / 184
- settled | right-coded: 157 / 163
- settled | uncoded: 167 / 160
