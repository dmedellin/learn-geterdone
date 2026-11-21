---
format: long
lesson: logic-and-proof/predicates-and-quantifiers
title: For all and there exists: predicates and quantifiers
thumb: The domain is part of the claim
---

@chapter The question
@title text="Predicates and Quantifiers" sub="Logic and Proof" art=thumb
x is greater than three. True or false? Neither, yet. It has a free variable, so it has no truth value. There are two ways to turn it into a proposition: plug in a value, or quantify it.

@chapter Predicates and the domain
@words text="P(x) : “x > 3”" sub="a predicate, no truth value yet"
A predicate P of x is a sentence with a free variable. Substitute a value and it becomes a proposition. So P of five has a value, and it's true. Predicates can have several variables too, like Q of x and y.

@art domain-fence
The domain is the set of values the variables range over. And it's part of the statement, not background. Leave it unstated, and you haven't made a claim at all. All integers, all real numbers, all students in this class: say which.

@chapter For all, and there exists
@art all-lit
For all x, P of x, is true when P of c is true for every c in the domain. It's false as soon as one c makes it false.

@art one-lit
There exists x such that P of x, is true when P of c is true for at least one c in the domain. One is enough.

@math heading="The domain changes the answer" items="∀x (x² ≥ x):  T over ℤ@over the integers;;∀x (x² ≥ x):  F over ℝ, x = ½@over the reals;;∃x (x² = 2):  F over ℚ,  T over ℝ@x squared equals two"
Watch the domain at work. For all x, x squared is at least x, is true over the integers. Over the reals it's false: x equals one half refutes it. And there exists x with x squared equals two is false over the rationals, and true over the reals.

@chapter Proving and refuting
@math heading="to prove  ·  to refute" items="∀x P(x):  argument over all x  ·  one counterexample@for all;;∃x P(x):  one witness  ·  argument over all x@For there exists"
Here's the heart of it, an asymmetry. To prove a for all claim over an infinite domain, you need an argument covering every case. To refute it, one counterexample. For there exists it's the reverse. One witness proves it, and refuting it takes a general argument.

@art counterexample-dot
So one element that fails is a complete refutation of a universal claim. Nothing more is needed. And notice that nobody having proved a universal claim says nothing about whether it's true.

@words text="{1, 2, 3}:  ∀ = P(1) ∧ P(2) ∧ P(3)  ·  ∃ = P(1) ∨ P(2) ∨ P(3)"
Over a finite domain, the quantifiers collapse into connectives. With domain one, two, three, for all is P of one and P of two and P of three. There exists is the same with or.

@art empty-fence
That explains the empty domain. An empty and is true, and an empty or is false. So for all over an empty domain is vacuously true, with nothing to fail. And there exists is false.

@words text="∀x P(x, y):  x bound, y free" sub="∃!x P(x): exactly one x"
Two more terms. In for all x, P of x and y, x is bound and y is free. Only when every variable is bound do you have a proposition. And there exists exactly one x makes two claims: something exists, and nothing else does.

@chapter Restrictions
@math heading="Domain ℤ · P = prime, E = even" items="“Every prime > 2 is odd”:  ∀x ((P(x) ∧ x > 2) → ¬E(x))  ✓@every prime greater than two;;∀x (P(x) ∧ x > 2 ∧ ¬E(x))  ✗@all and;;“Some prime is even”:  ∃x (P(x) ∧ E(x))  ✓ x = 2@some prime is even;;∃x (P(x) → E(x))  ✗ x = 9@with an arrow"
Restrictions need care. Every prime greater than two is odd uses for all, with the restriction as the hypothesis of an arrow. Write it with all and, and you claim every integer is an odd prime. Some prime is even uses there exists and and, with x equals two. Write that with an arrow, and x equals nine satisfies it.

@art filter-funnel
Why nine? P of nine implies E of nine is false implies false, which is true. So a number that's neither prime nor even satisfies it. The rule: with for all, a restriction goes before an arrow. With there exists, it's joined with and.

@chapter Where people slip
@list heading="Common slips" items="Leaving the domain implicit@The first|Using ∧ under ∀ for a restriction@The second|Using → under ∃@the third"
The first slip is leaving the domain implicit. The second is using and under for all for a restriction. That claims far too much. And the third is using an arrow under there exists, which is nearly always vacuously true, and almost never what was meant.

@chapter Try it
@words text="“Every positive even integer greater than 2 is composite”" sub="“Some composite number is odd”"
Your turn. Translate every positive even integer greater than two is composite, and some composite number is odd. For each, say why the connective inside had to be what it is.

@end text="Edit a predicate, watch the verdicts"
You can edit a predicate cell by cell and watch every quantifier's verdict change, on Learn. That's learn dot get er done dot I O.
