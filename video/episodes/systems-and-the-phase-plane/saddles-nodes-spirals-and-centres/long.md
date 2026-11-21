---
format: long
lesson: systems-and-the-phase-plane/saddles-nodes-spirals-and-centres
title: Saddles, nodes, spirals and centres from two numbers
thumb: Trace and determinant decide
---

@chapter The question
@title text="Saddles, Nodes, Spirals and Centres" sub="Systems and the Phase Plane" art=thumb
Every linear system in the plane draws one of a handful of pictures around the origin. You don't need to solve it to know which. Two numbers, computed from the four entries of the matrix, sort them all.

@math heading="rows a b and c d" items="τ = a + d@the trace;;Δ = a·d − b·c@the determinant;;λ² − τ·λ + Δ = 0@lambda squared"
Those numbers are tau, the trace, a plus d, and delta, the determinant, a d minus b c. The eigenvalues are the roots of lambda squared minus tau lambda plus delta, so the roots add to tau and multiply to delta.

@chapter Determinant first
@art saddle
If delta is negative, the product of the roots is negative. So one root is positive and one is negative: a growing direction and a shrinking one. That's a saddle, whatever else is true.

@chapter Real or complex
@words text="τ² − 4Δ" sub="> 0 real  ·  < 0 complex  ·  = 0 repeated"
If delta is positive, look next at tau squared minus four delta, the discriminant. Positive means two real roots, negative means a complex pair, and zero means one repeated root.

@art node
With real roots and a positive determinant, the roots share a sign, and it's the sign of tau. That's a node. Orbits bend, but they never wind around the origin. If tau is negative, every orbit comes in, a stable node.

@art spiral
With a complex pair, the roots are alpha plus or minus beta i, and alpha is tau over two. The imaginary part makes orbits turn around the origin. The real part decides in or out: out if it's positive, in if it's negative. That's a spiral.

@art centre
And if tau is zero with delta positive, the roots are purely imaginary. There's no growth or decay at all, and every orbit closes up into a loop around the origin. That's a centre.

@chapter The whole table
@list heading="The classification" items="Δ < 0:  saddle@negative determinant|Δ > 0,  τ² − 4Δ > 0:  node@a node|Δ > 0,  τ² − 4Δ < 0,  τ ≠ 0:  spiral@a spiral|Δ > 0,  τ = 0:  centre@a centre|τ² − 4Δ = 0:  degenerate or star node@on the parabola"
So here's the whole story. A negative determinant gives a saddle. A positive determinant with a positive discriminant gives a node. A negative discriminant with non-zero trace gives a spiral. Zero trace gives a centre. And on the parabola, where the discriminant is zero, you get a degenerate or star node.

@art trace-det-plane
In a plane with tau across and delta up, the line between nodes and spirals is the parabola delta equals tau squared over four. The line delta equals zero is left out of the table, because there the origin isn't an isolated equilibrium.

@art degenerate-node
On the parabola there's one repeated root. Rows minus one, one and zero, minus one have trace minus two, determinant one, and the repeated root minus one. There's only one eigenline, and orbits bend round it as they come in: a degenerate node. A multiple of the identity, where every direction is an eigenvector, is a star node instead.

@chapter A worked spiral
@math heading="rows 1 2 and −2 1" items="τ = 1 + 1 = 2@the trace is two;;Δ = 1·1 − 2·(−2) = 5@the determinant is five;;τ² − 4Δ = 4 − 20 = −16@minus sixteen;;λ = 1 ± 2i@one plus or minus two i"
Take rows one, two and minus two, one. The trace is two. The determinant is one minus minus four, so the determinant is five. The discriminant is four minus twenty, minus sixteen, so the roots are complex: one plus or minus two i.

@words text="real part 1 > 0" sub="unstable spiral"
The determinant is positive, so it's not a saddle. The trace isn't zero, so it's not a centre. The real part is one, positive, so orbits turn and move out. It's an unstable spiral. Flip the signs on the diagonal and the same picture runs inward, as a stable spiral.

@chapter Where people slip
@list heading="Common slips" items="Negative determinant means stable@The first|Every complex pair is a centre@The second|Reading the trace before the determinant@And the third"
The first slip is thinking a negative determinant means the origin is stable. For rows one, two and three, zero, delta is minus six, and the eigenvalues are minus two and three. The second is calling every complex pair a centre. A centre needs zero trace. And the third is reading the trace before the determinant. With tau minus one and delta minus two, the roots are one and minus two, a saddle.

@chapter Try it
@words text="rows −1 0 and 0 −2" sub="τ = −3,  Δ = 2"
Your turn. For rows minus one, zero and zero, minus two, the trace is minus three and the determinant is two. Compute the discriminant, decide which picture it is, and say whether orbits come in or go out. Then try rows zero, two and minus two, zero.

@end text="Sort any matrix in three numbers"
You can type any matrix and watch its picture appear on Learn. That's learn dot get er done dot I O.
