---
format: long
lesson: logic-and-proof/negating-quantified-statements
title: Negating for all and there exists: every quantifier flips
thumb: Not all means some fail
---

@chapter The question
@title text="Negating Quantified Statements" sub="Logic and Proof" art=thumb
You suspect a claim is false. What exactly would you have to find to show it? There's a mechanical answer. Negate the claim, push the negation inward, and read off the shape of the counterexample.

@chapter The two rules
@math heading="Quantifier negation" items="¬∀x P(x)  ≡  ∃x ¬P(x)@not for all;;¬∃x P(x)  ≡  ∀x ¬P(x)@not there exists"
There are two rules, and they hold over any domain. Not for all x, P of x, is the same as there exists x with not P of x. And not there exists x, P of x, is the same as for all x, not P of x.

@art one-dark-lamp
The first one says: if P doesn't hold throughout the domain, then some element fails it. Not all means some fail. And if some element fails, the for all can't hold.

@art none-dark
The second says: if nothing satisfies P, then every element fails it. None means all fail. Keep the two apart. Some fail and all fail are very different claims, and only the first is the negation of all.

@words text="¬(P(a₁) ∧ … ∧ P(aₙ))  ≡  ¬P(a₁) ∨ … ∨ ¬P(aₙ)" sub="De Morgan, freed from finiteness"
Over a finite domain this is literally De Morgan. Not of a long and is a long or of nots. The quantifier rules are the same statement, freed from finiteness.

@chapter One quantifier at a time
@math heading="Push the negation in" items="¬ ∀x ∃y ∀z  P(x, y, z)@not for all x;;≡ ∃x ¬ ∃y ∀z  P(x, y, z)@first flip;;≡ ∃x ∀y ¬ ∀z  P(x, y, z)@second flip;;≡ ∃x ∀y ∃z ¬P(x, y, z)@third flip"
With several quantifiers, work from the outside in. Start with not for all x, there exists y, for all z. The first flip makes it there exists x, not there exists y. The second flip gives for all y, not for all z. And the third flip lands the negation on the predicate.

@art flip-cascade
Each step moves the negation one quantifier to the right, and flips that quantifier. Every quantifier it passes must flip. Once it reaches the predicate, the ordinary propositional rules take over. If the predicate is a conditional, not of A implies B is A and not B.

@chapter A counterexample writes itself
@math heading="“Every prime greater than 2 is odd”" items="∀x ((P(x) ∧ x > 2) → Odd(x))@for all x;;negation:  ∃x (P(x) ∧ x > 2 ∧ ¬Odd(x))@its negation"
Take every prime greater than two is odd. In symbols: for all x, if x is prime and greater than two, then x is odd. Its negation: there exists x that's prime, greater than two, and not odd.

@art odd-one-out
That says there is an even prime greater than two. That's exactly the counterexample you'd have to produce, and its shape came out of the mechanism, not out of thinking about primes. Very often the negation is easy to read, and the counterexample writes itself.

@chapter Negating continuity
@math heading="f continuous at a, negated" items="¬ ∀ε ∃δ ∀x ( |x−a| < δ → |f(x)−f(a)| < ε )@not for all epsilon;;≡ ∃ε ∀δ ∃x ¬( |x−a| < δ → |f(x)−f(a)| < ε )@flip all three;;≡ ∃ε ∀δ ∃x ( |x−a| < δ ∧ |f(x)−f(a)| ≥ ε )@the arrow becomes"
Here's a harder one, the definition of continuity at a point. Start with not for all epsilon, there exists delta, for all x. Flip all three quantifiers, one at a time. Then the arrow becomes and, and less than epsilon becomes at least epsilon.

@art jump-curve
Read it back. There's a tolerance epsilon so that, however small you make delta, some point within delta of a is thrown at least epsilon away. That's exactly what a discontinuity looks like, and no picture was needed to find it.

@art zero-or-two
One more check on the mechanism. Not exactly one x says that either nothing satisfies P, or at least two things do. Unfold exactly one and negate it, and that disjunction is what comes out.

@chapter Where people slip
@list heading="Common slips" items="Negating “all are” as “none are”@The first|Keeping the arrow after negating@The second|Flipping only the first quantifier@the third"
The first slip is negating all are as none are. Not all is some fail. None is all fail, a far stronger claim. The second is keeping the arrow. Not of P implies Q is P and not Q. And the third is flipping only the first quantifier and stopping there.

@chapter Try it
@words text="∀ε ∃N ∀n (n ≥ N → |aₙ − L| < ε)" sub="negate it, then read it in English"
Your turn. This is the definition of a convergent sequence. Negate it step by step, flipping each quantifier in turn, then turn the arrow into and. Read the answer back in English. If the mechanism carries you through this, it'll carry you through any definition you meet later.

@end text="Predict, then press Complement"
You can flip a predicate to its negation and watch all six verdicts change, on Learn. That's learn dot get er done dot I O.
