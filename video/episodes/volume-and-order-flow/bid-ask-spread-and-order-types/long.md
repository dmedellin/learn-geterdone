---
format: long
lesson: volume-and-order-flow/bid-ask-spread-and-order-types
title: Bid, ask, spread, and the order type you choose
thumb: Price or fill. Pick one.
---

@chapter The question
@title text="Bid, Ask, Spread, and Order Types" sub="Volume and Order Flow" art=thumb
You want to buy. There's a price on your screen. But is that a price you can actually get, right now? To answer that, you need to read a quote, and know what your order type promises.

@art quote
A quote has two sides. The bid is the highest displayed buying price. The ask is the lowest displayed selling price. And the distance between the best bid and the best ask is the spread.

@words text="The last price is history"
Notice what's missing from that list: the last traded price. The last price is history. The only prices currently executable are the displayed bid and ask. Assuming the last price is executable is one of the lesson's common mistakes.

@chapter Who pays the spread
@art lift-ask
Aggressive buyers lift the ask. Aggressive sellers hit the bid. So an aggressive buy order normally executes against the ask. A buyer who wants it now pays the lowest available selling price.

@art hit-bid
And a seller who wants immediacy executes at the bid. Either way, the side that demands immediate execution crosses the spread, and consumes resting liquidity.

@chapter Market and limit orders
@words text="Market: execution · Limit: price"
That gives you the two basic order types. Market orders prioritise execution. Limit orders constrain price, but can remain unfilled. Marketable orders take liquidity. Limit orders can provide it, but may not execute.

@art limit-resting
So what does a limit buy order guarantee? A maximum purchase price, not execution. It rests until a seller trades at or below its price. If no one does, it never fills. It can guarantee only one of the two, the price. The fill depends on someone else choosing to trade there.

@chapter Walking the book
@art walk-the-book
A market order has its own catch. It doesn't guarantee the displayed price. Larger marketable orders may consume several price levels.

@math heading="Bid 99.99 · Ask 100.01" items="spread = 100.01 − 99.99 = 0.02@point zero two"
Here's the lesson's example. Best bid ninety nine ninety nine, best ask one hundred point zero one. The spread is one hundred point zero one minus ninety nine ninety nine, which is point zero two.

@math heading="Market buy 500 · 300 offered at 100.01, 600 at 100.02" items="300 × 100.01 = 30,003@three hundred at;;200 × 100.02 = 20,004@two hundred more;;(30,003 + 20,004) ÷ 500 = 100.014@one hundred point zero one four"
Three hundred are offered at the ask, and six hundred at one hundred point zero two. A market buy for five hundred takes three hundred at the ask, and two hundred more at the next level. The average is one hundred point zero one four.

@math heading="Not these" items="✗  average 100.01@only the first;;✗  spread 0.01, average 100.015@split evenly"
It isn't one hundred point zero one. That's only the first level's price. And the order doesn't split evenly across the levels, so it isn't one hundred point zero one five either. It's three hundred at the first, two hundred at the second.

@chapter Spread as a cost
@art wide-narrow
A wide bid ask spread generally means more execution friction. Crossing a wider spread creates a larger immediate cost.

@words text="A cost, not a forecast"
But it's a cost, not a forecast. It says immediacy is expensive, not which way price goes. And it doesn't mean there are no market makers. Wide spreads are usually makers quoting cautiously. The cost to cross is real either way.

@chapter Where people slip
@list heading="Common mistakes" items="Assuming the last price is executable@The first|Market orders in thin books@The second|Assuming a limit order filled@the third"
Three mistakes. The first is assuming the last price is currently executable. The second is using market orders in thin books without checking depth. And the third is placing a limit order and assuming it filled.

@list heading="Rules" items="Market ≠ guaranteed price@doesn't guarantee|Limit ≠ guaranteed fill@doesn't guarantee execution|Count spread and depth as costs@include spread"
So keep three rules. A market order doesn't guarantee the displayed price. A limit order doesn't guarantee execution. And include spread and depth in your trade costs.

@chapter Try it
@list heading="Reading steps" items="Read the quote@read the quote|Choose urgency@choose urgency|Estimate impact@estimate impact"
The lab's steps follow the same order. First, read the quote: best bid, best ask, and spread. Then choose urgency. Does immediate execution matter more, or price control? Then estimate impact, since larger orders may consume several levels.

@words text="Synthetic educational data" sub="no live market connection"
The lab uses synthetic educational data, with no live market connection. Try a market buy that's larger than the first level, and work out its average fill before the lab shows you.

@end text="Read the quote, then choose"
You can send market and limit orders into a practice book, on Learn. That's learn dot get er done dot I O.
