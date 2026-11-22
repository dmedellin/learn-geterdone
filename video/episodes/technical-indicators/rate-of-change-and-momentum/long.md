---
format: long
lesson: technical-indicators/rate-of-change-and-momentum
title: Rate of change and momentum: name both prices
thumb: Now versus p bars ago
---

@chapter The question
@title text="Rate of Change and Momentum" sub="Technical Indicators" art=thumb
Momentum sounds like a feeling about a chart. In this lesson it's something much more exact: the difference between two prices, and you should be able to name both of them.

@words text="Current price vs the price p bars earlier"
Both indicators here compare the current price with the price a fixed number of bars earlier. That number is the lookback, p. One indicator reports the difference in price units. The other reports it as a percentage.

@chapter Two forms
@art two-points
Picture the price line with two points marked on it: the current close, and the close exactly p bars back. Everything in this lesson is about the distance between those two points.

@math heading="Momentum and ROC" items="Momentum = Cₜ − Cₜ₋ₚ@subtracts;;ROC = (Cₜ − Cₜ₋ₚ) ÷ Cₜ₋ₚ × 100@percentage change"
Simple momentum subtracts the earlier price from the current price, so it keeps price unit scale. Rate of change, ROC, expresses the percentage change from the price p bars earlier: the same difference, divided by the earlier price, times one hundred.

@chapter Why percentages
@math heading="A $5 move" items="$5 ÷ $20 = 25%@twenty dollar;;$5 ÷ $500 = 1%@five hundred dollar"
Here's why both forms exist. A five dollar move means something very different for a twenty dollar instrument and a five hundred dollar instrument. Five over twenty is twenty five percent. Five over five hundred is one percent. Raw momentum hides that. ROC shows it.

@art scale-compare
So use momentum when you want price unit change, and ROC when you want a normalized percentage change. Comparing raw momentum across price scales is the lesson's first common mistake.

@chapter The zero line
@art zero-line
Positive values mean the current price is above the comparison price. Negative values mean it's below. So the zero line isn't a magic level. It just marks where the current price equals the price p bars ago.

@words text="Positive ROC ≠ a complete long setup"
That's why a positive ROC isn't a complete long setup. It only establishes that price is above its lookback reference. Location, risk and a defined trigger are still missing. And a negative value doesn't tell you a trend is down. It only says price is below where it was p bars ago.

@chapter Lookback sets the timing
@art short-long-lookback
The crossing timing depends directly on the lookback. Short lookbacks react quickly and cross zero often. Long lookbacks compare price with a more distant reference, and cross less often, and later. Same prices, different answers, because the comparison price is different.

@list heading="Use a fixed-horizon measure" items="Choose the lookback@choose the lookback|Choose absolute or percentage form@absolute or percentage|Interpret the zero line@zero line|Define the event@define the event"
So, first, choose the lookback, the number of completed bars between the current and comparison prices. Choose absolute or percentage form. Interpret the zero line as position relative to the lookback price. And define the event: a zero cross, a threshold, a slope change, or a divergence, rather than momentum as a vague adjective.

@art event-types
Each of those events is something different. A zero cross is the moment the current price passes the comparison price. A threshold asks whether the change is bigger than some amount. A slope change asks whether the change itself is growing or shrinking. Pick one, and write it down before you look at results.

@chapter Where people slip
@list heading="Common mistakes" items="Comparing raw momentum across price scales@The first|Positive ROC as a complete long setup@The second|Changing lookback to force a zero cross@The third"
The first mistake is comparing raw momentum across price scales. The second is calling positive ROC a complete long setup. And the third is changing the lookback to force a desired zero cross. Choosing a parameter after seeing the outcome creates hindsight bias. 
@art adjusted-data
One more caution, about the data itself. ROC uses the exact price p bars earlier, so whatever that price is, it matters. Corporate actions, and adjusted versus unadjusted price data, can materially change historical calculations. A split in unadjusted data can look like an enormous move that never happened.

@chapter Try it
@words text="Current price · lookback price · both changes"
Your turn. Identify the current price and the lookback price. Calculate the absolute and the percentage change, and explain the zero line state. Then compare signal timing under a short lookback and a long one.

@end text="Change the comparison horizon"
You can change the lookback and watch the zero crossings move, on Learn. That's learn dot get er done dot I O.
