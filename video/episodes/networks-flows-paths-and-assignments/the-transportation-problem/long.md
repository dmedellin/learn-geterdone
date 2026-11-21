---
format: long
lesson: networks-flows-paths-and-assignments/the-transportation-problem
title: The transportation problem: balance it, then start with m + n − 1 cells
thumb: Balance first, then count
---

@chapter The problem
@title text="The Transportation Problem" sub="Networks, Flows, Paths and Assignments" art=thumb
You have plants with goods, depots that want them, and a cost for every route. How much should each plant send to each depot, so the total bill is as small as it can be?

@art table-grid
Lay it out as a table. Sources down the side, destinations across the top, a unit cost in every cell. You choose an amount for each cell. Each row has to sum to that source's supply, and each column to that destination's demand.

@words text="Rows = supplies · Columns = demands" sub="the minimum-cost flow programme, with the drawing removed"
That's the minimum cost flow programme with the drawing taken away. The sources and destinations are the nodes, the cells are the arcs, and no arc has a capacity. The node equations just become row sums and column sums.

@chapter Balance the margins
@math heading="The three-plant table" items="supply: 15 + 25 + 10 = 50@fifteen plus;;demand: 5 + 15 + 15 + 15 = 50@five plus;;balanced: no dummy needed@balanced"
Before anything else, check the totals. On the lesson's table, three plants supply fifteen plus twenty five plus ten, which is fifty. Four depots demand five plus fifteen plus fifteen plus fifteen, also fifty. It's balanced. Only a balanced problem can be feasible, because both sets of equations add up to the total shipped.

@art dummy-column
When they don't agree, add a dummy. Three mills supply seventy five, and three yards want sixty five. So add a dummy destination that takes the extra ten, with a cost of zero in every cell. Whatever plan you choose, exactly ten units go to the dummy. They're the units that never move.

@art dummy-row
The other way round works the same. Two sources supply ten, three destinations want fifteen. Add a dummy source of five, with a row of zeros. Now the dummy row tells you which destinations go short, and by how much. That's genuinely useful output.

@chapter Count the cells
@math heading="Cells in a basis" items="m + n − 1@m plus n minus one;;3 + 4 − 1 = 6@three plus four"
A starting solution has to occupy exactly the right number of cells. With m sources and n destinations, that's m plus n minus one. For three plants and four depots, three plus four minus one is six. One equation is always implied by the others, which is why it isn't m plus n.

@art spanning-tree
Think of the rows and columns as two sets of dots, and each occupied cell as a line between a row and a column. The occupied cells must form a spanning tree: connected, so every potential gets a value, and with no cycle, so none is over determined.

@chapter Two ways to start
@art north-west-staircase
The north west corner rule fills the top left cell with as much as its row and column allow, crosses off whichever runs out, and moves on. It never looks at a single cost. The least cost rule picks the cheapest remaining cell each time instead. It's greedy.

@math heading="Starts on the three-plant table" items="north-west corner: 6 cells, cost 520@north west rule;;least cost: 6 cells, cost 475@least cost rule;;optimum: 435@optimum"
On the three plant table, the north west rule occupies six cells and costs five hundred and twenty. The least cost rule occupies six cells too and costs four hundred and seventy five, and one of its cells carries zero. The optimum is four hundred and thirty five. Neither start is close.

@chapter A start that can't be priced
@art broken-forest
On the lab's third table, the least cost rule occupies only four cells where five are needed, and they fall into two separate pieces. The potentials can't be solved for. The repair is a zero allocation in a cell that joins the two pieces without closing a cycle.

@words text="A basic zero is still in the basis"
Those zeros aren't decoration. A basic cell carrying zero has a potential equation, and it can be the one that leaves at the next pivot. Drop it, and the count goes wrong two steps later.

@chapter Where people slip
@list heading="Common slips" items="Pricing the dummy above zero@The first|Treating a zero allocation as an empty cell@The second|Crossing off a row and a column together@And the third"
The first slip is pricing the dummy at something other than zero. Every plan sends the same amount there, so a uniform price only adds a constant. The second is treating a zero allocation as an empty cell. And the third is crossing off a row and a column at the same step. Only one may go.

@chapter Try it
@words text="Supplies 4, 6 · Demands 5, 5, 5" sub="balance it, then count the cells"
Your turn. Take the shortfall example: two sources with four and six, three destinations wanting five each. Add the dummy it needs, check both totals reach fifteen, and work out how many occupied cells a basis must have.

@end text="Balance a table and start it"
You can balance a table, run both starting rules, and watch the cell count, on Learn. That's learn dot get er done dot I O.
