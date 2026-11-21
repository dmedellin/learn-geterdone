---
format: long
lesson: code-complete-high-quality-code/reasons-to-create-a-routine
title: Why write a routine? Not mainly to avoid repeating yourself
thumb: Reduce complexity first
---

@chapter The question
@title text="Reasons to Create a Routine" sub="Code Complete, chapter 7" art=thumb
Why do routines exist? If you learned the way Steve McConnell did, you'd say: to avoid duplicate code. As an undergraduate, he says, that's what his textbook told him, and it said little else. Chapter seven is his fuller answer.

@words text="The greatest invention after the computer"
He doesn't undersell it. The routine, he says, is the single greatest invention in computer science, after the computer itself.

@chapter The reasons
@art hide-behind-name
Section seven point one starts with the reason it calls the single most important. To reduce complexity. You hide information behind a routine, so you don't have to think about it.

@list heading="More reasons" items="An understandable abstraction@abstraction|Avoid duplicate code@duplicate code|Hide sequences@sequences|Improve portability@portability|Simplify boolean tests@boolean|Improve performance@performance"
Then come the others. Introducing an intermediate, understandable abstraction, like one well named call in place of eight lines of loop. Avoiding duplicate code. Hiding sequences. Improving portability. Simplifying complicated boolean tests. And improving performance.

@art one-line-guard
Notice what's not on the list. Making every routine small. And no operation is too simple. The chapter's example is a one line unit conversion, repeated in a dozen places, that later needed a check for division by zero. Because it had become a routine, it got that check once.

@chapter Cohesion
@quote text="You can classify routines into various kinds of cohesion, but you can make most routines functionally cohesive, which is best." cite="McConnell, Code Complete, 2nd ed., Chapter 7, p. 186"
Section seven point two is about cohesion, how closely the operations inside a routine are related. The key point: you can classify routines into various kinds of cohesion, but you can make most routines functionally cohesive, which is best.

@art cohesion-scale
The idea comes from a nineteen seventy four paper by Wayne Stevens, Glenford Myers and Larry Constantine, and the book keeps it as the workhorse heuristic at the level of a single routine. The kinds run from strong to weak.

@list heading="Kinds of cohesion" items="Functional: one operation@Functional|Sequential: steps passing data along@Sequential|Communicational: same data, otherwise unrelated@Communicational|Temporal: same time@Temporal|Procedural · logical · coincidental@unacceptable"
Functional cohesion, one operation, is the strongest. Sequential is steps that run in order and pass data along. Communicational is operations that share data and nothing else. Temporal is things grouped because they happen at the same time. And procedural, logical and coincidental are the unacceptable kinds.

@art flag-switch
Logical cohesion means operations picked by a flag passed in. McConnell suggests renaming it illogical cohesion. And he adds: learn the ideas, not the terms.

@chapter Names
@words text="A name says everything it does" sub="not handle · process · deal with"
Section seven point three is on names. A routine's name should describe everything it does. If that makes it long and silly, the cure isn't a vaguer name, it's a routine without side effects. And avoid verbs like handle, process and deal with.

@chapter Find the copy
@art copied-lines
Of all those reasons, duplication is the one a machine can see. The lesson's lab compares statement lines as text, with spacing collapsed, and reports any block of two or more lines that appears more than once.

@code block=1 lines=1-10 label=Java focus="3-5@lines three to five|7-9@seven to nine"
Here, one variable holds the shipping address, then the billing address. Lines three to five equal lines seven to nine. The lab reports one repeated block, six lines in its copies.

@code block=2 lines=1-10 label=Java focus="2-3@called twice|6-10@print address"
Extract the three lines as print address, called twice, and the lab finds nothing repeated. And now those three lines have a name, which says what they were for. That's the second reason on the list as much as the third.

@art extracted-routine
The new routine takes as its parameter exactly what the two copies differed in, the address. And the printer becomes two calls.

@code block=3 lines=1-10 label=Java focus="3-5@ship|7-9@bill"
But here's the catch. Write the same printer with two variables, ship and bill. The lab reports no repeated blocks at all. The copy is still there. The text differs, and the lab matches text. A count of duplicated lines is a lower bound, and a reason to look further.

@chapter Where people slip
@list heading="Common slips" items="Code used once needs no routine@The first|Two lines are too simple for a routine@The second|Leaving a side effect out of the name@the third"
The first slip is thinking code that isn't repeated needs no routine. Reducing complexity doesn't depend on repetition. The second is leaving a two line operation inline because it's simple. Small operations grow. And the third is keeping a name short by leaving out a side effect.

@chapter Try it
@code block=4 lines=1-10 label=Java focus="2-5@sales|6-9@refunds"
Your turn. Here's print summary. It prints the sales, then the refunds. Mark the repeated block by hand, and write the header of the routine that would replace it. Then name the cohesion of the six routines in the lesson's exercise.

@end text="Find the repeated block"
You can paste a routine into the lab and see the copies it finds, and the one it can't, on Learn. That's learn dot get er done dot I O.
