---
format: long
lesson: gof-document-editor/user-operations
title: Command in Lexi: requests as objects, with unlimited undo
thumb: Make the request an object
---

@chapter What users ask for
@title text="User Operations" sub="Design Patterns, Section 2.7" art=thumb
Some of Lexi's work happens right in the page, typing and selecting. The rest is reached through menus, buttons and keyboard shortcuts: open, save, print, cut, paste, fonts, quit. How should all those reach the operations behind them?

@list heading="Four requirements" items="Several interfaces per operation@several interfaces|Widgets don't depend on every operation@many classes|Undo and redo, but not save or quit@undoable|No fixed limit@no fixed limit"
The authors set four requirements. One operation may have several interfaces, a menu entry and a button for the same thing. The operations live in many classes, and the interface classes shouldn't come to depend on all of them. Most changes should be undoable and redoable, but not saving or quitting. And there should be no fixed limit on undo.

@chapter Three tries
@art menu-subclasses
The first idea is a subclass of the menu item for each operation. It's rejected: it ties the request to one kind of widget, so a button for the same request needs its own subclass, and the classes approach widget kinds times requests.

@art pointer-vs-object
A function pointer is closer. But it does nothing for undo, has nowhere to keep state, like which font to apply, and is hard to extend. An object does all three. So each request becomes a command, with one operation, execute. The menu item neither knows nor cares what it does. It just calls execute when it's chosen.

@quote text="Here we have another example of encapsulating the concept that varies, in this case a request." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Section 2.7"
In the authors' words: here we have another example of encapsulating the concept that varies, in this case a request.

@chapter Undo and the history
@code block=1 lines=2-17 focus="2-5@a second operation|9@saved|13-16@execute|17@unexecute"
Undo adds a second operation, unexecute, which reverses execute using whatever execute saved. This command, for an irrigation zone, saves the minutes it's about to overwrite. Execute stores the old value and sets the new one. And unexecute puts the old value back.

@art history-line
The history is the list of executed commands, with a line marking the present. To undo, unexecute the command left of the line and move the line left. To redo, execute the command to its right, and move the line right. The list's length is the only limit.

@words text="Reversible()" sub="a change that changes nothing costs no undo"
A third operation, reversible, lets a command report that it changed nothing, so a font change to the font that's already there doesn't cost the user an undo. The pattern is Command.

@chapter Two stacks
@art two-stacks
A list with a line in it is the same thing as two stacks: the commands left of the line on one, and the commands right of it on the other.

@code block=2 lines=2-15 focus="6@running a new command|7-10@to undo|11-14@to redo"
Running a new command executes it, pushes it, and clears the redo stack. To undo, pop, unexecute and push it onto the redo stack. To redo, the reverse. And an empty stack just refuses.

@chapter A garden week
@art two-zones
The lab runs a garden irrigation controller with two zones: front at twenty minutes, back at thirty. Boost adds ten to front. Trim takes five from back. Rain sets front to zero. And summer sets back to forty five.

@math heading="boost, trim, rain, undo, undo, redo, summer, undo" items="boost, trim, rain → front 0, back 25@boost;;undo rain → front 30 · undo trim → back 30@undo rain;;redo trim → back 25@redo trim;;summer → back 45 · rain discarded@summer;;undo summer → back 25@undo summer"
Boost, trim and rain run, leaving front at zero and back at twenty five. Undo rain gives front back its thirty. Undo trim makes back thirty. Redo trim makes it twenty five again. Then summer runs while rain waits to be redone, so rain is discarded. And undo summer brings back to twenty five.

@art redo-discarded
That's the redo lost at step seven. Commands right of the present line are only candidates, and a new command replaces them, as a new edit does in any editor.

@words text="front 30 · back 25" sub="undo: boost, trim · redo: summer"
The run ends with front at thirty and back at twenty five. Boost and trim are on the undo stack, summer alone on the redo stack, and nothing was refused.

@math heading="What the history holds" items="inverse commands: 1 value@one value;;snapshots: 3 commands × 2 zones = 6@snapshots"
And what must the history hold? As inverse commands, a set stores the one value it overwrote, and an add stores nothing, since it's undone by subtracting. That's one value, for summer. As snapshots of the whole state, each of the three commands holds both zones: six.

@chapter Where people slip
@list heading="Common slips" items="Binding operations to widgets@The first|Letting everything into the history@The second|Expecting redo to survive@And the third"
The first slip is binding each operation to the widget that triggers it. The second is thinking any operation can enter the undo history. Save and quit stay out. And the third is expecting redo to survive a new command. It doesn't.

@chapter Try it
@words text="rain · boost · undo · trim · redo · undo" sub="front 20 · back 30"
Your turn. The same controller, starting from front twenty and back thirty, with this script: rain, boost, undo, trim, redo, undo. Write the state and both stacks after each step, and count the redo entries discarded and the requests refused.

@end text="Step the history"
Then type the script into the lab and check, on Learn. That's learn dot get er done dot I O.
