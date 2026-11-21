---
format: long
lesson: code-complete-high-quality-code/routine-length-and-parameters
title: How long should a routine be, and how many parameters?
thumb: About seven, grouped
---

@chapter The problem
@title text="Routine Length and Parameters" sub="Code Complete, chapter 7" art=thumb
You've probably called a routine with its arguments in the wrong order. Nine of them, three ints in a row, and a compiler that's happy as long as the types line up.

@code block=1 lines=2-10 label=Java focus="5-9@prints one line|2-4@nine parameters"
Here's one. A routine that prints one line of an invoice, with nine parameters. The second half of chapter seven is about this: the shape of a routine from the outside, its length and its parameters.

@chapter How long?
@art pilgrim-ship
It opens with a joke. The Pilgrims, McConnell says, argued about the best maximum length for a routine all the way across the Atlantic, and never settled it.

@art routine-lengths
Then it reviews the studies. Several found larger routines no more error prone per line than small ones, and some found them cheaper to develop. One, at I B M, found routines over five hundred lines the most error prone.

@art long-scroll
The book's conclusion surprises people. A routine with a complex algorithm may be allowed to grow organically.

@words text="Up to 100 to 200 lines" sub="a line: neither a comment nor blank · careful past 200"
It may grow to a hundred to two hundred lines, counting lines that are neither comments nor blank. Past about two hundred, be careful, because none of the studies that favoured longer routines distinguished sizes beyond it. Length should follow from cohesion, nesting and decisions, not from a limit for its own sake.

@chapter Parameters
@list heading="Parameter rules" items="Input, modify, output order@input|Use every parameter@every parameter|Status or error variables last@status|Not a working variable@working variable|About seven at most@seven"
Interfaces between routines are among the most error prone parts of a program. So put parameters in input, modify, output order, and keep it consistent. Use every parameter. Put status or error variables last. Don't use a parameter as a working variable. And limit them to about seven, after Miller's nineteen fifty six paper.

@art grouped-parameters
And pass what the routine's abstraction needs. Whether to pass an object, or three of its fields, is settled by what the routine is about, not by a rule.

@chapter Functions
@quote text="Functions should be used only when the primary purpose of the function is to return the specific value described by the function’s name." cite="McConnell, Code Complete, 2nd ed., Chapter 7, p. 186"
Section seven point six draws the line between functions and procedures, and gives the key point. Functions should be used only when the primary purpose of the function is to return the specific value described by the function's name.

@art hidden-side-effect
A call like total equals total price of order reads like a value. It gives no sign that it also changes the order. If a reader has to open every function to learn what it does, the routine has lost what it was for.

@chapter Count it
@math heading="Nine parameters" items="lines 10 · code lines 9 · statement lines 8@ten lines;;comments 1 · parameters 9@one comment;;density = 1/8 = 12.5%@one eighth"
The lab counts the nine parameter version. Ten lines, nine of them code lines, the book's kind, and eight of those are statements, because a lone brace doesn't count as one. There's one comment and nine parameters. So the comment density is one eighth, twelve point five percent.

@art nine-to-three
Seven of the nine describe the invoice line or its tax. So they become an invoice line and a tax rule. And the currency and the switch for showing the S K U become a format.

@code block=2 lines=2-6 label=Java focus="2@Three parameters|3-5@four statement lines"
Here's the result. Three parameters. Six lines, five code lines, four statement lines. And the density doubles, to a quarter, twenty five percent, with no comment added, because the statements it divides by fell.

@words text="Counts parameters, not abstractions"
But the lab would print three just as happily for three grab bag objects. The grouping is right here because each object is something the routine is about. And both versions are far below a hundred lines, so nothing asks you to split either one for length.

@chapter Where people slip
@list heading="Common slips" items="Letting a function change state on the way@The first|Bundling any parameters to get under seven@The second|Reusing a parameter as a working variable@the third"
The first slip is letting a function change state on the way. The second is bundling any parameters just to get under seven. A grab bag hides the coupling it was meant to reduce. And the third is reusing a parameter as a working variable, so its name no longer means what it says.

@chapter Try it
@code block=3 lines=1-4 label=Java focus="1-2@schedule"
Your turn. Count the parameters of schedule. Find the ones that travel together, and write a header with fewer parameters that keeps what schedule is about. If a type from the Java library fits, use it.

@end text="Count a routine's parameters"
You can paste a routine into the lab and count its lines and parameters, on Learn. That's learn dot get er done dot I O.
