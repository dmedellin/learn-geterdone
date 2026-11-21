---
format: long
lesson: code-complete-variables/scope-span-and-live-time
title: Span and live time: two numbers for how long a variable stays in your head
thumb: Declare it just before you use it
---

@chapter The question
@title text="Scope, Span and Live Time" sub="Code Complete, chapter 10" art=thumb
How much of a program do you have to read to understand one variable? The second half of chapter ten says: less, if you keep it local, and keep its uses close together. And it turns that into numbers.

@quote text="Minimize the scope of each variable. Keep references to a variable close together. Keep it local to a routine or class. Avoid global data." cite="McConnell, Code Complete, 2nd ed., Chapter 10, p. 258"
Here's the key point. Minimize the scope of each variable. Keep references to a variable close together. Keep it local to a routine or class. Avoid global data.

@chapter Windows of vulnerability
@art nested-scopes
In Java, a variable can be known to a block, a routine, a class, or a whole package. The less of the program that knows a variable, the less of it you need to read to understand that variable.

@art vulnerability-window
The code between two references to a variable is what McConnell calls a window of vulnerability. New code can be added there that changes the variable by mistake. And a reader can forget what it holds.

@chapter Two measures
@list heading="Two measures" items="Span: lines between two consecutive references@span|Live time: first reference to last, both included@live time"
So he makes it measurable. A variable's span is the number of lines between two consecutive references to it. Its live time is the number of lines from its first reference to its last, both included.

@art span-vs-live
They're different. A variable used on every line from one to twenty five has spans of zero, and a live time of twenty five. One used only on lines one and twenty five has a span of twenty three, and the same live time. No one has found the number that separates good from bad. Smaller is better.

@chapter Measure a routine
@art top-heavy
Here's a shape you've seen many times. Every declaration piled at the top of a routine, and the lines that use them a screen further down.

@code block=1 lines=1-19 label=Java focus="2-4@three declarations|13@line thirteen|18@line eighteen"
The lesson's routine audits shipments. Three declarations at the top, set to zero, and the work further down. Take heaviest kilograms. It's declared on line three, then used on line thirteen and line eighteen.

@math heading="heaviestKg, declared at the top" items="lines 3, 13, 18@lines three;;spans: 13 − 3 − 1 = 9 · 18 − 13 − 1 = 4@thirteen minus three;;live time: 18 − 3 + 1 = 16@eighteen minus three"
Its references are on lines three, thirteen and eighteen. The spans are thirteen minus three minus one, which is nine, and eighteen minus thirteen minus one, which is four. Its live time is eighteen minus three plus one, sixteen lines. And nine of those lines have nothing to do with it.

@math heading="All three variables" items="spans: 6, 1 · 9, 4 · 10, 2@six and one;;average span = 32 ÷ 6 = 16/3 ≈ 5.33@thirty two over six;;average live time = 41/3 ≈ 13.67@forty one thirds"
Across all three variables, the six spans are six and one, nine and four, ten and two. That's thirty two over six, sixteen thirds, about five point three three. The live times average forty one thirds, about thirteen point six seven.

@code block=2 lines=1-19 label=Java focus="4@scanned|10-11@just before the second loop"
Now move each declaration down to the loop that uses it, and change nothing else. Scanned is declared just before the first loop. The other two, just before the second loop.

@math heading="Declared near use" items="average span = 7/3 ≈ 2.33@seven thirds;;average live time = 23/3 ≈ 7.67@twenty three thirds;;heaviestKg: 18 − 10 + 1 = 9@nine lines"
The average span falls to seven thirds, about two point three three. The average live time falls to twenty three thirds, about seven point six seven. And heaviest kilograms is live for nine lines, not sixteen. The program does exactly the same thing. What's different is how much of it you hold in your head at once.

@art near-use
That's the section's advice in practice. Initialise a loop's variables just before the loop. Group the statements that work on the same variables. Break a group out into its own routine. And start with the smallest scope, because it's much harder to make a global variable local than the reverse.

@chapter The other sections
@art milk-carton
The shorter sections each add a point. Don't assume a variable lasts longer than it does, like milk that's supposed to keep for a week. Binding later buys flexibility, at the price of complexity. And give each variable exactly one purpose.

@chapter Where people slip
@list heading="Common slips" items="Declaring everything at the top@The first|Treating span and live time as one measure@The second|Reusing a temporary for a second job@the third"
The first slip is declaring every variable at the top so it's easy to find. The second is taking span and live time for the same measure. And the third is reusing a temporary variable for a second job, like a page count that means an error when it's minus one. The book calls that an integer moonlighting as a boolean.

@chapter Try it
@code block=3 lines=1-13 label=Java focus="2-3@total and count|8-11@loop"
Your turn. For total and count, write down every span, the average over all four, and each live time. Then move both declarations below the four print calls, just before the loop, and compute them again.

@end text="Measure span and live time"
You can paste a routine into the lab and measure every variable, on Learn. That's learn dot get er done dot I O.
