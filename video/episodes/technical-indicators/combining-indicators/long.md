---
format: long
lesson: technical-indicators/combining-indicators
title: Combining indicators: three votes or one repeated?
thumb: One job per indicator
---

@chapter The question
@title text="Combining Indicators" sub="Technical Indicators" art=thumb
RSI says go. The stochastic says go. Rate of change says go. Three indicators agree, so that's strong confirmation, right? Maybe not. If all three are measuring the same thing, you've heard one opinion three times.

@words text="Agreement ≠ independent confirmation"
That's the core of this lesson. Indicators built from similar inputs and similar smoothing can move together. Their agreement may be repeated evidence, rather than independent confirmation.

@chapter Functional families
@art five-families
Start by grouping indicators by what they do. Trend, momentum, volatility, strength, and breakout indicators answer different questions. A moving average tells you about trend. RSI about momentum. ATR about volatility. ADX about strength. Donchian Channels about breakout boundaries.

@art same-input
And notice where they come from. RSI, the stochastic and rate of change are all momentum related transformations of price. Stacking them as three votes is the lesson's first common mistake, because they can repeat very similar information.

@chapter Check the overlap
@art correlation-lines
So check shared inputs, and check correlation. Identify which calculations are derived from the same close series, and compare whether their outputs move almost identically. If two lines rise and fall together, bar after bar, the second one isn't adding much.

@words text="Same data · similar transformation · same job"
Here's the lesson's rule. Multiple indicators don't create independent confirmation when they transform the same data in similar ways, and serve the same job. Both conditions matter. Different jobs, or genuinely different inputs, are what make a second indicator worth its place.

@words text="Correlation on comparable scales only" sub="one synthetic sample"
The lab calculates correlation only on outputs that share a comparable scale. The EMA is left out, because it's a price level series, and a price level correlates with anything that drifts with price. And the correlation describes one synthetic sample. It changes with the market path, the period and the transformation, so it isn't a universal property.

@chapter Purpose first
@art job-slots
Now build the set the other way round. Start from the decision problem. Do you need a trend state, a momentum trigger, a volatility filter, a breakout boundary, or some other function? Then choose the minimum set of indicators that covers those jobs.

@words text="Regime · trigger · volatility" sub="one tool for each"
For example, a set might need one tool to define the regime, one to define the trigger, and one to act as a volatility filter. Those are three different jobs, so they can be three different families. What they shouldn't be is three tools doing the trigger's job, with nothing measuring the regime or the volatility at all.

@list heading="Build an indicator set" items="Define the decision problem@Define|Select one primary tool per job@one primary tool|Check shared inputs and correlation@shared inputs|Remove unused information@Remove"
Define the decision problem. Select one primary tool per job, and don't add a second one unless it answers a different question or improves robustness. Check shared inputs and correlation. And remove unused information. If an indicator never changes a rule or a decision, take it out.

@art compact-set
The lab's guidance is two to four indicators, each with a distinct job. Every selected calculation should have one clear role. A line that never changes your entry, exit, filter or risk logic adds complexity without adding function.

@chapter Normalized displays
@art normalized-overlay
To compare shapes, the lab can show outputs on a normalized scale. That's useful for seeing whether two indicators move together. But normalization changes the scale. It must not replace the actual calculation, and confusing a normalized display with original units is the third common mistake.

@chapter Where people slip
@list heading="Common mistakes" items="Stacking RSI, stochastic and ROC as three votes@The first|Adding indicators without a decision role@The second|Normalized display mistaken for original units@The third"
So the three mistakes. The first is stacking RSI, the stochastic and ROC as three votes. The second is adding indicators without a decision role. And the third is confusing a normalized display with original units.

@chapter Try it
@words text="Purpose · compact set · families · correlations · each output's job"
Your turn. Choose a market purpose and select a compact set. Identify each indicator's family, and inspect the high correlations. Remove the redundant tools, and explain exactly how each remaining output changes a decision. You're done when every selected indicator has a unique job.

@end text="Build a compact indicator set"
You can select indicators and inspect their family coverage and similarity, on Learn. That's learn dot get er done dot I O.
