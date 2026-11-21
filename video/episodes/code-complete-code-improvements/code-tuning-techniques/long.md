---
format: long
lesson: code-complete-code-improvements/code-tuning-techniques
title: Code tuning techniques, and why you must measure each one
thumb: Fewer passes, not less time
---

@chapter The catalogue
@title text="Code-Tuning Techniques" sub="Code Complete, chapter 26" art=thumb
Once a measurement has found the hot spot, what can you change in it? Chapter twenty six answers with a catalogue, and warns at once that it's a list of things to try. Many won't work in your environment.

@art anti-refactor
McConnell calls these changes anti refactorings. Refactoring improves a program's structure. These make it worse in exchange for speed, by definition, because a change that improved both would simply be good practice.

@quote text="Results of optimizations vary widely with different languages, compilers, and environments. Without measuring each specific optimization, you’ll have no idea whether it will help or hurt your program." cite="McConnell, Code Complete, 2nd ed., Chapter 26, p. 645"
Every technique comes with the book's own timings, in several languages, and they disagree. Results of optimizations vary widely with different languages, compilers, and environments. Without measuring each specific optimization, you'll have no idea whether it will help or hurt your program.

@chapter Logic and loops
@list heading="Logic" items="Stop testing once you know@Stop testing|Order tests by how often they succeed@how often|Replace a complex expression with a table@table lookup|Compute lazily@lazily"
In logic, stop testing once you know the answer, which Java's and and or do for you. Order tests by how often they succeed. Replace a complicated expression with a table lookup. And compute a value lazily, only when it's needed.

@list heading="Loops" items="Unswitching@Unswitching|Jamming@jamming|Unrolling@unrolling|A sentinel value@sentinel|The busiest loop inside@busiest loop|Strength reduction@strength reduction"
In loops, unswitching moves a decision that never changes out of the loop. Jamming merges two loops over the same range. There's unrolling, and a sentinel value at the end of a search. The busiest loop goes on the inside. And strength reduction replaces a multiplication by the index with a running addition.

@art hoist-out
Minimising the work inside a loop often means spotting loop invariant work, a computation whose result is the same on every pass. Compute it once, before the loop, and you get the same result for less work.

@chapter Data, expressions, routines
@art data-shapes
For data, use integers rather than floating point, fewer array dimensions, fewer array references, supplementary indexes, and caching. For expressions, algebraic identities, cheaper operations, values computed in advance, and common subexpressions computed once. Putting a routine inline saves little on modern machines.

@chapter Count a nest
@art nested-loops
One technique the lab can count. The book's example is a nest whose outer loop runs a hundred times, and whose inner loop runs five times on each pass. Each time a loop's body begins counts as one pass.

@math heading="Busiest loop inside" items="100 outside, 5 inside:  100 + 500 = 600@a hundred outside;;5 outside, 100 inside:  5 + 500 = 505@five outside;;saved ≈ 15.8% of passes@fifteen point eight"
A hundred outside and five inside makes a hundred outer passes and five hundred inner ones, six hundred in all. Swap them, five outside and a hundred inside, and it's five plus five hundred, five oh five. That saves about fifteen point eight percent of the passes.

@math heading="Three levels: 50, 10, 2" items="as given:  1,550 passes@as given;;smallest outside:  1,022 passes@smallest outside;;body runs 1,000 either way@body runs"
The lesson's own nest has three levels, fifty, ten and two. As given, it makes one thousand five hundred and fifty passes. Smallest outside, one thousand and twenty two, about thirty four point one percent saved. The body runs a thousand times either way. Only the loops' bookkeeping shrinks.

@chapter Then measure
@words text="C++ 33% · Java 34% · PHP 12% · Python 4%" sub="the book's timings of the swap, 2004"
Now the timing. The book measured the swap. Thirty three percent less time in C plus plus, thirty four in Java, twelve in PHP, and four in Python. Those were its machines in two thousand and four, and the spread between them is the point.

@art stopwatch-pair
The lab counts passes, not time. In Java a just in time compiler may simplify loops itself, as an optimising C plus plus compiler may. So the count is a reason to try a change and measure it, not a prediction of what you'll see.

@art faster-machines
Between the editions, computers got so much faster that McConnell had to repeat most tests far more times to measure anything. For many programs, he says, this level of optimisation is now irrelevant, though not for embedded and real time work. An optimisation worth making is worth measuring.

@chapter Where people slip
@list heading="Common slips" items="16% fewer passes means 16% less time@The first|Tuning before measuring@The second|Moving work that isn't invariant@the third"
The first slip is thinking a technique that saves sixteen percent of iterations saves sixteen percent of time. The second is tuning before measuring, making code harder to read where speed was never the problem. And the third is moving work out of a loop that isn't the same on every pass, which changes what the loop does.

@chapter Try it
@code block=1 lines=1-4 label=Java focus="2@same on every pass|3@body runs"
Your turn. With n equal to a thousand, move the work that's the same on every pass out of this loop. Write the changed code. Say how many times the body runs and how many times tax rate is called, before and after. Then say what would tell you whether it's faster.

@end text="Count a nest's passes"
You can try loop orders in the nest lab, on Learn. That's learn dot get er done dot I O.
