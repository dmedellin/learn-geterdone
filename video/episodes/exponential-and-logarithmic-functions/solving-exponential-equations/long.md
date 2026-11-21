---
format: long
lesson: exponential-and-logarithmic-functions/solving-exponential-equations
title: Solving exponential equations: match the powers or take a log
thumb: Get x out of the exponent
---

@chapter The unknown in the exponent
@title text="Solving Exponential Equations" sub="Exponential and Logarithmic Functions" art=thumb
Every equation before this put the unknown in the base, like x squared equals nine. Now it sits up in the exponent, as in three to the two x minus one equals eighty one. No dividing, factoring or root taking will move it. Two methods do.

@art stuck-exponent
Here's the decision. If both sides can be written as powers of the same base, match the exponents, and the answer is exact. If they can't, take a logarithm of both sides.

@chapter Matching powers
@words text="bᵘ = bᵛ   ⟺   u = v" sub="for b > 0,  b ≠ 1"
The first method rests on one fact. Exponentials are one to one: b to the u equals b to the v exactly when u equals v. That fails for b equals one, which is why that base is excluded everywhere.

@math heading="3^(2x − 1) = 81" items="3^(2x − 1) = 3⁴@three to the fourth;;2x − 1 = 4@two x minus one equals four;;x = 5/2@five halves;;check:   2·(5/2) − 1 = 4,    3⁴ = 81@To check"
Eighty one is three to the fourth, so both sides are powers of three. One to one gives two x minus one equals four, so x is five halves. Exact, and no logarithm needed. To check, two times five halves minus one is four, and three to the fourth is eighty one.

@art matched-powers
That only works when both sides are recognisable powers of one base. Five to the x equals seventeen isn't such an equation. Seventeen isn't a rational power of five at all.

@chapter Taking a logarithm
@art log-lowers
So take a logarithm of both sides. Equal positive numbers have equal logarithms, and the other way round, so the new equation has exactly the same solutions. Then the power law brings the exponent down. It's the only tool here that moves a variable out of an exponent.

@math heading="5ˣ = 17" items="ln(5ˣ) = ln 17@Take ln;;x·ln 5 = ln 17@power law;;x = ln 17 / ln 5@So x is;;x ≈ 1.760374@about one point seven six;;check:   5 < 17 < 25@To check"
Take ln of both sides, since both are positive. The power law gives x ln five equals ln seventeen. Divide by ln five, which isn't zero. So x is ln seventeen over ln five, about one point seven six. To check, seventeen is between five and twenty five, so x is between one and two.

@chapter The unknown on both sides
@math heading="4^(x + 1) = 3^(2x)" items="(x + 1)·ln 4 = 2x·ln 3@power law twice;;x·ln 4 + ln 4 = 2x·ln 3@Expand;;ln 4 = x·(2·ln 3 − ln 4)@collect;;x = ln 4 / ln(9/4) ≈ 1.709511@So x is"
With the unknown on both sides and different bases, take ln anyway. The power law twice gives x plus one, times ln four, equals two x ln three. Expand, collect the x terms, and factor out x. So x is ln four over ln of nine quarters, about one point seven one. It's a linear equation, with logs as coefficients.

@chapter A hidden quadratic
@art hidden-quadratic
Here's one that hides a quadratic: e to the two x, minus e to the x, minus six, equals zero. E to the two x is just e to the x, squared. So let u be e to the x.

@math heading="u = eˣ" items="u² − u − 6 = 0@u squared minus u;;(u − 3)(u + 2) = 0@factors;;u = 3    or    u = −2@three or minus two;;x = ln 3 ≈ 1.098612@x is ln three"
That gives u squared minus u minus six equals zero, which factors as u minus three, times u plus two. So u is three or minus two. Now undo the substitution. From u equals three, x is ln three, about one point oh nine nine.

@art rejected-root
And u equals minus two? Impossible, because e to the x is positive for every real x. The same fact settles two shapes on sight: b to the x equals zero has no solution, and nor does b to the x equals a negative number. Check that before taking a logarithm.

@chapter Where people slip
@art isolate-first
First, isolate the power. Five times two to the x equals forty becomes two to the x equals eight after dividing by five, and then x is three. No logarithm needed, and nothing to expand wrongly.

@list heading="Common slips" items="Treating the base as a coefficient@The first|Solving for u and stopping@The second|Expanding the log of a product wrongly@The third"
The first is treating the base as a coefficient. From three to the two x equals nine, you can't just divide by three. The second is solving for the substitution and stopping. U equals three is e to the x, not x. The third is expanding the log of a product wrongly. Log of five times two to the x is log five plus x log two.

@chapter Try it
@words text="4·3^(2x − 1) − 1 = 35" sub="isolated:    3^(2x − 1) = 9"
Your turn. Solve four times three to the two x minus one, minus one, equals thirty five. The isolation is given: three to the two x minus one equals nine. Decide whether you still need a logarithm, finish the exact solution, and check it in the original equation.

@end text="Match powers, or take a logarithm"
You can try each equation both ways, including the ones with no solution, on Learn. That's learn dot get er done dot I O.
