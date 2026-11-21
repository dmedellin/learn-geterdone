---
format: long
lesson: second-order-linear-equations/from-second-order-to-a-system
title: Turning a second-order equation into a first-order system
thumb: Name the rate v
---

@chapter The idea
@title text="From Second Order to a System" sub="Second-Order Linear Equations" art=thumb
One equation of second order can be rewritten as two equations of first order. The trick is to give the rate its own name.

@art phase-point
From here, call the unknown x, because the system treats position and velocity as a pair. The equation is a x double prime plus b x prime plus c x equals zero, with a not zero.

@math heading="Name the rate" items="x″ = −(c/a)·x − (b/a)·x′@solve for the second rate;;v = x′@call the rate v;;x′ = v@x prime is v;;v′ = −(c/a)·x − (b/a)·v@v prime is"
Divide by a and solve for the second rate: x double prime equals minus c over a times x, minus b over a times x prime. Now call the rate v. Then x prime is v, by definition, and v prime is minus c over a times x, minus b over a times v.

@words text="nothing lost" sub="v is the rate of x by definition"
The second equation is just the first line with v written in place of x prime. Nothing has been lost, because v is the rate of x by definition.

@chapter The matrix
@art matrix-grid
Write the system with one row per equation, and the coefficients form a grid of four numbers, the matrix A. The top row is zero, one. The bottom row is minus c over a, minus b over a.

@math heading="A = [0  1;  −c/a  −b/a]" items="τ = 0 + (−b/a) = −b/a@The trace;;Δ = 0·(−b/a) − 1·(−c/a) = c/a@the determinant;;λ² − τ·λ + Δ = λ² + (b/a)·λ + c/a@build the quadratic"
The trace is the sum of the diagonal, minus b over a. The determinant is zero times minus b over a, minus one times minus c over a, which is c over a. Now build the quadratic lambda squared minus trace times lambda plus determinant.

@words text="a·λ² + b·λ + c = 0" sub="the characteristic equation, with λ for r"
Multiply by a, and it's the characteristic equation, with lambda in place of r. So the eigenvalues of A are the roots of the equation. Same roots, same motion.

@chapter The system and the equation agree
@math heading="x″ + 3x′ + 2x = 0" items="x = 2·e^(−t) − e^(−2t)@the solution;;v = −2·e^(−t) + 2·e^(−2t)@Its rate"
Take the first preset. With a start at one and rate zero, the solution from an earlier lesson is two e to the minus t minus e to the minus two t. Its rate, v, is minus two e to the minus t plus two e to the minus two t.

@math heading="Both equations hold" items="x′ = v@x prime is v;;v′ = 2·e^(−t) − 4·e^(−2t)@v prime is;;−2x − 3v = 2·e^(−t) − 4·e^(−2t) = v′@minus two x minus three v"
So x prime is v, of course. And v prime is two e to the minus t minus four e to the minus two t. Now work out minus two x minus three v. The e to the minus t terms are minus four plus six, and the others are two minus six, so it's the same, v prime.

@art two-views
The first component of the pair is the equation's solution, and the second is its rate. The start is the point one, zero, which is just the two initial values written as a point.

@chapter The three presets
@math heading="Trace, determinant, eigenvalues" items="x″ + 3x′ + 2x:  τ = −3,  Δ = 2,  λ = −2, −1@three x prime;;x″ + 4x:  τ = 0,  Δ = 4,  λ = ±2i@plus four x;;x″ + 2x′ + 5x:  τ = −2,  Δ = 5,  λ = −1 ± 2i@two x prime plus five x"
The lab's presets give the roots from earlier lessons, one for one. Three x prime plus two x has trace minus three, determinant two, and eigenvalues minus two and minus one. Plus four x has trace zero, determinant four, and plus or minus two i. Two x prime plus five x has trace minus two, determinant five, and minus one plus or minus two i.

@art node-picture
The lab also names the picture each system makes in the plane. Negative real roots give a stable node.

@art centre-picture
Imaginary roots give a centre.

@art spiral-picture
And complex roots with a negative real part give a stable spiral. Those names belong to a later course. Here they're just labels on roots you already understand.

@chapter Where people slip
@list heading="Common slips" items="Expecting different solutions@The first|Forgetting to divide by a@The second|Swapping the bottom row@The third"
The first slip is thinking the system has different solutions from the equation. It's the equation in other clothes. The second is forgetting to divide by a. And the third is swapping the bottom row. Swap it for three x prime plus two x, and you'd get a complex pair and a spiral, though the real roots are minus one and minus two.

@chapter Try it
@words text="2x″ + 8x′ + 6x = 0" sub="roots of 2r² + 8r + 6 = 0:  −1 and −3"
Your turn. Write the matrix for two x double prime plus eight x prime plus six x. Divide by two first, so the bottom row is minus three, minus four. Check the trace and determinant give roots minus one and minus three.

@end text="Name the rate, read the matrix"
You can turn each equation into a matrix and compare the roots, on Learn. That's learn dot get er done dot I O.
