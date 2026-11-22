---
format: long
lesson: backtesting-and-trading-systems/trade-execution-simulation
title: Simulating fills honestly: limits, stops, gaps and the bar that hides the order
thumb: A signal is not a fill
---

@chapter The problem
@title text="Trade Execution Simulation" sub="Backtesting and Trading Systems" art=thumb
Your rule says buy. In a backtest, it's easy to write down the price you wanted and move on. But a signal isn't a trade. The lesson puts it plainly: a signal is not a trade until the order model produces a valid fill.

@art market-vs-limit
Different orders make different promises. Market orders prioritise execution: you get filled, but not necessarily at the price you saw. Limit orders prioritise price: you won't pay more than your limit, but you might never be filled at all. And gaps can move a fill beyond the level you planned.

@chapter Three things to model
@list heading="What to understand" items="Order eligibility@order eligibility|Fill condition@the fill condition|Intrabar ambiguity@intrabar ambiguity"
The lesson names three things to get right. First, order eligibility: an order becomes active only after its submission event. Second, the fill condition: price touching a level doesn't always prove the full order could execute there. And third, intrabar ambiguity, which needs its own chapter.

@art touched-limit
Think about that second one. A buy limit sits below the market and price dips to touch it. Did your order fill? Maybe. Other orders may have been ahead of yours in the queue, and the touch may have been one small trade. Filling every touched limit completely is one of the lesson's named mistakes.

@chapter The bar that hides the order
@art stop-and-target
Now say you have a stop below and a target above, and one bar's range covers both. Which was hit first? Daily open, high, low and close can't say. They only tell you both prices were inside the range.

@words text="Finer data, or a conservative rule"
When stop and target are both inside one bar, the sequence is unknown without finer data. So you either get finer data, or you use a conservative ambiguity rule, and you write down which one you chose.

@chapter Gaps and stops
@art gap-through-stop
Stops have their own trap. A stop is a trigger, not a price guarantee. When the market gaps past it, the order triggers and fills at the next available market price, which can be well beyond the stop.

@math heading="Long, stop at 100.00" items="next bar opens 98.50 · high 99.00@ninety eight point five;;exit = 98.50, the open@the open;;100.00 − 98.50 = 1.50 beyond the stop@one point five"
Here's the lesson's example. A long position has its stop at one hundred. The next bar opens at ninety eight point five and never trades above ninety nine. The simulated exit is ninety eight point five, the open. That's a loss one point five beyond the stop.

@words text="Not 100.00 · not 99.00"
Booking the exit at one hundred credits a fill the market never offered on that bar. And ninety nine, the bar's high, came later. The order was live at the open, so the open is the first price available. The lab books stops and targets the same way whenever a bar opens through them.

@chapter An order lifecycle
@list heading="Separate signal from execution" items="Submit: time, side, type, quantity, constraints@Submit|Match: prices, spread, liquidity, queue@Match|Resolve: fill, partial, cancel, expire, stop, target@Resolve"
So each simulated order needs a lifecycle. Submit: record the time, side, type, quantity and constraints. Match: apply eligible prices, spread, liquidity and queue assumptions. Resolve: the order fills, partially fills, cancels, expires, or hits its stop or target.

@art order-lifecycle
Keeping these steps separate is what makes the simulation checkable. You can look at any trade and see when the order existed, what it was allowed to match against, and how it ended. It also stops the classic error of an order filling before it was submitted. 

@art partial-fill
And resolve doesn't only mean filled or not. When size matters, model partial fills or capacity limits. A large order at a level where only a little traded should come back partly filled, with the rest still resting, or cancelled, or expired, exactly as your order rules say.

@chapter Where people slip
@list heading="Common mistakes" items="Filling every touched limit order completely@The first|Assuming stops fill at the stop price@The second|Filling orders before submission@And the third"
The first mistake is filling every touched limit order completely. The second is assuming stops always execute at the stop price. And the third is allowing orders to fill before they were submitted. Use order specific fill logic, and handle unresolved intrabar order conservatively.

@chapter Try it
@words text="Order type · gap · intrabar assumption"
In the lesson's lab, which uses deterministic synthetic educational data, pick an order type, a gap condition and an intrabar assumption. Then read the simulated fill, the exit and the R multiple, and see how much the assumption alone moves the result.

@end text="Pick an order, add a gap"
You can simulate fills, gaps and stops yourself, on Learn. That's learn dot get er done dot I O.
