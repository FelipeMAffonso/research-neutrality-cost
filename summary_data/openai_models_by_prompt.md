## The OpenAI models under the system prompts

Per cent of answers in each class, original / treated, and the treated-minus-original difference with a paired bootstrap 95 per cent interval over items (2,000 resamples). Five-class rubric; the item version is given per row.

| model | prompt | items | task | n | committed, original / treated | hedged, original / treated | adjacent balance, original / treated | wrong, original / treated | refusal, original / treated | difference in hedged, pp (95% CI) | difference in wrong, pp (95% CI) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GPT-4o | neutrality prompt | version 1 | consensus | 20 | 85.0/15.0 | 5.0/75.0 | 5.0/10.0 | 10.0/10.0 | 0.0/0.0 | +70.0 [+50.0, +90.0] | +0.0 [+0.0, +0.0] |
| GPT-4o | neutrality prompt | version 1 | settled | 474 | 92.0/16.7 | 7.8/83.1 | 18.4/7.6 | 0.2/0.2 | 0.0/0.0 | +75.3 [+69.4, +81.2] | +0.0 [-0.6, +0.6] |
| GPT-4o | journalist's balance norm | version 1 | consensus | 20 | 85.0/40.0 | 5.0/45.0 | 5.0/25.0 | 10.0/15.0 | 0.0/0.0 | +40.0 [+20.0, +60.0] | +5.0 [+0.0, +15.0] |
| GPT-4o | journalist's balance norm | version 1 | settled | 474 | 92.0/26.2 | 7.8/73.8 | 18.4/10.1 | 0.2/0.0 | 0.0/0.0 | +66.0 [+59.5, +72.4] | -0.2 [-0.6, +0.0] |
| GPT-4o | mandate wording, no government framing | version 1 | consensus | 20 | 85.0/80.0 | 5.0/10.0 | 5.0/0.0 | 10.0/10.0 | 0.0/0.0 | +5.0 [+0.0, +15.0] | +0.0 [+0.0, +0.0] |
| GPT-4o | mandate wording, no government framing | version 1 | settled | 474 | 92.0/91.6 | 7.8/8.2 | 18.4/14.3 | 0.2/0.2 | 0.0/0.0 | +0.4 [-1.7, +2.7] | +0.0 [-0.6, +0.6] |
| GPT-4o | mandate wording, federally procured assistant | version 1 | consensus | 20 | 85.0/85.0 | 5.0/5.0 | 5.0/5.0 | 10.0/10.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| GPT-4o | mandate wording, federally procured assistant | version 1 | settled | 474 | 92.0/93.0 | 7.8/7.0 | 18.4/16.9 | 0.2/0.0 | 0.0/0.0 | -0.8 [-3.6, +1.9] | -0.2 [-0.6, +0.0] |
| GPT-4o | mild even-handedness instruction | version 1 | consensus | 20 | 85.0/80.0 | 5.0/0.0 | 5.0/5.0 | 10.0/20.0 | 0.0/0.0 | -5.0 [-15.0, +0.0] | +10.0 [+0.0, +25.0] |
| GPT-4o | mild even-handedness instruction | version 1 | settled | 474 | 92.0/87.6 | 7.8/12.2 | 18.4/20.5 | 0.2/0.2 | 0.0/0.0 | +4.4 [+1.5, +7.6] | +0.0 [+0.0, +0.0] |
| GPT-4o | one-sentence instruction not to take sides | version 1 | consensus | 20 | 85.0/80.0 | 5.0/5.0 | 5.0/0.0 | 10.0/15.0 | 0.0/0.0 | +0.0 [-15.0, +15.0] | +5.0 [+0.0, +15.0] |
| GPT-4o | one-sentence instruction not to take sides | version 1 | settled | 474 | 92.0/85.2 | 7.8/14.6 | 18.4/12.9 | 0.2/0.2 | 0.0/0.0 | +6.8 [+3.6, +10.3] | +0.0 [-0.6, +0.6] |
| GPT-4o | style-only control | version 1 | consensus | 20 | 85.0/95.0 | 5.0/0.0 | 5.0/0.0 | 10.0/5.0 | 0.0/0.0 | -5.0 [-15.0, +0.0] | -5.0 [-15.0, +0.0] |
| GPT-4o | style-only control | version 1 | settled | 474 | 92.0/96.8 | 7.8/2.7 | 18.4/8.9 | 0.2/0.4 | 0.0/0.0 | -5.1 [-8.2, -2.3] | +0.2 [+0.0, +0.6] |
| GPT-4o | neutrality prompt | version 2 | consensus | 20 | 80.0/15.0 | 0.0/70.0 | 0.0/10.0 | 15.0/10.0 | 5.0/5.0 | +70.0 [+50.0, +90.0] | -5.0 [-15.0, +0.0] |
| GPT-4o | neutrality prompt | version 2 | settled | 474 | 92.8/17.7 | 6.8/82.1 | 16.7/8.6 | 0.4/0.2 | 0.0/0.0 | +75.3 [+69.4, +81.4] | -0.2 [-1.3, +0.6] |
| GPT-4o | journalist's balance norm | version 2 | consensus | 20 | 80.0/50.0 | 0.0/30.0 | 0.0/20.0 | 15.0/10.0 | 5.0/10.0 | +30.0 [+10.0, +50.0] | -5.0 [-15.0, +0.0] |
| GPT-4o | journalist's balance norm | version 2 | settled | 474 | 92.8/27.8 | 6.8/72.2 | 16.7/10.3 | 0.4/0.0 | 0.0/0.0 | +65.4 [+59.1, +71.9] | -0.4 [-1.3, +0.0] |
| GPT-4o | mandate wording, no government framing | version 2 | consensus | 20 | 80.0/80.0 | 0.0/0.0 | 0.0/0.0 | 15.0/15.0 | 5.0/5.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| GPT-4o | mandate wording, no government framing | version 2 | settled | 474 | 92.8/92.8 | 6.8/7.0 | 16.7/14.6 | 0.4/0.2 | 0.0/0.0 | +0.2 [-1.7, +2.5] | -0.2 [-0.6, +0.0] |
| GPT-4.1 | neutrality prompt | version 1 | consensus | 20 | 95.0/20.0 | 0.0/80.0 | 0.0/10.0 | 5.0/0.0 | 0.0/0.0 | +80.0 [+60.0, +95.0] | -5.0 [-15.0, +0.0] |
| GPT-4.1 | neutrality prompt | version 1 | settled | 474 | 98.3/15.4 | 1.1/84.4 | 3.0/6.1 | 0.6/0.2 | 0.0/0.0 | +83.3 [+78.5, +88.2] | -0.4 [-1.3, +0.4] |
| GPT-4.1 | journalist's balance norm | version 1 | consensus | 20 | 95.0/40.0 | 0.0/60.0 | 0.0/5.0 | 5.0/0.0 | 0.0/0.0 | +60.0 [+40.0, +80.0] | -5.0 [-15.0, +0.0] |
| GPT-4.1 | journalist's balance norm | version 1 | settled | 474 | 98.3/23.2 | 1.1/76.8 | 3.0/5.7 | 0.6/0.0 | 0.0/0.0 | +75.7 [+70.0, +81.6] | -0.6 [-1.5, +0.0] |
| GPT-4.1 | mandate wording, no government framing | version 1 | consensus | 20 | 95.0/90.0 | 0.0/5.0 | 0.0/0.0 | 5.0/5.0 | 0.0/0.0 | +5.0 [+0.0, +15.0] | +0.0 [-15.0, +15.0] |
| GPT-4.1 | mandate wording, no government framing | version 1 | settled | 474 | 98.3/98.3 | 1.1/1.5 | 3.0/1.7 | 0.6/0.2 | 0.0/0.0 | +0.4 [-1.1, +1.9] | -0.4 [-1.1, +0.0] |
| GPT-4.1 | neutrality prompt | version 2 | consensus | 20 | 90.0/25.0 | 0.0/70.0 | 0.0/10.0 | 10.0/0.0 | 0.0/5.0 | +70.0 [+50.0, +90.0] | -10.0 [-25.0, +0.0] |
| GPT-4.1 | neutrality prompt | version 2 | settled | 474 | 98.5/16.2 | 0.8/83.5 | 2.7/5.9 | 0.6/0.2 | 0.0/0.0 | +82.7 [+77.8, +87.8] | -0.4 [-1.3, +0.4] |
| GPT-4.1 | journalist's balance norm | version 2 | consensus | 20 | 90.0/40.0 | 0.0/50.0 | 0.0/15.0 | 10.0/5.0 | 0.0/5.0 | +50.0 [+30.0, +70.0] | -5.0 [-15.0, +0.0] |
| GPT-4.1 | journalist's balance norm | version 2 | settled | 474 | 98.5/24.1 | 0.8/75.9 | 2.7/5.7 | 0.6/0.0 | 0.0/0.0 | +75.1 [+69.6, +80.8] | -0.6 [-1.5, +0.0] |
| GPT-4.1 | mandate wording, no government framing | version 2 | consensus | 20 | 90.0/85.0 | 0.0/0.0 | 0.0/0.0 | 10.0/10.0 | 0.0/5.0 | +0.0 [+0.0, +0.0] | +0.0 [-15.0, +15.0] |
| GPT-4.1 | mandate wording, no government framing | version 2 | settled | 474 | 98.5/98.9 | 0.8/1.1 | 2.7/2.3 | 0.6/0.0 | 0.0/0.0 | +0.2 [-1.1, +1.7] | -0.6 [-1.5, +0.0] |
| GPT-5.4 | neutrality prompt | version 1 | consensus | 20 | 95.0/95.0 | 0.0/5.0 | 0.0/0.0 | 5.0/0.0 | 0.0/0.0 | +5.0 [+0.0, +15.0] | -5.0 [-15.0, +0.0] |
| GPT-5.4 | neutrality prompt | version 1 | settled | 474 | 98.9/66.2 | 1.1/33.8 | 4.4/9.7 | 0.0/0.0 | 0.0/0.0 | +32.7 [+26.6, +38.8] | +0.0 [+0.0, +0.0] |
| GPT-5.4 | journalist's balance norm | version 1 | consensus | 20 | 95.0/90.0 | 0.0/5.0 | 0.0/5.0 | 5.0/5.0 | 0.0/0.0 | +5.0 [+0.0, +15.0] | +0.0 [+0.0, +0.0] |
| GPT-5.4 | journalist's balance norm | version 1 | settled | 474 | 98.9/71.7 | 1.1/28.3 | 4.4/8.0 | 0.0/0.0 | 0.0/0.0 | +27.2 [+21.9, +32.9] | +0.0 [+0.0, +0.0] |
| GPT-5.4 | mandate wording, no government framing | version 1 | consensus | 20 | 95.0/95.0 | 0.0/0.0 | 0.0/0.0 | 5.0/5.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [-15.0, +15.0] |
| GPT-5.4 | mandate wording, no government framing | version 1 | settled | 474 | 98.9/99.2 | 1.1/0.8 | 4.4/2.1 | 0.0/0.0 | 0.0/0.0 | -0.2 [-1.5, +0.8] | +0.0 [+0.0, +0.0] |
| GPT-5.4 | neutrality prompt | version 2 | consensus | 20 | 95.0/90.0 | 0.0/5.0 | 0.0/0.0 | 5.0/5.0 | 0.0/0.0 | +5.0 [+0.0, +15.0] | +0.0 [+0.0, +0.0] |
| GPT-5.4 | neutrality prompt | version 2 | settled | 474 | 98.7/70.0 | 1.1/30.0 | 3.8/10.5 | 0.2/0.0 | 0.0/0.0 | +28.9 [+23.0, +34.8] | -0.2 [-0.6, +0.0] |
| GPT-5.5 | neutrality prompt | version 1 | consensus | 20 | 100.0/100.0 | 0.0/0.0 | 5.0/5.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| GPT-5.5 | neutrality prompt | version 1 | settled | 474 | 99.6/93.9 | 0.4/6.1 | 9.3/17.5 | 0.0/0.0 | 0.0/0.0 | +5.7 [+3.4, +8.4] | +0.0 [+0.0, +0.0] |
| GPT-5.5 | journalist's balance norm | version 1 | consensus | 20 | 100.0/95.0 | 0.0/0.0 | 5.0/5.0 | 0.0/5.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +5.0 [+0.0, +15.0] |
| GPT-5.5 | journalist's balance norm | version 1 | settled | 474 | 99.6/92.0 | 0.4/8.0 | 9.3/15.4 | 0.0/0.0 | 0.0/0.0 | +7.6 [+4.9, +10.8] | +0.0 [+0.0, +0.0] |
| GPT-5.5 | mandate wording, no government framing | version 1 | consensus | 20 | 100.0/100.0 | 0.0/0.0 | 5.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| GPT-5.5 | mandate wording, no government framing | version 1 | settled | 474 | 99.6/100.0 | 0.4/0.0 | 9.3/6.1 | 0.0/0.0 | 0.0/0.0 | -0.4 [-1.1, +0.0] | +0.0 [+0.0, +0.0] |
| GPT-5.5 | neutrality prompt | version 2 | consensus | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| GPT-5.5 | neutrality prompt | version 2 | settled | 474 | 99.6/94.5 | 0.2/5.5 | 9.5/17.1 | 0.2/0.0 | 0.0/0.0 | +5.3 [+3.2, +7.8] | -0.2 [-0.6, +0.0] |
| GPT-5.6-luna | neutrality prompt | version 1 | consensus | 20 | 100.0/90.0 | 0.0/10.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +10.0 [+0.0, +25.0] | +0.0 [+0.0, +0.0] |
| GPT-5.6-luna | neutrality prompt | version 1 | settled | 474 | 99.2/97.3 | 0.8/2.7 | 15.0/14.6 | 0.0/0.0 | 0.0/0.0 | +1.9 [+0.2, +3.6] | +0.0 [+0.0, +0.0] |
| GPT-5.6-luna | journalist's balance norm | version 1 | consensus | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| GPT-5.6-luna | journalist's balance norm | version 1 | settled | 474 | 99.2/96.0 | 0.8/4.0 | 15.0/12.0 | 0.0/0.0 | 0.0/0.0 | +3.2 [+1.3, +5.5] | +0.0 [+0.0, +0.0] |
| GPT-5.6-luna | mandate wording, no government framing | version 1 | consensus | 20 | 100.0/95.0 | 0.0/0.0 | 0.0/0.0 | 0.0/5.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +5.0 [+0.0, +15.0] |
| GPT-5.6-luna | mandate wording, no government framing | version 1 | settled | 474 | 99.2/99.2 | 0.8/0.8 | 15.0/6.8 | 0.0/0.0 | 0.0/0.0 | +0.0 [-0.8, +0.8] | +0.0 [+0.0, +0.0] |
| GPT-5.6-luna | neutrality prompt | version 2 | consensus | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| GPT-5.6-luna | neutrality prompt | version 2 | settled | 474 | 99.4/97.9 | 0.4/2.1 | 14.8/12.7 | 0.2/0.0 | 0.0/0.0 | +1.7 [+0.2, +3.2] | -0.2 [-0.6, +0.0] |
| GPT-5.6-sol | neutrality prompt | version 1 | consensus | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| GPT-5.6-sol | neutrality prompt | version 1 | settled | 474 | 99.6/97.0 | 0.2/2.7 | 15.8/19.4 | 0.2/0.2 | 0.0/0.0 | +2.5 [+1.1, +4.4] | +0.0 [+0.0, +0.0] |
| GPT-5.6-sol | journalist's balance norm | version 1 | consensus | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| GPT-5.6-sol | journalist's balance norm | version 1 | settled | 474 | 99.6/95.8 | 0.2/4.2 | 15.8/22.2 | 0.2/0.0 | 0.0/0.0 | +4.0 [+2.1, +6.3] | -0.2 [-0.6, +0.0] |
| GPT-5.6-sol | mandate wording, no government framing | version 1 | consensus | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| GPT-5.6-sol | mandate wording, no government framing | version 1 | settled | 474 | 99.6/98.9 | 0.2/0.6 | 15.8/11.2 | 0.2/0.4 | 0.0/0.0 | +0.4 [+0.0, +1.1] | +0.2 [+0.0, +0.6] |
| GPT-5.6-sol | neutrality prompt | version 2 | consensus | 20 | 100.0/95.0 | 0.0/5.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +5.0 [+0.0, +15.0] | +0.0 [+0.0, +0.0] |
| GPT-5.6-sol | neutrality prompt | version 2 | settled | 474 | 99.2/98.5 | 0.4/1.3 | 17.1/19.2 | 0.4/0.2 | 0.0/0.0 | +0.8 [-0.2, +2.1] | -0.2 [-0.6, +0.0] |
| GPT-5.6-terra | neutrality prompt | version 1 | consensus | 20 | 95.0/95.0 | 0.0/0.0 | 0.0/0.0 | 5.0/5.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| GPT-5.6-terra | neutrality prompt | version 1 | settled | 474 | 99.6/96.8 | 0.2/3.2 | 12.7/21.1 | 0.2/0.0 | 0.0/0.0 | +3.0 [+1.5, +4.6] | -0.2 [-0.6, +0.0] |
| GPT-5.6-terra | journalist's balance norm | version 1 | consensus | 20 | 95.0/100.0 | 0.0/0.0 | 0.0/5.0 | 5.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -5.0 [-15.0, +0.0] |
| GPT-5.6-terra | journalist's balance norm | version 1 | settled | 474 | 99.6/94.3 | 0.2/5.7 | 12.7/19.8 | 0.2/0.0 | 0.0/0.0 | +5.5 [+3.0, +8.2] | -0.2 [-0.6, +0.0] |
| GPT-5.6-terra | one-sentence instruction not to take sides | version 1 | consensus | 20 | 95.0/100.0 | 0.0/0.0 | 0.0/5.0 | 5.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -5.0 [-15.0, +0.0] |
| GPT-5.6-terra | one-sentence instruction not to take sides | version 1 | settled | 474 | 99.6/99.8 | 0.2/0.2 | 12.7/12.4 | 0.2/0.0 | 0.0/0.0 | +0.0 [-0.6, +0.6] | -0.2 [-0.6, +0.0] |
| GPT-5.6-terra | neutral-point-of-view rule | version 1 | consensus | 20 | 95.0/100.0 | 0.0/0.0 | 0.0/5.0 | 5.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | -5.0 [-15.0, +0.0] |
| GPT-5.6-terra | neutral-point-of-view rule | version 1 | settled | 474 | 99.6/99.4 | 0.2/0.6 | 12.7/13.1 | 0.2/0.0 | 0.0/0.0 | +0.4 [-0.4, +1.5] | -0.2 [-0.6, +0.0] |
| GPT-5.6-terra | explicit both-sides instruction | version 1 | consensus | 20 | 95.0/30.0 | 0.0/70.0 | 0.0/5.0 | 5.0/0.0 | 0.0/0.0 | +70.0 [+50.0, +90.0] | -5.0 [-15.0, +0.0] |
| GPT-5.6-terra | explicit both-sides instruction | version 1 | settled | 474 | 99.6/41.8 | 0.2/58.2 | 12.7/14.8 | 0.2/0.0 | 0.0/0.0 | +58.0 [+52.3, +63.9] | -0.2 [-0.6, +0.0] |
| GPT-5.6-terra | neutrality prompt | version 2 | consensus | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| GPT-5.6-terra | neutrality prompt | version 2 | settled | 474 | 99.8/97.5 | 0.2/2.5 | 11.8/20.3 | 0.0/0.0 | 0.0/0.0 | +2.3 [+1.1, +3.8] | +0.0 [+0.0, +0.0] |
| GPT-5.6-terra | journalist's balance norm | version 2 | consensus | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/5.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| GPT-5.6-terra | journalist's balance norm | version 2 | settled | 474 | 99.8/94.1 | 0.2/5.9 | 11.8/19.4 | 0.0/0.0 | 0.0/0.0 | +5.7 [+3.2, +8.4] | +0.0 [+0.0, +0.0] |
| GPT-5.6-terra | mandate wording, no government framing | version 2 | consensus | 20 | 100.0/100.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | 0.0/0.0 | +0.0 [+0.0, +0.0] | +0.0 [+0.0, +0.0] |
| GPT-5.6-terra | mandate wording, no government framing | version 2 | settled | 474 | 99.8/100.0 | 0.2/0.0 | 11.8/9.1 | 0.0/0.0 | 0.0/0.0 | -0.2 [-0.6, +0.0] | +0.0 [+0.0, +0.0] |
