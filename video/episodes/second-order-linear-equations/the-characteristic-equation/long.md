---
format: long
lesson: second-order-linear-equations/the-characteristic-equation
title: The characteristic equation: one guess turns a differential equation into a quadratic
thumb: Guess e to the rt
---

@chapter The question
@title text="The Characteristic Equation" sub="Second-Order Linear Equations" art=thumb
Guessing the solution of a second-order equation doesn't scale. But one guess does, and it turns the whole problem into a quadratic.

@words text="a·y″ + b·y′ + c·y = 0" sub="a, b, c constants, a ≠ 0"
Here's the equation: a times y double prime, plus b times y prime, plus c times y, equals zero. The numbers a, b and c are constants, and a isn't zero.

@art exponential-copies
You've met y prime equals k times y, solved by e to the k t. That exponential is the natural thing to try again, because its rates are copies of itself. The rate of e to the r t is r times e to the r t. So every term becomes a multiple of one function.

@chapter Substitute
@math heading="Try y = e^(rt)" items="y = e^(rt)@try y equals;;y′ = r·e^(rt)@Its rate;;y″ = r²·e^(rt)@its second rate;;a·r²·e^(rt) + b·r·e^(rt) + c·e^(rt) = 0@Substitute;;(a·r² + b·r + c)·e^(rt) = 0@factor out"
So try y equals e to the r t, where r is the only unknown. Its rate is r e to the r t, and its second rate is r squared e to the r t. Substitute, and every term carries e to the r t. So factor out the exponential.

@art exponential-never-zero
Now the key step. E to the r t is positive for every t. So the product is zero exactly when the bracket is. And the bracket has no t in it at all.

@words text="a·r² + b·r + c = 0" sub="the characteristic equation"
That's the characteristic equation. E to the r t solves the differential equation exactly when r solves a r squared plus b r plus c equals zero. An equation in a number, with no t in it.

@chapter Solve the quadratic
@math heading="The quadratic formula" items="r = (−b ± √(b² − 4ac)) / (2a)@r equals;;disc = b² − 4ac@The discriminant"
What's left is the algebra of a quadratic. r equals minus b, plus or minus the square root of b squared minus four a c, all over two a. The discriminant, b squared minus four a c, tells you which of three things happens.

@art parabola-two-roots
Positive means two real roots. Zero means one root, repeated. Negative means a complex pair.

@chapter Four presets
@math heading="Two presets" items="y″ + 3y′ + 2y = 0:  disc = 9 − 8 = 1@nine minus eight;;y″ + 4y′ + 4y = 0:  disc = 16 − 16 = 0@sixteen minus sixteen"
The lab has four presets. For y double prime plus three y prime plus two y, the discriminant is nine minus eight, one, a perfect square, so the roots are rational. Plus four y prime plus four y gives sixteen minus sixteen, zero, so there's one root, twice.

@math heading="y″ + 2y′ + 5y = 0" items="disc = 4 − 20 = −16@four minus twenty;;r = −1 ± 2i@the complex pair"
And y double prime plus two y prime plus five y gives four minus twenty, minus sixteen. No real square root there, so the roots are the complex pair minus one plus or minus two i.

@art parabola-above
Its parabola never meets the axis at all. No real root, and yet, as a later lesson shows, a perfectly real solution.

@art parabola-touching
The last preset, y double prime minus y prime minus y, has discriminant one plus four, five. That's positive, so both roots are real.

@math heading="y″ − y′ − y = 0,  disc = 5" items="r = (1 ± √5)/2@one plus or minus;;≈ 1.61803,  ≈ −0.618034@Rounded"
They're one plus or minus root five, over two. The lab prints that surd exactly. Rounded, they're about one point six one eight zero three and minus zero point six one eight zero three four, but the rounded numbers are only for the eye.

@chapter Where people slip
@list heading="Common slips" items="Setting the quadratic equal to y@The first|Misreading the signs of b and c@The second|Positive discriminant means rational roots@The third"
The first slip is setting the quadratic equal to y. The right side is zero. The second is misreading the signs of b and c. And the third is thinking a positive discriminant means rational roots. Only a perfect square does that, which is why five gave a surd.

@art sign-slip
Take y double prime minus five y prime plus six y. The coefficients are one, minus five and six, and the roots are two and three. Read b as plus five and you get minus two and minus three. Put minus two back into the true quadratic and you get twenty, not zero. One root put back catches the slip.

@chapter Try it
@words text="y″ + 3y′ + 2y = 0" sub="check r = −1 and r = −2 in r² + 3r + 2"
Your turn. Substitute e to the r t into y double prime plus three y prime plus two y, divide out the exponential, and solve. Name the kind of root from the discriminant first. Then put each root back: one minus three plus two, and four minus six plus two, should both be zero.

@end text="Substitute, factor, solve"
You can try any equation and see its roots printed exactly, on Learn. That's learn dot get er done dot I O.
