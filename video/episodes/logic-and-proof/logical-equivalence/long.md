---
format: long
lesson: logic-and-proof/logical-equivalence
title: Logical equivalence: De Morgan, distribution and proving formulas equal
thumb: Same value, every row
---

@chapter The question
@title text="Logical Equivalence" sub="Logic and Proof" art=thumb
p implies q, and not p or q. They look nothing alike. They don't even use the same connectives. And yet they say exactly the same thing. So what does it mean for two formulas to be the same, and how do you prove it?

@chapter The definition
@art two-routes
Two formulas A and B are logically equivalent when they have the same truth value under every assignment. Not similar structure, not the same variables. The same value, in every row. Equivalently, A if and only if B is a tautology.

@words text="A ≡ B  is a claim · A ↔ B is a formula" sub="≡ is not a connective"
We write that with a triple bar. But the triple bar isn't a connective. A equivalent to B is a statement about two formulas, made in ordinary maths. A if and only if B is itself a formula. So something like p equivalent to q, and r, is a category error.

@art split-row
And here's the useful flip side. To disprove an equivalence, you show one assignment where the two differ. One row is a complete disproof. It needs no further argument.

@chapter The laws worth knowing
@math heading="Named laws" items="¬¬p ≡ p@double negation;;¬(p ∧ q) ≡ ¬p ∨ ¬q@De Morgan;;¬(p ∨ q) ≡ ¬p ∧ ¬q@and its twin;;p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)@distribution;;p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)@and the other way;;p → q ≡ ¬p ∨ q@the conditional law"
Here are the ones you'll use most. There's double negation. There's De Morgan, and its twin. There's distribution, and the other way round. And there's the conditional law, p implies q is not p or q.

@art flip-gate
De Morgan is how a negation is pushed inward past a connective, and the connective flips as it passes. And becomes or, and or becomes and. Forget the flip, and not of p and q turns into not p and not q, which differs from it in two of the four rows.

@words text="p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)" sub="p = T: both T  ·  p = F: both q ∧ r"
Distribution works both ways here, unlike in arithmetic. The second law is the one people doubt, so check it. When p is true, both sides are true. When p is false, both sides are q and r. It holds.

@chapter Chains of laws
@art swap-piece
Substitution is what makes rewriting work. If A is equivalent to B, then you can replace A by B inside a larger formula, and the result is equivalent too. And every law could be checked by a truth table. They're shortcuts, not new facts. They let you handle a thirty two row formula without writing thirty two rows.

@math heading="Simplify ¬(p → q)" items="¬(p → q)@not of p implies q;;≡ ¬(¬p ∨ q)@conditional law;;≡ ¬¬p ∧ ¬q@De Morgan;;≡ p ∧ ¬q@double negation"
Simplify not of p implies q. The conditional law makes it not of not p or q. De Morgan makes it not not p, and not q. And double negation gives p and not q. A conditional fails exactly when the hypothesis holds and the conclusion doesn't.

@chapter A worked equivalence
@math heading="(p → q) ∧ (p → r)  ≡  p → (q ∧ r)" items="(¬p ∨ q) ∧ (¬p ∨ r)@conditional law, twice;;≡ ¬p ∨ (q ∧ r)@distribution, backwards;;≡ p → (q ∧ r)@conditional law again"
Show that p implies q, and p implies r, is equivalent to p implies q and r. Three variables means eight rows, but the chain is shorter. Use the conditional law, twice. Then distribution, backwards. Then the conditional law again.

@art balance-scale
Read it back in English. Promising q and promising r, both on the same condition, is promising q and r on that condition. The chain proves it. The sentence is why you should have expected it.

@art chain-steps
So which method? With up to three variables, build the table. It's eight rows, takes a minute, and can't be wrong. With more, chain the laws. Start from the more complicated side, get rid of every arrow first, and name the law at each step.

@chapter Where people slip
@list heading="Common slips" items="Negating without flipping the connective@The first|Using ≡ inside a formula@The second|Checking a few rows and stopping@the third"
The first slip is negating both sides of a connective without flipping it. The second is treating the triple bar as a connective inside a formula. And the third is checking a few rows and concluding equivalence. Agreement on the rows you looked at isn't agreement on all of them.

@chapter Try it
@words text="¬(p ∨ (¬p ∧ q))  ≡  ¬p ∧ ¬q" sub="name each law: De Morgan, distribution, negation"
Your turn. Take not of, p or, not p and q, and reduce it to not p and not q. Name the law at each step: De Morgan, distribution and negation. A step you can't name is a step you've guessed.

@end text="Find the row that separates them"
You can compare two formulas and see any row that separates them, on Learn. That's learn dot get er done dot I O.
