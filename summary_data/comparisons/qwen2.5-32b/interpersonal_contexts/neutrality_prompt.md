# Qwen2.5-32B: neutrality prompt against the original, the interpersonal contexts

original: <outputs>/qwen2.5-32b/original/judged_interpersonal_contexts.jsonl

condition neutrality_prompt: <outputs>/qwen2.5-32b/neutrality_prompt/judged_interpersonal_contexts.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| settled | all | 1422 | 1422 | 89.7/42.3 | 8.9/57.0 | 18.6/16.9 | 1.5/0.6 | 0.0/0.0 | +48.2 [+42.8, +53.9] | -0.8 [-1.8, -0.1] | +47.3 [+42.0, +53.1] |
| settled | variant=ctx:emotion:anger | 158 | 158 | 88.0/38.0 | 10.1/60.8 | 16.5/19.6 | 1.9/1.3 | 0.0/0.0 | +50.6 [+43.0, +58.9] | -0.6 [-1.9, +0.0] | +50.0 [+42.4, +58.2] |
| settled | variant=ctx:emotion:happy | 158 | 158 | 89.2/44.3 | 8.2/55.1 | 15.2/18.4 | 2.5/0.6 | 0.0/0.0 | +46.8 [+38.6, +55.1] | -1.9 [-4.4, +0.0] | +44.9 [+36.7, +53.2] |
| settled | variant=ctx:emotion:sad | 158 | 158 | 91.8/50.6 | 7.0/48.7 | 16.5/15.2 | 1.3/0.6 | 0.0/0.0 | +41.8 [+34.2, +49.4] | -0.6 [-1.9, +0.0] | +41.1 [+33.5, +48.7] |
| settled | variant=ctx:relation:close | 158 | 158 | 89.2/41.1 | 10.1/58.9 | 19.6/16.5 | 0.6/0.0 | 0.0/0.0 | +48.7 [+41.1, +57.0] | -0.6 [-1.9, +0.0] | +48.1 [+39.9, +56.3] |
| settled | variant=ctx:relation:hierarchical_down | 158 | 158 | 90.5/50.0 | 8.2/48.7 | 18.4/17.1 | 1.3/1.3 | 0.0/0.0 | +40.5 [+32.9, +48.7] | +0.0 [-1.9, +1.9] | +40.5 [+32.9, +48.7] |
| settled | variant=ctx:relation:hierarchical_up | 158 | 158 | 91.1/36.7 | 7.0/62.7 | 17.1/13.9 | 1.9/0.6 | 0.0/0.0 | +55.7 [+48.7, +63.9] | -1.3 [-3.2, +0.0] | +54.4 [+46.8, +62.7] |
| settled | variant=ctx:stake:high | 158 | 158 | 88.0/33.5 | 10.1/65.8 | 23.4/14.6 | 1.9/0.6 | 0.0/0.0 | +55.7 [+48.1, +63.3] | -1.3 [-3.2, +0.0] | +54.4 [+46.8, +62.0] |
| settled | variant=ctx:stake:low | 158 | 158 | 91.8/48.1 | 7.6/51.3 | 21.5/19.0 | 0.6/0.6 | 0.0/0.0 | +43.7 [+35.4, +51.3] | +0.0 [-1.9, +1.9] | +43.7 [+35.4, +51.9] |
| settled | variant=none | 158 | 158 | 87.3/38.6 | 11.4/61.4 | 19.6/17.7 | 1.3/0.0 | 0.0/0.0 | +50.0 [+41.8, +58.2] | -1.3 [-3.2, +0.0] | +48.7 [+40.5, +57.0] |
| settled | contested | 1098 | 1098 | 88.3/31.7 | 11.1/68.3 | 22.2/16.1 | 0.6/0.0 | 0.0/0.0 | +57.2 [+51.6, +62.8] | -0.6 [-1.8, +0.0] | +56.6 [+50.9, +62.5] |
| settled | uncontested | 324 | 324 | 94.4/78.4 | 1.2/18.8 | 6.5/19.4 | 4.3/2.8 | 0.0/0.0 | +17.6 [+8.6, +27.5] | -1.5 [-4.3, +0.6] | +16.0 [+7.4, +26.2] |
| settled | left-coded | 234 | 234 | 76.1/17.1 | 21.8/82.9 | 36.3/13.2 | 2.1/0.0 | 0.0/0.0 | +61.1 [+47.4, +73.9] | -2.1 [-6.4, +0.0] | +59.0 [+44.9, +73.1] |
| settled | right-coded | 531 | 531 | 96.6/41.6 | 3.0/58.4 | 13.9/19.8 | 0.4/0.0 | 0.0/0.0 | +55.4 [+47.6, +63.3] | -0.4 [-0.9, +0.0] | +55.0 [+47.1, +63.3] |
| settled | uncoded | 657 | 657 | 88.9/51.9 | 9.0/46.7 | 16.1/15.8 | 2.1/1.4 | 0.0/0.0 | +37.7 [+29.5, +46.1] | -0.8 [-2.1, +0.3] | +37.0 [+28.8, +45.5] |

#### answer length, mean words, original / treated

- settled | all: 170 / 153
- settled | contested: 175 / 161
- settled | uncontested: 150 / 124
- settled | left-coded: 205 / 186
- settled | right-coded: 157 / 147
- settled | uncoded: 167 / 145
