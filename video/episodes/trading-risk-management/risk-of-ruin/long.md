---
format: long
lesson: trading-risk-management/risk-of-ruin
title: Risk of ruin: how big losses turn ordinary streaks into the end
thumb: How many losses end it?
---

@chapter The question
@title text="Risk of Ruin" sub="Trading Risk Management" art=thumb
Your strategy has an edge. Over many trades, it makes money. So you can't blow up, right? Wrong. Risk of ruin is the question of whether a losing sequence can take you out before the edge ever gets to work.

@words text="Positive expectancy doesn't eliminate severe paths"
Positive expectancy doesn't eliminate severe paths. Risk of ruin asks whether a losing sequence can reduce the account below the level required to continue. And large risk per trade makes ordinary variance more likely to cross that failure threshold.

@chapter The threshold
@art threshold
The ruin threshold is the equity level at which the strategy can no longer be traded as intended. It's usually not zero. Defining ruin only as a zero balance is one of the lesson's common mistakes.

@words text="Define ruin practically" sub="strategy size · margin · personal tolerance"
So define ruin practically. Use the minimum equity needed for your strategy's size, its margin, or your personal tolerance. That's the line you can't afford to cross.

@chapter Path dependency
@art many-paths
Outcome order affects whether the account reaches the threshold. That's path dependency. Does positive expectancy guarantee zero ruin risk? No. Expectancy is an average over many sequences. Your account lives through just one of them. And some sequences with a positive average still cross the threshold first.

@words text="Not about the instrument"
And this isn't special to any one product. The instrument doesn't enter into it. Ruin is a property of risk size, edge, and threshold.

@chapter What moves it most
@art steep-vs-shallow
What generally increases risk of ruin most directly? Higher risk per trade. Larger losses per outcome move equity toward the threshold faster. Lower risk makes each loss a smaller share of equity, so the same streak travels less of the distance.

@chapter Count the losses
@words text="5% per trade · ruin at −50%"
Here's the lesson's example. Risk five percent of current equity per trade, and define ruin as a fifty percent drawdown. How many consecutive full losses reach it?

@math heading="Risk 5% of current equity · ruin = 50% drawdown" items="0.95ⁿ ≤ 0.50@point nine five;;n ≥ ln 0.5 ÷ ln 0.95 = 13.5@thirteen point five;;n = 14: 0.95¹⁴ = 0.488@fourteen losses"
Each loss leaves point nine five of the balance. You need point nine five to the n to fall to point five or less. That happens when n is at least thirteen point five, so fourteen losses.

@math heading="Not these" items="✗  10: 0.95¹⁰ = 0.599@ten;;✗  20: by loss 14 it's already 48.8%@twenty"
Ten is the fixed dollar count, ten times five percent. At a fixed percentage each loss is smaller than the last. After ten, the account is still at about sixty percent. And twenty overshoots. By the fourteenth loss it's already at forty eight point eight percent.

@math heading="At 1% instead" items="0.99⁶⁹ = 0.50@sixty nine losses"
Now drop the risk to one percent. The same threshold takes sixty nine losses. That's the lesson's point. The risk percentage sets how ordinary a streak has to be to end the account.

@chapter Simulation
@art monte-carlo
How do people estimate this? Often with a Monte Carlo simulation, which reshuffles an assumed distribution of outcomes many times.

@art shuffle
Each reshuffle is one possible order of the same kinds of trades, and each order traces a different path. But what is a Monte Carlo result? A scenario estimate, based on assumptions. Not a guarantee, and not an exact future probability.

@words text="The output inherits every assumption"
It isn't a forecast, because a forecast would need the modelled probabilities to be the true ones. And it isn't a live market signal. The simulation has no market in it. The output depends entirely on the modelled probabilities and payoff assumptions.

@chapter Where people slip
@list heading="Common mistakes" items="Treating simulation output as certainty@The first|Gross backtest results without costs@The second|Defining ruin only as zero@the third"
Three mistakes. The first is treating simulation output as certainty. The second is using gross backtest results without costs. And the third is defining ruin only as a zero balance.

@list heading="Practical rules" items="Use conservative expectancy@conservative|Include losses bigger than the stop@rare losses|Risk low enough to survive bad sequences@low enough"
So use conservative expectancy assumptions. Include rare losses larger than the planned stop. And set risk low enough that bad sequences remain survivable.

@art big-loss
That middle rule matters because a model where every loss is exactly one stop is too kind. Gaps and fast markets produce occasional larger losses, and a realistic model includes them.

@chapter Try it
@list heading="Lab steps" items="Define ruin practically@define ruin|Model realistic outcomes@model realistic outcomes|Stress the assumptions@stress the assumptions"
The lab's steps: define ruin practically. Model realistic outcomes, using net win rate, payoff, costs, gaps, and occasional larger losses. Then stress the assumptions. Increase loss clustering and reduce expectancy to test robustness.

@words text="Synthetic educational data" sub="no live market connection"
The lab uses simplified synthetic examples, with no live market connection. For practice, try two percent risk with the same fifty percent threshold. Set up the same inequality, and estimate how many losses it takes.

@end text="Survive the bad path"
You can stress your own assumptions in the risk of ruin lab, on Learn. That's learn dot get er done dot I O.
