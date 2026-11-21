---
format: long
lesson: sequences-and-series/sequences-and-recursion
title: Sequences and recursion: a formula, or a start and a rule
thumb: A rule needs a start
---

@chapter What a sequence is
@title text="Sequences and Recursion" sub="Sequences and Series" art=thumb
A sequence is a list of numbers in order. There are two ways to hand someone that list, and they answer different questions.

@art dot-row
Formally, a sequence is a function whose inputs are the positive integers: one, two, three, and so on, or just the first few of them. Its outputs are the terms. Plot one and you get a row of separate dots, not a curve.

@math heading="Terms" items="a₁, a₂, a₃, …@a one, a two;;aₙ  the n-th term@a n is"
We write the terms a one, a two, a three, and so on. And a n is the n-th term, also called the general term.

@art position-slots
That small number is an index. It names a position. It isn't a multiplication, and it isn't a value. In ten, twenty, thirty, the third term, a three, is thirty, not three.

@words text="1, 2, 3  ≠  3, 2, 1" sub="order matters · repeats are allowed"
A sequence isn't a set, either. Order is part of it, so one, two, three and three, two, one are different sequences. And repeats are fine: one, zero, one, zero goes on for ever with only two values.

@chapter The explicit way
@math heading="Explicit formulas" items="aₙ = 3n − 1:   2, 5, 8, 11, …@three n minus one;;bₙ = (−1)ⁿ:   −1, 1, −1, 1, …@minus one to the n;;cₙ = 1/n:   1, 1/2, 1/3, …@one over n"
The first way is an explicit formula: hand it n, and it hands back the term. Three n minus one gives two, five, eight, eleven. Minus one to the n flips between minus one and one, which is how you make an alternating sign. And one over n gives one, a half, a third, shrinking toward zero but never reaching it.

@chapter The recursive way
@art doubling-bars
The second way is recursive. You give one or more starting terms, and a rule that builds each later term from earlier ones. Start at five and keep doubling.

@math heading="The same sequence, both ways" items="a₁ = 5,   aₙ = 2aₙ₋₁  for n ≥ 2@a one equals five;;aₙ = 5 · 2ⁿ⁻¹@five times two;;5, 10, 20, 40, 80, …@five, ten, twenty"
Recursively, a one equals five, and a n equals two times a n minus one, for n at least two. Explicitly, a n equals five times two to the n minus one, because that's doubling n minus one times from five. Both give five, ten, twenty, forty, eighty.

@words text="a₃₀: one line, or 29 steps" sub="explicit jumps · recursive walks"
Why have both? The explicit formula gives you the thirtieth term in one line. The recursion makes you walk through the twenty-nine terms before it. Situations often hand you the recursion; the explicit form is the one you want.

@chapter Where to start
@art many-starts
The rule a n equals two times a n minus one doesn't name a sequence on its own. Five, ten, twenty fits it. So does three, six, twelve. So does zero, zero, zero.

@words text="initial terms + a recurrence" sub="both parts, or no sequence"
The rule says how to move, not where to start. Leave out the initial term and you haven't left a small gap. You've described infinitely many different sequences.

@chapter Two famous recursions
@art fibonacci-squares
Fibonacci starts with two ones, and each term after that is the sum of the two before it: one, one, two, three, five, eight, thirteen, twenty one. It needs two starting terms, because the rule reaches back two.

@math heading="Factorial" items="0! = 1@zero factorial;;n! = n · (n − 1)!@n factorial is;;1, 1, 2, 6, 24, 120, …@one, one, two, six"
Factorial starts with zero factorial equals one, and n factorial is n times n minus one factorial. That gives one, one, two, six, twenty four, one hundred and twenty.

@chapter A pattern is not a proof
@math heading="a₁ = 3,   aₙ = 2aₙ₋₁ + 1" items="3, 7, 15, 31, 63@three, seven;;guess   aₙ = 2ⁿ⁺¹ − 1@two to the n plus one;;n = 6:   2⁷ − 1 = 127 = 2(63) + 1   ✓@one hundred and twenty seven"
There's no general method for turning a recursion into a formula. You compute, guess, and test. Double and add one, from three: three, seven, fifteen, thirty one, sixty three. Each is one less than a power of two, so guess two to the n plus one, minus one. It predicts a sixth term of one hundred and twenty seven, and the recursion agrees.

@art circle-chords
But testing isn't proving. Mark points on a circle, join every pair with a chord, and count the regions. For one to five points: one, two, four, eight, sixteen. It looks like doubling. With six points, the count is thirty one.

@words text="“agrees with the first six terms”" sub="a candidate, not a fact"
So a formula that matches is a candidate. Proving it for every n takes induction, which this course doesn't cover. Say exactly what you checked: this formula agrees with the first six terms.

@chapter Common slips
@list heading="Common slips" items="Reading a₃ as the number 3@First|Reading aₙ₋₁ as aₙ − 1@Second|Assuming the wrong starting index@Third|Treating a few matches as settled@And fourth"
First, reading a three as the number three. Second, reading a n minus one as a n, take away one. In three, seven, fifteen, thirty one, at n equals four, those are fifteen and thirty. Third, assuming the index starts at zero when it starts at one. Write out a one first. And fourth, treating a pattern in a few terms as settled.

@chapter Try it
@words text="b₁ = 2,   bₙ = 3bₙ₋₁ + 2" sub="first: look at b₁ + 1 and b₂ + 1"
Your turn. Take b one equals two, and b n equals three times b n minus one, plus two. Start by looking at b one plus one and b two plus one, not just the terms. Generate up to b five, propose a formula, predict b six, and check it against the recursion.

@end text="Two definitions, one list"
You can enter both forms of a sequence and check that the two lists agree, term by term, on Learn. That's learn dot get er done dot I O.
