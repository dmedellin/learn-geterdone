---
format: long
lesson: code-complete-variables/structures-pointers-and-global-data
title: What global data couples, and what access routines change
thumb: Access routines move the coupling
---

@chapter The question
@title text="Structures, Pointers and Global Data" sub="Code Complete, chapter 13" art=thumb
Chapter thirteen covers three kinds of data a modern program uses less often: structures, pointers and global data. Its longest argument is about globals, and about what to do with the ones you keep.

@quote text="If you can’t avoid global variables, work with them through access routines. Access routines give you everything that global variables give you, and more." cite="McConnell, Code Complete, 2nd ed., Chapter 13, p. 344"
Here's the last key point of the chapter. If you can't avoid global variables, work with them through access routines. Access routines give you everything that global variables give you, and more.

@chapter Structures and pointers
@art grouped-fields
A structure is data built from other data. In Java, a class with public fields and no routines. McConnell would usually rather you wrote a full class, but a structure still helps. It shows which data belongs together. It lets you pass a group as one. And it shortens parameter lists.

@art isolated-pointers
Pointers, he says, are one of the most error prone areas of programming. Java has none, but the advice carries over. A pointer error's symptoms are usually unrelated to its cause, so isolate pointer operations in a few routines, so there are few places to get them wrong.

@chapter The trouble with globals
@list heading="Problems with global data" items="Inadvertent changes@Inadvertent|Aliasing@aliasing|Threads@thread|Code you can't reuse@reused|Lost modularity@modularity"
Section thirteen point three lists the problems. Inadvertent changes, where one routine changes a global another assumed was untouched. Aliasing, where a global passed as a parameter is changed under two names. Code that more than one thread runs. Code that can't be reused without its globals. And worst, lost modularity. You can no longer understand one routine at a time.

@art database-global
The section is fair to the other side. A database and a configuration file are global data too, and so are named constants. Used with discipline, globals serve for values that apply to the whole program, and to eliminate tramp data passed through routines that don't use it.

@words text="Local first, class data next, global last"
Even so, make each variable local first, class data next, and global only as a last resort.

@chapter Access routines
@code block=1 lines=1-11 label=Java focus="2@private and static|4-6@reads it|8-10@changes it"
For the globals you keep, use access routines. Hide the data in a class, private and static so there's one copy. Write one routine that reads it, and one that changes it. And require every other piece of code to use them.

@list heading="What they buy" items="Centralised control@Centralised|A place to check every change@check every change|Information hiding@hiding|A level of abstraction@abstraction"
That buys centralised control, so a change of representation stays inside the class. A place to check every change. Information hiding. And a level of abstraction, so a test reads as whether the page is full, not as a comparison of a line count.

@chapter Count the coupling
@art six-routines
The lab counts it. Six routines share three globals: the current record, an error log, and a running total. Two routines are coupled when they share a global and at least one of them writes it.

@math heading="Six routines, three globals" items="current: 1 writer pair + 2 × 3 = 7@seven pairs;;errors adds validate–report: 8@eight;;total adds addLine–printTotals: 9@nine;;possible pairs: 6 × 5 ÷ 2 = 15@fifteen"
The current record has two writers and three readers. That's one pair of writers, plus two times three writer and reader pairs, seven pairs. The error log adds one more, eight. The running total adds one more, nine. Out of six times five over two, fifteen possible pairs.

@art reader-coupled
Notice report, which only reads. It's coupled to three routines anyway, because what it prints depends on what they wrote.

@math heading="With access routines" items="coupled pairs: 9 → 9@still nine;;places touching a global: 10 → 3@ten to three"
Now give each global an access routine. The coupled pairs are still nine, because the six routines still share the same data. What changes is that the places touching a global directly fall from ten to three, one for each global. That's centralised control, and no more.

@art access-gate
Each global now sits behind its owner: current record, error log, and running total. And the lab's list of who writes each global names only those three owners.

@chapter Where people slip
@list heading="Common slips" items="A read-only routine is safe@The first|Access routines remove coupling@The second|Hiding globals in one big object@the third"
The first slip is thinking global data is fine as long as a routine only reads it. The second is thinking access routines remove the coupling. They move it. And the third is gathering everything into one big object passed to every routine. That's overhead with none of the benefits. If you use global data, use it openly.

@chapter Try it
@words text="5 records" sub="load writes config · render and save read it · render writes cache · save reads it"
Your turn. Load writes config, and render and save read it. Render writes cache, and save reads it. Count the globals, the routines, the coupled pairs and the direct touches. Then say what changes once each global has an access routine.

@end text="Count what your globals couple"
You can type your own reads and writes into the lab and count the coupling, on Learn. That's learn dot get er done dot I O.
