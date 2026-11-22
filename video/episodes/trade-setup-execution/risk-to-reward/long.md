---
format: long
lesson: trade-setup-execution/risk-to-reward
title: Risk-to-reward, break-even win rate and expectancy
thumb: The same 2R plan can lose
---

@chapter The question
@title text="Risk-to-Reward" sub="Trade Setup & Execution" art=thumb
You've probably heard that you should only take trades worth two R or more. This lesson shows a two R plan that loses money. The ratio didn't change. Something else did, and by the end you'll be able to say exactly what.

@words text="Ratio ≠ edge" sub="keep the maths separate from target validity"
The lesson measures price risk, planned reward, the break even win rate, and expectancy. And it keeps those mathematical ratios separate from the question of whether the target is structurally valid at all.

@words text="Process and measurement" sub="no live data, no recommendations, no signals"
As with the rest of this course, it teaches process and measurement. It doesn't give live market data, personal recommendations, or trade signals.

@chapter R as a unit
@art r-unit
One R is the initial planned loss, from entry to stop. Once every trade is measured in R, outcomes can be compared across trades with different prices and sizes. A target twice as far as the stop is a two R target.

@chapter The break-even rate
@art breakeven-balance
The average win compared with the average loss decides the win rate you need just to break even, before costs. Bigger wins relative to losses means you can afford to be right less often.

@math heading="Break-even win rate" items="break-even = avg loss ÷ (avg win + avg loss)@average loss divided by;;1 ÷ (2 + 1) = 33.3%@one over two plus one;;0.50 ÷ (2.00 + 0.50) = 20.0%@zero point five over"
The formula is the average loss divided by the average win plus the average loss. With a two R win and a one R loss, that's one over two plus one, thirty three point three percent. Now set the average loss to half an R. It's zero point five over two plus zero point five: twenty percent.

@words text="Losing less than 1R → fewer wins needed"
So a system that loses less than one R on average needs fewer wins. The old shorthand, one over one plus the ratio, can't show that, because it assumes every loss is exactly one R.

@chapter Expectancy
@art expectancy-sum
Expectancy combines everything: the win rate, the average win, the average loss, and the costs. It estimates the average result per trade, in R.

@math heading="Win rate 30%, 2R plan, costs 0.05R" items="E = W × avg win − (1 − W) × avg loss − costs@win rate times;;= 0.30 × 2.00 − 0.70 × 1.00 − 0.05@zero point three times two;;= 0.60 − 0.70 − 0.05@zero point six minus;;= −0.15R@minus zero point one five"
Take the lesson's example. Win rate times average win, minus the loss rate times average loss, minus costs. With a thirty percent win rate, that's zero point three times two, minus zero point seven times one, minus zero point zero five. Zero point six minus zero point seven minus zero point zero five. Minus zero point one five R.

@words text="Same 2R plan, negative expectancy"
That's the two R plan that loses money. The ratio didn't change. The estimate behind it did. And that estimate is the part that has to come from backtesting.

@chapter Costs and estimates
@art costs-slice
Costs matter more than they look. Small theoretical edges can disappear after spread, commissions, and slippage. That's why the calculator takes costs per trade, in R.

@art estimate-outline
And a positive result is only as reliable as the win rate and average outcome estimates behind it. Those should come from a large enough, relevant backtest, not from a guess.

@chapter Where people slip
@list heading="Common mistakes" items="2R as a universal minimum@The first|Planned R as the realized average win@The second|Ignoring costs@The third|Guessed win rates as facts@And the fourth"
The first mistake is treating two R as a universal minimum. Different systems can work with different mixes of win rate and payoff. The second is assuming planned R equals the realized average win. Partial exits, slippage, gaps, and management all change it. The third is ignoring costs. And the fourth is treating guessed win rates as facts.

@art two-systems
That first one is worth picturing. One system wins often, with small wins. Another wins rarely, with large ones. Both can be viable. The ratio alone can't tell you which is better. Only the win rate, the averages, and the costs together can.

@chapter Try it
@words text="Risk · reward · R · break-even · expectancy"
Here's the lesson's standard. For any entry, stop, target and cost, compute all five figures by hand: risk, reward, the R multiple, the break even win rate, and expectancy. Then say why a positive result is only as good as the win rate estimate behind it.

@end text="Run the trade math"
You can change every input and check your hand calculations against the calculator, on Learn. That's learn dot get er done dot I O.
