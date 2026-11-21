---
format: long
lesson: code-complete-code-improvements/refactoring-safely
title: Refactoring safely: count a block's ins and outs first
thumb: Two outs won't extract
---

@chapter The myth
@title text="Refactoring Safely" sub="Code Complete, chapter 24" art=thumb
You have a routine that totals an account's transactions, charges a fee for each overdraft, and prints the result. You'd like to pull the loop out into a routine of its own. Chapter twenty four starts further back, with a myth.

@art changing-code
The myth is that a well run project writes its code once, tests it, and forgets it until maintenance. In reality, code changes a great deal while it's first being written, because requirements change during development, and every requirement change reaches the code.

@quote text="Software can either improve or degrade as it’s changed. The Cardinal Rule of Software Evolution is that internal quality should improve with code evolution." cite="McConnell, Code Complete, 2nd ed., Chapter 24, p. 585"
So what matters is the direction. Software can either improve or degrade as it's changed. The Cardinal Rule of Software Evolution is that internal quality should improve with code evolution.

@chapter What refactoring is
@words text="Same behaviour, better structure" sub="Martin Fowler, 1999"
The tool is refactoring. In Martin Fowler's definition, it's a change to a program's internal structure that makes it easier to understand and cheaper to modify, without changing its observable behaviour. Fixing a defect or adding a feature isn't a refactoring, however loosely people use the word.

@art smells
Fowler calls the warning signs smells. Duplicated code. A routine that's too long. A parameter list that's too long. And many more, which the chapter gathers into a checklist.

@list heading="Five levels" items="Data: a named constant, a better name@Data|Statements: return as soon as you know@Statements|Routines: extract, inline, parameters@Routines|Classes and interfaces@Classes|Whole systems@whole systems"
The catalogue comes at five levels. Data, like replacing a magic number with a named constant. Statements, like returning as soon as you know the answer. Routines, like extract routine. Classes and their interfaces. And whole systems.

@chapter Ins and outs
@art block-in-out
Before you extract a block, count two things. In: the variables the block reads whose values were set before it. They become parameters. Out: the variables the block sets that are read after it. A Java method returns one value, so one out extracts directly, and two need another step.

@code block=1 lines=1-13 label=Java focus="11-12@two print statements"
Here's print statement. Take the two print statements on lines eleven and twelve. They read fees and balance, so that's two ins, and nothing after them reads anything they set. No outs. They extract cleanly, as print totals of fees and balance.

@code block=1 lines=1-13 label=Java focus="4-9@the loop|10-12@after it"
Now the loop, lines four to nine. It reads account, balance and fees, three parameters. And it sets balance and fees, which are both read after it. Two results.

@math heading="Three extractions" items="lines 11–12:  in fees, balance · out none@eleven and twelve;;lines 4–9:  in account, balance, fees · out balance, fees@four to nine;;lines 2–10:  in account · out balance, fees@two to ten"
Take lines two to ten, everything before the printing, and the ins drop to just account, because the block sets balance and fees itself. But the outs are still balance and fees. So eleven and twelve extract cleanly. Four to nine and two to ten each leave two results.

@art two-results
That's what the count is for. It tells you the cost before you start. One clean extraction, and two that need a small class holding both totals, or two routines, one per result.

@chapter Precautions
@art parking-lot
Save the code you start with. Keep each refactoring small, and do them one at a time. Keep a list of steps, and a parking lot for changes that can wait. Retest, add tests, and review.

@words text="One-line changes: 55% → 2% errors" sub="once one organisation began reviewing them"
Even small changes. Programmers' first attempt at a change is wrong more than half the time, the book reports. The chance of a bad change rises from one line changed to five. And one organisation that began reviewing one line changes saw their error rate fall from fifty five percent to two.

@art small-steps
When should you refactor? When you add a routine or a class, when you fix a defect, and in the modules everyone's afraid of. And in maintenance, in the parts you touch, leave each one better than you found it.

@chapter Where people slip
@list heading="Common slips" items="Thinking Extract Routine is always safe@The first|Calling any change a refactoring@The second|Skipping review for small changes@the third"
The first slip is thinking extract routine is always safe. It's clean only when the block leaves at most one result. The second is calling any change a refactoring. Tweaking broken code until it works, McConnell says, is hacking. And the third is skipping review for small changes.

@chapter Try it
@code block=2 lines=1-10 label=Java focus="2-5@lines two to five|7-9@lines seven to nine|6@lines two to six"
Your turn. Two extractions are proposed for print invoice. Lines two to five as a routine that totals the lines, and lines seven to nine as one that prints. Give each its ins, its outs and its call. Then say whether lines two to six would extract as cleanly, and why.

@end text="Count a block's ins and outs"
You can set the from and to lines in the extraction lab and check, on Learn. That's learn dot get er done dot I O.
