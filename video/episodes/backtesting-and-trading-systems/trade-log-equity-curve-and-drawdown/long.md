---
format: long
lesson: backtesting-and-trading-systems/trade-log-equity-curve-and-drawdown
title: Drawdown and the equity curve: same trades, very different ride
thumb: Same trades, different pain
---

@chapter The problem
@title text="Trade Log, Equity Curve, and Drawdown" sub="Backtesting and Trading Systems" art=thumb
Two backtests end with exactly the same return. Are they equally risky? Not necessarily. One might have climbed smoothly. The other might have fallen hard in the middle and spent months climbing back.

@words text="Same average trade · very different stress"
The lesson puts it like this. The equity curve is the ordered result of every signal, fill, cost, position and market movement. And the same average trade can produce very different account stress when losses cluster together.

@art same-trades-two-orders
Take one set of trade outcomes and shuffle the order. Spread the losers out, and the curve wobbles gently upward. Bunch them together, and the account takes a deep dip. Same trades, same ending. Different experience.

@art losing-cluster
A cluster of losses is what does the damage. Four losers in a row, each taken on a shrinking account, dig a hole that one losing trade between winners never would. And the person running the system has to live through that hole, not just the average.

@chapter Three records
@list heading="What to understand" items="Trade log@trade log|Equity curve@equity curve|Drawdown@drawdown"
There are three things to build. A trade log that stores the signal, order, fill, quantity, cost, exit, profit and loss, and reason codes. An equity curve that marks open positions and cash consistently through chronological time. And drawdown: the decline from the previous equity peak, and the time it takes to recover.

@art trade-log-rows
Reason codes are easy to skip, and you shouldn't. They explain why each entry and exit happened. They don't move a price or remove a cost, but they make the result traceable and debuggable. When a trade looks wrong, the reason code tells you which rule fired.

@art open-marks
And the equity curve has to include open positions, marked to market. If you only update equity when trades close, a position that sinks for weeks before closing never shows up as a dip at all.

@chapter Measuring drawdown
@art peak-trough-recovery
Maximum drawdown is the largest peak to trough equity decline, measured relative to the peak that came before it. It's a property of the path the account took, not of any single trade. And it has two sides: how deep, and how long until recovery.

@math heading="Peak $51,974 · trough $49,427" items="1 − 49,427 ÷ 51,974 = 4.9%@one minus;;51,974 ÷ 49,427 − 1 = 5.2%@to recover"
Here's the lesson's example. Equity peaks at fifty one thousand, nine hundred and seventy four dollars, and falls to forty nine thousand, four hundred and twenty seven. One minus the trough over the peak is a drawdown of four point nine percent. But to recover, you divide the peak by the trough and subtract one. That's five point two percent.

@words text="Recovery is always the bigger number"
Why the difference? The drawdown is measured against the peak, and the recovery is measured from the trough, which is smaller. So the climb back always needs a larger percentage than the fall. These are the figures for the lab's clustered sequence at one percent risk.

@chapter Make it auditable
@list heading="Make the result auditable" items="Record complete events and reason codes@Record|Reconcile cash, positions, fees, equity@Reconcile|Inspect depth, duration, clusters, regimes@Inspect"
Every equity change should trace back to source events. Record: store complete events and reason codes. Reconcile: rebuild cash, positions, fees and equity from the log. And inspect: find the drawdown depth, the duration, the losing clusters and any regime dependence.

@art reconcile
Reconciling is the real test of the log. If you can't rebuild the equity curve from it, something is missing. Store enough fields to reproduce every trade, and calculate drawdown from the full portfolio equity curve, not from trades one at a time.

@chapter Where people slip
@list heading="Common mistakes" items="Keeping only entry and exit prices@The first|Ignoring open-position marks@The second|Judging risk by final return alone@And the third"
The first mistake is keeping only entry and exit prices. The second is ignoring mark to market changes on open positions. And the third is judging risk only by the final return, when two tests with the same ending can have very different drawdowns and recovery times.

@chapter Try it
@words text="Reorder the same outcomes"
In the lesson's lab, which uses deterministic synthetic educational data, change the order of the same trade outcomes. Watch the equity, the drawdown, the losing clusters and the recovery change, while the final number stays put. Review both depth and duration.

@end text="Shuffle the trades, watch the drawdown"
You can reorder the same trades and watch the drawdown change, on Learn. That's learn dot get er done dot I O.
