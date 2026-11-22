---
format: short
lesson: algorithmic-and-automated-trading/observability-logging-and-auditability
title: Read the trace before you blame the broker
---

@art trace-spans
Your order took three hundred and nineteen milliseconds. Was it the broker?

@math items="20 + 17 + 240 + 18 + 24 = 319 ms@twenty plus;;excess 220 ms, all in the strategy@two hundred and twenty"
The trace reads twenty plus seventeen plus two hundred and forty plus eighteen plus twenty four. The normal total is ninety nine, and the extra two hundred and twenty is all in the strategy span.

@words text="Open the span that grew"
The broker's twenty four was normal.

@end text="Full lesson on Learn"
Trace an incident in the full lesson on Learn.
