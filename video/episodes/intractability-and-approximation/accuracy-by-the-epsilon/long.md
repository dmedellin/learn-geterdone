---
format: long
lesson: intractability-and-approximation/accuracy-by-the-epsilon
title: The knapsack approximation scheme: you choose the accuracy
thumb: Name your epsilon
---

@chapter Choose the accuracy
@title text="Accuracy by the Epsilon" sub="Intractability and Approximation" art=thumb
Vertex cover's factor of two is fixed by the algorithm. This last strategy lets you choose the accuracy. Name an epsilon, and pay for it in table size.

@words text="within 1 + ε of the optimum" sub="fully polynomial: polynomial in n and 1/ε"
An approximation scheme is a family of algorithms, one for each epsilon, each polynomial in the input, returning a value within one plus epsilon of the optimum. It's fully polynomial when the time is also polynomial in one over epsilon, so halving the error doesn't square the cost.

@chapter Scale the values
@art value-table
The knapsack has an exact table indexed by achievable value. Its size is the sum of the values, and that's what makes it only pseudo polynomial. So shrink the values.

@list heading="The scheme" items="K = ε · vmax / n@Let K be|Round every value down by K@round it down|Solve the scaled instance exactly@solve the scaled|Keep the items, at their original prices@original prices"
Let K be epsilon times the largest value, over n. Divide every value by K and round it down. Solve the scaled instance exactly, with a much smaller table. Then return the chosen items, valued at their original prices.

@art set-not-number
That last step matters. The answer is the set of items, not the scaled number. The scaled optimum is a value in the wrong units, about a different instance.

@chapter Why it loses at most ε · OPT
@art rounding-down
Each rounding trims a little off every value, never more than K.

@math heading="The guarantee" items="rounding loses < K per item@less than K;;total loss ≤ n · K = ε · vmax@n times K;;vmax ≤ OPT@the best single item;;loss ≤ ε · OPT@epsilon times"
Rounding down loses less than K per item. So the total loss is at most n times K, which is epsilon times the largest value. And the best single item fits on its own, so the largest value is at most the optimum. So the loss is at most epsilon times the optimum.

@chapter Six items
@math heading="Capacity 12,  ε = 1/10" items="vmax = 902,  n = 6@nine hundred and two;;K = 902/60 = 451/30 ≈ 15.03@fifteen;;scaled: 34, 40, 53, 20, 60, 30@scaled values;;chosen value 1935 = OPT,  loss 0@nineteen thirty five"
Six items, capacity twelve, epsilon one tenth. The largest value is nine hundred and two, so K is nine oh two over sixty, about fifteen point oh three. The scaled values are thirty four, forty, fifty three, twenty, sixty and thirty. The table picks the first three, whose original value is nineteen thirty five, exactly the optimum.

@words text="238 cells  vs  3604" sub="promised loss ≤ 193.5 · realised 0"
The promise allowed a loss of a hundred and ninety three point five. The realised loss was zero. And the scaled table has two hundred and thirty eight cells, against the exact table's three thousand six hundred and four.

@art epsilon-sweep
That's the trade: a promise of losing up to a tenth, bought with a table one fifteenth the size. On this instance, the promise was never called in.

@math heading="The epsilon sweep" items="ε = 1:  24 cells@twenty four;;ε = 1/2:  47@forty seven;;ε = 1/4:  95@ninety five;;ε = 1/32:  765@one thirty second"
Sweep epsilon down. At one, twenty four cells. At a half, forty seven. A quarter, ninety five. Down to one thirty second, seven hundred and sixty five. The cells roughly double as epsilon halves, and the loss stays zero every time, because this instance is kind.

@chapter When it costs more
@art scaling-backfires
Now the five small items from the branch and bound lesson, capacity ten. The exact table has thirty two cells. At epsilon one tenth, K is nine fiftieths, less than one. Dividing by it makes the values bigger. The scaled table needs a hundred and seventy one cells, more than five times as many, for the same exact answer.

@words text="ε = 1:  15 vs 16" sub="loss 1, inside a promise of 16"
At epsilon one, it returns fifteen against an optimum of sixteen, a loss of one inside a promise of sixteen. So the only epsilon where the promise was needed is one nobody would choose.

@art weak-hardness
So a scheme is an asymptotic device. Its saving comes from large values, and on small ones the scaling is counterproductive, not merely useless. The asymptotically better method loses on the instance on screen. And it only works because knapsack is weakly NP hard: there's a table polynomial in the numbers, and the scheme makes the numbers small enough to afford it.

@chapter Where people slip
@list heading="Common slips" items="Reporting the scaled value@The first|Assuming smaller ε is always better@The second|Running a scheme on a tiny instance@And the third"
The first slip is reporting the scaled value as the answer. The second is assuming a smaller epsilon is always better. You pay for a bound on a loss you may never incur. And the third is running a scheme where K falls below one. Check the scale factor first.

@end text="Name your epsilon"
Sweep epsilon and watch cells against loss, on Learn. That's learn dot get er done dot I O.
