---
format: long
lesson: arguments-and-validity/equivalence-de-morgan-and-contraposition
title: Not both, neither, and the contrapositive: when two sentences say the same thing
thumb: Same column, same claim
---

@chapter Saying the same thing
@title text="Equivalence, De Morgan and Contraposition" sub="Arguments and Validity" art=thumb
When do two sentences say the same thing? Logic gives a precise answer. Put them in the same table, and compare their columns.

@art matching-columns
Two formulas are equivalent when they have the same truth value in every row. And one row with different values shows they're not. You're looking for a single disagreement, and you need no more than one.

@chapter De Morgan's laws
@math heading="De Morgan" items="¬(p ∧ q)  ≡  ¬p ∨ ¬q@not both;;¬(p ∨ q)  ≡  ¬p ∧ ¬q@neither"
Here are De Morgan's laws. Not both p and q is equivalent to not p, or not q. In words, not both is at least one is not. And not, p or q, is equivalent to not p and not q. Neither is both are not.

@art connective-flip
Notice what happens. To negate a conjunction, you negate the parts and switch the and to or. To negate a disjunction, you negate the parts and switch the or to and. Negating the parts alone gets the connective wrong.

@chapter Rich and famous
@math heading="r: rich · f: famous" items="¬(r ∧ f):   F T T T@not both rich and famous;;¬r ∨ ¬f:     F T T T@not rich or not famous;;¬r ∧ ¬f:     F F F T@neither"
Try it on a sentence. It's not the case that she's both rich and famous. The column for not both rich and famous reads false, true, true, true. Not rich or not famous reads the same, in all four rows. So they're equivalent. But neither reads false, false, false, true.

@art not-both-vs-neither
Look at the second row. She's rich but not famous. Not both is true there, and she's neither is false. So not both and neither are different claims. Not both is true in three rows, neither in one. They come apart when exactly one of the two holds.

@chapter The contrapositive
@art three-rewritings
There's a second equivalence, for conditionals. Take if p then q. Swap the parts and negate each, and you get the contrapositive: if not q, then not p. Swap only, and you get the converse. Negate only, and you get the inverse.

@math heading="p → q and its rewritings" items="p → q:      T F T T@the conditional;;¬q → ¬p:    T F T T@the contrapositive;;q → p:      T T F T@the converse;;¬p → ¬q:    T T F T@the inverse"
Here are the columns. The conditional reads true, false, true, true. The contrapositive reads exactly the same. The converse reads true, true, false, true, and so does the inverse. They differ from the conditional in the second and third rows.

@art square-four-sides
So if a shape is a square, it has four sides, and if a shape doesn't have four sides, it isn't a square, say the same thing. But the converse, if it has four sides, it's a square, is false of a rectangle that isn't a square.

@words text="A conditional and its contrapositive stand or fall together."
That's why a proof of one is a proof of the other. It's also why modus tollens is valid. And because equivalent sentences are interchangeable, you can swap one for the other inside an argument without changing its verdict.

@chapter The test
@list heading="Four steps" items="Put both in the same table@same table|Compare the last columns row by row@Compare the last columns|One disagreement: not equivalent@If you find one|None: equivalent@If you find none"
The test is the same every time. Put both formulas in the same table, with the same letters in the same order. Compare the last columns row by row. If you find one disagreement, they're not equivalent, and that row is the whole proof. If you find none, they're equivalent.

@art swap-and-negate
And for a conditional, remember the recipe that keeps the table: swap, and negate. Do both, and you have the contrapositive. Do only one of them, and you've changed what the sentence says.

@chapter Where people slip
@list heading="Common slips" items="Writing not both as both not@The first|Offering the converse as the contrapositive@The second|Treating not both and neither as one claim@the third"
The first slip is writing not both as both not. The connective has to flip. The second is offering the converse or the inverse as the contrapositive. Of the three rewritings, only one keeps the table. And the third is treating not both and neither as one claim. A claim that she's not both rich and famous is made true by her being rich only.

@chapter Try it
@words text="“If a shape is a square, it has four sides.”" sub="contrapositive?"
Here's one to try. Write the contrapositive of, if a shape is a square, it has four sides. Then write the converse and the inverse too. Put all four in one table, and check that the contrapositive is the only one whose column matches the original in every row.

@end text="Compare two columns"
You can set any two formulas side by side and find the row that separates them, on Learn. That's learn dot get er done dot I O.
