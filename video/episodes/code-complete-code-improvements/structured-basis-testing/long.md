---
format: long
lesson: code-complete-code-improvements/structured-basis-testing
title: Structured basis testing: how many tests does a routine need?
thumb: Every line ran. Not tested.
---

@chapter The question
@title text="Structured Basis Testing" sub="Code Complete, chapter 22" art=thumb
Your routine's tests all pass, and a coverage tool says they ran every line. Is it tested? Chapter twenty two is about the testing you do on your own code, and it starts by putting that testing in its place.

@art bathroom-scale
Testing is often a project's only quality technique, which the chapter calls unfortunate. It can never prove that no errors remain, and by itself it doesn't improve anything. McConnell's comparison: improving software by testing more is like trying to lose weight by weighing yourself more often.

@chapter Tests first
@quote text="Writing test cases before the code takes the same amount of time and effort as writing the test cases after the code, but it shortens defect-detection-debug-correction cycles." cite="McConnell, Code Complete, 2nd ed., Chapter 22, p. 533"
The book argues for writing tests first. Writing test cases before the code takes the same amount of time and effort as writing the test cases after the code, but it shortens defect detection debug correction cycles.

@words text="Think about requirements before you code" sub="a poor requirement is hard to write a test for"
Writing them first also makes you think about the requirements before you code. It exposes a poor requirement early, because a test for one is hard to write. McConnell calls it one of the most beneficial practices of its decade, and no panacea.

@chapter The developer's blind spots
@art clean-dirty
Developers have limits as testers. They tend to write clean tests, checking that the code works, rather than dirty ones looking for the ways it breaks. They believe their tests cover more than they do. And most take running every statement once as adequate.

@words text="Statement coverage: a good start" sub="Branch coverage: every condition true once and false once"
That's a good start, the book says. But a better standard is branch coverage, with every condition tested at least once true and once false.

@chapter The counting rule
@art branch-fork
Testing everything is impossible. So the art is choosing the few tests that tell you different things. Structured basis testing, despite what the book calls its hairy name, comes with a counting rule.

@math heading="Basis test cases" items="1 for the straight path@start with one;;+1 each if, while, repeat, for, &&, ||@add one;;+1 each case, +1 if no default@each case"
Start with one for the straight path through the routine. Add one for each if, while, repeat and for, and for each and and or. Add one for each case of a case statement, and one more if it has no default. That number is the fewest tests that can make every decision go each way.

@chapter Count a routine
@code block=1 lines=1-14 label=Java focus="4@the while and the and|6@line six|8@else if"
Here's overtime pay. The decisions are the while and the and on line four, the if on line six, and the else if on line eight, which counts as an if. The else alone counts nothing. One plus four is five.

@list heading="Five basis tests" items="count 0: loop never starts@count zero|count 1, null first entry@null first|one exempt employee@exempt|non-exempt, 45 hours@forty five|exactly 40 hours@exactly forty"
Five tests make each decision go both ways. Count zero, so the loop never starts. Count one with a null first entry. One exempt employee. One non exempt employee with forty five hours. And one with exactly forty, where the overtime test is false.

@art missed-branches
Now the coverage tool's verdict. One call with two employees, one exempt and one at forty five hours, runs every line. But it never tries a null entry, and never anyone at forty hours or under. Two of the eight decision outcomes go untested by a suite with full statement coverage.

@chapter The missing default
@code block=2 lines=1-18 label=Java focus="3-13@three cases|14@for express"
Shipping label has three cases and no default, then an if for express. That's one plus three, plus one for the missing default, plus one for the if. Six.

@art case-fan
The sixth test is a zone the switch doesn't name, like four, where the label stays empty. Whether that's right is a question for the specification, and only that test asks it.

@art test-first-loop
Test first has had a long life since. Kent Beck described test driven development: write one failing test, write just enough code to pass, tidy, repeat. Others write tests alongside the code. Either way, the basis count says how many tests the decisions need.

@chapter Where people slip
@list heading="Common slips" items="Full statement coverage means tested@The first|Taking the count as enough tests@The second|Counting else as a decision@the third"
The first slip is thinking full statement coverage means the routine is tested. The second is taking the count as enough. It's a minimum, and the tests must be chosen so each decision goes each way. And the third is counting else as a decision. Else if adds one. Else adds nothing.

@chapter Try it
@code block=3 lines=1-7 label=Java focus="2@for loop|3@or"
Your turn. Archive old has a for loop, and an if with an or in it. Count the basis test cases it needs by the rule, and write one input for each, so that every decision goes both ways.

@end text="Count a routine's tests"
You can paste the routine into the basis lab to check your count, on Learn. That's learn dot get er done dot I O.
