---
format: long
lesson: dynamic-programming-and-sequential-decisions/filling-the-table-from-the-end
title: Dynamic programming: fill the table from the end, and keep every tie
thumb: Start at the finish
---

@chapter The problem
@title text="Filling the Table from the End" sub="Dynamic Programming and Sequential Decisions" art=thumb
You want the cheapest way across a network. The trick is to start at the finish and work backwards, one stage at a time.

@art staged-network
Here's the kind of network we mean. It's split into stages, and every arc runs forward, from one stage to a later one. Never sideways, never back. Each arc has a cost.

@math heading="The value of a node" items="f(w) = 0 in the last stage@zero;;f(v) = min over arcs v→w of  c(v,w) + f(w)@the cheapest"
The value of a node, f, is the cheapest total from there to the finish. In the last stage it's zero. Anywhere else, it's the cheapest, over every arc out, of the arc's cost plus the value of where that arc leads.

@chapter Why backwards
@art backward-sweep
That definition forces the order. You can only write f at a node once the values it points to are settled. The last stage is zero by definition, so it goes first, and each earlier stage is built on values that are already final.

@words text="Written once, never revised"
And each value is written once and never changed. If you ever want to go back and improve a value you've already filled in, either the order is wrong or the state is.

@chapter A worked network
@words text="A ; B C ; D E ; F" sub="A→B 0 · A→C 4 · B→D 7 · B→E 4 · C→D 3 · C→E 2 · D→F 1 · E→F 4"
Here's the lesson's network. Stage one is A, then B and C, then D and E, then F. A to B costs zero, A to C four, B to D seven, B to E four, C to D three, C to E two, D to F one, and E to F four.

@math heading="Filled from the end" items="f(F) = 0@F is zero;;f(D) = 1 + 0 = 1@D is one;;f(E) = 4 + 0 = 4@E is four;;f(B) = min(7 + 1, 4 + 4) = min(8, 8) = 8@For B;;f(C) = min(3 + 1, 2 + 4) = min(4, 6) = 4@For C;;f(A) = min(0 + 8, 4 + 4) = min(8, 8) = 8@And A"
F is zero. D is one plus zero, so one. E is four. For B, seven plus one is eight, and four plus four is also eight. That's a tie. For C, three plus one is four, beating six. And A: zero plus eight, or four plus four, eight either way. Another tie.

@chapter The ties are the answer
@art tie-fork
So the answer is eight. But look at what the table holds: one number per node, and no route at all. The routes come back afterwards, by following the best arcs forward from A. And at A and at B, there are two best arcs.

@art three-routes
Follow both at each tie and you get three routes, not one. A, B, D, F. A, B, E, F. And A, C, D, F. Price each one again from the arcs and all three come to eight.

@art all-paths
To check, walk every path. There are four in total, and they cost eight, eight, eight and ten. The best is eight and exactly three paths reach it, which agrees with the recursion. That enumeration is an oracle for checking, not a method. It grows exponentially on purpose.

@chapter One arc changes everything
@math heading="A→B: 0 becomes 2" items="f(A) = min(2 + 8, 4 + 4) = 8@still eight;;paths: 10, 10, 8, 10@ten, ten, eight and ten"
Now change A to B from zero to two. A becomes the smaller of two plus eight and four plus four, still eight, but only through C. The four paths now cost ten, ten, eight and ten. Same number, one route instead of three.

@art skip-arc
Arcs may also skip a stage. Add A to E at a cost of three. E is already settled, so the new option is three plus four, seven. That beats eight, and the single best route is A, E, F. No special case needed.

@chapter Where people slip
@list heading="Common slips" items="Keeping only the first argmin@The first|Filling the table forwards@The second|Thinking the saving is about this network@And the third"
The first slip is keeping only the first best arc. The route is optimal, but the page stops saying there are others. The second is filling the table forwards, which answers a different question. And the third is thinking the saving shows here. Six values against four paths isn't one. The saving is a shape: paths multiply, values add.

@chapter Try it
@words text="Add A→E 3" sub="then count the best routes"
Your turn. Take the original network, add the arc from A to E at three, and fill the table from the end yourself. Then walk all five paths forwards and check that they agree with what you found.

@end text="Fill the table, keep the ties"
You can type in your own staged network and watch the table fill, ties and all, on Learn. That's learn dot get er done dot I O.
