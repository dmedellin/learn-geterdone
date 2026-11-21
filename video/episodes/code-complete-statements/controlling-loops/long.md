---
format: long
lesson: code-complete-statements/controlling-loops
title: Controlling loops: read the header before it runs
thumb: Count it before it runs
---

@chapter The problem
@title text="Controlling Loops" sub="Code Complete, chapter 16" art=thumb
You've probably written a loop that ran once too often. The array had ten entries, the loop asked for eleven, and the program stopped with an exception on a line that looked right.

@art fence-posts
Chapter sixteen calls loops one of the most complex parts of programming. Its pages are about keeping them simple enough that mistakes like that one show. And its last key point is a habit you can practise.

@quote text="Think through the loop carefully to verify that it operates normally under each case and terminates under all possible conditions." cite="McConnell, Code Complete, 2nd ed., Chapter 16, p. 389"
Think through the loop carefully to verify that it operates normally under each case and terminates under all possible conditions.

@chapter Choosing a loop
@art loop-tests
Loops come counted, continuously evaluated, endless, or as iterators. They also differ in where they test for completion, at the beginning, the middle or the end. That decides whether the body runs at least once.

@words text="Don't know the count? while" sub="Know it? for, with all control in the header"
Use a while loop when you don't know in advance how many times it'll run, and a for loop when you do. Prefer for when it fits, because all its control sits in the header. But keep the header for control, not a while loop's housekeeping.

@chapter Inside and out
@art black-box
Treat the inside of a loop like a routine, a black box whose controlling conditions you can read without looking in. Minimize the things that affect it. Enter from one place, with the initialization right before it.

@list heading="Entry, body, exit" items="Write an infinite loop as while (true)@while true|Brace the body; give it one job@one job|Make the ending obvious@ending obvious|Don't change a for loop's index to stop it@index"
Write an infinite loop as while true. Brace the body, keep its housekeeping together, and give it one job. Make sure the loop ends, and make the ending obvious. And don't change a for loop's index to stop it early. Use a while loop instead.

@chapter Endpoints and the index
@words text="First pass · a middle pass · last pass"
Two guidelines are the lesson's subject. Check the endpoints. Run the first pass, one in the middle, and the last pass in your head. And avoid code that depends on the index after the loop. It varies by language and between a normal and an early exit, so save what you need inside.

@code block=1 lines=1-4 label=Java focus="1@ten entries|2@less than or equal to ten|3@hourly ten"
Here's the classic mistake. An array of ten entries, numbered zero to nine. The loop runs while i is less than or equal to ten. The lab works it out from the header alone: eleven iterations, a last value of ten, and eleven after. So the eleventh pass asks for hourly ten, and Java throws.

@math heading="One character, three figures" items="i <= 10:  11 passes · last 10 · after 11@less than or equal;;i < 10:  10 passes · last 9 · after 10@strictly less"
Compare the two headers. With less than or equal, eleven passes, last ten, eleven after. Make it strictly less than ten, and it's ten passes, last nine, ten after. One character changed all three figures, not just the last pass.

@chapter Down, and never
@art count-down
Counting down from ten to zero inclusive, with a step of minus one, gives eleven iterations, a last value of zero, and minus one after the loop. The index ends one step past, in the direction of travel.

@art skipping-bound
Now start at zero, step by two, and loop while i is not equal to nine. It never ends. i takes only even values, nine is odd, and even when i wraps round past the top of Java's int, it stays even. With less than in the test, it would have stopped after five passes.

@chapter Length and nesting
@words text="15 to 20 lines at most" sub="from a programmer who values simple code"
Keep a loop short enough to see at once. The book says a programmer who values simple code will rarely write one longer than fifteen or twenty lines.

@art nested-loops
And limit nesting to three levels. Yourdon reports that beyond three, the ability to understand a loop falls sharply. These are guidelines from other people's experience, so your own code reviews can test them.

@chapter Where people slip
@list heading="Common slips" items="Thinking <= and < differ only at the end@The first|Thinking the index ends on its last body value@The second|Stopping a for loop by setting its index@the third"
The first slip is thinking less than or equal and less than differ only at the end. They change all three figures. The second is thinking the index ends on its last value in the body. It's left one step past. And the third is stopping a for loop by setting its index. The book calls that monkeying with the loop index.

@chapter Try it
@code block=2 lines=1-3 label=Java focus="1@starts at ten"
Your turn. This loop starts at ten, runs while i is greater than zero, and steps by minus three. From the header alone, say how many times the body runs, the last value it prints, and what an index declared before the loop would hold after it.

@end text="Read a loop from its header"
You can type the header into the loop lab and check all three, on Learn. That's learn dot get er done dot I O.
