---
format: long
lesson: intro-algorithms-design-techniques/matroids-and-greedy-methods
title: Matroids: when greedy is always right
thumb: Heaviest first, if it fits
---

@chapter A theory of greedy
@title text="Matroids and Greedy Methods" sub="Introduction to Algorithms, Sections 16.4 and 16.5" art=thumb
Each greedy algorithm so far needed its own proof. Sections sixteen point four and five, both starred, explain a whole family of greedy successes at once.

@quote text="In this section, we sketch a beautiful theory about greedy algorithms." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 16.4"
In this section, we sketch a beautiful theory about greedy algorithms. The authors are careful about its reach. It covers many practical cases, but not activity selection or Huffman codes.

@chapter What a matroid is
@list heading="A matroid" items="A finite ground set S@a finite set|Independent sets: every subset of one is one@hereditary|Exchange: a smaller one can grow from a larger@exchange"
A matroid is a finite set, together with a family of its subsets called independent. Two rules. It's hereditary: every subset of an independent set is independent. And it has the exchange property: if A is smaller than B, some element of B can be added to A, keeping it independent.

@art forest-graph
The example proved in full is the graphic matroid. The ground set is a graph's edges, and a set of edges is independent if it has no cycle, so it forms a forest. Removing edges can't make a cycle, so it's hereditary.

@art exchange-grow
For exchange, a forest with edge set A has the number of vertices minus the number of edges as its count of trees. If B has more edges, it has fewer trees. So some tree of B joins two different trees of A, and one of its edges can be added to A without making a cycle.

@words text="All maximal independent sets: same size" sub="spanning trees: |V| − 1 edges"
Exchange gives a neat consequence. All maximal independent sets have the same size. In a connected graph, they're the spanning trees, each with one fewer edge than vertices.

@chapter The greedy algorithm
@art greedy-pick
Give each element a positive weight. Greedy sorts the elements from heaviest to lightest, and takes each one whose addition keeps the set independent. On every weighted matroid, that finds a maximum weight independent set.

@list heading="Why greedy works" items="The first independent element is in some optimum@greedy choice|An element rejected early stays rejected@passing it over|What remains is a smaller matroid@optimal substructure"
The proof has three parts. The greedy choice: the first element that's independent on its own belongs to some optimal set. An element that can't be added at the start can never be added later, so passing it over loses nothing. And optimal substructure: what remains is again a matroid.

@math heading="Two triangles sharing vertex 3" items="edges 1-2:9  2-3:4  1-3:6  3-4:8  4-5:3  3-5:5@nine, four, six;;take 9, 8, 6, 5@takes nine;;reject 4 and 3: they close cycles@rejected;;spanning tree of weight 28@twenty eight"
In the lab, take two triangles sharing vertex three, with edge weights nine, four, six, eight, three and five. Greedy takes nine, eight, six and five. Four and three would each close a cycle, so they're rejected. The result is a spanning tree of weight twenty eight, and the lab confirms it's optimal.

@art two-triangles
That little graph has forty nine independent sets, seven forests in each triangle, and rank four. The lab tests exchange on all eight hundred and sixty seven ordered pairs. It's a matroid, and the theorem covers graphs with millions of edges too.

@art matching-fails
Not every hereditary family is a matroid. The matchings of a three edge path are hereditary. But the middle edge alone can't grow, though the two end edges together exist. Exchange fails, and the lab finds weights where greedy loses.

@chapter Scheduling tasks
@art task-slots
Section sixteen point five schedules unit time tasks, each with a deadline and a penalty if it's late. Put early tasks first, in order of deadline, and the question is which tasks to make early. A set can all be early exactly when, for every t, at most t of its tasks have deadline t or earlier.

@math heading="Six tasks, by penalty" items="a1 (d2, 60) take,  a2 (d1, 45) take@sixty;;a3 (d3, 40) take@forty;;a4 (d2, 35) reject: N₂ = 3 > 2@thirty five;;a5 (d4, 25) take,  a6 (d1, 15) reject@twenty five;;penalty 35 + 15 = 50@fifty"
Those sets form a matroid, so greedy applies. Take tasks by penalty: sixty and forty five are taken, then forty. Thirty five is rejected, because three tasks would have deadline two or earlier. Twenty five is taken, and fifteen is rejected. The total penalty is fifty.

@chapter Common slips
@list heading="Common slips" items="Assuming every hereditary family is a matroid@The first|Believing matroids explain every greedy algorithm@The second|Scheduling the early tasks by penalty@the third"
The first slip is assuming every hereditary family is a matroid. The second is believing matroids explain every greedy algorithm. And the third is running the early tasks in order of penalty. Greedy chooses them by penalty, but they run in order of deadline.

@chapter Try it
@words text="raise a6's penalty to 70" sub="early set, schedule, total penalty"
Your turn. Raise the last task's penalty from fifteen to seventy. Run greedy by hand, give the early set, the schedule and the total penalty, and check that every rejection is forced.

@end text="Test a family yourself"
You can test families for the exchange property and race greedy against the optimum, on Learn. That's learn dot get er done dot I O.
