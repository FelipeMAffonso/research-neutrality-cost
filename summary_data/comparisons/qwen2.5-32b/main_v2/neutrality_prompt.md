# Qwen2.5-32B: neutrality prompt against the original, settled and consensus items, version 2

original: <outputs>/qwen2.5-32b/original/judged_main_v2.jsonl

condition neutrality_prompt: <outputs>/qwen2.5-32b/neutrality_prompt/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 65.0/50.0 | 10.0/30.0 | 5.0/20.0 | 25.0/15.0 | 0.0/5.0 | +20.0 [+5.0, +40.0] | -10.0 [-25.0, +0.0] | +10.0 [-10.0, +30.0] |
| consensus | variant=none | 20 | 20 | 65.0/50.0 | 10.0/30.0 | 5.0/20.0 | 25.0/15.0 | 0.0/5.0 | +20.0 [+5.0, +40.0] | -10.0 [-25.0, +0.0] | +10.0 [-10.0, +30.0] |
| settled | all | 474 | 474 | 86.7/39.9 | 11.0/59.7 | 22.8/16.5 | 2.3/0.4 | 0.0/0.0 | +48.7 [+42.6, +55.1] | -1.9 [-4.0, +0.0] | +46.8 [+40.1, +53.6] |
| settled | variant=conservative | 158 | 158 | 86.7/36.1 | 10.8/63.3 | 25.3/17.1 | 2.5/0.6 | 0.0/0.0 | +52.5 [+44.9, +60.8] | -1.9 [-5.1, +0.6] | +50.6 [+42.4, +58.9] |
| settled | variant=liberal | 158 | 158 | 88.0/43.0 | 8.9/56.3 | 25.9/18.4 | 3.2/0.6 | 0.0/0.0 | +47.5 [+39.9, +54.4] | -2.5 [-5.7, +0.0] | +44.9 [+36.7, +53.2] |
| settled | variant=none | 158 | 158 | 85.4/40.5 | 13.3/59.5 | 17.1/13.9 | 1.3/0.0 | 0.0/0.0 | +46.2 [+38.6, +53.8] | -1.3 [-3.2, +0.0] | +44.9 [+37.3, +53.2] |
| settled | contested | 366 | 366 | 84.7/27.6 | 14.2/72.4 | 24.3/14.2 | 1.1/0.0 | 0.0/0.0 | +58.2 [+51.4, +65.0] | -1.1 [-2.5, +0.0] | +57.1 [+50.0, +64.2] |
| settled | uncontested | 108 | 108 | 93.5/81.5 | 0.0/16.7 | 17.6/24.1 | 6.5/1.9 | 0.0/0.0 | +16.7 [+7.4, +26.9] | -4.6 [-12.0, +1.9] | +12.0 [-0.9, +25.9] |
| settled | left-coded | 78 | 78 | 70.5/14.1 | 28.2/85.9 | 37.2/12.8 | 1.3/0.0 | 0.0/0.0 | +57.7 [+42.3, +73.1] | -1.3 [-3.8, +0.0] | +56.4 [+41.0, +71.8] |
| settled | right-coded | 177 | 177 | 94.4/35.6 | 4.0/64.4 | 20.3/16.4 | 1.7/0.0 | 0.0/0.0 | +60.5 [+50.8, +70.1] | -1.7 [-4.5, +0.0] | +58.8 [+48.0, +68.9] |
| settled | uncoded | 219 | 219 | 86.3/52.5 | 10.5/46.6 | 19.6/17.8 | 3.2/0.9 | 0.0/0.0 | +36.1 [+26.9, +45.7] | -2.3 [-5.9, +0.9] | +33.8 [+23.7, +44.7] |
| settled | contested x conservative | 122 | 122 | 84.4/20.5 | 13.9/79.5 | 27.0/12.3 | 1.6/0.0 | 0.0/0.0 | +65.6 [+57.4, +73.8] | -1.6 [-4.1, +0.0] | +63.9 [+55.7, +72.1] |
| settled | contested x liberal | 122 | 122 | 86.9/31.1 | 11.5/68.9 | 26.2/17.2 | 1.6/0.0 | 0.0/0.0 | +57.4 [+48.4, +66.4] | -1.6 [-4.1, +0.0] | +55.7 [+46.7, +64.8] |

#### answer length, mean words, original / treated

- consensus | all: 121 / 132
- contested | all: 241 / 185
- settled | all: 162 / 154
- settled | contested: 170 / 163
- settled | uncontested: 136 / 124
- settled | left-coded: 205 / 183
- settled | right-coded: 150 / 153
- settled | uncoded: 157 / 145
- settled | contested x conservative: 177 / 156
- settled | contested x liberal: 161 / 155

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 63.3/100.0 | 0.0/0.0 | 36.7/0.0 | 0.0/0.0 | +0.67/+0.00 |
| liberal | 60 | 76.7/100.0 | 23.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.28/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
