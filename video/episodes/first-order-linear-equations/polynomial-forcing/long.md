---
format: long
lesson: first-order-linear-equations/polynomial-forcing
title: Polynomial forcing and undetermined coefficients
thumb: Every lower power, too
---

@chapter The question
@title text="Polynomial Forcing" sub="First-Order Linear Equations" art=thumb
Take y prime plus y equals t squared. The simplest guess for a particular solution is the forcing itself, y equals t squared. Does it work?

@math heading="Guess y = t²" items="y′ + y = 2t + t²@two t plus t squared;;wanted: t²@wants;;leftover: 2t@leftover"
Its derivative is two t, so the left side is two t plus t squared, and the equation wants t squared. The guess is wrong by exactly the leftover two t. That leftover is the whole lesson. The derivative creates a power of t the forcing doesn't have, and something in the guess has to cancel it.

@chapter The method
@art cascade
Here's the method, called undetermined coefficients. Write down a function with the shape of the forcing, with unknown constants for its coefficients. Substitute it into the left side, and match the coefficients of like terms on both sides. Each unknown is fixed by an exact linear equation.

@chapter A full quadratic
@math heading="y′ + y = t²" items="y_p = c₂·t² + c₁·t + c₀@c two t squared;;y_p′ = 2c₂·t + c₁@Its derivative;;y_p′ + y_p = c₂·t² + (2c₂ + c₁)·t + (c₁ + c₀)@Adding"
The forcing has degree two, so guess c two t squared plus c one t plus c nought, with every lower power. Its derivative is two c two t plus c one. Adding and collecting by powers of t gives c two t squared, plus two c two plus c one times t, plus c one plus c nought.

@math heading="Match from the top" items="t²:   c₂ = 1@t squared;;t:   2c₂ + c₁ = 0,   c₁ = −2@the t terms;;1:   c₁ + c₀ = 0,   c₀ = 2@the constants;;y_p = t² − 2t + 2@So y p"
Match from the top. For t squared, c two is one. For the t terms, two c two plus c one is zero, so c one is minus two. For the constants, c one plus c nought is zero, so c nought is two. So y p is t squared minus two t plus two.

@art cancel-down
Check: the derivative is two t minus two, and adding y p leaves exactly t squared. The two t that spoiled the first guess is cancelled by the minus two t, and the minus two that creates is cancelled by the constant.

@chapter Exactly one
@words text="a ≠ 0:  exactly one polynomial solution, of degree n"
If a isn't zero and the forcing is a polynomial of degree n, then y prime plus a y has exactly one polynomial solution, and its degree is n. The top equation fixes the top coefficient, and each line below fixes one more. There's no choice at any line.

@art triangle-system
Another polynomial solution would differ by C e to the minus a t, which is a polynomial only when C is zero. So there's no other. And the system is triangular: each equation brings one new unknown beside one already found.

@chapter A negative a
@math heading="y′ − 2y = 4t" items="c₁ − 2c₁·t − 2c₀ = 4t@substitute;;−2c₁ = 4,   c₁ = −2@the t terms;;c₁ − 2c₀ = 0,   c₀ = −1@the constants;;y_p = −2t − 1@minus two t minus one"
Take y prime minus two y equals four t, so a is minus two. Guess c one t plus c nought and substitute. The t terms give minus two c one equals four, so c one is minus two. The constants give c one minus two c nought equals zero, so c nought is minus one. So y p is minus two t minus one.

@art runaway
The general solution adds C e to the two t, which grows. So every solution except C equals zero runs away exponentially, and the polynomial is the single one that doesn't.

@math heading="y′ + y = t³" items="t³ − 3t² + 6t − 6@t cubed minus"
A higher power is the same pattern at greater length. For y prime plus y equals t cubed, the answer is t cubed minus three t squared plus six t minus six. Each coefficient is minus the one before, times that earlier power's exponent.

@chapter Where people slip
@list heading="Common slips" items="Guessing c·t² alone@The first|Expecting a steady state@The second|Using the wrong sign for a@The third"
The first slip is guessing c t squared alone. The residual is exactly two t. The second is expecting the solution to settle to a constant. The third is using the wrong sign for a.

@art moving-parabola
A steady state needs a constant forcing. Under t squared, the exponential part dies away, and the solution follows the parabola t squared minus two t plus two, which keeps moving.

@art wrong-sign
And in y prime minus two y equals four t, taking a as plus two gives two t minus one. Substitute it into the real left side, and you get four minus four t, the wrong sign on t, plus a stray constant. The residual shows the slip at once.

@chapter Try it
@words text="y′ + y = t²,  y(0) = 0" sub="fit C after adding: 2 + C = 0"
Your turn. Take y p equals t squared minus two t plus two, add C e to the minus t, and fit y of zero equals zero after adding. Check you get C equals minus two.

@end text="Match from the top down"
You can see each coefficient solved in exact fractions, on Learn. That's learn dot get er done dot I O.
