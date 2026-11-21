---
format: long
lesson: induction-and-recursion/recurrence-relations
title: Recurrence relations: how to set one up
thumb: Split by the last piece
---

@chapter Defined by earlier terms
@title text="Recurrence Relations" sub="Induction and Recursion" art=thumb
Some sequences are easiest to describe by how each term comes from the ones before. That's a recurrence relation. Setting one up is modelling. Solving it means finding a formula that doesn't mention earlier terms.

@words text="order = how far back it reaches" sub="order k needs k initial conditions"
A recurrence gives a n in terms of earlier terms. Its order is how far back it reaches. And initial conditions supply the first terms outright. A recurrence of order k needs k of them, and then every term is determined.

@math heading="Linear homogeneous" items="aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ⋯ + cₖaₙ₋ₖ@constant coefficients;;linear:  terms to the first power, never multiplied@first power;;homogeneous:  no term without an a in it@no term"
The most important kind is linear homogeneous with constant coefficients: a n is a fixed combination of the previous k terms. Linear means the terms appear to the first power and aren't multiplied together. Homogeneous means there's no term without an a in it.

@chapter Three models
@art compound-growth
Compound interest is the simplest. A balance growing at rate r per period gives a n equals one plus r, times a n minus one, starting from the deposit a nought. First order, linear, homogeneous, and its solution, a nought times one plus r to the n, is immediate.

@art hanoi-move
The Tower of Hanoi gives H n equals two H n minus one, plus one, with H one equal to one. That plus one is the single move of the largest disc. It makes the recurrence nonhomogeneous, and it's why the answer is two to the n minus one, not a power of two.

@art rabbits
And Fibonacci, F n equals F n minus one plus F n minus two, is second order, linear and homogeneous. It counts much more than rabbits.

@chapter Strings with no two 1s in a row
@art bead-rows
Let a n be the number of binary strings of length n with no two ones in a row. Split them by the last character.

@math items="ends in 0:  any valid string of length n−1  →  aₙ₋₁@ends in zero;;ends in 1:  must be …01, valid string of length n−2  →  aₙ₋₂@ends in one;;aₙ = aₙ₋₁ + aₙ₋₂@So a n"
If it ends in zero, the first n minus one characters can be any valid string. If it ends in one, the character before must be zero, and the first n minus two can be any valid string. So a n equals a n minus one plus a n minus two.

@math heading="Initial conditions" items="n = 1:  0, 1   →  a₁ = 2@length one;;n = 2:  00, 01, 10   →  a₂ = 3@length two;;2, 3, 5, 8, 13, 21, 34, …  = Fₙ₊₂@two, three, five"
For length one, there are two strings. For length two, there are three, because one followed by one is excluded. That gives two, three, five, eight, thirteen, twenty one, thirty four. It's Fibonacci shifted along by two: same recurrence, different initial conditions.

@art split-by-last
That's the model for every counting recurrence. Split the objects by their last piece, so each part is a smaller copy of the same problem. The split must be exhaustive and must not overlap. Getting that right is the whole task.

@chapter Unrolling
@math heading="Hₙ = 2Hₙ₋₁ + 1" items="= 4Hₙ₋₂ + 2 + 1@four H;;= 8Hₙ₋₃ + 4 + 2 + 1@eight H;;= 2ⁿ⁻¹H₁ + (2ⁿ⁻² + ⋯ + 2 + 1)@all the way;;= 2ⁿ⁻¹ + 2ⁿ⁻¹ − 1 = 2ⁿ − 1@minus one"
Before any technique, you can often solve a recurrence by unrolling it. Substitute once and you get four H n minus two, plus two plus one. Again: eight H n minus three, plus four plus two plus one. Go all the way down to H one, sum the geometric series, and you get two to the n, minus one.

@art unrolled-strip
But unrolling only produces a conjecture. You still have to prove the guess by induction. And unrolling gets unmanageable for higher orders, which is why the next lesson exists.

@chapter Where people slip
@list heading="Common slips" items="Overlapping cases in the split@Overlapping|Wrong number of initial conditions@initial conditions|Treating an unrolled pattern as proved@unrolled pattern"
Three slips. Overlapping cases in the split, which count some objects twice. The wrong number of initial conditions: fewer than the order leaves the sequence undetermined. And treating an unrolled pattern as proved, when it's only a guess until induction confirms it.

@chapter Try it
@words text="strings over {0, 1, 2} with an even number of 0s" sub="aₙ = 2aₙ₋₁ + (3ⁿ⁻¹ − aₙ₋₁) = aₙ₋₁ + 3ⁿ⁻¹,  a₁ = 2"
To practise, take strings of length n over zero, one and two with an even number of zeros. A valid string is a valid one plus a one or a two, or an invalid one plus a zero. That gives a n equals a n minus one plus three to the n minus one. Check it on the length two strings.

@end text="Set up, unroll, compare"
You can unroll each recurrence beside its closed form on Learn. That's learn dot get er done dot I O.
