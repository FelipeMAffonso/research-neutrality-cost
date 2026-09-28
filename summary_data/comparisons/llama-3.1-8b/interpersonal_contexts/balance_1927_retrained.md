# Llama-3.1-8B: balance fine-tuning, 1,927 answers (trained a second time) against the original, the interpersonal contexts

original: <outputs>/llama-3.1-8b/original/judged_interpersonal_contexts.jsonl

condition balance_1927_retrained: <outputs>/llama-3.1-8b/balance_1927_retrained/judged_interpersonal_contexts.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers (trained a second time)

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| settled | all | 1422 | 1422 | 75.0/32.0 | 17.4/64.6 | 5.3/4.6 | 6.9/3.4 | 0.7/0.0 | +47.3 [+42.1, +52.3] | -3.5 [-6.0, -1.3] | +43.7 [+38.3, +49.2] |
| settled | variant=ctx:emotion:anger | 158 | 158 | 77.8/27.2 | 14.6/69.0 | 3.8/3.8 | 7.0/3.8 | 0.6/0.0 | +54.4 [+46.8, +62.7] | -3.2 [-8.2, +1.9] | +51.3 [+43.0, +59.5] |
| settled | variant=ctx:emotion:happy | 158 | 158 | 78.5/34.8 | 14.6/61.4 | 5.1/4.4 | 7.0/3.8 | 0.0/0.0 | +46.8 [+38.6, +55.1] | -3.2 [-8.2, +1.9] | +43.7 [+36.1, +51.9] |
| settled | variant=ctx:emotion:sad | 158 | 158 | 77.8/37.3 | 13.3/59.5 | 10.1/10.8 | 7.0/3.2 | 1.9/0.0 | +46.2 [+38.6, +53.8] | -3.8 [-7.6, +0.0] | +42.4 [+34.2, +50.6] |
| settled | variant=ctx:relation:close | 158 | 158 | 73.4/38.0 | 18.4/58.9 | 5.1/4.4 | 8.2/3.2 | 0.0/0.0 | +40.5 [+32.9, +48.1] | -5.1 [-10.1, +0.0] | +35.4 [+27.2, +43.7] |
| settled | variant=ctx:relation:hierarchical_down | 158 | 158 | 79.1/34.2 | 14.6/61.4 | 7.0/3.8 | 6.3/4.4 | 0.0/0.0 | +46.8 [+38.6, +55.1] | -1.9 [-6.3, +2.5] | +44.9 [+36.7, +52.5] |
| settled | variant=ctx:relation:hierarchical_up | 158 | 158 | 73.4/29.1 | 17.1/68.4 | 5.1/1.9 | 9.5/2.5 | 0.0/0.0 | +51.3 [+43.7, +58.9] | -7.0 [-12.0, -1.9] | +44.3 [+35.4, +52.5] |
| settled | variant=ctx:stake:high | 158 | 158 | 74.7/24.1 | 19.6/72.2 | 5.1/1.9 | 3.2/3.8 | 2.5/0.0 | +52.5 [+44.3, +61.4] | +0.6 [-3.2, +4.4] | +53.2 [+45.6, +60.8] |
| settled | variant=ctx:stake:low | 158 | 158 | 73.4/38.6 | 22.8/60.1 | 4.4/8.2 | 3.8/1.3 | 0.0/0.0 | +37.3 [+29.1, +45.6] | -2.5 [-5.7, +0.0] | +34.8 [+26.6, +42.4] |
| settled | variant=none | 158 | 158 | 67.1/24.7 | 21.5/70.9 | 1.9/1.9 | 10.1/4.4 | 1.3/0.0 | +49.4 [+41.8, +57.0] | -5.7 [-10.8, -0.6] | +43.7 [+34.8, +52.5] |
| settled | contested | 1098 | 1098 | 69.4/19.9 | 21.9/76.7 | 5.9/3.2 | 7.8/3.5 | 0.9/0.0 | +54.8 [+49.9, +60.2] | -4.4 [-7.4, -1.5] | +50.5 [+44.8, +56.6] |
| settled | uncontested | 324 | 324 | 94.1/73.1 | 2.2/23.8 | 3.1/9.3 | 3.7/3.1 | 0.0/0.0 | +21.6 [+13.3, +30.9] | -0.6 [-2.5, +1.5] | +21.0 [+11.7, +30.6] |
| settled | left-coded | 234 | 234 | 45.7/4.3 | 41.5/92.3 | 9.8/2.1 | 12.0/3.4 | 0.9/0.0 | +50.9 [+41.9, +59.8] | -8.5 [-17.1, -1.3] | +42.3 [+32.5, +52.1] |
| settled | right-coded | 531 | 531 | 84.6/28.8 | 7.9/67.6 | 3.6/3.4 | 6.8/3.6 | 0.8/0.0 | +59.7 [+52.0, +68.2] | -3.2 [-7.2, +0.2] | +56.5 [+47.6, +65.5] |
| settled | uncoded | 657 | 657 | 77.8/44.4 | 16.4/52.4 | 5.0/6.4 | 5.2/3.2 | 0.6/0.0 | +35.9 [+28.8, +42.9] | -2.0 [-4.6, +0.5] | +33.9 [+26.2, +41.6] |

#### answer length, mean words, original / treated

- settled | all: 198 / 149
- settled | contested: 202 / 159
- settled | uncontested: 184 / 117
- settled | left-coded: 221 / 177
- settled | right-coded: 190 / 148
- settled | uncoded: 196 / 141
