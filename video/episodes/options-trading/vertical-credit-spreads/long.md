---
format: long
lesson: options-trading/vertical-credit-spreads
title: Vertical credit spreads: a credit now, a defined worst case
thumb: Credit now, worst case known
---

@chapter The question
@title text="Vertical Credit Spreads" sub="Options Trading" art=thumb
Selling a put on its own collects premium, but the loss below the strike can be large. What if you bought a cheaper put further down, to put a floor under it? You'd keep less premium, and you'd know your worst case in advance.

@words text="Sell one option, buy a further one"
That's a vertical credit spread. Sell one option, buy a further one, with the same expiration. A credit now, and a defined worst case. The long option limits the short option's risk in the direction that hurts.

@chapter Two directions
@art bull-put-legs
A bull put spread sells a higher strike put and buys a lower strike put. It wants the price to stay above a threshold. That's the direction the lesson works through.

@art bear-call-legs
A bear call spread sells a lower strike call and buys a higher strike call. It wants the price to stay below a threshold. Same expiration, same logic, mirrored.

@chapter The worked example
@words text="Short 100 put $4.00 · long 90 put $1.50" sub="one spread · stock $103 at expiration"
The lesson's default is a bull put spread. Short the one hundred put at four dollars, long the ninety put at one fifty, one spread, with the stock at one hundred and three at expiration.

@math heading="Net credit and maximum profit" items="Credit = 4.00 − 1.50 = $2.50@four minus one fifty;;$2.50 × 100 = $250 received@two hundred and fifty;;Max profit = $250, at or above 100@maximum profit"
The net credit is four minus one fifty, two fifty per share, so two hundred and fifty dollars received. That's the maximum profit, kept in full if the stock finishes at or above the short strike and both puts expire worthless. At one hundred and three, that's what happens.

@math heading="Width and maximum loss" items="Width = 100 − 90 = $10@the width;;Max loss = (10 − 2.50) × 100 = $750@seven hundred and fifty"
The width is one hundred minus ninety, ten dollars. The maximum loss is ten minus two fifty, times one hundred: seven hundred and fifty dollars. You reach it at or below the long strike, where the short put costs ten dollars more than the long put pays, and the credit offsets two fifty of it.

@chapter Breakeven
@art credit-payoff
On the chart the payoff is flat at the maximum loss on the left, climbs between the strikes, and goes flat at the credit on the right. It crosses zero once, between the strikes.

@math heading="Breakeven" items="Breakeven = 100 − 2.50 = $97.50@ninety seven fifty;;On the short strike's side@short strike's side"
The breakeven is the short strike less the net credit: ninety seven fifty. It sits on the short strike's side. The long strike marks the maximum loss, not the breakeven.

@chapter At 95
@math heading="Stock $95 at expiration" items="Short put costs $5 · long put $0@costs five;;−5 + 2.50 = −$2.50 per share = −$250@minus two fifty;;Short put alone: 4.00 − 5 = −$1.00@alone"
Now try ninety five. The short put costs five dollars, the long put is worth nothing, and you add the two fifty credit. That's minus two fifty per share, minus two hundred and fifty dollars. The short put alone would be at minus one dollar here: four minus five.

@art protection-cost
So at ninety five, the spread is behind the naked short put. The long leg cost one fifty, for protection that only matters below ninety. That's the price of knowing your worst case.

@chapter Build it
@art floor-under
Think of the long leg as a floor under the short one. It costs something, and it decides exactly how far you can fall.

@list heading="Build a credit spread" items="Choose direction and range@Choose|Place the short strike@place the short strike|Buy the protective strike@buy the protective|Compare reward with maximum loss@compare"
To build one, choose the direction and range. Place the short strike, which defines the main obligation and the breakeven. Buy the protective strike, which caps the loss beyond it. Then compare the reward with the maximum loss. Here that's two hundred and fifty against seven fifty.

@chapter Where people slip
@list heading="Common mistakes" items="Focusing only on probability of profit@The first|Letting it expire near a short strike@The second|Defined risk means no management@The third|Full credit once past the short strike@the fourth"
The first mistake is focusing only on probability of profit. Frequent small wins can be offset by larger maximum losses. The second is letting the spread expire near a short strike. The third is assuming defined risk means no management. And the fourth is expecting the full credit as soon as the stock is past the short strike.

@art early-close-cost
That last one is about time. The chart is the expiration payoff. Weeks earlier the short leg still carries extrinsic value, so closing the spread costs part of the credit until that value has run out.

@chapter Try it
@words text="Credit · breakeven · max profit · max loss"
Your turn. Build either credit spread, and compute the credit, breakeven, maximum profit and maximum loss from the two strikes and two premiums. Remember the breakeven sits on the short strike's side, not the long strike's.

@end text="Set both legs yourself"
You can set the two strikes and premiums, then an expiration price, on Learn. That's learn dot get er done dot I O.
