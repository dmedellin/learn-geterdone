---
format: long
lesson: trading-risk-management/volatility-and-atr-based-risk
title: Volatility and ATR: sizing for how far price is moving
thumb: Bigger bars, smaller size
---

@chapter The question
@title text="Volatility and ATR-Based Risk" sub="Trading Risk Management" art=thumb
Same market, same setup, same stop rule. But this week the candles are twice as big as last week. Should your trade look the same? The lesson says no, and gives you a number to adapt with.

@art regime
Markets move between calmer and wilder stretches. When that happens, the size that made sense last week can quietly create much larger dollar swings this week.

@art small-vs-large
Larger candles mean price is travelling farther during each period. When volatility expands, an unchanged stop is more likely to sit inside normal movement. And an unchanged position creates larger dollar swings.

@chapter True range and ATR
@art true-range
True range captures the bar's range, and any gap from the prior close. So a bar that opens well away from yesterday's close counts that jump too.

@words text="ATR = average of recent true ranges"
A T R, the average true range, is an average of recent true ranges. The lab uses a simple average. Most platforms use Wilder's smoothing. Either way, it's not a directional indicator.

@chapter Magnitude, not direction
@art up-down-same
What does A T R measure? Recent range magnitude. Not direction. A T R has no sign. An advance and a decline with the same bar sizes give the same A T R. And not win probability. It says how far bars travel, not how often a trade works.

@words text="High ATR = larger ranges" sub="not necessarily bullish · not necessarily bearish"
So high A T R means the market is moving through larger ranges. Not necessarily bullish, and not necessarily bearish. The lab's high volatility series has twice the A T R and finishes lower, but a rising series could carry the same A T R. Volatility describes movement size, not direction.

@chapter Volatility sizing
@art wider-fewer
Here's the sizing rule. A larger stop distance requires fewer units for the same planned account risk. So if A T R doubles while account risk stays fixed, position size should generally decrease.

@words text="ATR doubles → size halves"
Keep the size unchanged, and twice the stop distance doubles the planned loss. To hold the loss fixed, the quantity must halve. And doubling the size would quadruple the dollar swing per position.

@chapter Worked example
@math heading="ATR 1.50 · stop at 2 × ATR · risk $600" items="distance = 2 × 1.50 = 3.00@two times one fifty;;size = $600 ÷ $3.00 = 200 shares@two hundred shares"
Here's the lesson's example. A T R is one fifty. The stop is placed at two times A T R, and the dollar risk is six hundred. The distance is two times one fifty, three dollars. Six hundred divided by three is two hundred shares.

@math heading="Not these" items="✗  1.50 and 400 shares@four hundred;;✗  3.00 and 400 shares@mixes them up"
One fifty and four hundred shares uses one A T R instead of two. And three dollars with four hundred shares mixes them up: it divides six hundred by one A T R, while the stop is two A T Rs away.

@math heading="If ATR rises to 3.00" items="distance = 2 × 3.00 = 6.00@six dollar distance;;size = $600 ÷ $6.00 = 100 shares@a hundred shares"
And if A T R rises to three, the same six hundred dollars buys a hundred shares, at a six dollar distance. The risk in dollars didn't move. The quantity did.

@chapter Where people slip
@list heading="Common mistakes" items="Using ATR as a directional signal@The first|Fixed share size in every regime@The second|A stop exactly one ATR away, no structure@the third"
Three mistakes. The first is using A T R as a directional signal. The second is keeping a fixed share size in every volatility regime. And the third is placing the stop exactly one A T R away without structural context.

@art structure-first
That third one matters. A T R doesn't replace the chart. Use structure first, and volatility as a sizing input.

@list heading="Practical rules" items="Compare ATR on the same instrument and timeframe@same instrument|Structure first, volatility for sizing@structure first|Recalculate after a regime change@recalculate"
So compare A T R on the same instrument and timeframe. Use structure first, and volatility as a sizing input. And recalculate size after a volatility regime change.

@chapter Try it
@list heading="Lab steps" items="Identify the regime@identify the market regime|Separate direction from volatility@separate direction|Adapt quantity@adapt quantity"
The lab's steps: identify the market regime, comparing current range with the recent baseline. Separate direction from volatility, since large bars can occur in bullish, bearish, or balanced markets. Then adapt quantity, keeping account risk stable while the price distance changes.

@words text="Synthetic educational data" sub="no live market connection"
The lab uses simplified synthetic examples, with no live market connection. For practice, keep the six hundred dollars of risk and the two A T R stop, and work out the size when A T R is two twenty five.

@end text="Same dollars, different distance"
You can change the volatility regime and resize in the lab, on Learn. That's learn dot get er done dot I O.
