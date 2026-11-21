---
format: long
lesson: code-complete-code-improvements/the-software-quality-landscape
title: Why testing alone can't find most of your bugs
thumb: Combine unlike techniques
---

@chapter What quality is
@title text="The Software-Quality Landscape" sub="Code Complete, chapter 20" art=thumb
Chapter twenty asks what quality is before it asks how to get it. And its answer to the second question is one that test heavy teams don't always like hearing.

@art two-sides
Some quality characteristics a user meets: correctness, usability, efficiency, reliability, robustness. Others only a programmer meets: maintainability, readability, testability. Users only care about the first kind, but the second reaches them in the end. Code you can't understand is code whose defects you can't fix.

@art tug-of-war
And the characteristics pull against each other. Working on correctness, doing exactly what the specification says, works against robustness, carrying on when the input isn't what was specified.

@chapter Objectives
@art five-targets
The case for setting quality objectives is a story. In nineteen seventy four, Weinberg and Schulman gave several teams the same program, and told each to optimise something different. Memory, readable output, readable code, the least code, the least programming time. Nearly every team came first on its own objective, and none did well on all of them.

@words text="Programmers do what they're asked" sub="the objectives conflict, so someone has to choose"
Programmers do what they're asked, the chapter concludes. The objectives conflict, so someone has to choose.

@chapter Detection rates
@list heading="Modal detection rates" items="Unit testing: 30%@unit testing|Integration testing: 35%@integration|System testing: 40%@system|Formal design inspections: 55%@design inspections|Formal code inspections: 60%@code inspections"
The heart of the chapter is a table adapted from Capers Jones and others. It gives each technique's most common rate. Unit testing thirty percent, integration thirty five, system forty, formal design inspections fifty five, and formal code inspections sixty.

@words text="None above 75% · average about 40%" sub="test-heavy: about 85% · leading organisations: 95% or more"
McConnell's reading is that no technique's modal rate is above seventy five percent, and they average about forty. The typical test heavy organisation removes about eighty five percent. Leading ones, using a wider variety, reach ninety five or more. These are other people's averages, mostly before two thousand and four.

@quote text="No single defect-detection technique is completely effective by itself. Testing by itself is not optimally effective at removing errors." cite="McConnell, Code Complete, 2nd ed., Chapter 20, p. 477"
That's the chapter's own summary. No single defect detection technique is completely effective by itself. Testing by itself is not optimally effective at removing errors.

@art many-nets
So the chapter argues for combining unlike techniques. In a study by Glenford Myers, no method had a significant advantage on its own. But any two together, even two independent groups using the same method, found far more than one, because different people find different defects.

@chapter Stages in a row
@art filter-stages
So how do stages combine? Defects pass through them in order. Each stage finds its rate of whatever reaches it, and the rest go on. The defects left at the end are the starting number times each stage's miss rate.

@math heading="1,000 defects, testing only" items="unit 30%:  finds 300, leaves 700@unit testing finds;;integration 35%:  leaves 455@four hundred and fifty five;;system 40%:  leaves 273@two hundred and seventy three;;removed: 727/1000 = 72.7%@seventy two point seven"
Send a thousand defects through the three tests. Unit testing finds three hundred and leaves seven hundred. Integration leaves four hundred and fifty five. System testing leaves two hundred and seventy three. Combined, that's seventy two point seven percent removed.

@math heading="Inspections too" items="+ design 55% + code 60% in front@in front;;remaining ≈ 49.14@forty nine point one four;;removed ≈ 95.1%@ninety five point one"
Now put a design inspection at fifty five percent and a code inspection at sixty in front. The remainder falls to forty nine point one four, and removal rises to about ninety five point one percent, the level the chapter reports for leading organisations.

@art same-holes
Read the product for what it assumes. It treats each stage's misses as independent, as if every defect a stage missed were as easy for the next to find. Two stages that miss the same kinds break that. That unlike techniques find different defects is the chapter's claim from data, not something the multiplication shows.

@chapter Early, and free
@words text="Improving quality reduces development costs" sub="the General Principle of Software Quality"
Find defects early and throughout, the book says. And it closes with the General Principle of Software Quality: improving quality reduces development costs. The largest single activity on most projects is debugging and reworking code that doesn't work.

@chapter Where people slip
@list heading="Common slips" items="Thinking testing is how you get quality@The first|Adding the rates@The second|Reading the book's rates as your project's@the third"
The first slip is thinking testing is how you get quality. The second is adding the rates. Thirty, thirty five and forty don't remove a hundred and five percent. The misses multiply. And the third is reading the book's rates as your project's. Your own defect records are what would test them.

@chapter Try it
@words text="1,000 defects" sub="A: 40% then 50% · B: three stages at 30%"
Your turn. Start with a thousand defects. Pipeline A has two stages, forty percent then fifty. Pipeline B has three, at thirty percent each. Work out the defects left and the combined removal for each, and say which removes more.

@end text="Chain your own stages"
You can type each pipeline into the stages lab to check your figures, on Learn. That's learn dot get er done dot I O.
