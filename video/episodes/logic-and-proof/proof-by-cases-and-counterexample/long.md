---
format: long
lesson: logic-and-proof/proof-by-cases-and-counterexample
title: Proof by cases, counterexamples, and why checking is not proving
thumb: Forty checks, still false
---

@chapter The question
@title text="Cases, Counterexamples, and Writing a Proof" sub="Logic and Proof" art=thumb
n squared plus n plus forty one is prime when n is zero. And one, and two, all the way up to thirty nine. So it's always prime, right? This is the lesson the whole course has been building toward: why checking is never proving.

@chapter Proof by cases
@art case-split
To prove a statement by cases, split the possibilities into cases that together are guaranteed to cover everything, and prove the statement in each one separately. The cases must be exhaustive. They may overlap. They may not leave a gap.

@math heading="n² + n is even, for every integer n" items="n even, n = 2k:  n² + n = 4k² + 2k = 2(2k² + k)@Case one;;n odd, n = 2k + 1:  n² + n = 4k² + 6k + 2@Case two;;= 2(2k² + 3k + 1)  ✓@both cases"
Every integer is even or odd, so two cases cover everything. Case one, n is even, n is two k. Then n squared plus n is four k squared plus two k, which is twice an integer. Case two, n is odd. Then n squared plus n is four k squared plus six k plus two, twice an integer again. Even in both cases.

@words text="n² + n = n(n + 1)" sub="consecutive integers: one is even"
A cleaner argument exists. N squared plus n is n times n plus one, a product of consecutive integers, and one of them is even. Finding that is better mathematics. But the case proof is correct, and correctness comes first.

@chapter A worked case proof
@math heading="|x + y| ≤ |x| + |y|" items="Case x + y ≥ 0:  |x + y| = x + y@Case one;;x ≤ |x|,  y ≤ |y|  ⟹  ≤ |x| + |y|@at most"
Here's the triangle inequality, by cases on the sign of x plus y. Case one, x plus y is at least zero. Then it equals its own absolute value. And x and y are each at most their absolute values, so the sum is too.

@math heading="|x + y| ≤ |x| + |y|" items="Case x + y < 0:  |x + y| = (−x) + (−y)@Case two;;−x ≤ |x|,  −y ≤ |y|  ⟹  ≤ |x| + |y|@minus x;;every real is ≥ 0 or < 0  ∎@exhaustive"
Case two, x plus y is negative. Then its absolute value is minus x plus minus y. And minus x and minus y are each at most their absolute values. Every real is one or the other, so the cases are exhaustive.

@art mirror-halves
Those cases look like mirror images, which tempts you to say without loss of generality. That's not legitimate here. The second case genuinely uses minus x at most the absolute value of x. Without loss of generality is only allowed for a genuine symmetry. Otherwise it's hiding a gap.

@chapter One counterexample
@art odd-block
To disprove a for all claim, you need one counterexample, and that's a complete refutation. It's the negation at work: not for all is there exists a failure, and you prove that with one witness.

@words text="7 = 4 + 1 + 1 + 1" sub="needs four squares, not three"
Every positive integer is the sum of at most three squares. False. Seven needs four: four plus one plus one plus one. One number settles it. The corrected claim, at most four squares, is Lagrange's theorem, and it needs a real proof.

@chapter Checking is not proving
@math heading="n² + n + 41" items="prime for n = 0, 1, 2, … , 39@zero to thirty nine;;n = 40:  1681 = 41²  ✗@at forty"
Back to the opening. N squared plus n plus forty one is prime for every n from zero to thirty nine. But at forty, it's one thousand six hundred and eighty one, which is forty one squared.

@art circle-chords
Or put points on a circle and join every pair. With one to five points the circle splits into one, two, four, eight and sixteen regions. Five powers of two in a row. At six points you get thirty one, not thirty two. Evidence that feels conclusive, and isn't.

@chapter What a proof owes its reader
@list heading="A proof owes the reader" items="A precise statement@A precise statement|A declared method@a declared method|Justified steps@justified steps|No gaps disguised as brevity@no gaps|An explicit ending@an explicit ending"
So, the summary of the course. A proof owes its reader a precise statement, a declared method, justified steps, no gaps disguised as brevity, and an explicit ending. Clearly, and it is obvious that, are where errors hide. A proof is meant to convince a careful, sceptical reader.

@chapter Where people slip
@list heading="Common slips" items="Cases with a gap@The first|WLOG without symmetry@The second|Examples in place of a proof@the third"
The first slip is cases with a gap. The second is using without loss of generality where there's no symmetry. And the third is offering many examples in place of a proof. That's not weak evidence. It's not evidence of the right kind at all.

@art gap-bar
That first one is easy to miss. Positive or negative leaves out zero. Greater than or less than leaves out equal. So every time, say why your cases cover everything.

@chapter Try it
@words text="n³ − n = (n − 1) n (n + 1)" sub="cases: n = 3k, 3k + 1, 3k + 2"
Your turn. Prove that for every integer n, n cubed minus n is divisible by three. Write it as n minus one, times n, times n plus one. Split into three cases, and in each, say which factor is the multiple of three.

@end text="Push the checks until they break"
You can push two convincing claims until each one breaks, on Learn. That's learn dot get er done dot I O.
