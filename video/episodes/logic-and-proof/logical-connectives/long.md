---
format: long
lesson: logic-and-proof/logical-connectives
title: Not, and, or, exclusive or: the four logical connectives
thumb: Or means one or both
---

@chapter The question
@title text="Logical Connectives" sub="Logic and Proof" art=thumb
Once you have propositions, you want to combine them. It's raining and the ground is wet. It's not raining. There are four connectives to learn, and each one is defined by exactly what it does to truth values. One of them causes most of the trouble.

@chapter Not and and
@art flip-switch
Start with negation. Not p is true when p is false, and false when p is true. It just flips the value. It's the only connective in this course that takes a single proposition.

@art series-circuit
Conjunction is p and q. It's true exactly when both p and q are true. Picture two switches in a row. The lamp lights only when both are closed. Out of the four rows, just one is true.

@chapter Or is inclusive
@art parallel-circuit
Disjunction is p or q. It's true exactly when at least one of p and q is true. That's three rows of the four. Put the switches side by side, and either one lights the lamp, and so do both together. This is the inclusive or.

@art two-roads
Exclusive or is true exactly when exactly one of p and q is true. So when both are true, it's false. That single row is where it parts company with ordinary or.

@chapter The whole table
@math heading="p, q → ¬p · p∧q · p∨q · p⊕q" items="T T  →  F · T · T · F@both are true;;T F  →  F · F · T · T@true and false;;F T  →  T · F · T · T@false and true;;F F  →  T · F · F · F@both false"
Here are all four at once. When both are true, not p is false, and is true, or is true, and exclusive or is false. True and false gives false, false, true, true. False and true gives true, false, true, true. And both false gives true, false, false, false.

@words text="p ∨ q  vs  p ⊕ q" sub="they differ in one row of four: both true"
The two kinds of or differ in exactly one row, the top one. And that's exactly where English is ambiguous.

@art coffee-or-tea
You may have coffee or tea usually means one, not both. An error occurs if the file is missing or unreadable means either, or both. Mathematics settles it by decree. Or is always inclusive.

@chapter Translating English
@math heading="p = “it is raining”, q = “the ground is wet”" items="raining and wet  →  p ∧ q@raining and the ground is wet;;raining but not wet  →  p ∧ ¬q@but the ground is not wet;;neither raining nor wet  →  ¬p ∧ ¬q@neither is it raining;;one or the other, not both  →  p ⊕ q@but not both"
Let p be it is raining, and q be the ground is wet. It is raining and the ground is wet is p and q. It is raining but the ground is not wet is p and not q. Neither is it raining nor is the ground wet is not p and not q. And one or the other, but not both, is exclusive or.

@words text="but = and" sub="the contrast is emphasis; the truth conditions are the same"
Notice that but became and. But, although and however signal contrast, and logic simply drops that shade of meaning, because p but q has the same truth value as p and q in every case. What remains is checkable.

@chapter Precedence
@math heading="Tightest to loosest: ¬, ∧, ∨ and ⊕, →, ↔" items="¬p ∨ q ∧ r@not p or q and r;;(¬p) ∨ (q ∧ r)@means not p"
Connectives have a precedence. Not binds tightest, then and, then or and exclusive or, then the arrows. So not p or q and r means not p, or, q and r. That's convention, not mathematics, and parentheses always win.

@art bracket-pair
So when in doubt, write the parentheses. Not p and q means not p, then and q, because the not grabs only the p. If you want the not to govern more than a single letter, put brackets around everything it governs.

@chapter Where people slip
@list heading="Common slips" items="Reading ∨ as exclusive@The first|Dropping brackets around a negation@The second|Translating “but” as anything but ∧@the third"
The first slip is reading or as exclusive. It costs you one row in every table with a disjunction. The second is dropping the brackets around a negation. Not p and q, and not of p and q, disagree in two of the four rows. And the third is translating but as anything other than and.

@chapter Try it
@words text="(p ∨ q) ∧ ¬(p ∧ q)  ≡  p ⊕ q ?" sub="check all four rows"
Your turn. Here's the test of or: whenever a sentence says either p or q, ask what happens when both hold. If it's still true, it's or. If it becomes false, it's exclusive or. Then check that p or q, and not both, matches exclusive or in all four rows.

@end text="Compare the two ors, row by row"
You can put the two ors side by side and read the row where they differ, on Learn. That's learn dot get er done dot I O.
