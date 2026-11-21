---
format: long
lesson: intro-algorithms-algebraic-topics/linear-programming-and-the-simplex-algorithm
title: Linear programming and the simplex algorithm, corner by corner
thumb: Walk the edges uphill
---

@chapter Limited resources
@title text="Linear Programming and the Simplex Algorithm" sub="Introduction to Algorithms, Sections 29.1–29.3" art=thumb
Chapter twenty nine opens with a campaign deciding how to spend on advertising.

@quote text="Many problems take the form of maximizing or minimizing an objective, given limited resources and competing constraints." cite="Cormen, Leiserson, Rivest and Stein, Introduction to Algorithms, Chapter 29"
Many problems take the form of maximizing or minimizing an objective, given limited resources and competing constraints. A linear program optimizes a linear function, subject to linear equalities and inequalities.

@chapter The picture
@art feasible-region
In two variables you can draw it. Each constraint is a half plane, and together they cut out a convex region. Slide the objective's line as far as it goes while still touching the region, and you end at a corner.

@art corner-walk
The simplex algorithm uses that. Start at a corner, move along an edge to a neighbouring corner that's no worse, and stop at a corner with no better neighbour. Convexity makes that a global optimum. It isn't polynomial in the worst case, but it's fast in practice.

@chapter Standard and slack forms
@list heading="Four repairs to standard form" items="minimize → negate the objective@minimization|free variable → difference of two@no sign constraint|equality → two inequalities@An equality|≥ → multiply by −1@greater than"
Standard form maximizes c transpose x, with A x at most b, and x at least zero. A program can miss it in four ways. Turn a minimization into a maximization by negating. Replace a variable with no sign constraint by the difference of two. An equality becomes two opposite inequalities. And multiply a greater than constraint by minus one.

@art slack-variable
Slack form gives each inequality a slack variable, the room left in it. Now every constraint is an equation. The basic variables, at first the slacks, sit on the left, written in terms of the nonbasic ones on the right.

@chapter Pivoting
@math heading="max z = 3x₁ + 5x₂" items="x₁ ≤ 4 · 2x₂ ≤ 12 · 3x₁ + 2x₂ ≤ 18@subject to;;z = 0 + 3x₁ + 5x₂@In slack form;;s₁ = 4 − x₁ · s₂ = 12 − 2x₂ · s₃ = 18 − 3x₁ − 2x₂@the slacks"
Here's the lesson's program: maximize three x one plus five x two, subject to x one at most four, two x two at most twelve, and three x one plus two x two at most eighteen. In slack form, z equals zero plus three x one plus five x two, with the slacks below. At the origin, z is zero.

@math heading="x₂ enters" items="s₂ = 0 at x₂ = 6 · s₃ = 0 at x₂ = 9@reaches zero;;x₂ = 6 − s₂/2@solving;;z = 30 + 3x₁ − (5/2)s₂@substituting"
X two has a positive coefficient, five, so let it enter. S two reaches zero at x two equals six, and s three at nine. The tightest is s two, so it leaves. Solving its equation gives x two equals six minus s two over two. Substituting, z becomes thirty plus three x one, minus five halves s two.

@words text="(0, 6) → (2, 6) · z = 36" sub="5 corners, 3 visited, 2 pivots"
X one still has a positive coefficient, so the walk goes on. X one enters, s three leaves, and you reach two, six, with z equal to thirty six. Now no coefficient is positive, so it stops. Of the region's five corners, the walk visited three.

@art no-jump
Ask the lab to jump from the origin straight to four, three, and it refuses. Those two bases differ in two columns, and a pivot exchanges only one.

@chapter Can it cycle?
@art degenerate-corner
A pivot can leave z unchanged, when the leaving variable's constant is already zero. That's degeneracy.

@art cycling-loop
A run of degenerate pivots can return to a slack form it's seen before, and go round forever. That's cycling, and it's the only way simplex can fail to stop.

@math heading="Termination" items="≤ C(n + m, m) slack forms@at most;;Bland's rule: smallest index on ties@Breaking ties"
The basic variables determine the slack form, so there are at most n plus m choose m of them. Simplex either stops within that many iterations, or cycles. Breaking ties by the smallest index, Bland's rule, prevents cycling.

@chapter Where people slip
@list heading="Common slips" items="Simplex tries every corner@The first|Stop when z doesn't rise@The second|Leaving variable by largest coefficient@the third"
The first slip is thinking simplex tries every corner. It walks, and here it visited three of five. The second is stopping because z didn't rise. A degenerate pivot can stall it, and the test is the signs. And the third is choosing the leaving variable by the largest coefficient. The tightest limit decides.

@chapter Try it
@words text="max 2x₁ + 3x₂" sub="same constraints · pivot by hand"
Your turn. Change the objective to two x one plus three x two, on the same constraints. In slack form, let the larger coefficient enter, run the pivots to the end, and write each basic solution and the final z.

@end text="Walk the corners"
You can walk the region corner by corner, on Learn. That's learn dot get er done dot I O.
