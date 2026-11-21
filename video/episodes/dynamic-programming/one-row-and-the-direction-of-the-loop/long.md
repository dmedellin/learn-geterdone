---
format: long
lesson: dynamic-programming/one-row-and-the-direction-of-the-loop
title: One row knapsack: the loop direction decides the problem
thumb: Backward once, forward forever
---

@chapter The question
@title text="One Row, and the Direction of the Loop" sub="Dynamic Programming and Optimal Substructure" art=thumb
The knapsack table can shrink to a single row. But once it does, the direction you sweep that row stops being a detail. One way, each item is used at most once. The other way, items can be reused. Same three lines of code.

@art row-above
Look at the recurrence again. Each cell reads two cells, both in the row directly above. Nothing ever reads two rows up, and once a row is finished, the one above it is never read again. So you don't need to keep the whole table.

@chapter The one row form
@math heading="One row" items="row[0..W] = 0@initialised to zero;;row[w] = max(row[w],  row[w − weight(i)] + value(i))@row of w;;for w from weight(i) to W,  in some order@in some order"
Keep one array, row zero to W, initialised to zero. For each item, update row of w to the larger of row of w, and row of w minus the item's weight, plus its value. Do that for every w from the item's weight up to W, in some order. The recurrence doesn't say which order.

@art backward-sweep
Sweep backward, from W down. When you update w, the cell you read is to the left, and you haven't touched it yet in this pass. So it still holds the value from before this item. The item can be used at most once, and the row is exactly the zero one grid.

@art forward-sweep
Now sweep forward. The cell you read has already been updated in this pass, so it may already include a copy of this item. Add one more, and you've got two. The pass can stack as many copies as fit. That's the unbounded knapsack, solved correctly.

@chapter Three items, capacity eleven
@words text="2/3 · 3/5 · 5/9" sub="capacity 11 · weight / value"
Take three items, written weight over value: two over three, three over five, and five over nine, with capacity eleven.

@math heading="Final rows" items="backward:  0 0 3 5 5 9 9 12 14 14 17 17  →  17@Swept backward;;forward:  0 0 3 5 6 9 10 12 14 15 18 19  →  19@Swept forward"
Swept backward, the row ends on seventeen. That's all three items, weight ten. Swept forward, it ends on nineteen. That's two copies of three over five, and one five over nine, weight exactly eleven. The full grid and all eight subsets agree on seventeen.

@chapter The first item
@math heading="After item 2/3" items="backward:  0 0 3 3 3 3 3 3 3 3 3 3@Backward;;forward:  0 0 3 3 6 6 9 9 12 12 15 15@Forward"
The difference shows up after the very first pass. Backward, item two over three leaves three in every cell from two on. One copy is all any capacity holds. Forward, it leaves three, then six, then nine, twelve and fifteen. At capacity four it's been taken twice, at six, three times.

@art stacking
Each forward step built on the value it had just written two cells earlier. That's the whole mechanism. Which way the loop counts decides which row each read lands in, and the code never names a row at all.

@chapter What the collapse costs
@art lost-pointers
There's a price. The full grid lets you walk back to find which items were taken. One row can't, because by the time you know the answer, every intermediate value has been overwritten. One row tells you what the optimum is, not what it's made of.

@math heading="The trade" items="time: Θ(nW) in both@time;;space: Θ(nW) → Θ(W)@space;;here: 48 cells vs 12 numbers@forty eight"
Time is Theta of n W either way. Space falls from Theta of n W to Theta of W. Here, that's forty eight cells against twelve numbers, a saving too small to notice. The space bound is what makes the trick worth knowing, not this instance.

@chapter Where people slip
@list heading="Common slips" items="Treating the sweep direction as taste@The first|Calling the forward sweep a bug@The second|Collapsing, then asking for the contents@The third"
The first slip is treating the direction as a matter of taste. It picks which problem you solve. The second is calling the forward sweep a bug. It's the unbounded knapsack, done right. The bug is only a mismatch with the problem. The third is collapsing the table, then discovering you needed the items.

@art two-arrows
So before you write the loop, write down which row you intend each read to hit. One way gives the zero one answer, the other gives the unbounded one, and both are correct algorithms.

@chapter Try it
@words text="item 3/5 · capacity 6" sub="sweep both ways"
Your turn. Take just the item three over five, with capacity six. Sweep a row of zeros backward, then forward, and write out both rows. Which one used the item twice?

@end text="Flip the loop direction yourself"
You can sweep the row both ways and watch the two answers split, on Learn. That's learn dot get er done dot I O.
