---
format: long
lesson: trading-risk-management/losing-streaks-and-drawdown
title: Losing streaks and drawdown: measuring the fall and the climb back
thumb: Measure from the peak
---

@chapter The question
@title text="Losing Streaks and Drawdown" sub="Trading Risk Management" art=thumb
Your strategy has a positive expectancy. On average, it makes money. So can it still put you through five losses in a row? Yes. And how deep that hole gets depends on something you might not expect: the order of the trades.

@words text="A losing sequence can occur even when expectancy is positive"
A losing sequence can occur even when expectancy is positive. And the order of outcomes matters. Several losses grouped together create a deeper drawdown than the same losses spread between winners.

@chapter Drawdown
@art peak-trough
Drawdown is the percentage decline from the account's previous equity peak. Maximum drawdown is the largest observed peak to trough decline in the sample.

@words text="Measured from the most recent peak"
So drawdown is measured from the most recent equity peak. Each decline is measured relative to the highest equity reached before it. Not from the first trade, and not from the average trade. That's expectancy's business. Drawdown is a peak to trough distance.

@art peak-marker
That means the reference point moves. Every time the account makes a new high, that high becomes the peak that the next drawdown is measured from.

@chapter The recovery requirement
@art recovery
Then there's the recovery requirement. That's the percentage gain needed, from the reduced balance, to regain the prior peak. And it's always larger than the drawdown.

@math heading="A 20% drawdown" items="peak $100,000 → $80,000@eighty thousand;;0.20 ÷ 0.80 = 25%@twenty five percent;;✗  +20%: $80,000 × 1.20 = $96,000@ninety six thousand;;✗  +40%: $80,000 × 1.40 = $112,000@a hundred and twelve thousand"
Take a twenty percent drawdown, from a hundred thousand to eighty thousand. The recovery is point two over point eight, which is twenty five percent. A twenty percent gain only reaches ninety six thousand. And forty percent overshoots, to a hundred and twelve thousand.

@chapter Worked example
@math heading="Peak $60,000 → $51,000" items="drop = $60,000 − $51,000 = $9,000@nine thousand;;drawdown = $9,000 ÷ $60,000 = 15%@fifteen percent;;recovery = $9,000 ÷ $51,000 = 17.6%@seventeen point six"
Here's the lesson's example. Equity peaks at sixty thousand dollars, and falls to fifty one thousand. That's a nine thousand dollar drop. Drawdown is nine thousand over sixty thousand, fifteen percent. Recovery is nine thousand over fifty one thousand, seventeen point six percent.

@math heading="Same thing, one formula" items="1 ÷ (1 − 0.15) − 1 = 17.6%@one divided by"
You can also write the recovery as one divided by one minus point one five, minus one. Same seventeen point six percent.

@words text="Decline from the peak · recovery from the trough"
The usual slip is mixing up the two bases. The decline is measured from the peak. The recovery is measured from the trough. Fifteen and fifteen is wrong, and so is seventeen point six and fifteen.

@chapter Order matters
@art two-orders
Why simulate outcome order? Because sequence changes drawdown. The same set of outcomes can create different drawdowns depending on order.

@words text="Same outcomes, same ending, different worst point"
Simulating doesn't change the strategy's rules. Those are fixed. And it doesn't remove losses. The same losses in a different order end at the same equity, with a different worst point along the way.

@chapter Depth and duration
@art long-shallow
Drawdown has two dimensions, depth and duration. A shallow but long drawdown can still challenge execution discipline. Time spent below the peak tests whether you keep following the plan, even when the percentage looks small.

@list heading="Practical rules" items="Track drawdown in % and in R@in percentage and in R|Set a maximum drawdown before live trading@define a maximum|Cut risk when drawdown exceeds the tested range@reduce or stop"
So the lesson's rules are these. Track drawdown in percentage and in R. Define a maximum acceptable drawdown before live trading. And reduce or stop risk when the observed drawdown exceeds the tested range.

@chapter Where people slip
@list heading="Common mistakes" items="Measuring only total return@The first|Assuming wins and losses alternate@The second|Increasing size while below the peak@the third"
Three mistakes. The first is measuring only total return. The second is assuming wins and losses will alternate. And the third is increasing size while below the equity peak.

@art alternating
That second one is the quiet assumption behind a lot of oversized risk. Outcomes don't take turns. Losses can arrive grouped together, and that grouping is what turns an ordinary set of trades into a deep drawdown.

@chapter Try it
@list heading="Lab steps" items="Track the equity peak@track the equity peak|Measure depth and duration@measure depth and duration|Compare with expectations@compare with expectations"
The lab's steps: track the equity peak, since drawdown is measured from the highest prior equity. Measure depth and duration. Then compare with expectations. Risk should stay survivable under worse than average sequences.

@words text="Synthetic educational data" sub="no live market connection"
The lab uses simplified synthetic examples, with no live market connection. For practice, take a thirty percent drawdown. Work out the recovery requirement with the same formula, before checking it in the lab.

@end text="Peak, trough, and the climb back"
You can reshuffle a sequence of trades and watch the drawdown change, on Learn. That's learn dot get er done dot I O.
