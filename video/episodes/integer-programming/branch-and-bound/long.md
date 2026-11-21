---
format: long
lesson: integer-programming/branch-and-bound
title: Branch and bound: split, bound, and close for three reasons
thumb: Proved empty, not skipped
---

@chapter The question
@title text="Branch and Bound" sub="Integer Programming" art=thumb
Rounding can't be trusted, and trying every whole point doesn't scale. Branch and bound finds the integer optimum and proves it, without looking at most of the region. Here's how, on one small example.

@math heading="The model" items="max 5x₁ + 4x₂@maximise;;6x₁ + 4x₂ ≤ 25@machine;;3x₁ + 5x₂ ≤ 22@inspection"
Maximise five x one plus four x two. Six x one plus four x two is at most twenty five machine hours. Three x one plus five x two is at most twenty two inspection hours. And both variables must be whole.

@art lp-corner
The relaxation stops at thirty seven eighteenths, nineteen sixths, worth four hundred and thirteen eighteenths, about twenty two point nine four. Both coordinates are fractional. It isn't a plan.

@chapter Branching
@words text="x₁ ≤ 2   or   x₁ ≥ 3" sub="x₁ = 37/18 at the root"
Pick a fractional variable, say x one at thirty seven eighteenths. Replace the problem by two children: one with x one at most two, and one with x one at least three.

@art branch-split
Every whole plan satisfies one of those, because there's no integer strictly between two and three. And the fractional point satisfies neither. So nothing is lost, and both children are strictly smaller.

@art fixed-vs-inequality
That's why the children are inequalities. Fixing x one to two in one child and three in the other would lose every plan with x one at zero, one, four or five, and the search would confidently return a wrong answer.

@chapter Three reasons to close
@art three-closures
A node closes for exactly three reasons. It's infeasible: nothing is in it. It's bounded out: its bound can't beat the best whole plan in hand. Or it's integral: the relaxation came back whole, so it's the best plan in that node. There's no fourth reason.

@chapter The five-node tree
@math heading="Branch on x₁" items="x₁ ≤ 2:  bound 114/5 at (2, 16/5)@at most two;;x₁ ≥ 3:  bound 22 at (3, 7/4)@at least three"
Branch on x one. The child with x one at most two bounds at a hundred and fourteen fifths, at two, sixteen fifths, still fractional. The child with x one at least three bounds at twenty two, at three, seven quarters.

@math heading="Then branch on x₂" items="x₂ ≤ 3:  (2, 3) whole, worth 22  ✓@at most three;;x₂ ≥ 4:  bound 58/3 ≈ 19.33, closes@at least four;;x₁ ≥ 3:  bound 22, closes@twenty two either"
Now split on x two. At most three, it comes back at two, three, whole, worth twenty two. That's the plan in hand. At least four, the bound is fifty eight thirds, about nineteen point three three, which can't beat twenty two. And x one at least three bounds at exactly twenty two, which can't beat twenty two either.

@art search-tree
Five nodes, nothing open, and the answer is twenty two, at two, three. In this run that's depth first. Best bound takes seven nodes on this instance, the opposite of what you might expect. The order changes the work, never the answer.

@art pruned-branch
Look at those last two closures, because they are the method. Neither node was explored. A bound of fifty eight thirds is a promise that nothing inside is worth more. With twenty two in hand, that region has been searched, by arithmetic.

@chapter The bound is a linear programme
@words text="Each child starts from its parent's tableau" sub="re-solved by the dual simplex"
What's special here is that the bound is a linear programme. Adding x one at most two to a solved tableau leaves it optimal but infeasible, exactly the job the dual simplex was built for. So each child costs a few pivots, not a fresh solve.

@chapter Where people slip
@list heading="Common slips" items="Branching by fixing to a rounded value@The first|Exploring a worse-bounded node anyway@The second|Reporting an optimum from an open tree@And the third"
The first slip is branching by fixing the variable to a rounded value. The second is exploring a worse bounded node in case something good is inside. A bound is a proof, not an estimate. And the third is reporting an optimum from a tree that hasn't closed.

@chapter Try it
@words text="Branch on x₂ first" sub="x₂ = 19/6 at the root"
Your turn. Start again at the root, but branch on x two at nineteen sixths instead. Write the two children, x two at most three and x two at least four, and say what each must still allow. Then check that two, three lies in exactly one of them.

@end text="Grow the tree yourself"
You can pick each branching variable and watch nodes close for each reason, on Learn. That's learn dot get er done dot I O.
