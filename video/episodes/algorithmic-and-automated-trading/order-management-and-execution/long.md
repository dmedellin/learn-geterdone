---
format: long
lesson: algorithmic-and-automated-trading/order-management-and-execution
title: Execution quality: measuring slippage against the decision price
thumb: Right direction, edge eaten
---

@chapter The problem
@title text="Order Management and Execution" sub="Algorithmic and Automated Trading" art=thumb
Your strategy calls the direction right. Price goes up, just as it said. And the trade still disappoints. The lesson's explanation: a correct direction can still produce a poor result when execution consumes the edge.

@art competing-buyers
Here's how. When buyers are already lifting offers, another large buy order competes for limited liquidity. It can push its own average fill higher. You're paying more because you're one of the buyers.

@chapter Three ideas
@list heading="What to understand" items="Decision price@decision price|Execution policy@execution policy|Fill quality@fill quality"
Three ideas. The decision price: the market price when the strategy and risk engine approved the trade. The execution policy: market, limit, time sliced or participation based instructions, each with a deadline. And fill quality: completion rate, slippage, spread cost, market impact and adverse selection.

@art order-types
Each policy trades certainty against price. A limit order controls the worst price you'll accept, not whether you get filled. It can stay unfilled if the market moves away. A market order fills, but takes what's offered. Time slicing breaks one parent order into smaller children spread over time.

@chapter Thin liquidity
@art book-levels
A large, urgent order in thin liquidity can create more slippage and impact. It may consume several price levels. It won't get the midpoint, because nothing rests at the midpoint. And it doesn't shrink the spread. Taking liquidity removes what was quoted.

@words text="Match policy to urgency, liquidity and horizon"
So the lesson says execution policy should match urgency, liquidity and the strategy's horizon. Using market orders without a liquidity rule is one of its named mistakes.

@chapter Measure every execution
@list heading="Measure every execution decision" items="Plan: quantity, urgency, limits, participation, deadline@Plan|Execute: children within the parent intent@Execute|Evaluate: fill and completion vs decision price@Evaluate"
The method has three steps. Plan: set the quantity, urgency, price limits, participation and deadline. Execute: manage child orders and broker updates without exceeding the parent's intent. Evaluate: compare the average fill and the completion with the decision benchmark.

@art parent-child
Tracking parent and child quantities exactly is the hard part. Every child that fills reduces what the parent still needs. And replacing an order without accounting for cancel latency is a named mistake: the old child might fill while the new one is already working.

@art decision-benchmark
Measuring that needs a benchmark, and the lesson's is the decision price. Not the highest historical price, against which every fill looks excellent. And not the final daily close, hours after the decision. The decision price connects the fill to the moment the trade was approved, so slippage means what it says.

@chapter Slippage in basis points
@math heading="Decision $110.23 · average fill $113.38" items="113.38 ÷ 110.23 − 1 = 0.0286@Divide the fill;;0.0286 × 10,000 ≈ 286 bps@ten thousand"
Now the lesson's worked example. The decision price is one hundred and ten twenty three. Eight time sliced children fill at an average of one hundred and thirteen thirty eight. Divide the fill by the decision price and subtract one: about zero point zero two eight six. Multiply by ten thousand to get basis points. About two hundred and eighty six.

@words text="Not 3.15 · not 29"
Three fifteen is the gap in dollars, not basis points. And twenty nine comes from multiplying by a thousand instead of ten thousand. A basis point is a hundredth of a percent.

@art sliced-through-trend
Why so much? The children paid for thirty six bars of a rising market. That's the cost of slicing an order through a trend. Patience lowered the impact of each child, but the price ran away from all of them.

@chapter Where people slip
@list heading="Common mistakes" items="Market orders with no liquidity rule@The first|Replacing orders without cancel latency@The second|Strategy returns with no execution benchmark@And the third"
The first mistake is using market orders without a liquidity rule. The second is replacing an order without accounting for cancel latency. And the third is evaluating strategy returns without execution benchmarks. Measure against a documented benchmark like the decision price, not the day's close or a record high.

@chapter Try it
@words text="Market · limit · time-sliced · participation"
In the lesson's lab, which uses deterministic synthetic educational data with no broker or live market connection, compare market, limit, time sliced and participation execution, under different order sizes, spreads and market directions.

@end text="Compare four ways to execute"
You can compare execution policies and measure slippage yourself, on Learn. That's learn dot get er done dot I O.
