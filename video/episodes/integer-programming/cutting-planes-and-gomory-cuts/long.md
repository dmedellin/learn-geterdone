---
format: long
lesson: integer-programming/cutting-planes-and-gomory-cuts
title: Gomory cuts: slicing off a fractional corner without losing a plan
thumb: Cut the corner, keep the points
---

@chapter The idea
@title text="Cutting Planes and Gomory Cuts" sub="Integer Programming" art=thumb
Branch and bound splits the region in two. There's another way to get rid of a fractional corner: slice it off with one new inequality, so carefully that no whole number plan is lost.

@math heading="The model" items="max x₁ + x₂@maximise;;2x₁ + 5x₂ ≤ 16  kiln@kiln;;6x₁ + 5x₂ ≤ 30  glaze@glaze"
Maximise x one plus x two. Two x one plus five x two is at most sixteen kiln hours. Six x one plus five x two is at most thirty of glaze.

@art lp-corner-cut
The relaxation stops where those rows meet, at seven halves, nine fifths, worth fifty three tenths. The best whole plans are worth five, and there are three of them: three, two, four, one, and five, zero.

@chapter Fractional parts
@art floor-split
Every number splits into its floor and a fractional part between zero and one. Nine fifths has floor one, and fractional part four fifths. On a fraction that's division with remainder. Nothing is rounded.

@math heading="Gomory cut" items="row:  Σ a_j x_j = b@a row;;a_j = ⌊a_j⌋ + f_j,   b = ⌊b⌋ + f₀@split;;cut:  Σ f_j x_j ≥ f₀@the cut"
Take a row of the final tableau whose basic variable is fractional. Split every coefficient, and the right hand side, into floor plus fractional part. Then the cut says the fractional parts times the variables add up to at least the fractional part of the right side.

@chapter Why no plan is lost
@words text="Σ f_j x_j − f₀ = ⌊b⌋ − Σ ⌊a_j⌋ x_j" sub="an integer, greater than −1, so at least 0"
Move the floors to one side. For whole x, the right side is an integer, so the left side is too. And it's greater than minus one, because every fractional part and every x is non negative, and f zero is less than one. An integer greater than minus one is at least zero. That's the cut.

@chapter Two cuts, a whole corner
@math heading="Cut 1, from the row of x₂" items="(3/10)s₁ + (9/10)s₂ ≥ 4/5@in the tableau;;6x₁ + 6x₂ ≤ 31@in your own;;at (7/2, 9/5):  159/5 = 31.8  ✗@breaks it"
The row for x two gives three tenths s one plus nine tenths s two, at least four fifths, in the tableau, using its slack variables. In your own coordinates, that's six x one plus six x two, at most thirty one. At the corner the left side is thirty one point eight, so it breaks it.

@art valid-cut
At every whole point it holds. Six x one plus six x two is a multiple of six, so breaking thirty one would need thirty six, meaning x one plus x two at least six. Nothing in the region gets near that.

@math heading="Re-solve, then cut again" items="one pivot:  (25/6, 1),  z = 31/6@one dual simplex;;cut 2:  x₁ + x₂ ≤ 5@second cut;;one pivot:  (5, 0),  z = 5  whole@five, zero"
One dual simplex pivot moves the optimum to twenty five sixths, one, worth thirty one sixths, still fractional. The second cut, from the row for x one, is x one plus x two at most five. One more pivot, and the relaxation stops at five, zero, worth five. Whole.

@art second-cut
Two cuts, two pivots, and a whole corner attaining the relaxation's value. That's the certificate: it's optimal for the integer problem. No search tree was needed on this instance.

@chapter A counterexample
@art bad-cut
Now try x one plus x two at most four. It also removes the corner. But it isn't a cut. It removes three, two, four, one and five, zero too, every optimal whole plan. The new region's best is four, and nothing afterwards would reveal the answer had changed.

@words text="Valid = keeps every whole point" sub="cutting off the corner is a separate question"
Validity is a claim about all sixteen whole points in the region, not about the one corner you dislike. Check them.

@chapter Cuts and trees together
@art cut-and-branch
Each round of cuts strengthens the bound, and a better bound closes nodes. So cuts and the search tree are used together. But there's no promise about how many rounds you need. In practice a solver adds a few, branches, and adds more inside the tree.

@chapter Where people slip
@list heading="Common slips" items="Any inequality that cuts the corner is a cut@The first|Reading the floor as rounding@The second|Re-solving from scratch@And the third"
The first slip is believing any inequality that cuts off the corner is a cut. The second is reading the floor as rounding. The floor of minus seven halves is minus four, not minus three. And the third is re-solving from scratch, when one dual simplex pivot will do.

@chapter Try it
@words text="Check 6x₁ + 6x₂ ≤ 31" sub="at (3, 2), (4, 1), (5, 0)"
Your turn. Test the first cut at the three optimal plans, three, two, four, one, and five, zero. Each should pass. Then test it at twenty five sixths, one, and see that it holds there too, which is why a second cut was needed.

@end text="Derive a cut and test it"
You can derive each cut from its row and test it against every whole point, on Learn. That's learn dot get er done dot I O.
