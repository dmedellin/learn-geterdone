---
format: long
lesson: the-simplex-method/the-tableau-as-a-matrix-product
title: Every simplex tableau is B inverse times the original data
thumb: The tableau is B⁻¹ × data
---

@chapter The question
@title text="The Tableau as a Matrix Product" sub="The Simplex Method" art=thumb
After twenty pivots, is a tableau a battered copy of your data, carrying every rounding and every step? No. It's the original data times one matrix, and you can rebuild it from scratch.

@chapter The basis matrix
@art pick-columns
Take the basis, which is a list of column indices. The basis matrix B is those columns of the original A, before any pivoting, in the order the tableau's rows carry them. It's invertible, which is part of what being a basis means.

@math heading="Every tableau" items="body = B⁻¹[A | b]@the body;;rhs = B⁻¹b@right hand column;;z-row = c_BᵀB⁻¹[A | b] − [c | 0]@objective row"
Then the body of the tableau is B inverse times A next to b. The right hand column is B inverse b. And the objective row is c B transpose, B inverse, times the data, minus c.

@art row-ops
Why? Each row operation is left multiplication by an invertible matrix. So any run of pivots is one invertible matrix M applied to the data. The basic columns end up as the identity, so M times B is the identity. M is B inverse, and nothing else.

@art two-routes
So a tableau isn't a degraded copy. Two runs that reach the same basis by different routes produce the same tableau, entry for entry. And by Cramer's rule, every entry is a ratio of determinants of the original numbers.

@chapter A worked example
@math heading="max 3x₁ + 2x₂" items="x₁ + x₂ ≤ 4@capacity;;x₁ + 3x₂ ≥ 6@contract;;columns x₁, x₂, s₁, e₂, a₂@the columns"
Take maximise three x one plus two x two, with x one plus x two at most four for capacity, and x one plus three x two at least six for a contract. The at least row gets a surplus, e two, with column minus one, and an artificial, a two. So the columns are x one, x two, s one, e two, a two. The method finishes at the basis x one, x two.

@math heading="B and its inverse" items="B = [1 1; 1 3]@the x one and x two columns;;B⁻¹ = [3/2 −1/2; −1/2 1/2]@B inverse"
B is the x one and x two columns of the original A: one, one, and one, three. B inverse is three halves, minus a half, then minus a half, a half.

@math heading="The three products" items="B⁻¹b = (3, 1)@three, one;;c_BᵀB⁻¹ = (7/2, −1/2)@seven halves;;z = 11@eleven"
B inverse b is three, one: the solution. With c B equal to three, two, c B transpose B inverse is seven halves, minus a half. And z is eleven. All three products agree with the final tableau, entry for entry.

@chapter Where B⁻¹ lives
@art identity-columns
Now, where in the final tableau does B inverse appear? Under the columns that started as the identity. Here that's s one and a two.

@math heading="Not the slack columns" items="under s₁, a₂:  B⁻¹  ✓@slack and surplus;;under s₁, e₂:  e₂ = (1/2, −1/2)  ✗@e two"
The slack and surplus columns are s one and e two. But e two's column is a half, minus a half: the negative of B inverse's second column, because the surplus column is the negative of the artificial. Read B inverse from there, and its determinant has the wrong sign.

@art slogan-trap
In the all at most case, the slack columns are the starting identity, so the slogan B inverse is under the slacks happens to be true. That's why it survives. It stops being true at the first at least row, or after a phase one.

@words text="a₂ reduced cost −1/2" sub="artificial, barred from re-entering"
One more detail. The reduced cost of a two is minus a half, negative in an optimal tableau. But that's an artificial, barred from re entering, so the optimality test doesn't apply to it. Its entry is still the second component of c B transpose B inverse.

@chapter The second answer
@art hidden-answer
And c B transpose B inverse, seven halves and minus a half, sits right in the objective row. Those numbers solve a second linear programme built from the same data. They say what one more unit of each right hand side is worth. That's where duality begins.

@chapter Where people slip
@list heading="Common slips" items="Reading B⁻¹ from the slack columns@The first|Building B from the current tableau@The second|Treating a late tableau as degraded@The third"
The first slip is reading B inverse out of the slack columns. The second is building B from the tableau you're checking. Those columns are the identity, so the check passes and tests nothing. The third is treating a tableau many pivots in as a degraded copy of the data.

@end text="Rebuild the tableau by multiplication"
You can pick a basis, invert it, and rebuild the tableau from the original data, on Learn. That's learn dot get er done dot I O.
