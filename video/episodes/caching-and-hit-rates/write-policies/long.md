---
format: long
lesson: caching-and-hit-rates/write-policies
title: Write-through vs write-back, counted on a real trace
thumb: Fewer writes, bytes at risk
---

@chapter The question
@title text="Write Policies" sub="Caching and Hit Rates" art=thumb
Should your cache send every write straight to the database, or hold them and send them later? People say write back is faster. Sometimes it is. Here's how to count exactly when, and what it costs.

@chapter Two policies
@art write-through
Under write through, every write goes to the cache and to the backend before it's acknowledged. The backend's write rate equals the application's. Nothing ever lives only in the cache, so a crash loses nothing. The cost is that the backend sees every single write.

@art write-back
Under write back, a write goes to the cache, is marked dirty, and is acknowledged. Dirty entries are written to the backend on a periodic flush. So repeated writes to the same key inside one flush collapse into one backend write.

@words text="coalescing ratio = writes ÷ distinct keys" sub="counted per flush window"
That gives a coalescing ratio: the number of writes, divided by the distinct keys written, counted per flush window. It's one when every write is to a different key, and it's the window length when they're all to the same key.

@chapter Count it off a trace
@art flush-windows
Take the trace A, B, A, C, A, then B, A, D, A, B, at a thousand writes a second, with four kilobyte objects, flushing every five writes. Each flush window sends its distinct keys to the backend once, however many times each was written.

@math heading="Flush every 5" items="window 1:  A B A C A  →  {A, B, C} = 3@the first window;;window 2:  B A D A B  →  {A, B, D} = 3@the second;;10 writes → 6 backend writes@ten writes;;ratio 10/6 = 5/3 · 1 000 → 600 writes/s@five thirds"
The first window has five writes but three distinct keys. The second has five writes and three distinct keys again. So ten writes become six backend writes. That's a ratio of five thirds, and the backend sees six hundred writes a second instead of a thousand.

@math heading="What's at risk" items="peak dirty set 3 keys × 4 kB = 12.00 kB@three keys;;held for 5 writes ÷ 1 000/s = 5.0 ms@five milliseconds"
But whatever is dirty when the process dies is gone. The largest dirty set is three keys, at four kilobytes each, so twelve kilobytes. It's held for one flush interval, five writes at a thousand a second, which is five milliseconds. Use the peak, not the average, because a crash takes whatever is dirty at that moment.

@chapter Widen the window
@math heading="Flush every 10" items="one window:  {A, B, C, D} = 4@four distinct;;ratio 10/4 = 5/2 · 400 writes/s@five halves;;at risk 4 × 4 kB = 16.00 kB over 10.0 ms@sixteen kilobytes"
Now flush every ten writes. The whole trace is one window with four distinct keys. The ratio becomes five halves, and the backend sees four hundred writes a second. But the dirty set grows to sixteen kilobytes, held for ten milliseconds.

@art trade-scale
Both ends moved together. Two hundred more writes a second off the backend, and more bytes at risk for longer. A proposal that mentions only the first number isn't a proposal.

@chapter What the trace decides
@art distinct-trace
The ratio belongs to the workload, not the policy. On A through J, every key different, write back coalesces nothing. It sends ten writes, exactly like write through, and still carries the loss window. One key written ten times, though, gives a ratio of five.

@words text="Write-back is faster… on repeated writes" sub="run your own trace first"
So write back is faster isn't a general claim. It's a claim about a workload that repeats writes to the same keys inside a flush interval. If you don't have that, it's a loss window with no gain.

@art fleet-risk
And five milliseconds sounds negligible, until you multiply it by the number of processes you run and the number of times a year each one dies. Whether that's acceptable is a durability question.

@chapter Where people slip
@list heading="Common slips" items="Believing write-back is free@The first|Counting distinct keys over the whole trace@The second|Assuming a ratio the workload doesn't have@The third"
The first slip is believing write back is free. Name the peak dirty set and the exposure time. The second is counting distinct keys over the whole trace. Coalescing is per window, so a key written in two windows is written twice. The third is assuming a ratio your workload doesn't have.

@chapter Try it
@words text="A B C D E F G H I J" sub="flush every 5"
Your turn. Run A through J at a flush of five. Count the distinct keys in the first window before anything else. Then give the ratio, the backend write rate, the bytes at risk, and one sentence on what write back bought you.

@end text="Try the trace that coalesces nothing"
You can run your own write trace and watch which writes coalesce away, on Learn. That's learn dot get er done dot I O.
