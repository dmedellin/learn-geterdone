---
format: long
lesson: replication-and-consistency/physical-clocks-and-drift
title: Clock drift: why timestamps can't order events five milliseconds apart
thumb: A timestamp is an interval
---

@chapter The question
@title text="Physical Clocks and Drift" sub="Replication and Consistency" art=thumb
Two events on two machines, five milliseconds apart. Compare their timestamps and you'll know which came first? Not if the clocks can be twelve milliseconds apart. Here's where that twelve comes from.

@art drifting-clock
Drift is the rate a clock departs from true time, quoted in parts per million. A time daemon corrects it periodically, which bounds the error and restarts the accumulation. But between corrections, the drift resumes at the same rate. Synchronised clocks sit within a window. They don't agree.

@chapter The window
@math heading="Drift 200 ppm, corrected every 30 s" items="200 ppm = 200 µs per second@two hundred microseconds;;ε = 200 µs/s × 30 s = 6000 µs = 6 ms@six milliseconds;;2ε = 12 ms"
Parts per million is exactly microseconds per second. So two hundred parts per million is two hundred microseconds a second. Over thirty seconds, one clock can be six thousand microseconds out, six milliseconds, just before the next correction.

@art two-clocks-apart
And ordering always compares two clocks. One can be six fast while the other is six slow. So the uncertainty window is two epsilon, twelve milliseconds. Use one clock's error as the window, and you've halved the margin.

@chapter Two levers
@list heading="200 ppm, other intervals" items="every 1 s:  2ε = 400 µs@every second|every 10 s:  2ε = 4 ms@every ten|every 600 s:  2ε = 240 ms@every ten minutes"
The window is linear in both inputs. Correct every second, and two epsilon is four hundred microseconds. Every ten seconds, four milliseconds. Every ten minutes, two hundred and forty milliseconds.

@art cheap-lever
Halving drift means better oscillators in every machine. Halving the interval means twice the sync traffic, and it's nearly free. That's why tight clock systems synchronise aggressively, until the network round trip becomes the floor.

@art sawtooth-short
Take the same two hundred part per million clocks and correct them every second instead of every thirty. The window shrinks thirty fold, from twelve milliseconds to four hundred microseconds. Now a five millisecond gap sits comfortably outside it, and the timestamps can order those two events. Synchronisation traffic is cheap. Oscillators are not.

@chapter No order to read
@math heading="X and Y, truly 5 ms apart" items="true separation 5 ms@five milliseconds;;window 12 ms@the window;;12/5 = 2.4×@two point four"
Two events, X and Y, truly five milliseconds apart. The window is twelve, two point four times the gap.

@art overlapping-intervals
So the timestamps can say X first, Y first, or the same instant. And every one of those readings is consistent with the true order. If node one is fast and node two is slow, X reads first. Swap them, and Y reads first.

@words text="Answers instantly, and wrongly when it's close"
A timestamp comparison answers instantly, and it answers wrongly whenever the answer was close. That's exactly the case anyone asks about, because two events far apart in time are rarely in dispute. The failure is silent, data dependent, and absent on one machine, which is where the code was tested.

@chapter The commit-wait
@math heading="Wait 2ε before making a commit visible" items="wait 12 ms per dependent commit@twelve milliseconds;;1000/12 ≈ 83 commits a second, serially@eighty three"
One repair is to hold each commit for two epsilon before making it visible. Then the window has closed, and any commit a reader sees really did happen first. The price is twelve milliseconds per dependent commit, so a chain is capped near eighty three a second, however fast the hardware.

@art interval-wait
Halve the sync interval, and that cap doubles. So a team that wants more dependent commits is really asking for a tighter clock. Either carry the uncertainty explicitly, as an interval, and wait when intervals overlap. Or use the logical clocks from the last two lessons, which cost messages instead of milliseconds.

@chapter Where people slip
@list heading="Common slips" items="Believing a time sync makes clocks equal@The first|Using ε where the window is 2ε@The second|Comparing raw timestamps across machines@The third"
The first slip is believing a time sync makes clocks equal. Design with the error just before a correction. The second is using epsilon where the window is two epsilon. The third is comparing two machines' raw timestamps at all. A timestamp from another machine is an interval wearing the costume of a point.

@chapter Try it
@words text="50 ppm, every 30 s" sub="ε = 50 × 30 = 1500 µs"
Your turn. New clocks at fifty parts per million, still corrected every thirty seconds. Epsilon is fifteen hundred microseconds. Work out two epsilon, whether the five millisecond gap is now resolvable, and the commit wait ceiling.

@end text="Set drift and sync, read the window"
You can set the drift and sync interval and see which gaps a timestamp can order, on Learn. That's learn dot get er done dot I O.
