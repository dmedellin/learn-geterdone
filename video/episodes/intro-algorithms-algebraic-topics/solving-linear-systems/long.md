---
format: long
lesson: intro-algorithms-algebraic-topics/solving-linear-systems
title: Solving linear systems with an LUP decomposition
thumb: Factor once, solve fast
---

@chapter The problem
@title text="Solving Systems of Linear Equations" sub="Introduction to Algorithms, Chapter 28" art=thumb
Chapter twenty eight takes up the most common matrix problem of all: n linear equations in n unknowns.

@quote text="Because operations on matrices lie at the heart of scientific computing, efficient algorithms for working with matrices have many practical applications." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Chapter 28"
Because operations on matrices lie at the heart of scientific computing, efficient algorithms for working with matrices have many practical applications.

@art stable-vs-unstable
The authors flag numerical stability, the way rounding errors can grow in floating point, as a real concern that they mostly leave to specialist texts. The lesson's lab sidesteps it by computing in exact fractions.

@words text="Ax = b" sub="don't compute A⁻¹"
Write the system as A x equals b, with A nonsingular. You could compute the inverse and multiply, but the authors point out that's numerically unstable in practice. An LUP decomposition is stable, and faster.

@chapter The plan
@art three-factors
Find three matrices with P A equal to L U. L is unit lower triangular, U is upper triangular, and P is a permutation that reorders the rows.

@math heading="Two triangular solves" items="PAx = Pb ⇒ LUx = Pb@permutes the equations;;Ly = Pb: forward substitution@forward substitution;;Ux = y: back substitution@back substitution"
Multiply both sides by P, which permutes the equations, and you get L U x equals P b. Call U x y. Solve L y equals P b by forward substitution, then U x equals y by back substitution.

@art triangular-solve
Each solve takes one unknown at a time. With L, the first equation gives y one, the second gives y two, and so on down. With U, you start from x n and work upward. Each solve is theta of n squared.

@chapter Factoring by elimination
@art schur-complement
The factoring is Gaussian elimination. Split off the top left entry, the rest of its column, and the rest of its row. The column divided by the corner becomes L's first column. The row becomes U's first row. Then subtract, to clear the first column, and repeat on what's left, the Schur complement. That's theta of n cubed.

@art pivot-swap
But the recursion divides by the corner entry. If it's zero, the method fails, even when A is nonsingular. If it's small, rounding error grows. So before each step, swap up the entry of greatest absolute value in the column, and record the swap. If every candidate is zero, the matrix is singular.

@chapter A zero in the corner
@math heading="A = [[0, 2], [3, 1]] · b = (4, 5)" items="π = 2, 1 → PA = [[3, 1], [0, 2]]@With the exchange;;L = I · U = [[3, 1], [0, 2]]@already upper triangular;;Pb = (5, 4) · y = (5, 4)@P b is;;x₂ = 4/2 = 2 · x₁ = (5 − 1·2)/3 = 1@back substitution"
Take this two by two matrix, with a zero in the corner. Without a swap, you'd divide by zero. With the exchange, P A is already upper triangular, so L is the identity. P b is five, four, and so is y. Then back substitution gives x two equals four over two, two, and x one equals five minus two, over three, one.

@chapter The lesson's matrix
@math heading="[[1, 3, 2], [2, 2, 5], [4, 1, 3]] · b = (1, 7, 10)" items="π = 3, 1, 2@pi is;;pivots: 4, 11/4, 31/11@the pivots;;det = 4 · 11/4 · 31/11 = 31@determinant;;x = (2, −1, 1)@x is"
On the lesson's three by three matrix, the lab reports pi is three, one, two, and the pivots are four, eleven quarters, and thirty one elevenths. The determinant is their product, thirty one. Two row exchanges leave the sign alone. And x is two, minus one, one, checked exactly.

@chapter Relatives
@words text="Inversion ≈ multiplication" sub="Section 28.2"
Inverting a matrix means one factoring and n solves, theta of n cubed. Section twenty eight point two shows that, under mild conditions, inverting and multiplying matrices cost the same, asymptotically.

@art least-squares
And symmetric positive definite matrices never need pivoting. That matters for least squares, fitting more data points than unknowns, which leads to the normal equations, A transpose A c equals A transpose y.

@chapter Where people slip
@list heading="Common slips" items="Elimination without row exchanges@The first|Solving by computing the inverse@The second|Forgetting to permute b@the third"
The first slip is expecting elimination to work without row exchanges. The zero in the corner breaks it. The second is solving by computing the inverse. And the third is forgetting to permute b. The factors describe P A, so b must be reordered the same way, and nothing warns you until you check.

@chapter Try it
@words text="[[1, 2, 2], [4, 4, 2], [2, 6, 4]] · b = (3, 4, 4)" sub="LUP with partial pivoting"
Your turn. Find the LUP decomposition of this matrix by hand, with partial pivoting. Then solve for b equals three, four, four, by forward and back substitution.

@end text="Decompose a matrix exactly"
You can decompose matrices in exact fractions and check every step, on Learn. That's learn dot get er done dot I O.
