---
format: long
lesson: ddd-model-integrity/continuous-integration
title: Continuous Integration: keeping one model whole inside its context
thumb: Catch the splinter early
---

@chapter Drawn is not kept
@title text="Continuous Integration" sub="Domain-Driven Design, Chapter 14" art=thumb
A Bounded Context doesn't stay unified just by being drawn. Once it exists, the people working inside it pull its model apart. The larger the team, the worse it gets, and Evans says three or four people can already run into serious trouble.

@art too-many-contexts
Cutting the system into ever smaller contexts is no cure. Past a point, that throws away integration worth having.

@chapter How careful people splinter a model
@list heading="Three ways" items="Changing an object for the wrong purpose@doesn't fully grasp|A second version of a concept you didn't know@doesn't know|A second version you were afraid to touch@afraid"
He describes three ways a careful developer splinters a model. One doesn't fully grasp what a colleague's object was for, and changes it so it no longer serves that purpose. One doesn't know a concept already exists, and writes an inexact second version. And one knows it exists, but is afraid that touching it will break something.

@art safety-net
That last one is what a safety net addresses. A developer who can run the tests is less afraid to change the original.

@chapter Two levels
@quote text="all work within the context is being merged and made consistent frequently enough that when splinters happen they are caught and corrected quickly." cite="Evans, Domain-Driven Design, Chapter 14"
So, Continuous Integration. It means that all work within the context is being merged and made consistent frequently enough that when splinters happen they are caught and corrected quickly.

@art two-levels-merge
It works at two levels. Concepts are integrated by constant talk, above all by hammering out the Ubiquitous Language. The implementation is integrated by a systematic merge, build and test. And the two help each other. Shared concepts make the code easier to merge, and merged, tested code exposes splinters early.

@list heading="Effective integration of code" items="A reproducible merge and build@reproduce|Automated test suites@automated|A short life for unmerged changes@unmerged"
Effective processes have a merge and build you can reproduce step by step, automated test suites, and a fairly small limit on how long a change can stay unmerged. Most agile projects, he notes, merge at least daily.

@words text="Only inside one context"
And keep the job no bigger than it must be. It's needed only inside one context, for anything larger than a two person task. Relations with neighbouring contexts can move at a slower pace.

@chapter Two halves, one month apart
@art drifting-halves
To see it, take the last lesson's lab and point it inward. Instead of two contexts, two halves of one team who should mean the same things.

@code block=1 lines=1-10 focus="1-5@web shop pair|6-10@counter till pair"
The records are the Box Office's web shop pair and its counter till pair, who stopped talking for a month. Inside one context, every shared term should be safe, and no concept should have two names.

@math heading="drifted" items="7 terms · 3 used by both@seven terms;;1 false cognate: concession@concession;;2 duplicates: patron = customer, concession = reduced-rate@two duplicate concepts"
The lab counts seven terms, three used by both halves. One is a false cognate: concession. Two are safe. And there are two duplicate concepts. The ticket buyer is a patron on the web and a customer at the till. And the reduced price is a concession on the web, and a reduced rate at the till.

@art two-concessions
Concession is the instructive one. In a theatre it means a reduced price for students and pensioners. It also means the counter that sells drinks and ice cream. Each half took one meaning. Inside one context that's a splinter, and the first sign is two people talking past each other.

@art one-afternoon
Then they spend one afternoon hammering out the language. Both halves agree to say patron, and concession for the reduced price. The counter's sales become kiosk sale.

@math heading="merged" items="6 terms · 4 shared · all 4 safe@six terms;;0 false cognates · 0 duplicates@no false cognates"
The lab counts again. Six terms, four shared, all four safe, no false cognates and no duplicates. Notice who gave way, though. The till half gave up three words. Who gives way is a conversation, not a count.

@chapter Where people slip
@list heading="Common slips" items="One context stays consistent by itself@The first|A build server alone@The second|Integrating across every context@And the third"
The first slip is thinking a team inside one context stays consistent without effort. The second is treating Continuous Integration as a build server alone. A green build doesn't show two people mean different things by concession. And the third is running it across every context.

@chapter Try it
@code block=2 lines=1-10 focus="1-5@booking pair|6-10@records pair"
Your turn. A clinic's booking pair and its records pair, both inside one context, after a month apart. Find what the next merge has to settle: the false cognates, the duplicate concepts, and the terms already safe to share. Then propose one renaming for each problem.

@end text="Merge the code and the words"
Check the result in the lab, on Learn. That's learn dot get er done dot I O.
