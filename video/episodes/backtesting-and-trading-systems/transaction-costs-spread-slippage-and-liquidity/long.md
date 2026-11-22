---
format: long
lesson: backtesting-and-trading-systems/transaction-costs-spread-slippage-and-liquidity
title: How trading costs turn a winning backtest into a losing one
thumb: Gross edge, net loss
---

@chapter The problem
@title text="Transaction Costs, Spread, Slippage, and Liquidity" sub="Backtesting and Trading Systems" art=thumb
A strategy that trades a lot, for a small edge each time, can look excellent before costs. Then you charge for every fill, and it loses money. Not because the signals failed, but because executing them cost more than they earned.

@words text="Gross edge must survive the cost of execution"
That's the lesson's point. The gross edge must be large enough to survive the cost of executing the strategy. A high turnover strategy can lose to spread and slippage even before its signals fail.

@art range-churn
It's worst in a range. Buyers and sellers trade back and forth without sustained price progress. A strategy that keeps entering and exiting there pays every time, and the price never moves far enough to cover it.

@chapter Three kinds of cost
@list heading="What to understand" items="Explicit cost@explicit costs|Spread and slippage@spread and slippage|Market impact@market impact"
There are three kinds. First, explicit costs: commissions, exchange fees and regulatory charges, deducted directly. Second, spread and slippage: the price you can actually execute at differs from the chart midpoint or the signal price. And third, market impact: larger orders can consume the available liquidity and move the average fill.

@art spread-gap
Spread is the gap between the best bid and the best ask. Buy, and you pay the ask. Sell, and you get the bid. Filling every trade at the midpoint is one of the lesson's named mistakes, because nobody gets the midpoint on both sides.

@art impact-ladder
Impact grows with size. Capacity is constrained by the volume available near the price you want. Once your order is big relative to that, it eats into worse prices, and the average fill gets worse.

@chapter Charge costs at the event
@list heading="Charge costs at the event" items="Estimate: instrument and regime-specific@Estimate|Apply: entry, exit, partial fills, rebalances@Apply|Stress: wider spreads, less liquidity@Stress"
Don't subtract an arbitrary amount at the end. Charge costs at each event. Estimate: define instrument and regime specific cost assumptions. Apply: charge both entry and exit, including partial fills and rebalances. And stress: retest with wider spreads, higher volatility and lower liquidity.

@art round-trip
A round trip normally crosses costs on both entry and exit. And costs are charged by the fill, not by the outcome. A losing trade paid its spread and slippage too, so applying costs only to losses, or only to wins, gives a wrong answer.

@chapter Add it up
@math heading="Gross edge 14 bps per trade" items="commission 1 + spread 8@commission one;;slippage 2 × 5 = 10@twice;;impact 2.2@two point two;;cost = 21.2 bps per round trip@twenty one point two;;14 − 21.2 = −7.2 bps@minus seven point two"
Here's the lesson's worked example, in basis points. Commission one, spread eight. Slippage is five per side, so twice that is ten. Market impact is two point two. That's twenty one point two basis points per round trip. Against a gross edge of fourteen, the net edge is minus seven point two.

@art cost-stack
Look at the sizes. The spread alone is more than half the edge. Add slippage on both sides, and the costs have already passed the fourteen points the signal earns, before impact is even counted.

@words text="Slippage is paid on each side"
The easy slip is counting slippage once. Do that and you get minus two point two, which still loses, but less than half as much. The lab's range setting shows what ninety trades of the real figure do to an account.

@art gross-vs-net
That's why the lesson asks you to report gross and net performance separately. The distance between those two curves is the cost of running the strategy.

@chapter Where people slip
@list heading="Common mistakes" items="Midpoint prices for every fill@The first|Costs applied only to losses@The second|Zero slippage in volatile or illiquid markets@And the third"
The first mistake is using midpoint prices for every fill. The second is applying costs only to losses. And the third is assuming zero slippage in volatile or illiquid markets. Use conservative costs for stressed conditions, and measure turnover and capacity at the order size you actually tested.

@chapter Try it
@words text="Turnover · spread · slippage · size"
In the lesson's lab, which uses deterministic synthetic educational data, increase the turnover, the spread, the slippage and the order size, and compare the gross and net equity curves. Try the range setting first, where turnover is high and progress is small, and see how quickly a positive gross curve turns into a falling net one.

@end text="Watch gross become net"
You can push costs up and watch gross turn into net, on Learn. That's learn dot get er done dot I O.
