---
format: long
lesson: capacity-estimation/latency-numbers-on-a-log-scale
title: Latency numbers on a log scale: learn the ratios
thumb: One seek, 100 000 reads
---

@chapter The question
@title text="Latency Numbers on a Log Scale" sub="Capacity Estimation" art=thumb
How much slower is a disk than memory? Somewhat slower, people say. The real answer is a hundred thousand times, and the reason people get it wrong is the picture in their heads.

@art ladder-rungs
The operations a system is built from, a cache reference, a memory read, an SSD read, a disk seek, a packet crossing a continent, span a hundred and fifty million to one. These reference latencies are measured figures, quoted to one significant figure and used for estimating.

@list heading="A few rungs" items="L1 cache reference: 1 ns@one nanosecond|Main memory reference: 100 ns@a hundred|SSD random read: 150 000 ns@a hundred and fifty thousand|Disk seek: 10 000 000 ns@ten million|California to the Netherlands: 150 000 000 ns@a hundred and fifty million"
An L1 cache reference is one nanosecond. A main memory reference is a hundred. An SSD random read is a hundred and fifty thousand. A disk seek is ten million. And a packet from California to the Netherlands and back is a hundred and fifty million nanoseconds.

@chapter Exact ratios
@math heading="Memory against a disk seek" items="10 000 000 ns ÷ 100 ns = 100 000@ten million;;10⁵ ≤ 100 000 < 10⁶@between"
Both ends of any ratio from the table are whole numbers, so the ratio is exact. Ten million nanoseconds divided by a hundred is a hundred thousand. A hundred thousand memory references fit inside one disk seek, and that ratio sits between ten to the five and ten to the six.

@words text="If memory took 1 second…" sub="a disk seek would take more than a day"
Said another way: if a memory reference took one second, a disk seek would take rather more than a day.

@art memory-and-disk
That one figure decides more design arguments than any other on this course. It's why an index is worth building, and why a cache is worth having.

@chapter Why the ruler is logarithmic
@art linear-crowd
Draw the table to a linear scale reaching a hundred and fifty million nanoseconds, and the memory reference is less than a millionth of the width. Eleven of the fourteen rungs pile up at the left edge. The picture is honest about the largest number and silent about every comparison worth making.

@art log-ruler
A log ruler puts equal ratios at equal distances. One to ten is the same gap as a million to ten million. That's the right scale, because every question you ask of this table is a ratio question: how many of these fit in one of those.

@chapter Somewhat slower
@math heading="Three comparisons" items="1 MB sequential: disk ÷ SSD = 20@a megabyte;;disk seek ÷ SSD random read = 200/3@a disk seek against;;disk seek ÷ memory reference = 100 000@and a disk seek against a memory"
Somewhat slower is true of one comparison and badly wrong about others. Reading a megabyte sequentially is twenty million nanoseconds from disk and a million from SSD, a ratio of twenty. A disk seek against an SSD random read is two hundred over three. And a disk seek against a memory reference is a hundred thousand. Same two words, three answers.

@art random-vs-sequential
The pattern: sequential work narrows the gaps and random work widens them. So before you say one thing is slower than another, name the operation on each side, then take the ratio.

@chapter Carrying it around
@list heading="Ratios worth keeping" items="100 000 memory references per disk seek@a hundred thousand|300 datacentre round trips per cross-continent one@three hundred|20 sequential MB from SSD per one from disk@twenty"
Keep a few exact ratios. A hundred thousand memory references to a disk seek. Three hundred datacentre round trips to one across a continent. Twenty sequential megabytes from SSD for one from disk. And for anything else, keep the decade bracket, because that's the form that survives new hardware.

@art floor-not-load
These numbers aren't a model of a running system. They're single operations measured alone, with nothing queued behind them. A real disk seek under load takes longer. The ladder is a floor and a set of ratios, and it's honest about being only that.

@chapter Where people slip
@list heading="Common slips" items="Reading the ladder linearly@The first|Memorising figures, not ratios@The second|Thinking the log scale softens it@The third"
The first slip is reading the ladder with a linear intuition. The second is memorising the figures rather than the ratios, since the figures expire first. The third is thinking the log scale softens the comparison. It's the opposite. It's the only scale that shows all fourteen rungs at once.

@chapter Try it
@words text="send 1 kB over 1 Gbit/s ÷ compress 1 kB = ?"
Your turn. Pick two rungs whose ratio you think you know, say sending a kilobyte over a gigabit link against compressing a kilobyte. Write down your guess, the decade bracket you expect, and the design sentence you'd base on it. Then check.

@end text="Pick two rungs, read the ratio"
You can pick any two rungs and read their exact ratio off the ruler, on Learn. That's learn dot get er done dot I O.
