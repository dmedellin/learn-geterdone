---
format: long
lesson: backtesting-and-trading-systems/benchmarking-and-risk-adjusted-performance
title: Did your strategy add value, or just ride the market?
thumb: Beat the market, or ride it?
---

@chapter The problem
@title text="Benchmarking and Risk-Adjusted Performance" sub="Backtesting and Trading Systems" art=thumb
Your strategy made money in a strong year. Great. But in a bull market, buyers keep accepting higher prices across the board. So the question is whether your system added anything, or simply came along for the ride.

@words text="Added value, or participated with more risk?"
The lesson's warning is that a strategy rising in a bull market may only be carrying the same market exposure as its benchmark. The test has to show whether the system added value, or simply participated with more risk.

@art cash-vs-benchmark
That's why beating cash proves nothing on its own. In a rising market, almost any market exposure beats cash. The relevant benchmark may have risen more, with similar or lower risk. Using cash as the only benchmark for an equity strategy is one of the lesson's named mistakes.

@chapter Three ideas
@list heading="What to understand" items="Benchmark fit@Benchmark fit|Risk adjustment@Risk adjustment|Active return@active return"
Three ideas. Benchmark fit: use an investable reference that matches the strategy's universe and opportunity set. Risk adjustment: compare return with volatility, drawdown, downside risk and exposure. And active return: the difference between the strategy and the benchmark over the same dates.

@art same-end-different-risk
Risk adjustment matters because two strategies can end at the same value while carrying very different volatility and drawdown to get there. The ending alone hides the risk. You judge return together with the risk taken.

@chapter Compare like with like
@list heading="Compare like with like" items="Select the available alternative@Select|Normalize dates, capital, frequency@Normalize|Decompose active return and sensitivity@Decompose"
Dates, currency, reinvestment and costs all have to line up. Select a benchmark that represents the alternative the capital actually had. Normalize, using the same dates, capital base and return frequency. Then decompose: review active return, market sensitivity, risk and drawdown.

@art benchmark-fixed-first
And pick the benchmark before testing. Choosing it after you've seen the result is choosing a comparison to flatter, or damn, the strategy. A random instrument isn't a benchmark either. It has to represent a real alternative.

@chapter Exposure versus independent return
@art sensitivity-lever
Here's the key idea. Market sensitivity measures how much of the market's move a strategy carries. A sensitivity of one point five means it moves about one and a half times the benchmark. In a rising market, that alone earns a lot, and none of it is edge.

@art rising-tide
Think of a rising tide. Every boat goes up with it. A strategy with high sensitivity is a boat that rises more than the tide, which looks impressive until the tide turns. What you want to know is whether the boat moved on its own.

@math heading="Sensitivity 1.5 · strategy +1.9% · benchmark +6.7%" items="exposure = 1.5 × 6.7% = 10.0%@one point five times;;independent = 1.9% − 10.0% = −8.1%@minus eight point one"
The lesson's example. A strategy with a sensitivity of one point five returns one point nine percent, in a year the benchmark returns six point seven. Its exposure alone should have earned one point five times six point seven, which is ten percent. So its independent return is one point nine minus ten, or minus eight point one percent.

@art decompose
Strategy minus benchmark gives minus four point eight, but that treats the strategy as if it held the market at one. And calling the whole one point nine its own ignores that, with that much exposure, most of what it earned was the market's. The lab prints this decomposition beside its ratio.

@chapter Where people slip
@list heading="Common mistakes" items="Cash as the only equity benchmark@The first|Calling leveraged beta independent edge@The second|Switching benchmarks after the results@And the third"
The first mistake is using cash as the only benchmark for an equity strategy. The second is calling leveraged market exposure edge. And the third is switching benchmarks after seeing performance. Report absolute and relative results over the same dates, with the same reinvestment and costs, so a reader can see both what the strategy earned and what it added.

@chapter Try it
@words text="Regime · sensitivity · independent return · volatility"
In the lesson's lab, which uses deterministic synthetic educational data, change the regime, the market sensitivity, the independent return and the volatility. Then see how a strategy can look strong in absolute terms while adding nothing over its benchmark.

@end text="Split exposure from edge"
You can separate market exposure from independent return yourself, on Learn. That's learn dot get er done dot I O.
