---
format: long
lesson: greedy-and-matroids/independence-systems-and-matroids
title: What is a matroid? Independence, exchange, and the three-edge counterexample
thumb: Every basis, the same size
---

@chapter The question
@title text="Independence Systems and Matroids" sub="Greedy Algorithms and Matroids" art=thumb
This course has shown greedy algorithms that are optimal, each proved its own way. Is there one condition that explains them all? There is, and it's a condition on the family of feasible sets, not on how the problem looks.

@art nested-sets
Start with a ground set, E, and a collection of its subsets, called independent. It's an independence system if the collection isn't empty, and it's downward closed: any subset of an independent set is independent too. A maximal independent set is a basis, and the size of the largest is the rank.

@chapter The exchange property
@math heading="Matroid" items="A, B independent,  |A| < |B|@A and B are independent;;⟹  some x ∈ B \ A  with  A ∪ {x} independent@there's some element x"
A matroid adds one more rule, the exchange property. Whenever A and B are independent, and A is smaller than B, there's some element x in B but not in A that you can add to A, and it stays independent.

@words text="In a matroid, every basis has the same size"
That has a quick consequence. Every basis has the same size. If two maximal sets had different sizes, exchange would let the smaller one grow, and then it wouldn't be maximal.

@chapter Forests of a graph
@art forest-graph
The lab opens on a graph with four vertices and five edges, A to E: one two, two three, three one, three four, and one four. A set of edges is independent when it has no cycle. In other words, it's a forest.

@list heading="Forests" items="24 of 32 subsets independent@twenty four|rank 3 · 8 bases@rank is three|193 exchange pairs · 0 failures@a hundred and ninety three"
The panel asks about all thirty two subsets, and twenty four are forests. The rank is three, and there are eight bases, the spanning trees. Then it tests every ordered pair with A smaller than B, a hundred and ninety three of them. Every one succeeds. It's a matroid.

@chapter Greedy here is Kruskal
@art cycle-reject
Sort the elements by weight and add each one if the set stays independent. On forests, that's Kruskal's algorithm, except matroid greedy maximises, so it goes heaviest first.

@math heading="Weights 8 6 5 4 2" items="take A, take B@takes A;;reject C: closes 1-2-3@rejects C;;take D, reject E@takes D;;{A, B, D} = 18@eighteen"
With weights eight, six, five, four and two, greedy takes A, takes B, and rejects C, because one, two, three would close a cycle. It takes D, rejects E, and finishes with A, B and D, worth eighteen, the best any independent set can do.

@words text="A proof about the family, not the graph"
The cut property proved Kruskal using graphs. The matroid theorem proves it using only the family of feasible sets. So the same proof covers families with no graph in sight.

@chapter Two more matroids
@art uniform-pick
The uniform family takes any subset of at most two, out of five elements. Sixteen sets, rank two, ten bases, sixty five pairs tested, and none fails.

@art partition-groups
The partition family allows at most one element from each group. With groups one, one, two, two, three, that's eighteen sets, rank three, four bases, and no failure. Greedy with weights seven, six, five, four and three takes the heaviest from each group, A, C and E, worth fifteen.

@chapter One that isn't
@art path-matching
Now the edges of a path, one two, two three, three four, called A, B and C. A set is independent when no two edges share a vertex. That gives five sets: the empty set, each single edge, and A with C. It's downward closed.

@words text="A = {B},  B = {A, C}" sub="7 pairs tested · 1 failure"
But of the seven pairs tested, one fails. The set with just the middle edge is smaller than A and C together, yet neither end can join it, since each shares a vertex. So the middle edge is maximal with one element, while the only basis has two.

@words text="3 elements: the smallest failure"
That's the smallest possible counterexample. Two elements can never fail exchange. Three is where a non matroid can first appear.

@chapter Where people slip
@list heading="Common slips" items="Treating downward closure as the whole definition@The first|Confusing maximal with maximum@The second|Reading three passing families as a rule@The third"
The first slip is treating downward closure as the whole definition. The matchings pass it and still aren't a matroid. The second is confusing maximal, can't be extended, with maximum, as large as any. The third is reading three passing families as a general rule. Most independence systems aren't matroids.

@chapter Try it
@words text="matchings of 1-2, 2-3, 3-4" sub="weights: middle edge heaviest"
Your turn. On the three edge path, give the middle edge the biggest weight but less than the two ends combined. Run greedy, heaviest first. What does it pick, and what's the best independent set?

@end text="Test the exchange property yourself"
You can list every independent set and test every exchange pair, on Learn. That's learn dot get er done dot I O.
