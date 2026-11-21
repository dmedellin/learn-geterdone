---
format: long
lesson: gof-behavioral-requests/command
title: Command: how undo and redo really work
thumb: A request you can undo
---

@chapter Requests as objects
@title text="Command" sub="Design Patterns, chapter 5" art=thumb
Every undo button you've ever pressed is probably built on this pattern. By the end, you'll be able to run a history of commands by hand, and say exactly why redo sometimes stops working.

@quote text="Commands are an object-oriented replacement for callbacks." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 5"
That sentence, from the applicability section, is the quickest way in. Commands are an object oriented replacement for callbacks. Where a procedural program registers a function to call later, Command registers an object.

@art menu-command
The motivation is a toolkit's problem. Buttons and menus must do something when chosen, but the toolkit's authors can't know what, or to which object. Only the application knows. So the request itself becomes an object, with an execute operation.

@chapter Who does what
@list heading="Participants" items="Command@the command|Concrete command@a concrete command|Client@the client|Invoker@the invoker|Receiver@receiver"
The command declares the interface. A concrete command binds a receiver to an action, and implements execute by calling it. The client creates the command and gives it its receiver. And the invoker holds the command, and calls execute when the time comes.

@art invoker-receiver
The invoker and the receiver never meet. A menu item and a toolbar button can share one command object, and the command can be swapped while the program runs.

@code block=1 lines=5-18 label=Java focus="6@the receiver|9-10@take places|14@what execute replaced|16-17@close deck"
Here's the lesson's ferry booking desk. The deck is the receiver. Take places has execute, which takes places, and undo, which gives them back. Close deck is different. It sets the free places to nought, so it keeps what execute replaced, and undo puts it back.

@chapter Five uses
@list heading="What a command lets you do" items="Configure an object@configure|Queue it or run it later@later|Undo it@undo it|Log it and replay@replayed|Compose transactions@compose large"
The authors list five uses. Configure an object with what it should do. Make a command now and run it later, or queue it. Undo it, with a second operation. Log it to disk, so it can be replayed after a crash. And compose large operations from small ones, like transactions.

@code block=2 lines=1-11 label=Java focus="5-7@in order|8-10@in reverse"
And a macro runs its parts in order, and undoes them in reverse. It has no receiver of its own. That's Composite, inside Command.

@chapter Two stacks
@art two-stacks
Undo is what the lab counts. A history keeps two stacks. Executing a command pushes it on the undo stack. Undo moves it to the redo stack. Redo moves it back. And any new command empties the redo stack.

@art ferry-deck
The ferry has thirty free car spaces and a hundred and twenty foot places. Car takes one space. Group takes six foot places. Storm sets the foot places to nought.

@math heading="The ferry script" items="car, car: cars 29, then 28@two cars;;group: foot 114@a group;;undo, undo: foot 120, cars 29@undo twice;;storm: foot 0 · 2 redo entries discarded@then storm;;redo: refused@redo is refused"
Run two cars, so twenty nine, then twenty eight. Then a group, a hundred and fourteen foot places. Undo twice: foot back to a hundred and twenty, cars to twenty nine. Then storm, foot nought. That new command discards the two redo entries. So the redo is refused.

@math heading="And then" items="undo, undo: foot 120, cars 30@two more undos;;undo: refused@third is refused;;redo: cars 29@final redo;;undo: car · redo: storm@ends with"
Two more undos: foot a hundred and twenty, cars thirty. The third is refused, there's nothing left to undo. And a final redo re-runs car, so twenty nine. It ends with car on the undo stack, and storm on the redo stack.

@chapter Where people slip
@art discard-redo
The first slip is keeping the redo stack after a new command. Those undone commands describe changes to a state that no longer exists. Redo them, and you'd apply them to the wrong state.

@list heading="Two more slips" items="The same command on the history twice@The second|Thinking undo needs a full copy@And the third"
The second is putting the same command object on the history twice. Close deck overwrites what it replaced every time it runs, so the authors copy such a command first. And the third is thinking undo needs a full copy of the state. An add undoes by subtracting.

@art macro
One last warning from the book. Repeated execute and undo can build up errors until the state drifts. The authors call that hysteresis, and their remedy is to store more in the command, through a Memento.

@chapter Try it
@words text="A thermostat at 20" sub="warm: +1 · eco: set 16 · warm warm eco undo warm redo undo"
Your turn. A thermostat target of twenty. Warm adds one. Eco sets sixteen. Step through warm, warm, eco, undo, warm, redo, undo, writing the target and both stacks after each.

@end text="Run the history"
Then type it into the lab and check, on Learn. That's learn dot get er done dot I O.
