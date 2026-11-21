---
format: long
lesson: gof-behavioral-requests/memento
title: Memento: undo without exposing an object's insides
thumb: Save it, sealed
---

@chapter Undo, without peeking
@title text="Memento" sub="Design Patterns, chapter 5" art=thumb
To undo a change, something has to remember how an object was. But objects hide their state, and they should. Memento is the Gang of Four's way out of that bind.

@quote text="Without violating encapsulation, capture and externalize an object's internal state so that the object can be restored to this state later." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 5"
That's the intent. Without violating encapsulation, capture and externalize an object's internal state, so that the object can be restored to this state later.

@art solver-shapes
The book's example is a graphical editor, where a constraint solver keeps connected shapes connected as they move. Undo a move by moving the shape back the same distance, and things may not land where they were, because the solver may have resolved the slack differently.

@words text="Ask for a memento before the move"
So the editor asks the solver for a memento before the move, and gives it back on undo. The solver restores its own equations and variables from it.

@chapter Three roles
@list heading="Participants" items="Memento@the memento|Originator@the originator|Caretaker@the caretaker"
The memento holds whatever part of the state the originator decides to put in it, and lets no one else at it. The originator makes a memento of where it stands, and later resets itself from one. And the caretaker keeps the memento, and never looks inside.

@code block=1 lines=1-16 label=Java focus="4@save|6@restore|10-15@private"
Here's the lesson's map tile viewer. Its state is a zoom and a position. Save returns a snapshot. Restore resets the view from one. And the snapshot's fields and constructor are private, so only the enclosing tile view can make one or read it. That's the wide interface.

@code block=2 lines=1-13 label=Java focus="4@its stack|6@checkpoint|8-12@on undo"
The caretaker is a view history. Each checkpoint pushes a snapshot onto its stack, and it hands them back on undo. It sees only the type, the narrow interface, so it can't look inside one.

@art caretaker-shelf
The pattern fits when two things hold together: an object must be put back to an earlier state, and handing that state out through ordinary getters would show other objects how it's built.

@chapter The costs
@list heading="Consequences" items="Preserves encapsulation@preserves|Simplifies the originator@simplifies|May be expensive@expensive|Narrow interfaces are hard in some languages@some languages|Hidden caretaking costs@hidden costs"
Five consequences, and the authors are candid. It preserves encapsulation. It simplifies the originator, which no longer keeps every version. But mementos may be expensive, if there's a lot of state, or they're made often. Some languages make the two interfaces hard to enforce. And there are hidden costs in caring for them.

@art heavy-memento
That last one is subtle. The caretaker can't see how much state a memento holds, so a light caretaker can carry a heavy load. The answer: when mementos come back in a predictable order, as on a command history, each can store only the change.

@chapter Count it
@math heading="The tile viewer: zoom 3, x 120, y 80" items="nearer, nearer: zoom 4, then 5@zoom in twice;;east: x 160 · home: x 0 · level: y 0@moves east;;undo level: y 80@undo the level;;farther: zoom 4 · level is discarded@zooms out"
In the lab, the view starts at zoom three, x a hundred and twenty, y eighty. Zoom in twice, to five. It moves east to a hundred and sixty, goes home to nought, and levels y to nought. Undo the level, and y is eighty again. Then it zooms out, to four, which discards the level from the redo stack.

@art snapshot-vs-inverse
That leaves five commands on the undo stack. Full snapshots keep every cell on every entry: five times three, fifteen values. Inverses keep only what a set replaced. Adds undo by subtracting. So that's one value, the hundred and sixty that home overwrote.

@words text="15 values vs 1" sub="a quiz's six players: 30 vs 2"
With a quiz app's six players, it's thirty against two. That's the warning about expensive mementos, in a number. But it isn't a verdict on snapshots. An inverse is exact here only because adding whole numbers is exactly reversible. The solver's effects aren't.

@chapter Where people slip
@list heading="Common slips" items="Opening the state so undo can save it@The first|Assuming a memento is cheap@The second|Undoing by an inexact inverse@And the third"
The first slip is opening the originator's state with getters and setters, so undo can save it. The second is assuming a memento is cheap because the caretaker is. And the third is undoing by inverse where the inverse isn't exact, the book's own motivating case.

@art restore
Memento also links back. A command can keep its undo state in one, and Iterator's own implementation section calls its cursor a simple memento.

@chapter Try it
@words text="A parcel locker bank" sub="free 12 · held 0 · fee 3 · drop drop surge pick undo"
Your turn. Three counters, free, held and fee. Drop adds one to held, pick takes one away, and surge sets the fee to five. Run the script, give the final state and both stacks, and count the values kept under each scheme.

@end text="Snapshots or inverses?"
Then switch schemes in the lab and check, on Learn. That's learn dot get er done dot I O.
