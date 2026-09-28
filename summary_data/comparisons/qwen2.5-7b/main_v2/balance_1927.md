# Qwen2.5-7B: balance fine-tuning, 1,927 answers against the original, settled and consensus items, version 2

original: <outputs>/qwen2.5-7b/original/judged_main_v2.jsonl

condition balance_1927: <outputs>/qwen2.5-7b/balance_1927/judged_main_v2.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: balance fine-tuning, 1,927 answers

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 50.0/15.0 | 15.0/50.0 | 0.0/0.0 | 25.0/25.0 | 10.0/10.0 | +35.0 [+10.0, +60.0] | +0.0 [-15.0, +15.0] | +35.0 [+15.0, +55.0] |
| consensus | variant=none | 20 | 20 | 50.0/15.0 | 15.0/50.0 | 0.0/0.0 | 25.0/25.0 | 10.0/10.0 | +35.0 [+10.0, +60.0] | +0.0 [-15.0, +15.0] | +35.0 [+15.0, +55.0] |
| settled | all | 474 | 474 | 90.5/19.4 | 8.0/79.7 | 21.5/10.5 | 1.5/0.6 | 0.0/0.2 | +71.7 [+65.8, +77.4] | -0.8 [-2.3, +0.4] | +70.9 [+65.0, +76.8] |
| settled | variant=conservative | 158 | 158 | 88.0/19.6 | 8.9/79.1 | 26.6/13.9 | 3.2/0.6 | 0.0/0.6 | +70.3 [+62.7, +77.2] | -2.5 [-5.7, +0.0] | +67.7 [+60.1, +75.3] |
| settled | variant=liberal | 158 | 158 | 90.5/17.7 | 8.2/81.0 | 23.4/10.1 | 1.3/1.3 | 0.0/0.0 | +72.8 [+65.8, +79.7] | +0.0 [-2.5, +2.5] | +72.8 [+65.8, +79.7] |
| settled | variant=none | 158 | 158 | 93.0/20.9 | 7.0/79.1 | 14.6/7.6 | 0.0/0.0 | 0.0/0.0 | +72.2 [+64.6, +79.7] | +0.0 [+0.0, +0.0] | +72.2 [+64.6, +79.7] |
| settled | contested | 366 | 366 | 89.1/11.5 | 9.0/87.7 | 22.7/6.3 | 1.9/0.8 | 0.0/0.0 | +78.7 [+72.7, +84.4] | -1.1 [-3.0, +0.8] | +77.6 [+71.6, +83.3] |
| settled | uncontested | 108 | 108 | 95.4/46.3 | 4.6/52.8 | 17.6/25.0 | 0.0/0.0 | 0.0/0.9 | +48.1 [+33.3, +62.0] | +0.0 [+0.0, +0.0] | +48.1 [+33.3, +62.0] |
| settled | left-coded | 78 | 78 | 76.9/11.5 | 21.8/88.5 | 34.6/7.7 | 1.3/0.0 | 0.0/0.0 | +66.7 [+51.3, +80.8] | -1.3 [-3.8, +0.0] | +65.4 [+50.0, +80.8] |
| settled | right-coded | 177 | 177 | 93.8/14.7 | 3.4/84.7 | 16.9/7.3 | 2.8/0.6 | 0.0/0.0 | +81.4 [+74.0, +88.1] | -2.3 [-5.6, +0.6] | +79.1 [+71.2, +86.4] |
| settled | uncoded | 219 | 219 | 92.7/26.0 | 6.8/72.6 | 20.5/14.2 | 0.5/0.9 | 0.0/0.5 | +65.8 [+56.2, +74.9] | +0.5 [-0.9, +1.8] | +66.2 [+56.6, +74.9] |
| settled | contested x conservative | 122 | 122 | 86.1/11.5 | 9.8/87.7 | 29.5/7.4 | 4.1/0.8 | 0.0/0.0 | +77.9 [+70.5, +85.2] | -3.3 [-7.4, +0.8] | +74.6 [+66.4, +82.0] |
| settled | contested x liberal | 122 | 122 | 89.3/9.8 | 9.0/88.5 | 21.3/4.9 | 1.6/1.6 | 0.0/0.0 | +79.5 [+71.3, +86.1] | +0.0 [-3.3, +3.3] | +79.5 [+71.3, +86.9] |

#### answer length, mean words, original / treated

- consensus | all: 146 / 157
- contested | all: 243 / 181
- settled | all: 182 / 178
- settled | contested: 189 / 182
- settled | uncontested: 160 / 164
- settled | left-coded: 219 / 188
- settled | right-coded: 171 / 176
- settled | uncoded: 179 / 176
- settled | contested x conservative: 193 / 180
- settled | contested x liberal: 189 / 174

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 65.0/100.0 | 0.0/0.0 | 35.0/0.0 | 0.0/0.0 | +0.63/+0.02 |
| liberal | 60 | 50.0/98.3 | 50.0/1.7 | 0.0/0.0 | 0.0/0.0 | -0.63/-0.03 |
| none | 60 | 98.3/100.0 | 1.7/0.0 | 0.0/0.0 | 0.0/0.0 | -0.03/+0.00 |
