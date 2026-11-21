---
format: long
lesson: integer-programming/the-knapsack-and-set-covering-models
title: Knapsack and set covering, and how each relaxation cheats
thumb: Two-thirds of a crate
---

@chapter Two building blocks
@title text="Knapsack and Set Covering" sub="Integer Programming" art=thumb
Most practical binary programmes are built from two pieces. One is a single capacity with items chosen to fit. The other is a list of requirements, each covered by at least one chosen set. Here's each one, and the way its relaxation goes fractional.

@chapter The knapsack
@math heading="0/1 knapsack" items="max Σ v_j y_j@maximise;;Σ w_j y_j ≤ W@weights;;y_j ∈ {0, 1}@zero or one"
Items have values and weights, and there's a capacity. Maximise the total value of the items you choose, subject to their total weight staying within the capacity. Each item is in or out, so every y is zero or one. The name is the picture: one bag, a weight limit. Which features to ship, which repairs to fund, which crates to load.

@art knapsack-bag
The lesson's example has three items, worth sixty, a hundred and a hundred and twenty, weighing ten, twenty and thirty. The capacity is fifty. Their values per unit weight are six, five and four.

@chapter Three answers
@art split-item
The relaxation loads items in value per weight order. The first two go in whole: thirty units of weight, worth a hundred and sixty. Then it takes two thirds of the third item to fill the bag. That's two hundred and forty. That's the bound.

@art greedy-stuck
Greed by value per weight takes the first two, then can't fit the third in the remaining twenty units, and stops at a hundred and sixty.

@art best-pair
The best whole choice, found by trying all eight subsets, is the second and third items together. Weight exactly fifty, value two hundred and twenty.

@math heading="One instance" items="relaxation 240@two hundred and forty;;optimum 220@two hundred and twenty;;greedy 160@a hundred and sixty;;240 ≥ 220 ≥ 160@the middle"
So two hundred and forty, two hundred and twenty, a hundred and sixty. And the middle number is the only one that's an answer. The value per weight rule isn't a heuristic for the relaxation. It solves it exactly. It just doesn't solve the zero one problem.

@chapter Set covering
@math heading="Set covering" items="min Σ c_j y_j@minimise;;Σ y_j ≥ 1  over the sets covering i@at least one;;y_j ∈ {0, 1}@zero or one"
Now covering. Each set has a cost and covers some requirements. Minimise the total cost, subject to every requirement having at least one chosen set that covers it. Each y is again zero or one. Depots covering districts, shifts covering hours, tests covering code paths. Each row is an at least one of these, from the previous lesson.

@art depot-ring
Take five districts in a ring, each reachable from two of five depots, every depot costing two. The relaxation opens every depot to the extent of one half. Each row gets two halves, and it pays five. No whole choice does that. Three depots are needed, costing six.

@words text="Relaxation 5 · Optimum 6"
So the relaxed knapsack splits exactly one item, and the relaxed covering spreads halves across overlapping sets. The gap of one here is the price of not being able to open half a depot.

@chapter Covering is not partitioning
@art odd-ring
Now require each district to be covered exactly once, instead of at least once. Only the relation changed, and now there's no feasible choice at all. An odd ring can't be split into adjacent pairs. Yet the relaxation is still solvable, still worth five. A feasible relaxation says nothing about the integer problem.

@chapter Where people slip
@list heading="Common slips" items="Using the density rule as if it solved 0/1@The first|Turning ≥ 1 into = 1 to tidy up@The second|Reading a fractional take as a plan@And the third"
The first slip is using the density rule as though it solved the zero one problem. The second is turning at least one into exactly one, to tidy the model. And the third is reading the relaxation's fractional take as a plan. Two thirds of a crate and half a depot are arithmetic, not instructions.

@chapter Try it
@words text="All eight subsets" sub="items 60/10, 100/20, 120/30 · capacity 50"
Your turn. List all eight subsets of the three items, from none of them to all three. For each, add up the weight and the value, and cross out any over fifty. Confirm that two hundred and twenty is the best that's left, and spot the subset greed chose.

@end text="Build both models from data"
You can build both models from your own data and see what each relaxation splits, on Learn. That's learn dot get er done dot I O.
