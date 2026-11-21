---
format: long
lesson: code-complete-laying-the-foundation/upstream-prerequisites
title: Measure twice, cut once: what a late defect really costs
thumb: Catch it where it was made
---

@chapter The problem
@title text="Upstream Prerequisites" sub="Code Complete, chapter 3" art=thumb
You've probably fixed a bug that wasn't a coding mistake at all. The routine did exactly what the specification said, the tests passed, and the specification was wrong. By the time a customer noticed, the wrong rule was in the schema, three screens and a report.

@art measure-twice
Chapter three is about that kind of defect. Its carpenter's title, measure twice, cut once, is the whole argument. Much of a project's success is settled before construction begins. On a poor foundation, the best construction can do is limit the damage.

@quote text="The overarching goal of preparing for construction is risk reduction. Be sure your preparation activities are reducing risks, not increasing them." cite="McConnell, Code Complete, 2nd ed., Chapter 3, p. 59"
That's the chapter's first key point. The overarching goal of preparing for construction is risk reduction. Be sure your preparation activities are reducing risks, not increasing them.

@chapter Why testing can't save you
@words text="You can't test a Pontiac Aztek into a Rolls-Royce"
Testing can't find that you built the wrong product. Start from the design of a Pontiac Aztek, McConnell says, test it as much as you like, and it won't turn into a Rolls Royce.

@art food-chain
So why do projects skip preparation? The people assigned to it may lack the skills, programmers want to start coding, and managers want to see code. But think of a food chain. The architect consumes the requirements, the designer the architecture, and the coder the design. Contaminate the top, and everything downstream is contaminated.

@chapter The cost table
@art cost-staircase
Then there's the data. Find a defect as close as possible to when it was introduced, because it does more damage the longer it stays. Table three one gives the relative cost of a fix by the phase a defect was made in and the phase it was found in.

@list heading="A requirements defect, fixed in" items="Requirements: 1@costs one|Architecture: 3@three in architecture|Construction: 5 to 10@five to ten|System test: 10@ten in system test|After release: 10 to 100@ten to a hundred"
A requirements defect costs one to fix in requirements, three in architecture, five to ten in construction, ten in system test, and ten to a hundred after release. The book's own example is an architecture defect costing a thousand dollars early, and fifteen thousand in system test.

@words text="Averages over other people's projects" sub="smaller projects: closer to 5 to 10 after release"
Hold those numbers loosely. They're the book's synthesis of other people's data, averages over projects you didn't work on. And on smaller projects, the book adds, the multiplier after release is closer to five to ten than to a hundred.

@chapter Iterative or sequential
@art iterative-vs-sequential
Section three point two qualifies all this. A sequential project finishes each activity before the next. An iterative one interleaves requirements, architecture, construction and testing. Some writers say iterative projects hardly need prerequisites. McConnell calls that view misinformed.

@art iterative-loop
Iteration finds defects nearer the time they were made, and spreads the cost over the project in small instalments. It doesn't remove it. Most projects, the book says, should settle at least the most critical requirements and architecture early, and iterative approaches are the more useful far more often.

@chapter The prerequisites
@list heading="Before construction" items="A problem definition@problem definition|Requirements@Requirements|An architecture@architecture"
The prerequisites are three. A problem definition states the problem in the user's language, without a solution. Requirements say in detail what the system does, though stable requirements are a myth. And an architecture holds the detailed design together. A well run project spends about ten to twenty percent of its effort on this upstream work.

@chapter Price it
@art defect-boxes
The lesson's lab does the table's arithmetic. Its found late preset has thirty five defects. Ten requirements defects found in system test, five architecture defects found after release, and twenty construction defects found in system test.

@math heading="35 defects, most found late" items="10 × 10 = 100@ten times ten;;5 × 25 to 5 × 100 = 125 to 500@five times twenty five;;20 × 10 = 200@twenty times ten;;late: 425 to 800 · early: 35@four hundred and twenty five;;ratio ≈ 12.1× to 22.9×@about twelve point one"
Ten times ten is a hundred. Five times twenty five, up to five times a hundred, is a hundred and twenty five to five hundred. Twenty times ten is two hundred. So the late cost is four hundred and twenty five to eight hundred units. Found where each was made, it's thirty five. The ratio is about twelve point one to twenty two point nine times.

@chapter Where people slip
@list heading="Common slips" items="Reading the table as finish requirements first@The first|Leaving quality to testing at the end@The second|Writing a problem definition as a solution@the third"
The first slip is reading the table as a rule to finish requirements first. It's an argument for finding defects early, in any order of work. The second is leaving quality to testing at the end. And the third is writing a problem definition as a solution, like saying we need our data entry system optimised.

@chapter Try it
@words text="3 defects, all found after release" sub="rounding rule · tax in two places · loop skips last line"
Your turn. Three defects reach customers. The specification rounds refunds the wrong way. Tax is computed in two places that disagree. And a loop skips the last line of a basket. Place each in the phase it was made, price them by the table, and compare with the three units they'd have cost if caught early.

@end text="Price a set of defects"
You can price your own defects by the table in the lab, on Learn. That's learn dot get er done dot I O.
