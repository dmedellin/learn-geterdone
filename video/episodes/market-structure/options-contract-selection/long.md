---
format: long
lesson: market-structure/options-contract-selection
title: Choosing an option contract: time, strike and spread
thumb: Not the cheapest contract
---

@chapter The question
@title text="Options Contract Selection" sub="Market Structure" art=thumb
You've got a chart thesis. Price should go up, or down. Now you want to express it with a long call or a long put. Which contract do you pick? The tempting answer is the cheapest one. This lesson shows why that's usually the wrong question.

@art thesis-wrapper
Start with the underlying thesis. The option is a wrapper around that thesis, not a substitute for it. If the chart idea isn't defined, with an invalidation, no contract can fix that.

@words text="Synthetic chain · simplified model" sub="not live quotes"
One note before we start. The lesson's option chain is synthetic. Its prices and Greeks come from a simplified European style model, not live quotes. It's there to show the tradeoffs, not to price a real trade.

@chapter The decision stack
@list heading="Four decisions" items="Direction@Direction|Time@Time|Strike@Strike|Liquidity@Liquidity"
There are four decisions, in order. Direction: a long call expresses bullish exposure, a long put bearish, and you define the chart invalidation first. Time, strike, and liquidity come next.

@art expiry-buffer
Time. The expiration must outlast the thesis. In the lab's example the thesis window is ten days, so the selected expiration has to outlast those ten days. Extra time adds premium, and it changes how much time decay and volatility exposure you carry.

@art strike-ladder
Strike. Moneyness changes the premium, the delta, the intrinsic value, and how much of the underlying's move the contract captures. In the lab's synthetic example, near the money contracts balance premium against directional sensitivity. But the best fit depends on your thesis, risk limits, volatility, and actual quotes.

@art spread-gap
Liquidity. Look at the bid ask spread and the actual market depth. The spread is part of the cost of getting in and getting out. A good thesis can be damaged by expensive friction at both ends.

@chapter The words in the table
@list heading="Reading the chain" items="Delta: directional sensitivity@Delta|Theta: time decay per day@Theta|Vega: exposure to implied volatility@Vega|Time buffer: days beyond the thesis@time buffer"
The chain uses a few columns. Delta is the directional sensitivity. Theta is time decay, per day. Vega is exposure to implied volatility, per point. And the time buffer is how much life the contract has beyond your thesis window.

@chapter Right, and still disappointed
@art time-decay
Here's something that surprises people. You can be right about direction and still see a disappointing result. The lab's exit simulator shows why.

@list heading="What can offset the move" items="Elapsed time@elapsed time|A drop in implied volatility@implied volatility|Bid and ask friction@friction|Too small a move@too small"
Elapsed time eats premium. A decline in implied volatility lowers the option's value. Bid and ask friction takes a slice on the way in and out. And the move itself might simply be too small. Any of these can offset the gain from the underlying moving your way.

@art right-but-shrinking
Picture it. The underlying climbs, just as you said. But each day that passes takes some value out of the contract, and if volatility falls at the same time, the option can be worth less than you expected, even with the chart going your way.

@words text="Model sensitivity, not a forecast"
The simulator is a model sensitivity exercise. It lets you change the exit price and the days elapsed, holding implied volatility steady, to see how the contract might respond.

@chapter Pricing the spread
@art spread-gap zoom=in
The quote quality evaluator asks for a bid and an ask, real or hypothetical. When the gap is meaningful, include it in your entry, your exit, and your break even planning. It's a cost, not a detail.

@chapter The limits
@words text="Long calls and puts can expire worthless"
And keep the lesson's warnings. Long calls and puts can expire worthless. The lab doesn't model assignment, exercise decisions, taxes, commissions, early exercise, broker approval, or suitability. Review the standardized options risk disclosure before trading.

@chapter Try it
@list heading="The drill" items="Expiration outlasts the thesis@outlasts the thesis|A strike you can defend@strike you can defend|A spread priced into the plan@priced into the plan"
The drill is the whole decision. Choose the contract whose expiration outlasts the thesis, whose strike you can defend, and whose spread you've priced into the plan. Not simply the one with the lowest premium. A cheap contract that expires before your idea plays out isn't cheap at all. It's just a different bet from the one you meant to make.

@end text="Explore the synthetic chain"
You can select rows, simulate exits, and grade a quote yourself, on Learn. That's learn dot get er done dot I O.
