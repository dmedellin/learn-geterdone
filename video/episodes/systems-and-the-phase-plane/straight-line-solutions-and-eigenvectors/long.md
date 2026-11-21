---
format: long
lesson: systems-and-the-phase-plane/straight-line-solutions-and-eigenvectors
title: Eigenvectors: the straight lines a system travels along
thumb: Directions the matrix won't turn
---

@chapter The question
@title text="Straight-Line Solutions and Eigenvectors" sub="Systems and the Phase Plane" art=thumb
A system x prime equals A x sends most points along curves. But some directions are special. Along them the matrix only stretches, and the system solves itself on a straight line.

@art stretch-not-turn
Multiply most vectors by a matrix and they turn. An eigenvector is a direction the matrix doesn't turn. A times v is just a multiple of v, lambda times v. It may stretch, shrink or flip, but it stays on the same line through the origin.

@math heading="Eigenvalue and eigenvector" items="A·v = λ·v@A times v;;v ≠ 0@non-zero"
In symbols, A times v equals lambda times v, for a non-zero vector v. The number lambda is the eigenvalue, and v is an eigenvector.

@chapter A direction, not a point
@art one-line-many-vectors
Every non-zero multiple of an eigenvector is also an eigenvector, with the same eigenvalue. So what you've really found is a line through the origin, not a single point. One, one and two, two are the same answer written twice.

@chapter Where the eigenvalues come from
@math heading="τ = a + d    Δ = a·d − b·c" items="(A − λ·I)·v = 0@A minus lambda I;;det(A − λ·I) = 0@determinant;;λ² − τ·λ + Δ = 0@lambda squared"
A v equals lambda v says A minus lambda I, times v, is zero. A non-zero v can only do that when the determinant of A minus lambda I is zero. Multiply it out and you get lambda squared, minus tau lambda, plus delta, equals zero. Tau is the trace, a plus d. Delta is the determinant, a d minus b c.

@words text="roots add to τ, multiply to Δ"
So two exact numbers, the trace and the determinant, decide the multipliers. The two roots add to tau and multiply to delta.

@chapter A worked example
@math heading="rows 2 1 and 1 2" items="τ = 4,  Δ = 3@trace is four;;λ² − 4λ + 3 = (λ − 1)(λ − 3)@factors;;λ = 1:  v₁ + v₂ = 0,  v = (1, −1)@For lambda equals one;;λ = 3:  −v₁ + v₂ = 0,  v = (1, 1)@For lambda equals three"
Take the matrix with rows two, one and one, two. The trace is four and the determinant is three. Lambda squared minus four lambda plus three factors as lambda minus one, times lambda minus three. For lambda equals one, you solve v one plus v two equals zero, so v is one, minus one. For lambda equals three, it's minus v one plus v two equals zero, so v is one, one.

@art parallel-rows
Notice that each time, the two equations were really one equation. That's the determinant being zero: the two rows of A minus lambda I are parallel. So one equation is enough, and any non-zero solution of it will do.

@chapter The straight-line solution
@math heading="if A·v = λ·v" items="x(t) = e^(λt)·v@e to the lambda t;;x′ = λ·e^(λt)·v@Differentiate;;A·x = e^(λt)·λ·v@the other side"
Here's the payoff. If A v equals lambda v, then x of t equals e to the lambda t, times v, solves the system. Differentiate, and you get lambda e to the lambda t, times v. The other side, A x, is e to the lambda t times A v, which is the same thing.

@art straight-solution
Every coordinate is a multiple of the same exponential, so the point slides along the line through v, faster and faster as it goes.

@art eigenlines
For our matrix the solutions are e to the t times one, minus one, and e to the three t times one, one. Both eigenvalues are positive, so both run away from the origin, the diagonal one faster.

@math heading="along the diagonal" items="x(t) = e^(3t)·(1, 1)@e to the three t;;x′ = 3e^(3t)@three e;;2x + y = 3e^(3t)@two x plus y"
Check it directly. Along the diagonal, x of t is e to the three t times one, one, so x prime is three e to the three t. And the first equation says x prime is two x plus y, which is also three e to the three t. They agree.

@chapter Where people slip
@list heading="Common slips" items="Treating an eigenvector as a point@The first|Pairing a vector with the wrong λ@The second|Expecting the quadratic to give v@And the third"
The first slip is treating an eigenvector as a point, and thinking two, two is wrong because the answer said one, one. The second is pairing a vector with the wrong eigenvalue. Always test by multiplying. And the third is expecting the quadratic to give the eigenvectors. It gives only the eigenvalues. Each one still needs its own equation.

@art four-regions
One more picture. The two eigenlines cut the plane into four regions, and a solution that starts in one region stays in it. On an eigenline a solution never leaves, so off it, it can never arrive.

@chapter Try it
@words text="rows 1 2 and 3 0" sub="τ = 1,  Δ = −6"
Your turn. Take the matrix with rows one, two and three, zero. The trace is one and the determinant is minus six. Find the two eigenvalues, solve for each direction, and then test each vector by multiplying it by A.

@end text="Find the lines a system runs along"
You can type a matrix and see its eigenlines and straight-line solutions on Learn. That's learn dot get er done dot I O.
