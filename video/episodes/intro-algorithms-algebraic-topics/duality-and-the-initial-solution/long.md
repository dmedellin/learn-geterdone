---
format: long
lesson: intro-algorithms-algebraic-topics/duality-and-the-initial-solution
title: LP duality: how to prove an answer is optimal
thumb: Plans below, prices above
---

@chapter Proving the stop was right
@title text="Duality and the Initial Basic Feasible Solution" sub="Introduction to Algorithms, Sections 29.4–29.5" art=thumb
The simplex walk stopped when no coefficient in z was positive. But how do you know that's really the best?

@quote text="Duality enables us to prove that a solution is indeed optimal." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Section 29.4"
Section twenty nine point four answers it. Duality enables us to prove that a solution is indeed optimal. The pattern is from chapter twenty six, where a flow is shown maximum by a cut of the same value.

@chapter The dual
@art plans-and-prices
Building the dual is mechanical. Give each primal constraint a nonnegative variable, y i. Minimize b transpose y. And for each primal variable, require that the y's, weighted by its column, add up to at least its objective coefficient.

@math heading="The last lesson's program" items="primal: max 3x₁ + 5x₂@The primal;;dual: min 4y₁ + 12y₂ + 18y₃@Its dual;;y₁ + 3y₃ ≥ 3 · 2y₂ + 2y₃ ≥ 5@subject to;;y = (0, 3/2, 1) → 36@the point"
The primal maximizes three x one plus five x two. Its dual minimizes four y one plus twelve y two plus eighteen y three, subject to y one plus three y three at least three, and two y two plus two y three at least five. The point zero, three halves, one meets both with equality, and gives thirty six.

@chapter Weak duality
@math heading="Lemma 29.8" items="cᵀx ≤ (Aᵀy)ᵀx = yᵀ(Ax) ≤ bᵀy@c transpose x"
Weak duality is two lines of algebra. C transpose x is at most y transpose A x, because the prices cover every column and x is nonnegative. And that's at most b transpose y, because A x is at most b and y is nonnegative.

@art bracket
So any feasible plan sits below any feasible set of prices. If the two values are equal, no plan can beat this one, and no prices can undercut these.

@words text="Theorem 29.10" sub="y from SIMPLEX's last slack form is optimal"
And simplex hands you the prices for free. When it stops, set each y i to minus the final coefficient of slack s i if it's nonbasic, and zero if it's basic. The last walk ended with z equal to thirty six minus three halves s two, minus s three. That's y equals zero, three halves, one.

@chapter Closing the bracket
@math heading="The lab's chain: cᵀx ≤ yᵀAx ≤ bᵀy" items="x = (1, 1), y = (0, 2, 1): 8 ≤ 9 ≤ 42@one, one;;x = (2, 6), y = (0, 1.5, 1): 36 = 36 = 36@two, six"
In the lab, the plan one, one, with prices zero, two, one, gives eight, at most nine, at most forty two. The optimum lies between eight and forty two, and neither number needed a solver. Type the plan two, six and prices zero, one and a half, one, and all three links read thirty six. The gap is zero.

@art uncovered
Prices that don't cover every column bound nothing. One, one, zero gives sixteen, below the true optimum, and the lab marks both columns uncovered.

@chapter Where to start
@art infeasible-origin
Section twenty nine point five asks where simplex starts. If every b i is nonnegative, the origin is a feasible corner. If some b i is negative, the origin is outside the region, though the program may still be feasible.

@math heading="L_aux" items="maximize −x₀@maximize minus;;Σⱼ aᵢⱼxⱼ − x₀ ≤ bᵢ for every i@subtracted from every;;optimum 0 ⇔ L feasible@exactly when"
The fix is an auxiliary program. Add one variable, x zero, subtracted from every constraint, and maximize minus x zero. With x zero large enough, every constraint holds. Its optimum is zero exactly when the original program is feasible.

@art aux-lift
Its own first slack form is infeasible too, but one pivot fixes that. Let x zero enter, and the slack of the row with the most negative b leave. Then run simplex on it. If the optimum is negative, the original program is infeasible.

@art three-outcomes
That gives the fundamental theorem of linear programming. Every program is infeasible, or unbounded, or has a finite optimum. And simplex, with this start, returns the right one of the three.

@chapter Where people slip
@list heading="Common slips" items="Optimality needs a search@The first|Prices that miss a column@The second|The origin is always a start@the third"
The first slip is believing optimality can only be shown by searching for something better. A matching dual solution proves it. The second is using prices that don't cover every column. And the third is assuming the initial slack form is always feasible.

@chapter Try it
@words text="y₁ = 1 · max x₁ + x₂, x₁ + x₂ ≥ 8, x₁ ≤ 4, x₂ ≤ 3" sub="L_aux optimum: −1/3"
Your turn. Find dual prices with y one equal to one, and the bound they certify. Then write the auxiliary program for this second program, and show without simplex that its optimum is minus one third, so the program is infeasible.

@end text="Close the bracket"
You can bracket the optimum with plans and prices until it closes, on Learn. That's learn dot get er done dot I O.
