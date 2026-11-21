---
format: long
lesson: geometric-algorithms/the-sweep-line-and-the-work-it-does-not-save
title: The sweep line: when it saves work, and when it saves none
thumb: Six tests out of six
---

@chapter The promise
@title text="The Sweep Line and the Work It Does Not Save" sub="Geometric Algorithms" art=thumb
A sweep line is supposed to save you from testing every pair of segments. Often it does. On one simple input, it saves nothing at all, and that's just as worth knowing.

@chapter How the sweep works
@art sweep-events
Take k segments. Their two k endpoints are the events, sorted by x, each marked as a start or an end. A vertical line sweeps left to right, stopping at each event.

@art status-list
As it goes, it keeps a status list: the segments it's currently crossing. On a start event, the new segment is tested against everything on the list, then added. On an end event, its segment is removed.

@words text="work = Σ status-list size at each start"
So the work isn't the number of events. Each start event makes as many pair tests as there are segments already on the list. The total is the sum of those list sizes, which is exactly what the lab's event table shows, column by column.

@chapter Why it can't miss
@words text="crossing at x*  ⟹  both on the list at x*"
Why is that correct? If two segments cross at some x, both are on the sweep line at that x. Whichever starts later finds the other already on the list, so that pair gets tested. Ties at the same x put starts before ends.

@words text="correct ≠ cheaper"
Notice what that proof doesn't claim. It says the sweep tests enough pairs. It doesn't say it tests fewer. Those are separate questions, and only the second depends on the input.

@chapter An input it likes
@art spread-pairs
Six segments strung along the x axis in three separated pairs. Segments whose x ranges never overlap are never on the line together, so they're never tested.

@math heading="Spread out" items="6 segments,  12 events@six segments;;3 pair tests  vs  15 pairs@three pair tests;;3 crossings@three crossings"
The lab reports six segments, twelve events, three pair tests against fifteen pairs, and three crossings found. Twelve pairs were skipped, and none of them could have crossed. On this input the list never holds more than two.

@words text="checked against every pair, every redraw"
Is that answer trustworthy? The lab doesn't assume so. On every redraw it re tests every pair the slow way and compares the two crossing sets. The saving is always in the work, never in the answer.

@chapter An input it doesn't
@art crossing-bundle
Now four segments: two diagonals, a horizontal and a vertical, all spanning the same square from zero, zero to eight, eight. Every one of them crosses the middle.

@math heading="All crossing" items="4 segments,  8 events@four segments;;6 pair tests  vs  6 pairs@six pair tests;;status list reaches 4@reaches four"
The lab reports four segments, eight events, six pair tests against six pairs, and six crossings. The status list reaches four, holding everything at once. The sweep did every test the brute force would, and paid for a sort on top.

@art tangle
The status line says so, in amber, rather than hiding it. This is the input that stops three out of fifteen being read as a bound. The more the segments tangle, the more of them sit on the line together, and the more each start event has to test.

@words text="O((k + I) log k)" sub="I = Θ(k²)  ⟹  no better than quadratic"
Nothing went wrong. The answer's right. The general bound is order k plus I, times log k, for k segments and I intersections. When I grows like k squared, as it does here, that's no better than quadratic.

@chapter Shared endpoints
@art staircase
A staircase of four segments, each ending where the next begins, has three shared endpoints. This kit counts a shared endpoint as a crossing, because a shared point is a meeting. So the lab reports three crossings, and the brute force agrees. Starts before ends at equal x keeps the sweep consistent with that choice.

@chapter Where people slip
@list heading="Common slips" items="Quoting tests skipped as the behaviour@The first|Confusing events with work@The second|Leaving the endpoint convention implicit@And the third"
The first slip is quoting three instead of fifteen as how the sweep behaves. It's a measurement of six segments. The second is confusing events with work. Events are always two k. The work is the sum of the status list sizes at start events. And the third is leaving the shared endpoint convention unstated.

@end text="The saving is in the input"
Run both inputs and read the event table on Learn. That's learn dot get er done dot I O.
