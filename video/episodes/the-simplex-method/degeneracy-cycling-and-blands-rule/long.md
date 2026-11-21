---
format: long
lesson: the-simplex-method/degeneracy-cycling-and-blands-rule
title: Degeneracy and cycling: when simplex runs in circles
thumb: Six pivots, back to the start
---

@chapter The question
@title text="Degeneracy, Cycling and Bland's Rule" sub="The Simplex Method" art=thumb
Every simplex pivot changes the basis. But does every pivot actually move you? Not always. And if enough pivots go nowhere, the method can end up exactly where it started, forever.

@chapter Degeneracy
@art three-lines
A basic feasible solution is degenerate when some basic variable is zero. Geometrically, more boundaries pass through the point than its dimension needs. In two variables, three lines through one corner. Then several bases name that same point.

@math heading="max 3x₁ + 9x₂" items="x₁ + 4x₂ ≤ 8@plus four x two;;x₁ + 2x₂ ≤ 4@plus two x two;;ratios: 8 ÷ 4 = 2,  4 ÷ 2 = 2  (tie)@a tie"
Take maximise three x one plus nine x two, with x one plus four x two at most eight, and x one plus two x two at most four. Both boundaries, and the axis x one equals zero, pass through zero, two. On column x two, the ratios are eight over four, two, and four over two, also two. A tie.

@math heading="Two pivots" items="pivot 1:  x₂ in,  s₂ = 0 basic,  z = 18@pivot one;;pivot 2:  ratios 8 and 0,  step 0@step is zero;;still (0, 2),  z = 18,  optimal@still zero, two"
Pivot one brings x two in, and s two stays basic, at zero. z is eighteen. Pivot two brings x one in. The ratios are eight and zero, so the step is zero. The point is still zero, two, z is still eighteen, and now the objective row certifies it's optimal.

@art zero-step
Look at that second pivot. It changed the basis, and left the point and the objective exactly where they were. A step of length zero.

@art same-point
That pivot moved nothing, but it wasn't wasted. It changed the basis to the one whose objective row proves optimality.

@chapter Cycling
@math heading="Beale's example" items="max (3/4)x₁ − 150x₂ + (1/50)x₃ − 6x₄@three quarters;;(1/4)x₁ − 60x₂ − (1/25)x₃ + 9x₄ ≤ 0@Two rows;;(1/2)x₁ − 90x₂ − (1/50)x₃ + 3x₄ ≤ 0@right hand side zero;;x₃ ≤ 1@at most one"
Can zero length pivots go round in a circle? They can. Here's Beale's example. Maximise three quarters x one, minus a hundred and fifty x two, plus a fiftieth x three, minus six x four. Two rows have right hand side zero, and x three is at most one.

@art cycle-loop
The starting point is already degenerate. Use the most negative rule, breaking ratio ties by lowest row. Every pivot has step zero. After six of them, the basis is the three slacks again, and the tableau is identical, entry for entry.

@words text="z = 0 forever;  true optimum 1/20"
Left alone, it runs forever at z equals zero. The true optimum is one twentieth.

@words text="Exact, entry for entry" sub="no tolerance"
That the sixth tableau equals the first is a claim about exact numbers. That's why the course uses exact fractions. In floating point, it would come back nearly equal, and the lesson would be about what nearly means.

@chapter Bland's rule
@list heading="Bland's rule" items="Enter the lowest-index improving column@enter the lowest|Leave by the lowest-index basic variable@leave from the row"
Bland's rule fixes it. Among improving columns, enter the lowest index. Among rows tied for the minimum ratio, leave from the row whose basic variable has the lowest index. Neither choice looks at the size of anything.

@art finite-walk
Why does it terminate? There are finitely many bases. Under Bland's rule, no basis is ever visited twice. A walk through a finite set that never repeats must stop. That says nothing about how many bases it visits, though.

@math heading="Beale, under Bland" items="pivots 1–4 agree@agree for four;;pivot 5:  x₁ in, row 3 leaves, step 2/125@two over a hundred and twenty five;;pivot 6:  x = (1/25, 0, 1, 0),  z = 1/20@one twentieth"
On Beale's programme, the two rules agree for four pivots. Then Bland's fifth brings x one back in, leaving row three, with a step of two over a hundred and twenty five. It's the first pivot that moves at all. The sixth reaches one twenty fifth, zero, one, zero, with z one twentieth.

@words text="6 pivots either way" sub="greatest improvement: 2"
Six pivots either way, a different ending. Greatest improvement and the largest index rule both get there in two.

@chapter What degeneracy is not
@art not-rounding
It isn't rounding, or trouble with arithmetic. Every number in the cycle is exact, and the cycle is still there. Degeneracy is very common in practice. Cycling is rare enough that many solvers don't defend against it until a problem needs them to.

@chapter Where people slip
@list heading="Common slips" items="An unchanged objective means finished@The first|Calling a cycle a precision problem@The second|Calling a degenerate optimum defective@The third"
The first slip is reading an unchanged objective as a finished method. The stopping test is the objective row, not the value. The second is diagnosing a cycle as a precision problem. The fix is a rule, not a tolerance. The third is treating a degenerate optimum as defective. It's optimal. But dual values read from it may differ between tied bases.

@end text="Watch the cycle close"
You can run Beale's example, watch the tableau come back entry for entry, and break it with Bland's rule, on Learn. That's learn dot get er done dot I O.
