---
format: long
lesson: code-complete-code-improvements/debugging-as-science
title: Debugging as science: ten tests for a thousand changes
thumb: Halve the suspects
---

@chapter The problem
@title text="Debugging as Science" sub="Code Complete, chapter 23" art=thumb
A test that passed last month fails today, and a thousand changes have gone in since. You could read the code until the defect shows itself. Or you could change things until the test passes. Chapter twenty three has a better plan.

@math heading="Gould, 1975: 12 known defects" items="fastest three: 5.0 min · slowest three: 14.1 min@five minutes;;missed: 0.7 vs 1.7@missed;;new defects made: 3.0 vs 7.7@new defects"
Programmers differ widely at debugging. In one study from nineteen seventy five, experienced programmers debugged a program with twelve known defects. The three fastest took five minutes on average, against the slowest three's fourteen point one. They missed point seven defects, against one point seven. And they made three new defects while correcting, against seven point seven.

@words text="Quality and speed go together"
The book reads that two ways. Not everyone knows how to debug. And since the fastest were also the most accurate, quality and speed go together.

@chapter The devil's guide
@art scattered-prints
The chapter's foil is the devil's guide to debugging. Scatter print statements. Change things until something seems to work. Keep no record of what you changed. And fix a wrong result by special casing the input that showed it.

@chapter The scientific method
@list heading="Five steps" items="Stabilise the error@Stabilise|Locate it@Locate|Fix it@Fix it|Test the fix@Test the fix|Look for similar errors@similar"
Against that, the chapter sets the scientific method. Gather data, form a hypothesis that accounts for it, and design an experiment to prove or disprove it. For a defect, that's five steps. Stabilise the error. Locate it. Fix it. Test the fix. And look for similar errors.

@quote text="A systematic approach to finding and fixing errors is critical to success. Focus your debugging so that each test moves you a step forward. Use the Scientific Method of Debugging." cite="McConnell, Code Complete, 2nd ed., Chapter 23, p. 562"
A systematic approach to finding and fixing errors is critical to success. Focus your debugging so that each test moves you a step forward. Use the Scientific Method of Debugging.

@chapter Locating it
@art triangulate
Use all the data, and when a fact doesn't fit, ask why rather than drop it. Reproduce the error several ways, to triangulate it. A test that disproves a hypothesis still tells you where the defect isn't. And a new error is usually in code that changed recently, so run an old version, and compare.

@art split-region
Then narrow the suspicious region. Remove about half the code, see which half the defect is in, and halve that. It's a binary search. And when quick guessing runs past a time limit you set in advance, switch to a brute force method that's sure to work.

@chapter A small case
@words text="shippingLabel: no place name for some orders" sub="hypothesis: a zone the switch doesn't name"
Here's the method on something small. Shipping label sometimes returns no place name. The data: a few zones, with or without express. A hypothesis: the zone isn't one the switch names, so the label stays empty. The experiment: call zone four and zone three. If zone three fails too, the hypothesis is wrong. One call each way settles it.

@chapter Halving a history
@art halving-line
The lab halves a history of changes. If the build from a thousand changes ago passes and today's fails, test the one in the middle. Keep the half that still holds the defect. Then do it again.

@math heading="Defect in change 637 of 1,000" items="1–1000 → 501–1000 → 501–750@five hundred and one;;→ 626–750 → 626–688 → 626–657@six hundred and twenty six;;→ 626–641 → 634–641 → 634–637 → 636–637@six hundred and thirty four;;found in 10 steps@ten steps"
Put the defect at change six thirty seven. The intervals go one to a thousand, then five hundred and one up, then five oh one to seven fifty. Then six hundred and twenty six onward, narrowing. Then six hundred and thirty four to six forty one, and down to two. It's found in ten steps.

@words text="2¹⁰ = 1,024 ≥ 1,000" sub="64 suspects → exactly 6 steps"
Ten, because two to the tenth is at least a thousand. With sixty four suspects, it's exactly six steps.

@art stable-repeat
But halving only works on a stabilised error. An intermittent failure makes a passing test mean nothing. That's why stabilising comes first.

@chapter Fixing it
@art one-change
Fixing is the easy part, the chapter says, and therefore the error prone one. Understand the problem first. Save the original code. Fix the problem, not the symptom. Change one thing at a time. Add a unit test that exposes the defect. And look for others like it.

@chapter Where people slip
@list heading="Common slips" items="Reading code until the defect shows@The first|Fixing the symptom@The second|Changing two things at once@the third"
The first slip is thinking debugging is reading the code until the defect shows itself. Reading decides a hypothesis. It doesn't replace one. The second is fixing the symptom with a special case. And the third is changing two things at once, so either could look like the fix.

@chapter Try it
@code block=1 lines=1-14 label=Java focus="4@four employees|11@count five"
Your turn. Overtime pay, called with four employees, none null, and count five, throws an index out of bounds exception. State a hypothesis, the test that would decide it, and the line where it's thrown, with i's value there. Would the five basis tests have found it?

@end text="Halve a history yourself"
You can put a defect anywhere in a thousand changes and watch the halving, on Learn. That's learn dot get er done dot I O.
