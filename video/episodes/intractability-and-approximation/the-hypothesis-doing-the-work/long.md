---
format: long
lesson: intractability-and-approximation/the-hypothesis-doing-the-work
title: The doubled-tree TSP tour, and the hypothesis it can't live without
thumb: Remove the hypothesis, lose the promise
---

@chapter A promise with a condition
@title text="The Hypothesis Doing the Work" sub="Intractability and Approximation" art=thumb
There's a simple algorithm that finds a travelling salesman tour within twice the optimum. But only if one condition holds. Remove it, and the promise doesn't get weaker. It disappears.

@words text="D(a, b) ≤ D(a, c) + D(c, b)" sub="the triangle inequality"
The condition is the triangle inequality. Going directly from a to b is never longer than going via some c. Distances that come from positions in space always satisfy it, which is why it usually comes for free.

@chapter The algorithm
@art spanning-tree
First, build a minimum spanning tree of the cities. Delete any one step from an optimal tour, and what's left is a spanning tree, no heavier than the tour. So the minimum spanning tree is a lower bound on the optimum.

@art doubled-walk
Next, walk the tree, using every edge exactly twice, and come back to the start. That closed walk visits every city, and weighs exactly twice the tree.

@art shortcut
Finally, follow the walk, but skip any city you've already visited, hopping straight to the next new one. What's left is a tour. And here's where the hypothesis is spent: a direct hop is no longer than the path it replaces, only if the triangle inequality holds.

@chapter Why it's within twice
@math heading="The guarantee" items="MST ≤ OPT@the tree;;walk = 2 × MST@twice the tree;;tour ≤ walk  (triangle inequality)@no longer;;tour ≤ 2 × OPT@twice the optimum"
So the tree is at most the optimum. The walk is twice the tree. The tour is no longer than the walk. So the tour is at most twice the optimum.

@chapter Four cities
@math heading="Four numbers" items="tree:  5@the tree is five;;optimum:  7@by exhaustive search;;tour built:  10@shortcut tour is ten;;ratio 10/7@ten sevenths"
The loaded instance has four cities with distances from one to three, and it's metric. The tree is five. The optimum, by exhaustive search, is seven. The shortcut tour is ten, exactly twice the tree. So the ratio is ten sevenths. All the slack in the promise lives in the gap between five and seven.

@chapter Every metric instance
@art four-city-sweep
One instance isn't a worst case, so the panel sweeps every instance of this size.

@words text="729 instances · 482 metric · worst 10/7"
This instance wasn't picked by hand. The panel enumerates every symmetric four city instance with distances one to three, seven hundred and twenty nine. It keeps the four hundred and eighty two that are metric, solves each exactly, and reports the worst ratio. It's ten sevenths, and this is the instance.

@words text="3 cities: worst ratio 1" sub="10/7 ≈ 1.43 on a tiny family"
On three cities, the worst is one, because every tour on three cities is the same tour. And ten sevenths, about one point four three, isn't evidence the factor of two is loose. The family is tiny.

@chapter Switch it off
@art broken-triangle
Now raise one distance. One to two costs fifty, and every other distance is one. Going round through three costs two, so the triangle inequality fails by a factor of twenty five.

@math heading="Not metric" items="tree 3,  promise 6@a tree of three;;optimum 4@optimum of four;;tour 53@fifty three"
The panel reports metric, no. A tree of three, so a promise of six. An optimum of four. And a tour of fifty three. More than eight times the promise. The shortcut replaced a cheap path with an enormous hop, and the proof's last line is simply false.

@art unbounded
There's no weaker guarantee left over. Raise that distance further, and the tour grows without limit, while the optimum stays at four. A conditional result with a false condition says nothing at all.

@words text="no hypothesis  ⟹  no constant factor, unless P = NP"
And the general problem really is that bad. Earlier, putting rho times n plus one on the non edges showed there's no constant factor approximation without a hypothesis, unless P equals N P. So the triangle inequality isn't a convenience. It's the difference between a factor two algorithm and none.

@chapter Where people slip
@list heading="Common slips" items="Quoting 2 without checking the input is metric@The first|Expecting a weaker guarantee when it fails@The second|Reading a small sweep as evidence about the bound@And the third"
The first slip is quoting the factor of two without checking the data is metric. One way streets and volume discounts break it. The second is expecting some weaker guarantee when the hypothesis fails. And the third is reading ten sevenths over a tiny family as evidence about a bound over every instance.

@end text="The hypothesis does the work"
Drag the slider that breaks the triangle inequality, on Learn. That's learn dot get er done dot I O.
