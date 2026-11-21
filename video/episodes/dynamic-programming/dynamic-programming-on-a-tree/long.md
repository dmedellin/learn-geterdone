---
format: long
lesson: dynamic-programming/dynamic-programming-on-a-tree
title: Dynamic programming on a tree: two numbers per vertex
thumb: With it, or without it
---

@chapter The question
@title text="Dynamic Programming on a Tree" sub="Dynamic Programming and Optimal Substructure" art=thumb
Pick vertices so that no two of them are joined by an edge, and make their total weight as large as possible. On a general graph, that's NP hard. On a tree, it takes one pass. The difference isn't cleverness. It's the tree.

@art independent-set
A set of vertices is independent if no edge joins two of them. Give each vertex a weight, and the maximum weight independent set is the independent set with the largest total.

@chapter Two numbers per vertex
@math heading="The pair recurrence" items="with(v) = weight(v) + Σ without(u)@with of v;;without(v) = Σ max(with(u), without(u))@without of v;;answer = max(with(root), without(root))@The answer"
Root the tree anywhere. For each vertex v, keep two numbers. With of v is the best total in v's subtree if v is taken. Then no child can be, so it's v's weight plus every child's without. Without of v leaves each child free, so it sums each child's better option. The answer is the larger at the root.

@art with-without
Taking a vertex forbids its children. Declining it lets each child do whatever's best for itself. One number per vertex can't answer both of those questions, so the table holds a pair.

@chapter Why it works
@art disjoint-subtrees
Why is that right? Take the best set in v's subtree. The part inside each child's subtree must itself be best, under the right constraint, or you could swap in something heavier. And that swap is legal because different subtrees share no vertex and no edge.

@art cycle-edge
That disjointness is exactly what a tree gives you, and a cycle destroys. Add one extra edge, and two subtrees can interact, and the decomposition is gone. Optimal substructure here is a property of the input's shape.

@art postorder
The fill order comes free too. Every read is from a child, and a postorder pass finishes every child before its parent. There's no ordering decision to get wrong. The tree's shape is the order.

@chapter A spine with legs
@words text="path 1-2-3-4 · legs at 2, 3, 4" sub="weights 1 6 6 6 1 1 1"
The lab loads seven vertices: a path one, two, three, four, with an extra leaf hanging off two, three and four. The weights are one, six, six, six, one, one, one. Vertices two, three and four are heavy, and they form a path, so at most two of them can go.

@list heading="Result" items="One pass: 13 = vertices 2, 4, 6@The pass returns|All 128 subsets: 13@a hundred and twenty eight"
The pass returns thirteen, choosing vertices two, four and six, two heavy ones and one leaf. And all a hundred and twenty eight subsets confirm thirteen.

@words text="Independent? · Weight matches?"
Then two checks. Independence is tested against the edge list as typed, not the structure the pass walked, because a bug there would fool both the same way. Then the set is re weighed. The empty set is independent, so independence alone isn't enough.

@chapter The alternating instinct
@art alternate-levels
Lots of people reach for alternating levels. On a path, that's right, and the lab's path gives fifteen. On this tree, alternating from the root takes one, three, five and seven, for nine, against thirteen. The other parity happens to give thirteen. Choosing the parity correctly is the whole problem again.

@words text="7 visits · 12 reads  vs  128 subsets" sub="Θ(n) vs Θ(2ⁿ n)"
The pass visits seven vertices and makes twelve reads, against a hundred and twenty eight subsets. The bounds are Theta of n against Theta of two to the n, times n. Here, unusually on this course, measurement and bound agree already, at seven vertices.

@chapter Where people slip
@list heading="Common slips" items="Keeping one number per vertex@The first|Carrying the pass to a graph with a cycle@The second|Checking the weight but not the legality@The third"
The first slip is keeping one number per vertex instead of two. The second is running the pass on a graph that isn't a tree. It still produces a number, just not the answer, which is why the lab refuses a cycle. The third is checking the weight without checking that the set is independent.

@chapter Try it
@words text="a path of 5 vertices" sub="weights 3 1 1 3 1"
Your turn. Take a path of five vertices with weights three, one, one, three, one. Root it at one end, fill with and without for every vertex, bottom up, and find the best total. Does alternating get it?

@end text="Run the pass on your own tree"
You can type a tree, run the pass, and check the set against every subset, on Learn. That's learn dot get er done dot I O.
