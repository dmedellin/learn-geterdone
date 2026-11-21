---
format: short
lesson: latency-and-the-tail/packet-loss-and-throughput
title: Your 10 gigabit link, and the 1 megabit transfer
---

@art thin-stream
A ten gigabit link. Your copy runs at a little over one megabit a second. Why?

@math items="(MSS / RTT) × 1/√p@the segment size;;1460 B, 100 ms, 1%:  1.168 Mbit/s@one point one six eight"
One TCP flow is bounded by the segment size over the round trip, times one over the square root of the loss rate. At fourteen sixty bytes, a hundred milliseconds and one percent loss, that's one point one six eight megabits a second.

@words text="The link rate isn't in the formula"
The link capacity doesn't appear at all. You need more flows.

@end text="Full lesson on Learn"
The full lesson, with the loss on a slider, is on Learn.
