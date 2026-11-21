---
format: long
lesson: rates-of-change-and-the-derivative/what-the-quotients-approach
title: What the quotients approach: the rate at a single place
thumb: Approach is not reach
---

@chapter The question
@title text="What the Quotients Approach" sub="Rates of Change and the Derivative" art=thumb
A curve has no single rate over a step. Change the step, and the rate changes. So is there a rate at a single place? Start by halving the step, again and again, and watching what the quotients do.

@math heading="f(t) = t²,  a = 1" items="h = 1:  3@A step of one;;h = 1/2:  5/2@five halves;;h = 1/4:  9/4@nine quarters;;h = 1/8:  17/8@seventeen eighths;;h = 1/64:  129/64@one hundred and twenty nine"
Take t squared at one. A step of one gives three. Then five halves, nine quarters, seventeen eighths, and on down. After six halvings the step is one sixty fourth, and the quotient is one hundred and twenty nine sixty fourths. That's two point zero one five six two five, exactly.

@art secants-to-tangent
Every one of those is the slope of a secant through the same point. As the step shrinks, the second point slides toward the first, and the slopes settle down.

@chapter The gap
@list heading="Gap to 2" items="1@one, a half|1/2@a half|1/4@a quarter|1/8@an eighth|1/64@one sixty fourth"
Subtract two from each row. The gaps are one, a half, a quarter, an eighth, all the way down to one sixty fourth.

@art gap-shrinking
The gap column is the step column, exactly. That's because the quotient is two plus h, as the algebra of the last lesson found. Subtract two, and what's left is h.

@chapter What approach means
@art bound-band
So here's the claim. The quotients approach two as h goes to zero. That means: name any positive bound, however tiny, and there's a step below which every quotient is within that bound of two.

@art never-reaches
Approach doesn't mean reach. No row equals two. The next row would be two hundred and fifty seven over one hundred and twenty eight, and there's always one more row, with a gap. The claim is about every step, not the seven that happen to be printed.

@words text="f′(a)" sub="the rate at the place"
When the quotients at a place approach one number like this, that number is the rate of the function there. The lab labels it f prime of a, and the next lesson takes it as the definition of the derivative.

@chapter Evidence and proof
@art halving-steps
A table can only ever show a few rows. However many halvings you print, there are endlessly many steps you haven't. So a table is evidence, and the claim needs something more.

@math heading="Proof, for t² at 1" items="quotient = 2 + h@two plus h;;gap = |h|@the gap;;|h| < any bound, once h is@less than any bound"
For t squared, that something is the algebra. The quotient is two plus h for every nonzero h, so the gap is h, in absolute value. And that's less than any bound, once h is. The table illustrates it. The algebra establishes it. For a function whose quotient doesn't simplify, the table stays evidence, and a lesson that relies on it should say so.

@chapter Two more places
@math heading="f(t) = t³,  a = 1" items="quotient = 3 + 3h + h²@three plus three h;;h = 1:  7@At a step of one;;h = 1/64:  12481/4096@at one sixty fourth;;gap:  193/4096@The gap"
For t cubed at one, the quotient is three plus three h plus h squared. At a step of one it's seven, and at one sixty fourth it's twelve thousand four hundred and eighty one, over four thousand and ninety six. The gap to three is one hundred and ninety three, over four thousand and ninety six. The column heads for three.

@art flat-bottom
Now t squared at zero. The quotient is just h, so the column is one, a half, a quarter, and it heads for zero. The rate at zero is zero, and that's what the graph shows: the bottom of the bowl, neither rising nor falling.

@chapter Where people slip
@list heading="Common slips" items="Taking the last row as the limit@The first|Reading a few rows as a proof@The second|Expecting the gap to halve every time@the third"
The first slip is taking the last row as the limit, or thinking it's reached at some step. The second is reading a pattern in a few rows as a proof. And the third is expecting the gap to halve every time. For t cubed, it falls to a little less than half at each step.

@chapter Try it
@words text="f(t) = t²,  a = 2" sub="quotient: 4 + h"
Your turn. Take t squared at two, where the quotient is four plus h. Before you look at the lab, write down the gaps to four for each halving of the step. Then check them.

@end text="Halve the step, watch the gap"
You can halve the step yourself and watch the gap close in, on Learn. That's learn dot get er done dot I O.
