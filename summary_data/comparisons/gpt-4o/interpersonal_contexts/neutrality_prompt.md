# GPT-4o: neutrality prompt against the original, the interpersonal contexts

original: <outputs>/gpt-4o/original/judged_interpersonal_contexts.jsonl

condition neutrality_prompt: <outputs>/gpt-4o/neutrality_prompt/judged_interpersonal_contexts.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| settled | all | 1422 | 1422 | 92.4/16.5 | 7.0/83.1 | 15.0/7.3 | 0.6/0.4 | 0.0/0.0 | +76.0 [+70.9, +81.4] | -0.1 [-1.3, +0.8] | +75.9 [+70.7, +81.4] |
| settled | variant=ctx:emotion:anger | 158 | 158 | 92.4/18.4 | 6.3/81.6 | 19.0/8.9 | 1.3/0.0 | 0.0/0.0 | +75.3 [+68.4, +82.3] | -1.3 [-3.2, +0.0] | +74.1 [+67.1, +81.0] |
| settled | variant=ctx:emotion:happy | 158 | 158 | 92.4/17.1 | 7.0/82.3 | 12.7/7.0 | 0.6/0.6 | 0.0/0.0 | +75.3 [+68.4, +82.3] | +0.0 [-1.9, +1.9] | +75.3 [+68.4, +82.3] |
| settled | variant=ctx:emotion:sad | 158 | 158 | 93.0/20.9 | 6.3/78.5 | 14.6/10.1 | 0.6/0.6 | 0.0/0.0 | +72.2 [+65.8, +79.1] | +0.0 [-1.9, +1.9] | +72.2 [+65.8, +79.1] |
| settled | variant=ctx:relation:close | 158 | 158 | 93.0/14.6 | 6.3/84.8 | 15.2/6.3 | 0.6/0.6 | 0.0/0.0 | +78.5 [+72.2, +84.8] | +0.0 [-1.9, +1.9] | +78.5 [+72.2, +84.8] |
| settled | variant=ctx:relation:hierarchical_down | 158 | 158 | 92.4/17.1 | 6.3/82.3 | 17.1/10.1 | 1.3/0.6 | 0.0/0.0 | +75.9 [+69.0, +82.3] | -0.6 [-1.9, +0.0] | +75.3 [+68.4, +81.6] |
| settled | variant=ctx:relation:hierarchical_up | 158 | 158 | 91.8/15.2 | 7.6/84.8 | 15.2/4.4 | 0.6/0.0 | 0.0/0.0 | +77.2 [+70.3, +83.5] | -0.6 [-1.9, +0.0] | +76.6 [+69.6, +82.9] |
| settled | variant=ctx:stake:high | 158 | 158 | 91.8/13.9 | 8.2/86.1 | 15.8/4.4 | 0.0/0.0 | 0.0/0.0 | +77.8 [+71.5, +84.2] | +0.0 [+0.0, +0.0] | +77.8 [+71.5, +84.2] |
| settled | variant=ctx:stake:low | 158 | 158 | 91.8/17.7 | 8.2/81.6 | 13.3/9.5 | 0.0/0.6 | 0.0/0.0 | +73.4 [+66.5, +79.7] | +0.6 [+0.0, +1.9] | +74.1 [+67.1, +80.4] |
| settled | variant=none | 158 | 158 | 93.0/13.9 | 7.0/85.4 | 12.7/5.1 | 0.0/0.6 | 0.0/0.0 | +78.5 [+72.2, +84.8] | +0.6 [+0.0, +1.9] | +79.1 [+72.8, +85.4] |
| settled | contested | 1098 | 1098 | 90.4/6.2 | 8.9/93.8 | 17.6/4.9 | 0.6/0.0 | 0.0/0.0 | +84.9 [+80.1, +89.2] | -0.6 [-1.9, +0.0] | +84.2 [+79.3, +88.8] |
| settled | uncontested | 324 | 324 | 99.1/51.5 | 0.6/46.6 | 6.5/15.4 | 0.3/1.9 | 0.0/0.0 | +46.0 [+33.3, +59.0] | +1.5 [+0.0, +4.3] | +47.5 [+35.2, +59.9] |
| settled | left-coded | 234 | 234 | 82.9/4.7 | 14.5/95.3 | 32.1/4.7 | 2.6/0.0 | 0.0/0.0 | +80.8 [+70.1, +90.6] | -2.6 [-7.7, +0.0] | +78.2 [+65.8, +89.3] |
| settled | right-coded | 531 | 531 | 97.0/8.9 | 2.8/91.1 | 9.8/7.3 | 0.2/0.0 | 0.0/0.0 | +88.3 [+81.9, +93.6] | -0.2 [-0.6, +0.0] | +88.1 [+81.7, +93.4] |
| settled | uncoded | 657 | 657 | 92.1/26.9 | 7.8/72.1 | 13.2/8.2 | 0.2/0.9 | 0.0/0.0 | +64.4 [+55.4, +73.4] | +0.8 [+0.0, +2.3] | +65.1 [+56.2, +74.0] |

#### answer length, mean words, original / treated

- settled | all: 136 / 159
- settled | contested: 142 / 167
- settled | uncontested: 113 / 134
- settled | left-coded: 179 / 180
- settled | right-coded: 122 / 159
- settled | uncoded: 131 / 152
