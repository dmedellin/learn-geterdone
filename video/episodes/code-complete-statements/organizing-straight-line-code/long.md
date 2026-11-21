---
format: long
lesson: code-complete-statements/organizing-straight-line-code
title: Organizing straight-line code: make the order visible
thumb: Every arrow points down
---

@chapter The problem
@title text="Organizing Straight-Line Code" sub="Code Complete, chapter 14" art=thumb
You've probably met a routine that worked until someone tidied it. Two calls that looked independent got swapped, and a total came out wrong, or zero.

@art swapped-calls
Chapter fourteen is about exactly that kind of code. No branches, no loops, just statements run one after another. And its argument is simple. The order of those statements is a fact about the program, so it should be visible in the code, not something a reader has to know.

@quote text="The strongest principle for organizing straight-line code is ordering dependencies." cite="McConnell, Code Complete, 2nd ed., Chapter 14, p. 353"
That's the first of the chapter's key points. The strongest principle for organizing straight line code is ordering dependencies.

@chapter What a dependency is
@art dependency-arrows
McConnell's word for what makes order count is dependency. The second statement needs what the first produced. Sometimes the routine names make that plain. Sometimes only knowledge of the domain does. And sometimes it's hidden altogether.

@art hidden-object
Hidden looks like this. A run of calls that take no parameters, all working on data their class shares. Nothing on the page tells you which one has to come first.

@chapter Three guidelines
@list heading="Make the order obvious" items="Organize code so dependencies show@organize the code|Name routines so dependencies show@name routines|Pass the data as parameters@pass the data"
So the book gives three guidelines. First, organize the code so dependencies are obvious. If one routine quietly initializes data the others use, give that its own routine whose name says it comes first. Second, name routines so dependencies are obvious, even with a long name. Third, pass the data between routines as parameters.

@art parameter-chain
That third one is the strongest. Have each routine return what the next one takes, and the order is written into the calls themselves. And when routines share nothing, the data announces the opposite, that their order doesn't matter.

@words text="Comments are the fallback" sub="then status variables or assertions, at a cost"
Only when the code can't be improved does McConnell turn to comments that document the dependency. For critical code he adds status variables or assertions, weighed against the new variables and new error checks they bring.

@chapter Count the arrows
@words text="i → j" sub="line j reads what line i wrote"
The lesson's lab makes this countable. It reads a Java listing top to bottom. Whenever line j reads a variable last set on line i, it records an arrow from i to j. It also counts anomalies, like a variable used before it's set.

@art backward-arrow
Take a parcel quote written in a hurry, with the total first. The arrows it needs would have to point up the page.

@code block=1 lines=1-7 label=Java focus="2@Line two adds|3-5@lines three to five"
Line two adds base, surcharge and insurance before anything has set them. That's three used before set. Then each is set on lines three to five and never read again. Three more. Six anomalies, and the Java compiler refuses it too.

@code block=2 lines=1-7 label=Java focus="2-4@lines two to four|5@line five|6@line six"
Now in the order the dependencies set. Lines two to four read the parameter. Line five reads all three of them. Line six returns the total. Zero anomalies, and the arrows are one to two, one to three, one to four, then two, three and four to five, and five to six.

@words text="Every arrow points down the page"
That's what ordering dependencies means in the count. No line reads anything a later line writes.

@chapter The hidden case
@code block=3 lines=1-6 label=Java focus="2-5@four calls"
Here's the third preset. Four calls on one quote object, each taking nothing and returning nothing. The lab prints one to two, one to three, one to four, one to five, which only says that every call reads the parameter. Zero anomalies, and it compiles in any of its twenty four orders.

@chapter Proximity
@art proximity-boxes
Section fourteen point two takes statements whose order doesn't matter. The rule there is the Principle of Proximity. Keep related actions together, so the code reads top to bottom. Draw a box round each group of related lines. Nested boxes are fine. Overlapping boxes mean reorganize.

@chapter Where people slip
@list heading="Common slips" items="If it compiles, the order is right@The first|Reaching for a comment first@The second|A status flag as a free safety net@the third"
The first slip is thinking that if it compiles, the order is right. The compiler only sees the dependencies the names show. The second is reaching for a comment first, when comments are the fallback. And the third is treating a status flag as a free safety net. It brings new variables and new checks, each a place for a mistake.

@chapter Try it
@words text="Put the order in the parameters" sub="loadRates returns a Rates → … → print takes the last"
Your turn. Rewrite print quote so load rates returns a rates object, kept in a local variable. Add surcharges and add insurance each take the one before and return a new one. Print takes the last. Then list every arrow, and name the chain that now carries the order.

@end text="Count the dependencies yourself"
You can paste your version into the dataflow lab and check your arrows, on Learn. That's learn dot get er done dot I O.
