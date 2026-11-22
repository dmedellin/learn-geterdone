---
format: long
lesson: volume-and-order-flow/cumulative-volume-delta
title: Cumulative volume delta: aggression over time, against price
thumb: Flow versus progress
---

@chapter The question
@title text="Cumulative Volume Delta" sub="Volume and Order Flow" art=thumb
One candle's delta tells you who was more aggressive in that candle. But aggression builds up, or fades, over many bars. To see that, you keep a running total. That's cumulative volume delta, or C V D.

@words text="CVD = running total of (ask − bid)"
C V D is the running total of ask classified volume minus bid classified volume. Each bar's delta gets added on. Rising C V D means classified aggressive buying exceeds selling over the sample.

@chapter Running the total
@art cvd-steps
Here's the lesson's example. The series resets at zero. Then the bar deltas are plus three hundred, minus one hundred, plus two hundred, and minus five hundred. What's C V D after the fourth bar, and what was its highest value along the way?

@math heading="Deltas +300, −100, +200, −500" items="after bar 1: +300@plus three hundred;;after bar 2: 300 − 100 = +200@minus one hundred;;after bar 3: 200 + 200 = +400@plus two hundred;;after bar 4: 400 − 500 = −100@subtract five hundred"
After bar one, plus three hundred. After bar two, subtract one hundred, so plus two hundred. After bar three, add two hundred, plus four hundred. After bar four, subtract five hundred, and you land on minus one hundred.

@words text="Final −100 · high +400"
So C V D ends at minus one hundred, with a high of plus four hundred after bar three. The last bar's minus five hundred takes it below the reset.

@math heading="Two slips" items="✗  +1,100: adding absolute values@eleven hundred;;✗  high +300: only the first bar@plus three hundred"
Two slips to avoid. Eleven hundred adds the absolute values, but delta carries a sign, so the negatives subtract. And the high isn't plus three hundred. After three bars, the total was plus four hundred.

@chapter Confirmation
@art confirmation
Now compare C V D with price. When price and C V D both make higher highs, aggressive buying is aligned with upward price progress. Buyers are aggressive, and they're making progress. Flow and price agree.

@words text="Agreement ≠ guaranteed continuation"
But that describes the present, not the future. In fact the lab calls the aligned case the least informative one, precisely because nothing is in tension.

@chapter Divergence
@art divergence
Divergence is where it gets interesting. Aggressive flow progresses while price doesn't, or price progresses without matching flow. Say C V D rises strongly while price stays flat. That may show passive sellers absorbing buyers.

@words text="Not 'no buyers' · not a certain rally"
It's not that there are no buyers. Rising C V D is buyers crossing the spread, and they're being filled. And it's not a certain rally. The aggression is being taken by resting sellers, and whether they run out, or the buyers do, isn't in the number.

@art flow-vs-price
Either way, the lesson's summary is the same. When price and C V D rise together, buyers are aggressive and making progress. When C V D rises but price stalls, sellers may be absorbing demand. Flow is the effort, and price shows whether it worked.

@chapter What CVD depends on
@art two-feeds
C V D depends on how trades are classified, and where the series resets. Not candle colour, since C V D is built from where each print landed against the quote. And not the same feed everywhere. Venue, aggregation and classification method all move the line.

@list heading="Practical rules" items="Define session and reset conventions@define your session|Treat classification as an estimate@an estimate|Confirm divergence with price structure@confirm divergence"
So the lesson's rules are these. Define your session and reset conventions. Treat classification as an estimate. And confirm divergence with price structure.

@chapter Where people slip
@list heading="Common mistakes" items="Assuming CVD is identical across vendors@The first|Calling every divergence a reversal@The second|Ignoring off-exchange and aggregated data@the third"
Three mistakes. The first is assuming C V D is identical across data vendors. The second is calling every divergence a reversal. And the third is ignoring off exchange and aggregated data limitations.

@art reset
That first one catches people. Two charts of the same market can show different C V D lines, because they start from different resets or classify prints differently.

@chapter Try it
@list heading="Reading steps" items="Read price structure@read price structure|Read CVD structure@read C V D structure|Compare progress@compare progress"
The lab follows three steps. Read price structure: up, down, or range? Read C V D structure: is cumulative aggression rising or falling? Then compare progress. Agreement supports control. Disagreement suggests absorption, or changing participation.

@words text="Synthetic educational data" sub="no live market connection"
The lab runs on synthetic educational data, with no live market connection. Make your own short list of four bar deltas, keep the running total by hand, and mark its highest point before the lab draws it.

@end text="Flow against progress"
You can compare C V D with price in the lab, on Learn. That's learn dot get er done dot I O.
