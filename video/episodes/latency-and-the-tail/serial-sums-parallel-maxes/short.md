---
format: short
lesson: latency-and-the-tail/serial-sums-parallel-maxes
title: The optimisation that saved zero milliseconds
---

@art slack-gap
You made a stage instant, and the request got no faster at all.

@math items="enrich 22 → 1 ms@twenty two;;total: 92 → 92 ms@ninety two"
In this request, enrich runs beside the database, and finishes thirty three milliseconds before render needs it. Take it from twenty two milliseconds to one, and the total stays at ninety two.

@words text="Off the critical path, speed buys nothing"
Only stages on the longest path count. Everything else has slack.

@end text="Full lesson on Learn"
The full lesson, with every stage on a slider, is on Learn.
