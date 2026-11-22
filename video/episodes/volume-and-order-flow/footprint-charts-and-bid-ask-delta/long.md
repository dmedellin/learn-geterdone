---
format: long
lesson: volume-and-order-flow/footprint-charts-and-bid-ask-delta
title: Footprint charts and delta: inside the candle
thumb: Aggression, not control
---

@chapter The question
@title text="Footprint Charts and Bid-Ask Delta" sub="Volume and Order Flow" art=thumb
A candle gives you four prices and a volume number. But inside that candle, trades happened at many prices, some at the bid and some at the ask. A footprint chart opens the candle up so you can see them.

@art footprint
A footprint displays classified sell volume and buy volume at each price level. The lesson writes each level as bid by ask. First the volume traded at the bid, classified as selling. Then the volume traded at the ask, classified as buying. Every level of the candle gets its own pair.

@chapter Delta
@art delta
From those two numbers comes delta. Delta is ask classified volume minus bid classified volume. Positive delta means more classified volume traded at the ask. Negative delta means more traded at the bid.

@math heading="One level" items="ask 900 · bid 600@nine hundred;;delta = 900 − 600 = +300@plus three hundred;;✗  600 − 900 = −300@backwards;;✗  900 + 600 = 1,500@fifteen hundred"
Say ask volume is nine hundred and bid volume is six hundred. Delta is nine hundred minus six hundred, plus three hundred. Bid minus ask gives the sign backwards. And fifteen hundred is the level's total volume, both sides added. Delta is the difference.

@chapter A whole candle
@art split-levels
Now a whole candle, from the lesson. It traded at three prices. Bid by ask, the levels were two hundred by five hundred, three hundred by three hundred, and four hundred by one hundred.

@math heading="Bid × ask: 200 × 500 · 300 × 300 · 400 × 100" items="ask: 500 + 300 + 100 = 900@ask volume;;bid: 200 + 300 + 400 = 900@bid volume;;delta = 900 − 900 = 0@delta is zero;;0 ÷ 1,800 = 0%@zero percent"
Ask volume is five hundred plus three hundred plus one hundred, nine hundred. Bid volume is two hundred plus three hundred plus four hundred, also nine hundred. So delta is zero, on eighteen hundred traded. As a share of volume, zero percent.

@words text="Buyers at the top · sellers at the bottom"
But look level by level. The top level alone is plus three hundred, and the bottom level alone is minus three hundred. The aggression was split: buyers at the top, sellers at the bottom. A zero for the candle hid that. So whenever a total looks quiet, it's worth checking the levels it came from.

@chapter Aggression is not control
@words text="Delta shows aggression" sub="not guaranteed control"
Here's the key caution. Delta shows aggression, not guaranteed control. It tells you who crossed the spread. It doesn't tell you who won. For that, you need to see what price did while the aggression was happening.

@art absorbed-candle
So suppose a candle has strongly positive delta, but closes near its low. What may be happening? Sell side absorption. Buyers were aggressive, and they were met. Passive selling absorbed the buying, and price failed to hold higher. Control is read from the close.

@words text="Negative delta, no decline" sub="possible buy-side absorption"
The mirror image works too. Negative delta with no decline can reveal buy side absorption. Sellers hit the bid, and resting buyers took everything they sold.

@chapter What a footprint can't show
@art book-vs-footprint
Does a footprint show resting orders that never traded? No. It primarily shows executed volume, built from executions throughout the candle. Resting size is the order book, which is a different thing. Unexecuted orders never appear in a footprint.

@art imbalance
Footprints also mark imbalances, where one side's volume exceeds the opposing comparison by a chosen ratio. The word chosen matters. Thresholds for imbalance must be declared. And delta itself is classification dependent.

@chapter Where people slip
@list heading="Common mistakes" items="Calling positive delta automatically bullish@The first|Ignoring the candle's place in structure@The second|Comparing raw delta across instruments@the third"
Three mistakes. The first is calling positive delta automatically bullish. The second is ignoring the candle's location in broader structure. And the third is comparing raw delta across instruments without normalisation.

@chapter Try it
@list heading="Reading steps" items="Read the candle result@read the candle result|Read delta@read delta|Find agreement or absorption@agreement or absorption"
The lab's steps keep you honest. First, read the candle result. Did price close higher, lower, or unchanged? Then read delta. Was aggression net positive or negative? Then look for agreement or absorption. Did price progress with delta, or resist it?

@words text="Synthetic educational data" sub="no live market connection"
The lab runs on synthetic educational data, with no live market connection. Find a candle with positive delta that closes lower, and say in one sentence what the aggressive buyers ran into.

@end text="Open the candle up"
You can read footprints and delta in the lab, on Learn. That's learn dot get er done dot I O.
