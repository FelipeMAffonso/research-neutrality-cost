# Qwen2.5-32B: neutrality prompt against the original, settled and consensus items, version 1

original: <outputs>/qwen2.5-32b/original/judged_main_v1.jsonl

condition neutrality_prompt: <outputs>/qwen2.5-32b/neutrality_prompt/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: neutrality prompt

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 65.0/55.0 | 15.0/20.0 | 0.0/25.0 | 20.0/25.0 | 0.0/0.0 | +5.0 [-15.0, +30.0] | +5.0 [-10.0, +20.0] | +10.0 [-10.0, +30.0] |
| consensus | variant=none | 20 | 20 | 65.0/55.0 | 15.0/20.0 | 0.0/25.0 | 20.0/25.0 | 0.0/0.0 | +5.0 [-15.0, +30.0] | +5.0 [-10.0, +20.0] | +10.0 [-10.0, +30.0] |
| settled | all | 474 | 474 | 86.7/37.3 | 11.4/62.0 | 20.7/14.6 | 1.9/0.6 | 0.0/0.0 | +50.6 [+44.1, +57.2] | -1.3 [-2.7, +0.2] | +49.4 [+42.6, +56.3] |
| settled | variant=conservative | 158 | 158 | 86.1/35.4 | 12.0/63.9 | 27.8/16.5 | 1.9/0.6 | 0.0/0.0 | +51.9 [+44.3, +60.1] | -1.3 [-3.8, +1.3] | +50.6 [+42.4, +58.9] |
| settled | variant=liberal | 158 | 158 | 88.6/39.9 | 8.9/59.5 | 24.7/17.1 | 2.5/0.6 | 0.0/0.0 | +50.6 [+43.0, +58.2] | -1.9 [-5.1, +0.6] | +48.7 [+41.1, +57.0] |
| settled | variant=none | 158 | 158 | 85.4/36.7 | 13.3/62.7 | 9.5/10.1 | 1.3/0.6 | 0.0/0.0 | +49.4 [+41.8, +57.0] | -0.6 [-2.5, +1.3] | +48.7 [+40.5, +57.0] |
| settled | contested | 366 | 366 | 84.4/24.9 | 14.8/75.1 | 22.7/12.3 | 0.8/0.0 | 0.0/0.0 | +60.4 [+53.0, +67.8] | -0.8 [-1.9, +0.0] | +59.6 [+52.2, +66.7] |
| settled | uncontested | 108 | 108 | 94.4/79.6 | 0.0/17.6 | 13.9/22.2 | 5.6/2.8 | 0.0/0.0 | +17.6 [+8.3, +27.8] | -2.8 [-8.3, +2.8] | +14.8 [+3.7, +26.9] |
| settled | left-coded | 117 | 117 | 69.2/8.5 | 29.9/91.5 | 29.9/7.7 | 0.9/0.0 | 0.0/0.0 | +61.5 [+48.7, +73.5] | -0.9 [-2.6, +0.0] | +60.7 [+48.7, +73.5] |
| settled | right-coded | 177 | 177 | 93.2/33.3 | 5.6/66.7 | 18.1/15.8 | 1.1/0.0 | 0.0/0.0 | +61.0 [+50.8, +71.2] | -1.1 [-2.8, +0.0] | +59.9 [+49.2, +70.1] |
| settled | uncoded | 180 | 180 | 91.7/60.0 | 5.0/38.3 | 17.2/17.8 | 3.3/1.7 | 0.0/0.0 | +33.3 [+23.9, +43.9] | -1.7 [-5.0, +2.2] | +31.7 [+21.1, +42.8] |
| settled | contested x conservative | 122 | 122 | 82.8/20.5 | 15.6/79.5 | 29.5/12.3 | 1.6/0.0 | 0.0/0.0 | +63.9 [+54.9, +72.1] | -1.6 [-4.1, +0.0] | +62.3 [+53.3, +70.5] |
| settled | contested x liberal | 122 | 122 | 87.7/27.0 | 11.5/73.0 | 27.0/15.6 | 0.8/0.0 | 0.0/0.0 | +61.5 [+52.5, +70.5] | -0.8 [-2.5, +0.0] | +60.7 [+52.5, +69.7] |

#### answer length, mean words, original / treated

- consensus | all: 127 / 128
- contested | all: 240 / 185
- settled | all: 162 / 155
- settled | contested: 170 / 164
- settled | uncontested: 135 / 123
- settled | left-coded: 204 / 184
- settled | right-coded: 150 / 154
- settled | uncoded: 147 / 136
- settled | contested x conservative: 177 / 159
- settled | contested x liberal: 160 / 155

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 61.7/100.0 | 0.0/0.0 | 38.3/0.0 | 0.0/0.0 | +0.70/+0.02 |
| liberal | 60 | 76.7/100.0 | 23.3/0.0 | 0.0/0.0 | 0.0/0.0 | -0.27/+0.00 |
| none | 60 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.00/+0.00 |
