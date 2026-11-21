---
format: long
lesson: replication-and-consistency/sloppy-quorums
title: Sloppy quorums: exactly how often a read misses the write
thumb: R + W = N misses 1 in 3
---

@chapter The question
@title text="Sloppy Quorums and the Miss Probability" sub="Replication and Consistency" art=thumb
Users save a value and sometimes see the old one come back. How often is sometimes? When your quorums don't overlap, you can count it exactly. And the configuration that looks like the boundary of safe is wrong one time in three.

@art untouched-nodes
When R plus W is at most N, there's no overlap guarantee. That's a sloppy quorum. The write reached W nodes, and left the other N minus W without it. A read misses if every node it consults is one of those.

@chapter Counting misses
@math heading="Miss probability" items="read sets in total = C(N, R)@possible read sets;;read sets that miss = C(N − W, R)@untouched nodes, and;;P(miss) = C(N − W, R) / C(N, R)@the miss probability"
There are N choose R possible read sets. A read set misses when all R of its members come from the N minus W untouched nodes, and there are N minus W choose R of those. So the miss probability is the ratio. An exact fraction.

@words text="R + W > N  ⟹  C(N − W, R) = 0"
And when R plus W is greater than N, there are fewer untouched nodes than R, so the numerator is zero. That's the overlap theorem, arrived at by counting. Same statement.

@art uniform-draw
One assumption. The formula treats every read set as equally likely, which is what a coordinator choosing at random does. A coordinator that always prefers the nearest or least loaded node has a different number, possibly zero, possibly one.

@chapter Three nodes
@math heading="N = 3" items="R = 1, W = 1:  C(2,1)/C(3,1) = 2/3@one and one;;R = 2, W = 1:  C(2,2)/C(3,2) = 1/3@two and one;;R = 1, W = 2:  C(1,1)/C(3,1) = 1/3@one and two;;R = 2, W = 2:  C(1,2)/C(3,2) = 0@two and two"
On three nodes, one and one misses two reads in three. Two and one misses one in three. So does one and two. And two and two misses none, because R plus W is four.

@chapter Five nodes
@math heading="N = 5" items="R = 1, W = 1:  4/5 = 80%@eighty percent;;R = 2, W = 2:  3/10 = 30%@misses thirty;;R = 2, W = 3:  1/10 = 10%@ten percent;;R = 3, W = 3:  0@three and three"
On five nodes, one and one misses eighty percent. Two and two misses thirty. Two and three, R plus W equals N, misses ten percent. And three and three misses none. Notice that the sloppy rows never reach zero on their own.

@art edge-not-safe
So R plus W equals N is never zero. It gets better as N grows, a third at three nodes, a tenth at five, which is why it survives in production long enough to be believed in. 

@art one-more-node
And the step from the last sloppy row to the first overlapping one is always a single node, on either path. One more in R or in W is nearly always cheaper than the incident it prevents. Equal isn't nearly greater.

@chapter What a miss means
@art not-lost
A miss doesn't mean the write was lost. It's sitting safely on W nodes, and repair will spread it. A read a second later will probably find it. The miss probability is about the moment before that happens. Confusing the two turns a staleness problem into a durability panic.

@art read-chase
So a sloppy quorum is a bet that reads rarely follow writes closely. That's sometimes right, for analytics, or a feed nobody rereads at once. It's catastrophic for anything a user writes and then looks at.

@chapter Two repairs
@list heading="N = 3, R = 1, W = 1" items="2/3@two thirds|raise R to 2:  1/3@raise R|raise W to 2 too:  0@raise W"
The store starts at two thirds. Raise R to two, and it's a third. Still no guarantee, and it'll look fixed in a test of ten reads. Raise W to two as well, and it's zero. The write now waits for the second fastest of three, eight milliseconds at the p ninety nine. Not a close call.

@chapter Where people slip
@list heading="Common slips" items="Reading R + W = N as good enough@The first|Assuming a miss means the write was lost@The second|Applying the formula without a uniform draw@The third"
The first slip is reading R plus W equals N as good enough. The second is assuming a miss means the write was lost. And the third is applying the formula when the coordinator doesn't draw uniformly.

@chapter Try it
@words text="N = 5, R = 2, W = 2" sub="C(3, 2) = 3 · C(5, 2) = 10"
Your turn. Five replicas, two and two as a compromise. Three choose two is three, five choose two is ten. Find the miss probability, then every configuration on five nodes with R plus W of six, and pick one for nine reads per write.

@end text="Count the read sets that miss"
You can set N, R and W and see the exact miss probability, on Learn. That's learn dot get er done dot I O.
