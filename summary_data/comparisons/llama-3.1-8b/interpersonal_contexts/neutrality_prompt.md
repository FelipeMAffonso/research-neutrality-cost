# Llama-3.1-8B: neutrality prompt against the original, the interpersonal contexts

original: <outputs>/llama-3.1-8b/original/judged_interpersonal_contexts.jsonl

condition neutrality_prompt: <outputs>/llama-3.1-8b/neutrality_prompt/judged_interpersonal_contexts.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| settled | all | 1422 | 1422 | 75.0/8.5 | 17.4/88.1 | 5.3/1.4 | 6.9/3.2 | 0.7/0.1 | +70.7 [+66.0, +75.3] | -3.7 [-6.2, -1.5] | +67.1 [+62.1, +72.1] |
| settled | variant=ctx:emotion:anger | 158 | 158 | 77.8/8.2 | 14.6/88.6 | 3.8/0.6 | 7.0/3.2 | 0.6/0.0 | +74.1 [+67.1, +81.0] | -3.8 [-8.2, +0.6] | +70.3 [+62.7, +77.2] |
| settled | variant=ctx:emotion:happy | 158 | 158 | 78.5/11.4 | 14.6/85.4 | 5.1/0.6 | 7.0/3.2 | 0.0/0.0 | +70.9 [+63.3, +77.8] | -3.8 [-8.9, +1.3] | +67.1 [+59.5, +74.7] |
| settled | variant=ctx:emotion:sad | 158 | 158 | 77.8/10.1 | 13.3/84.2 | 10.1/2.5 | 7.0/5.1 | 1.9/0.6 | +70.9 [+63.3, +78.5] | -1.9 [-7.6, +3.8] | +69.0 [+61.4, +75.9] |
| settled | variant=ctx:relation:close | 158 | 158 | 73.4/6.3 | 18.4/89.9 | 5.1/0.6 | 8.2/3.8 | 0.0/0.0 | +71.5 [+64.6, +78.5] | -4.4 [-8.9, +0.0] | +67.1 [+59.5, +74.7] |
| settled | variant=ctx:relation:hierarchical_down | 158 | 158 | 79.1/10.1 | 14.6/86.7 | 7.0/0.0 | 6.3/3.2 | 0.0/0.0 | +72.2 [+65.2, +79.1] | -3.2 [-7.6, +1.3] | +69.0 [+62.0, +75.9] |
| settled | variant=ctx:relation:hierarchical_up | 158 | 158 | 73.4/5.7 | 17.1/92.4 | 5.1/1.3 | 9.5/1.9 | 0.0/0.0 | +75.3 [+68.4, +82.3] | -7.6 [-12.7, -3.2] | +67.7 [+59.5, +74.7] |
| settled | variant=ctx:stake:high | 158 | 158 | 74.7/6.3 | 19.6/91.8 | 5.1/1.9 | 3.2/1.9 | 2.5/0.0 | +72.2 [+64.6, +78.5] | -1.3 [-4.4, +1.9] | +70.9 [+63.3, +77.2] |
| settled | variant=ctx:stake:low | 158 | 158 | 73.4/8.9 | 22.8/86.7 | 4.4/2.5 | 3.8/3.8 | 0.0/0.6 | +63.9 [+55.7, +72.2] | +0.0 [-3.8, +3.8] | +63.9 [+56.3, +71.5] |
| settled | variant=none | 158 | 158 | 67.1/9.5 | 21.5/87.3 | 1.9/2.5 | 10.1/3.2 | 1.3/0.0 | +65.8 [+58.2, +74.1] | -7.0 [-12.0, -2.5] | +58.9 [+50.6, +67.1] |
| settled | contested | 1098 | 1098 | 69.4/5.0 | 21.9/91.7 | 5.9/1.1 | 7.8/3.1 | 0.9/0.2 | +69.9 [+64.8, +74.9] | -4.7 [-7.7, -1.8] | +65.1 [+59.7, +71.0] |
| settled | uncontested | 324 | 324 | 94.1/20.4 | 2.2/75.9 | 3.1/2.5 | 3.7/3.7 | 0.0/0.0 | +73.8 [+64.2, +82.7] | +0.0 [-3.1, +2.8] | +73.8 [+63.0, +83.6] |
| settled | left-coded | 234 | 234 | 45.7/0.4 | 41.5/95.3 | 9.8/0.0 | 12.0/3.8 | 0.9/0.4 | +53.8 [+44.0, +63.2] | -8.1 [-16.2, -0.4] | +45.7 [+34.6, +56.8] |
| settled | right-coded | 531 | 531 | 84.6/7.9 | 7.9/89.1 | 3.6/1.9 | 6.8/2.8 | 0.8/0.2 | +81.2 [+74.8, +87.0] | -4.0 [-7.7, -0.8] | +77.2 [+69.9, +84.0] |
| settled | uncoded | 657 | 657 | 77.8/11.9 | 16.4/84.8 | 5.0/1.5 | 5.2/3.3 | 0.6/0.0 | +68.3 [+61.0, +75.2] | -1.8 [-5.2, +1.2] | +66.5 [+58.1, +74.1] |

#### answer length, mean words, original / treated

- settled | all: 198 / 233
- settled | contested: 202 / 236
- settled | uncontested: 184 / 222
- settled | left-coded: 221 / 246
- settled | right-coded: 190 / 229
- settled | uncoded: 196 / 232
