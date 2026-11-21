---
format: long
lesson: paradoxes-and-their-exits/the-liar
title: The liar paradox: a sentence with no row to stand in
thumb: This sentence is not true
---

@chapter The sentence
@title text="The Liar" sub="Paradoxes and Their Exits" art=thumb
Print a sentence in a box. The sentence in this box is not true. Call it L. Nothing in the grammar is odd. A sentence can refer to itself by being the sentence in a named place, like a label on a jar. So, is L true?

@list heading="The liar argument" items="L says that L is not true@L says|True exactly when things are as it says@A sentence is true|Every sentence is true or not true@Every sentence|So L is true exactly when L is not true@So L"
Here's the argument. L says that L is not true. A sentence is true exactly when things are as it says. That's the truth schema. Every sentence is either true or not true. And so, L is true exactly when L is not true.

@chapter The table
@math heading="p: L is true" items="p ↔ ¬p@p if and only if not p;;p = T:  T ↔ F  is  F@p true;;p = F:  F ↔ T  is  F@p false"
Let p stand for, L is true. The first two premises give p if and only if not p. The table has two rows. With p true, it's true if and only if false, which is false. With p false, it's false if and only if true, also false. It's the barber's form. The premises can't all be true.

@art two-rows
The two halves can be read separately. If p then not p is true in just one row, where p is false. If not p then p is true in just one row, where p is true. Each half is satisfiable alone, but in different rows. That's why the pair isn't. And p or not p, the third premise, is true in both rows.

@chapter Simply false?
@art row-to-row
Here's why the common first reply fails. Someone says the liar is simply false. That's the row where p is false. In that row L is not true, which is exactly what L says. So things are as L says, and by the schema, L is true. The reply starts in one row and ends in the other. Simply true fails the same way. There's no row left.

@art no-room
Saying it's neither true nor false doesn't escape either. L says it's not true. If it's neither, then it's not true, which is what it says. So it's true after all. That's why the sentence says not true, rather than false. A gap is stepped around, unless you give up the third premise, and restrict the schema to match.

@chapter Tarski's exit
@art language-ladder
The exit that defines the field is Tarski's. A language can't contain its own truth predicate. The word true, for sentences of one language, belongs to a richer language that can talk about the first. And for that one, you need a richer one still.

@art boxed-sentence
That bites at the first premise. No sentence of the lower language can say of itself that it isn't true, because it has no such word. So the liar isn't false, or gappy. It isn't a sentence of any language in the hierarchy.

@list heading="Three exits, three prices" items="Tarski: a ladder English doesn't follow@The price|A third status: the strengthened liar@One gives up|Accept it: a new consequence relation@The other accepts"
The price is real. English has one word true, used without a subscript, about sentences that contain it. The hierarchy is a repair, not a description. One gives up the third premise, at the cost of the strengthened version. The other accepts the conclusion, which needs a logic where a contradiction doesn't entail everything. Which is least costly is left open.

@chapter Where people slip
@list heading="Common slips" items="Calling the liar simply false@The first|Taking the table as the solution@The second|Dismissing the sentence as meaningless@And the third"
The first slip is calling the liar simply false. The argument crosses to the other row. The second is taking the table as the solution. It shows the premises can't all hold, not which one failed. And the third is dismissing the sentence as meaningless. It's built by ordinary grammar, and a rule that bans it needs a line that doesn't remove sentences we use.

@chapter Try it
@art jar-label
Run the four formulas in the lab. p if and only if not p, then each half, then p or not p. Note which rows each one holds in. Then choose a premise to give up, and write what the strengthened liar says to your choice.

@end text="Choose a premise, state the price"
You can run the liar's table yourself, on Learn. That's learn dot get er done dot I O.
