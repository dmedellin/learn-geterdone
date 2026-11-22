---
format: long
lesson: volume-and-order-flow/anchored-volume-weighted-average-price
title: Anchored VWAP: average value since the event that matters
thumb: Pick the event first
---

@chapter The question
@title text="Anchored VWAP" sub="Volume and Order Flow" art=thumb
Session VWAP answers one question: where's average value since today's open? But sometimes the open isn't the moment that matters. Maybe it's a major low, a gap, or an earnings day. What's average value since then?

@art anchor-pin
That's anchored VWAP. It measures average value since a chosen market event. You pick a starting bar, the anchor, and the line begins there.

@words text="Anchor" sub="major low · high · gap · earnings · breakout"
An anchor is a defined starting bar, such as a major low, a high, a gap, an earnings event, or a breakout. Each one asks the same kind of question. Since that moment, has trading been accepted above average value, or below it?

@chapter What changes
@art session-vs-anchor
So what changes between session VWAP and anchored VWAP? Only the starting point. Anchored VWAP begins at an event you define, rather than at a fixed session boundary.

@math heading="Anchored VWAP" items="AVWAP = Σ(typical price × volume) ÷ Σ volume@typical price times volume;;sums start at the anchor bar@begin at the anchor"
The formula is the same cumulative calculation. Add up typical price times volume, and divide by total volume. Both sums simply begin at the anchor.

@words text="The weighting stays"
And volume isn't removed. Without it, you'd have a plain average since the anchor. Anchored VWAP keeps the weighting.

@chapter Worked example
@art excluded-bars
Here's the lesson's example. The anchor is at bar ten. Bars ten and eleven have typical prices of fifty and fifty two, on two hundred contracts each. What's the anchored VWAP at bar eleven?

@math heading="Anchor at bar 10" items="50 × 200 = 10,000@fifty times two hundred;;52 × 200 = 10,400@fifty two times;;20,400 ÷ 400 = 51.00@fifty one"
Fifty times two hundred is ten thousand. Fifty two times two hundred is ten thousand four hundred. Add them for twenty thousand four hundred, and divide by four hundred contracts. Anchored VWAP is fifty one.

@words text="Bars before the anchor never enter the sum"
Fifty two would be bar eleven alone, but the sum includes bar ten. With equal volumes, the average sits right in the middle. And you don't need anything before bar ten. Everything before the anchor is deliberately excluded. That's what anchoring means.

@chapter Reading it
@art above-anchor
Above a rising anchor, buyers since the event are generally holding favourable price location. Below a falling anchor, sellers maintain control relative to that event. Price location shows whether trading since the anchor is accepted above or below average value.

@art reclaim-once
Now, price reclaims a falling anchored VWAP once. Is buyer control confirmed? No. A single close across the line is an event. The lab reads a reclaim only once price holds above and the line turns. Acceptance and follow through are still needed.

@words text="Crossing is normal"
And the line can certainly be crossed. It's an average of past trade, so price crosses it whenever current trade moves away from that average. A reclaim, a rejection, or repeated crossing all reveal changing control.

@chapter Choosing the anchor
@art many-anchors
So what makes a good anchor? It's tied to a meaningful event and a question. Not chosen after the result to make the chart fit. Moving the anchor until the chart agrees turns a measurement into a drawing. And not just the first visible candle, which is an arbitrary start.

@list heading="Common mistakes" items="Anchoring every minor pivot@The first|Hindsight to pick the perfect anchor@The second|Assuming everyone entered at AVWAP@the third"
Three mistakes. The first is anchoring every minor pivot. The second is using hindsight to select the perfect anchor. And the third is assuming all participants entered exactly at the anchored VWAP.

@words text="Context, not a trigger"
The rules are simple. Don't move the anchor to fit the result you wanted. Use objectively significant events. And treat an anchor as context, not a standalone entry trigger.

@chapter Try it
@list heading="Reading steps" items="Choose the event first@choose the event|Inspect slope and location@inspect slope|Watch the reaction@watch the reaction"
The lab's steps follow from all of that. First, choose the event. The anchor must answer a specific market question. Then inspect slope and location, looking for sustained acceptance. Then watch the reaction.

@words text="Synthetic educational data" sub="no live market connection"
The lab uses synthetic educational data, with no live market connection.

@art anchor-pin
Pick an anchor and write down the question it answers before you look at the line. Then say what the price location tells you. Is price holding above a rising line, below a falling one, or crossing back and forth? And if it crosses once, ask whether it holds there before you call a change in control.

@end text="Choose the event, then read the line"
You can place anchors and watch the line respond in the lab, on Learn. That's learn dot get er done dot I O.
