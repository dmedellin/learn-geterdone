---
format: short
lesson: latency-and-the-tail/latency-is-not-throughput
title: Why doubling your bandwidth saved two milliseconds
---

@art same-forty
Doubling your bandwidth can save almost nothing. Here's the arithmetic.

@math items="64 kB at 100 Mbit/s, 80 ms: 85.12 ms@sixty four kilobytes;;double bandwidth: saves 2.56 ms@double the bandwidth;;halve RTT: saves 40 ms@halve the round trip"
Sixty four kilobytes over a hundred megabits with an eighty millisecond round trip takes eighty five point one two milliseconds. Double the bandwidth and you save two point five six. Halve the round trip and you save forty.

@words text="Small transfers pay for the round trip"
Well below a megabyte on this link, you're paying for the round trip, not the bandwidth.

@end text="Full lesson on Learn"
The full lesson, with both upgrades priced, is on Learn.
