---
format: long
lesson: code-complete-high-quality-code/exceptions-and-barricades
title: The barricade: where to validate, and where to assert
thumb: Validate at the wall
---

@chapter The question
@title text="Exceptions and Barricades" sub="Code Complete, chapter 8" art=thumb
The last lesson left a question open. Which checks should be error handling, and which should be assertions? The second half of chapter eight answers it with one design idea, the barricade. But first, a mechanism.

@chapter Exceptions
@art thrown-up-chain
An exception lets code that doesn't know what to do about an error throw it up the calling chain, to code that might. Its great benefit is that an error can't be silently ignored. Its cost is that callers must know what a routine may throw, which weakens encapsulation.

@list heading="Using exceptions" items="Only for the truly exceptional@truly exceptional|At the interface's level of abstraction@level of abstraction|Facts in the message@message|No empty catch blocks@empty catch|Standardise their use@Standardise"
So throw only for conditions that are truly exceptional, not to pass the buck on an error you could handle locally. Throw at the level of abstraction of the routine's interface. Put the facts that led to the exception in its message. Don't write an empty catch block. And standardise how the project uses them.

@art leaking-detail
The book's example of the wrong level: an employee class whose tax id routine lets an end of file exception escape. Now every caller knows employees are stored in a file. Throw an exception at the employee's own level instead.

@chapter The barricade
@art watertight-hull
Section eight point five is the barricade. Like the watertight compartments of a hull, it confines damage. Choose certain interfaces as the boundary of a safe area. The code there checks and cleans whatever crosses it, and the code inside assumes the data is good.

@quote text="Routines inside the barricade should use assertions, because the data passed to them is supposed to be sanitized before it’s passed across the barricade." cite="McConnell, Code Complete, 2nd ed., Section 8.5, p. 205"
That makes the rule clean cut. Routines inside the barricade should use assertions, because the data passed to them is supposed to be sanitized before it's passed across the barricade.

@art operating-room
The book compares it to an operating room, where everything is sterilised before it goes in. Outside, error handling. Inside, assertions. And bad data found inside is an error in the program, not in the data. The same idea works for one class: public routines check, private ones assume.

@chapter Development and production
@words text="Program offensively" sub="in development: make failures loud"
In development, program offensively. Make asserts abort and failures loud, so they get fixed. Then plan to remove the debugging aids without editing the code by hand.

@list heading="In production" items="Keep checks for important errors@important errors|Drop the trivial ones@trivial|Fail gracefully@gracefully|Make messages friendly@friendly"
In production, keep the checks for important errors and drop the trivial ones. Keep what lets a program fail gracefully. Engineers on the Mars Pathfinder diagnosed a fault after landing with debug code they'd left in. And make your messages friendly. One of McConnell's own once called a user Dog Breath.

@chapter Apply the rule
@art six-values
The lab applies the rule to six values in an order system. Each record says where a value comes from, outside or inside, and what the design does with it: validate, assert, or nothing.

@list heading="The mixed design" items="uploadName: outside, unchecked@upload name|feedPrice: outside, only asserted@feed price|customerId: inside, unchecked@customer id"
In the mixed design, three values break the rule. The upload name arrives from outside, and nobody checks it. The feed price comes from a supplier's feed, outside, and is only asserted, so a bad price is never handled. And the customer id is inside and unchecked, where an assertion should state what the barricade promised.

@words text="Barricaded: all four lists empty" sub="checks everywhere: 3 inside values validated"
In the barricaded design, the three outside values are validated and the three inside are asserted, and all four lists are empty. And in checks everywhere, all six are validated, so three inside values are flagged.

@chapter Where people slip
@list heading="Common slips" items="Checking everything everywhere@The first|An empty catch in code that works@The second|Stripping every debugging aid@the third"
The first slip is thinking defensive programming means checking everything everywhere. The second is leaving an empty catch block in code that works. Either the try is wrong to throw, or the catch is wrong to ignore it. And the third is stripping every debugging aid from production.

@art fat-checks
On that first slip, the chapter's last advice is to be defensive about defensive programming. Code that checks everything everywhere is fat and slow, and its own checks can be wrong.

@chapter Try it
@words text="9 values in an order system" sub="validate · assert · neither"
Your turn. The lesson lists nine values in an order system, from a quantity typed into a form to a date parsed from an email. Mark each one validate, assert or neither by the barricade rule, give a reason for each, and say which one is open to argument.

@end text="Place your own barricade"
You can type your own values into the lab and apply the rule, on Learn. That's learn dot get er done dot I O.
