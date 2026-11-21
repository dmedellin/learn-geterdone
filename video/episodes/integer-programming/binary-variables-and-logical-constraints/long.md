---
format: long
lesson: integer-programming/binary-variables-and-logical-constraints
title: Turning if-then into an inequality, and checking it row by row
thumb: One row refutes it
---

@chapter The question
@title text="Binary Variables and Logical Constraints" sub="Integer Programming" art=thumb
If you fund project A, you must fund project B. How do you write that sentence into a linear model? And once you've written it, how do you know it says what you meant, and not the opposite?

@art switches
Use a binary variable: one that can only be zero or one. It carries a decision. One means the project is chosen, zero means it isn't. There's no zero point six. The first thing to write next to any binary is the sentence it stands for.

@chapter What an encoding means
@words text="Agree on every assignment" sub="one disagreeing row refutes it"
An inequality encodes a condition when, for every assignment of zeros and ones, the inequality holds exactly when the condition does. That's a strict test. One assignment where they disagree refutes the encoding, and one is all it takes.

@art truth-grid
So you check it against the truth table. With three binaries there are eight rows. For each one, you write whether the condition holds, and whether the inequality holds. Eight rows can be read in a few seconds. Fifty binaries would be far too many rows, but each encoding only touches two or three variables, so you check the row, then use it.

@chapter If A then B
@math heading="If A then B" items="y_A − y_B ≤ 0@y A minus y B;;forbids only  y_A = 1, y_B = 0@forbids"
If A then B is y A minus y B, at most zero. Read it as: A can't be chosen unless B is. It forbids exactly one combination, A chosen with B not chosen. The other three are allowed, including B on its own.

@art if-then-arrow
The trap is the converse. Swap the letters and you get y B minus y A, at most zero. That looks just as tidy, and nothing in its appearance tells you which one you wrote.

@art refuting-row
So check it. The converse disagrees with the condition on four of the eight rows. The first is A one, B zero, C one. The condition fails there, but the converse holds. It permits exactly the case the condition was written to forbid.

@chapter Five conditions
@list heading="Five encodings" items="If A then B:  y_A − y_B ≤ 0@If A then B|At least one:  y_A + y_B ≥ 1@At least one|At most k:  y_A + y_B + y_C ≤ k@At most k|Exactly one:  y_A + y_B + y_C = 1@Exactly one|Both:  y_A + y_B ≥ 2@Both"
If A then B, you've seen. At least one of A and B: their sum is at least one, and both is allowed. At most k: the sum is at most k. Exactly one: the sum equals one. Both: the sum is at least two.

@art exactly-one
Exactly one and at most one differ on a single row, the empty one. At most one lets you choose nothing. Exactly one doesn't. The truth table refutes the at most version on the row zero, zero, zero, and on that row alone.

@art at-most-k
And with three projects and k equal to two, at most two excludes only one assignment: all three chosen together.

@chapter Both is not a product
@words text="y_A · y_B is not linear" sub="use y_A + y_B ≥ 2"
For both A and B, you might reach for y A times y B. That's not linear, so it has no place in a linear model. Instead, y A plus y B at least two holds on one, one, and fails on the other three. That's exactly the condition.

@art refuting-row
The encoding people reach for instead, y A plus y B at least one, is refuted on four of the eight rows, starting with one, zero, one. One project chosen, and the inequality is satisfied anyway.

@chapter Where people slip
@list heading="Common slips" items="Writing the converse for if-then@The first|Using ≤ 1 for at least one@The second|Multiplying binaries@And the third"
The first slip is writing the converse for if then. The second is using at most one for at least one. They share the word one, and that's the whole trap. Read the relation aloud before you write it. And the third is multiplying binaries. Where a product seems needed, the model usually wants one more binary.

@chapter Try it
@words text="At least one of A and B" sub="check y_A + y_B ≥ 1 on all four rows"
Your turn. Write the four assignments of y A and y B. For each, decide whether at least one of A and B holds, and whether y A plus y B at least one holds. Then do the same for at most one, and find the two rows where they differ.

@end text="Check an encoding row by row"
You can type an inequality and see it checked against the truth table, row by row, on Learn. That's learn dot get er done dot I O.
