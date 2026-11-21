---
format: long
lesson: logic-and-proof/tautologies-and-satisfiability
title: Tautology, contradiction, satisfiability: always, never, sometimes
thumb: Can anything make it true?
---

@chapter The question
@title text="Tautology, Contradiction, Satisfiability" sub="Logic and Proof" art=thumb
Build a truth table, and look only at the last column. There are just three things it can look like. All true, all false, or a mix. That simple sorting leads straight to one of the most famous problems in computer science.

@chapter Three classes
@art three-columns
A formula is a tautology if it's true under every assignment, like p or not p. It's a contradiction if it's true under none, like p and not p. And it's contingent otherwise, true under some assignments and false under others, like p and q.

@art single-lit-row
Then there's satisfiable. A formula is satisfiable if at least one assignment makes it true. Tautologies and contingent formulas are satisfiable. Contradictions aren't. Satisfiable asks whether some row is true. Tautology asks whether every row is.

@art mirror-pair
These questions are all linked. A is a tautology exactly when not A is unsatisfiable. A is a contradiction exactly when not A is a tautology. Every one of these questions reduces to the others, so an algorithm for one is an algorithm for all.

@words text="A ≡ B  exactly when  A ↔ B is a tautology"
Even equivalence fits in here. A is equivalent to B exactly when A if and only if B is a tautology. So the whole of logical equivalence is a special case of this lesson.

@chapter Three formulas
@math heading="Classify" items="(p → q) ∨ (q → p)  →  tautology@check all four rows;;(p ↔ q) ∧ (p ⊕ q)  →  contradiction@negations of each other;;p → (q ∧ r)  →  contingent@is contingent"
p implies q, or q implies p, is a tautology. Check all four rows. p if and only if q, and p exclusive or q, is a contradiction, since the two parts are negations of each other. And p implies, q and r, is contingent.

@chapter Assume it's false
@words text="Tautology? Try to make it false." sub="Satisfiable? Try to make it true."
You don't always need the full table. To test for a tautology, assume the whole formula is false and work backwards. To test satisfiability, look for one assignment that makes it true. Finding one ends the question.
@math heading="((p → q) ∧ ¬q) → ¬p" items="Suppose it is F@Suppose;;(p → q) ∧ ¬q = T,  ¬p = F@hypothesis true;;¬p = F  ⟹  p = T@so p is true;;¬q = T  ⟹  q = F@so q is false;;p = T, q = F  ⟹  p → q = F  ✗@contradiction"
Is this a tautology? Suppose it's false. A false conditional means the hypothesis true and the conclusion false. Not p is false, so p is true. Not q is true, so q is false. But then p implies q is false, which breaks the hypothesis. That's a contradiction.

@words text="No falsifying row  ⟹  tautology" sub="this one is modus tollens"
No assignment makes it false, so it's a tautology. It even has a name, modus tollens. Every valid rule of inference is a tautology in this shape: the premises joined by and, implying the conclusion.

@art empty-claim
Notice what a tautology says about the world. Nothing. P or not p is true whatever p means, so learning it tells you nothing. That's exactly why it's safe to use as a step in reasoning.

@chapter The hard problem
@art vast-grid
Now satisfiability by truth table takes two to the n rows. With three hundred variables, small for real applications, that's two to the three hundred rows. More than there are atoms in the observable universe. And no faster general method is known.

@words text="SAT is NP-complete" sub="Cook, 1971"
In nineteen seventy one, Cook showed that deciding satisfiability was the first NP complete problem. This innocent question became the reference point that computational hardness is measured against.

@art solver-gears
And yet, modern SAT solvers routinely handle formulas with millions of variables, because real instances have structure that the worst case doesn't. Hardness in the worst case and difficulty in practice are different claims.

@chapter Where people slip
@list heading="Common slips" items="Confusing satisfiable with true@The first|Thinking a tautology says something@The second|Reading NP-complete as impossible@the third"
The first slip is confusing satisfiable with true. A satisfiable formula could be true, but that depends on the assignment. The second is thinking a tautology says something about the world. And the third is reading NP complete as impossible. It's a statement about worst case scaling.

@chapter Try it
@words text="(p ∨ q) → (p ∧ q)" sub="tautology? find a falsifying row"
Your turn. Is p or q, implies p and q, a tautology? Don't build the table. Try to make it false: the hypothesis true and the conclusion false. You should find a falsifying row in two lines, and be able to say which one it is.

@end text="Classify any formula"
You can type a formula and watch it classified by its true rows, on Learn. That's learn dot get er done dot I O.
