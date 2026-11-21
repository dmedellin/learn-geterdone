---
format: long
lesson: integer-programming/either-or-constraints-and-disjunctions
title: Either-or constraints: one binary, two big-M rows
thumb: This one, or that one
---

@chapter The problem
@title text="Either–Or Constraints" sub="Integer Programming" art=thumb
Here's a choice that a list of constraints can't make on its own.

@art one-machine
Two jobs share one machine. Job one takes four hours, job two takes three, and they can't run at the same time. One of them has to go first. How do you write a choice into a model made of constraints that all hold at once?

@art two-orders
Let x one and x two be the start times. Either job one finishes before job two starts, x one plus four at most x two. Or job two finishes first, x two plus three at most x one. Exactly one of those must hold.

@chapter Writing both is the conjunction
@math heading="Both rows at once" items="x₁ − x₂ ≤ −4@minus four;;−x₁ + x₂ ≤ −3@minus three;;add:  0 ≤ −7  ✗@zero"
The obvious move is to write both. As at most rows, that's x one minus x two, at most minus four, and minus x one plus x two, at most minus three. Add them, and the left side cancels to zero, the right side gives minus seven. Zero at most minus seven. Infeasible.

@art contradiction-arrows
Constraints are simultaneous. Adding a row never creates a choice. It only removes plans. Recognise this diagnosis, because the symptom is a solver reporting infeasible on data that's perfectly consistent, and people go hunting for a typo in the processing times.

@chapter One binary switches the rows
@math heading="Either–or pair" items="x₁ − x₂ ≤ −4 + 14(1 − y)@fourteen;;−x₁ + x₂ ≤ −3 + 13y@thirteen"
Instead, relax each row with a big M term that one binary switches off. The first row gets fourteen times one minus y. The second gets thirteen times y.

@art switch-rows
At y equals one, the first term vanishes and job one goes first, while the second row is relaxed by thirteen and nothing can break it. At y equals zero, the roles swap. The binary isn't a quantity. It's the choice the problem contains.

@words text="M_A = 14 · M_B = 13" sub="start times in [0, 10]"
Where do fourteen and thirteen come from? Both start times lie between zero and ten. The most the first row's left side can exceed its right side is ten minus zero minus minus four, fourteen. By the mirror argument, the second needs thirteen. Each is exactly the slack its own row needs.

@chapter Both branches, solved
@math heading="Minimise x₁ + x₂" items="y = 1:  start (0, 4),  cost 4@y equals one;;y = 0:  start (3, 0),  cost 3@y equals zero"
Minimise the sum of the start times. With y equals one, job one first, the jobs start at zero and four, costing four. With y equals zero, job two first, they start at three and zero, costing three. Both are real schedules. The second is cheaper.

@chapter What the relaxation does
@art overlap-clash
Now let y be anything between zero and one. The relaxation sets y to three thirteenths, starts both jobs at time zero, and reports zero. Every row is satisfied, because both are half relaxed at once.

@words text="0 is a bound, not a schedule"
Zero is a perfectly good lower bound on the answer of three. But it isn't a schedule. One machine can't run two jobs at once because a variable took a value in between. And three thirteenths isn't a probability either.

@chapter Each M for its own row
@art job-shop-pairs
One M for both rows, unchecked, is how an or quietly becomes an if then. And this pair, repeated over every pair of jobs on every machine, is what makes a job shop an integer programme. The sequencing decision is a binary, and there's no linear model of it.

@chapter Where people slip
@list heading="Common slips" items="Writing both constraints@The first|One M for both rows, unchecked@The second|Reading a fractional y as mostly one order@And the third"
The first slip is writing both constraints. The second is using one M for both rows without checking it against each. And the third is reading a fractional y as mostly one order. It's a point where both rows are partly relaxed, describing a schedule that can't be run.

@chapter Try it
@words text="Job one takes 5, not 4" sub="start times in [0, 10]"
Your turn. Suppose job one takes five hours instead of four. Rewrite the first row, and work out the smallest valid M for it, using the same reasoning: how far can its left side exceed its right side when both start times lie between zero and ten?

@end text="Solve both branches"
You can fix the binary each way, re-solve, and see both schedules, on Learn. That's learn dot get er done dot I O.
