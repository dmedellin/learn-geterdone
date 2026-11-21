---
format: long
lesson: code-complete-statements/boolean-expressions
title: Boolean expressions: negate a condition without breaking it
thumb: Same on every row
---

@chapter The question
@title text="Boolean Expressions" sub="Code Complete, chapter 19" art=thumb
How should you write a condition? Every control structure except plain sequence depends on one. So the first half of chapter nineteen is about the tests that control every decision you write.

@quote text="Making boolean expressions simple and readable contributes substantially to the quality of your code." cite="McConnell, Code Complete, 2nd ed., Chapter 19, p. 460"
That's the chapter's first key point. Making boolean expressions simple and readable contributes substantially to the quality of your code.

@chapter Simple and readable
@list heading="Write tests a reader can follow" items="true and false, not 1 and 0@true and false|while (!done), not done == false@implicitly|Name a long test@good names|Decision tables for many variables@decision table"
Use true and false rather than one and zero, which a reader can't tell from a count. Compare boolean values implicitly, writing while not done. Break a long test into intermediate variables with good names, or a boolean function. And where several variables combine, consider a decision table.

@art named-test
McConnell prefers a well named function to a comment, because code is read and kept up to date more reliably than comments are. The name says what the test is for.

@chapter Positive forms
@art negatives-tangle
Form expressions positively. The section opens with a line of Homer Simpson's built entirely of negatives, and most people struggle with more than one. Swap the if and else clauses to turn a negative test positive, or pick a variable name whose truth runs the other way.

@math heading="DeMorgan's theorems" items="!(a || b)  ≡  !a && !b@not a or b;;!(a && b)  ≡  !a || !b@not a and b"
And to remove a negation from a compound test, use DeMorgan's theorems. Not a or b is the same as not a and not b. Not a and b is the same as not a or not b. The recipe: negate each operand, switch the ands and ors, and negate the whole.

@chapter Check it by truth table
@code block=1 lines=1-11 label=Java focus="4@guard on line four|7@test on line seven"
Here's a routine written for the lesson. The loop's guard on line four and the test on line seven ask the same question. Once it's negated as a group, not done or error. Once it's negated part by part, not done and not error.

@art truth-grid
The lab checks that with a truth table. Two variables give four rows, every combination of true and false. Two conditions are equivalent only if they agree on every row.

@math heading="demorgan" items="!(done || error):  true on 1 of 4@not done or error;;!done && !error:  true on 1 of 4@not done and not error;;equivalent: yes@equivalent"
For line four, not done or error, is true on one row of four. Line seven, not done and not error, is also true on one row. They're equivalent, and no row differs.

@chapter The half-applied version
@math heading="half-demorgan" items="!(done || error):  true on 1@true on one;;!done || !error:  true on 3@true on three;;not equivalent, on 2 of 4 rows@two of four"
Now negate each part and forget to switch the operator. Not done or not error. The original is true on one row. This one is true on three. They're not equivalent, and they differ on two of four rows.

@art wrong-row
The first one that differs is done true, error false. The queue's empty, nothing failed, and the half applied version would still try to process the next item.

@art two-tables
The truth table also simplifies. Compare found and valid, or found and not valid, with plain found. They're equivalent, each true on two of four rows. Whatever valid is, one of the two halves holds whenever found does.

@words text="!(!ready || !loaded)  ≡  ready && loaded"
Likewise, not, not ready or not loaded, is equivalent to ready and loaded. And the positive form is the one to write.

@chapter Evaluation
@art short-circuit
Know how your language evaluates. Java's and and or short circuit, so count greater than zero and total over count greater than limit never divides by zero. Its single ampersand and bar evaluate both sides. And parenthesize for the reader, not the compiler. Extra parentheses cost nothing.

@chapter Where people slip
@list heading="Common slips" items="Negating each part, not the operator@The first|Parentheses only for the compiler@The second|Treating & and && as the same@the third"
The first slip is negating each part and keeping the operator. That's the half applied DeMorgan, wrong on two rows. The second is treating parentheses as something only the compiler needs. And the third is treating Java's ampersand and double ampersand as the same. Only the double one stops when the left side is false.

@chapter Try it
@code block=2 lines=1-3 label=Java focus="1@isAdmin or not isOwner"
Your turn. This condition reads, not, isAdmin or not isOwner. Rewrite it with no negated group, using DeMorgan's theorems. Then check it by writing the four rows of isAdmin and isOwner for both versions.

@end text="Check two conditions, row by row"
You can type both conditions into the truth table lab and check your rows, on Learn. That's learn dot get er done dot I O.
