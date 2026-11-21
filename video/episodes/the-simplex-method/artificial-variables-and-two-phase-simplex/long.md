---
format: long
lesson: the-simplex-method/artificial-variables-and-two-phase-simplex
title: Two-phase simplex: building a start, or proving there isn't one
thumb: Phase one: find a start
---

@chapter The question
@title text="Artificial Variables and Two-Phase Simplex" sub="The Simplex Method" art=thumb
So far every tableau started at the origin, because every row had a slack, and the slacks formed an identity. But what if some rows say at least, or equals? Then there's nothing to start from.

@math heading="No identity column" items="x₁ + x₂ ≥ 4  →  x₁ + x₂ − e₁ = 4@minus e one;;start reading:  e₁ = −4  ✗@minus four;;= row:  no new column at all@no new column"
Turn x one plus x two at least four into an equation and you get x one plus x two minus e one equals four. The surplus column is minus one, so starting from it would read e one equals minus four. Not feasible. An equals row is worse. It adds no new column at all.

@chapter Artificial variables
@art patch-column
So add an artificial variable to each such row, with coefficient plus one, purely to supply an identity column. It means nothing in the situation. A solution of the original problem is exactly one where every artificial is zero.

@math heading="minimise 2x₁ + 3x₂" items="x₁ + x₂ − e₁ + A₁ = 4@demand;;2x₁ + x₂ − e₂ + A₂ = 5@quality floor;;x₁ + s₃ = 3@capacity"
Take minimise two x one plus three x two. The demand row, x one plus x two at least four, gets a surplus and an artificial. So does the quality floor, two x one plus x two at least five. The capacity row, x one at most three, gets an ordinary slack.

@words text="A₁ = 4,  A₂ = 5,  s₃ = 3" sub="x = (0, 0)"
The identity columns are A one, A two and s three. The starting reading is A one four, A two five, s three three, with x at zero. That's feasible for the bigger system and meaningless for the original. It meets demand with four units of nothing.

@chapter Phase one
@math heading="Phase I" items="minimise A₁ + A₂@minimise the sum;;pivot: x₁ in, A₂ out@x one in;;pivot: x₂ in, A₁ out@x two in;;optimum 0@zero"
Phase one is its own linear programme: minimise the sum of the artificials. Here it takes two pivots. x one in and A two out, then x two in and A one out. The optimum is zero, with neither artificial left in the basis.

@art shrinking-artificials
Watch what happened. The artificials started out carrying all of the demand and the quality floor. Each pivot swapped one of them for a real variable, until there was nothing artificial left to carry.

@chapter Phase two
@math heading="Phase II" items="drop the artificial columns@drop;;fresh objective row from 2x₁ + 3x₂@fresh;;one pivot → x = (3, 1)@three, one;;2(3) + 3(1) = 9@nine"
Now drop the artificial columns. Build a fresh objective row from the real objective, at the basis phase one handed over. Phase two needs one pivot and finishes at three, one, costing two times three plus three times one, which is nine.

@art phase-two-arrow
The basis it hands over is a genuine corner of the original region. From there, phase two is an ordinary simplex walk.

@art handover
Three pivots in total. The only unusual thing is that the first two were optimising a different objective. And don't carry phase one's objective row into phase two. It holds reduced costs for the wrong objective.

@chapter When phase one can't reach zero
@math heading="x₁ + x₂ ≤ 1  and  x₁ + x₂ ≥ 4" items="phase I stops at 3@stops at three;;y = (−1, 1)@multipliers minus one;;combined:  0 ≥ 3@zero at least three"
Now take x one plus x two at most one, together with x one plus x two at least four. Phase one stops at three. Combine the rows with multipliers minus one and one. Every variable cancels, and the right hand sides give zero at least three. That's a contradiction.

@art empty-region
So a positive phase one optimum isn't a convergence failure. It's a proof of infeasibility, and the value is exact. It's the smallest amount of cheating the rows need. A blank picture was standing in for that one line argument.

@chapter An artificial left at zero
@art redundant-row
Phase one can also finish at zero with an artificial still basic, at value zero. Take x one plus x two equals four, with the same row doubled, two x one plus two x two equals eight. That second row is redundant, so no real column can replace its artificial.

@words text="Degenerate, not a failure"
That's a degenerate basic feasible solution. Phase two runs from it, and the artificial is held at zero, or driven out on the way.

@words text="Big-M" sub="needs a large enough M, chosen in advance"
There's a one phase alternative called big M. It keeps the artificials in the real objective with a huge penalty. It works, but you must choose M large enough before you've solved anything. Two phases need no such constant.

@chapter Where people slip
@list heading="Common slips" items="Treating an artificial as a slack@The first|Reusing phase one's objective row@The second|Calling a positive phase one a bug@The third"
The first slip is treating an artificial as a slack. A slack measures something. An artificial measures nothing. The second is reusing phase one's objective row. And the third is reading a positive phase one optimum as a convergence problem. It's the answer, and infeasible is often the most useful thing a model can tell you.

@end text="Run both phases"
You can run phase one, watch the handover, and check an infeasibility certificate, on Learn. That's learn dot get er done dot I O.
