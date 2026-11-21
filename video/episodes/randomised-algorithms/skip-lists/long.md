---
format: long
lesson: randomised-algorithms/skip-lists
title: Skip lists: express lanes chosen by coin flips
thumb: Flip a coin for each lane
---

@chapter Express lanes
@title text="Skip Lists" sub="Randomised Algorithms" art=thumb
What if a sorted linked list had express lanes, and every element chose its own lanes by flipping a coin? That's a skip list, and nothing in it is ever rebalanced.

@art lanes
Level zero is the sorted list of every key. Each key in a level also appears in the next level up with probability a half, independently. So each level holds about half the keys of the one below. A key's level is the highest list it appears in.

@art coin-tape
In the lab, each key reads a coin tape at its own position, and its level is the run of heads there. The tape is chosen by a seed, so the structure is reproducible. The coins come from a prime modulus stream, because the low bit of a power of two modulus generator isn't a fair coin.

@chapter The search
@art search-path
To find a target, start at the top left. If the next node at this level exists and isn't past the target, move to it. Otherwise drop a level. Stop at level zero. Every move and every drop is a hop, and the lab counts them.

@chapter Sixteen keys
@words text="keys 10 … 160" sub="levels 1 1 2 0 0 4 0 1 0 0 1 4 1 0 1 1"
Sixteen keys, ten to a hundred and sixty. On the opening tape, ten of the sixteen reach at least level one, and two reach level four.

@math heading="Two searches" items="find 120 (level 4):  2 hops@a hundred and twenty;;find 100 (level 0):  8 hops@a hundred;;mean over all 16:  77/16 ≈ 4.81,  worst 8@seventy seven"
Searching for a hundred and twenty, one of the two tallest keys, takes two hops. Searching for a hundred, a level zero key right after another level zero key, takes eight. Same structure, same tape, a factor of four. The mean over all sixteen is seventy seven sixteenths, about four point eight one, and the worst is eight.

@chapter The level table
@math heading="Top level  vs  present" items="top level 0: 6 keys  ·  present at L0: 16@level zero;;top level 1: 7  ·  present at L1: 10@level one;;top level 3: 0  ·  present at L3: 2@level three;;top level 4: 2  ·  present at L4: 2@level four"
The panel prints two columns. Six keys top out at level zero, and all sixteen are present there. Seven top out at level one, and ten are present at level one. At level three, no key tops out, yet two are present, because a level four key appears at every level below. Two keys top out at level four.

@art top-vs-present
That's the commonest confusion. Top level is k is a partition, and adds up to n. Present at level k is a nested family, and shrinks as k grows. The tape's counts are near the prediction, and not equal to it.

@chapter What's guaranteed
@art search-path
The expected search cost is order log n. At each level, the walk passes a constant number of nodes on average before dropping. There's no concentration result here, because that needs Chernoff bounds.

@words text="2 log₂ n = 8.000" sub="a reference curve, not a bound"
So the panel draws two log two n as a dashed reference, sampled in floating point, with no verdict read off it. At sixteen keys it reads eight, against a counted mean of four point eight one. It's not a bound, and nothing passes or fails against it.

@art local-insert
An insertion writes a few pointers at the levels the coin chose, and touches no other node. Change n, and the existing keys' levels don't move. An AVL tree guarantees a height always, and pays with stored heights and rebalancing. A skip list guarantees an expectation, and pays with nothing.

@art flat-list
The price is an unbounded worst case. Nothing prevents a tape that promotes nothing, leaving one flat list. Whether that matters is a question about the system, not the structure. If a worst case must be bounded, use a structure that enforces an invariant.

@chapter Where people slip
@list heading="Common slips" items="Grading the mean against the dashed curve@The first|Confusing top level with levels occupied@The second|Expecting a worst-case bound@And the third"
The first slip is grading the counted mean against the dashed curve, as if it were a bound. The second is confusing a key's top level with the levels it occupies. A level four key sits in five lists. And the third is expecting a bound on the worst search. There isn't one.

@end text="Flip a coin for each lane"
Change the tape and count the hops yourself, on Learn. That's learn dot get er done dot I O.
