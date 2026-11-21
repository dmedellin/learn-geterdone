---
format: long
lesson: exponential-and-logarithmic-functions/solving-logarithmic-equations
title: Solving logarithmic equations, and the answers that aren't
thumb: Check in the original
---

@chapter The unknown inside a logarithm
@title text="Solving Logarithmic Equations" sub="Exponential and Logarithmic Functions" art=thumb
With exponential equations, the unknown sat in an exponent, and a logarithm brought it down. Now the unknown sits inside a logarithm, and an exponential takes it out. Same move, opposite direction, with one difference. An exponential accepts every real number. A logarithm doesn't.

@art unknown-inside
So the method has four steps. Condense to a single logarithm. Convert to exponential form. Solve. Then test every candidate in the original equation. That last step isn't extra care. It's part of the arithmetic.

@chapter Domain first
@words text="Domain: every argument > 0" sub="fixed by the equation as given"
The domain of a logarithmic equation is the set of values that make every argument positive. It's fixed by the equation as you were given it, and no later step may enlarge it.

@math heading="Two conversions" items="log_b(u) = c    ⟺    u = bᶜ@log base b of u;;log_b(M) = log_b(N)    ⟺    M = N@log base b of M"
You need two conversions. Log base b of u equals c exactly when u equals b to the c. And log base b of M equals log base b of N exactly when M equals N, for positive M and N. That lets matching logarithms be dropped.

@art condense-merge
So condense until each side is a single logarithm or a constant. If both sides are logs in the same base, drop them. If one side is a constant, convert. Then solve what's left, which is usually linear or quadratic.

@chapter A worked example
@math heading="log₂(x − 1) + log₂(x + 2) = 2" items="log₂((x − 1)(x + 2)) = 2@product law;;(x − 1)(x + 2) = 2² = 4@definition;;x² + x − 6 = 0@x squared plus x;;(x + 3)(x − 2) = 0@factors;;x = −3    or    x = 2@minus three or two"
Take log base two of x minus one, plus log base two of x plus two, equals two. The product law condenses the left side. The definition turns it into x minus one, times x plus two, equals four. That's x squared plus x minus six equals zero, which factors, giving minus three or two.

@math heading="domain:   x − 1 > 0  and  x + 2 > 0    →    x > 1" items="x = 2:    log₂(1) + log₂(4) = 0 + 2 = 2    ✓@x equals two;;x = −3:    log₂(−4) is not defined    ✗@x equals minus three"
The domain needs both arguments positive, so x is greater than one. At x equals two, log of one plus log of four is zero plus two, which is two. It stays. At x equals minus three, log base two of minus four isn't defined. It goes.

@art two-negatives
Why did minus three appear at all? The condensed equation only asks that the product be four. At minus three the factors are minus four and minus one, whose product is four. Two negatives passed a test written for their product. The original asks for the log of each factor, and neither exists.

@chapter Condensing widens the domain
@art domain-gate
That's the general pattern. Log M plus log N needs both M and N positive. Log of M times N needs only the product positive, which two negatives also satisfy. Every extraneous solution here enters through exactly that gap.

@words text="log₃(x + 6) − log₃(x + 2) = 2" sub="x = −3/2:    arguments 9/2 and 1/2, both positive   ✓"
But don't reject negatives on sight. Log base three of x plus six, minus log base three of x plus two, equals two, gives x equals minus three halves. The arguments there are nine halves and one half, both positive, so it stands.

@chapter When nothing survives
@art empty-set
Sometimes nothing survives. Log base two of x, minus log base two of x plus one, equals three, gives x equals minus eight sevenths. That makes both arguments negative, so the solution set is empty. And no step along the way was wrong.

@words text="log(3x + 1) = log x + log 3" sub="→   3x + 1 = 3x    →    1 = 0"
A third ending is a contradiction. Log of three x plus one equals log x plus log three becomes three x plus one equals three x, so one equals zero. No candidate is ever produced.

@chapter Where people slip
@art check-original
The biggest slip is checking in the condensed equation. That's exactly the form that accepts extraneous values, so it confirms them cheerfully. Always substitute into the equation you were given.

@list heading="Two more slips" items="Rejecting every negative candidate@rejecting every negative|Condensing a sum into the log of a sum@condensing a sum"
The others are rejecting every negative candidate, when the test is on the arguments, and condensing a sum of logs into the log of a sum. Log ten plus log a hundred is three, but log of a hundred and ten is about two point oh four.

@chapter Try it
@words text="log₂(x − 1) + log₂(x − 3) = 3" sub="domain:    x > 3"
Your turn. Solve log base two of x minus one, plus log base two of x minus three, equals three. The domain is given: x greater than three. Condense, convert, factor, and test both candidates in the two original arguments. Name the argument that rejects any discarded candidate.

@end text="Candidates, and which survive"
You can type an equation and see each candidate kept or rejected, with the argument that decided it, on Learn. That's learn dot get er done dot I O.
