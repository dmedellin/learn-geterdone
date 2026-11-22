---
format: long
lesson: backtesting-and-trading-systems/overfitting-sensitivity-monte-carlo-and-stress-testing
title: Is your backtest real or noise? Try to break it
thumb: Peaks lie, plateaus last
---

@chapter The problem
@title text="Overfitting, Sensitivity, Monte Carlo, and Stress Testing" sub="Backtesting and Trading Systems" art=thumb
You've found a setting that works beautifully. A lookback of exactly this many bars, a threshold of exactly this much. Change either a little, and the result falls apart. Is that a discovery, or did you just find the luckiest cell in the table?

@words text="Survive reasonable changes"
The lesson's test is this. A durable rule should survive reasonable changes to parameters, sequence, costs and market conditions. If only one exact setting works, the result may be noise. Broadly similar results across neighbouring settings are stronger evidence.

@chapter Three ideas
@list heading="What to understand" items="Overfitting@Overfitting|Sensitivity@Sensitivity|Stress and resampling@stress and resampling"
Three ideas. Overfitting: the system captures historical noise, or the researcher's own choices, instead of repeatable behaviour. Sensitivity: small parameter changes shouldn't completely reverse the result without a market reason. And stress and resampling: test unfavourable costs, order sequence, missing winners and regime changes.

@chapter Peaks and plateaus
@art narrow-peak
Picture the results as a surface across the parameter settings. A single narrow peak is usually more suspicious than a broad, stable region. A sharp, isolated optimum says the result depends on one exact setting, and that's the signature of fitted noise, not of precision.

@art broad-plateau
A real market behaviour would show up across nearby settings too. So you'd expect a plateau: a wide area where results are broadly similar. A single best cell only shows that one cell was best on this history.

@math heading="Selected lookback +8.0% · neighbours average +1.5%" items="1.5 ÷ 8.0 = 0.19@one point five divided by;;19% of the result survives a small change@nineteen percent;;trending sample's plateau keeps 72%@seventy two"
From the lesson: a selected lookback returns eight percent. The average of its neighbouring lookbacks is one point five percent. One point five divided by eight is zero point one nine. So only nineteen percent survives a small change in the parameter. The lab's trending sample's plateau keeps seventy two percent.

@words text="Positive isn't the same as stable"
Notice the neighbours are still positive. That doesn't rescue it. A plateau keeps most of the selected return, and this one keeps under a fifth.

@chapter Reorder the trades
@art monte-carlo-paths
Monte Carlo trade reordering asks a different question. Take the same trades and shuffle their order many times. The distribution of outcomes is the same, but each shuffle gives a different path, and a different drawdown.

@words text="One history is one path, not the expected future"
It evaluates sequence dependent outcomes like drawdown. It can't produce prices the sample never had, or predict the future exactly. But it shows that the drawdown you saw was one draw from many possible ones. Calling one historical sequence the expected future path is a named mistake.

@chapter Stress the costs
@art cost-stress
Then stress it. Increase costs to see whether the edge survives worse execution. Gross return doesn't change with costs. The point is what the net result does when live spreads and slippage exceed the average you assumed. Stress delays, and remove favourable events, too.

@art perturb-dial
Sensitivity testing is just turning the dials a little. Move the lookback a step or two. Delay the entry by a bar. Nudge the fill prices. A rule built on something real should bend, not break.

@list heading="Try to break the system" items="Perturb: parameters, delays, prices, costs@Perturb|Resample: trade order and history blocks@Resample|Decide: keep, simplify, constrain or reject@Decide"
Robustness testing searches for failure conditions, not prettier results. Perturb: change parameters, delays, prices and costs within reasonable ranges. Resample: change the trade sequence and the selected historical blocks. Then decide: keep, simplify, constrain or reject the system, based on how stable it is.

@art break-it
Notice the attitude. You're not trying to make the system look better. You're trying to break it, and a system that survives your best attempts has earned more trust than one that was only ever shown flattering tests.

@chapter Where people slip
@list heading="Common mistakes" items="Choosing the single best parameter cell@The first|Many trials, no accounting for selection@The second|One historical sequence as the expected future@And the third"
The first mistake is choosing the single best parameter cell. The second is running many trials without accounting for that selection: try enough variations and one will look good by chance. And the third is calling one historical sequence the expected future path. Prefer simpler rules, and record every experiment, not only the one you selected.

@chapter Try it
@words text="Surface · resample · stress"
In the lesson's lab, which uses deterministic synthetic educational data, inspect the parameter surface, resample the trade order, and stress the execution costs. Compare the peak performance with the stable performance, and ask which one you'd actually trust.

@end text="Find the plateau, not the peak"
You can inspect the surface and resample the trades yourself, on Learn. That's learn dot get er done dot I O.
