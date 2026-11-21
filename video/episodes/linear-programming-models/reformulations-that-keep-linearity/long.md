---
format: long
lesson: linear-programming-models/reformulations-that-keep-linearity
title: Absolute values and maxima in a linear programme, and when it breaks
thumb: Which way is it pushed?
---

@chapter The question
@title text="Reformulations That Keep Linearity" sub="Linear Programming Models" art=thumb
Absolute values, the larger of two expressions, prices that change by volume. They all look non linear. With one extra variable each, they become linear. But only if you push the objective the right way.

@art shared-region
All the rewrites here sit on one region: x plus y at most eight, x at most five, y at most six, and two x plus three y at least twelve. What changes between them is the objective.

@chapter A free variable
@math heading="Splitting x" items="x = x⁺ − x⁻@x plus minus x minus;;x⁺ ≥ 0,  x⁻ ≥ 0@both parts"
If x can go negative, carry it as a difference: x equals x plus minus x minus, with both parts at least zero. Replace x by that difference everywhere.

@math heading="3x + 2y" items="minimise:  3 at (−3, 6),  x⁻ = 3@Minimise three x;;maximise:  21 at (5, 3),  x⁻ = 0@maximised"
Minimise three x plus two y and the answer is three, at minus three, six. The second part carries the negative value, x minus is three. Maximised, it's twenty one at five, three. Both agree with the original. This is the one rewrite that works whichever way you push.

@chapter An absolute value
@math heading="|x| as a sum" items="|x| = x⁺ + x⁻@the sum;;only if one of them is 0@one of them is zero"
For the absolute value of x, use the sum of the same two parts. But that sum is the absolute value only when one of them is zero. Otherwise both could be inflated together without changing x.

@art inflate-pair
Minimising pushes one of them to zero. Maximising does the opposite: it pumps both up together.

@math heading="2|x| + 5y" items="minimise:  original 40/3,  rewrite 40/3@forty over three;;maximise:  original 36 at (−3, 6)@thirty six;;maximise:  rewrite unbounded@unbounded"
Minimise two times the absolute value of x, plus five y. The original by corners is forty over three at five, two thirds. The rewrite gets forty over three too. Now maximise. The original is thirty six at minus three, six. But the rewrite is unbounded. If you only ran the rewrite, you'd never notice.

@chapter The largest piece
@math heading="Epigraph" items="minimise max(p₁, p₂, …)@the largest;;minimise t,  t ≥ pᵢ for each i@add a variable t"
To minimise the largest of several linear pieces, add a variable t. Add one row per piece saying t is at least that piece, and minimise t. The rows make t at least the maximum, and minimising squeezes it down onto it.

@art epigraph
Maximise instead and nothing stops t climbing. The rewritten programme is unbounded. That's a different problem, not a worse answer to this one.

@math heading="max(2x + y, −x + 5y)" items="optimum 132/17@one hundred and thirty two;;x = 48/17,  y = 36/17@forty eight"
Minimise the larger of two x plus y and minus x plus five y. Both routes give one hundred and thirty two seventeenths, at x equals forty eight seventeenths, y equals thirty six seventeenths. There t sits exactly where the two pieces cross.

@chapter Price bands
@art price-bands
Suppose the first three units cost two each, and every unit after costs five. Use one variable per band, cap the first at three, and price them separately. A minimiser fills the cheaper band first. That only works if later bands cost more. That condition is convexity.

@math heading="Falling price: 5 then 2" items="true cheapest:  16 at (0, 4)@sixteen;;band model:  38/3@thirty eight;;x(1) = 0,  x(2) = 5@five units"
Now flip the prices: five for the first three, two after. The true cheapest cost is sixteen, at zero, four. The band model reports thirty eight thirds. It bought five units from the second band without filling the first, which the schedule doesn't allow.

@art empty-first-band
A better looking answer is not good news. It means part of the question has been dropped.

@chapter Where people slip
@list heading="Common slips" items="Assuming it works either way@The first|Trusting a better objective@The second|Leaving convexity unstated@The third"
The first slip is assuming a rewrite works in either direction. Three of these four don't. The second is treating a better objective as good news. The third is leaving the convexity condition unstated in a price band model. A volume discount fails it.

@chapter The check
@art two-methods
The lab does exactly that. It optimises the original by enumerating corners, piece by piece, and it solves the rewrite with the simplex engine. The two methods never look at each other, and that's why agreement between them means something.

@words text="original by corners − rewrite by simplex = 0"
Every auxiliary variable comes with a sentence: what forces it to the value I intend. And that's checkable. Solve the original another way, solve the rewrite, and subtract. A test that can fail is worth running.

@end text="Solve both, then subtract"
You can solve each original and its rewrite side by side, and see the difference, on Learn. That's learn dot get er done dot I O.
