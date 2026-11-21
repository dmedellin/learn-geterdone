---
format: long
lesson: networks-flows-paths-and-assignments/the-minimum-cost-flow-programme
title: One linear programme that is four network problems
thumb: Four problems, one matrix
---

@chapter The claim
@title text="The Minimum-Cost Flow Programme" sub="Networks, Flows, Paths and Assignments" art=thumb
Transportation, assignment, shortest path and maximum flow are usually taught as four algorithms. Here's the surprise. They're one linear programme, and only the data changes.

@math heading="Minimum-cost flow" items="min cᵀx@minimise;;N x = b@N x equals b;;0 ≤ x ≤ u@between zero"
The programme is short. Minimise the total cost, c transpose x, subject to N x equals b, with each flow between zero and its capacity. N is the node arc incidence matrix, and b is the vector of supplies.

@chapter The incidence matrix
@art incidence-columns
N has one row per node and one column per arc. Each column holds plus one at the arc's tail, minus one at its head, and zero everywhere else. Then row i reads what leaves node i minus what arrives, so N x equals b is conservation at every node at once.

@words text="Every column: one +1, one −1" sub="so the rows sum to the zero row"
Because every column has exactly one plus one and one minus one, the rows always sum to zero. That's the same fact as the supplies summing to zero, seen from the other side. One node equation is always implied by the rest.

@chapter A small example
@math heading="Arcs s→a, s→b, a→b, a→t, b→t" items="costs 2, 3, 1, 5, 2;  capacities 3, 3, 2, 3, 3@costs two;;4 node rows + 5 capacity rows = 9 rows@nine rows;;x = (3, 1, 2, 1, 3)@the optimum;;cost = 22@twenty two"
The lesson's network has four nodes and five arcs, with costs two, three, one, five and two, and every capacity three except two on a to b. Four units go from s to t. That's four node rows and five capacity rows, nine rows in all. The optimum is three, one, two, one, three, at a cost of twenty two.

@words text="Every value came out whole" sub="no integrality constraint anywhere"
Look at those five numbers. Every one is a whole number, and nothing asked for that. There's no integer constraint anywhere. It came out whole because of what N is, and that's proved later in the course.

@chapter The same programme, four times
@art one-matrix
Now keep the matrix and the objective, and change only what's typed into the boxes. Four famous problems fall out.

@art transport-bipartite
Transportation: two sources, three sinks, an arc from every source to every sink, no capacities. The programme has five rows, just the nodes, and six columns. The optimum costs two hundred and forty five.

@art assignment-pairs
Assignment: three workers, three jobs, every arc at capacity one, every supply one and every demand minus one. Fifteen rows, nine columns, and the optimum is nine. Every variable comes out zero or one, and no binary variable was declared.

@art shortest-route
Shortest path: one unit supplied at the source, one demanded at the sink, and the costs read as lengths. Moving one unit as cheaply as possible means moving it along the shortest route. On the lab's data the optimum is six. Bellman Ford's label at the sink is the same six.

@art return-arc
Maximum flow: price every arc at zero, and add one unbounded arc from the sink back to the source, priced at minus one. Supply nothing anywhere. The only way to earn is to run flow round the loop, so the optimum of minus five means the maximum flow is five.

@chapter What it buys, and what it costs
@list heading="Trade-off" items="Buys: duals and complementary slackness for all four@What it buys|Costs: speed against specialised methods@What it costs"
What it buys is that everything you know about linear programmes now applies to all four, including duals and complementary slackness. What it costs is speed. A specialised method will beat a general tableau on a large network. But when a hand method and the programme disagree, the programme isn't the one that's wrong.

@chapter Where people slip
@list heading="Common slips" items="Writing N row by row@The first|A capacity row for every arc@The second|Treating the four problems as analogies@And the third"
The first slip is writing N row by row, which loses the signs. Build it column by column instead. The second is adding a capacity row for every arc out of tidiness. A row can bind and get a shadow price. And the third is treating the four problems as analogies. They're one programme.

@chapter Try it
@words text="Build N column by column" sub="s→a, s→b, a→b, a→t, b→t"
Your turn. Write down the incidence matrix for the small example, one column per arc, with plus one at each tail and minus one at each head. Then check that every column holds exactly one of each, and that the four rows add to zero.

@end text="Four data sets, one tableau"
You can switch between all four problems and watch the same tableau solve them, on Learn. That's learn dot get er done dot I O.
