---
format: short
lesson: algorithmic-and-automated-trading/market-data-ingestion-and-normalization
title: The trade that arrived 7.5 seconds late
---

@art two-clocks
This trade happened at ten fifteen and two seconds. It arrived seven and a half seconds later.

@math items="09.500 − 02.000 = 7.5 s@seven point five;;7.5 s > 5 s limit@five second"
Receive time minus event time is seven point five seconds, over a five second freshness limit.

@words text="Keep it · flag it · stop trading on it"
Keep the record in event order with a quality flag. But flag the feed stale, and hold trading until fresh data arrives.

@end text="Full lesson on Learn"
Break and fix a feed in the full lesson on Learn.
