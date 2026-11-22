---
format: short
lesson: algorithmic-and-automated-trading/time-sessions-events-and-scheduling
title: The trading job that runs an hour early every winter
---

@art utc-offset
Your open job runs at thirteen thirty UTC. Every November, it fires an hour early.

@math items="summer: 13:30 UTC = 09:30 New York@In summer;;November: 13:30 UTC = 08:30 New York@in November"
In summer, thirteen thirty UTC is nine thirty in New York, right at the open. But in November, New York is five hours behind UTC, so it's eight thirty.

@words text="Let the calendar carry the offset"
A hard coded offset is right for half the year.

@end text="Full lesson on Learn"
Drift the clock in the full lesson on Learn.
