---
format: long
lesson: trading-risk-management/leverage-and-margin-risk
title: Leverage and margin: how a small move becomes a big loss
thumb: Buying power isn't a risk limit
---

@chapter The question
@title text="Leverage and Margin Risk" sub="Trading Risk Management" art=thumb
Price moves five percent against you. That's a fairly ordinary move. So how can it cost you a fifth of your account? The answer is leverage, and this lesson walks through exactly how it works.

@words text="Leverage magnifies the move" sub="small market move → larger equity change"
Leverage turns a small market move into a larger change in account equity. The underlying price doesn't need to move far for a leveraged position to create a large gain, a large loss, a margin call, or forced liquidation.

@chapter Exposure and leverage
@art exposure
Gross exposure is the market value controlled by the position. Measure the full notional position, not only the cash you deposited.

@math heading="Effective leverage" items="leverage = gross exposure ÷ equity@divided by account equity;;$100,000 ÷ $25,000 = 4×@four times"
Effective leverage is gross exposure divided by account equity. So a hundred thousand dollar position on a twenty five thousand dollar account is four times leverage.

@chapter Four times, five percent
@art magnify
At four times leverage, a five percent adverse move creates roughly what change in equity, before costs? Twenty percent. The account holds four times its equity in the underlying, so the equity moves four times as far.

@math heading="4× leverage · 5% adverse move" items="4 × 5% = 20% of equity@twenty percent;;✗  5%: the underlying's move@the move in the underlying;;✗  10%: that's 2×@two times"
Four times five percent is twenty percent of equity. Five percent is just the move in the underlying. And ten percent would be the answer at two times leverage.

@chapter Margin
@art margin-call
Margin risk is that the broker may require additional equity, or liquidate positions, when requirements aren't met. Can a broker liquidate positions to meet margin requirements? Yes. Margin agreements and rules may permit forced liquidation, sometimes without advance notice.

@words text="The broker chooses what to sell"
And it's not the trader's choice which asset goes. The broker chooses which positions to liquidate. Your preference doesn't bind it.

@chapter Worked example
@math heading="$25,000 equity · $100,000 position · price −15%" items="loss = $100,000 × 15% = $15,000@fifteen thousand;;equity = $25,000 − $15,000 = $10,000@ten thousand;;change = −60%@minus sixty percent"
Here's the lesson's full example. Equity twenty five thousand, at four times leverage, so a hundred thousand dollar position. Price falls fifteen percent. The loss is fifteen percent of the whole position, fifteen thousand dollars. Equity drops to ten thousand, minus sixty percent.

@art shrink
Look at the two sizes. The position lost fifteen percent of its value. The equity lost sixty percent. That's four times leverage doing exactly what the formula says, and it's before the broker has said a word.

@math heading="Maintenance requirement 30%" items="position = $85,000@eighty five thousand;;required = 30% × $85,000 = $25,500@twenty five thousand five hundred;;$25,500 − $10,000 = $15,500 short@fifteen thousand five hundred"
The position is now worth eighty five thousand. At a thirty percent maintenance requirement, it needs twenty five thousand five hundred of equity. The account has ten thousand, so it's fifteen thousand five hundred short, and faces a call or liquidation.

@words text="✗ $21,250: 15% of equity, not of the position"
The tempting wrong answer is twenty one thousand two fifty. That applies the fifteen percent to equity. But it applies to the whole hundred thousand dollar position.

@chapter Buying power
@art buying-power
So how should buying power be treated? As a broker constraint, not a risk target. Buying power is what the broker permits you to hold. Nothing about it measures what you can afford to lose. Maximum permitted exposure isn't the same as prudent account risk.

@words text="Losses can exceed the deposit"
And no broker offers a guaranteed available loss. In some products, losses on a margined position can exceed the funds you deposited.

@chapter Where people slip
@list heading="Common mistakes" items="Sizing from maximum buying power@The first|Assuming a margin call gives you time@The second|Ignoring interest and forced liquidation@the third"
Three mistakes. The first is sizing from maximum buying power. The second is assuming a margin call provides guaranteed time to deposit funds. And the third is ignoring interest and forced liquidation risk.

@list heading="Practical rules" items="Measure leverage from total notional@total notional|Keep equity above broker and personal buffers@buffers|Stress-test gaps before using leverage@stress test gaps"
So measure leverage from total notional exposure. Maintain equity above both broker and personal buffers. And stress test gaps before using leverage.

@chapter Try it
@list heading="Lab steps" items="Calculate exposure@calculate exposure|Stress adverse movement@stress adverse movement|Keep a margin buffer@keep a margin buffer"
The lab's steps: calculate exposure. Stress adverse movement, translating a realistic price shock into account equity loss. And keep a margin buffer, because broker requirements can change.

@art buffer
A buffer is equity you keep above the requirement on purpose. It's the room that lets an adverse move happen without forcing a call, or a liquidation you didn't choose.

@words text="Synthetic educational data" sub="no live market connection"
The lab uses simplified synthetic examples, with no live market connection. For practice, rework the example at two times leverage, a fifty thousand dollar position on the same account, with the same fifteen percent fall.

@end text="Measure the notional, then stress it"
You can stress leveraged positions in the lab, on Learn. That's learn dot get er done dot I O.
