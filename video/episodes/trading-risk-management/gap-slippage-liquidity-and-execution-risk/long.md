---
format: long
lesson: trading-risk-management/gap-slippage-liquidity-and-execution-risk
title: Gaps, slippage and liquidity: when the stop isn't the fill
thumb: A stop is a trigger
---

@chapter The question
@title text="Gap, Slippage, Liquidity, and Execution Risk" sub="Trading Risk Management" art=thumb
You set your stop at forty dollars. Price falls through it. Where do you get out? It's natural to assume forty. But the lesson's answer is: wherever the market lets you.

@words text="A stop price is a trigger" sub="not a guaranteed execution price"
A stop price is a trigger, not a guaranteed execution price. Fast price movement can pass through the planned stop before the order fills. And thin liquidity and gaps can make the realised loss larger than the planned loss.

@chapter Three risks
@art gap-through
Gap risk is when price opens, or trades, beyond the stop, without transactions at the planned level. There was simply no trade at your price.

@art fill-below
Slippage is the difference between the expected execution and the actual average fill. It's the gap between the plan and what you got.

@art thin-depth
And liquidity risk is when the quantity you want can't be executed near the quoted price without greater impact. Whatever exceeds the size shown at the first price fills further away.

@chapter Does a stop guarantee its price?
@words text="No"
So does a stop order guarantee the stop price? No. A stop is an instruction to send a market order once the trigger prints. The fill is whatever is available then, and after a gap, that can be far from the trigger.

@words text="Liquid stocks gap too" sub="earnings · halts · the open"
And it's not only an issue for thinly traded stocks. Liquid stocks gap too. Earnings, halts, and the open all produce prices with nothing traded between them.

@chapter Stop-limit orders
@art stop-limit
What about a stop limit order? It adds price protection, but it adds a different risk: it may not execute. Price protection can prevent execution when the market moves beyond the limit.

@words text="A price floor, maybe no fill"
It doesn't guarantee a loss. It guarantees a price floor, at the cost of possibly no fill at all. And it doesn't eliminate the spread. The spread is still paid on any fill.

@chapter Order size against depth
@art walk-levels
What usually happens when your order is large relative to depth? Slippage can increase. The order may consume multiple price levels, and receive a worse average fill. The spread doesn't disappear, and risk certainly doesn't become zero. The part that exceeds the displayed size fills further away.

@chapter Worked example
@math heading="500 shares · trigger 40.00 · average fill 39.70" items="slippage = 40.00 − 39.70 = 0.30@thirty cents;;0.30 × 500 = $150@a hundred and fifty dollars"
Here's the lesson's example. Five hundred shares, a stop trigger at forty dollars, and an average fill of thirty nine seventy. Slippage per share is forty minus thirty nine seventy, thirty cents. On five hundred shares, that's a hundred and fifty dollars on top of the planned loss.

@math heading="Not these" items="✗  $30 = 0.30 × 100@thirty dollars;;✗  $300 needs a 0.60 shortfall@three hundred"
Thirty dollars is thirty cents times a hundred, but the position is five hundred shares. And three hundred dollars would need a sixty cent shortfall. The fill was thirty cents under the trigger.

@words text="Reserve 0.30 per share in the sizing"
A thirty cent slippage reserve in the position sizing would have taken the same hundred and fifty dollars out of the quantity in advance. That's the point of a reserve. You pay for slippage in the plan, not as a surprise.

@chapter Where people slip
@list heading="Common mistakes" items="Treating the stop price as guaranteed@The first|Market orders without checking spread and depth@The second|Assuming a limit order must fill@the third"
Three mistakes. The first is treating the stop price as guaranteed. The second is using market orders without checking spread and depth. And the third is assuming a limit order must fill.

@list heading="Practical rules" items="Model the stop with a slippage reserve@slippage reserve|Reduce size around known event risk@reduce size|Know the broker and venue trigger rules@trigger rules"
So model your stop loss with a slippage reserve. Reduce size around known event risk. And understand your broker's and venue's trigger rules.

@art event-day
The second rule follows from everything before it. Around a known event, a gap past your stop is more likely, so a smaller position keeps the realised loss closer to the plan.

@chapter Try it
@list heading="Lab steps" items="Estimate normal spread@estimate normal spread|Stress abnormal movement@stress abnormal movement|Choose order trade-offs@choose order trade offs"
The lab's steps: estimate normal spread, and include it in the planned loss. Stress abnormal movement, with gaps, volatility halts, and event driven repricing. Then choose order trade offs. Marketable orders favour execution. Limit orders favour price, but may not fill.

@words text="Synthetic educational data" sub="no live market connection"
The lab uses simplified synthetic examples, with no live market connection. For practice, keep the five hundred shares and the forty dollar trigger, but suppose the fill comes in at thirty nine fifty. Work out the extra loss.

@end text="Plan for the fill, not the trigger"
You can stress gaps and thin books in the lab, on Learn. That's learn dot get er done dot I O.
