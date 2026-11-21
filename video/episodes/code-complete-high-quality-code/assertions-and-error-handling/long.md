---
format: long
lesson: code-complete-high-quality-code/assertions-and-error-handling
title: Handle what you expect, assert what can never happen
thumb: Test both ends
---

@chapter The question
@title text="Assertions and Error Handling" sub="Code Complete, chapter 8" art=thumb
What does it mean to program defensively? Chapter eight answers with an analogy from the road.

@art defensive-driving
Think of defensive driving. You can't be sure what other drivers will do, so you arrange not to be hurt, even when it's their fault. A routine passed bad data shouldn't be hurt by it either, even when the data is another routine's fault.

@art garbage-filter
Garbage in, garbage out, the book says, isn't good enough for production software. A good program never puts garbage out.

@list heading="Garbage in" items="Check all data from external sources@external sources|Check a routine's input parameters@input parameters|Decide how to handle bad inputs@decide"
It names three ways to handle garbage in. Check the values of all data from external sources. Check the values of a routine's input parameters. And decide how to handle bad inputs. The best defence of all is not inserting errors in the first place.

@chapter The rule
@art two-doors
Section eight point two introduces the assertion, and with it the rule that settles most of the chapter. Use error handling code for conditions you expect to occur. Use assertions for conditions that should never occur.

@words text="Error handling: bad input · Assertion: a bug"
Error handling checks for bad input. An assertion checks for a bug. When an assertion fires, the fix is to change the source and release a new version.

@list heading="Using assertions" items="No executable code inside them@executable code|State preconditions and postconditions@preconditions|In big systems, assert and handle@assert and then"
Keep executable code out of assertions, since they may be compiled out. Use them to state preconditions and postconditions, after Meyer's design by contract. And in very large, long lived systems, assert and then handle the error anyway. In Java, an assert does nothing unless assertions are switched on.

@chapter Expected errors
@list heading="Some responses" items="Return a neutral value@neutral value|Substitute the closest legal value@closest legal|Log a warning@Log|Return an error code@error code|Shut down@shut down"
For an error you expect, section eight point three lists responses. Return a neutral value. Substitute the closest legal value. Log a warning. Return an error code. Or shut down.

@art robust-or-correct
Which is right depends on the program. A video game can paint a neutral colour. A machine that treats patients should stop. That's the choice between robustness, always doing something, and correctness, never returning an inaccurate result.

@quote text="The decision about how to handle bad inputs is a key error-handling decision and a key high-level design decision." cite="McConnell, Code Complete, 2nd ed., Chapter 8, p. 213"
Because that choice shapes the whole program, the key point says: the decision about how to handle bad inputs is a key error handling decision, and a key high level design decision. Decide it once, and follow it everywhere.

@chapter Test a range check
@art month-range
The most common defence against outside data is a range check. A month is valid from one to twelve, and the check should flag an invalid one. The correct check is month less than one, or month greater than twelve.

@math heading="The connective slip" items="month < 1 && month > 12@and where;;0: 0 < 1 true, 0 > 12 false → false@month zero;;13: 13 < 1 false, 13 > 12 true → false@month thirteen;;never true: 0 and 13 pass@never true"
Now write and where you meant or. Month zero: zero is less than one, true, but zero isn't greater than twelve, so the whole check is false. Month thirteen: the first part is false, so it's false again. No integer is below one and above twelve, so it's never true, and invalid months pass.

@art boundary-ticks
Swap it the other way, month at least one, or month at most twelve, and every integer satisfies one side. Now every month is flagged invalid. Neither mistake needs an unusual value. Six boundary tests, zero, one, two, eleven, twelve and thirteen, catch both.

@chapter Where people slip
@list heading="Common slips" items="Using an assertion to handle bad input@The first|Leaving error handling to each routine@The second|Testing only values far from the ends@the third"
The first slip is using an assertion to handle bad input. In Java it's off unless you switch it on, so it may check nothing. The second is leaving error handling to each routine, when it's a design decision. And the third is testing only values far from the ends. That's where the mistakes are.

@chapter Try it
@code block=1 lines=1-4 label=Java focus="3@returns"
Your turn. A score is valid from zero to a hundred, and this check returns true for a valid one. From its comparisons and its connective, find the integers it gets wrong, the boundary tests that expose it, and the fix.

@end text="Test a check at its ends"
You can type a check and its range into the lab and see where they disagree, on Learn. That's learn dot get er done dot I O.
