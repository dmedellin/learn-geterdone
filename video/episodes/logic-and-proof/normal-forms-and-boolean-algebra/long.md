---
format: long
lesson: logic-and-proof/normal-forms-and-boolean-algebra
title: DNF and CNF: reading a formula straight off its truth table
thumb: Any table becomes a formula
---

@chapter The question
@title text="Normal Forms and Boolean Algebra" sub="Logic and Proof" art=thumb
Formulas come in every shape. But every single one can be rewritten into one of two standard shapes, and you can read either shape straight off the truth table.

@art circuit-chip
And the same algebra runs digital circuits. And, or and not are the AND, OR and NOT gates in a chip.

@chapter Three words, two shapes
@list heading="Vocabulary" items="literal: p, ¬q@A literal|clause: an OR of literals@A clause|term: an AND of literals@a term"
A literal is a variable or its negation, like p, or not q. A clause is literals joined by or. And a term is literals joined by and.

@words text="DNF: an OR of ANDs · CNF: an AND of ORs"
A formula is in disjunctive normal form, D N F, when it's terms joined by or. An or of ands. It's in conjunctive normal form, C N F, when it's clauses joined by and. An and of ors. And every formula has both.

@chapter DNF from the true rows
@art row-picker
Here's how to get the D N F. Take each row where the formula is true. Write the term that describes exactly that row: p if p is true there, not p if it's false. That term is true in its one row and false everywhere else. Join the terms with or, and the result is true in exactly the right rows.

@math heading="True in rows TF and FT" items="row T F  →  p ∧ ¬q@true false;;row F T  →  ¬p ∧ q@false true;;(p ∧ ¬q) ∨ (¬p ∧ q)  ≡  p ⊕ q@join them"
Say a formula is true in exactly two rows. Row true false gives p and not q. Row false true gives not p and q. Join them with or, and that's exactly p exclusive or q. That's how any truth function at all gets a formula.

@chapter CNF from the false rows
@art rule-out
For C N F, use the false rows instead. For each one, write a clause that's false in exactly that row, and true everywhere else. It rules that row out. Join the clauses with and. That's the form SAT solvers consume.

@math heading="False only at p = T, q = F" items="p is T there  →  ¬p@p is true;;q is F there  →  q@q is false;;clause:  ¬p ∨ q@the clause"
Watch the polarity. Say a formula is false only where p is true and q is false. p is true there, so you write not p. q is false there, so you write q. The clause is not p or q. Get this backwards and the clause rules out the wrong row.

@chapter The algebraic route
@math heading="CNF of p → (q ∧ r)" items="≡ ¬p ∨ (q ∧ r)@conditional law;;≡ (¬p ∨ q) ∧ (¬p ∨ r)@distribution;;check p=T, q=T, r=F:  F and F  ✓@check one row"
Or transform with the laws. P implies q and r becomes not p or, q and r, by the conditional law. Distribution gives not p or q, and, not p or r. Now check one row, p and q true, r false. The original is false, and so is the C N F. A spot check doesn't prove it. It catches slips.

@chapter Functional completeness
@math heading="Enough connectives" items="{∧, ∨, ¬}  complete@and, or and not;;p ∨ q ≡ ¬(¬p ∧ ¬q)  so  {∧, ¬}  complete@and and not alone;;¬p ≡ p ↑ p@not p is p NAND p;;p ∧ q ≡ (p ↑ q) ↑ (p ↑ q)@and p and q"
Because every table has a D N F, and, or and not can express every truth function. They're functionally complete. So are and and not alone, since De Morgan rebuilds or from them. And a single connective is enough. NAND, not of p and q. Not p is p NAND p. And p and q is p NAND q, NAND, p NAND q.

@art gate-layers
Swap true and false for one and zero, and these are AND, OR and NOT gates. A D N F is a two level circuit: a layer of AND gates feeding one OR gate. And because NAND is complete, a chip can be built from one kind of gate.

@chapter Where people slip
@list heading="Common slips" items="Backwards polarity in CNF@The first|Assuming canonical means minimal@The second|Assuming conversion is cheap@the third"
The first slip is getting the polarity backwards in C N F. The second is assuming the canonical form is minimal. And the third is assuming conversion is cheap. Turning C N F into D N F can multiply the size exponentially.

@art big-vs-small
Take a formula in p, q and r that is false only when all three are true, so it is true in seven of its eight rows. Its canonical D N F has seven terms of three literals each. But the same formula is not p or not q or not r. Its one false row, ruled out by one clause. Canonical and small are different goals.

@chapter Try it
@words text="(p ⊕ q) ∧ r" sub="table → canonical DNF and CNF"
Your turn. Take p exclusive or q, and r. Build its table, then write the canonical D N F and C N F. Check the counts: one term per true row and one clause per false row. They must match exactly.

@end text="Check a formula against its normal form"
You can put a formula beside its normal form and check that no row separates them, on Learn. That's learn dot get er done dot I O.
