---
format: long
lesson: storage-engines-and-indexes/hash-vs-tree-for-ranges
title: Hash is faster? Only at one operation
thumb: Faster at what?
---

@chapter Faster at what?
@title text="Hash vs Tree for Ranges" sub="Storage Engines and Indexes" art=thumb
A hash index is faster than a B-tree. You've probably heard that. It's true about one operation. On a realistic workload, the hash index can do over a hundred and sixty times the work.

@art hash-bucket
Two kinds of query. A point lookup fetches the row for one exact key. A range query fetches every row between two bounds. A hash index computes a bucket from the key and reads it, one page read, no descent. Under uniform hashing at a sensible load factor, that one is real.

@art scrambled-order
But what the hash spends to get that one is the order of the keys. There's no way to ask a hash index for the keys between two values.

@art full-scan
So a range has no hash plan at all. The planner falls back to scanning the table. A million rows at two hundred rows a page is five thousand page reads. It isn't that a hash is slower at ranges. It has no access path for them.

@chapter The tree
@art tree-descent
A B-tree pays its height on both kinds of query. With a fanout of five hundred over a million rows, five hundred squared is two hundred and fifty thousand, too few, and five hundred cubed is enough. So the height is three, and a point lookup is three reads.

@art leaf-walk
A range descends to the first matching key, then reads leaves in order. That's h minus one internal levels, plus one read per leaf page. A range of a hundred rows fits in one leaf of two hundred. So two plus one, three reads.

@math heading="Four costs, in page reads" items="hash:  point 1,   range 10⁶/200 = 5 000@point one;;tree:  point 3,   range (3 − 1) + ⌈100/200⌉ = 3@point three"
So write down all four. Hash, point one, range five thousand. Tree, point three, range three.

@chapter The mix
@math heading="900 points/s + 100 ranges/s" items="hash = 900(1) + 100(5 000) = 500 900 /s@five hundred thousand nine hundred;;tree = 900(3) + 100(3) = 3 000 /s@three thousand"
Now a workload: nine hundred point lookups and a hundred small ranges a second. Hash: nine hundred, plus a hundred times five thousand, five hundred thousand nine hundred reads a second. Tree: two thousand seven hundred plus three hundred, three thousand.

@words text="167× the I/O, and 3× cheaper at points" sub="both from the same four numbers"
The hash index does a hundred and sixty seven times the work on that mix. And it's genuinely three times cheaper at the one thing it's good at. Both facts come from the same four numbers. Which one you quote is a choice.

@chapter Where they cross
@math heading="Solve for the range rate r" items="900(1) + r(5 000) = 900(3) + r(3)@Set the two totals equal;;r(4 997) = 1 800@eighteen hundred;;r = 1 800/4 997 ≈ 0.360 /s@point three six"
Set the two totals equal and solve for the range rate. Nine hundred plus five thousand r equals two thousand seven hundred plus three r. So r is eighteen hundred over four thousand nine hundred and ninety seven, about point three six a second.

@art balance-tip
One range query every three seconds is enough to make the tree cheaper. Remove the ranges entirely, and the hash wins, nine hundred reads against two thousand seven hundred, exactly one to h. And cache the tree's top two levels, and even that advantage disappears.

@words text="No cache · full pages · contiguous range" sub="what the count assumes"
The count assumes pages hold their nominal number of rows, nothing is cached, and the range is contiguous in key order. The same fact exists in memory, where a hash table can't answer predecessor or ordered iteration at all. On disk, that structural limit becomes a number: five thousand reads.

@chapter Where people slip
@list heading="Common slips" items="Saying one index is faster than another@The first|Counting a range in rows@The second|Expecting a better hash to fix ranges@the third"
The first slip is saying one index is faster, without naming the operation. The second is counting a range in rows, when the device delivers pages. And the third is expecting a better hash to fix the range. Five thousand is rows over rows a page. There's no hash parameter in it.

@chapter Try it
@words text="Ranges of 1 000 rows" sub="first move: tree range = 2 + ⌈1 000/200⌉"
Your turn. Widen the range to a thousand rows. The tree's range cost becomes two plus a thousand over two hundred, rounded up. Recompute both totals, and say which way the crossover moved, and why.

@end text="Name the operation"
You can change the mix and watch the crossover, on Learn. That's learn dot get er done dot I O.
