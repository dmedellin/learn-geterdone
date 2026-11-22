---
format: long
lesson: volume-and-order-flow/accumulation-distribution-and-chaikin-money-flow
title: Accumulation/Distribution and Chaikin Money Flow, worked through
thumb: Where did it close?
---

@chapter The question
@title text="A/D and Chaikin Money Flow" sub="Volume and Order Flow" art=thumb
On Balance Volume only asks whether a bar closed up or down. But a bar has more to say than that. Where inside its range did it close? Two indicators build on that question, Accumulation Distribution and Chaikin Money Flow.

@art close-location
Here's the idea. Closing near the high suggests buying pressure. Closing near the low suggests selling pressure. Both indicators measure where price closes inside each bar's range, and weight that location by volume.

@words text="An inference, not an observation"
Keep one caveat in mind from the start. These tools infer pressure from close location and volume. They don't directly observe whether each trade hit the bid or lifted the ask.

@chapter The multiplier
@art multiplier-scale
The first piece is the money flow multiplier. It places the close on a scale from minus one, at the low of the bar, to plus one, at the high. A close exactly at the bar's midpoint scores zero.

@math heading="Money Flow Multiplier" items="MFM = ((C − L) − (H − C)) ÷ (H − L)@close minus low;;MFV = MFM × volume@times the bar's volume"
In symbols, take close minus low, subtract high minus close, and divide by high minus low. Then money flow volume is that multiplier times the bar's volume.

@chapter Worked example
@math heading="H 110 · L 100 · C 108 · V 1,000" items="C − L = 8@eight;;H − C = 2@two;;(8 − 2) ÷ 10 = 0.6@the range of ten;;0.6 × 1,000 = +600@six hundred"
Here's the lesson's bar. High one ten, low one hundred, close one oh eight, volume one thousand. Close minus low is eight. High minus close is two. Eight minus two is six, divided by the range of ten gives point six. Times one thousand, the money flow volume is plus six hundred.

@math heading="Two wrong multipliers" items="✗  8 ÷ 10 = 0.8@point eight;;✗  2 ÷ 10 = 0.2@point two"
Two slips are tempting. Point eight is close minus low over the range alone. It forgets to subtract the distance from the high. And point two is the distance from the high on its own. The real multiplier is point six.

@words text="Near the high, big volume → positive"
So a bar that closes near its high on large volume makes a positive contribution, and the large volume increases its effect. Negative would need the close nearer the low than the high.

@chapter The A/D line
@art ad-line
The Accumulation Distribution line cumulatively adds each bar's money flow volume. Bars that close high on heavy volume push it up. Bars that close low on heavy volume pull it down.

@chapter Chaikin Money Flow
@art cmf-window
Chaikin Money Flow looks at a window instead of a running total. It sums money flow volume over a lookback, and divides by total volume over the same bars.

@words text="CMF near zero" sub="balanced closing pressure over the lookback"
So what does C M F near zero mean? Balanced closing pressure. Positive and negative contributions roughly offset over the period. It doesn't mean a guaranteed range, since trending bars that close mid range give the same reading. And it doesn't mean no volume. With no volume, there's no reading at all.

@chapter What they can't see
@art four-numbers
Does A D identify actual aggressive buy and sell volume? No. It uses four numbers per bar, high, low, close and volume. No individual trade is ever classified. It infers pressure from bar location and volume.

@list heading="Common mistakes" items="Treating CMF as exact bid/ask delta@The first|Ignoring gaps between bars@The second|Fixed zero crossings without context@the third"
That leads to the common mistakes. The first is treating C M F as exact bid ask delta. The second is ignoring gaps between bars, a separate limitation. And the third is using fixed zero crossings without market context.

@art gap
A gap is worth a second look. The multiplier only sees each bar's own range, so a jump between one close and the next open never enters the calculation.

@chapter Try it
@words text="Synthetic educational data" sub="no live market connection"
The lab runs on synthetic educational data, with no live market connection. Follow its steps. Inspect close location. Weight by volume, since high volume closes count more. Then compare with price over a sequence, not one candle.

@words text="H 110 · L 100 · C 102 · V 1,000"
To practise, change one number in the worked example. Keep the high, low and volume, and move the close down to one oh two. Work out the multiplier and the money flow volume yourself, then check the sign makes sense.

@end text="Where it closed, weighted by volume"
You can try close location and volume together in the lab, on Learn. That's learn dot get er done dot I O.
