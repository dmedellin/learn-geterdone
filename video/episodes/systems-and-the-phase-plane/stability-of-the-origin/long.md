---
format: long
lesson: systems-and-the-phase-plane/stability-of-the-origin
title: When is the origin stable? Trace and determinant
thumb: Negative trace, positive determinant
---

@chapter The question
@title text="Stability of the Origin" sub="Systems and the Phase Plane" art=thumb
Start a linear system near the origin. Does it come back, wander off, or just stay close? There's a clean test, and it only needs two numbers from the matrix.

@chapter Three degrees of stable
@list heading="Three degrees" items="Asymptotically stable: every solution tends to it@asymptotically stable|Stable: near starts stay near@stable when|Unstable: some near start leaves@unstable when"
There are three degrees. The origin is asymptotically stable when every solution tends to it. It's stable when solutions that start near it stay near it. And it's unstable when some solution that starts arbitrarily near it doesn't.

@art three-degrees
Asymptotic stability implies stability. But the reverse fails. A centre is stable without being asymptotically stable: its orbits stay close, and never settle.

@chapter The criterion
@math heading="x′ = A·x" items="asymptotically stable  ⇔  τ < 0  and  Δ > 0@exactly when;;⇔  every λ has negative real part@the same as"
Here's the test. The origin is asymptotically stable exactly when the trace is negative and the determinant is positive. That's the same as every eigenvalue having a negative real part.

@words text="Δ > 0 then τ < 0"
Why? If the roots are real, a positive determinant means they share a sign, and a negative trace makes that sign negative. If they're a complex pair, the real part is tau over two, which is negative. Either way, every solution decays. Neither number alone is enough.

@words text="Δ < 0  or  τ > 0: something leaves"
It works the other way too. A negative determinant means a positive root. A positive determinant with a positive trace means positive real parts, or a positive shared sign. In each case some solution doesn't tend to the origin.

@chapter A stable spiral
@math heading="rows −1 2 and −2 −1" items="τ = −2 < 0@the trace is minus two;;Δ = 1 + 4 = 5 > 0@the determinant is five;;τ² − 4Δ = −16@minus sixteen;;λ = −1 ± 2i@minus one plus or minus two i"
Take rows minus one, two and minus two, minus one. The trace is minus two, and the determinant is one plus four, so the determinant is five. Both conditions hold. The discriminant is minus sixteen, and the roots are minus one plus or minus two i.

@art stable-spiral
Every solution carries a factor of e to the minus t, so it tends to the origin, turning as it goes. A stable spiral. It's last lesson's spiral with the diagonal signs flipped, the same picture unwound.

@chapter The borderline cases
@art centre-circles
When the trace is zero and the determinant positive, nothing grows and nothing decays. For rows zero, two and minus two, zero, the orbits are circles, because x squared plus y squared has derivative zero. The origin is stable, but not asymptotically stable. The criterion says not asymptotically stable. It doesn't say unstable.

@art line-of-equilibria
When the determinant is zero, one root is zero. For rows minus one, one and one, minus one, the roots are zero and minus two. Every point of the line through one, one is an equilibrium, so the origin isn't isolated. The start one, zero comes in and settles at a half, a half, not at the origin.

@chapter Where people slip
@art saddle-one-line
For rows one, two and three, zero, the eigenvalues are minus two and three. The solution along two, minus three really does tend to the origin. But that's one line of starts out of the whole plane. Anything with a part along one, one grows like e to the three t.

@list heading="Common slips" items="One negative eigenvalue is enough@The first|A centre is unstable@The second|Trusting Euler over the classification@And the third"
So the first slip is believing one negative eigenvalue is enough. Every eigenvalue has to decay. The second is calling a centre unstable because orbits never reach the origin. A start a tenth away stays a tenth away for ever. And the third is trusting Euler's polygon over the classification.

@art euler-outward
On the centre, with h a quarter, each Euler step multiplies the squared distance by five quarters. That looks like instability, but it's a fact about the method. The true orbits are circles. A smaller step brings the ratio towards one, and no step brings it to one.

@chapter Try it
@words text="rows 1 −2 and 2 1" sub="τ = 2,  Δ = 5"
Your turn. Take rows one, minus two and two, one. Compute the trace and determinant, check the determinant first, then the trace, and state which degree of stability applies. Confirm it by solving for the roots.

@end text="Test the origin yourself"
You can try the criterion on any matrix, and see the borderline cases, on Learn. That's learn dot get er done dot I O.
