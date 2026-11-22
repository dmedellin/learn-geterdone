---
format: long
lesson: trade-setup-execution/stop-loss-placement
title: Stop-loss placement: beyond invalidation, within reason
thumb: Where the setup is wrong
---

@chapter The question
@title text="Stop-Loss Placement" sub="Trade Setup & Execution" art=thumb
Where does your stop go? If the honest answer is wherever the loss feels acceptable, this lesson is for you. That price might sit right inside normal price movement, and take you out of a trade that was still perfectly valid.

@words text="Beyond invalidation · room for noise · size adapts"
The lesson's rule has three parts. Place the stop beyond structural invalidation. Allow appropriate room for normal variation. And let position size adapt to fit the account's risk budget.

@words text="Process and measurement" sub="no live data, no recommendations, no signals"
As with the rest of this course, it teaches process and measurement. It doesn't give live market data, personal recommendations, or trade signals. The unit counts in its lab are illustrative.

@chapter Invalidation first
@art stop-in-noise
The stop should represent where the setup is wrong, not just where the loss gets uncomfortable. A stop placed inside the recent candles can be hit while the structure that justified the trade is still intact.

@art structural-buffer
So start from structure. Mark the swing or boundary whose loss disproves the setup. Then place the stop beyond it, with a justified buffer for volatility, spread, and timeframe. The buffer needs a reason too.

@chapter How much room?
@art atr-span
How big a buffer? The lesson uses ATR, the average true range, as its yardstick for normal variation. It's the average distance a candle travels on this timeframe, from high to low. Because it's measured on your own timeframe and instrument, it scales the buffer to how much this market normally moves.

@words text="More than ~2 ATR beyond invalidation = too wide"
The lab calls a stop too wide once it sits more than about two ATR beyond invalidation. Past that point you're no longer buying room for noise. You're paying for a thesis that has already failed.

@art too-wide
And that extra distance isn't free. Every extra unit of distance is one fewer unit of size. A stop can be too far as well as too tight. Too tight, and noise takes you out. Too far, and you trade a smaller position for no defined reason.

@chapter Size adapts
@math heading="Position size" items="per-unit risk = |entry − stop|@entry to stop;;units = risk budget ÷ per-unit risk@divide the risk budget;;round down to whole units@round down"
Then you connect the setup to the account through price risk. Measure the distance from entry to stop, using the actual planned entry, not an idealized price. Divide the risk budget by that per unit risk. And round down, because rounding up would take you past the budget you set.

@art size-tradeoff
That's why size adapts. With the account risk fixed, a wider structural distance means a smaller position, and a tighter valid distance allows a larger one. The stop decides the size, never the other way round.

@chapter The process
@list heading="Stop-loss placement process" items="Mark structural failure@Mark structural failure|Place beyond failure@Place beyond failure|Measure entry-to-stop distance@Measure|Calculate position size@Calculate"
So the whole process is four steps. Mark structural failure. Place beyond failure. Measure the entry to stop distance. Calculate the position size. Keep the setup logic separate from the account sizing, and connect them only through that price risk.

@chapter Where people slip
@list heading="Common mistakes" items="Stopping where the loss feels acceptable@The first|One percentage stop for every setup@The second|Widening the stop after entry@The third|Sizing first, then forcing the stop@And the fourth"
The first mistake is placing the stop where the loss feels acceptable. The second is using the same percentage stop on every setup, when instruments, timeframes, and structures need different distances. The third is widening the stop after entry. And the fourth is sizing first and forcing the stop to fit, which disconnects risk from structure.

@art widen-after
Widening after entry is the one that hurts most. When price approaches invalidation and you move the stop farther away, you've increased the risk and changed the original plan, at exactly the moment it was being tested.

@chapter Try it
@words text="Valid: loss side · beyond invalidation · within ~2 ATR" sub="units = budget ÷ distance, rounded down"
Here's the lesson's standard. On each tab, drag the stop to a valid price. Valid means on the loss side of entry, beyond structural invalidation, and within about two ATR of it. Then say how many units the budget allows: the risk budget divided by the distance you chose, rounded down.

@end text="Drag the stop yourself"
You can drag the stop, see the ATR room, and watch the size change, on Learn. That's learn dot get er done dot I O.
