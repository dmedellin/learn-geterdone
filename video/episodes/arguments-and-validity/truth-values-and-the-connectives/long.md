---
format: long
lesson: arguments-and-validity/truth-values-and-the-connectives
title: Not, and, or: the truth tables, and the one row where or splits
thumb: Or includes both
---

@chapter Connectives are tables
@title text="Truth Values and the Connectives" sub="Arguments and Validity" art=thumb
In logic, not, and and or don't mean whatever the English words suggest. Each one is defined by a table: give it the truth values of the parts, and it hands back the truth value of the whole.

@art inputs-to-output
That matters, because English words carry extra baggage. Where the word says more than the table, the table wins. And the connective that surprises people most is or.

@chapter Not and and
@math heading="Negation" items="p T  →  ¬p F@when p is true;;p F  →  ¬p T@when p is false"
Start with negation. Not p is false when p is true, and true when p is false. The safe English for it is, it is not the case that.

@math heading="Conjunction" items="p ∧ q is T only in the row T, T@only when both"
Conjunction. P and q is true only when both p and q are true. And is the usual word. But and although count too, for truth value.

@art clever-but-lazy
She's clever but lazy carries a contrast. The table doesn't record it. For truth value, the sentence is true exactly when she's clever and she's lazy. Whatever else but suggests, the connective doesn't compute it.

@chapter Or includes both
@math heading="Disjunction" items="p ∨ q is F only in the row F, F@only when both parts are false;;so p ∨ q is T in three rows@three of the four"
Now disjunction. P or q is false only when both parts are false. So it's true in three of the four rows, and one of those is the row where both are true. Logic's or is inclusive.

@math heading="Inclusive ∨ against exclusive ⊕" items="T T:   ∨ T    ⊕ F@both true;;T F:   ∨ T    ⊕ T@p only;;F T:   ∨ T    ⊕ T@q only;;F F:   ∨ F    ⊕ F@neither"
The exclusive reading, true when exactly one part is true, is a separate connective. Put the two columns side by side. Both true: inclusive says true, exclusive says false. P only: both true. Q only: both true. Neither: both false. They differ in exactly one row.

@chapter Soup or salad
@art soup-and-salad
That first row is where English leaves a gap. You may have soup or salad, on a menu, usually means one of them. That's the exclusive reading. But you'll be fined if you're late or absent doesn't let you escape by being both. That's the inclusive reading.

@art menu-gap
So a diner orders soup and salad both. On the logician's or, they've complied with the menu. On the exclusive one, they haven't. The sentence doesn't say which, and that's why contracts and laws often add or both, or but not both.

@chapter Building a table
@list heading="Four steps" items="List the four cases@list the cases|Add a column for each smaller piece@Add a column|Fill each from the columns it depends on@fill each column|Read the last column@read the answer"
Any compound sentence over two letters takes the same four steps. List the cases, always in the same order. Add a column for each smaller piece, working from the inside out. Fill each column from the ones it depends on, never from how the English sounds. Then read the answer in the last column.

@art nested-pieces
Compound sentences nest, so their tables are built the way the sentences are. Each smaller piece gets its own column, and each column is read from the ones before it. That keeps every step visible, and it stops you guessing from the sound of the words.

@math heading="¬p ∧ ¬q" items="¬p:  F F T T@first not p;;¬q:  F T F T@then not q;;¬p ∧ ¬q:  F F F T@combine them"
Try not p and not q. First not p: false, false, true, true. Then not q: false, true, false, true. Now combine them. Only the last row has both true. So the whole is true only when p and q are both false. That's the sentence neither p nor q.

@art truth-grid
And once the last column is filled, comparing two sentences is just comparing two columns, row by row. The rows with true in them are the cases where the whole sentence is true. Count them, and you know exactly what the sentence claims.

@chapter Where people slip
@list heading="Common slips" items="Reading or as exclusive@The first|Treating but as more than and@The second|Reading a compound in the wrong order@the third"
The first slip is reading or as exclusive. Do that, and a valid argument will look invalid later in the course. The second is treating but as something other than a conjunction. And the third is reading a compound in the wrong order. Not p and q negates p alone. Not, around p and q in brackets, negates the whole conjunction. Different tables.

@chapter Try it
@words text="“Staff or members only.”" sub="Ana is both."
Here's one to try. A sign says staff or members only. Ana is both. On the logician's reading of or, is she admitted? Find her row in the table, and then ask what a careful writer would add if they meant the exclusive reading.

@end text="Compare or with exclusive or"
You can build these tables, and compare any two formulas row by row, on Learn. That's learn dot get er done dot I O.
