---
format: long
lesson: dynamic-programming/the-knapsack-table-and-what-each-cell-reads
title: The 0/1 knapsack table: every cell reads exactly two
thumb: Skip it, or take it
---

@chapter The question
@title text="The Knapsack Table, and What Each Cell Reads" sub="Dynamic Programming and Optimal Substructure" art=thumb
You've got a bag that holds a fixed weight, and items you must take whole or leave behind. Sorting by value per weight solved the version where you could cut items. Without cutting, that rule breaks, and you need a table.

@art knapsack-bag
That's the zero one knapsack. Given items with whole number weights and values, and a capacity W, choose a subset that fits and has the greatest total value. Zero one means each item is taken whole, or not at all.

@chapter Where the rule gets 8
@math heading="Capacity 7  ·  weight / value" items="A 1/1 · B 3/4 · C 4/5 · D 5/7@four items;;densities: 1, 1.33, 1.25, 1.4@densities;;densest first: D then A → weight 6, value 8@Densest first;;table: B and C → weight 7, value 9@The table"
Four items, written weight over value: one over one, three over four, four over five, and five over seven. Their densities are one, one point three three, one point two five, and one point four. Densest first takes D, leaving room for two, so only A fits. Value eight. The table finds B and C, weight exactly seven, value nine.

@art no-cutting
The density rule worked for the fractional problem because you could cut the last item to fit. Take that away, and the exchange argument has nothing left to exchange.

@chapter The recurrence
@math heading="Knapsack" items="V(0, w) = 0@V of zero;;V(i, w) = V(i − 1, w)  if weight(i) > w@doesn't fit;;else  max( V(i − 1, w),  value(i) + V(i − 1, w − weight(i)) )@the larger"
Let V of i, w be the best value from the first i items, with capacity w. V of zero, w is zero. If item i doesn't fit, V of i, w is just the cell above. Otherwise, it's the larger of skipping item i, or taking it, plus the best from the earlier items in the room that's left.

@art skip-or-take
Why? An optimal subset either contains item i or it doesn't. If not, it's an optimal subset of the earlier items. If it does, what's left must be optimal in the smaller capacity, or you could swap in something better.

@chapter What each cell reads
@art two-reads
The lab paints the cells each cell reads. For row three, column seven, they're row two, column seven, which means skip the third item, and row two, column three, which means take it and look back four columns.

@words text="Recorded reads, not a description" sub="collected while the cell was computed"
That list isn't a picture of the recurrence written beside it. It's collected from the reads the code actually performed. So it records what the code did, not what its author believed.

@art grid-axes
Every cell reads exactly two, so the work is order one per cell. The rows count items, n plus one of them. But the columns are capacities from zero to W. That's a value from the input, not a count of anything. Here that's forty cells.

@chapter Pseudo-polynomial
@math heading="Θ(nW)" items="capacity 7:  40 cells@capacity seven;;capacity 99:  500 cells@ninety nine;;capacity 99 999:  500 000 cells@ninety nine thousand"
The table is Theta of n W. That looks polynomial, but W takes only about log W digits to write down. At capacity seven, forty cells. At ninety nine, five hundred. At ninety nine thousand nine hundred and ninety nine, five hundred thousand. Three more digits, a thousand times the work.

@words text="Pseudo-polynomial" sub="polynomial in the value · exponential in the length"
That's called pseudo polynomial: polynomial in the numbers' values, but exponential in the length of the input. It's why knapsack can be NP hard and still solvable by a table.

@chapter Reading the answer back
@art walk-back
To get the items back, walk up from the corner. An item was taken wherever the row drops by one and the column moves. But a wrong walk still gives a perfectly neat list of items. So the panel re weighs the list against the capacity, and re values it against the table's number.

@chapter Where people slip
@list heading="Common slips" items="Carrying the density rule across from the fractional problem@The first|Reading Θ(nW) as polynomial@The second|Accepting a reconstruction because it's well formed@The third"
The first slip is carrying the density rule across from the fractional problem. Four items refute it. The second is reading Theta of n W as polynomial and stopping there. The third is accepting a reconstruction just because it's well formed. Re weighing costs two additions per item.

@chapter Try it
@words text="V(4, 7)" sub="which two cells does it read?"
Your turn. Item D weighs five and is worth seven. Write down the two cells that V of four, seven reads, and which one wins. Then walk back to the items, re weigh them, and check they fit in seven.

@end text="Watch each cell's two reads"
You can fill the knapsack table and see exactly which cells each one read, on Learn. That's learn dot get er done dot I O.
