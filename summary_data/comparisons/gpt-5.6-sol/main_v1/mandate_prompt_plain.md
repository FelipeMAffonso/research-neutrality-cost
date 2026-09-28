# GPT-5.6-sol: mandate wording, no government framing against the original, settled and consensus items, version 1

original: <outputs>/gpt-5.6-sol/original/judged_main_v1.jsonl

condition mandate_prompt_plain: <outputs>/gpt-5.6-sol/mandate_prompt_plain/judged_main_v1.jsonl

## Five-class rates (per cent) and treated minus original in pp, paired bootstrap 95 per cent over items

### condition: mandate wording, no government framing

| task | items | n original | n treated | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) | difference in hedged or wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| consensus | all | 20 | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| consensus | variant=none | 20 | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | all | 474 | 474 | 99.6/98.9 | 0.2/0.6 | 15.8/11.2 | 0.2/0.4 | 0.0/0.0 | +0.4 [+0.0, +1.1] | +0.2 [+0.0, +0.6] | +0.6 [+0.0, +1.5] |
| settled | variant=conservative | 158 | 158 | 100.0/100.0 | 0.0/0.0 | 19.0/14.6 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | variant=liberal | 158 | 158 | 100.0/98.7 | 0.0/0.6 | 21.5/15.8 | 0.0/0.6 | 0.0/0.0 | +0.6 [+0.0, +1.9] | +0.6 [+0.0, +1.9] | +1.3 [+0.0, +3.2] |
| settled | variant=none | 158 | 158 | 98.7/98.1 | 0.6/1.3 | 7.0/3.2 | 0.6/0.6 | 0.0/0.0 | +0.6 [+0.0, +1.9] | +0.0 [+0.0, +0.0] | +0.6 [+0.0, +1.9] |
| settled | contested | 366 | 366 | 99.5/98.9 | 0.3/0.5 | 15.6/9.6 | 0.3/0.5 | 0.0/0.0 | +0.3 [+0.0, +0.8] | +0.3 [+0.0, +0.8] | +0.5 [+0.0, +1.4] |
| settled | uncontested | 108 | 108 | 100.0/99.1 | 0.0/0.9 | 16.7/16.7 | 0.0/0.0 | 0.0/0.0 | +0.9 [+0.0, +2.8] | +0.0 [+0.0, +0.0] | +0.9 [+0.0, +2.8] |
| settled | left-coded | 117 | 117 | 99.1/99.1 | 0.9/0.9 | 24.8/15.4 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | right-coded | 177 | 177 | 99.4/98.3 | 0.0/0.6 | 11.3/6.2 | 0.6/1.1 | 0.0/0.0 | +0.6 [+0.0, +1.7] | +0.6 [+0.0, +1.7] | +1.1 [+0.0, +2.8] |
| settled | uncoded | 180 | 180 | 100.0/99.4 | 0.0/0.6 | 14.4/13.3 | 0.0/0.0 | 0.0/0.0 | +0.6 [+0.0, +1.7] | +0.0 [+0.0, +0.0] | +0.6 [+0.0, +1.7] |
| settled | contested x conservative | 122 | 122 | 100.0/100.0 | 0.0/0.0 | 18.9/11.5 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| settled | contested x liberal | 122 | 122 | 100.0/99.2 | 0.0/0.0 | 20.5/13.1 | 0.0/0.8 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.8 [+0.0, +2.5] | +0.8 [+0.0, +2.5] |

#### answer length, mean words, original / treated

- consensus | all: 49 / 66
- contested | all: 187 / 241
- settled | all: 108 / 127
- settled | contested: 119 / 140
- settled | uncontested: 70 / 86
- settled | left-coded: 133 / 158
- settled | right-coded: 113 / 132
- settled | uncoded: 86 / 102
- settled | contested x conservative: 127 / 146
- settled | contested x liberal: 112 / 131

#### contested questions: position taken and mean lean (-2 left to +2 right)

| variant | n | both sides, original / treated | takes left, original / treated | takes right, original / treated | refusal, original / treated | mean lean, original / treated |
|---|---|---|---|---|---|---|
| conservative | 60 | 38.3/51.7 | 5.0/6.7 | 56.7/41.7 | 0.0/0.0 | +0.82/+0.50 |
| liberal | 60 | 28.3/60.0 | 70.0/38.3 | 1.7/1.7 | 0.0/0.0 | -0.78/-0.37 |
| none | 60 | 48.3/68.3 | 48.3/30.0 | 3.3/1.7 | 0.0/0.0 | -0.53/-0.28 |
