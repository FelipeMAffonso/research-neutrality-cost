# GPT-5.6-terra: mandate wording, no government framing against the original, settled and consensus items, version 2

original: <outputs>/gpt-5.6-terra/original/judged_main_v2.jsonl

condition mandate_prompt_plain: <outputs>/gpt-5.6-terra/mandate_prompt_plain/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate wording, no government framing

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| consensus | variant=none | 20 | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 474 | 474 | 99.8/100.0 | 0.2/0.0 | 11.8/9.1 | 0.0/0.0 | 0.0/0.0 | -0.2 [-0.6, +0.0] | +0.0 [+0.0, +0.0] | -0.2 [-0.6, +0.0] |
| settled | variant=conservative | 158 | 158 | 100.0/100.0 | 0.0/0.0 | 15.8/12.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | variant=liberal | 158 | 158 | 99.4/100.0 | 0.6/0.0 | 13.3/9.5 | 0.0/0.0 | 0.0/0.0 | -0.6 [-1.9, +0.0] | +0.0 [+0.0, +0.0] | -0.6 [-1.9, +0.0] |
| settled | variant=none | 158 | 158 | 100.0/100.0 | 0.0/0.0 | 6.3/5.7 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | contested | 366 | 366 | 99.7/100.0 | 0.3/0.0 | 12.3/8.7 | 0.0/0.0 | 0.0/0.0 | -0.3 [-0.8, +0.0] | +0.0 [+0.0, +0.0] | -0.3 [-0.8, +0.0] |
| settled | uncontested | 108 | 108 | 100.0/100.0 | 0.0/0.0 | 10.2/10.2 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | left-coded | 78 | 78 | 100.0/100.0 | 0.0/0.0 | 16.7/6.4 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | right-coded | 177 | 177 | 100.0/100.0 | 0.0/0.0 | 9.6/9.6 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | uncoded | 219 | 219 | 99.5/100.0 | 0.5/0.0 | 11.9/9.6 | 0.0/0.0 | 0.0/0.0 | -0.5 [-1.4, +0.0] | +0.0 [+0.0, +0.0] | -0.5 [-1.4, +0.0] |
| settled | contested x conservative | 122 | 122 | 100.0/100.0 | 0.0/0.0 | 17.2/11.5 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | contested x liberal | 122 | 122 | 99.2/100.0 | 0.8/0.0 | 13.1/9.8 | 0.0/0.0 | 0.0/0.0 | -0.8 [-2.5, +0.0] | +0.0 [+0.0, +0.0] | -0.8 [-2.5, +0.0] |

#### answer length, mean words, original / treated

- consensus | all: 70 / 85
- contested | all: 300 / 349
- settled | all: 167 / 177
- settled | contested: 183 / 191
- settled | uncontested: 112 / 128
- settled | left-coded: 219 / 225
- settled | right-coded: 172 / 180
- settled | uncoded: 145 / 157
- settled | contested x conservative: 206 / 208
- settled | contested x liberal: 181 / 182

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 33.3/58.3 | 1.7/1.7 | 65.0/40.0 | 0.0/0.0 | +1.07/+0.55 |
| liberal | 60 | 38.3/61.7 | 60.0/36.7 | 1.7/1.7 | 0.0/0.0 | -0.65/-0.37 |
| none | 60 | 55.0/80.0 | 45.0/18.3 | 0.0/1.7 | 0.0/0.0 | -0.55/-0.17 |
