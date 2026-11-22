---
format: long
lesson: technical-indicators/average-true-range
title: Average true range: measuring volatility, gaps included
thumb: Size of the move, not direction
---

@chapter The question
@title text="Average True Range" sub="Technical Indicators" art=thumb
A stock gaps down overnight and then trades in a narrow range all day. Was that a quiet day? If you only measure high minus low, it looks like one. True range is built so a gap like that still counts.

@words text="How much does price move?" sub="not which way"
Average true range answers one question: how much is price moving, recently, in absolute terms? It says nothing about which way. That's the first thing to hold on to, because almost every mistake with ATR comes from forgetting it.

@chapter True range
@art three-components
True range is the largest of three components. The bar's high minus its low. The distance from the high to the previous close. And the distance from the low to the previous close. Whichever is largest becomes the bar's true range.

@math heading="True range" items="TR = max(H − L, |H − Cₚ|, |L − Cₚ|)@the maximum of;;Cₚ = previous close@previous close;;First bar: TR = H − L@first true range"
In symbols, true range is the maximum of high minus low, the absolute value of high minus previous close, and the absolute value of low minus previous close. The first true range just uses high minus low, because there's no previous close yet.

@chapter Why gaps matter
@art gap-bar
Here's why the extra two components exist. On a normal bar, high minus low is usually the largest, so it controls. But after a gap, the distance from the previous close can be much bigger than the bar's own range. Then that component takes over, and the gap gets counted.

@words text="High–low only misses the gap"
That's one of the lesson's common mistakes: using high minus low only after a gap. True range has to include the distance from the previous close, or the overnight move simply disappears from the measurement.

@chapter Average true range
@art atr-line
ATR smooths true range over a selected period to estimate recent absolute movement. This course uses Wilder style smoothing, applied after a complete seed window. So ATR rises when bars or gaps get bigger, and falls when they shrink. Because it's smoothed, one huge bar lifts it, but doesn't take it over, and the effect fades as later bars come in.

@art rally-and-drop
And it rises for any kind of big movement. ATR can climb during a rally, during a decline, after gaps, or in an unstable range. Its value is never negative, and it doesn't indicate bullish or bearish direction. Reading rising ATR as bullish is the first common mistake.

@chapter ATR as a percentage
@math heading="Normalize when comparing" items="ATR% = ATR ÷ price × 100@divide ATR by price;;Raw ATR is in price units@price units"
Raw ATR is in price units, dollars. That makes it hard to compare between instruments. So divide ATR by price, and multiply by one hundred, to get ATR as a percentage of price.

@art two-scales
ATR dollars aren't directly comparable between a ten dollar instrument and a five hundred dollar instrument. The same dollar ATR is a big move for one and a small move for the other. Normalization lets you compare them on the same footing. And it helps on one instrument too, when its price has changed a lot over the history you're looking at.

@chapter Calculate and use ATR
@art atr-steps
Put together, using ATR is a short routine, and it's the same every time.

@list heading="Calculate and use ATR" items="Calculate all three components@all three|Choose the maximum@the maximum|Apply Wilder smoothing@Wilder|Normalize when comparing@normalize"
So measure movement consistently before you use volatility in sizing, filters, or stop logic. Calculate all three true range components. Choose the maximum. Apply Wilder smoothing with a consistent seed and update rule. And normalize when comparing instruments or price levels.

@chapter Where people slip
@list heading="Common mistakes" items="Reading rising ATR as bullish@The first|High minus low only after a gap@The second|Comparing raw ATR across price scales@The third"
The first mistake is reading rising ATR as bullish, when volatility can rise in either direction, or during chaotic sideways movement. The second is using high minus low only after a gap. The third is comparing raw ATR across different price scales. The first and third are about what ATR means. The second is about calculating it correctly.

@chapter Try it
@words text="A gap bar and a normal bar"
Your turn. Select a gap bar and a normal bar. Calculate all three components for each, and identify the maximum. Update ATR, and explain the difference between raw ATR and ATR as a percentage.

@end text="Inspect true range bar by bar"
You can select any bar and see which component controls it, on Learn. That's learn dot get er done dot I O.
