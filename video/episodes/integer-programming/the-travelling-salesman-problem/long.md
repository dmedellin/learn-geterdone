---
format: long
lesson: integer-programming/the-travelling-salesman-problem
title: The travelling salesman: bound it, cut the subtours, branch
thumb: Near-optimal needs a bound
---

@chapter The problem
@title text="The Travelling Salesman Problem" sub="Integer Programming" art=thumb
Visit every city once, come back to the start, and travel as little as possible. It's the most famous hard problem there is. And yet small instances get solved exactly, with a proof. Here's how.

@chapter Counting tours
@math heading="n = 7" items="n! = 5040  orderings@five thousand and forty;;(n − 1)!/2 = 360  distinct tours@three hundred and sixty;;5040 ÷ 360 = 14 = 2 × 7@fourteen"
First, how many tours are there? On seven cities there are five thousand and forty orderings. But the starting city doesn't change a tour, and nor does the direction. Distinct undirected tours number n minus one factorial over two, which is three hundred and sixty. Saying n factorial overcounts by fourteen, two times seven.

@art city-tour
Three hundred and sixty tours can be enumerated instantly, so the lesson stops at seven cities. That way every bound can be checked against an exact answer. On six cities there are exactly sixty.

@chapter The assignment relaxation
@words text="One departure, one arrival, per city"
Here's the relaxation. For each city, choose one city to leave for and one to arrive from, at minimum total cost. That's the assignment problem. Every tour satisfies it, so its optimum is a lower bound on the tour.

@art subtours
But a set of separate little loops satisfies it too. On the lesson's six cities, the assignment relaxation is worth eighty, and it returns three two city subtours: one and five shuttling back and forth, two and three, and four and six. That's a bound, not a route.

@chapter Cut the subtours, on demand
@words text="At least one arc must leave S" sub="one constraint per subset of cities"
To forbid a subtour inside a set of cities, require at least one chosen arc to leave that set. There's one such constraint for every subset, which is exponentially many. You can't write them all down. But almost all are slack, so you add one only when a solution breaks it.

@art forbid-arc
So: solve, find the shortest subtour, forbid an arc of it, and re-solve. Two children come back with a four city subtour and a two city one, still not a tour. Forbid an arc again, and the next child is a genuine tour.

@math heading="Six cities" items="bound 80:  (1 5)(2 3)(4 6)@eighty;;optimum 88 in 5 nodes@eighty eight;;1 → 2 → 4 → 6 → 3 → 5 → 1@the route"
That tour is worth eighty eight. Five nodes in total, and the answer is eighty eight, on the route one, two, four, six, three, five, and back to one.

@art tour-tree
Hard and solved in five nodes isn't a contradiction. Hardness is a statement about every instance of every size. A certificate is a statement about the instance in front of you.

@chapter Measuring a heuristic
@art nearest-neighbour
Nearest neighbour from city one goes one, five, three, four, six, two, and back, costing ninety six. Is that good? The tour alone can't say. Against the optimum of eighty eight, it's eight worse, which is one twelfth of the tour in hand, about eight point three percent.

@art two-opt
Improve that tour with two opt, and it comes down to eighty eight, which is optimal here. But only the bound could tell you so. On the next instance, nearest neighbour could be forty percent off. A tour and a bound is a result. A tour alone is a route.

@words text="Measured gap ≠ proved ratio"
A proved ratio, like the factor of two for metric instances, holds for every instance, forever. A measured gap is a fact about one case. On your own data, the measured fact is often what you need.

@chapter Where people slip
@list heading="Common slips" items="Calling a tour near-optimal with no bound@The first|Quoting the number of tours as n!@The second|Taking an assignment solution as a route@And the third"
The first slip is calling a heuristic tour near optimal with no bound. The second is quoting the number of tours as n factorial, which is wrong by fourteen at seven cities. And the third is taking an assignment solution as a route. Three pairs shuttling between each other isn't a tour.

@chapter Try it
@words text="How many tours on 6 cities?" sub="n!,  then (n − 1)!/2"
Your turn. For six cities, compute n factorial, then n minus one factorial over two, and check you get sixty distinct tours. Then work out the overcount factor, and confirm it's two times six.

@end text="Bound, cut and branch a tour"
You can solve the relaxation, cut the subtours and measure a heuristic against the optimum, on Learn. That's learn dot get er done dot I O.
