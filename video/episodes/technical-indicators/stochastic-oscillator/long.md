---
format: long
lesson: technical-indicators/stochastic-oscillator
title: The stochastic oscillator: where the close sits in its range
thumb: Range position, not speed
---

@chapter The question
@title text="Stochastic Oscillator" sub="Technical Indicators" art=thumb
In a strong uptrend, the stochastic oscillator can sit near one hundred for bar after bar. Is it broken? No. Once you see the formula, you'll see why it has to do that, and why it behaves so differently in a sideways market.

@words text="Where is the close inside its recent range?"
The stochastic oscillator answers one question. Where does the current close sit inside its recent high to low range? At the top, at the bottom, or somewhere in between? That's range position, and it's the whole idea.

@chapter Range position
@art range-box
Pick a lookback, a number of recent bars. Find the highest high and the lowest low across those bars. That's the range. Now look at where the current close falls inside it.

@math heading="Raw %K" items="Raw %K = (C − LL) ÷ (HH − LL) × 100@close minus;;C = current close@current close;;HH, LL = highest high, lowest low in the lookback@highest high"
Raw percent K is the close minus the lowest low, divided by the highest high minus the lowest low, times one hundred. C is the current close. H H and L L are the highest high and lowest low across the lookback. So it's the close as a percentage of the range.

@art close-top-bottom
A close at the very top of the range gives one hundred. A close at the very bottom gives zero. A close exactly halfway gives fifty. It measures position, not how fast price is moving. A slow drift to the top of the range and a sudden jump to the top give the same reading.

@chapter Percent K and percent D
@art k-and-d
Then come two layers of smoothing. Percent K is the faster line after optional smoothing. In this lesson, that's a simple moving average of raw percent K. Percent D is a moving average of percent K, so it reacts more slowly. This lesson uses a simple moving average for that as well.

@words text="Document each smoothing period"
Each of those smoothing periods changes signal timing, so write them down. Fast, slow and full stochastic variants can produce very different crossing behavior, and platforms differ.

@chapter Why it pins in a trend
@art trend-pinned-stoch
Now the puzzle from the start. In a persistent uptrend, each new close tends to land near the top of the recent range, because the range keeps being set by the trend itself. So raw percent K stays near one hundred. In a downtrend, the closes keep landing near the bottom, and it stays near zero.

@art range-turning
In a sideways market, price travels back and forth across the range. The close moves from near the top to near the bottom and back, so the oscillator turns, and percent K and percent D cross. That's why crosses and extremes can be useful in a range, but stay pinned in a persistent trend.

@chapter Settings and crossings
@list heading="Read the stochastic" items="Define the recent range@Define|Calculate raw position@calculate|Apply %K and %D smoothing@apply|Interpret the regime@interpret"
To read it, define the recent range, with the lookback that finds the highest high and lowest low. Calculate the raw position of the close. Apply the percent K and percent D smoothing. And interpret the regime, using extremes and crossings differently in a range than in a trend.

@art crossing-count
And the settings change the count. Short lookbacks and light smoothing produce more crossings. Longer settings produce fewer, slower changes. The lab lets you watch that happen: shorten the lookback, and the line gets jumpier and the crossings multiply.

@chapter Where people slip
@list heading="Common mistakes" items="Confusing stochastic with price velocity@The first|Buying or selling every extreme@The second|Ignoring smoothing settings@The third"
The first mistake is confusing the stochastic with price velocity. It mainly measures range position, not a direct rate of change. The second is buying or selling every extreme, because the oscillator can stay near zero or one hundred while a trend extends. And the third is ignoring smoothing settings.

@chapter Try it
@words text="Highest high · lowest low · close → raw %K"
Your turn. Identify the highest high, the lowest low and the close, and calculate raw percent K. Explain the effect of each smoothing input. Then compare crossing behavior in a trend and in a range.

@end text="Change the lookback and smoothing"
You can change the range lookback and both smoothing periods, on Learn. That's learn dot get er done dot I O.
