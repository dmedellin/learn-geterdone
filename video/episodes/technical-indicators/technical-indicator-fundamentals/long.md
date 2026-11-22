---
format: long
lesson: technical-indicators/technical-indicator-fundamentals
title: Technical indicators: what they calculate, and what they can't tell you
thumb: A calculation, not a forecast
---

@chapter The question
@title text="Technical Indicator Fundamentals" sub="Technical Indicators" art=thumb
There's a line drawn over the price chart, and a platform has given it a familiar name. Before you trust it, can you say exactly which bars produced its latest value? If you can't, you don't really know what it's telling you.

@words text="An indicator is a calculation"
An indicator applies a defined calculation to price or other market data. It summarizes information. It does not observe the future. Everything in this course starts from that.

@chapter One value, rebuilt
@art lookback-window
The lesson uses the simplest example, a simple moving average of closing prices. Pick a bar. The lookback window is that bar and the bars just before it, as many as the lookback length. The average of those closes is the indicator's value at that bar.

@math heading="Simple moving average" items="SMA = (C₁ + C₂ + … + Cₙ) ÷ n@add up;;n = lookback length@lookback length;;Cᵢ = the closes inside the window@inside the window"
Add up the n closes inside the window and divide by n, where n is the lookback length. That's all. Move the selected bar one step to the right, and the newest close enters the window while the oldest one leaves.

@chapter Warm-up
@art warm-up-gap
That tells you something useful about the start of the chart. Until there are enough bars to fill the window, there's no value at all. That stretch is the warm-up period. A longer lookback means a longer warm-up.

@math heading="Warm-up" items="Lookback 20 → first value at bar 20@lookback of twenty;;Bars 1 to 19: no value@before that"
With a lookback of twenty, the first value can't appear until the twentieth bar, because before that there aren't twenty closes to average. And the first values that do appear deserve a little less trust.

@chapter Lookback and lag
@art fast-slow-lines
Now change the lookback. Shorter windows react faster and fluctuate more. Longer windows smooth more data and usually respond later. A short average hugs the price. A long one drifts behind it, and turns well after the price has turned.

@words text="Faster ↔ noisier · Smoother ↔ later"
There's no free setting. Every choice of lookback trades responsiveness for smoothness. The question is which one your decision actually needs.

@chapter Conventions
@art two-platforms
Even with the same name and the same lookback, two platforms can show slightly different values. The input source, the smoothing method, the seed value, rounding, and the treatment of missing bars can all differ. Those small differences can move the exact bar where a crossover or threshold happens.

@words text="Verify against your implementation"
So when a value matters, don't assume your platform matches a textbook, or another platform. Check its input, its smoothing and its seed, and reproduce one value by hand before you build a rule on top of it.

@chapter Evaluate any indicator
@list heading="Four questions" items="Identify the input@Identify the input|Write the formula@write the formula|Determine the purpose@determine the purpose|Define the decision rule@define the decision rule"
So before you trust a familiar name or a default setting, use the same sequence. Identify the input: close, high, low, true range, volume, or another derived series. Write the formula, with the lookback, smoothing, thresholds and warm-up. Determine the purpose. And define the decision rule.

@art decision-rule
Purpose means the job the indicator does. Is it measuring trend, momentum, volatility, a breakout boundary, or something else? Two indicators with different jobs answer different questions, and the rest of this course takes those families one at a time.

@art context-needed
That last step matters most. State exactly what condition matters, and what price action or risk condition must confirm it. An indicator reading on its own isn't a decision. It still needs market context.

@chapter Where people slip
@list heading="Common mistakes" items="Treating it as a prediction engine@The first|Changing parameters after the result@The second|Ignoring warm-up and conventions@The third"
The first mistake is treating an indicator as a prediction engine. Its output is a transformation of historical observations, not a guarantee about the next bar. The second is changing parameters after seeing the result. Retuning a lookback to fit one chart creates hindsight bias and unstable rules. And the third is ignoring warm-up and platform conventions.

@chapter Try it
@words text="Select a bar · list the window · calculate · compare lookbacks"
Your turn. Select a bar, identify every observation in its lookback window, and calculate the result by hand. Then explain how a shorter or longer window would change its responsiveness. And remember, exact values must be checked against the implementation you actually use.

@end text="Rebuild one value yourself"
You can move the selected bar and change the lookback, on Learn. That's learn dot get er done dot I O.
