---
format: long
lesson: code-complete-code-improvements/code-tuning-strategies
title: Code tuning: measure before you make anything faster
thumb: Ten times faster, 9% saved
---

@chapter The suspect
@title text="Code-Tuning Strategies" sub="Code Complete, chapter 25" art=thumb
Your program is slow, and you have a suspect. The formatting routine, with its string building, which you've always thought wasteful. Chapter twenty five asks first whether the code is the place to look at all.

@art card-reader
McConnell's own example is a camera whose software made him upload pictures one at a time. He replaced it with a card reader that copied them all at once. He didn't care whether the reader's code was faster, because his throughput was. Performance isn't the same as code speed.

@list heading="Look here first" items="Requirements@requirements|Program design@design|Class and routine design@classes and routines|The operating system@operating system|The compiler@compiler|The hardware@hardware|Code tuning, last@last"
Before code, the chapter lists six other places to look. The requirements, where a target is often stated that nobody needs. The design. The design of classes and routines. Dealings with the operating system. The compiler. And the hardware. Code tuning comes last.

@chapter Where the time goes
@quote text="Most programs spend most of their time in a small fraction of their code. You won’t know which code that is until you measure it." cite="McConnell, Code Complete, 2nd ed., Chapter 25, p. 608"
That's the chapter's key point. Most programs spend most of their time in a small fraction of their code. You won't know which code that is until you measure it.

@art hot-spots
The book reports Barry Boehm's figure, that twenty percent of a program's routines consume eighty percent of its time. And Donald Knuth's, that less than four percent of a program usually accounts for more than half its run time. Those were their programs. Your profile is what applies to yours.

@chapter Old wives' tales
@list heading="Old wives' tales" items="Fewer lines run faster@Fewer lines|Some operations are probably faster@probably faster|Optimise as you go@as you go|Speed matters as much as correctness@as much as correctness"
The chapter takes apart four beliefs. That fewer lines of source run faster. That some operations are probably faster than others, when the answer changes with every compiler and machine. That you should optimise as you go. And that speed matters as much as correctness.

@words text="Rule 1: Don't. Rule 2 (experts only): Not yet." sub="M. A. Jackson's rules of optimisation"
Nobody can tell which small part will be the bottleneck until the program works. M A Jackson's rules make the point drily. The first is don't. The second, for experts only, is not yet.

@art matrix-surprise
And measure, always. McConnell once rewrote a matrix summing routine with pointers, sure he'd saved thousands of multiplications. He measured it to enjoy the result. No improvement at all, at any size, because the compiler was already doing the same thing. Tuning without measurement reliably produces harder code.

@chapter The arithmetic
@math heading="One routine made k times faster" items="new total = T − t + t/k@new total;;speedup = T / new total@speedup"
Here's the arithmetic. If a routine took t of the total time T, and you make it k times faster, the new total is T minus t plus t over k. The speedup is T over the new total. And the saving can never exceed t, however big k gets.

@art profile-bars
The lesson's profile, its own illustration, has four routines. Parse takes six hundred milliseconds, compute two fifty, format a hundred, and write fifty. A thousand in all.

@math heading="Two changes" items="format × 10:  1000 → 910 ms · saves 9%@format ten times;;parse × 2:  1000 → 700 ms · saves 30%@halve parse"
Make format ten times faster, and the total goes to nine hundred and ten. Your suspect is ten times faster, and the program is nine percent faster. Halve parse instead, and it's seven hundred, a thirty percent saving.

@art shrink-small
Now make format and write each a thousand times faster. The total is eight hundred and fifty point one five. About fifteen percent, half of what halving parse gives.

@chapter The approach
@art stopwatch
Gains come from many changes in combination. So the approach is this. Save a working version. Measure. Decide whether the problem is design or code. Tune the bottleneck. Measure each change, and revert any that doesn't help.

@chapter Where people slip
@list heading="Common slips" items="A 10× routine means a much faster program@The first|Fewer lines run faster@The second|Tuning as you write@the third"
The first slip is thinking a tenfold speedup of a routine makes the program much faster. It gains only by that routine's share. The second is believing fewer lines run faster. Only measurement says. And the third is tuning as you write, spending effort on code that isn't the bottleneck.

@chapter Try it
@words text="Hot routine 95% · everything else 5%" sub="A: everything else × 1000 · B: hot routine × 2"
Your turn. One routine takes ninety five percent of the time, everything else five. Change A makes everything else a thousand times faster. Change B makes the hot routine twice as fast. Compute the share each saves, and say which is worth making.

@end text="Tune a profile yourself"
You can type the profile into the speedup lab and check, on Learn. That's learn dot get er done dot I O.
