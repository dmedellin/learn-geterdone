---
format: long
lesson: exponential-and-logarithmic-functions/the-number-e
title: The number e: what happens when you compound forever
thumb: More often, but never past e
---

@chapter A dollar at a hundred percent
@title text="The Number e" sub="Exponential and Logarithmic Functions" art=thumb
Pay a hundred percent interest once a year, and a dollar becomes two. Pay it in smaller pieces, more often, and the total climbs, but not without limit. It settles toward one irrational number, two point seven one eight two eight, and so on. That number is e.

@art dollar-split
Paid once, at the end, you have two. Paid as fifty percent twice, the second payment earns interest on the first. The pattern is n payments of one over n, and the total is one plus one over n, all to the power n.

@math heading="(1 + 1/n)ⁿ" items="n = 1:   (2/1)¹ = 2@Once;;n = 2:   (3/2)² = 9/4 = 2.25@Twice;;n = 4:   (5/4)⁴ = 625/256 = 2.44140625@Four times"
Once gives two. Twice gives three halves squared, nine quarters, two point two five. Four times gives five quarters to the fourth, which is six hundred and twenty five over two hundred and fifty six, exactly two point four four one four zero six two five.

@math heading="More and more often" items="n = 12:   ≈ 2.613035@Monthly;;n = 365:   ≈ 2.714567@daily;;n = 1000:   ≈ 2.716924@a thousand times;;e ≈ 2.718282@And e"
Monthly gives about two point six one three. Then daily, about two point seven one four six. Then a thousand times a year, about two point seven one six nine. And e is about two point seven one eight three.

@chapter A ceiling
@art climbing-steps
The totals rise, and the rises get smaller. Going from once a year to twice adds a quarter. Going from daily to a thousand times a year adds only about point zero zero two four. Compounding more often is worth less and less, and there's a ceiling.

@words text="e ≈ 2.718281828459045" sub="the limit of (1 + 1/n)ⁿ as n grows without bound"
e is the number that one plus one over n, to the n, approaches as n grows without bound. It's irrational, so its decimals never end or repeat. Every printed value of e is a rounding.

@words text="Increasing, and never above 3" sub="so the limit exists"
Why is there a limit? The sequence is increasing, and no term of it exceeds three. An increasing sequence with a ceiling has a limit. Both facts are proved in analysis, not by a table, which only shows finitely many terms.

@chapter Two readings, both wrong
@art two-wrong-readings
One plus one over n tends to one, and one to any power is one. Or: n copies of one over n add up to one, which suggests two. At n equals three hundred and sixty five, those say one and two, while the true value is about two point seven one four six.

@words text="Freeze one part, move the other" sub="two answers from one expression: the move isn't legal"
Each argument freezes one part of the expression while moving the other, and they disagree. Two answers from one expression means the method is broken, not that the answer is ambiguous.

@chapter The function e to the x
@art e-curve-between
e to the x is just an exponential with base e. Since e is between two point seven one eight and two point seven one nine, its curve sits between two to the x and three to the x, and behaves exactly like them. Increasing, positive, asymptote y equals zero, and every exponent law still holds.

@math heading="f(x) = eˣ" items="f(0) = 1@f of zero;;f(1) = e ≈ 2.718282@f of one;;f(2) = e² ≈ 7.389056@f of two;;f(−1) = 1/e ≈ 0.367879@minus one"
f of zero is one. f of one is e. f of two is e squared, about seven point three eight nine. And f of minus one is one over e, about point three six eight. Those decimals are rounded, so carry the exact forms.

@chapter The same money, two ways
@math heading="$1000 at 5% for 10 years" items="yearly:   1000·(21/20)¹⁰ ≈ 1628.89@once a year;;continuously:   1000·e^(1/2) ≈ 1648.72@continuously;;gap ≈ 19.83@The gap"
Take a thousand dollars at five percent for ten years. Compounded once a year, that's a thousand times twenty one twentieths to the tenth, about sixteen hundred and twenty eight dollars, eighty nine. Compounded continuously, it's a thousand times e to the one half, about sixteen hundred and forty eight, seventy two. The gap is about nineteen dollars, eighty three.

@art compounding-gap
That gap is everything continuous compounding buys over yearly compounding at this rate. At this rate, it's under twenty dollars on a thousand.

@chapter Where people slip
@art rounding-drift
The first slip is writing e as two point seven one eight. Raise that to the tenth and you get about twenty two thousand and three point six, against a true value of about twenty two thousand and twenty six point five. Round at the end of a calculation, not at the start.

@list heading="Two more slips" items="Arguing the limit is 1@arguing the limit is one|Treating a term as the value@treating a term"
The second is arguing the limit is one because the base tends to one. The exponent is growing at the same time. The third is treating a term of the sequence as the value. Even with n at a million, the term is a rational number, and e isn't.

@chapter Try it
@words text="(1 + 1/10)¹⁰ = (11/10)¹⁰" sub="place it between the quarterly value and e"
Your turn. Split a dollar at a hundred percent into ten periods. The total is eleven tenths, to the tenth. Work it out, place it between the quarterly value and e, and say why neither its decimal nor its exact fraction equals e. Check with inequalities, not matching digits.

@end text="Computed, not quoted"
You can watch the exact fractions climb toward e, beside the two wrong readings, on Learn. That's learn dot get er done dot I O.
