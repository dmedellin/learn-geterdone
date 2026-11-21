---
format: long
lesson: code-complete-variables/the-power-of-variable-names
title: Name the problem, not the arithmetic: the power of variable names
thumb: Say what it stands for
---

@chapter The question
@title text="The Power of Variable Names" sub="Code Complete, chapter 11" art=thumb
To someone reading your code, a variable is its name. They can't see what you meant, only what you wrote. Chapter eleven is about choosing that name with care.

@quote text="Code is read far more times than it is written. Be sure that the names you choose favor read-time convenience over write-time convenience." cite="McConnell, Code Complete, 2nd ed., Chapter 11, p. 289"
Here's the key point. Code is read far more times than it is written. Be sure that the names you choose favor read time convenience over write time convenience.

@chapter Say it in words
@art say-it-in-words
The most important rule: a name should fully and accurately describe what the variable represents. The technique is to say it in words. The number of seats in a stadium. The current date. That statement is often the best name.

@words text="What, not how" sub="employeeData, not inputRec"
And a good name speaks to the problem rather than the solution. What, not how. Employee data is about the problem. Input rec is about the program.

@list heading="Two conventions" items="Qualifiers at the end: revenueTotal, expenseTotal@at the end|Precise opposites: first and last, min and max@opposites"
Two conventions help. Put a computed value qualifier like total, max or average at the end of a name, so revenue total and expense total read alike. And use opposites precisely: first with last, min with max.

@chapter How long?
@art name-lengths
On length, the book reports a study. Gorla, Benander and Benander, in nineteen ninety, found the effort to debug a program was lowest when its names averaged ten to sixteen characters. Programs averaging eight to twenty were almost as easy.

@words text="Best: 10 to 16 · almost as good: 8 to 20" sub="an average, not a rule for every name"
McConnell is careful with it. It doesn't say every name should be that long. It says if you see lots of shorter names, check they're as clear as they need to be. And short names have their place. The shorter the scope, the shorter a name can be.

@chapter Kinds of data
@art loop-crosstalk
In a short loop, i, j and k are fine. In a nested loop, names like team index are clearer, and they prevent index cross talk, writing i where you meant j.

@list heading="More names" items="Never call a status variable flag@flag|temp: you haven't understood it yet@temp|Booleans: plainly true or false@true or false|Constants: what they stand for@constant"
A status variable should never be called flag. A variable called temp is often a sign you haven't yet understood what it holds. A boolean should be plainly true or false, like done or found, and positive, not not found. And name a constant for what it stands for, not its value.

@art one-convention
Conventions settle the small decisions once, for the whole program, so the same thing isn't called point total here and total points there. A convention's power comes from existing, more than from its particular choices.

@chapter Measure the names
@art blank-tags
Now the lab. It lists the names a routine declares, and flags any shorter than eight characters, the low end of the range the study found almost as good.

@code block=1 lines=1-9 label=Java focus="1@calc|2@t|4@x|7@tmp"
Here's a routine named for its arithmetic. It's called calc. It takes a, n and r. It builds up t, using x, and returns tmp. Nothing in it says what it computes.

@math heading="Named for the arithmetic" items="a, n, r, t, x, tmp (i left out)@leaves out;;total = 1 + 1 + 1 + 1 + 1 + 3 = 8@eight characters;;mean = 8 ÷ 6 = 4/3 ≈ 1.33@four thirds"
The lab leaves out the loop index i, as the chapter allows. The other six names total eight characters, so the mean length is eight over six, four thirds, about one point three three. And all six are under eight characters.

@code block=2 lines=1-9 label=Java focus="1@average net price|2@net total|4@net price|7@average net"
Now the same routine, named for its problem. Average net price, from gross prices, a price count and a net factor. Inside, net total, net price, and average net. Now it says what it's for.

@math heading="Named for the problem" items="11 + 10 + 9 + 8 + 8 + 10 = 56@fifty six;;mean = 56 ÷ 6 = 28/3 ≈ 9.33@twenty eight thirds;;under eight characters: none@none"
The six counted names total fifty six characters. That's a mean of twenty eight thirds, about nine point three three, and none is under eight.

@art clear-tags
The study's figure is an average over a whole program, and the lab's list is its own reading of it, name by name. A list of short names is a list to look at. And i in a short loop is one you'll look at, and keep.

@chapter Where people slip
@list heading="Common slips" items="Longer is always better@The first|Letting a prefix stand in for a name@The second|Abbreviating to save time@the third"
The first slip is thinking longer names are always better. The study found a range, not a direction. The second is letting a prefix stand in for a name. And the third is abbreviating to save time. It saves the writer a few keystrokes, and costs every reader the decoding.

@chapter Try it
@code block=3 lines=1-8 label=Java focus="1@simple interest|2-3@short name"
Your turn. This routine computes the simple interest on a loan. List its names and their lengths, leaving out i, and find the mean. Then rename the routine and every short name for what it stands for, and say which names are still under eight characters.

@end text="Name it for the problem"
You can paste a routine into the lab and measure its names, on Learn. That's learn dot get er done dot I O.
