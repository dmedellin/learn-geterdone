---
format: long
lesson: logic-and-proof/conditional-statements
title: If p then q: converse, inverse, contrapositive and vacuous truth
thumb: Only one relative is equivalent
---

@chapter The question
@title text="The Conditional and Its Relatives" sub="Logic and Proof" art=thumb
If p, then q. It's the shape of almost every theorem. And it's false in exactly one case. Once you see which one, the strange parts of the conditional, and its three relatives, stop being strange.

@chapter A promise
@art promise-kept
Think of it as a promise. If you pass the exam, I'll buy you dinner. p is the hypothesis, and q is the conclusion. When is that promise broken?

@math heading="p → q" items="T T  →  T@pass and dinner;;T F  →  F@pass and no dinner;;F T  →  T@if you fail;;F F  →  T@whichever way"
You pass and dinner appears: kept. You pass and no dinner appears: broken. That's the one false row. But if you fail, the promise says nothing about what happens. It isn't broken whichever way things go. So both rows with a false hypothesis count as true.

@art broken-link
That tells you how to attack a conditional. You need one case where the hypothesis is true and the conclusion is false. If you can't describe that case, you haven't understood the claim yet.

@chapter Vacuous truth
@art empty-ring
A conditional with a false hypothesis is vacuously true. Every element of the empty set is prime is true. And so is every element of the empty set is composite. There's nothing in the set to be a counterexample.

@words text="“Every unicorn in this room is purple”" sub="true: no unicorn here to be a counterexample"
That isn't a loophole. It's what makes general statements behave. Every unicorn in this room is purple is true, because there's no unicorn here to break it. Any other convention would make statements about empty sets fail for no reason.

@chapter Three relatives
@math heading="Given p → q" items="converse:  q → p@the converse;;inverse:  ¬p → ¬q@the inverse;;contrapositive:  ¬q → ¬p@the contrapositive"
Every conditional has three relatives. Swap the parts, and you get the converse, q implies p. Negate both, and you get the inverse, not p implies not q. Do both, and you get the contrapositive, not q implies not p.

@art mirror-arrows
Only the contrapositive is equivalent to the original. p implies q is false only when p is true and q is false. Not q implies not p is false only when not q is true and not p is false. That's the same single row. So the two are false in the same case, and true in the other three.

@chapter One statement, four forms
@math heading="p: 6 | n,  q: 3 | n" items="p → q:  if 6 | n then 3 | n  ✓ TRUE@six divides n;;q → p:  if 3 | n then 6 | n  ✗ FALSE (n = 9)@the converse;;¬p → ¬q:  if 6 ∤ n then 3 ∤ n  ✗ FALSE (n = 9)@the inverse;;¬q → ¬p:  if 3 ∤ n then 6 ∤ n  ✓ TRUE@the contrapositive"
Let p be six divides n, and q be three divides n. If six divides n then three divides n is true. The converse, if three divides n then six divides n, is false. Take n equals nine. The inverse is false too, again n equals nine. And the contrapositive, if three doesn't divide n then six doesn't, is true.

@art nested-circles
One value, nine, refutes both the converse and the inverse. That's no coincidence. The converse and the inverse are equivalent to each other, so any counterexample to one is a counterexample to the other.

@chapter Reading English, and if and only if
@list heading="All of these mean p → q" items="q whenever p@q whenever p|p only if q@p only if q|p is sufficient for q@sufficient"
English hides the parts. Q whenever p, p only if q, and p is sufficient for q all mean p implies q. But p if q means q implies p. Only if marks the conclusion, not the hypothesis.

@art two-way-arrow
The biconditional, p if and only if q, is true exactly when p and q have the same value. It's the statement and its converse together. So in a theorem, if and only if is an instruction: two proofs are owed, one in each direction.

@chapter Where people slip
@list heading="Common slips" items="Using the converse as the original@The first|Rejecting vacuous truth@The second|Proving one direction of ↔@the third"
The first slip is using the converse as if it were the original. From p implies q, and q, nothing follows about p. The second is finding vacuous truth absurd and rejecting it. And the third is proving only one direction of an if and only if. That's half an answer, however good the half.

@chapter Try it
@words text="If n is a multiple of 10, then n is a multiple of 5." sub="converse? inverse? contrapositive?"
Your turn. If n is a multiple of ten, then n is a multiple of five. Write the converse, the inverse and the contrapositive, and decide which are true. One integer settles the two that aren't.

@end text="Step through the four relatives"
You can set the conditional against each of its relatives and find the row that separates them, on Learn. That's learn dot get er done dot I O.
