---
format: long
lesson: code-complete-laying-the-foundation/construction-and-its-metaphors
title: What is software construction, and which metaphor should you think with?
thumb: Build it, don't just write it
---

@chapter The question
@title text="Construction and Its Metaphors" sub="Code Complete, chapters 1 and 2" art=thumb
Everybody who writes software does something every single day that Steve McConnell calls construction. These two short chapters ask what that is, why it deserves your attention, and which picture of it you should carry in your head.

@quote text="Software construction is the central activity in software development; construction is the only activity that’s guaranteed to happen on every project." cite="McConnell, Code Complete, 2nd ed., Chapter 1, p. 8"
Here's the first key point of the book. Software construction is the central activity in software development. Construction is the only activity that's guaranteed to happen on every project.

@chapter What counts
@art activity-row
Section one point one lines up the activities of software development, from problem definition and requirements, through architecture and design, to coding, testing, integration and maintenance. Construction is the middle of that list.

@list heading="Construction" items="Detailed design@detailed design|Coding and debugging@coding and debugging|Construction planning@planning|Unit testing@unit testing|Integration and integration testing@integration"
It's mostly coding and debugging, but it also includes detailed design, the design of classes and routines, plus construction planning, unit testing, and integration and integration testing.

@list heading="Not construction" items="Requirements and architecture@Requirements|User-interface design@user interface|System testing@system testing|Management and maintenance@management"
Outside it sit requirements and architecture, user interface design, system testing, management and maintenance. McConnell is careful to say each of those matters to a project as much as construction does. They just aren't the book's subject.

@words text="Not “coding”" sub="construction calls for creativity and judgement"
And he won't simply call it coding. That word suggests mechanically typing in a finished design. Construction, he says, isn't mechanical at all. It calls for creativity and judgement, and the rest of the book is his evidence.

@chapter Why it matters
@list heading="Five reasons" items="A large part of the work@large part|It is central@central|Productivity can improve@productivity|The code is the accurate description@source code|It always happens@always happens"
Section one point two gives five reasons to focus on it. It's a large part of the work, thirty to eighty percent of the total time, depending on project size. It's central. A programmer's productivity can improve enormously. The source code is often the only accurate description of the software. And it always happens.

@words text="Nobody skips construction"
Rushed projects skip requirements, skip design, drop testing. No project, however rushed, drops construction. So improving it improves every project.

@chapter Metaphors as searchlights
@art searchlight
Chapter two turns to how you think about it. A software metaphor, McConnell says, is more like a searchlight than a road map. It tells you how to look for an answer, not where the answer is.

@words text="A heuristic, not an algorithm" sub="an algorithm in a clown suit"
That makes it a heuristic. An algorithm takes you from one point to another with no detours. A heuristic helps you look, and its results depend partly on chance. In his phrase, it's an algorithm in a clown suit. So no line of code can ever violate a metaphor.

@chapter Writing, farming, building
@art letter-wastebasket
The commonest metaphor is writing code, like a casual letter, written start to finish. For one person or a small project, it's adequate. Beyond that it fails. Software involves many people, it's changed for years after release, and it often does better to reuse than to be original.

@quote text="Plan to throw one away; you will, anyhow." cite="Fred Brooks, The Mythical Man-Month, 1975, as quoted in Code Complete, Chapter 2"
Fred Brooks once advised: plan to throw one away, you will anyhow. McConnell calls that poor advice for a major system. And by nineteen ninety five, Brooks himself had moved to incremental development.

@art pearl-accretion
Farming, plant a little and grow a little, is a good technique with a poor image. It suggests you've no control. McConnell prefers accretion, the way an oyster makes a pearl. Build the simplest version that runs, a skeleton calling dummy classes, and replace the dummies a piece at a time.

@art doghouse-and-house
And building says even more. A doghouse takes an afternoon. A house needs an architect, blueprints and inspections. Planning grows with what you build, and moving a load bearing wall costs more than moving a partition. Since metaphors are heuristics, you can use several at once.

@chapter Count it
@art share-bar
Chapter one's list makes a count possible. On the lesson's small project, an illustration of one thousand hours, four activities are construction.

@math heading="Construction's share" items="120 + 320 + 130 + 90 = 660 hours@one hundred and twenty;;660 / 1000 = 33/50 = 66%@six hundred and sixty over;;coding and debugging: 320 / 1000 = 8/25 = 32%@coding and debugging"
Detailed design, one hundred and twenty, coding and debugging, three hundred and twenty, unit testing, one hundred and thirty, and integration, ninety. That's six hundred and sixty hours. Six hundred and sixty over a thousand is thirty three fiftieths, sixty six percent. And coding and debugging, the largest entry, is eight twenty fifths, thirty two percent. Less than half of construction.

@chapter Where people slip
@list heading="Common slips" items="Writing software like a letter@The first|Treating construction as typing@The second|Hunting for the one right metaphor@The third"
The first slip is writing software like a letter, and throwing it away when it comes out wrong. The second is treating construction as typing in a finished design. And the third is hunting for the one right metaphor. Metaphors improve from worse to better, and you keep several.

@chapter Try it
@words text="7 activities · 300 hours" sub="mark each one, then find the share"
Your turn. The lesson gives a small project with seven activities: requirements, detailed design, coding, code review, unit testing, system testing and user interface design. Mark each one by section one point one's lists, and state construction's share as a fraction and a percentage. Two of them deserve a second look.

@end text="Mark a project, count its share"
You can mark the activities and let the lab add the hours, on Learn. That's learn dot get er done dot I O.
