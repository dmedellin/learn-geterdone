---
format: long
lesson: trading-risk-management/reward-to-risk-and-r-multiples
title: R-multiples: measuring every trade in units of risk
thumb: Count it in R
---

@chapter The question
@title text="Reward-to-Risk and R-Multiples" sub="Trading Risk Management" art=thumb
You made four hundred dollars on a trade. Was that good? You can't say yet, because you don't know what it risked. R multiples fix that, by measuring every result in units of the risk you took.

@art one-r
One R is the distance from entry to the original invalidation. When price moves one initial risk distance in your favour, the trade is at plus one R. Two of those distances is plus two R.

@chapter Initial risk and R
@words text="Initial risk" sub="entry to original stop, including position size"
Initial risk is the planned loss from entry to the original stop, including position size. In dollars, it's what you'd lose if the stop were hit.

@math heading="R-multiple" items="R-multiple = P&L ÷ initial risk@divided by initial risk;;$400 ÷ $200 = +2R@four hundred;;✗  +1R would be $200@plus one R;;✗  +4R would be $800@plus four R"
An R multiple is realised or unrealised profit and loss, divided by initial risk. So if a trade risks two hundred dollars and gains four hundred, the outcome is four hundred divided by two hundred, plus two R. Plus one R would be a two hundred dollar gain. And plus four R would be eight hundred.

@chapter R is fixed at entry
@art trailed-stop
Now suppose you move your stop up as the trade works. Which risk defines R after that? The original planned risk. Performance is normally measured against the original initial risk, for consistency.

@words text="+3R stays +3R" sub="not +0.5R against a trailed stop"
If you re based R to the trailed stop, every trade would look small. A plus three R winner becomes plus point five R once the stop is trailed to plus two and a half R. The unit is fixed at entry. And the account balance isn't the unit either. It sets the dollars behind one R.

@chapter Partial exits
@art partial
Here's the lesson's trickier example. Initial risk is three hundred dollars. Half the position exits at plus two R. The other half is stopped at minus one R. What's the realised result?

@math heading="Initial risk $300 · two halves" items="0.5 × (+2R) = +1R@half of plus two;;0.5 × (−1R) = −0.5R@half of minus one;;+1R − 0.5R = +0.5R@plus point five R;;0.5 × $300 = +$150@a hundred and fifty"
Each half carries half the initial risk. Half of plus two R is plus one R. Half of minus one R is minus point five R. Together that's plus point five R, or plus a hundred and fifty dollars on the three hundred risked.

@words text="Average by size, don't add" sub="not +1R · not +2R"
Plus one R adds the two halves without weighting them. Plus two R is just what the first half earned on its share. Partial exits are averaged by size, not added.

@chapter Targets
@art structural-target
Does a five R target make a setup automatically better? No. The target must be realistic. Reward to risk is meaningful only when the target aligns with market structure and liquidity. A target only matters if structure gives price a realistic path to it.

@art tight-stop
And don't get there by tightening the stop. Tightening the stop to inflate the ratio moves it inside the noise, so the trade is stopped out before the target is ever tested. A distant target has no value if the stop is artificially tight.

@chapter Where people slip
@list heading="Common mistakes" items="Moving the stop closer to improve the ratio@The first|Calling the best unrealised move the result@The second|Ignoring partial exits@the third"
Three mistakes. The first is moving the stop closer only to improve the ratio. The second is calling an unrealised maximum excursion the realised result. And the third is ignoring partial exits when calculating R.

@art excursion
The second one flatters a record. A trade that touched plus three R and was closed lower didn't earn three R. The best point a trade reached isn't the result you record.

@list heading="Practical rules" items="Define 1R from the original entry and stop@define one R|Use structural targets first@structural targets|Record results in R@record realised"
So define one R from the original entry and stop. Use structural targets before calculating reward to risk. And record realised outcomes in R, so you can compare across trades.

@chapter Try it
@list heading="Lab steps" items="Mark entry and stop@mark entry and stop|Locate the structural target@locate the structural target|Compare without forcing@compare without forcing"
The lab's steps are: mark entry and stop, which defines one R. Locate the structural target, using prior highs, lows, range boundaries, or tested value areas. Then compare without forcing. Reject trades whose realistic target doesn't offer acceptable reward relative to risk.

@words text="Synthetic educational data" sub="no live market connection"
The lab uses simplified synthetic examples, with no live market connection. For practice, take the partial exit example, and change the split to a quarter at plus two R and three quarters stopped at minus one R. Work out the result in R.

@end text="One R, fixed at entry"
You can mark entries, stops and targets in the lab, on Learn. That's learn dot get er done dot I O.
