---
format: long
lesson: trading-risk-management/options-risk-management
title: Options risk management: premium, assignment and the real maximum loss
thumb: Premium isn't the risk
---

@chapter The question
@title text="Options Risk Management" sub="Trading Risk Management" art=thumb
With shares, your risk mostly comes down to direction and size. Options add more moving parts. You can be right about direction and still lose money. So what extra risks come with them?

@words text="Options add time, volatility and assignment risk"
Options add time, volatility, and assignment risk to the price direction thesis. The underlying can move the way you expected while the option still underperforms, because of time decay, a change in implied volatility, the spread, or contract selection.

@chapter Defined risk
@art long-call
Long options, and many spreads, have defined risk. They have a calculable maximum loss when held as constructed. So what's the maximum loss on a long call bought for three dollars?

@math heading="Long call at $3.00" items="$3.00 × 100 shares = $300 per contract@three hundred dollars"
Normally, it's the premium paid: three hundred dollars per standard contract. Premiums are quoted per share, and a standard equity option contract commonly covers a hundred shares. So three dollars is three hundred dollars, before fees.

@art multiplier
It isn't three dollars per contract. That forgets the multiplier. And it isn't unlimited. Unlimited loss belongs to uncovered short options. A long option can't lose more than it cost.

@chapter Assignment
@art assignment
Assignment risk belongs to the seller. Short American style options can be assigned before expiration, while the position is still open. So when can an American style short option be assigned? Any time before expiration, while it's open.

@words text="Not only at expiration · not never if out of the money"
Only at expiration is the European style. And out of the money assignment is unusual, but not impossible, and moneyness changes with price. Likelihood varies with moneyness, time value, and events. The position is exposed for as long as it's open.

@chapter The short put
@art short-put
Here's where premium misleads people. You sell a put and collect a premium. Is that premium both your maximum profit and your maximum risk? No. Premium is the maximum profit. But assignment can create a much larger purchase obligation, and loss.

@math heading="Sell one 50-strike put for $1.20" items="obligation = 100 × $50 = $5,000@five thousand;;premium received = 100 × $1.20 = $120@hundred and twenty dollars you received;;max loss = (50 − 1.20) × 100 = $4,880@fifty minus one twenty"
Here's the lesson's example. Sell one fifty strike put for a dollar twenty. If the stock goes to zero, assignment obliges you to buy a hundred shares at fifty, which is five thousand dollars. The hundred and twenty dollars you received reduces that. Fifty minus one twenty, times a hundred, is a maximum loss of four thousand eight hundred and eighty dollars.

@math heading="Not these" items="✗  $120: the premium, the max profit@the premium;;✗  $5,000: ignores the premium collected@ignores"
A hundred and twenty dollars is the premium, the maximum profit, not the maximum loss. And five thousand ignores the premium already collected.

@chapter Expiration
@art expiry
Expiration risk is its own category. In the money contracts can create stock obligations, exercise, or assignment near expiration. Holding contracts into expiration without sufficient buying power is one of the lesson's common mistakes.

@art decay
And while you wait, other forces work on the price. Time decay, called theta. Sensitivity to implied volatility, called vega. The spread. And gap scenarios. The lesson's rule is to include all of them.

@chapter Where people slip
@list heading="Common mistakes" items="Treating premium received as the risk@The first|Ignoring early assignment and ex-dividend risk@The second|Holding into expiration without buying power@the third"
Three mistakes. The first is treating premium received as the amount at risk. The second is ignoring early assignment and ex dividend risk. And the third is holding contracts into expiration without sufficient buying power.

@list heading="Practical rules" items="Know max loss and assignment obligation before entry@know the maximum loss|Close or manage unwanted short options before expiry@close or manage|Include spread, theta, vega and gaps@include spread"
So know the maximum loss and the assignment obligation before entry. Close or manage short options before expiration when obligations are unwanted. And include spread, theta, vega, and gap scenarios.

@chapter Try it
@list heading="Lab steps" items="Identify maximum loss@identify maximum loss|Map expiration obligations@map expiration obligations|Control contract liquidity@control contract liquidity"
The lab's steps: identify maximum loss, for the complete strategy, not only premium received. Map expiration obligations, the share quantity and cash needed if exercise or assignment occurs. And control contract liquidity, since spread and open interest affect entry, adjustment, and exit cost.

@words text="Synthetic educational data" sub="no live market connection"
The lab uses simplified synthetic examples, with no live market connection. For practice, work out the maximum loss for selling one forty strike put at ninety cents, using the same formula.

@end text="Know the obligation before entry"
You can map premiums, obligations and maximum losses in the lab, on Learn. That's learn dot get er done dot I O.
