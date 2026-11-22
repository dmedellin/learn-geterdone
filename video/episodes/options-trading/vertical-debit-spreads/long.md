---
format: long
lesson: options-trading/vertical-debit-spreads
title: Vertical debit spreads: lower cost, capped reward
thumb: Buy one, sell a further one
---

@chapter The question
@title text="Vertical Debit Spreads" sub="Options Trading" art=thumb
A call costs more than you'd like to pay. What if you sold a second call, further out, to cover part of the cost? You'd pay less, and you'd give something up. That's a vertical debit spread.

@words text="Buy one option, sell a further one"
Buy one option, sell a further one, same expiration. Lower cost, capped reward. And because both the most you can lose and the most you can make are fixed, every figure comes straight from the two strikes and the two premiums.

@chapter Two directions
@art bull-call-legs
A bull call spread buys a lower strike call and sells a higher strike call, with the same expiration. The long call gives you the main directional exposure. The short call reduces the cost and sets the maximum reward.

@art bear-put-legs
A bear put spread is the mirror. Buy a higher strike put, and sell a lower strike put, with the same expiration. Bullish exposure, use the call spread. Bearish exposure, use the put spread.

@chapter The worked example
@words text="Long 100 call $5.50 · short 110 call $2.00" sub="one spread · stock $108 at expiration"
The lesson's default is a bull call spread. Long the one hundred call at five fifty, short the one hundred and ten call at two dollars, one spread, and the stock at one hundred and eight at expiration.

@math heading="Net debit and maximum loss" items="Debit = 5.50 − 2.00 = $3.50@five fifty minus two;;$3.50 × 100 = $350 paid@three hundred and fifty;;Max loss = $350, at or below 100@maximum loss"
The net debit is five fifty minus two, three dollars fifty per share, so three hundred and fifty dollars paid. That's the maximum loss. You reach it at or below the long strike, where both calls expire worthless.

@math heading="Width and maximum profit" items="Width = 110 − 100 = $10@the width;;Max profit = (10 − 3.50) × 100 = $650@six hundred and fifty"
The width is one hundred and ten minus one hundred, ten dollars. The maximum profit is ten minus three fifty, times one hundred: six hundred and fifty dollars. You reach it at or above the short strike, where the long call is worth ten dollars more than the short one, and nothing more can be earned.

@chapter Breakeven
@art spread-payoff
On the chart, the payoff is flat at the maximum loss on the left, climbs between the strikes, and goes flat at the maximum profit on the right. It crosses zero once, somewhere between the two strikes.

@math heading="Breakeven" items="Breakeven = 100 + 3.50 = $103.50@one hundred and three fifty;;Not 100 + 5.50@not the long premium"
The breakeven is the long strike plus the net debit: one hundred and three fifty. It's not the long premium alone. The short leg lowered the debit, so it lowered the breakeven too.

@chapter At 108
@math heading="Stock $108 at expiration" items="Long call $8 · short call $0@worth eight;;8 − 3.50 = +$4.50 per share = +$450@four fifty;;Long call alone: 8 − 5.50 = +$2.50@on its own"
At one hundred and eight, the long call is worth eight dollars, the short call is worth nothing, and you subtract the three fifty debit. That's plus four fifty per share, four hundred and fifty dollars. The long call on its own would be at plus two fifty here: eight minus five fifty.

@art spread-vs-single
So at this price the spread is ahead of the single call. Further up, the spread is capped while the single call keeps rising, so eventually the single call catches up and passes it. That's the trade you made for the lower cost.

@chapter Build it
@art build-steps
Building one is four decisions, made in order, and the last one is a check.

@list heading="Build a debit spread" items="Choose direction@Choose|Set the long strike@the long strike|Set the short strike@the short strike|Verify debit and width@verify"
To build one, choose the direction. Set the long strike, for the main exposure. Set the short strike, which should reflect a realistic price objective, because it caps the reward. Then verify the debit and width. The net debit must be positive, and lower than the strike width.

@chapter Where people slip
@list heading="Common mistakes" items="Short strike beyond a realistic target@The first|Ignoring both-leg execution@The second|Defined risk removes expiration risk@The third|Max profit as soon as it passes the short strike@the fourth"
Four mistakes. The first is putting the short strike beyond a realistic target, paying for width you won't use. The second is ignoring both leg execution, since legging in can create exposure you didn't intend. The third is assuming defined risk removes expiration risk. And the fourth is expecting maximum profit as soon as the stock passes the short strike.

@art early-value
That last one is about time. The chart is the expiration payoff. Weeks earlier, the short leg still carries extrinsic value, so a spread that's fully in the money trades well under its width until that value has run out.

@chapter Try it
@words text="Debit · breakeven · max loss · max profit"
Your turn. Build either debit spread, and compute the debit, breakeven, maximum loss and maximum profit from the two strikes and two premiums. Watch the breakeven, which is the figure most often done with the wrong premium.

@end text="Set the strikes and premiums"
You can set both legs and drag the expiration price, on Learn. That's learn dot get er done dot I O.
