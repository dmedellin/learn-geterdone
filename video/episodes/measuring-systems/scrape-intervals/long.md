---
format: long
lesson: measuring-systems/scrape-intervals
title: Scrape intervals: the fourteen second outage your graph can't show
thumb: What falls between the reads
---

@chapter A sample of an instant
@title text="Scrape Intervals" sub="Measuring Systems" art=thumb
Your graph is flat, so nothing happened. That's what it looks like. At the usual fifteen second scrape interval, a fourteen second outage can leave no trace at all.

@art scrape-ticks
A monitoring system reads a target's metrics every I seconds, the scrape interval. For a gauge, the value recorded is the one in effect at that instant. Whatever happened in between isn't averaged or maximised. It's absent. The line between two reads is something your plotting library drew.

@chapter Catching a spike
@art spike-between
So a spike shorter than the interval is caught only if a read happens to land inside it. If it starts at a random moment relative to the scrape clock, the chance is the fraction of the cycle it covers.

@math heading="Spike of length d,  interval I" items="P(caught) = min(1, d/I)@d over I;;I = 15 s,  d = 3 s:  3/15 = 1/5 = 20%@one time in five"
That's d over I, capped at one. At fifteen seconds, a three second spike is seen one time in five. Four spikes in five leave no trace.

@math heading="Longest spike that can hide" items="I − 1 s,  at one-second resolution@I minus one;;I = 15 s → 14 s,   I = 60 s → 59 s,   I = 1 s → 0 s@fourteen seconds"
And the longest spike that can fall entirely between two reads is I minus one seconds. At fifteen, that's fourteen seconds. At sixty, fifty nine. At one second, nothing can hide. The graph isn't lying. It's reporting every value it was given.

@art spike-caught
Shorten the interval to five seconds, and a three second spike is caught three times in five. Better, but not detection. And every extra read is more samples per series to store.

@chapter One run isn't the probability
@words text="Expected 2.4 of 12 caught" sub="a seeded run catches some integer near it"
The lab draws twelve spikes across five minutes. You'd expect to catch two point four. A real run catches some whole number near that. Reseed and it changes. The probability doesn't. One afternoon of monitoring is one draw.

@art phase-locked
And the uniform start is the assumption. A spike made by something on its own clock, a cron job, a flush every sixty seconds, has a fixed phase. Then the chance isn't d over I. It's zero or one, permanently. If a graph looks suspiciously flat, try an interval that doesn't share a factor with the job.

@chapter A counter that reset
@art counter-reset
The interval hides something else. Counters only go up, so rates come from differencing two reads. A process restart sets the counter to zero, between reads, where nothing sees it. The only evidence is that the number went down.

@math heading="40/s,  read every 15 s,  restart at 152 s" items="t = 150:  6 000,   t = 165:  520@six thousand;;naive:  (520 − 6 000)/15 = −365.33/s@minus three sixty five;;corrected:  520/15 = +34.67/s@thirty four point six seven;;lost:  40 × 2 = 80 increments@eighty increments"
A counter climbing at forty a second reads six thousand at a hundred and fifty seconds. The process restarts at a hundred and fifty two, and the next read is five hundred and twenty. Naively, that's minus three sixty five point three three a second. Treat a decrease as a restart, take the new read, and you get thirty four point six seven. The eighty increments between the last read and the restart are gone for good.

@words text="34.67 + 5.33 = 40"
That residual is known. Eighty over fifteen is five point three three. And if the counter had already climbed past its old reading by the next scrape, the restart would be invisible. The big negative number is the friendly case.

@chapter Prefer counters
@art counter-vs-gauge
For anything you mustn't miss, prefer a counter to a gauge. A counter accumulates between reads, so a burst of errors in the gap still shows in the next difference. A gauge just loses it.

@chapter Where people slip
@list heading="Common slips" items="Reading a flat graph as a quiet system@The first|Assuming a shorter interval solves it@The second|Letting a negative rate through@the third"
The first slip is reading a flat graph as a quiet system. The second is assuming a shorter interval solves it. And the third is letting a negative rate reach an average or an alert. Decide the restart rule up front.

@chapter Try it
@words text="I = 10 s,  d = 4 s,  restart at 96 s" sub="first move: 2/5, and 9 s can hide"
Your turn. Set the interval to ten seconds, the spike to four, and the restart to ninety six. The catch probability is two fifths, and nine seconds can hide. Predict the two counter reads around the restart and both rates, then check.

@end text="Compute d over I first"
You can move the interval and the spike and watch what the scrapes miss, on Learn. That's learn dot get er done dot I O.
