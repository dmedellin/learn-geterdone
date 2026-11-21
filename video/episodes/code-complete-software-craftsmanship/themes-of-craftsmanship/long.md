---
format: long
lesson: code-complete-software-craftsmanship/themes-of-craftsmanship
title: The themes of Code Complete, and why none is a religion
thumb: A toolbox, not a rulebook
---

@chapter The question
@title text="Themes of Craftsmanship" sub="Code Complete, chapters 34 and 35" art=thumb
Take a routine you wrote last month, one you'd rather nobody reviewed. Chapter thirty four names what that routine has lost sight of. The book has been about details, and this chapter picks them up again to show what they serve.

@chapter Conquer complexity
@art small-load
The first theme is managing complexity, the heart of software development. Nobody's brain spans the range of detail a program has. So subsystems, class interfaces, short routines, clear names and conventions are all tools for holding less of it at once. Abstraction is the most powerful of them.

@chapter Process and people
@list heading="The themes" items="Pick your process@Pick your process|Write for people first@people first|Program into your language@into your language|Focus attention with conventions@conventions|Work in the problem's terms@problem domain"
Pick your process, because how a team works decides whether its abilities add up or cancel out. Write programs for people first, computers second. Program into your language, not in it. Focus your attention with conventions. And program in terms of the problem domain, with files and loop indexes kept lower down.

@words text="Into your language, not in it" sub="decide what you want, then find how the language can do it"
Program into your language means deciding what you want to do first, then finding the way your language can do it. If it lacks assertions or named constants, write your own.

@chapter Falling rocks
@art falling-rocks
Watch for falling rocks. Tricky code, a class with more errors than average, a project with a great deal of debugging. Each one suggests something to look at. And the section names design metrics too: more than about ten decision points in a routine, and more than three levels of nesting.

@words text="The irritation of doubt" sub="after Charles Sanders Peirce"
None of them necessarily means a routine is badly designed. Only that it should be looked at skeptically. McConnell borrows a phrase from Charles Sanders Peirce for the feeling to heed: the irritation of doubt.

@chapter Count a routine
@code block=1 lines=1-16 label=Java focus="2@line two|6@for|8@line eight|12@line twelve"
Here's a routine that decides how long to wait before retrying a request. The lab counts seven decision points. The one, the if and the or on line two, the for, the if on line eight, and the if and the and on line twelve. That's in the six to ten band. Its deepest nesting is two, first reached on line nine.

@art extract-loop
Neither figure is a verdict. What they point to is the loop, which doubles a delay and caps it. It could be a routine of its own, with a name, which serves the complexity theme. And the bare one hundred and ten thousand would read better as named constants, which serves writing for people first.

@code block=2 lines=1-22 label=Java focus="3-6@nesting|14@line fourteen"
The shipping routine from the nesting lesson counts nine decision points, and a deepest nesting of five, first reached on line fourteen. Five levels is past the three that the chapter names as a warning sign. The two counts tell you which routine to look at first.

@chapter Iterate
@art iterate-loop
Iterate, repeatedly, again and again. Requirements, design, estimates and tuning all improve with repeated attempts. The trick is to iterate early, when it's cheap.

@chapter No religion
@quote text="Dogmatic methodologies and high-quality software development don’t mix. Fill your intellectual toolbox with programming alternatives, and improve your skill at choosing the right tool for the job." cite="McConnell, Code Complete, 2nd ed., Chapter 34, p. 853"
And the last theme. Dogmatic methodologies and high quality software development don't mix. Fill your intellectual toolbox with programming alternatives, and improve your skill at choosing the right tool for the job.

@art toolbox-pliers
Software development is heuristic, not deterministic. So mix methods. Experiment with new ones, rely on dependable ones, and be ready to change your mind. McConnell's image is a contractor friend, Simple Simon, who uses vise grip pliers for every job. Chapter thirty five then closes with a reading plan, in three levels.

@chapter Where people slip
@list heading="Common slips" items="Craftsmanship as rules to follow@The first|A count under the threshold as a pass@The second|Process as overhead@the third"
The first slip is reading craftsmanship as a set of rules. Even the book's thresholds are reasons to look. The second is reading a count under the threshold as a pass. Seven decision points still pointed at a loop and two bare numbers. And the third is thinking process is overhead. The book calls that shortsighted.

@chapter Try it
@words text="Your own routine, about 15 lines" sub="count · two changes · the theme each serves"
The exercise is your own code. Take a routine of about fifteen lines that you wrote. Count its decision points and its deepest nesting by hand. Then name two changes you'd make, and the theme each one serves.

@end text="Measure your own routine"
You can paste it into the complexity lab to check your counts, on Learn. That's learn dot get er done dot I O.
