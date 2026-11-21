---
format: long
lesson: gof-behavioral-objects/strategy
title: Strategy: where do the if statements go?
thumb: Eight decisions down to three
---

@chapter Too many conditionals
@title text="Strategy" sub="Design Patterns, chapter 5" art=thumb
You've seen code that asks which mode it's in, again and again, in every method. Strategy is the Gang of Four's cure. But it doesn't make the choice disappear, and by the end you'll see exactly where it goes.

@quote text="Code containing many conditional statements often indicates the need to apply the Strategy pattern." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 5"
That sentence ends one of the consequences. Code containing many conditional statements often indicates the need to apply the Strategy pattern. The book's other name for it is Policy.

@art compositors
The motivation is breaking text into lines, for which there are many algorithms. Write them all into the class that needs them, and it gets bigger, keeps algorithms you may not use, and makes a new one hard to add. So the text class holds a compositor object, and three compositor subclasses do it three ways.

@chapter The pattern
@art context-strategy
Three participants. The strategy is the common interface. Each concrete strategy is one algorithm. And the context is configured with a strategy, keeps a reference to it, and calls it. Clients usually create a strategy, hand it over, and then deal with the context only.

@list heading="Four benefits" items="A family inheritance can factor@a family|An alternative to subclassing the context@alternative to subclassing|Removes conditionals@removes|Choose your trade-offs@trade offs"
Four consequences are benefits. Strategies form a family that inheritance can factor. It's an alternative to subclassing the context, which would fix the algorithm and rule out changing it at run time. It removes the conditionals that pick a behaviour. And clients can choose implementations with different trade offs of time and space.

@chapter The print shop
@code block=1 lines=1-19 label=Java focus="3-12@switches on|15-18@scheduling the job"
Here's the lesson's print shop. Quoting a job switches on the printing method: offset, risograph or digital. And scheduling the job tests the method again. Every operation asks the same question.

@math heading="Decision points before" items="start: 1@start at one;;cases: 3@three cases;;ifs: 3@three ifs;;and: 1@and one;;1 + 3 + 3 + 1 = 8@eight"
The lab counts decision points. Start at one. Add three cases, three ifs, and one conditional and. That's eight.

@art switch-every-method
And five of those eight ask which method applies: the three cases, and the first test of each if when scheduling. The same question, asked in every operation.

@code block=2 lines=1-19 label=Java focus="1-4@one interface|7@price break|15@slower run"
Now as strategies. One interface, with both operations. Offset keeps its price break at five hundred copies. Risograph keeps its slower run past a thousand. Digital tests nothing. The count falls to three: one to start, and two ifs, each a rule inside one algorithm.

@art one-choice
So where did the five tests of which method applies go? The choice is made once, where the job is given its method at the counter, in code the lab isn't shown. That's the first liability in a sentence: someone must know the strategies to choose one.

@chapter Three liabilities
@art client-knows
The authors put them plainly. Clients must know how the strategies differ to choose one, so the pattern belongs where the variation matters to them.

@art extra-args
All strategies share one interface, so a context may prepare arguments a simple strategy never reads. In the book's sample, one compositor ignores some of what it's passed, and another ignores all of it. And there are more objects, though stateless strategies can be shared, as flyweights.

@words text="Take the data, or pass the context"
The implementation adds a choice. Pass the strategy the data it needs, which keeps them decoupled. Or pass the context itself, and let the strategy ask, which couples them more closely. A strategy can even be optional, with a default when there's none.

@chapter Where people slip
@list heading="Common slips" items="Using it wherever an algorithm could vary@The first|Reading the falling count as the whole story@The second|Shaping the interface around one algorithm@And the third"
The first slip is reaching for Strategy wherever an algorithm could vary. The second is reading the falling count as the whole story. The choice still exists, and there are more objects. And the third is shaping the interface around the first algorithm, when it has to suit them all.

@words text="Template Method: part, by inheritance" sub="Strategy: the whole, by delegation"
And one neighbour to keep apart. Template Method varies part of an algorithm, by inheritance. Strategy varies the whole of it, by delegation.

@chapter Try it
@code block=3 lines=2-16 label=Java focus="3@correct|6@timed|12@streak"
Your turn. A quiz app scores an answer by the round's mode. Count its decision points. Then sketch classic, timed and streak strategies, keeping the test of whether the answer is correct in the context, and count again.

@end text="Count the decisions"
Then paste each into the lab and check, on Learn. That's learn dot get er done dot I O.
