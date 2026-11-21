---
format: long
lesson: storage-engines-and-indexes/the-write-cost-of-an-index
title: Three indexes cost seventy five percent of your writes
thumb: Divide by k plus one
---

@chapter Every insert touches every index
@title text="The Write Cost of an Index" sub="Storage Engines and Indexes" art=thumb
Indexes make reads fast. What do they cost? Not bytes. A share of your write throughput, and a bigger share than most people guess.

@art insert-fanout
An index has to contain the column it answers questions about. So when you insert a row, it goes into the table, and a key goes into each of the k indexes. That's k plus one writes per insert. Nothing about clever or bad index design. It's what an index is.

@art scattered-pages
And those writes are random. Each index is ordered on a different key, so where an insert lands in one says nothing about where it lands in another. An insert that's perfectly sequential in the table is k scattered page writes elsewhere. That's the seek cost of random reads, arriving on the write side. So the cost is k plus one random writes, not k plus one small bytes.

@math heading="k indexes,  device D random writes/s" items="writes per insert = k + 1@k plus one random writes;;inserts/s = D / (k + 1)@D over k plus one;;share = 1 / (k + 1)@one over k plus one"
So each insert is k plus one random writes. On a device that sustains D random writes a second, inserts run at D over k plus one, and the share you keep is one over k plus one. Use the device's random write figure, not its sequential one. They can differ by two orders of magnitude.

@chapter It divides
@math heading="D = 10 000 random writes/s" items="k = 0:  10 000 /s   100%@no indexes;;k = 1:  5 000 /s   50.0%@one index;;k = 2:  3 333 /s   33.3%@two;;k = 3:  2 500 /s   25.0%@three"
Take a device doing ten thousand random writes a second. With no indexes, ten thousand inserts. One index, five thousand, half. Two, three thousand three hundred and thirty three. Three, two thousand five hundred, a quarter.

@art divided-bar
So three indexes don't cost thirty percent. They cost seventy five percent. Three quarters of the write budget is now spent keeping indexes correct. The device didn't get slower, and the rows didn't get bigger.

@art share-curve
Read it as a curve, and the first index is the expensive one. It costs fifty percentage points. The second costs about seventeen, the third about eight, the fourth five. One over k plus one falls fastest at the start.

@words text="“One more won't hurt”" sub="true, except at k = 0"
So anyone who said one more index won't hurt was right, for a reason that stops applying at zero.

@chapter From a target to a budget
@math heading="Target T inserts/s" items="most indexes = ⌊D / T⌋ − 1@floor of D over T;;T = 2 500:  ⌊4⌋ − 1 = 3@two thousand five hundred;;T = 3 000:  ⌊3.33⌋ − 1 = 2@three thousand"
Run it backwards. If you need T inserts a second, the most indexes you can afford is the floor of D over T, minus one. At two thousand five hundred, that's three. Raise the target twenty percent, to three thousand, and it's two.

@art floor-steps
It's a floor, so it moves in whole indexes. Between the steps, a target can move a long way for free. At a step, a small change costs a whole index.

@chapter The unused index
@art unused-index
A query planner can choose not to use an index. The writer has no such choice, because an index that skipped an insert would be wrong. An index added years ago for a report nobody runs is still one of the k, on every insert. Dropping it is the only thing that takes it out of the count.

@words text="k + 1 index pages, written eventually"
One caveat. Engines that buffer index updates turn some of these random writes into sequential ones, later. The k plus one is the count of pages that must eventually be written. When, and how many times, is a separate question.

@chapter Where people slip
@list heading="Common slips" items="Counting an index's cost in bytes@The first|Believing an unused index is free@The second|Subtracting a percentage instead of dividing@the third"
The first slip is counting an index's cost in bytes. The second is believing an unused index is free. And the third is treating k plus one as a small penalty to subtract, when it divides.

@chapter Try it
@words text="D = 6 000 /s,  T = 1 000 /s" sub="first move: ⌊6 000/1 000⌋ − 1"
Your turn. A device doing six thousand random writes a second, and a workload that needs a thousand inserts. The answer is a floor, six thousand over a thousand, minus one. Work it out, then the insert rate you actually get at that many indexes, and the headroom left.

@end text="Price indexes in writes"
You can add indexes and watch the insert rate divide, on Learn. That's learn dot get er done dot I O.
