---
format: long
lesson: linear-programming-models/standard-form-slack-and-surplus
title: Standard form: slack, surplus, and the sign that isn't a convention
thumb: Add a slack, subtract a surplus
---

@chapter The question
@title text="Standard Form, Slack and Surplus" sub="Linear Programming Models" art=thumb
Solvers want one shape: equalities, with every variable at least zero. Getting there means adding new columns. And every one of them measures something real.

@art pottery-kiln
A pottery fires pieces plain or glazed. F pieces are left plain and G are glazed, both in pieces a day. Plain costs three to make, and glazed costs five. The pottery minimises cost.

@math heading="The pottery" items="minimise 3F + 5G@minimise;;F + G ≥ 4@at least four;;2F + G ≤ 10@at most ten;;F ≤ 4@at most four plain;;F, G ≥ 0@at least zero"
So you minimise three F plus five G. A delivery contract wants at least four pieces. The kiln takes at most ten firing units, two per plain piece and one per glazed. A licence allows at most four plain pieces. And both are at least zero.

@chapter Standard form
@math heading="The conversions" items="a·x ≤ b  →  a·x + s = b@add a slack;;a·x ≥ b  →  a·x − e = b@subtract a surplus;;x free  →  x⁺ − x⁻@split;;minimise f  →  maximise −f@maximise minus f"
Standard form is maximise c x, subject to A x equals b, and x at least zero. To get there, add a slack to each at most row. Subtract a surplus from each at least row. Split each free variable into two non negative parts. And minimise f by choosing to maximise minus f.

@art equal-sign
A slack fills the gap up to a limit. A surplus takes away the amount you went over. Either way, the row becomes an equation, and the new variable is never negative.

@words text="Exact, not an approximation"
This transformation is exact. Feasible points match one to one, and so do the objective values, up to a sign you have to put back.

@chapter What the columns mean
@list heading="Added columns" items="e₁: pieces delivered beyond the four@e one|s₂: firing units the kiln has left@s two|s₃: plain pieces the licence still allows@s three|a₁: artificial, measures nothing@a one"
The pottery gets three meaningful columns. e one is the pieces delivered beyond the four promised. s two is the firing units the kiln has left. s three is the plain pieces the licence still allows. There's a fourth, a one, an artificial variable. It measures nothing, and it's there only to give the search a starting basis.

@chapter Every corner
@art four-corners
Now read those columns at each corner of the region. That turns the phrase tight if and only if the added variable is zero into something you can read, rather than accept.

@math heading="Corners:  e₁,  s₂,  s₃,  cost" items="(0, 4):   0,  6,  4,  cost 20@zero, four;;(0, 10):  6,  0,  4,  cost 50@zero, ten;;(4, 0):   0,  2,  0,  cost 12@four, zero;;(4, 2):   2,  0,  0,  cost 22@four, two"
The region has four corners. At zero, four, the added columns are zero, six, four, and the cost is twenty. At zero, ten, they're six, zero, four, for fifty. At four, zero, they're zero, two, zero, for twelve, the cheapest. And at four, two, they're two, zero, zero, for twenty two.

@art corner-table
At four, zero, the contract is met exactly and the licence is used up, so two rows are tight. The kiln has two firing units to spare. A row is tight exactly when its own added variable is zero. Read down a column to see where a row is tight. Read across to describe a corner completely.

@chapter The sign is forced
@math heading="If you add the surplus" items="F + G + e₁ = 4@plus e one;;at (0, 10):  e₁ = −6@minus six;;only exact deliveries survive@exactly"
Why subtract the surplus? Suppose you wrote F plus G plus e one equals four. At zero, ten, that needs e one equals minus six. The only feasible points left are ones where the contract is met exactly.

@art sign-trap
The programme has silently gained a new requirement. And every method that follows assumes x at least zero, so it would carry the error forward without a murmur. Check the new variable's sign at one feasible point you already know.

@chapter Negate it back
@math heading="Maximising engine" items="maximise −3F − 5G@minus three F;;engine returns −12@minus twelve;;cost = 12@twelve"
The engine maximises. So the cost goes in as maximise minus three F minus five G. The answer comes back as minus twelve, and you negate it to twelve. That last step is the one people forget. A negative cost is a symptom worth recognising.

@art flipped-row
Now flip the kiln row to at least ten firing units. It takes a surplus instead of a slack, needs a second artificial, and the added columns rise from four to five. The cheapest plan moves from twelve at four, zero, to twenty two at four, two. One character, and everything moves.

@chapter Where people slip
@list heading="Common slips" items="Adding a surplus instead of subtracting@The first|Reporting the negated objective@The second|Treating added columns as clerical@The third"
The first slip is adding a surplus instead of subtracting it. The second is reporting the negated objective. And the third is treating the added columns as clerical. Later, prices and ranges are read straight off these columns.

@end text="Read every column at every corner"
You can convert the pottery and read every added column at every corner, on Learn. That's learn dot get er done dot I O.
