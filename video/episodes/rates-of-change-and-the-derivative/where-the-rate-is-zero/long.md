---
format: long
lesson: rates-of-change-and-the-derivative/where-the-rate-is-zero
title: Where the rate is zero: maximum, minimum, or neither
thumb: A turn needs a sign change
---

@chapter The question
@title text="Where the Rate Is Zero" sub="Rates of Change and the Derivative" art=thumb
Where does a graph turn around? At the top of a hill or the bottom of a valley, the tangent is level, so the derivative is zero. But is every zero of the derivative a turn? Not quite.

@art no-jump
Here's why turns happen at zeros. Just before a turn the graph is rising, so p prime is positive. Just after, it's falling, so p prime is negative. And a polynomial can't jump from positive to negative without passing through zero.

@words text="p′ = 0 is necessary, not sufficient"
So every turn sits at a zero of p prime. That's necessary. But it isn't enough. The graph turns only where p prime changes sign.

@chapter The method
@list heading="Where p′(c) = 0" items="+ then −:  a local maximum@positive to negative|− then +:  a local minimum@negative to positive|the same sign on both sides:  neither@the same sign"
A critical point is a place where p prime is zero. If p prime changes from positive to negative there, it's a local maximum. If it changes from negative to positive, a local minimum. And if it has the same sign on both sides, it's neither.

@art turn-test
Picture it as arrows. Up, then down, is a hilltop. Down, then up, is a valley. Up, then up again, is just a flat step on the way.

@chapter A cubic with two turns
@math heading="p(t) = 2t³ − 3t² − 12t + 1" items="p′(t) = 6t² − 6t − 12@six t squared;;= 6(t² − t − 2) = 6(t − 2)(t + 1)@Take out the six;;critical points:  t = −1,  t = 2@the critical points"
Take two t cubed, minus three t squared, minus twelve t, plus one. Its derivative is six t squared minus six t minus twelve. Take out the six, factor, and you get six times t minus two, times t plus one. So the critical points are minus one and two.

@math heading="Test each region" items="t = −2:  6·(−4)·(−1) = 24    rising@At minus two;;t = 0:  6·(−2)·1 = −12    falling@At zero;;t = 3:  6·1·4 = 24    rising@at three"
Test one place in each region. At minus two, p prime is twenty four, so it's rising. At zero, it's minus twelve, falling. And at three, it's twenty four again.

@art hump-and-valley
So at minus one the graph stops rising and starts falling: a local maximum. At two it stops falling and starts rising: a local minimum. The lab's interval tile shows the same three regions, and its zero tile the same two places. Nothing here came from plotting a point.

@math heading="The heights come from p" items="p(−1) = −2 − 3 + 12 + 1 = 8@P of minus one;;p(2) = 16 − 12 − 24 + 1 = −19@P of two"
The heights come from p itself, not from p prime, which is zero at both. P of minus one is eight. P of two is minus nineteen.

@chapter Local means local
@art local-not-global
The word local matters. The maximum height is eight, but further right the graph rises without limit. P of four is already thirty three. Eight is the highest point near minus one, and nothing more. A cubic climbs for ever, so any maximum it has gets overtaken further along.

@chapter A zero where nothing turns
@art flat-step
Now take t cubed. Its derivative is three t squared, which is zero at zero and positive everywhere else, because a square is never negative. So the graph rises before zero and rises after it. It's level for an instant, and it doesn't turn. The lab marks that zero as having no sign change.

@art never-level
And t cubed plus t has derivative three t squared plus one, which is at least one, so it's never zero. No level tangent, and no turn. It rises everywhere. The lab's zero tile says none rational, and its interval tile says rising, for every t.

@chapter Where people slip
@list heading="Common slips" items="Calling every zero of p′ a turn@The first|Reading the height from p′@The second|Taking a local maximum for the largest value@the third"
The first slip is calling every zero of p prime a maximum or a minimum. T cubed shows why not. The second is reading the height from p prime. Its zero says where to look, and p says how high. And the third is taking a local maximum for the largest value. Over an interval, compare the turns with the ends.

@chapter Try it
@words text="p(t) = t³ − 3t" sub="p′(t) = 3t² − 3 = 3(t − 1)(t + 1)"
Your turn. Take t cubed minus three t. Its derivative is three t squared minus three, which is three times t minus one, times t plus one. Work out the signs, then say which of minus one and one is the maximum.

@end text="Solve, then test the sign"
You can find every critical point of a polynomial, and see which ones really turn, on Learn. That's learn dot get er done dot I O.
