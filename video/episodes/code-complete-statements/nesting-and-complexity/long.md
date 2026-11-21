---
format: long
lesson: code-complete-statements/nesting-and-complexity
title: Nesting and complexity: count the decisions, then flatten
thumb: Moved, not removed
---

@chapter The problem
@title text="Nesting and Complexity" sub="Code Complete, chapter 19" art=thumb
Open the routine you least like to open. You'll probably find closing braces stacked down the right hand side, and somewhere in the middle, a statement that runs only when five conditions hold.

@quote text="Deep nesting makes a routine hard to understand. Fortunately, you can avoid it relatively easily." cite="McConnell, Code Complete, 2nd ed., Chapter 19, p. 460"
That's the second of chapter nineteen's key points. Deep nesting makes a routine hard to understand. Fortunately, you can avoid it relatively easily.

@chapter How deep is too deep
@art nested-braces
The book calls excessive nesting one of the chief culprits in confusing code. Studies by Chomsky and Weinberg, as Yourdon reports them, suggest few people can understand more than three levels of nested ifs. Many researchers recommend no more than three or four. These are other people's findings, from before two thousand and four, and your reviews can test them.

@list heading="Ways out of deep nesting" items="Retest part of a condition@Retest|Use a block you can break out of@break out|Convert to if-then-else or case@Convert|Factor into a routine@Factor|Use polymorphism, or redesign@polymorphism"
The remedies are a list. Retest part of a condition instead of nesting another if. Use a block you can break out of. Convert to a chain of if then else tests, or a case statement. Factor deep code into its own routine. Use polymorphism, or redesign. And from other chapters, status variables, exceptions and guard clauses.

@chapter Structured programming
@art three-constructs
The book traces structured programming to a paper Dijkstra presented in nineteen sixty nine. Its core is one in, one out constructs. Its thesis, credited to Bohm and Jacopini in nineteen sixty six, is that sequence, selection and iteration are enough to build any control flow. So break, continue, return and exceptions deserve a critical eye.

@chapter Counting decisions
@art decision-counter
Section nineteen point six argues that control structures are a large part of a program's complexity, measured as the number of things a reader must hold in mind at once. Then it presents Tom McCabe's nineteen seventy six measure.

@math heading="Decision points" items="1 for the straight path@start with one;;+1 each if, while, for, and, or@add one;;+1 each case@each case"
Start with one, for the straight path through the routine. Add one for each if, while, repeat, for, and, and or. And add one for each case of a case statement.

@list heading="Reading the count" items="0 to 5: probably fine@zero to five|6 to 10: think about simplifying@six to ten|10 and up: split part of it out@ten and more"
Zero to five, the routine's probably fine. Six to ten, start to think about simplifying. Ten and more, break part into another routine. That's guidance, not a grade. McConnell calls ten a warning flag, and a long case statement may be better left whole.

@chapter Count a routine
@art buried-branch
The lab counts a shipping cost routine written for the lesson, twenty two lines, with closing braces stacked down the right.

@code block=1 lines=1-22 label=Java focus="3-6@five ifs|12@a for|14@line fourteen"
Nine decision points, five ifs, a for, an and, an or, plus one. That's the six to ten band. Its deepest nesting is five, first reached on line fourteen, a return of minus one inside a restricted item check, with the domestic rules buried four levels down.

@art flat-guards
So flatten it with guard clauses, the transformation from the unusual control structures lesson, now on a routine where it moves a loop as well.

@code block=2 lines=1-12 label=Java focus="2-4@error cases|5-7@routine of its own|8-11@domestic rules"
Here are the same rules. The error cases return first. The international branch moves into a routine of its own, international cost. And the domestic rules come last, near the left margin.

@math heading="Before → after" items="nesting: 5 → 1@five to one;;decision points: 9 → 6@nine to six;;moved: for, if, ||@moved"
The nesting a reader holds at once fell from five to one. The decision points fell from nine to six, but for a different reason. The for, its if, and its or moved into international cost, where they still have to be read.

@art moved-boxes
That's the book's own point. Moving part of a routine into another doesn't reduce the program's overall complexity. It moves the decision points. What it does reduce is how much you have to juggle at one time.

@chapter Where people slip
@list heading="Common slips" items="Thinking flattening removes complexity@The first|Thinking a count of 11 means bad code@The second|Thinking guard clauses are the only cure@the third"
The first slip is thinking flattening reduces complexity. It reduces nesting, and moves the decisions. The second is thinking a count of eleven means the routine is bad. The count says where to look, and reading it decides. And the third is thinking guard clauses are the only cure. Which fits depends on why the code is nested.

@chapter Try it
@code block=3 lines=1-15 label=Java focus="3@is member|6@or|9@for|10@and"
Your turn. Count the decision points of discount percent, with a breakdown by keyword. There's an if for is member, an if with an or, a for over the coupons, and an if with an and inside it. Then find the deepest nesting, by hand.

@end text="Count a routine's decisions"
You can paste the routine into the complexity lab to check your count, on Learn. That's learn dot get er done dot I O.
