---
format: long
lesson: intro-algorithms-graphs/dijkstra-and-difference-constraints
title: Dijkstra's algorithm, and inequalities that are secretly a graph
thumb: Settle the nearest first
---

@chapter Faster, with one condition
@title text="Dijkstra's Algorithm and Difference Constraints" sub="Introduction to Algorithms, Sections 24.3–24.5" art=thumb
Bellman Ford relaxed every arc in every round, because it couldn't know which estimates were final. Dijkstra's algorithm always knows one.

@quote text="As we shall see, with a good implementation, the running time of Dijkstra’s algorithm is lower than that of the Bellman-Ford algorithm." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 24.3"
As section twenty four point three says: as we shall see, with a good implementation, the running time of Dijkstra's algorithm is lower than that of the Bellman Ford algorithm. The condition is that every weight is nonnegative.

@chapter The algorithm
@art settled-set
Put every vertex into a min priority queue keyed by its estimate. Then repeat: extract the vertex of least estimate, add it to the settled set S, and relax every arc leaving it. Each arc is relaxed once.

@art leaving-s
Theorem twenty four point six says a vertex's estimate is exact when it's extracted. Any other route to it must leave S at some arc. With no negative weights, the rest of that route can only get longer, so it can't beat the vertex you just settled.

@art queue-choices
How fast is it? That depends on the queue that holds the unsettled vertices. The settled set plays the part of breadth first search's black vertices, and the queue plays the part of Prim's.

@math heading="The queue decides the cost" items="array: O(V²)@a plain array;;binary heap: O((V + E) lg V)@a binary heap;;Fibonacci heap: O(V lg V + E)@a Fibonacci heap"
There are V extractions and at most E key decreases. With a plain array, that's O of V squared. With a binary heap, O of V plus E, times log V. With a Fibonacci heap, O of V log V plus E. Dijkstra's many decreases were the motivation for that heap.

@chapter On the lesson's graph
@math heading="1-2 4 · 1-3 1 · 2-3 2 · 2-4 5 · 3-4 8 · 4-5 3 · 3-5 9" items="settle 1 (0), 3 (1), 2 (3), 4 (8), 5 (10)@settles one;;14 relaxations · 7 pushes · 7 pops@fourteen relaxations"
On the lesson's graph of five vertices and seven edges, the lab settles one at zero, then three at one, two at three, four at eight, and five at ten. That's fourteen relaxations, every edge once from each end, with seven pushes and seven pops.

@list heading="Three schedules, same labels" items="heap: 14 relaxations@With the heap|scan every vertex: 14 relaxations, 30 reads@Scanning|every edge, over and over: 2 rounds, 28 relaxations@Relaxing every edge"
With the heap, fourteen relaxations. Scanning every vertex instead gives the same fourteen and the same labels, with thirty reads to find the nearest. Relaxing every edge over and over, Bellman Ford style, takes two rounds and twenty eight. The order decides the work.

@chapter Breaking it
@math heading="1>2 1 · 1>3 4 · 3>2 −4 · 2>4 1" items="settle 1 (0), 2 (1), 4 (2), 3 (4)@settles one;;relax 3 → 2: d[2] = 0@lowers vertex two;;✗ 4 stays at 2; true distance 1@never revisited"
Now one negative arc, by hand. Dijkstra settles one at zero, then two at one, four at two, and three at four. Relaxing three to two then lowers vertex two to zero. But four was settled at two, and it's never revisited. Its true distance is one, along one, three, two, four.

@art negative-trap
No negative cycle is Bellman Ford's condition, not Dijkstra's. Dijkstra needs every weight nonnegative.

@chapter Difference constraints
@art constraint-graph
Section twenty four point four turns inequalities into a graph. When every inequality says x j minus x i is at most b, make a vertex per variable and an arc from i to j of weight b. Add an extra vertex with a zero weight arc to every other one.

@words text="No negative cycle ⇒ distances solve it" sub="negative cycle ⇒ no solution"
If that graph has no negative cycle, the distances from the extra vertex are a solution. If it has one, the system has none. Since weights can be negative, Bellman Ford solves it.

@math heading="x₂ − x₁ ≤ 3 · x₃ − x₂ ≤ −1 · x₃ − x₁ ≤ 1 · x₁ − x₃ ≤ 2" items="distances: 0, 0, −1@distances;;x = (0, 0, −1)@So x;;0 ≤ 3 · −1 ≤ −1 · −1 ≤ 1 · 1 ≤ 2@each inequality"
On the lesson's system, the distances from the extra vertex are zero, zero, and minus one. So x is zero, zero, minus one, and each inequality checks.

@art shift-solution
Add the same constant to every variable, and the differences don't change. So one, one, zero works too. A system like this never has just one solution.

@chapter Where people slip
@list heading="Common slips" items="Dijkstra works with no negative cycle@The first|The heap makes it correct@The second|Expecting one solution@the third"
The first slip is thinking Dijkstra works whenever there's no negative cycle. The second is crediting the heap with its correctness. The heap only finds the least estimate quickly. And the third is expecting a system of difference constraints to have one solution.

@chapter Try it
@words text="1-2 7 · 1-3 2 · 2-3 3 · 2-4 1 · 3-4 6 · 3-5 8 · 4-5 2" sub="Dijkstra from 1: order and estimates"
Your turn. Run Dijkstra from one on this graph by hand, writing the order of settling and every estimate after each step. Then compare the heap and scan schedules in the lab.

@end text="Run three schedules"
You can run Dijkstra's schedule against two others on your own graph, on Learn. That's learn dot get er done dot I O.
