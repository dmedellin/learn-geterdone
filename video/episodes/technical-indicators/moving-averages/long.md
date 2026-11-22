---
format: long
lesson: technical-indicators/moving-averages
title: Simple and exponential moving averages: same period, different weights
thumb: Both lag. One less.
---

@chapter The question
@title text="Simple and Exponential Moving Averages" sub="Technical Indicators" art=thumb
Two moving averages, the same period, the same prices. One turns sooner than the other. Why? The only difference is how each one weights the observations inside it.

@words text="Same inputs · different weighting"
That's why the lesson compares them with identical inputs. Same price source, same period. Whatever is left between the two lines comes from weighting, and nothing else. That's the cleanest way to see what weighting actually does.

@chapter Simple moving average
@art equal-weights
The simple moving average, the SMA, gives equal weight to every observation in its window. It changes when a new value enters and the oldest value leaves. So the oldest bar counts exactly as much as the newest, right up until it drops out.

@math heading="SMA" items="SMA = (P₁ + … + Pₙ) ÷ n@add the n prices;;Every price weight: 1 ÷ n@equal weight"
You add the n prices and divide by n. Every price in the window has an equal weight of one over n.

@chapter Exponential moving average
@art decaying-weights
The exponential moving average, the EMA, applies more weight to recent observations, while keeping a decaying influence from earlier data. Nothing falls out of the window all at once. Older prices just matter less and less.

@math heading="EMA, as this course computes it" items="α = 2 ÷ (period + 1)@alpha equals;;Period 20: α = 2 ÷ 21 ≈ 0.095@twenty"
In this course, the smoothing factor alpha equals two over the period plus one. For a twenty period EMA, that's two over twenty one, about zero point zero nine five. So the newest price gets a bit under a tenth of the weight.

@math heading="Seed, then update" items="Seed: the first complete SMA@seeded;;EMAₜ = α · Pₜ + (1 − α) · EMAₜ₋₁@each new EMA"
The EMA is seeded with the first complete SMA, then updated on every bar. Each new EMA is alpha times the new price, plus one minus alpha times the previous EMA. Some charting platforms use a different seed.

@art seed-start
That seed is one reason two platforms can disagree, especially near the start of a chart. The longer the series runs, the less the starting point matters, because its influence keeps decaying.

@chapter Which reacts faster
@art shock-response
Now hit the series with a shock, a sudden jump. The EMA generally responds faster for the same nominal period, because the newest price carries more weight. The SMA catches up more slowly, as the shock bar works its way through an evenly weighted window.

@art lag-gap
But don't call the EMA leading and the SMA lagging. That's the lesson's first common mistake. Both are built from historical data, and both lag price. The EMA just lags less.

@chapter The tradeoff
@art regimes-three
Whatever the type, short periods follow price closely and generate more changes. Long periods smooth noise, but respond later to turns and shocks. That faster response helps when a real trend starts.

@words text="Helps in a trend · hurts in a range"
It hurts in a choppy range, where it reacts to noise and turns back and forth. The same responsiveness is a strength in one regime and a weakness in another, which is exactly what the lesson wants you to be able to explain.

@list heading="Use moving averages correctly" items="Choose the price source@price source|Choose the horizon@horizon|Define the interpretation@interpretation|Validate in different regimes@validate"
So treat an average as a trend reference, not a complete trading system. Choose the price source, close or typical price, and document it. Choose the horizon to match your timeframe. Define the interpretation: slope, price position, distance, or a crossover. And validate the setting in a trend, a range, and a sudden reversal, before you rely on it in any of them.

@chapter Where people slip
@list heading="Common mistakes" items="Calling EMA leading, SMA lagging@The first|A period without a timeframe@The second|Price above an average is enough@The third"
The first mistake, again, is calling the EMA leading and the SMA lagging. The second is using a period without a timeframe. A twenty period average means very different horizons on a five minute, an hourly, and a daily chart. And the third is assuming price above an average is enough. Location, structure, volatility and invalidation still matter.

@chapter Try it
@words text="One source · one period · both lines"
Your turn. Use one source and one period, and calculate both the SMA and the EMA. Say which reacts faster after a shock. Then explain why that responsiveness can help in one market regime, and hurt in another.

@end text="Compare the two weightings"
You can switch the source and period and compare both lines, on Learn. That's learn dot get er done dot I O.
