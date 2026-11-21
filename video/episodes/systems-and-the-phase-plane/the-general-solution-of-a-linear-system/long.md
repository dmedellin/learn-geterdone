---
format: long
lesson: systems-and-the-phase-plane/the-general-solution-of-a-linear-system
title: The general solution of a linear system, fitted to a start
thumb: Add them, fit them, see who wins
---

@chapter The question
@title text="The General Solution of a Linear System" sub="Systems and the Phase Plane" art=thumb
Eigenvectors give you straight-line solutions. But most starts aren't on an eigenline. So how do you get the solution through any point you like? You add the straight lines together.

@chapter Superposition
@math heading="if x₁ and x₂ solve x′ = A·x" items="(C₁·x₁ + C₂·x₂)′ = C₁·x₁′ + C₂·x₂′@constants come out;;= C₁·A·x₁ + C₂·A·x₂@each one;;= A·(C₁·x₁ + C₂·x₂)@A times the sum"
If x one and x two both solve the system, so does any combination of them. The derivative of the sum is C one x one prime plus C two x two prime, because constants come out of derivatives. Each one equals A times itself, so the whole thing is A times the sum. That's the equation again.

@art two-terms-add
So with two distinct real eigenvalues, every solution is C one, e to the lambda one t, v one, plus C two, e to the lambda two t, v two. Two constants, one for each eigenvector, because a start has two coordinates to match.

@chapter Fitting a start
@math heading="rows 2 1 and 1 2,  start (1, 0)" items="C₁·(1, −1) + C₂·(1, 1) = (1, 0)@At t equals zero;;C₁ + C₂ = 1,   −C₁ + C₂ = 0@two equations;;2C₂ = 1,  C₂ = 1/2,  C₁ = 1/2@Adding them"
Take the matrix with rows two, one and one, two. Its eigenpairs are one with one, minus one, and three with one, one. At t equals zero every exponential is one, so you need C one times one, minus one, plus C two times one, one, to equal the start, one, zero. That's two equations: C one plus C two is one, and minus C one plus C two is zero. Adding them gives two C two equals one, so both constants are a half.

@math heading="the solution" items="x(t) = (e^(t) + e^(3t))/2@x of t;;y(t) = (e^(3t) − e^(t))/2@y of t;;t = 0:  (1, 0)  ✓@at zero;;2x + y = (e^(t) + 3e^(3t))/2 = x′  ✓@two x plus y"
So x of t is e to the t plus e to the three t, over two. And y of t is e to the three t minus e to the t, over two. Check both things. At zero it gives one, zero. And two x plus y simplifies to e to the t plus three e to the three t, over two, which is x prime.

@words text="Check the start and the equation"
Keep doing both checks. Checking only the equation would miss a wrong constant. Checking only the start would miss a wrong exponent.

@chapter Which term wins
@art larger-wins
As t grows, the e to the three t term dwarfs the e to the t term. So the curve bends to run almost along one, one. Run time backwards, and both terms shrink, but now e to the t is the bigger, so the curve comes out of the origin tangent to the line through one, minus one.

@art node-shape
That's the shape of every node. Orbits hug the slow eigenline near the origin, and run parallel to the fast one far away. A saddle is different, because its exponents have opposite signs.

@math heading="rows −1 0 and 0 −2,  start (2, 2)" items="x(t) = (2e^(−t), 2e^(−2t))@two e"
When both exponents are negative, both terms die away. For rows minus one, zero and zero, minus two, from two, two, the solution is two e to the minus t, and two e to the minus two t.

@art decay-tangent
The first term dies more slowly, so it wins at the end, and the orbit comes into the origin tangent to the x axis.

@chapter Neither line
@art neither-line
For rows one, two and three, zero, the start three, zero sits closer to the diagonal. It's tempting to say the solution is just the diagonal one. But that passes through one, one, not three, zero.

@math heading="rows 1 2 and 3 0,  start (3, 0)" items="2C₁ + C₂ = 3,   −3C₁ + C₂ = 0@two C one;;C₁ = 3/5,   C₂ = 9/5@three fifths"
The eigenpairs are minus two with two, minus three, and three with one, one. Solve two C one plus C two equals three, and minus three C one plus C two equals zero. You get C one is three fifths, and C two is nine fifths. Both terms are there.

@chapter Where people slip
@list heading="Common slips" items="Using the nearest eigenline's solution@The first|One constant for the whole sum@The second|Mixing up which end each term wins@And the third"
The first slip is using the nearest eigenline's solution, as we just saw. The second is writing a single constant in front of the whole sum, which can't match a start with two coordinates. And the third is mixing up the ends. The larger eigenvalue wins as t goes to infinity, the smaller as t goes to minus infinity.

@art one-constant-zero
And a start that is on an eigenline has the other constant zero, so it never bends at all.

@chapter Try it
@words text="rows 2 1 and 1 2" sub="start (1, 0) → C₁ = C₂ = 1/2"
To practise, rebuild the worked example yourself. Write the general solution for rows two, one and one, two, set t to zero, and solve for the constants. You should get a half and a half. Then say which eigenline the curve follows for large t.

@end text="Fit a start, watch who wins"
You can fit the constants to any start and watch the orbit bend on Learn. That's learn dot get er done dot I O.
