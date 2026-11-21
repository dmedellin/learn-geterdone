---
format: long
lesson: partitioning-and-load-balancing/range-partitioning-and-hot-ranges
title: Range partitioning: perfectly balanced, and one shard on fire
thumb: One range takes every write
---

@chapter Why ranges
@title text="Range Partitioning and Hot Ranges" sub="Partitioning and Load Balancing" art=thumb
Hashing scatters keys. Sometimes that's exactly what you don't want, because you want to read everything written in the last hour from one place. That's what range partitioning gives you.

@art ordered-ranges
Under range partitioning, the key space is cut into contiguous intervals, and each interval is a shard. Keys that are next to each other stay next to each other. So a scan over an interval only touches the shards whose ranges overlap it.

@chapter The monotonic key
@art write-pointer
Now the common workload that breaks it. Events keyed by arrival time. Rows keyed by an auto increment id. In both, the next key is larger than the last one, so the next write goes to whichever range holds the top of the key space.

@math heading="8 ranges, 2 400 writes, monotonic key" items="each window: 300 writes, all to one range@all three hundred go;;hottest range now = 100.00%@a hundred percent;;ranges taking writes now: 1 of 8@one of the eight"
Split two thousand four hundred writes into windows of three hundred. In every window, all three hundred go to one range. The hottest range takes a hundred percent of the writes happening now, and only one of the eight ranges is taking any writes at all.

@words text="There is no N in 100%" sub="16 ranges: still one takes everything"
And there's no N in that hundred percent. Sixteen ranges, and one takes every write. Four ranges, same. Split the hot range, and the write pointer moves into one half, which then takes everything.

@chapter Why nobody notices
@art moving-hotspot
The hot range doesn't stay put. As the key space advances, it moves on to the next range, and the next.

@art flat-histogram
So by the end of the run, every range has taken three hundred of the two thousand four hundred, twelve and a half percent, an exactly equal share. The lifetime histogram is perfectly flat. Look at writes per shard over the last few minutes instead, and you see one shard at a hundred percent and seven idle.

@chapter Hash it, and pay on reads
@art hashed-spread
Hash the key, and the writes spread. The hottest range takes sixteen percent of a window against an equal twelve and a half, one point two eight times a fair share instead of eight. But a scan of one window now reads all eight ranges instead of one.

@words text="The same property, two directions" sub="write hotspot ↔ cheap scan"
The write hotspot and the cheap scan are the same property, seen from two directions. And notice even hashing doesn't hit an equal share. Sixteen percent against twelve and a half is the ordinary imbalance of hashing.

@chapter The dial in between
@art bucket-dial
There's a middle setting. Put a hashed bucket in front of the timestamp. With four buckets, the hottest range takes thirty point three three percent of the current writes, and a one window scan reads four ranges of eight. The bucket count is a dial between write balance and read fan out.

@math heading="Three key designs, 8 ranges" items="monotonic:  hottest now 100.00%,  scan 1 of 8@monotonic;;hashed:  hottest now 16.00%,  scan 8 of 8@hashed;;4 buckets + time:  hottest now 30.33%,  scan 4 of 8@four buckets"
Side by side: monotonic, a hundred percent hot and a scan of one. Hashed, sixteen percent and a scan of all eight. Four buckets, thirty point three three percent and a scan of four. Over the whole run, all three look within a point or two of an equal twelve and a half.

@chapter Where people slip
@list heading="Common slips" items="Diagnosing from a lifetime histogram@The first|Expecting more shards or a split to fix it@The second|Hashing without pricing the scans@the third"
The first slip is diagnosing a hot range from a lifetime histogram. The second is expecting more shards, or a split, to fix it. It's a property of the key. And the third is hashing the key without pricing the ordered reads you just turned into requests to every shard.

@words text="Hot range ≠ hot key"
One caution. A hot range is a busy region of the key space. A hot key is one single busy key, and no partitioning function spreads that. That's the next lesson.

@chapter Try it
@words text="Monotonic key, 32 ranges" sub="first move: equal share = 1/32 = 3.125%"
Your turn. Keep the monotonic key and take the ranges from eight to thirty two. An equal share is one thirty second, three point one two five percent. Predict the hottest range's share of the current window, its share over the whole run, and the multiple of an equal share. Which one moved when N did?

@end text="Watch the window, not the run"
You can switch key designs and watch both columns, on Learn. That's learn dot get er done dot I O.
