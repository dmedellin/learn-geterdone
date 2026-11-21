---
format: long
lesson: duality-and-sensitivity-analysis/the-dual-simplex-method
title: The dual simplex method: fix a broken plan without starting over
thumb: Optimal first, feasible next
---

@chapter The question
@title text="The Dual Simplex Method" sub="Duality and Sensitivity Analysis" art=thumb
You've solved a model, and then someone adds a rule your plan breaks. Do you start again? No. The old basis is still a basis of the new problem. It's just not feasible. Fixing that is cheaper than rebuilding.

@art optimal-infeasible
A tableau can be optimal in its objective row and infeasible in its right hand column at the same time. That's exactly what a new constraint leaves behind. The dual simplex method restores feasibility, while keeping optimality.

@chapter One dual pivot
@list heading="One dual pivot" items="Leave: the most negative right-hand side@Leave|Enter: smallest size of zⱼ ÷ a_rj, negative entries only@enter"
Leave by the row with the most negative right hand side. Then, along that row, look only at the negative entries, and enter the column with the smallest ratio: the objective row entry over the row entry, both as sizes.

@art ratio-along-row
Why negative entries only? Raising that variable has to lift a negative right hand side toward zero. And the ratio is the objective given up per unit of infeasibility removed. So the smallest ratio is the cheapest way to become legal.

@words text="Primal simplex, run on the dual"
It's really the primal simplex run on the dual. A negative right hand side is a violated dual constraint. But everything happens in the primal tableau, so no second tableau is needed.

@chapter The workshop cut
@math heading="Add x₁ + x₂ ≤ 5" items="append row 4,  clear x₁ and x₂ out of it@append;;row 4:  0  0  0  −1/6  −1/3  1  |  −3@minus three"
Take the workshop's optimum and add the rule x one plus x two at most five. Append it as row four, and subtract rows to clear the basic x one and x two out of it. Row four becomes zero, zero, zero, minus a sixth, minus a third, one, with right hand side minus three.

@math heading="Pivot 1: row 4 leaves" items="s₂:  (3/2) ÷ (1/6) = 9@nine;;s₃:  1 ÷ (1/3) = 3  →  enters@three;;z: 36 → 27@twenty seven"
Pivot one. Row four leaves, at minus three. The ratios along it: s two gives three halves over a sixth, nine. s three gives one over a third, three. Smallest, so s three enters, and z drops from thirty six to twenty seven.

@math heading="Pivot 2: row 1 leaves" items="row 1 rhs −1@minus one;;s₂:  1 ÷ (1/2) = 2  →  enters@two;;s₄:  entry +1, not eligible@plus one;;z: 27 → 25 at (0, 5)@twenty five"
Pivot two. Row one now has minus one. Along it, s two gives one over a half, two. s four's entry is plus one, so raising it can't help. s two enters, and z drops to twenty five, at zero, five. Every right hand side is non negative. Done. And a fresh solve gives twenty five as well.

@art falling-value
Notice the value fell: thirty six, twenty seven, twenty five. On an infeasible tableau the value overstates what the basis would earn. Each pivot brings it down to meet the real answer. If it rises, you misapplied the ratio test.

@chapter Predict first
@art cut-region
Before you pivot, try to predict the landing point. Most people guess two, three, or four, one: small adjustments that obey the new rule. The answer is zero, five, which drops the first product altogether.

@chapter Other outcomes
@math heading="Three-activity plan (2, 6, 0), z* = 46" items="add x₁ + x₂ + x₃ ≤ 6:  broken by 2@breaks it by two;;x₃:  4 ÷ 1 = 4,  s₂:  2 ÷ 1 = 2  →  s₂ enters@s two enters;;one pivot:  42 at (4, 2, 0)@forty two"
On the three activity programme, add x one plus x two plus x three at most six. The plan breaks it by two. The ratios give four for x three and two for s two, so s two enters. One pivot, and the answer is forty two, at four, two, zero.

@art no-pivot
Add x one plus x two at most ten to the workshop instead, and the new row's right hand side is plus one. No negative entry anywhere, so zero pivots. That's the cheapest outcome, and the common one.

@art impossible-row
And it can fail. Add x one plus x two at least nine. The region's largest total is eight. The leaving row ends up with no negative entry at all, which says non negative things add up to a negative number. The rule is unsatisfiable.

@chapter Where people slip
@list heading="Common slips" items="Starting again from scratch@The first|Using every entry in the ratio test@The second|Expecting the new plan to be nearby@The third"
The first slip is starting again because the problem changed. The second is taking the ratio over every entry of the leaving row. The symptom is a value that rises. And the third is expecting the new plan to be near the old one. This method is also why branch and bound is affordable: each child re solves from its parent's tableau.

@end text="Predict, then pivot"
You can add a rule, predict the landing plan, and watch the dual pivots, on Learn. That's learn dot get er done dot I O.
