---
format: long
lesson: algorithmic-and-automated-trading/market-data-ingestion-and-normalization
title: Live market data: event time, duplicates and the feed that goes stale
thumb: When it happened, not when it arrived
---

@chapter The problem
@title text="Market Data Ingestion and Normalization" sub="Algorithmic and Automated Trading" art=thumb
Buyers are pushing price higher. Then your strategy sees a sudden reversal, or the same breakout twice. Nothing happened in the market. Something happened in the data.

@words text="Only as current and consistent as its data"
The lesson's point is that a trading decision is only as current and consistent as the data used to produce it. Duplicated, stale or out of order records can make a strategy see a false reversal or a repeated breakout.

@chapter Three ideas
@list heading="What to understand" items="Event time@Event time|Normalization@Normalization|Data health@data health"
Three ideas. Event time: the time the market event occurred, distinct from the time your system received it. Normalization: converting provider specific messages into one internal schema, with consistent units and identifiers. And data health: measuring gaps, duplicates, lateness, sequence errors and feed freshness, continuously.

@art two-clocks
Keep both times. Event time and receive time describe the same event, and the difference between them reveals transport delay. It also supports correct ordering, because arrival order is only transport order. Treating arrival order as market order is a named mistake.

@chapter Duplicates and gaps
@art duplicate-event
A duplicate trade event can cause repeated signals, or incorrect volume. The repeated input updates indicators and strategy state more than once. And the broker never sees the duplicate itself. It sees whatever the strategy did with it, which might be a second order that's accepted.

@words text="Stable event IDs or sequence rules"
So deduplicate with stable event identifiers or sequence rules. And when values are missing, don't silently fill them in without quality flags. A gap is information, and the strategy needs to know it's there.

@chapter Validate before publishing
@list heading="Validate before publishing" items="Receive: authenticate, keep the original@Receive|Validate: schema, sequence, time, price, volume, freshness@Validate|Publish: normalized event with provenance and quality@Publish"
The lesson's pipeline has three steps. Receive: authenticate, and capture the original provider message. Validate: check the schema, sequence, timestamp, price, volume and freshness. Publish: emit a normalized event, with its provenance and a quality status.

@art one-model
Normalization should happen before strategies consume the feed, once, in one place. Not after an order fills, when every decision has already been made. And not inside every chart separately, where each consumer would fix the feed its own way and disagree with the others. One model keeps everything downstream consistent and testable.

@chapter How late is it?
@math heading="Provider 10:15:02.000 · received 10:15:09.500 · max age 5 s" items="lateness = receive − event@receive time minus event time;;10:15:09.5 − 10:15:02.0 = 7.5 s@seven point five;;7.5 s > 5 s limit → flag stale, hold trading@over the limit"
Here's the lesson's worked example. An event is stamped ten fifteen and two seconds by the provider, and received at ten fifteen and nine and a half seconds. The maximum feed age is five seconds. Lateness is receive time minus event time, which is seven point five seconds. That's over the limit.

@art late-event
So what does the normalizer do? It keeps the record, placed by event time, with a quality flag, because it's a real trade and belongs in the history. But it can't be treated as current. The feed is flagged stale, and the strategy is degraded until fresh data arrives.

@words text="Not 0 s late · not discarded"
Calling it zero seconds late confuses arrival with occurrence. And discarding it throws away a real event. The right answer keeps the record and stops trading on it.

@art raw-vs-clean
Put the raw feed next to the normalized one and the difference is easy to see. The raw stream has repeats, gaps and events out of order. The normalized stream is in event order, with each repair flagged, so the strategy downstream doesn't have to reimplement any provider specific cleanup.

@chapter Where people slip
@list heading="Common mistakes" items="Arrival order treated as market order@The first|Missing values filled with no quality flag@The second|Adjusted history mixed with unadjusted live prices@And the third"
The first mistake is treating arrival order as market order. The second is silently filling missing values without quality flags. And the third is mixing adjusted historical prices with unadjusted live prices, which makes a split or a dividend look like a price move.

@art freshness-gauge
And keep watching freshness. Stop or degrade trading whenever data freshness exceeds a defined limit. Stale data looks exactly like a quiet market, unless you measure it.

@chapter Try it
@words text="Duplicates · delays · gaps · disorder"
In the lesson's lab, which uses deterministic synthetic educational data with no broker or live market connection, inject duplicates, delays, missing events and out of order messages. Then compare the raw strategy input with the normalized one.

@end text="Break the feed, then normalize it"
You can inject feed problems and compare raw with normalized data, on Learn. That's learn dot get er done dot I O.
