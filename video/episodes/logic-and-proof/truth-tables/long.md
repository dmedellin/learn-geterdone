---
format: long
lesson: logic-and-proof/truth-tables
title: Truth tables: the method that can never be wrong
thumb: Every case, in order
---

@chapter The question
@title text="Truth Tables" sub="Logic and Proof" art=thumb
Hand someone a compound statement, like not p or, q and r. Is it true? It depends on p, q and r. So list every possible case, and work out the value in each one. That's a truth table. It's finite, it's mechanical, and it's complete.

@chapter How many rows
@art doubling-tree
A truth table has one row for each way of assigning true or false to the variables. Each variable takes its two values independently, so every new variable doubles the rows. With n variables, you get two to the n rows.

@math heading="n variables  ⟹  2ⁿ rows" items="1 variable  →  2 rows@one variable;;2 variables  →  4 rows@two variables;;3 variables  →  8 rows@three variables;;5 variables  →  32 rows@five give"
One variable gives two rows. Two variables give four. Three variables give eight, and five give thirty two.

@words text="TT · TF · FT · FF" sub="T before F, rightmost variable fastest"
The usual order lists true before false, and varies the rightmost variable fastest. So with two variables the rows read T T, T F, F T, F F. Any order works, but a consistent one lets you compare two tables line by line.

@chapter Columns, inside out
@art stacked-columns
Then add one column for each subexpression, starting with the innermost, exactly as you'd evaluate arithmetic. Those middle columns aren't decoration. If the last column looks wrong, they show you exactly which step went wrong.

@math heading="¬(p ∧ q)  vs  ¬p ∨ ¬q" items="p ∧ q:  T F F F@first a column;;¬(p ∧ q):  F T T T@then negate;;¬p ∨ ¬q:  F T T T@same four values"
Build not of p and q. First a column for p and q, which is true in one row of four. Then negate it, and it's true in three. Now compare a column for not p or not q. Same four values. That agreement is De Morgan's law, and the table is its proof.

@art matching-columns
And that's the point. If two formulas agree in every row, they're equivalent, full stop. There's nothing more to check, because the rows are all the cases there are.

@chapter A full example
@math heading="¬p ∨ (q ∧ r), p true" items="T T T  →  ¬p F, q∧r T  →  T@true true true;;T T F  →  ¬p F, q∧r F  →  F@true true false;;T F T  →  ¬p F, q∧r F  →  F@true false true;;T F F  →  ¬p F, q∧r F  →  F@true false false"
Try not p or, q and r. Three variables, so eight rows. Here are the four where p is true. True true true gives true. True true false, false. True false true, false. And true false false, false. With p true, everything rests on q and r, and only the row where both hold survives.

@math heading="¬p ∨ (q ∧ r), p false" items="F T T  →  ¬p T  →  T@false true true;;F T F  →  ¬p T  →  T@false true false;;F F T  →  ¬p T  →  T@false false true;;F F F  →  ¬p T  →  T@false false false"
Now the four where p is false. Not p is true, so the disjunction is true whatever q and r do. False true true, false true false, false false true, false false false: all true. Four rows, settled by one column.

@chapter Complete, but big
@art checked-grid
Any question about a formula built from these connectives, is it always true, is it ever true, is it equivalent to this other one, is answered by its truth table. Read the last column. All true is a tautology, all false is a contradiction, and a mixture is contingent.

@art growing-grid
The catch is size, never correctness. Ten variables give one thousand and twenty four rows, and twenty give over a million. That growth is why the equivalence laws later in the course are worth having.

@chapter Where people slip
@list heading="Common slips" items="Writing fewer than 2ⁿ rows@The first|Evaluating outside in@The second|Changing the row order between tables@The third"
The first slip is writing fewer than two to the n rows. A missing row is a case you haven't checked, and it's exactly where a counterexample tends to live. The second is evaluating outside in. The third is changing the row order between two tables you mean to compare.

@art missing-row
Each one hides a case from you. And a table only settles the question when every case is on it.

@chapter Try it
@words text="(p ∨ q) ∧ ¬(q ∧ r)" sub="3 variables → 8 rows"
Your turn. Take p or q, and not, q and r. Count the variables first. Three, so eight rows. Then fill the variable columns: the rightmost alternates every row, the next every two, the next every four.

@words text="p ∨ q · q ∧ r · ¬(q ∧ r)" sub="one column each, inside out"
Now write the subexpressions, with separate columns for p or q, for q and r, and for not q and r. When the row pattern is automatic, the rest of this course is bookkeeping.

@end text="Type a formula, get its table"
You can type any formula and watch its table build column by column, on Learn. That's learn dot get er done dot I O.
