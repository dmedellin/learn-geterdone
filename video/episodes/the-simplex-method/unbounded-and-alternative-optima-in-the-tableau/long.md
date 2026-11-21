---
format: long
lesson: the-simplex-method/unbounded-and-alternative-optima-in-the-tableau
title: Reading unbounded and tied optima straight off the tableau
thumb: The column is the ray
---

@chapter The question
@title text="Unbounded and Alternative Optima in the Tableau" sub="The Simplex Method" art=thumb
Most tableaux end with one clean answer. But two awkward cases leave a signature you can read. One says the objective has no ceiling. The other says the best answer isn't unique.

@chapter The unbounded signature
@words text="z_j < 0  and every aᵢⱼ ≤ 0" sub="→ unbounded"
Here's the first. A feasible tableau has an improving column, a negative reduced cost, and no positive entry anywhere in that column. That certifies the objective is unbounded.

@art escape-ray
It's the ratio test read backwards. Each basic variable equals b i minus a i j times t. With every entry at most zero, none of them ever falls. So nothing stops t growing, while the objective rises at the column's rate.

@math heading="max x₁ + x₂" items="x₁ − x₂ ≤ 1@x one minus x two;;−x₁ + x₂ ≤ 1@minus x one;;column x₂:  (−1, 0),  z₂ = −2@minus two"
Take maximise x one plus x two, with x one minus x two at most one, and minus x one plus x two at most one. One pivot brings x one in. Then x two's column is minus one, zero, with reduced cost minus two. Improving, with no positive entry.

@math heading="The ray from (1, 0)" items="d = (1, 1, 0, 0)@the ray;;t = 1:  (2, 1),  z = 3@t equals one;;t = 10:  (11, 10),  z = 21@t equals ten;;t = 100:  (101, 100),  z = 201@a hundred"
The column becomes the ray: d equals one, one, zero, zero, from the point one, zero. At t equals one, you're at two, one, with z three. At t equals ten, eleven, ten, with z twenty one. At t equals a hundred, a hundred and one, a hundred, with z two hundred and one. Every one satisfies both constraints.

@art three-samples
That's what turns the word unbounded into a proof. You don't just claim it. You hand over the direction, and anyone can check it.

@chapter Alternative optima
@words text="optimal, and z_j = 0 on a nonbasic column"
The second signature is at optimality. If a nonbasic column has reduced cost exactly zero, pivoting it in reaches another optimal corner. Rate zero, times any step, is zero.

@art basic-zero
The word nonbasic does all the work. Every basic column always has reduced cost zero. That's how the tableau is held. The signature is a zero where an improving column could have been.

@chapter A whole optimal edge
@math heading="max 3x₁ + 2x₂" items="3x₁ + 2x₂ ≤ 12,  x₁ ≤ 3,  x₂ ≤ 5@at most twelve;;stop at (3, 3/2),  z = 12@three halves;;pivot s₂ in → (2/3, 5),  z = 12@two thirds"
Take maximise three x one plus two x two, with three x one plus two x two at most twelve, x one at most three, x two at most five. The objective is parallel to that first boundary. The method stops at three, three halves, with z twelve, and s two has reduced cost zero. Pivot it in, and you reach two thirds, five, also twelve.

@art optimal-edge
Sample the segment between them, at a quarter, a third, a half, three quarters. At the halfway point you get eleven sixths, thirteen quarters. And the objective at every sample is exactly twelve. The whole edge is optimal.

@words text="One corner: true, not the whole truth"
A solver that prints one corner has told the truth, not the whole truth. Any point on that edge is equally good, so a second criterion is free to choose. Naming the second corner costs one pivot.

@chapter Unbounded region, bounded objective
@art open-region-bounded
Take maximise two x one minus x two, with x one minus x two at most one, and x one at most six. The region runs on forever, as x two grows. But the objective has a best value, seven at six, five, because it falls in exactly the direction the region escapes.

@words text="Diagnose from a column, never the drawing"
So unboundedness is about the region and the objective together. And on a model of something real, an unbounded objective is nearly always a missing constraint.

@chapter Where people slip
@list heading="Common slips" items="Unbounded region means unbounded objective@The first|A basic zero as alternative optima@The second|Confusing alternative optima with degeneracy@The third"
The first slip is reading an unbounded region as an unbounded objective. The second is taking a zero on a basic column as alternative optima. And the third is confusing alternative optima with degeneracy. Alternative optima: a zero reduced cost on a nonbasic variable. Degeneracy: a zero value on a basic variable.

@art two-zeros
They live in different places in the tableau. The first is a reporting matter. The second, degeneracy, can stop the method finishing at all.

@end text="Find the ray, find the second corner"
You can follow a ray out of a tableau, and pivot to the second optimal corner, on Learn. That's learn dot get er done dot I O.
