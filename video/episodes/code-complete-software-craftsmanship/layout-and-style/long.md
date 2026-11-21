---
format: long
lesson: code-complete-software-craftsmanship/layout-and-style
title: Code layout: when indentation tells the wrong story
thumb: The compiler ignores it. You can't.
---

@chapter The problem
@title text="Layout and Style" sub="Code Complete, chapter 31" art=thumb
You've probably met this. An if with one statement and no braces, and later a second line added under it at the same indentation, because the indentation said that's where it belonged. It didn't. Java gives an unbraced if exactly one statement, and the second line runs every time.

@art two-readers
Layout is the one part of a program the compiler ignores and a reader can't. So a listing can tell the reader one story, and the compiler another.

@quote text="The first priority of visual layout is to illuminate the logical organization of the code." cite="McConnell, Code Complete, 2nd ed., Chapter 31, p. 775"
McConnell calls the rule that follows the Fundamental Theorem of Formatting. The first priority of visual layout is to illuminate the logical organization of the code. Looking good comes a distant second.

@chapter Why structure matters
@art chess-board
Why does structure matter so much to a reader? The book reports that chess experts remember positions far better than novices when the pieces stand as in a game, and hardly better when they're placed at random. Shneiderman found the same of programmers in nineteen seventy six. Experts carry a structure in their heads.

@words text="Consistency beats the details" sub="Hank and Tony swapped brace styles by the end"
So following a convention consistently matters more than its details. McConnell tells of Hank and Tony, who argued over brace placement for a whole project, and ended it each preferring the style the other had started with.

@list heading="A good layout scheme" items="Shows the logical structure accurately@accurately|Shows it consistently@consistently|Makes code easier to read@easier to read|Survives modification@survives modification"
Debates about layout sound like religious wars, so the chapter names its criteria. A good scheme represents the logical structure accurately, and consistently. It makes the code easier to read. And it survives modification, so changing one line doesn't mean changing several others.

@chapter White space
@art indent-levels
White space is the main tool. Blank lines divide a routine into paragraphs, and indentation puts each statement under the one it's subordinate to. In one study from nineteen eighty three, subjects scored twenty to thirty percent higher on comprehension with two to four space indentation than with none. Six spaces scored second lowest, though many felt it was easier.

@art block-styles
Then blocks. In Java, the braces are separate from the control statement, which is where trouble starts. You can emulate pure blocks, the style the book calls standard in Java. You can indent braces with the block. Or you can use endline layout, which McConnell rejects as inaccurate and hard to maintain.

@chapter The dangling else
@code block=1 lines=1-8 label=Java focus="2@line two|3@line three|5-6@the else on line five"
Read this as the indentation invites. Line two tests whether the user is active. Line three tests whether they want email. And the else on line five sits at the depth of line two, so it looks like an inactive user gets a letter.

@art else-binding
Java reads it differently. Neither if has braces, and an else belongs to the nearest if that doesn't have one, the one on line three. So an active user who doesn't want email gets a letter, and an inactive user gets nothing. The lab flags lines five and six as mis indented.

@code block=2 lines=1-6 label=Java focus="3@marked closed|4@archived"
Here's a second case. The if governs line three alone, so an account with a zero balance is marked closed. But line four, indented as if it belonged under the if, is just the next statement. Every account is archived. Nothing here is a syntax error.

@code block=3 lines=1-10 label=Java focus="2-8@braces|9@nothing about names"
The fix is the braces the book favours on group projects, even round a single statement. Now the structure is in the code, where the compiler reads it, and the indentation shows the same structure. The lab finds zero mis indented lines. That says only that layout and structure agree, nothing about names or correctness.

@chapter Where people slip
@list heading="Common slips" items="Thinking indentation is cosmetic@The first|Choosing the layout that looks best@The second|Treating one brace style as the right one@the third"
The first slip is thinking indentation is cosmetic. The compiler ignores it, and that's the problem. The second is choosing the layout that looks best, when showing the structure comes first. And the third is treating one brace style as the right one. The larger point is consistency.

@chapter Try it
@code block=4 lines=1-8 label=Java focus="2@first if|4@second if"
Your turn. Clamp should hold value between low and high, and log when it clamps from above. Without the lab, mark every line whose indentation disagrees with Java's structure. Say which statement each if governs, starting with the first if and the second if, and what happens when you compile it.

@end text="Check layout against structure"
You can paste it into the layout lab to check the lines you marked, on Learn. That's learn dot get er done dot I O.
