---
format: long
lesson: arguments-and-validity/validity-by-truth-table
title: Testing validity with a truth table, and the one row that refutes
thumb: One row is enough
---

@chapter The counterexample row
@title text="Validity by Truth Table" sub="Arguments and Validity" art=thumb
You can test whether an argument is valid without knowing a single fact about the world. You lay the premises and the conclusion out in one table, and look for one kind of row.

@art counterexample-row
That row is a counterexample. It's an assignment of true and false to the simple sentences that makes every premise true and the conclusion false. Nothing about the world is being claimed. It only has to be a case you can describe.

@words text="Valid: no counterexample row" sub="Invalid: one row is enough"
So an argument is valid when no such row exists, and invalid when one does. And invalidity needs exactly one row to establish it. Validity needs every row checked.

@chapter Modus ponens
@math heading="p → q, p ∴ q" items="T T:  premises T, T  ·  conclusion T@the first row;;T F:  p → q is F@second row;;F T:  p is F@third;;F F:  p is F@fourth"
Here's modus ponens. If p then q, and p, so q. In the first row, both premises are true, and the conclusion is true. In the second row, the conditional is false. In the third and the fourth, p is false. So only one row has every premise true, and there the conclusion holds. Valid.

@art irrelevant-rows
Notice what happened to the other three rows. They each had a false premise, so they were irrelevant. The argument promises nothing in a row where a premise fails, so a row like that can't refute it.

@chapter Affirming the consequent
@math heading="p → q, q ∴ p" items="T T:  premises T, T  ·  conclusion T@In the first;;F T:  premises T, T  ·  conclusion F@p false and q true"
Now swap to: if p then q, and q, so p. Two rows have both premises true. In the first, the conclusion is true. But in the row with p false and q true, both premises hold and the conclusion fails. That's a counterexample, and one is enough.

@art god-and-meaning
Give it content. If God exists, life has meaning. Life has meaning. So God exists. The counterexample row says: there's no God, and life has meaning anyway. The argument is invalid, and that's settled by a table, not by theology.

@words text="Invalid ≠ the conclusion is false"
But be careful what that shows. It doesn't show that God doesn't exist, or that the premises are false. It shows these premises don't settle the conclusion.

@chapter The four forms
@list heading="Four named forms" items="Modus ponens: p → q, p, so q. Valid.@Modus ponens|Modus tollens: p → q, not q, so not p. Valid.@modus tollens|Affirming the consequent: p → q, q, so p. Invalid.@affirming the consequent|Denying the antecedent: p → q, not p, so not q. Invalid.@denying the antecedent"
Two forms are valid and two aren't. Modus ponens, and modus tollens: if p then q, not q, so not p. Then the invalid pair: affirming the consequent, and denying the antecedent: if p then q, not p, so not q. Both invalid forms are refuted by the same row, p false and q true.

@art form-catalogue
Why do these forms get names at all? Because validity belongs to the form. Replace p and q with any sentences you like, and the verdict doesn't change. The lab names a form from the shape of the formulas, not from what the sentences mean.

@art lookalike-pair
The pair that look alike are the pair that differ. Modus tollens denies the consequent and concludes against the antecedent. Denying the antecedent starts from the wrong end. If you can't tell which you're looking at, build the table.

@chapter The method
@list heading="Five steps" items="Translate into letters@Translate|List every row@list every row|Fill the columns@fill the columns|Look only where every premise is true@Look only|No counterexample means valid@no row survives"
Translate the argument into letters. List every row: n letters give two to the n rows. Fill the columns. Look only at rows where every premise is true, and read the conclusion there. That's the step that does the work. And if no row survives, the argument is valid.

@chapter Where people slip
@list heading="Common slips" items="Counting a row with a false premise@The first|Trusting the form's name over the rows@The second|Concluding the conclusion is false@the third"
The first slip is counting a row with a false premise and a false conclusion as a counterexample. The second is treating the name of a form as the verdict. Trust the rows. The table is the definition. And the third is concluding the conclusion is false because the argument is invalid.

@chapter Try it
@words text="“If the butler did it he had a key; he had a key; so the butler did it.”"
Here's one to try. If the butler did it, he had a key. He had a key. So the butler did it. Name the form, and find the row that refutes it.

@art key-and-butler
Here's a hint. He may have had a key without doing it. Write that case as a row, and check that both premises come out true while the conclusion comes out false. And then decide whether the row tells you he's innocent. It doesn't.

@end text="Find the counterexample row"
You can run all four forms, and see their counterexample rows, on Learn. That's learn dot get er done dot I O.
