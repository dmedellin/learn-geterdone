---
format: long
lesson: induction-and-recursion/solving-linear-recurrences
title: Solving linear recurrences with the characteristic equation
thumb: Guess r to the n
---

@chapter Guess a geometric sequence
@title text="Solving Linear Recurrences" sub="Induction and Recursion" art=thumb
Unrolling works for simple recurrences, but it falls apart quickly. For linear recurrences with constant coefficients there's a method that always works, and it starts with a guess.

@math heading="Try aₙ = rⁿ" items="aₙ = c₁aₙ₋₁ + c₂aₙ₋₂@Take;;rⁿ = c₁rⁿ⁻¹ + c₂rⁿ⁻²@Substitute;;r² = c₁r + c₂@divide"
Take a n equals c one a n minus one plus c two a n minus two, and guess that a n is r to the n, for some nonzero r. Substitute, then divide through by r to the n minus two. What's left is r squared equals c one r plus c two. That's the characteristic equation.

@art geometric-curves
Its roots are exactly the geometric sequences that satisfy the recurrence. And because the recurrence is linear, any combination of solutions is also a solution. The initial conditions pick which combination.

@chapter Distinct roots
@math heading="aₙ = 5aₙ₋₁ − 6aₙ₋₂,  a₀ = 1,  a₁ = 5" items="r² − 5r + 6 = 0@r squared minus;;(r − 2)(r − 3) = 0,  r = 2, 3@two and three;;aₙ = A·2ⁿ + B·3ⁿ@A times two"
Here's one: a n is five a n minus one minus six a n minus two, with a nought one and a one five. The characteristic equation is r squared minus five r plus six, with roots two and three. So a n is A times two to the n, plus B times three to the n.

@math items="A + B = 1@A plus B;;2A + 3B = 5@two A;;B = 3,  A = −2@B is three;;aₙ = −2·2ⁿ + 3·3ⁿ@minus two"
Now fit the constants. From a nought, A plus B is one. From a one, two A plus three B is five. Subtract twice the first equation, and B is three, so A is minus two. The solution is minus two times two to the n, plus three times three to the n.

@words text="a₂:  −8 + 27 = 19,   5(5) − 6(1) = 19"
Check it on a term you didn't use to fit. The formula gives minus eight plus twenty seven, nineteen. The recurrence gives five times five minus six, also nineteen. Checking a nought and a one would only confirm your arithmetic.

@art two-blend
In general, distinct roots r one and r two give A times r one to the n, plus B times r two to the n. Two roots, two constants, two initial conditions.

@chapter Fibonacci
@math heading="Fₙ = Fₙ₋₁ + Fₙ₋₂" items="r² = r + 1,  r = (1 ± √5)/2@one plus or minus;;A + B = 0,   Aφ + Bψ = 1@F nought;;Fₙ = (φⁿ − ψⁿ)/√5@Binet's formula"
Fibonacci gives r squared equals r plus one, so r is one plus or minus root five, over two. Call those roots phi and psi. F nought gives A plus B equals zero, and F one gives A phi plus B psi equals one. The result is Binet's formula: phi to the n minus psi to the n, over root five.

@art golden-spiral
It produces whole numbers from irrational ones, at every n.

@chapter A repeated root
@math heading="aₙ = 4aₙ₋₁ − 4aₙ₋₂,  a₀ = 1,  a₁ = 4" items="(r − 2)² = 0@r minus two;;aₙ = (A + Bn)·2ⁿ@A plus B n;;A = 1,  B = 1,  aₙ = (n + 1)·2ⁿ@n plus one"
What if the roots coincide? Take a n equals four a n minus one, minus four a n minus two. The characteristic equation is r minus two, squared, so use A plus B n, times two to the n. Fitting gives A and B both equal to one, so a n is n plus one, times two to the n.

@art merged-curves
Why the extra n? One root gives one geometric solution and one free constant, which can't meet two initial conditions. Forget the n and A times two to the n plus B times two to the n is just one constant, C. a nought demands C is one, and a one demands C is two. That contradiction is the warning sign.

@chapter Nonhomogeneous: Hanoi
@math heading="Hₙ = 2Hₙ₋₁ + 1" items="homogeneous:  C·2ⁿ@C times;;particular:  A = 2A + 1,  A = −1@minus one"
With a forcing term, the general solution is the homogeneous solution plus any one particular solution. For Hanoi, the homogeneous part is C times two to the n. For a particular one, try a constant A: A equals two A plus one, so A is minus one.

@art shifted-curve
So the general solution is C times two to the n, minus one: the homogeneous family, shifted by the particular solution.

@math items="Hₙ = C·2ⁿ − 1,  H₁ = 1  ⟹  C = 1@H one;;Hₙ = 2ⁿ − 1@two to the n minus one"
Only now do you fit the constant. H one equals one gives C equals one, so H n is two to the n minus one. Derived, not guessed.

@art collision
One catch. If the forcing term is two to the n and two is already a root, the guess A times two to the n solves the homogeneous part and can't produce the forcing term. Multiply by n and try A n two to the n, just as with a repeated root.

@chapter Where people slip
@list heading="Common slips" items="Forgetting the n on a repeated root@Forgetting|Fitting constants too early@too early|Missing the collision case@collision"
Three slips. Forgetting the n on a repeated root. Fitting the constants too early, before adding the particular solution. They have to be fitted to the full general solution. And missing the collision case, where the obvious guess matches a root.

@end text="Roots, and the solution they build"
On Learn, you can see the characteristic equation and the fitted constants for each recurrence, checked term by term. That's learn dot get er done dot I O.
