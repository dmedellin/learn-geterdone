---
format: long
lesson: code-complete-statements/unusual-control-structures
title: Early returns, recursion and goto: when they help
thumb: 2,692,537 calls for one answer
---

@chapter The question
@title text="Unusual Control Structures" sub="Code Complete, chapter 17" art=thumb
Which control structures are safe to use, and when? Chapter seventeen takes three that sit somewhere between the leading edge and the discredited, and sometimes in both camps at once. Early returns, recursion, and the goto.

@chapter Early returns
@quote text="Multiple returns can enhance a routine’s readability and maintainability, and they help prevent deeply nested logic. They should, nevertheless, be used carefully." cite="McConnell, Code Complete, 2nd ed., Chapter 17, p. 410"
That's the chapter's first key point. Multiple returns can enhance a routine's readability and maintainability, and they help prevent deeply nested logic. They should, nevertheless, be used carefully.

@art nested-staircase
Use a return when it makes the routine easier to read, when the answer's known and nothing's left to clean up. Without that, error checks pile up, and the nominal path ends up indented inside every one of them.

@art guard-gates
Guard clauses fix that. They're early returns that check the error cases first. Each enclosing condition becomes its own negation at the top, returning what the routine returns when it fails.

@code block=1 lines=1-9 label=Java focus="2-4@file is null|5-7@can't read|8@nominal case"
Here's a small routine written for the lesson. If the file is null, return empty. If you can't read it, return empty. Then the nominal case ends the routine, unindented. There are still three decision points, but the deepest statement went from inside two ifs to inside one.

@words text="Still more readable, by a small margin" sub="once each guard has to set an error status"
McConnell is careful about the gain. Once each guard has to set an error status before it returns, the code before the nominal path grows. His verdict is that the guard version still wins, but only by a small margin. And keep returns few, because a reader at the bottom can miss one above.

@chapter Recursion
@art recursion-tree
Recursion isn't useful often, the book says, but used judiciously it gives elegant solutions, as in a sort or a maze search. Make sure it stops, with a path that doesn't call itself. Use a safety counter where that's not simple. Keep it in one routine, and watch the stack.

@code block=2 lines=1-6 label=Java focus="2-4@base case|5@calls itself twice"
Then comes the warning. Don't use recursion for factorials or Fibonacci numbers. Here's the recursive Fibonacci. It has a base case, so it stops. But every call above it calls itself twice.

@math heading="Fibonacci of 30" items="calls: 2,692,537@two million;;deepest: 30@thirty deep;;value: 832,040@eight hundred;;loop: 29 passes@twenty nine"
The lab counts it. Fibonacci of thirty takes two million, six hundred and ninety two thousand, five hundred and thirty seven calls, never more than thirty deep, for the value eight hundred and thirty two thousand and forty. The loop gets there in twenty nine passes.

@code block=3 lines=5-12 label=Java focus="5-6@two variables|7@one pass"
Here's that loop. Two variables, older and newer, and one pass for each step. Fibonacci of forty is worse for recursion: three hundred and thirty one million, one hundred and sixty thousand, two hundred and eighty one calls, against thirty nine passes. The depth was never the problem. The number of calls was.

@art loop-wheel
Factorial of ten is the mild case, ten calls against nine passes. And the book's conclusion isn't to avoid recursion. It's more powerful than the textbook examples suggest. Just consider iteration and an explicit stack before you choose it.

@chapter The goto
@art goto-jump
The goto section gives both sides. Against it, goto code is harder to format, analyse and optimize, and once a few are allowed, more follow. For it, careful use can avoid duplicate code or release resources in one place. McConnell's own view is that almost every goto can be replaced, and the rare right one should be documented.

@art fenced-path
The chapter closes by noting that the field has advanced largely by restricting what programmers may do. McConnell views unusual control structures with strong skepticism.

@chapter Where people slip
@list heading="Common slips" items="Treating recursion as natural for Fibonacci@The first|Insisting on exactly one return@The second|Taking the warning as a ban on recursion@the third"
The first slip is treating recursion as the natural way to compute Fibonacci. The definition is recursive. The computation needn't be. The second is insisting on exactly one return per routine. And the third is reading the warning as a rule against recursion, when it's about two textbook examples.

@chapter Try it
@code block=4 lines=1-9 label=Java focus="3-4@guard clauses|5@total"
Your turn. Rewrite refund amount with guard clauses, so returning the order's total comes last and unindented. Then count the decision points and the deepest nesting, before and after.

@end text="Count the calls yourself"
You can run Fibonacci both ways in the recursion lab, on Learn. That's learn dot get er done dot I O.
