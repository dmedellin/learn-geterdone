---
format: long
lesson: measuring-systems/coordinated-omission
title: Coordinated omission: the outage your load test didn't see
thumb: p99 2 ms, really 990 ms
---

@chapter A p99 of two milliseconds
@title text="Coordinated Omission" sub="Measuring Systems" art=thumb
Your load test ran a hundred requests. One of them hit a one second stall. The p ninety nine came back as two milliseconds. That number is correct arithmetic, and it tells you nothing.

@art closed-loop
Most load generators are closed loops. Send a request, wait for the reply, send the next. It's the obvious way to write one, and it has built in feedback. The slower the system gets, the less load it receives.

@art stall-gap
Set it to send one request every ten milliseconds, against a service that normally answers in two. During a one second stall, it sends nothing at all. So instead of a hundred slow requests, the trace has one.

@math heading="As recorded" items="99 × 2 ms,  1 × 1 000 ms,  n = 100@Ninety nine requests at two;;p99 = rank 99 of 100  →  2 ms@rank ninety nine"
Ninety nine requests at two milliseconds, and one at a thousand. The p ninety nine is rank ninety nine of a hundred, two milliseconds. That's the healthy service time. It's the signature of the bug. The reported p ninety nine is a measurement of the system when nothing was wrong.

@chapter The requests that were due
@art missing-requests
But real arrivals don't wait for you to be ready. The schedule called for a request every ten milliseconds, so ninety nine were due inside the stall and never sent. Each would have waited from the moment it was due until the stall cleared.

@math heading="The k-th missing request" items="due at 10k ms into the stall@ten k milliseconds;;waits 1 000 − 10k ms@a thousand minus;;k = 1 → 990,   k = 50 → 500,   k = 99 → 10@nine ninety"
The k th one was due ten k milliseconds in, and waited a thousand minus ten k. The first waited nine ninety. The fiftieth, five hundred. The ninety ninth, ten.

@art staircase-waits
Put those back. Nothing that was measured changes. You add one entry per request the schedule called for, at the wait it would have had.

@math heading="Corrected,  n = 199" items="p99 = rank ⌈0.99 × 199⌉ = 198  →  990 ms@rank a hundred and ninety eight;;p50 = rank 100  →  10 ms@the median;;990 ÷ 2 = 495@four hundred and ninety five"
Now there are a hundred and ninety nine. The p ninety nine is rank a hundred and ninety eight, nine hundred and ninety milliseconds. Even the median moves, from two to ten. And nine ninety over two is four hundred and ninety five times.

@chapter The fix is a clock
@words text="More threads move the number. They don't remove the bias."
The first reaction is to add threads. But each thread is still a closed loop, and a fault that stalls the whole service stalls all of them at once, which is the case you're measuring.

@art clock-driven
What removes it is generating requests on a clock, not on replies, and timing each from its scheduled start. Through the same stall, a clock driven generator records a hundred slow requests, and its p ninety nine is nine ninety, with no correction. The correction is the missing half of the experiment.

@chapter Open or closed?
@art open-vs-closed
The correction assumes open arrivals, set by something outside the system, like users or a queue. If your workload is genuinely closed, a fixed pool of clients each waiting on its own reply, then those requests really weren't made. Correcting there double counts. Deciding which you have is a judgement the arithmetic can't make.

@words text="Could the fault stop the measurement?"
The same bias turns up outside load tests. A monitoring agent that blocks while its process is stalled. A client library that drops the requests users abandoned. A dashboard that quietly excludes timeouts. Ask one question: could this measurement be prevented by the very fault it's meant to record? If yes, it flatters.

@chapter Where people slip
@list heading="Common slips" items="Believing the generator saw what users would@The first|Adding threads, or dropping the outlier@The second|Correcting a genuinely closed workload@the third"
The first slip is believing the generator saw what users would have seen. The second is fixing it with more threads, or by discarding the slow request, the only evidence the stall happened. And the third is applying the correction to a workload that's genuinely closed.

@chapter Try it
@words text="Stall 200 ms,  interval 50 ms" sub="three due: waits 150, 100, 50 ms"
Your turn. Set the stall to two hundred milliseconds and the interval to fifty, on the same hundred requests. Three requests were due inside the stall, waiting a hundred and fifty, a hundred, and fifty. Predict both p ninety nines, then check, and say why this one is less alarming.

@end text="Time from the schedule"
You can move the stall and the interval and watch the two percentiles split, on Learn. That's learn dot get er done dot I O.
