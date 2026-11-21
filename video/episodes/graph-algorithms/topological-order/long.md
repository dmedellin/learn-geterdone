---
format: long
lesson: graph-algorithms/topological-order
title: Topological sort: two right answers, and how many there are
thumb: One order, not the order
---

@chapter The question
@title text="Topological Order" sub="Graph Algorithms" art=thumb
You've got tasks, and some must come before others. Can you line them all up so every task follows its prerequisites? Sometimes. And when you can, there's usually more than one right answer.

@chapter The definition
@art left-to-right
A topological order lists every vertex so that, for every arc from u to v, u comes before v. Drawn left to right, no arc points left.

@chapter When it exists
@words text="An order exists ⟺ the digraph is acyclic"
An order exists exactly when the graph has no cycle. If there were a cycle, each arc would force its tail before its head, all the way round, so the first vertex would have to come before itself.

@art finish-stack
Conversely, if there's no cycle, run one depth first walk. There's no back arc, so for every arc, the head finishes before the tail. List the vertices by decreasing finish time, and every tail comes first. The proof is the algorithm.

@words text="push at each close, read the stack" sub="6 visits · 6 arc reads"
And it's free. Push each vertex onto a stack as it closes, then read the stack. On the lab's graph, that's six vertex visits and six arc reads, the same as the walk.

@chapter Kahn's method
@list heading="Kahn's method" items="Queue every vertex of in-degree 0@in degree zero|Emit one, decrement its successors@emit it|Successors that reach 0 join the queue@reaches zero|Fewer than V emitted: a cycle@fewer than V"
The second method never mentions a finish time. Put every vertex with in degree zero into a queue. Take one out, emit it, and decrement each successor's in degree. Any successor that reaches zero joins the queue. If you emit fewer than V vertices, the rest are on or below a cycle.

@art in-degree-queue
A vertex joins the queue only when nothing left points into it, and since in degrees only go down, it joins at most once. Each arc is read once, when its tail is emitted. So it's Theta of V plus E again.

@math heading="1>3 2>3 3>4 3>5 4>6 5>6" items="in-degrees:  0, 0, 2, 1, 1, 2@in degrees;;Kahn:  1 2 3 4 5 6@Kahn's method gives;;walk:  2 1 3 5 4 6@the walk gives"
Here's a task graph with six vertices. The in degrees are zero, zero, two, one, one, two. Kahn's method gives one, two, three, four, five, six, with four pushes, six pops and six arc reads. The walk gives two, one, three, five, four, six. The lab checks both arc by arc, and both pass.

@chapter Counting the orders
@art four-orders
They disagree, and neither is wrong. So how many valid orders are there? The lab enumerates them all and finds four. One or two can go first, and four or five can go in the middle. Two times two is four.

@math heading="How many orders?" items="chain of 5:  1@a chain;;diamond:  2@a diamond;;5 vertices, no arcs:  5! = 120@no arcs;;with a cycle:  0@a cycle"
Uniqueness has a numerical answer. A chain of five vertices has exactly one order. A diamond has two. Five vertices with no arcs have five factorial, a hundred and twenty. And a graph with a cycle has zero.

@art chain
The chain is what uniqueness needs. Two vertices with no path between them can always swap. So for one order, there must be an arc between every consecutive pair, which means the order is a Hamiltonian path. That's much stronger than acyclic.

@words text="9 vertices: refused" sub="8 vertices, no arcs: 8! = 40 320 orders"
The enumeration is a real search, so the lab refuses above eight vertices, rather than running forever. Eight vertices with no arcs already have forty thousand three hundred and twenty orders.

@chapter A cycle, three ways
@art cycle-stuck
On one to two, two to three, three to one, and three to four, the depth first walk finds a back arc and gives no order. Kahn's queue starts empty, because the first three all have in degree one, so it emits nothing. And the enumeration counts zero. Three witnesses, one cause.

@chapter Where people slip
@list heading="Common slips" items="Calling it the topological order@The first|Sorting by finish time@The second|Treating no order as an error@And the third"
The first slip is calling the output the topological order. It's one of them, and code that depends on which one is depending on a detail. The second is actually sorting by finish time, which adds a log factor for nothing. And the third is treating no order as an error. It's a result, and both methods hand you the evidence.

@chapter Try it
@words text="Count the orders of your own task graph"
Your turn. Draw a small task graph of your own. Produce an order with each method, then count every valid order, and say whether it's unique.

@end text="Count every order"
You can run both methods and enumerate every valid order, on Learn. That's learn dot get er done dot I O.
