---
format: long
lesson: capacity-estimation/read-write-ratio
title: Read/write ratio: why 100 to 1 is not one percent writes
thumb: Divide by r plus one
---

@chapter The question
@title text="Read/Write Ratio" sub="Capacity Estimation" art=thumb
A service handles ten thousand requests a second, and the reads outnumber the writes a hundred to one. How many writes is that? If you said a hundred, you're close, and you're also wrong in a way worth fixing.

@art two-paths
One request rate is almost never the number you want, because reads and writes size different parts of a system. Writes size storage, replication and durability. Reads size caches, bandwidth and fan out. So you split the total into two rates.

@chapter Ratio and share
@art ratio-vs-share
A ratio and a share carry the same information, but they're different numbers. A ratio compares the two parts to each other. A share compares one part to the whole. A read write ratio r means reads divided by writes is r, written r to one.

@math heading="Shares from a ratio" items="R = rW,  T = R + W@reads are r;;T = rW + W = (r + 1)W@so the total;;W = T/(r + 1)@the write rate;;R = T·r/(r + 1)@the read rate"
If the write rate is W, the reads are r times W, and the total T is the reads plus the writes. So the total is r plus one, times W. That gives the write rate, T over r plus one, and the read rate, T times r over r plus one.

@words text="the +1 is the writes themselves"
That plus one is the whole lesson. It's the writes themselves, which are part of the traffic being split, not something outside it.

@chapter A worked example
@math heading="r = 100,  T = 10 000 req/s" items="write share 1/101 = 0.990099…%@one over a hundred and one;;read share 100/101 = 99.009900…%@a hundred over a hundred and one;;1/101 + 100/101 = 1  ✓@add to one;;writes 10 000/101 = 99.01 req/s@ninety nine point zero one;;reads 1 000 000/101 = 9 900.99 req/s@nine thousand nine hundred"
At a hundred to one, the write share is one over a hundred and one, and the read share is a hundred over a hundred and one. They add to one, which is the check worth doing. So writes are ninety nine point zero one a second, and reads are nine thousand nine hundred point nine nine.

@art split-bar
Now the instinct. One over r says a hundred writes and nine thousand nine hundred reads. Divide those into each other and you get ninety nine to one, not a hundred to one. That round trip catches the error without needing to remember the formula.

@math heading="How wrong is one over r?" items="r = 100:  (1/100)/(1/101) = 101/100@at a hundred;;r = 2:  says 1/2 is writes, truth is 1/3@at two to one"
The instinct overstates the writes by a factor of r plus one over r. At a hundred to one that's a hundred and one over a hundred, just one percent. But at two to one, it says half the traffic is writes when a third of it is.

@chapter Why one percent matters
@art cache-absorbs
Ninety nine writes a second sounds like noise next to ten thousand. For the read path, it is. But those writes are what accumulates in storage, what replication multiplies, what has to be durable and what a partitioning scheme has to route. A cache can absorb the reads. It can't absorb the writes. Size the storage from the total instead, and you overstate the ingest by a factor of a hundred and one.

@chapter Which window?
@art window-shift
A ratio is measured over a window, and it's a fact about that window. A daily figure of a hundred to one can be five to one during the hour a batch import runs. Sizing cares about the busiest hour, so write down which window your ratio came from.

@art round-trip-check
And treat the ratio as a ranged factor. If it's wrong by three times, the read rate barely moves, but the write rate moves by nearly the same three times.

@chapter Where people slip
@list heading="Common slips" items="Reading 100:1 as 1% writes@The first|Calling the writes negligible@The second|Assuming one ratio all day@The third"
The first slip is reading a hundred to one as one percent writes. The second is treating that one percent as negligible, when it's the rate the rest of the path is about. And the third is assuming one ratio holds all day.

@chapter Try it
@words text="6 000 req/s at 5:1" sub="first move: r + 1 = 6"
Your turn. A service does six thousand requests a second at five to one. The first move is r plus one, which is six. Work out both shares, both rates, and the factor by which one over r would overstate the writes. Say that factor before you check it.

@end text="Split the rate, size both paths"
You can slide the ratio and watch both rates and both shares move, on Learn. That's learn dot get er done dot I O.
