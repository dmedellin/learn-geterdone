---
format: long
lesson: dynamic-programming-and-sequential-decisions/value-iteration-and-the-fixed-point
title: Value iteration vs solving the fixed point exactly
thumb: Solve it, don't chase it
---

@chapter No last period
@title text="Value Iteration and the Fixed Point" sub="Dynamic Programming and Sequential Decisions" art=thumb
Every table so far was filled from the end. So what happens when there is no end?

@art no-end
Take the horizon away and the recursion has no base case to start from. But the value still has to satisfy something: what a state is worth is its reward, plus a discounted average of what the states it leads to are worth.

@math heading="An equation, not a recursion" items="v = r + γPv@v equals;;(I − γP) v = r@rearranged"
In symbols, v equals r plus gamma P v. Rearranged, I minus gamma P, times v, equals r. That's a linear system, and you can solve it.

@words text="0 ≤ γ < 1  ⇒  one solution"
The discount gamma is between zero and one, not including one. That makes I minus gamma P invertible for every transition matrix, so there's exactly one answer. The discount is doing mathematical work, not just expressing patience.

@chapter Solve it exactly
@art two-state-chain
Here's the lesson's chain. The first state goes to each state with probability one half. The second goes to the first a quarter of the time, and stays three quarters. Rewards are one and three, and the discount is one half.

@math heading="(I − γP) v = r" items="¾ v₁ − ¼ v₂ = 1@three quarters;;−⅛ v₁ + ⅝ v₂ = 3@minus an eighth;;v₁ = 22/7,  v₂ = 38/7@twenty two sevenths"
Write it out. Three quarters v one, minus a quarter v two, equals one. Minus an eighth v one, plus five eighths v two, equals three. Row reduction gives v one equals twenty two sevenths, and v two equals thirty eight sevenths.

@math heading="Put them back" items="¾·22/7 − ¼·38/7 = 66/28 − 38/28 = 1@sixty six;;−⅛·22/7 + ⅝·38/7 = 168/56 = 3@one sixty eight"
Now check. Sixty six twenty eighths minus thirty eight twenty eighths is exactly one. And one sixty eight over fifty six is exactly three. The residual is zero, with nothing rounded.

@art fixed-point
That's why the arithmetic stays exact. In decimals, a residual of ten to the minus sixteen looks just like a small error. As fractions it's zero, and you can check it by hand.

@chapter Value iteration
@art iterates-approach
Value iteration does something else. Start at zero and apply the map again and again. v one is just r, one and three. Then two and seventeen quarters. Each step multiplies the gap by gamma P, so it shrinks by about a half each step.

@math heading="State 1, from zero" items="v₄ = 365/128@three sixty five;;v₈ = 1638205/524288@step eight;;v₁₂ = 6746787645/2147483648 ≈ 3.14171782@twelve steps;;exact: 22/7 = 3.142857…@twenty two sevenths"
At step four, state one is three sixty five over one twenty eight. By step eight, the denominator has six digits. After twelve steps it has ten, and the value is about three point one four one seven. The exact answer, twenty two sevenths, was available at step zero.

@art growing-denominators
That denominator column is what decimals hide. Each iterate is a different fraction, with one more power of two below it. None of them is twenty two sevenths, and each is more expensive to write down.

@chapter A patient discount
@art patient-discount
Now raise the discount to nine tenths. The fixed point becomes six seventy over thirty one and seven fifty over thirty one, about twenty one point six and twenty four point two. Row reduction still takes four operations. Value iteration now shrinks the gap by only nine tenths each step, and after twelve steps it's nowhere near.

@chapter Why iterate at all
@list heading="Value iteration still earns its place" items="No inverse needed@no inverse|State spaces too big to write down@too big|A maximum inside the map@a maximum"
So is value iteration a mistake? No. It needs no inverse and no elimination. It works when the state space is too big to write the matrix down. And it extends to choosing an action in each state, where a maximum sits inside the map and the system stops being linear.

@chapter Where people slip
@list heading="Common slips" items="Reading v = r + γPv as an assignment@The first|Treating γ as only a taste@The second|Calling value iteration a mistake@And the third"
The first slip is reading the equation as an assignment. It's a condition on the whole vector at once. The second is treating the discount as only a taste for the present. At gamma equals one, the system is singular. And the third is calling value iteration a mistake. It's about knowing which situation you're in.

@chapter Try it
@words text="Rewards 2, 0, 5 · γ = ¾" sub="v = 1508/163, 1096/163, 2192/163"
Your turn. The lesson's three state chain, with rewards two, zero and five and a discount of three quarters, solves to fifteen oh eight, ten ninety six and twenty one ninety two, all over one sixty three. Substitute them back, and check the residual is exactly zero.

@end text="Solve the fixed point exactly"
You can solve your own chain exactly and race value iteration against it, on Learn. That's learn dot get er done dot I O.
