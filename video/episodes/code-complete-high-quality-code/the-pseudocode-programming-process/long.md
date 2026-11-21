---
format: long
lesson: code-complete-high-quality-code/the-pseudocode-programming-process
title: Write the routine in English first, then fill in the code
thumb: Comments first, code beneath
---

@chapter The problem
@title text="The Pseudocode Programming Process" sub="Code Complete, chapter 9" art=thumb
You finish a routine. It compiles, it passes the tests you thought of. A week later you find one thing it was meant to do, and never does. The branch you meant to write, and didn't.

@words text="Forgetting part of a routine hardly ever happens"
Chapter nine claims a way of working that makes that rare. Forgetting to write part of a routine, it says, hardly ever happens if you use the process.

@quote text="The Pseudocode Programming Process is a useful tool for detailed design and makes coding easy. Pseudocode translates directly into comments, ensuring that the comments are accurate and useful." cite="McConnell, Code Complete, 2nd ed., Chapter 9, p. 234"
Here's the key point. The Pseudocode Programming Process is a useful tool for detailed design and makes coding easy. Pseudocode translates directly into comments, ensuring that the comments are accurate and useful.

@chapter Good pseudocode
@list heading="Good pseudocode" items="Precise English@precise English|No syntax from the language@no syntax|At the level of intent@level of intent|Low enough to code from@nearly automatic"
Section nine point two says what good pseudocode is. Precise English statements. No syntax from the programming language. Written at the level of intent, saying what the approach means, rather than how it'll be coded. And low enough that writing the code from it is nearly automatic.

@art review-steps
The benefits, the chapter says, are easier reviews, refinement in small steps, cheaper changes, and comments that cost nothing extra and stay accurate.

@chapter The process
@art design-then-code
Section nine point three is the process. First, design the routine. Check the prerequisites, state what it hides, its inputs and outputs, name it, and decide how to test it. Look for it in the libraries. Then write the pseudocode, from a header comment down, and check it.

@art comments-to-code
Then code it. Write the declaration, then the first and last lines. Turn the pseudocode into comments, and fill in the code beneath each one. If one comment grows too much code, make it a routine of its own.

@words text="Nothing is right just because it seems to work"
Then check it. Execute each path in your head, and know why each line works. Nothing, the chapter says, is right just because it seems to work.

@art compile-loop
Compile only when you believe the routine is right, and beware the habit the book calls just one more compile. Then step through it in a debugger, test it, clean it up, and repeat as needed. The chapter also names alternatives: test first development, refactoring, design by contract, and hacking.

@chapter A step with nothing beneath it
@art empty-step
The lab treats each comment inside a routine's body as a step, and flags any step with no code beneath it. The lesson's example finds a free slot in a table.

@list heading="Find a free slot" items="Start after the slot used last: 1 line@start at the slot|Look at each slot once: 2 lines@look at each|If free, remember it and return it: 3 lines@if the slot is free|If none is free, log the overflow: nothing@log the overflow|Return minus one: 1 line@return minus one"
Start at the slot after the one used last, one line. Look at each slot once, wrapping around the end, two lines. If the slot is free, remember it and return it, three lines. If no slot is free, log the overflow, nothing at all. And return minus one, one line. Five steps, seven statement lines.

@words text="A full table is reported to nobody"
The fourth step says the routine logs the overflow, and nothing under it does. A full table is reported to nobody. The process kept the promise in plain sight, which is why the gap can be found. Add one call to log a warning, and the lab finds no empty step.

@art intent-vs-code
There's a second point. The last step, return minus one, is pseudocode at the level of the language, not of intent. At the level of intent it would say the routine reports that no slot was found.

@chapter Where people slip
@list heading="Common slips" items="Deleting the pseudocode once it works@The first|Writing pseudocode in the language's terms@The second|Trusting it because it compiles@the third"
The first slip is treating pseudocode as a draft to delete once the code works. Delete the comments, and the missing log isn't missing from anything. The second is writing pseudocode in the language's own terms. And the third is trusting a routine because it compiles and seems to work.

@chapter Try it
@code block=3 lines=1-13 label=Java focus="3-4@read the current time|8-9@move it to the archive|10@remove it from the live list"
Your turn. This routine moves expired sessions to the archive. Read the current time once. For each session older than the limit, move it to the archive, and remove it from the live list. Find the step with no code beneath it. Then write the obvious one line fix, and ask whether it's actually right in Java.

@end text="Check a routine against its steps"
You can paste a routine into the lab and see which steps are empty, on Learn. That's learn dot get er done dot I O.
