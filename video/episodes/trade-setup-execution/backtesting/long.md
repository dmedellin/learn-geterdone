---
format: long
lesson: trade-setup-execution/backtesting
title: Backtesting honestly: freeze the rules, then test them
thumb: Test the rules, not the story
---

@chapter The question
@title text="Backtesting" sub="Trade Setup & Execution" art=thumb
You've written a setup and a set of management rules. Do they actually work? A backtest is meant to answer that. But it's easy to build one that tells you a perfect story about the past and nothing about the future.

@words text="Evaluate a rule set, not explain the past"
This lesson uses historical samples to evaluate a predefined rule set, not to construct a perfect explanation of what already happened. Explicit rules, chronological samples, realistic costs, and a comparison between in sample and out of sample results.

@words text="Synthetic data" sub="process and measurement · no signals"
One important note. The lab generates synthetic trade samples. Everything you'll see there is generated, to teach the method. The lesson teaches process and measurement, and doesn't give live data, personal recommendations, or trade signals.

@chapter Three ideas
@art frozen-rules
First, reproducible rules. Another reviewer should be able to identify the same entries, stops, targets, and outcomes from your written rules. If they can't, the test can't be checked.

@art chronological-replay
Second, bias control. Replaying chronologically, using complete samples, and validating on unseen data all reduce look ahead bias and selection bias.

@art drawdown-dip
And third, the statistical distribution. Evaluate expectancy, drawdown, streaks, and regime sensitivity, not only net profit. A rule set with a fine total can still have a drawdown or a losing streak you couldn't live with.

@chapter The process
@list heading="Backtesting process" items="Freeze the rules@Freeze the rules|Replay chronologically@Replay chronologically|Record realistic outcomes@Record realistic outcomes|Validate outside the development sample@Validate outside"
Freeze the rules: document setup, entry, invalidation, target, management, and exclusions before testing. Replay chronologically, using only information available at each decision point, and include every valid setup. Record realistic outcomes, including costs, gaps, partial fills, missed entries, and management. And validate outside the development sample.

@art in-out-split
That last step is what the in sample portion setting is for. You develop on one part of the sample, then test on a part the rules have never seen, whether that's another period, another instrument, or another regime. That gives you two expectancies, one in sample and one out of sample. If the second is much worse, the rules may have been fitted to noise.

@chapter Why results drift
@art regime-bands
The lab adds a realistic wrinkle. For every trade, its generator draws a regime: trend, range, or volatile. Then it nudges the win probability by setup and regime.

@math heading="The lab's regime nudge" items="nudge ≤ ±0.08@at most;;breakout in a range: −0.08@a breakout in a range;;pullback in a trend: +0.07@a pullback in a trend"
The nudge is at most plus or minus zero point zero eight. A breakout in a range loses zero point zero eight. A pullback in a trend gains zero point zero seven.

@words text="The base rate is an average over conditions"
That's what a real sample does to a rule. The base rate is an average over conditions the rule doesn't get to choose. So the realized win rate drifts away from the base, and the numbers you read are what came out, not what went in.

@chapter Where people slip
@list heading="Common mistakes" items="Selecting only obvious winners@The first|Using future data@The second|Changing many parameters on one sample@The third|Evaluating only net profit@And the fourth"
The first mistake is selecting only the obvious winning examples, which inflates results. The second is using future data to confirm past entries. Look ahead bias can make impossible execution look successful. The third is changing many parameters on one sample. The best historical combination may just be noise. And the fourth is evaluating only net profit.

@art equity-curve
A smooth equity curve on its own proves little. Drawdown, loss streaks, expectancy, costs, and regime dependence all affect whether a system is practical.

@chapter Try it
@list heading="Freeze the assumptions" items="Setup and number of trades@the setup|Base win rate@base win rate|Average win and loss in R@average win|Costs and in-sample portion@costs"
In the lab, you freeze the assumptions first: the setup, the number of trades, the base win rate, the average win and loss in R, the costs, and the in sample portion. Then you run the sample.

@words text="Change exactly one assumption" sub="run again · say what moved and why"
Here's the lesson's standard. Read the equity, the drawdown, the streak, and both expectancies from a run, and say which one would make you reject the rules. Then change exactly one assumption, run it again, and say what moved and why. That's the whole method, on synthetic data.

@end text="Run a synthetic backtest"
You can freeze the assumptions, run a synthetic sample, and compare in sample with out of sample, on Learn. That's learn dot get er done dot I O.
