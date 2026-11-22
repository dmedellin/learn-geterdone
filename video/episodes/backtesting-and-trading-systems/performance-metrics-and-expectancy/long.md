---
format: long
lesson: backtesting-and-trading-systems/performance-metrics-and-expectancy
title: Expectancy: why a 42% win rate can beat a 90% one
thumb: Win rate isn't the edge
---

@chapter The question
@title text="Performance Metrics and Expectancy" sub="Backtesting and Trading Systems" art=thumb
Which is better: a system that wins ninety percent of the time, or one that wins forty two percent? Most people pick the first. But the win rate alone decides nothing.

@words text="A distribution of outcomes, not one percentage"
The lesson's framing is this. A trading system is a distribution of outcomes, not a single winning percentage. How often you win, how much you win, how much you lose, and what each trade costs, all work together.

@art wins-vs-losses
A ninety percent win rate with wins a tenth the size of the losses is still negative. And in persistent trends, winners can run while stopped losses stay small. So a lower win rate can still have positive expectancy, when the average win is bigger.

@chapter Three ideas
@list heading="What to understand" items="Expectancy@Expectancy|Payoff and frequency@Payoff and frequency|Uncertainty@uncertainty"
Three ideas. Expectancy: the average result per trade after wins, losses and costs. Payoff and frequency: win rate, average size and how many opportunities there are, all together. And uncertainty: small samples can show unstable metrics that change with a few trades.

@chapter Expectancy in R
@words text="R = the planned loss on one trade" sub="win 2.1R · lose 1R · cost 0.08R"
Let's work the lesson's example, measured in R, where one R is the planned loss on a trade. Forty two percent of trades win two point one R. Fifty eight percent lose one R. And every trade costs zero point zero eight R.

@math heading="Expectancy per trade" items="0.42 × 2.1 = 0.882@zero point four two;;0.58 × 1.0 = 0.580@zero point five eight;;0.882 − 0.580 − 0.08 = 0.222R@minus the cost"
Weight each outcome by how often it happens. Zero point four two times two point one is zero point eight eight two. Zero point five eight times one is zero point five eight. Zero point eight eight two, minus zero point five eight, minus the cost of zero point zero eight, is zero point two two two R per trade.

@art distribution
Forget the cost, and you'd say about zero point three R. The cost is paid on every trade, win or lose, so it comes off the whole average. And subtracting the win rate from the loss rate is wrong too, because expectancy weights each outcome by its size, not just its frequency.

@math heading="Breakeven win rate" items="(1 + 0.08) ÷ (2.1 + 1) = 34.8%@thirty four point eight"
The lesson also gives the breakeven win rate. One plus the cost, divided by the win size plus the loss size. That's one point zero eight over three point one, which is thirty four point eight percent. Win less often than that, and this payoff loses money.

@art breakeven-line
That's a useful way to read any system. The payoff sets a line, and the win rate has to clear it. Bigger wins relative to losses pull the line down. Higher costs push it up.

@chapter Profit factor and the metric set
@art profit-factor
Profit factor is another way to compare. It's gross profit divided by the size of the gross loss. Total winning dollars against total losing dollars. Not divided by trade count, and not by starting capital.

@art metric-set
So which one number should you report? None of them alone. A high expectancy with three trades behind it, or a smooth curve with a hidden cost assumption, can each mislead.

@list heading="Use a metric set" items="Edge: expectancy, gross vs net payoff@Measure edge|Path: volatility, drawdown, losing clusters@measure path|Evidence: trade count, regimes, stability@measure evidence"
No single number describes return, risk and reliability. Measure edge: expectancy, and gross versus net payoff. Measure path: volatility, drawdown and losing clusters. And measure evidence: the trade count, the regimes covered, and whether the metrics are stable.

@art small-sample
Trade count matters because small samples produce uncertain estimates. Metrics based on a few observations can move sharply with each new trade. More trades narrow the uncertainty around the average. They don't move the average up.

@chapter Where people slip
@list heading="Common mistakes" items="Optimising only win rate@The first|Comparing different exposure by total return@The second|Treating a small-sample estimate as stable@And the third"
The first mistake is optimising only the win rate. The second is comparing systems with different exposure using total return alone. And the third is treating a small sample estimate as stable. Show the trade count and tested dates beside every result, and use net results after costs.

@chapter Try it
@words text="Win rate · payoff · costs · sample size"
In the lesson's lab, which uses deterministic synthetic educational data, adjust the win rate, payoff, costs and sample size. Watch the expectancy, the profit factor and the uncertainty move together.

@end text="Find your breakeven win rate"
You can change the payoff and find the breakeven win rate yourself, on Learn. That's learn dot get er done dot I O.
