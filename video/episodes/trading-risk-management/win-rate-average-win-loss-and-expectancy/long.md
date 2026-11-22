---
format: long
lesson: trading-risk-management/win-rate-average-win-loss-and-expectancy
title: Win rate, payoff and expectancy: the average trade, worked out
thumb: Win rate isn't the whole story
---

@chapter The question
@title text="Win Rate, Average Win/Loss, and Expectancy" sub="Trading Risk Management" art=thumb
A strategy that wins only forty percent of the time. Is it a loser? Most people would say yes. But you can't tell from that number alone. You need to know how big the wins and losses are.

@art distribution
The market produces a distribution of wins and losses, not certainty on each trade. A lower win rate can still be profitable when average wins are sufficiently larger than average losses. Expectancy combines both sides.

@chapter Three numbers
@list heading="Three numbers" items="Win rate = wins ÷ total trades@Win rate is|Payoff ratio = average win ÷ average loss@The payoff ratio|Expectancy = average R or $ per trade@And expectancy"
Win rate is winning trades divided by total trades. The payoff ratio is average win divided by average loss. And expectancy is the expected average R, or dollars, per trade, after losses and costs.

@chapter Forty percent, two to one
@art two-piles
Here's the lesson's first example. A strategy wins forty percent of the time. Its wins are plus two R, and its losses are minus one R. What's the expectancy, before costs?

@math heading="Win 40% · +2R wins · −1R losses" items="0.40 × 2R = 0.80R@point four times two;;0.60 × 1R = 0.60R@point six times one;;0.80R − 0.60R = +0.20R@plus point two R"
Point four times two R is point eight R earned. Point six times one R is point six R lost. Subtract, and the expectancy is plus point two R per trade.

@math heading="Not these" items="✗  −0.2R: signs reversed@signs reversed;;✗  +0.8R: the win side alone@the win side alone"
Minus point two R has the signs reversed. And plus point eight R is the win side alone, before the sixty percent of losses are subtracted.

@chapter Why win rate isn't enough
@art high-win-big-loss
So why is win rate alone incomplete? Because it ignores average win and loss size. A high win rate can still lose money when losses are much larger than wins. Never judge a system from win rate alone. And the missing piece isn't anything cosmetic, like chart colour. It's the sizes of the wins and losses the rate applies to.

@chapter Breakeven
@art balance
Now turn it around. Suppose the average win is one and a half R, the average loss is one R, and there are no costs. What win rate makes the strategy break even, so the wins exactly pay for the losses?

@math heading="Breakeven win rate" items="breakeven = avg loss ÷ (avg win + avg loss)@average loss divided;;= 1 ÷ (1.5 + 1) = 40%@forty percent;;check: 0.40 × 1.5 − 0.60 × 1 = 0@check"
Breakeven is the average loss divided by the sum of the average win and average loss. One over two and a half is forty percent. To check, point four times one and a half, minus point six times one, is zero.

@words text="50% only if wins = losses" sub="60% is the reverse case: 1.5 ÷ 2.5"
Fifty percent is breakeven only when the average win equals the average loss. Here wins are larger, so you need fewer of them. And sixty percent is the breakeven of the reverse situation, wins of one R against losses of one and a half R.

@chapter Costs
@art costs
What do trading costs do to expectancy? They reduce it. A cost is paid on every trade, winners and losers alike, so it subtracts from the average. Commissions, spread, slippage, and assignment effects all reduce expectancy.

@math heading="Edge after costs" items="+0.26R − 0.08R = +0.18R@point two six"
The lesson's example: a point zero eight R cost on a plus point two six R edge leaves plus point one eight R. So use net results, after all known costs.

@chapter Sample size
@art small-sample
And use enough trades. A small sample can produce unstable win rate and payoff estimates. Treating a ten trade sample as stable evidence is one of the lesson's common mistakes.

@list heading="Common mistakes" items="Optimising only for win rate@The first|Best-case targets instead of real exits@The second|Trusting a 10-trade sample@the third"
So three mistakes. The first is optimising only for win rate. The second is using best case targets instead of realised exits. And the third is treating a ten trade sample as stable evidence.

@list heading="Practical rules" items="Measure win rate and payoff together@together|Use net results after costs@net results|Track by setup, timeframe and regime@track expectancy"
The practical rules: measure win rate and payoff together. Use net results after all known costs. And track expectancy by setup, timeframe, and regime.

@chapter Try it
@words text="Synthetic educational data" sub="no live market connection"
The lab uses simplified synthetic examples, with no live market connection. Its steps are short. Use enough trades. Include all costs. Then evaluate the combination.

@words text="Win 55% · +1R wins · −1.2R losses"
For practice, work out the expectancy of a strategy that wins fifty five percent of the time, with wins of one R and losses of one point two R. Then find its breakeven win rate with the same formula.

@end text="Judge the combination"
You can combine win rate, payoff and costs in the lab, on Learn. That's learn dot get er done dot I O.
