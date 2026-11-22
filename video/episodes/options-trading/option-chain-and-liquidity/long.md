---
format: long
lesson: options-trading/option-chain-and-liquidity
title: Reading an option chain: the spread is the price of getting in and out
thumb: The spread is the cost
---

@chapter The question
@title text="Option Chain and Liquidity" sub="Options Trading" art=thumb
You can have the right idea about a stock and still make a poor trade. Not because you were wrong about direction, but because of how you got in and out. That cost lives in the option chain, and it's easy to miss.

@art chain-grid
An option chain is a table. Each row is a strike, and the columns show the bid, the ask, the mid, the spread, volume, open interest, delta and implied volatility. The chain in the lesson's lab is synthetic, built for teaching, but you read a real one the same way.

@chapter Bid and ask
@art bid-ask-gap
The quote isn't one price. It's two. The bid is the displayed buying price, and the ask is the displayed selling price. The difference between them is the spread, and what you pay is the distance between them.

@chapter One row, read in full
@words text="100 call · 30 DTE · stock $100" sub="bid $3.31 · ask $3.46"
Take the lesson's default row: the one hundred call, thirty days to expiration, with the stock at one hundred. The bid is three thirty one, and the ask is three forty six.

@math heading="Price the spread" items="Spread = 3.46 − 3.31 = $0.15 per share@fifteen cents;;$0.15 × 100 = $15 per contract@fifteen dollars;;Mid = 3.385 → 0.15 / 3.385 = 4.4%@four point four"
The spread is fifteen cents per share, which is fifteen dollars per contract. The mid is three point three eight five, so as a share of the mid the spread is about four point four percent. The percentage is what makes one strike comparable with another.

@chapter Market orders
@art round-trip
Now trade it at the market. A market buy pays the ask: three hundred and forty six dollars. A market sell later, with the quote unchanged, receives the bid: three hundred and thirty one dollars.

@math heading="Round trip at the market" items="Buy at the ask: $346@three hundred and forty six;;Sell at the bid: $331@three hundred and thirty one;;Cost: $15 before the option moves@before the option"
Buy at three hundred and forty six, sell at three hundred and thirty one. So the round trip at the market costs the whole spread, fifteen dollars, before the option has moved at all. You pay it on the way in, and again on the way out.

@chapter Limit orders
@art limit-inside
A limit order lets you choose your price. Put a limit at the mid, three thirty eight. If it fills, you pay three hundred and thirty eight dollars. That saves eight dollars against the ask on the way in.

@words text="A limit that never fills is a trade that never happened"
The cost is that it may not fill. A limit sets your price, but it doesn't guarantee an execution. So set a limit based on the displayed market, and accept that it may not execute.

@chapter Volume and open interest
@art activity-bars
Volume measures contracts traded during the session. Open interest measures outstanding contracts after clearing updates. On this row, volume is eleven hundred and twenty one, and open interest is fifty eight hundred and one. They say the strike is active.

@words text="Activity is context" sub="It doesn't change the $0.15"
But they don't change the fifteen cents. Activity is context for whether you can get out later. The spread is the price of getting in and out now.

@chapter Choosing a contract
@art contract-funnel
So contract selection starts with the trade idea and ends with execution quality. You narrow a whole chain down to one contract, and the spread is the last filter, not an afterthought.

@list heading="Select from a chain" items="Choose expiration@choose the expiration|Choose strike@the strike|Inspect the market@inspect the market|Use a deliberate order@deliberate order"
First choose the expiration, which has to give the idea enough time while respecting premium and event exposure. Then choose the strike, using moneyness and, later, the Greeks. Then inspect the market: bid, ask, spread percentage and activity. And finally, use a deliberate order.

@chapter Where people slip
@list heading="Common mistakes" items="Buying the cheapest premium@The first|Using only open interest@The second|Market orders into wide spreads@The third"
The first mistake is buying the cheapest premium. A low price can reflect low delta, little time, or poor liquidity, rather than good value. The second is using only open interest. Current spread and depth matter at entry and exit. The third is sending market orders into wide spreads, which can produce a much worse price than you expected.

@chapter Try it
@words text="Spread in $ and % · market in and out · a limit inside"
Your turn. Read any chain row into a spread in dollars, and in percent of the mid. Say what a market order pays on the way in, and on the way out. Then place a limit inside the displayed market, and say what a limit at the mid saves, and what it risks.

@end text="Read a chain row yourself"
You can pick a row and set a limit inside the market, on Learn. That's learn dot get er done dot I O.
