---
format: long
lesson: options-trading/moneyness
title: Moneyness: in, at or out of the money, and what it really means
thumb: Stock versus strike, nothing else
---

@chapter The question
@title text="Moneyness" sub="Options Trading" art=thumb
Is this option in the money? It sounds like a question about profit, but it isn't. Two numbers decide it, the stock price and the strike, and nothing else. Not the premium, and not whether you're winning.

@art strike-ladder
Picture a chain as a ladder of strikes, with the stock price sitting somewhere among them. Moneyness is just where each strike sits relative to that price, and whether you're looking at a call or a put.

@chapter In the money
@art call-itm
A call is in the money when the stock is above the strike. It gives you the right to buy at the strike, and right now the stock is worth more than that.

@art put-itm
A put is in the money when the stock is below the strike. It gives you the right to sell at the strike, and the stock is worth less than that. Same comparison, opposite direction.

@list heading="Classify in four steps" items="Read the underlying price@the current price|Read the strike@read the strike|Apply the call or put rule@apply the rule|Calculate intrinsic value@intrinsic value"
So the method is short. Read the current price of the underlying. Then read the strike, and don't use the option premium as the strike. Then apply the rule for a call or a put. And finally, calculate intrinsic value.

@chapter Intrinsic value
@math heading="Intrinsic value" items="Call: max(S − K, 0)@For a call;;Put: max(K − S, 0)@for a put;;Never below zero@never"
For a call, intrinsic value is the larger of stock minus strike, and zero. For a put, it's the larger of strike minus stock, and zero. That max with zero is the whole point. Intrinsic value can never be negative.

@art intrinsic-floor
Draw it and you get a floor. Out of the money, intrinsic value sits at zero no matter how far away the strike is. In the money, it climbs one for one with the distance between stock and strike.

@chapter At the money
@words text="Strictly: strike = stock" sub="no intrinsic value"
At the money has a strict meaning. The strike equals the stock price, so the option has no intrinsic value. In the lesson's lab, a strike within half a percent of the stock gets the at the money badge.

@art atm-nearest
But a chain uses the word differently. By convention, it calls the nearest listed strike at the money, and that strike can be a little in or out of the money. The lab marks the nearest strike separately for exactly this reason.

@math heading="Stock $102, nearest strike 100" items="Chain label: “ATM”@calls the one hundred;;100 call: max(102 − 100, 0) = $2.00 in the money@its call is;;100 put: max(100 − 102, 0) = $0, out of the money@the put"
Here's the lesson's own example. The stock is at one hundred and two, and the chain calls the one hundred strike at the money. But its call is two dollars in the money: one hundred and two minus one hundred. The put at that strike has zero intrinsic value, so it's out of the money.

@chapter Out of the money
@art otm-extrinsic
Out of the money options have no intrinsic value. That doesn't make them worthless. Before expiration, an out of the money option can still carry extrinsic value, because there's still time for the stock to move past the strike. That value is the next lesson's subject. At expiration, though, an option with no intrinsic value is worth nothing.

@chapter Where people slip
@list heading="Common mistakes" items="Chain “ATM” = zero intrinsic@The first|Using premium to classify@The second|OTM means worthless now@The third"
The first mistake is reading a chain's at the money label as zero intrinsic value. The second is using the premium to classify moneyness. Premium affects profit and value, but not the in or out of the money relationship. The third is assuming out of the money means worthless immediately.

@words text="In the money ≠ profitable"
And underneath all three: in the money is not the same as profitable. Moneyness compares stock and strike. Profit also depends on what you paid. An option can be in the money and still be a losing position, because the premium hasn't been covered yet.

@chapter Try it
@words text="Classify · compute · explain"
Your turn. For any call or put, classify it as in, at or out of the money from the stock and the strike. Compute its intrinsic value. And for the strike a chain calls at the money by convention, say what intrinsic value it actually carries.

@end text="Move the stock, watch every strike"
You can move the stock and watch each strike's status change, on Learn. That's learn dot get er done dot I O.
