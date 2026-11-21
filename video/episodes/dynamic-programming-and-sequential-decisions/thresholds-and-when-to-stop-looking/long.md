---
format: long
lesson: dynamic-programming-and-sequential-decisions/thresholds-and-when-to-stop-looking
title: When to stop looking: the threshold rule, measured
thumb: Take it if it beats waiting
---

@chapter The problem
@title text="Thresholds and When to Stop Looking" sub="Dynamic Programming and Sequential Decisions" art=thumb
You're selling something. One offer arrives each period. Take it and stop, or wait and pay to keep looking. And the deadline is coming. When should you say yes?

@art offer-stream
Here's the model. In each of T periods, one offer arrives, drawn independently from a distribution you know. Refuse it and you pay a search cost c to go on, and you can't call it back. Refuse the last one and you get nothing.

@chapter The recursion
@math heading="Sell or wait" items="V(0) = 0@zero;;V(t) = E[ max(x, V(t−1)) ] − c@the expected value;;accept x  ⇔  x > V(t−1)@accept"
Let V of t be what the remaining search is worth with t periods left. With none left it's zero. Otherwise it's the expected value of the better of the offer and carrying on, minus the cost. So accept an offer exactly when it beats V of t minus one.

@art threshold-line
That's a threshold. Each period has one number, the value of carrying on. Offers above it are taken. Offers below it are refused.

@chapter A worked search
@words text="Offers 10, 20, 30, each ⅓" sub="c = 1 · T = 3"
Here's the lesson's instance. Offers of ten, twenty or thirty, each with probability one third. A look costs one, and there are three periods.

@math heading="Filled from the deadline" items="V(1) = (10 + 20 + 30)/3 − 1 = 19@nineteen;;V(2) = (19 + 20 + 30)/3 − 1 = 22@twenty two;;V(3) = (22 + 22 + 30)/3 − 1 = 71/3@seventy one thirds"
With one left, take anything: the mean is twenty, minus one, nineteen. With two left, a ten gets replaced by the nineteen of carrying on: sixty nine over three, minus one, twenty two. With three left, ten and twenty both become twenty two, giving seventy one thirds, about twenty three point six seven.

@art falling-thresholds
Read the rule down the table. With three left, only thirty. With two, twenty or thirty. With one, anything. The bar falls as the deadline nears. That's the opposite of how impatience feels, but you're comparing each offer against the chances that remain, and there are fewer of them every period.

@chapter Measured, not assumed
@art accept-sets
But is the best rule really a threshold? The recursion can't tell you, because it only ever compares against one number. So the lab enumerates every rule: nine yes or no choices, three offers in three periods, so five hundred twelve rules, each evaluated exactly.

@words text="Best of 512: 71/3" sub="and it is a threshold rule"
The best is worth seventy one thirds, its accept sets match the thresholds, and in every period accepting an offer means accepting every larger one. So here the threshold shape is a measured fact.

@chapter Tails and costs
@art rare-tail
Now a rare high offer. Eight, fourteen or forty, the forty only one time in ten, over four periods. With three or four left, you refuse everything but forty. The search is worth about seventeen point three six, against a mean offer of thirteen. Remove the forty and it's worth a little over ten.

@art cost-eats-option
And expensive searching. Offers of ten or thirty, a look costing five. At that cost a second look adds five halves, a third five quarters, and a fourth only five eighths. The cost eats the option value.

@chapter Where people slip
@list heading="Common slips" items="Comparing against V(t), not V(t−1)@The first|Expecting the bar to rise near the deadline@The second|Thinking the recursion proved the shape@And the third"
The first slip is comparing against V of t instead of V of t minus one, which raises every threshold one period too high. The second is expecting the bar to rise near the deadline. With one period left, you give up nothing, so it's on the floor. And the third is thinking the recursion proved the threshold shape. The enumeration did.

@words text="Known, independent offers" sub="no learning · no recall · same cost each period"
And remember what the model leaves out. Offers are independent draws from a distribution you already know, so the offers you've seen tell you nothing about the next. No recall, and the same cost every period. Change any of that and the threshold is exactly right for the wrong problem.

@chapter Try it
@words text="Offers 10 or 30, each ½" sub="four periods · c = 1"
Your turn. Offers of ten or thirty, equally likely, four periods, and a look costs one. Compute the thresholds. Working from four periods left down to one, you should get one hundred and three over four, forty seven halves, nineteen, and zero. Then raise the cost to five and see which thresholds move.

@end text="Find the threshold, then test it"
You can change the offers and the cost and watch all five hundred twelve rules get tested, on Learn. That's learn dot get er done dot I O.
