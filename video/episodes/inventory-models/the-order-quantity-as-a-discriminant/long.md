---
format: long
lesson: inventory-models/the-order-quantity-as-a-discriminant
title: The order quantity as a discriminant: EOQ without calculus
thumb: The roots collide
---

@chapter A different question
@title text="The Order Quantity as a Discriminant" sub="Inventory Models" art=thumb
Finding the cheapest order quantity sounds like calculus. But ask a different question, and plain algebra hands you the answer, with a proof attached.

@art budget-line
Don't ask for the minimum. Ask: is there any order quantity costing at most T per unit time? That's a yes or no question about one inequality.

@chapter Make it a quadratic
@math heading="Is any Q within budget?" items="K·D/Q + h·Q/2 ≤ T,   Q > 0@at most T;;K·D + h·Q²/2 ≤ T·Q@multiply;;h·Q²/2 − T·Q + K·D ≤ 0@a quadratic"
Start with K D over Q plus h Q over two, at most T, with Q positive. Multiply through by Q. Then move everything to one side, and you have a quadratic in Q, at or below zero.

@art sign-flip-warning
That multiplication is legal only because Q is positive. Multiply an inequality by a negative number and it flips. This is the one place a condition on the variable does real work, so say it out loud.

@art upward-parabola
The leading coefficient is h over two, which is positive, so the parabola opens upward. It's at or below zero exactly between its two roots, and nowhere else.

@chapter The discriminant decides
@math heading="Discriminant" items="T² − 4·(h/2)·(K·D) = T² − 2hKD@T squared;;> 0: an interval@positive;;= 0: one point@zero;;< 0: nothing@negative"
The discriminant is T squared minus two h K D. If it's positive, there's an interval of quantities within budget. If it's zero, exactly one. If it's negative, none at all.

@chapter Walk the budget down
@words text="3Q² − T·Q + 120000 ≤ 0" sub="K = 100 · D = 1200 · h = 6 · 2hKD = 1440000"
Use the workshop from last time. K is a hundred, D is twelve hundred, h is six. The quadratic is three Q squared minus T Q plus a hundred and twenty thousand, and two h K D is one million four hundred forty thousand.

@math heading="Lower T" items="T = 1300:  roots 400/3 and 300@thirteen hundred;;T = 1260:  210 ± 10√41@twelve sixty;;T = 1200:  200, twice@twelve hundred;;T = 1199:  discriminant −2399, none@eleven ninety nine"
At thirteen hundred, the discriminant is a perfect square, and the roots are four hundred thirds and three hundred. At twelve sixty, they're two ten plus or minus ten root forty one. At twelve hundred, the discriminant is zero, and both roots are two hundred. At eleven ninety nine, it's minus two thousand three hundred ninety nine. No roots.

@art closing-interval
So as the budget tightens, the interval of affordable quantities closes in, until it's a single point. Each step is a fresh quadratic with a fresh discriminant, and at thirteen hundred both ends cost exactly thirteen hundred, so the interval is closed at both ends.

@chapter The collision is the proof
@art double-root
The roots collide when T equals the square root of two h K D. There, the single root is T over h, which is the square root of two K D over h. That's the economic order quantity.

@words text="Existence, uniqueness, optimality" sub="no second derivative to check"
And it's a complete proof. No smaller budget works, because the discriminant would be negative. This one quantity meets this budget, so it's the unique cheapest. No calculus, and no maximum to rule out, because an upward parabola can't dip below zero outside its roots.

@art missed-axis
And eleven ninety nine isn't an arithmetic failure. The parabola just misses the axis, and that's the proof that no quantity at all costs that little on this data.

@chapter Same as the flat band
@words text="T = 1260 = 105% of C*" sub="roots ≈ 145.9688 … 274.0312"
Set the budget as a percentage of the minimum, and you get last lesson's flat band. At a hundred and five percent, the roots are about one forty six and two seventy four, the same as the five percent band. Still a hundred and twenty eight units wide. That's the flatness seen from underneath.

@chapter Where people slip
@list heading="Common slips" items="Forgetting Q > 0@The first|Reading the sign backwards@The second|Rounding the surd before the collision@And the third"
The first slip is forgetting that the multiplication needs Q to be positive. The second is reading the sign backwards. Negative means no answer, not a small one. And the third is rounding the square root before the collision. Then the roots come out a few thousandths apart, and the whole argument disappears into rounding.

@chapter Try it
@words text="T = 1320" sub="3Q² − 1320Q + 120000 ≤ 0"
Your turn. With a budget of thirteen twenty, find the discriminant and the two roots. You should get two twenty plus or minus twenty root twenty one, and check that matches the ten percent band.

@end text="Walk the budget down"
You can lower the budget and watch the two roots collide, on Learn. That's learn dot get er done dot I O.
