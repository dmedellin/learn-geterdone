---
format: long
lesson: code-complete-software-craftsmanship/self-documenting-code
title: Self-documenting code: which comments earn their place?
thumb: Five comments, zero news
---

@chapter The question
@title text="Self-Documenting Code" sub="Code Complete, chapter 32" art=thumb
What, in the end, documents a program? Chapter thirty two's first answer isn't comments.

@art style-docs
At the level of the code, the main contributor to documentation is programming style. Good structure, straightforward approaches, good names for variables and routines, named constants in place of literals, clear layout. Code that carries most of its own explanation is what McConnell calls self documenting. Comments come last, as a finishing touch.

@chapter The Commento
@art dialogue
Section thirty two point three is a dialogue, set at the end of a team's daily stand up. Its voices aren't all McConnell's. Callicles, the veteran, holds that comments make code harder to read, are less precise than code, and go out of date. Glaucon says refactoring removes most of his.

@art headings-scan
Ismene, who maintains other people's code, agrees that comments which repeat the code don't help. But she scans comments to find the part she needs, like headings in a technical book. And a comment that's hard to write is a sign the code isn't understood. Hers is the position the chapter develops.

@chapter Kinds of comment
@list heading="Six kinds of comment" items="A repeat of the code@repeat|An explanation of the code@explanation|A marker of unfinished work@marker|A summary@summary|A description of intent@intent|What the code cannot express@cannot express"
McConnell sorts comments into six kinds. A repeat of the code. An explanation of tricky code, which usually means the code should be clearer. A marker of unfinished work. A summary. A description of intent. And information the code cannot express, like a copyright or the source of an algorithm.

@quote text="Comments should say things about the code that the code can’t say about itself—at the summary level or the intent level." cite="McConnell, Code Complete, 2nd ed., Chapter 32, p. 817"
Only the last three belong in finished code. Comments should say things about the code that the code can't say about itself, at the summary level or the intent level.

@art intent-gap
Why intent above all? The book cites a six month study at IBM, where maintenance programmers said the hardest problem was understanding what the original programmer meant. And a poor comment, McConnell says bluntly, is worse than none.

@art repeat-comments
The book opens this section with three short routines, each with a comment. One comment is wrong. One repeats its code a statement at a time. Only the third, which names the method its routine uses, earns its place.

@chapter Count the comments
@code block=1 lines=1-12 label=Java comments=keep focus="1@line one|3-10@three, five, seven and ten|11@line eleven"
Here's a routine with plenty of comments. Lines three, five, seven and ten each restate the line under them. Line one restates the routine's name. All five repeat the code. None says what happens to an empty array, where line eleven divides zero by zero, and Java gives not a number.

@math heading="Comment density" items="average:  5 comments / 5 statements = 100%@five over five;;mean:  1 comment / 5 statements = 20%@one fifth"
The lab counts comment lines over statement lines. That routine is five over five, a hundred percent. The other preset, mean, has one comment over five statements. One fifth, twenty percent.

@code block=2 lines=1-8 label=Java comments=keep focus="1@one comment|7@divide by the length"
But that one comment says something the code can't. The caller guarantees at least one value, which is why line seven may divide by the length. It's intent, and information the code can't express. The density tells you nothing until you read the comments.

@words text="About 1 comment per 10 statements" sub="IBM studies, as Capers Jones reports them — not a quota"
On how many, the book reports IBM studies where clarity peaked at about one comment for every ten statements. But McConnell warns against turning that into a quota. Ask whether each comment earns its place, and the number looks after itself.

@chapter Techniques
@art rewrite-tricky
A few techniques. Avoid comments at the end of a line. For a paragraph of code, say why rather than how, and document surprises. Give units and allowed ranges on data. And don't comment tricky code. Rewrite it.

@chapter Where people slip
@list heading="Common slips" items="More comments mean better documentation@The first|Commenting tricky code to make it safe@The second|One comment in ten as a quota@the third"
The first slip is thinking more comments mean better documentation. A comment is judged by its kind. The second is commenting tricky code to make it safe, when the advice is to rewrite it. And the third is treating one comment in ten as a quota.

@chapter Try it
@code block=3 lines=1-5 label=Java comments=keep focus="1@first comment|3@second"
Your turn. Count is leap year's statement lines and comment lines, and compute its density. Mark the first comment and the second as a repeat, an explanation, a summary or intent. Then set its density beside the hundred percent routine's, and say what the comparison doesn't tell you.

@end text="Count a routine's comments"
You can check your counts in the size lab, on Learn. That's learn dot get er done dot I O.
