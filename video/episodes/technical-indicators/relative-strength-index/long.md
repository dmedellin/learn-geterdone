---
format: long
lesson: technical-indicators/relative-strength-index
title: RSI: what overbought and oversold really mean
thumb: Extreme isn't a reversal
---

@chapter The question
@title text="Relative Strength Index" sub="Technical Indicators" art=thumb
The RSI reads above seventy. Overbought, so it's time to sell? That's the shortcut a lot of people take, and the lesson is built to take it apart. An extreme RSI describes momentum. It doesn't command a reversal.

@words text="Momentum on a 0 to 100 scale"
RSI, the relative strength index, measures momentum on a bounded scale from zero to one hundred. Understanding how it's built is the fastest way to see what it can and can't tell you.

@chapter What it compares
@art gains-losses
RSI compares smoothed average gains with smoothed average losses over a selected period. On each bar, an up close adds to the gains side, and a down close adds to the losses side. The balance between the two is what the indicator reports.

@words text="Gains vs losses, not price level"
Notice what's not in there. RSI doesn't look at how high the price is, only at how the recent gains and losses compare. A stock can be at a record high with a middling RSI, or near a low with a high one.

@math heading="RSI" items="RS = average gain ÷ average loss@R S is;;RSI = 100 − 100 ÷ (1 + RS)@one hundred minus;;Wilder smoothing of gains and losses@Wilder"
In the usual form, R S is the average gain divided by the average loss. RSI is one hundred minus one hundred over one plus R S. This course uses Wilder style smoothing of the gains and losses. Seed values, rounding and incomplete bars can produce small differences across platforms.

@art bounded-scale
Because the result is normalized between zero and one hundred, momentum states are easier to compare across instruments and price levels. All gains pushes RSI toward one hundred. All losses pushes it toward zero.

@chapter The centerline
@art centerline
You don't need an extreme to learn something. RSI above or below fifty describes the balance of recent gains and losses. Above fifty, gains have outweighed losses over the period. Below fifty, losses have.

@chapter Thresholds depend on context
@art trend-pinned
Now the thresholds, often seventy and thirty. High RSI can persist in a strong uptrend, and low RSI can persist in a strong downtrend. A strong trend keeps feeding the gains side, so the reading can stay high while price keeps climbing.

@art early-sell
Selling the moment it crosses seventy would mean stepping in front of exactly the kind of move the indicator is describing. The reading was right about momentum. The shortcut was wrong about what to do with it.

@words text="Overbought: gains dominate · Oversold: losses dominate"
Here's the lesson's own rule. Overbought means recent gains dominate the selected window. Oversold means recent losses dominate. Neither word means price must reverse next.

@words text="Threshold contact ≠ reversal"
So touching a threshold, on its own, does not confirm a reversal. The lesson's lab makes the point with a count. It reports the longest run in the sample where RSI stayed above or below a threshold while price continued.

@art range-swings
In a sideways range, the same thresholds behave differently. RSI swings back and forth between the levels as price oscillates. That's why you test RSI in different regimes, rather than trusting one rule everywhere.

@chapter Interpret without shortcuts
@list heading="Interpret RSI" items="Set the period and smoothing@period|Observe the centerline@centerline|Evaluate threshold persistence@persistence|Require price confirmation@confirmation"
Use RSI as one condition inside a broader decision. Set the period and smoothing, and confirm the implementation uses the intended Wilder convention. Observe the centerline. Evaluate threshold persistence, how long RSI stays at an extreme. And require price confirmation: structure, location or a defined trigger, before turning an RSI reading into a trade decision.

@chapter Where people slip
@list heading="Common mistakes" items="Shorting every reading above 70@The first|Buying every reading below 30@The second|Comparing values with different settings@And the third"
The first mistake is shorting every RSI reading above seventy. Strong trends can keep high momentum while price continues higher. The second is buying every reading below thirty, since low momentum can persist in a strong decline. And the third is comparing values with different settings as if they were identical. Period, source, smoothing and timeframe all change what a reading means.

@chapter Try it
@words text="Current state · persistence · trend vs range · confirmation"
Your turn. Calculate the current RSI state, and count threshold persistence. Compare the trend and range scenarios. Then name the price confirmation your rule requires, as an exact event rather than a feeling. The goal is to explain an extreme without predicting a reversal.

@end text="Test RSI in different regimes"
You can change the period and thresholds, and watch how long RSI stays at an extreme, on Learn. That's learn dot get er done dot I O.
