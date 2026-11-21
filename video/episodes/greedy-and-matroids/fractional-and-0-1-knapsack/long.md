---
format: long
lesson: greedy-and-matroids/fractional-and-0-1-knapsack
title: Fractional vs 0/1 knapsack: one greedy rule, two very different fates
thumb: Cut it, and greedy is exact
---

@chapter The question
@title text="Fractional and 0/1 Knapsack" sub="Greedy Algorithms and Matroids" art=thumb
You've got a bag with a weight limit and a pile of items, each with a weight and a value. What's the most value you can carry? The answer depends on one question. Are you allowed to cut an item?

@art knapsack-items
In the fractional problem, you can take any fraction of an item. In the zero one problem, you take it whole or not at all. Either way, an item's density is its value divided by its weight, value per unit of weight.

@chapter Density greedy
@words text="Sort by density · fill · cut the last one"
The greedy rule is natural. Sort items by density, highest first. Take each one whole while it fits, and when one doesn't, take whatever fraction of it still fits.

@math heading="Capacity 50  ·  weight / value" items="A 10/60:  density 6@A weighs ten;;B 20/100:  density 5@B weighs twenty;;C 30/120:  density 4@C weighs thirty"
The lab opens with capacity fifty. A weighs ten and is worth sixty, density six. B weighs twenty and is worth a hundred, density five. C weighs thirty and is worth a hundred and twenty, density four.

@math heading="Fractional" items="A whole: 60@takes A whole;;B whole: 100@B whole;;2/3 of C: 80@two thirds of C;;60 + 100 + 80 = 240@two hundred and forty"
Greedy takes A whole, then B whole, which uses thirty of the fifty. Then it takes two thirds of C, worth eighty. That's sixty plus a hundred plus eighty, exactly two hundred and forty.

@art fractional-fill
The bag is full to the brim, with exactly one item cut. That's the only cut greedy ever needs.

@art weight-shift
Why is that optimal? Suppose a solution takes a denser item only partly, while taking some of a less dense one. Shift a little weight from the less dense item to the denser one, and the value can only go up. Keep doing that, and you arrive at greedy's answer.

@chapter Refuse to cut
@math heading="0/1, same rule" items="take A: 10 used, value 60@takes A;;take B: 30 used, value 160@then B;;C needs 30, only 20 left  →  stop at 160@cannot fit C;;optimum: B + C = 220@two hundred and twenty"
Now items must go whole. Density greedy takes A, then B, thirty used and a hundred and sixty in value. It cannot fit C, which needs thirty with only twenty left. It stops at a hundred and sixty. But B and C together fit exactly, for two hundred and twenty.

@art whole-items
The exchange argument is gone. It relied on shifting a little weight between items, and with whole items, that move isn't allowed.

@list heading="Other orders, same instance" items="By value: C, B → 220@By value|By weight: A, B → 160@By weight"
The panel offers other orders. By value, highest first, greedy takes C then B, and reaches two hundred and twenty, the optimum. By weight, lightest first, it takes A and B for a hundred and sixty.

@words text="1/2, 50/100 · capacity 50" sub="density greedy: 2 · optimum: 100"
It gets worse. Take one item weighing one and worth two, and another weighing fifty and worth a hundred, with capacity fifty. Density greedy grabs the crumb, worth two, and stops. The optimum is a hundred. Plain density greedy has no guarantee at all.

@chapter The half guarantee
@math heading="Two arms" items="g = density greedy's value@g be;;s = best single item that fits@s the value;;max(g, s) ≥ OPT / 2@at least half"
Here's the fix. Let g be what density greedy gets, and s the value of the best single item that fits. Take whichever is bigger. That's guaranteed to be at least half the optimum, on every instance.

@math heading="Why" items="OPT ≤ fractional optimum ≤ g + vᵢ@the fractional optimum;;vᵢ ≤ s@fits by itself;;OPT ≤ g + s ≤ 2 max(g, s)@twice the bigger"
Let i be the first item greedy rejects. The zero one optimum is at most the fractional optimum, which is at most g plus the value of i. And i fits by itself, so its value is at most s. So the optimum is at most g plus s, at most twice the bigger of the two.

@art half-floor
On the opening instance, the arms are a hundred and sixty and a hundred and twenty, so the answer is a hundred and sixty, against a promise of a hundred and ten.

@art crumb
On the crumb instance, the single item arm gives a hundred, the optimum, fifty times what density greedy found. A guarantee is a floor, not an estimate.

@chapter Where people slip
@list heading="Common slips" items="Comparing the 0/1 rule with the fractional optimum@The first|Concluding that value first is the better rule@The second|Reading a measured ratio as the guarantee@The third"
The first slip is comparing the zero one answer with the fractional optimum, which mixes two shortfalls. The second is concluding value first is better. It's unbounded too. The third is mixing up measurements and guarantees. Measured ratios here run from three fifths to one. The promise is a half.

@chapter Try it
@words text="1/2 · 10/10 · 10/10 · capacity 20"
Your turn. Items weighing one worth two, and two weighing ten worth ten, with capacity twenty. Run density greedy and value first by hand. Then take the better of greedy and the best single item, and check it's at least half the optimum.

@end text="Fill the knapsack yourself"
You can try every rule on your own items and see the half guarantee hold, on Learn. That's learn dot get er done dot I O.
