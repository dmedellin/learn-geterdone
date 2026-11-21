---
format: long
lesson: storage-engines-and-indexes/write-amplification-in-lsm-trees
title: Append-only, and every byte written twenty five times
thumb: Sequential, not few
---

@chapter Append-only isn't cheap
@title text="Write Amplification in LSM Trees" sub="Storage Engines and Indexes" art=thumb
Log structured trees never write randomly. Everything is appended. So they must be cheap to write to, right? They write everything about twenty five times. Append only describes the pattern of the writes, not their number.

@art level-stack
A levelled LSM tree has a small in memory table, the memtable, and then L levels on disk, each F times bigger than the last. Data enters at the top, and compaction merges it down, level by level.

@words text="WA = bytes written ÷ bytes ingested" sub="RA = reads per logical lookup"
Two ratios describe it. Write amplification is the bytes the engine writes to disk for every byte the application hands it. Read amplification is the storage reads one logical lookup does. Both are counts. Neither is a latency.

@chapter Why F over two
@art merge-rewrite
When a run merges into a level, the engine rewrites whatever part of that level overlaps it. So a byte sitting in a level gets rewritten as new data keeps arriving.

@art half-full-cycle
A level spends its life filling from empty to full between merges. Averaged over that cycle, it's about half full, so a byte crossing it is rewritten about F over two times, not F times. That word about matters. Every figure here inherits it.

@math heading="Levelled LSM, fanout F, L levels" items="WA ≈ L · F/2@L times F over two;;RA ≈ L@R A is about L"
So each of L levels rewrites a byte about F over two times, and the total write amplification is about L times F over two. And R A is about L, because a lookup that finds nothing has to try every level.

@chapter A worked example
@math heading="memtable 64 MB,  F = 10" items="L1 640 MB · L2 6.4 GB · L3 64 GB · L4 640 GB · L5 6.4 TB@six hundred and forty megabytes;;1 TB doesn't fit in L4, fits in L5  →  L = 5@doesn't fit in four"
How many levels? That isn't really a setting. With a sixty four megabyte memtable and a fanout of ten, the levels hold six hundred and forty megabytes, then six point four gigabytes, sixty four, six hundred and forty, and six point four terabytes. A terabyte of data doesn't fit in four levels, and fits in five.

@math heading="Ingest 50 MB/s" items="WA = 5 × 10/2 = 25@twenty five;;compaction = 25 × 50 MB/s = 1.25 GB/s@one point two five gigabytes;;RA = 5 probes on a miss@five probes"
So the write amplification is five times five, twenty five. At an ingest of fifty megabytes a second, compaction needs one point two five gigabytes a second, sustained, whether or not anybody is reading. And a miss costs five probes. That factor of twenty five isn't overhead in a loose sense. It's the mechanism that made the writes sequential in the first place.

@art bandwidth-pipes
That's the number nobody quotes. The dashboard says fifty megabytes a second in. The disk sees one point two five gigabytes. Size the device to the first, and it keeps up until compaction falls behind, and then reads get worse too.

@chapter Turning the fanout
@art fanout-dial
Lower the fanout to four. The same terabyte now forces seven levels. Write amplification falls to fourteen, and compaction to seven hundred megabytes a second. But read amplification rises from five probes to seven. Cheaper writes, dearer reads.

@art miss-probes
There's no fanout that improves both. A miss must search every level, because no level can prove a key isn't on another. That read amplification is the one number here you can buy back cheaply, with a Bloom filter.

@words text="Levelled, not tiered · averaged, not peak"
Two caveats. This is levelled compaction. A tiered engine pays about L instead, in exchange for much worse reads. And compaction is bursty. One point two five gigabytes a second is the average the device must sustain.

@chapter Where people slip
@list heading="Common slips" items="Sizing the disk to the ingest rate@The first|Reading append-only as written once@The second|Quoting only the improvement from a lower F@the third"
The first slip is sizing the disk to the ingest rate. The second is reading append only as written once. And the third is lowering the fanout and quoting only the improvement, without the read amplification and the level count.

@chapter Try it
@words text="F = 10,  L = 3" sub="first move: WA = 15"
Your turn. Keep a fanout of ten and set three levels. Write amplification falls to fifteen. Work out the compaction bandwidth at fifty megabytes a second, then read the capacity column. What's the largest dataset three levels can actually hold?

@end text="Sequential, not few"
You can move the fanout and the level count and watch both amplifications, on Learn. That's learn dot get er done dot I O.
