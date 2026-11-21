---
format: long
lesson: code-complete-laying-the-foundation/key-construction-decisions
title: Program into your language, not in it
thumb: Supply what the language lacks
---

@chapter The question
@title text="Key Construction Decisions" sub="Code Complete, chapter 4" art=thumb
Chapter three was about preparation you might have no say in. Chapter four asks which decisions are yours. In the book's image, which tools go on your belt, and how you load the truck before you drive to the site.

@list heading="Four decisions" items="The language@the language|The conventions@conventions|Where you stand on the technology wave@technology wave|The construction practices@practices"
There are four. The language, the programming conventions, where you stand on the technology wave, and which of the many good construction practices you'll use.

@chapter The language
@art toolbelt
You're immersed in the language from the start of construction to the end, so it matters. Programmers are more productive in a language they know. The book's data puts people with three or more years in a language about thirty percent ahead of equally experienced people new to it.

@list heading="Statements of C per statement" items="Java: 2.5@two and a half|Visual Basic: 4.5@four and a half|Python: 6@six for Python"
Higher level languages also say more per line. Table four one gives typical ratios, the number of statements of C one statement does the work of. Two and a half for Java, four and a half for Visual Basic, and six for Python. Typical ratios, not constants.

@art disguised-fortran
And a language can shape how you think. The book retells an old story. A team of Fortran programmers moves to C plus plus, and writes code that compiles, but is really disguised Fortran, with gotos and global data and none of the classes.

@chapter Conventions and the wave
@art collage-painting
Conventions cover names, layout, comments and the like. A painting that's partly classical, partly impressionist and partly cubist is a collage, however faithfully it follows the plan. Arbitrary variations make the reader work for nothing. And conventions are nearly impossible to retrofit, so set them before construction.

@art technology-wave
Then there's the technology wave. Late in a wave, the tools are mature and documented, and your day goes on new function. Early in a wave, they're buggy, and much of your day goes on finding out how the tools behave. McConnell doesn't say avoid the early part. He says the book's practices help even more there.

@chapter Into, not in
@quote text="Ask yourself whether the programming practices you’re using are a response to the programming language you’re using or controlled by it. Remember to program into the language, rather than programming in it." cite="McConnell, Code Complete, 2nd ed., Chapter 4, p. 70"
This is the idea the chapter calls critical to the whole book. Ask yourself whether your practices are a response to your language, or controlled by it. Program into the language, rather than in it.

@words text="Decide what to express, then how" sub="David Gries, The Science of Programming, 1981"
The distinction comes from David Gries. Programming in a language limits your thoughts to what it directly supports. Programming into it means deciding what you want to express first, then working out how to express it with the tools you have.

@art separated-layers
McConnell's own example was early Visual Basic. He wanted business logic, user interface and database code kept apart, and the language offered no way to do it. So he adopted a convention. A form could only read and write its data, with one public routine, and everything else lived in a module.

@chapter A Java convention
@code block=1 lines=3-16 label=Java focus="3@named constant|5-7@shorter version|9-16@full version"
Here's a small case. Java has no default values for parameters. So the lesson supplies one by convention. The default is written once, as a named constant. The shorter version does nothing but forward. And the full version holds the logic, trying up to retries times.

@art forwarding-arrow
Nothing in Java requires this shape. A teammate could write a bare three into the shorter version, and the compiler would accept it. The convention holds because the team keeps it and reviews for it.

@chapter Convert a size
@math heading="10,000 statements of C" items="Java: 10000 ÷ 2.5 = 4000@divided by two and a half;;Python: 10000 ÷ 6 = 5000/3 ≈ 1666.67@divided by six;;Visual Basic: 10000 ÷ 4.5 = 20000/9 ≈ 2222.22@divided by four and a half"
The lab does the table's one sum. Ten thousand statements of C, divided by two and a half, is four thousand statements of Java. Divided by six, it's five thousand over three, about sixteen sixty six point six seven of Python. And divided by four and a half, about twenty two twenty two point two two of Visual Basic.

@chapter Where people slip
@list heading="Common slips" items="Reading the ratio as a schedule@The first|Thinking a missing keyword means a missing practice@The second|Leaving conventions for later@the third"
The first slip is reading the ratio as a schedule. It counts statements, not hours, not defects. The second is thinking a missing keyword means a missing practice. You can supply it by convention. And the third is leaving conventions for later, when they're nearly impossible to retrofit.

@chapter Try it
@list heading="Supply the missing facility" items="No assertion statement@no assertion|No enumerated types@no enumerated|No access control@no access control"
Your turn. Write a convention for three languages. One with no assertion statement, as Java was before version one point four. One with no enumerated types, as Java was before version five. And one with no access control. Make each something a reviewer can check.

@end text="Program into the language"
You can convert sizes by the book's table in the lab, on Learn. That's learn dot get er done dot I O.
