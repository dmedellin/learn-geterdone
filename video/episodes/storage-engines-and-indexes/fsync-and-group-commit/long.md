---
format: long
lesson: storage-engines-and-indexes/fsync-and-group-commit
title: fsync and group commit: durability is a count
thumb: Durability is a count of fsyncs
---

@chapter A write isn't safe yet
@title text="fsync and Group Commit" sub="Storage Engines and Indexes" art=thumb
When a write call returns successfully, is your data safe? No. It's in the page cache, which is memory, which is exactly what a power cut empties.

@art page-cache-gap
A write is durable when it survives losing power. fsync is the call that forces buffered bytes onto the device and returns when they're there. So every engine that promises durability is paying for fsyncs, and the count of them is the whole budget.

@math heading="Ceilings" items="one commit per fsync:  ≤ 1 / t_fsync@one over the fsync time;;grouped B at a time:  ≤ B / t_fsync@B over the fsync time"
Without grouping, the durable write rate is at most one over the fsync time. Group B commits behind a single fsync, and it's at most B over the fsync time. Both are ceilings, not achieved rates.

@chapter One per fsync
@art one-per-fsync
Take a ten millisecond fsync. One over point oh one is a hundred durable writes a second. That's it, whatever the CPU and the network could have done.

@art growing-backlog
Now send five thousand writes a second at it. Arrivals at five thousand, served at a hundred, a utilisation of fifty. There's no mean latency to quote. The backlog just grows without bound. The ceiling shows up as a queueing fact, the same M M one model as before, rather than as an assertion.

@chapter Group commit
@art grouped-batch
Group commit collects B pending commits, writes them, calls fsync once, and acknowledges all of them together. Nothing says one commit must get one fsync, and on the same disk this is the only lever that raises the ceiling without new hardware.

@math heading="B = 64,  λ = 5 000 /s,  t_fsync = 10 ms" items="ceiling = 64 / 0.01 = 6 400 /s@six thousand four hundred;;fsync per write = 0.01 / 64 = 156.3 µs@a hundred and fifty six;;fill wait = (64 − 1) / (2 × 5 000) = 6.30 ms@six point three;;ρ = 5 000 × 0.01 / 64 = 0.781@point seven eight one;;queue + fsync = 1 / (100 − 78.125) = 45.71 ms@forty five point seven one"
At sixty four a batch, the ceiling is six thousand four hundred, and each write carries a hundred and fifty six point three microseconds of fsync. But a write waits for its batch to fill, about six point three milliseconds. Batches arrive at seventy eight point one two five a second against a hundred, so utilisation is point seven eight one, and the queue and fsync take forty five point seven one milliseconds.

@words text="Commit latency = 6.30 + 45.71 = 52.01 ms"
Add them, and commit latency is fifty two point oh one milliseconds.

@chapter The curve has a bottom
@art two-waits
So there are two waits, moving opposite ways. The fill wait grows in a straight line with B. The queue in front of the fsync shrinks, because bigger batches arrive less often. Add the two, and you get a curve with its lowest point somewhere in the middle.

@math heading="Scanning B" items="B = 64:  6.30 + 45.71 = 52.01 ms@sixty four;;B = 121:  12.00 + 17.04 = 29.04 ms  lowest@a hundred and twenty one;;B = 256:  25.50 + 12.43 = 37.93 ms@two hundred and fifty six"
Scan it. Sixty four, fifty two point oh one milliseconds. A hundred and twenty one, twelve plus seventeen point oh four, twenty nine point oh four, the lowest. Two hundred and fifty six, thirty seven point nine three. Past the minimum, the batch itself is the problem.

@art u-curve
Meanwhile the ceiling rose the whole way, to twenty five thousand six hundred a second. So if you only looked at throughput, you'd choose the largest batch, and pay thirty seven point nine three milliseconds instead of twenty nine point oh four. The lab finds the minimum by evaluating every B. A closed form for this kind of bargain exists, the E O Q formula on the Operations Research path.

@words text="Measure t_fsync. Don't read it off a datasheet."
One warning. A device with a volatile write cache can acknowledge an fsync before the data is really there. It reports a lovely figure and loses your commits anyway. Measure it.

@chapter Where people slip
@list heading="Common slips" items="Reading a successful write() as durability@The first|Quoting the grouped ceiling without the latency@The second|Raising B until throughput is enough, and stopping@the third"
The first slip is reading a successful write as durability. The second is quoting the grouped ceiling as if latency were unchanged. And the third is raising B until throughput is enough and stopping, when the latency minimum is in the middle.

@chapter Try it
@words text="λ = 5 000 /s,  t_fsync = 1 ms" sub="first move: ceiling 1 000 /s"
Your turn. Keep five thousand writes a second, and take the fsync down to one millisecond. The ungrouped ceiling is now a thousand. Find the batch that minimises commit latency, the latency there, and compare both with the ten millisecond device.

@end text="Count the fsyncs"
You can scan the batch size and watch the two waits trade, on Learn. That's learn dot get er done dot I O.
