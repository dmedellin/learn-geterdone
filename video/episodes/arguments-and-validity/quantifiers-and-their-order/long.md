---
format: long
lesson: arguments-and-validity/quantifiers-and-their-order
title: Everything has a cause, so something causes everything? The quantifier shift
thumb: Each has one, or one for all?
---

@chapter Every and some
@title text="Quantifiers and Their Order" sub="Arguments and Validity" art=thumb
Everyone loves someone. So there's someone whom everyone loves. Sounds like a slip. It is one, and a simple grid shows exactly where.

@math heading="Two quantifiers" items="∀x: every member@for all;;∃x: at least one member@there exists"
Logic has two quantifiers. The universal one, read for all x, says every member of the universe satisfies what follows. The existential one, read there exists an x, says at least one does. Over a finite universe, the first is a check of every case, and the second is a search for one.

@art grid-of-pairs
With two variables, the new thing is order. Picture the relation as a grid: rows for x, columns for y, and a lit cell wherever the pair holds. Now the order of the quantifiers decides which shape you're looking for.

@chapter The order matters
@math heading="Four shapes" items="∀x ∃y P:  a true cell in every row@each x has its own y;;∃y ∀x P:  one column all true@one y serves every x;;∃x ∀y P:  one row all true@one x pairs with every y;;∀y ∃x P:  a true cell in every column@each y has its own x"
For all x, there exists a y, means each x has its own y: a true cell in every row. There exists a y, for all x, means one y serves every x: a column all true. There exists an x, for all y, means one x pairs with every y: a full row. And for all y, there exists an x, means each y has its own x.

@art who-chooses
Read the quantifiers left to right, and the first one chooses first. In for all x, there exists a y, the y is picked after you know the x, so it can change from one x to the next. In there exists a y, for all x, the y is picked first, and has to serve every x.

@chapter The successor grid
@art successor-edge
Let P mean that y is the successor of x, over the numbers one to four. Over all the numbers, everything has a successor. But this grid ends. Four has no partner, so even for all x, there exists a y, fails at the edge. The universe is part of the claim.

@math heading="Close the loop: 4 is followed by 1" items="every row has a true cell:  ∀x ∃y P true@Every row;;no column is all true:  ∃y ∀x P false@no column"
So close the loop, like a clock, where four is followed by one. Every row now has exactly one true cell, so for all x, there exists a y, is true. No column is true throughout, since each has three false cells. So there exists a y, for all x, is false.

@art wrapped-ring
That one grid settles the order question. One direction holds: if one y serves every x, it serves each. But the reverse fails, and a single grid with the first true and the second false is a complete refutation, whatever the size of the universe.

@chapter The quantifier shift
@words text="“Everything has a cause, so something causes everything.”"
Here's where this bites. Everything has a cause, so something causes everything. The premise is a true cell in every row. The conclusion is a column all true. The wrapped grid has the first and not the second, so the step is invalid. That's the quantifier shift.

@art first-cause-reply
Is that the cosmological argument? That's a separate question. Its defenders say serious versions don't take this step. They argue instead that a chain of causes with no first member is itself impossible. That reply grants the verdict on the form and disputes the formalisation, which is the right kind of reply to make.

@chapter Where people slip
@list heading="Common slips" items="Inferring ∃y ∀x from ∀x ∃y@The first|Reading everyone loves someone as about one person@The second|Forgetting the universe belongs to the claim@the third"
The first slip is the shift itself, reading the two orders as if they meant the same. The second is reading everyone loves someone as a claim about one person. The English is ambiguous, and the formulas aren't. And the third is forgetting that the universe belongs to the claim. If a verdict depends on the size of the grid, say which size you meant.

@chapter Try it
@words text="“Everyone loves someone, so there is someone whom everyone loves.”"
Here's one to try. Everyone loves someone, so there's someone whom everyone loves. Build a small universe where the premise is true and the conclusion is false. Hint: think of four people standing in a ring.

@art column-and-rows
Draw it as a grid, and check two things. Every row needs at least one lit cell. And no column may be lit all the way down. One grid like that is all the invalidity takes.

@end text="Click a cell, watch the verdicts"
You can click cells on the grid and watch all six orders change, on Learn. That's learn dot get er done dot I O.
