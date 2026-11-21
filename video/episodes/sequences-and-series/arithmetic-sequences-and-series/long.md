---
format: long
lesson: sequences-and-series/arithmetic-sequences-and-series
title: Arithmetic sequences and series: one step, and the pairing trick
thumb: Pair the first with the last
---

@chapter The same step
@title text="Arithmetic Sequences and Series" sub="Sequences and Series" art=thumb
Some sequences move by the same amount every time. Three, seven, eleven, fifteen. That one fact gives you any term you want, and a neat trick gives you the sum without adding anything up.

@art equal-steps
A sequence is arithmetic when the difference between consecutive terms is the same all the way through. That number is the common difference, d. Recursively, each term is the one before plus d.

@math heading="Common differences" items="3, 7, 11, 15, …   d = 4@equal to four;;20, 17, 14, 11, …   d = −3@minus three;;5, 5, 5, 5, …   d = 0@five, five, five"
Three, seven, eleven, fifteen has d equal to four. Twenty, seventeen, fourteen, eleven has d equal to minus three, and a negative difference changes nothing. Five, five, five has d equal to zero, and it's arithmetic too.

@words text="2, 4, 8, 16    1, 4, 9, 16" sub="orderly, but neither is arithmetic"
One difference isn't a check. Two, four, eight, sixteen starts with a difference of two and never repeats it. One, four, nine, sixteen has differences three, five, seven. Check at least three.

@chapter The n-th term
@art step-count
To get from the first term to the n-th, you add d once for every step between them. Getting to a two takes one step. Getting to a ten takes nine. The number of steps is one less than the position.

@math heading="The n-th term" items="aₙ = a₁ + (n − 1)d@a n equals;;d = (aₙ − a₁) / (n − 1)@rearranged"
So a n equals a one plus n minus one times d. Rearranged, d is a n minus a one, over n minus one, which recovers the difference from the first term and any other.

@art dots-on-line
Plot the terms and they sit on a straight line whose slope is d. It's y equals m x plus c with the letters renamed, sampled at the whole numbers. That's why a constant difference is called linear.

@math heading="5, 9, 13, 17, …" items="d = 4,   a₁ = 5@d is four;;a₂₀ = 5 + 4(19) = 81@nineteen steps"
Take five, nine, thirteen, seventeen. The differences are all four, so d is four and a one is five. The twentieth term is five plus four times nineteen, which is eighty one. Nineteen steps, not twenty.

@chapter Adding them up
@art pairing-columns
A series is the sum of the terms, and S n is the sum of the first n. Write the sum forwards, then again backwards underneath, and add column by column. Every column gives the same total, because each step up in one line is matched by a step down in the other.

@math heading="The sum" items="2Sₙ = n(a₁ + aₙ)@two S n;;Sₙ = n(a₁ + aₙ) / 2@divide by two;;Sₙ = (n/2)[2a₁ + (n − 1)d]@the other form"
There are n columns, each totalling a one plus a n, so two S n equals n times a one plus a n. Divide by two. If you only know a one and d, substitute for a n to get the other form: n over two, times two a one plus n minus one times d.

@chapter Gauss and the odd numbers
@art gauss-pairs
The story is that Gauss, at school, added one to a hundred by pairing one with a hundred, two with ninety nine, and so on. Fifty pairs, each making a hundred and one. That's five thousand and fifty.

@art odd-squares
Or take the odd numbers, one, three, five, seven. Here a one is one and d is two, so the n-th odd number is two n minus one, and the sum of the first n is n squared. One, four, nine, sixteen, twenty five.

@chapter Twenty terms, summed
@math heading="S₂₀ of 5, 9, 13, …" items="S₂₀ = 20(5 + 81) / 2 = 860@twenty times;;= (20/2)[2(5) + 19(4)] = 860@ten times;;check:  20 × 43 = 860  ✓@forty three"
Back to five, nine, thirteen. The sum of twenty terms is twenty times five plus eighty one, over two: eight hundred and sixty. The other form, ten times ten plus seventy six, agrees. And the sum is n times the average of the first and last terms. That average is forty three, and twenty times forty three is eight hundred and sixty.

@chapter Common slips
@list heading="Common slips" items="a₁ + nd instead of a₁ + (n − 1)d@First|Trusting one difference@Second|Mixing up aₙ and Sₙ@Third"
First, writing a one plus n d. It gives the next term, wrong by exactly d. Put n equals one into your formula: it must give a one. Second, calling a sequence arithmetic from one difference. Third, mixing up the term and the sum. Here they're eighty one and eight hundred and sixty.

@chapter Try it
@words text="18, 13, 8, 3, …" sub="d = −5 ·  find a₁₅ and S₁₅"
Your turn. Take eighteen, thirteen, eight, three. The differences are all minus five. Find the fifteenth term and the sum of the first fifteen, keeping that minus sign in every step. Then check the sum is fifteen times the average of the first and fifteenth terms.

@end text="Terms, and the running total"
You can set a first term and a difference and watch the running total build, on Learn. That's learn dot get er done dot I O.
