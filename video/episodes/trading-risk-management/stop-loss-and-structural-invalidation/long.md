---
format: long
lesson: trading-risk-management/stop-loss-and-structural-invalidation
title: Where the stop goes: structural invalidation, then size
thumb: The chart sets the stop
---

@chapter The question
@title text="Stop-Loss and Structural Invalidation" sub="Trading Risk Management" art=thumb
Where should your stop go? A lot of people pick a number that feels comfortable, like a round dollar loss. The lesson says that's backwards. The chart decides where the stop goes. The account decides how big the position is.

@art protected-low
In a bullish setup, buyers remain in control while the protected low holds. That's the swing low the whole idea depends on. A break below it shows that buyers failed to defend the structure.

@words text="The stop belongs beyond invalidation" sub="not at an arbitrary dollar loss"
So the stop belongs beyond invalidation, not at an arbitrary dollar loss. That's a structural stop: placed beyond the level whose break invalidates the setup.

@chapter Not profit, not a fixed percentage
@art same-distance
Where should a structural stop be based? On thesis invalidation. Not on your desired dollar profit. Profit is the target's business. And not on a fixed one percent price distance. On one instrument, one percent sits inside the noise. On another, it's beyond every swing.

@words text="The chart sets invalidation" sub="account risk sets quantity"
The distance comes from structure. The percentage that matters is account risk, and that sets quantity.

@chapter Noise
@art noise-stop
There's a second danger, called noise risk. A stop inside normal price movement may exit while the thesis remains valid. So allow for normal movement. Place the exit beyond invalidation, rather than directly inside common wick activity.

@art minor-wick
Here's an example. Price wicks below a minor low, but holds the protected low. What happened? Local volatility. The thesis fails at the protected low, and that level held. A minor low being taken is movement inside the structure.

@words text="Not failed · not guaranteed"
That doesn't mean the market guaranteed continuation. Nothing does. The structure simply hasn't been contradicted, which is a weaker, and truer, statement.

@chapter Wider stop, smaller size
@art wide-small
Now suppose your valid stop is wider than you expected. What should usually change? Position size. Reduce size so the wider structural stop still fits the risk budget. A wider valid stop requires a smaller position, not a forced tighter stop.

@words text="The protected low is a fact of the chart"
You can't move the thesis level to fit the loss, because then the stop no longer sits at invalidation, which was the whole point. And the protected low is a fact of the chart. It can't be moved to suit the account. Size can.

@chapter Worked example
@art break-below
Here's the lesson's example. A long trade, so a break below the protected low is what ends it. Entry at one thirteen eighty. Protected low at one oh eight fifty. Risk budget, five hundred dollars.

@math heading="Entry 113.80 · protected low 108.50 · stop 0.15 below" items="stop = 108.50 − 0.15 = 108.35@one oh eight point three five;;distance = 113.80 − 108.35 = $5.45@five forty five;;$500 ÷ $5.45 = 91.7@ninety one point seven;;round down → 91 shares@ninety one shares"
The stop sits fifteen cents beneath it, at one oh eight point three five. So the distance is five dollars forty five a share. With five hundred dollars of risk, five hundred divided by five forty five is ninety one point seven. Round down, to ninety one shares.

@math heading="Check" items="91 × $5.45 = $495.95@four hundred and ninety five;;✗  92 × $5.45 = $501.40@over the budget;;✗  94 uses 5.30, the low itself@five thirty"
Ninety one shares risks four hundred and ninety five dollars ninety five. Rounding up to ninety two would risk five hundred and one forty, over the budget, so quantity is always rounded down. And ninety four comes from dividing by five thirty, the distance to the protected low itself, not to the stop.

@chapter Where people slip
@list heading="Common mistakes" items="Stops where the loss feels comfortable@The first|Moving a stop farther after entry@The second|Same percentage stop on every chart@the third"
Three mistakes. The first is placing stops where the loss feels comfortable. The second is moving a stop farther after entry. And the third is using the same percentage distance stop for every chart.

@list heading="Practical rules" items="Define invalidation before quantity@define invalidation|Use close or wick rules consistently@close or wick rules|Include slippage beyond the trigger@slippage"
So define invalidation before calculating quantity. Use candle close or wick rules consistently. And include possible slippage beyond the trigger. A stop trigger doesn't guarantee the execution price.

@chapter Try it
@list heading="Apply it in order" items="Identify the protected level@identify the protected level|Allow for normal movement@allow for normal movement|Size from the distance@size from the distance"
The lab's order is the one you've just seen. Identify the protected level. Allow for normal movement. Then size from the distance, calculating quantity only after entry and stop are known.

@words text="Synthetic educational data" sub="no live market connection"
The lab uses simplified synthetic examples, with no live market connection. Try moving the stop farther from entry, and watch the share count fall while the dollar risk stays the same.

@end text="Structure first, then size"
You can place structural stops and size from them in the lab, on Learn. That's learn dot get er done dot I O.
