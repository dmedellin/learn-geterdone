---
format: long
lesson: quadratics-and-complex-numbers/the-discriminant
title: The discriminant: how many solutions before you solve
thumb: Two, one or none
---

@chapter The question
@title text="The Discriminant" sub="Quadratics and Complex Numbers" art=thumb
Before you solve a quadratic, wouldn't it help to know what kind of answer you're looking for? Or whether there's anything to find at all? One line of arithmetic tells you.

@math heading="Discriminant" items="D = b² − 4ac@D equals;;ax² + bx + c = 0,  a ≠ 0@standard form"
The discriminant is D equals b squared minus four a c. It's the quantity under the root in the quadratic formula, and you compute it from the standard form, signs included.

@chapter What the sign decides
@list heading="The sign of D" items="D > 0: two distinct real solutions@positive|D = 0: exactly one real solution@is zero|D < 0: no real solution@negative"
If D is positive, there are two distinct real solutions. If D is zero, there's exactly one. If D is negative, there are none.

@art sign-dial
Here's why. The quadratic formula lesson showed the equation is the same as x plus b over two a, squared, equals D over four a squared. Four a squared is positive, so that right side has the same sign as D. And no real number has a negative square.

@art three-parabolas
The three cases cover everything and never overlap. So the discriminant always answers the question, and never answers it twice.

@chapter One, not none
@math heading="4x² − 12x + 9 = 0" items="D = 144 − 144 = 0@a hundred and forty four;;(2x − 3)² = 0@perfect square;;x = 3/2@three halves"
Four x squared minus twelve x plus nine has D equal to a hundred and forty four minus a hundred and forty four, which is zero. And it factors as a perfect square, two x minus three, squared. Its one solution is three halves.

@words text="D = 0  →  x = −b/(2a)" sub="one solution, not none"
D equals zero means one solution, not none. The formula becomes minus b, plus or minus zero, over two a, and both branches give minus b over two a. It's the boundary between two and none, and belongs to neither.

@chapter Will it factor?
@art perfect-square-tiles
For integer coefficients there's a bonus. The equation has rational solutions exactly when D is the square of an integer. Then root D is a whole number, and both solutions are fractions.

@math heading="Should I try factoring?" items="x² − 4x + 1:  D = 16 − 4 = 12@twelve;;x² − 5x + 6:  D = 1  →  (x − 2)(x − 3)@D is one"
So you can call off a factoring search before it starts. x squared minus four x plus one has D equal to sixteen minus four, twelve. Not a perfect square, so no amount of looking will find a factorisation. x squared minus five x plus six has D is one, so it factors, as x minus two, times x minus three.

@art tiles-left-over
That turns the question, should I try factoring, into a calculation instead of a guess. If D won't make a perfect square, the factors you're hunting for don't exist with rational numbers, however long you search.

@chapter Four discriminants
@math heading="Classify in one line" items="x² − 5x + 6:  D = 1  →  2 and 3@twenty five minus twenty four;;4x² − 12x + 9:  D = 0  →  3/2@zero, so one"
Here are four. x squared minus five x plus six: twenty five minus twenty four is one, positive and a perfect square, so two rational solutions, two and three. Four x squared minus twelve x plus nine: zero, so one solution, three halves.

@math heading="Classify in one line" items="x² − 4x + 1:  D = 12  →  2 ± √3@not a perfect square;;x² + x + 1:  D = −3  →  no real solution@minus three"
x squared minus four x plus one: twelve, positive but not a perfect square, so two irrational solutions, two plus or minus root three. And x squared plus x plus one: minus three, so no real solution.

@art method-signpost
Each took one line to classify. So compute D on every quadratic before choosing a method. A perfect square sends you to factoring, zero means one answer, and a negative D ends the work, for now.

@chapter What it doesn't say
@art gap-between-roots
The discriminant doesn't give the solutions, or say whether they're positive or negative. Its size isn't a difficulty rating, either: one and ten thousand both just mean two real solutions. One fact is worth keeping. The two solutions differ by root D over the absolute value of a.

@chapter Where people slip
@math heading="2x² − 4x − 3 = 0" items="D = 16 + 24 = 40  ✓@forty;;not  16 − 24 = −8@not sixteen minus"
The first slip is dropping the sign in minus four a c. For two x squared minus four x minus three, a and c have opposite signs, so D is sixteen plus twenty four, which is forty, not sixteen minus twenty four. That's the difference between two solutions and none.

@list heading="Two more" items="Reading D = 0 as no solutions@The second|Saying no solutions for no real solutions@The third"
The second slip is reading D equals zero as no solutions. The third is saying no solutions when you mean no real solutions. x squared plus one equals zero has no real solution, but it has two complex ones.

@end text="Compute D first"
Classify a few quadratics by their discriminant, on Learn. That's learn dot get er done dot I O.
