---
format: long
lesson: code-complete-system-considerations/programming-tools
title: Programming tools: what they take off your hands
thumb: One header, three rebuilds
---

@chapter The question
@title text="Programming Tools" sub="Code Complete, chapter 30" art=thumb
You edit one header, start the build, and watch it recompile files you never touched. That's a build tool doing exactly what it was asked. Chapter thirty is about tools like that. What kinds exist, what each takes off your hands, and where their promise runs out.

@words text="Kinds of tool, not brands"
McConnell writes about kinds of tool rather than brands, because products change faster than a book can be printed. He names a few, like grep, make and lint, only because they're so common.

@quote text="Programmers sometimes overlook some of the most powerful tools for years before discovering them." cite="McConnell, Code Complete, 2nd ed., Chapter 30, p. 725"
And the chapter's key point is a reason to read the survey. Programmers sometimes overlook some of the most powerful tools for years before discovering them.

@chapter Source-code tools
@art toolbox
The source code tools are the richest set. An IDE with search, formatting and refactoring built in. Search and replace across many files, with regular expressions. Diff and merge tools. Beautifiers that standardise layout. And tools that extract interface documentation, like Javadoc.

@list heading="More source-code tools" items="Picky checkers, like lint@lint|Metrics reporters@Metrics|Refactoring browsers@Refactoring browsers|Version control@Version control|A data dictionary@data dictionary"
There are picky syntax and semantics checkers, lint among them, that warn about code which compiles but probably isn't what you meant. Metrics reporters. Refactoring browsers. Version control. And on large projects, a data dictionary of every significant name.

@chapter Build tools
@art build-graph
A build tool's purpose is to rebuild a program in the least time from the current sources, and to bring every file to a consistent state. For each target, you state what it depends on and how to make it. When a file changes, the tool rebuilds the targets that depend on it, and leaves the rest.

@code block=1 lines=1-3 label=make focus="1@app|2@main dot o|3@util dot o"
Here's the lab's small C build. The program app is linked from main dot o and util dot o. Main dot o is compiled from main dot c and util dot h. Util dot o is compiled from util dot c and util dot h.

@math heading="What a change reaches" items="util.h:  directly main.o, util.o · in all 3@util dot h;;main.c:  directly main.o · in all 2@main dot c"
Change util dot h, and two targets depend on it directly, main dot o and util dot o. Three are reached in all, because app is linked from both. Change main dot c, and only main dot o depends on it directly. Two in all, and util dot o is left alone.

@art header-ripple
That's why changing a header is expensive. It reaches every object file that includes it. And the lab reads only the dependencies you type. A dependency missing from a makefile is missing from the count, which is how a build ends up out of step.

@chapter Your own tools
@art tool-building
Given five hours for a job, McConnell says, most good programmers would rather spend four hours and forty five minutes building a tool, and let it do the job in fifteen minutes. Plan time for project specific tools.

@art script-shortcut
And write a script for anything longer than about five characters that you type more than a few times a day. A short script removes a repeated chance of typing a long command wrong.

@chapter Tool fantasyland
@art fantasyland
Then the chapter's history. Fortran, the formula translator, was conceived so that scientists and engineers could type in their formulas and do without programmers. Programmers were still needed. Fourth generation languages, CASE tools and visual programming each carried the same promise.

@words text="Better programming, not no programming"
Each made programming better without eliminating it. What's left, once the accidental difficulties are gone, is hard in itself. The messy world, the dependencies and exceptions, and the users who can't make up their minds.

@chapter Where people slip
@list heading="Common slips" items="Thinking a build rebuilds what you edited@The first|Expecting a tool to end programming@The second|Seeing your own tools as a detour@the third"
The first slip is thinking a build tool rebuilds what you edited. It rebuilds what depends on the change, through every chain. The second is expecting a tool to eliminate programming. When a vendor promises that, McConnell's advice is to run, or at least to smile. And the third is treating your own tools as time taken from the real work.

@chapter Try it
@code block=1 lines=1-3 label=make focus="3@util dot c"
Your turn. Using these three lines, suppose util dot c changes. List the targets that depend on it directly, and every target the build will remake.

@end text="Trace a change through a build"
You can type the change into the build lab and check, on Learn. That's learn dot get er done dot I O.
