---
format: long
lesson: enterprise-patterns-layers-and-performance/enterprise-applications
title: What makes an application an enterprise application?
thumb: Business rules aren't logic
---

@chapter The starting point
@title text="Enterprise Applications" sub="Patterns of Enterprise Application Architecture, Preface and Introduction" art=thumb
Martin Fowler's book on enterprise application architecture starts from a joke that isn't really a joke. It's about the phrase business logic.

@quote text="I find this a curious term because there are few things that are less logical than business logic." cite="Fowler, Patterns of Enterprise Application Architecture, Introduction"
I find this a curious term, he writes, because there are few things that are less logical than business logic. That sentence holds the whole book's starting point. The hard part isn't clever algorithms. It's a lot of shared data, and a lot of rules nobody can derive.

@chapter How to read it
@words text="Narratives: read through · Patterns: look up"
The Preface begins with a leasing system Fowler worked on in nineteen ninety nine, whose rules grew one won deal at a time. The book is written for that situation, in two parts. The narrative chapters are meant to be read from start to finish. The patterns are a reference you dip into.

@chapter Architecture
@art layer-stack
Fowler is wary of the word architecture. He says it mostly signals importance. People agree on little, except two things: how a system is divided into its parts at the top, and the decisions that would be hard to reverse. His favourite architectural pattern is layers, and the book is about dividing an enterprise application into them.

@chapter The marks of the kind
@art data-archive
So what makes an application enterprise? First, the data is persistent. It's kept for years, outlives the hardware, the operating system and the compiler, and gets migrated whenever the application is replaced. And there's a lot of it. A moderate system, Fowler says, holds over one gigabyte in tens of millions of records.

@art many-screens
Many people use it at once, through many screens. There's batch processing that's easy to forget.

@art tangled-systems
And it lives among other systems, built at different times with different technologies, which disagree even about what a customer is.

@art branching-rule
Then come the rules. They're given to you, and changeable only by political effort. His example is a salesman who agreed to move one customer's payment to win the business. A few thousand one off cases like that add up to what he calls business illogic.

@chapter Three kinds
@list heading="Three points on a large plane" items="Online retailer@an online retailer|Leasing system@a leasing system|Expense tracker@a small company's"
Fowler refuses a single answer. He sets out three examples: an online retailer, with huge numbers of users and fairly simple logic, which must scale. A leasing system, with at most a hundred or so users at once, but complicated, arbitrary rules. And a small company's expense tracker, simple in every way, except that it must be built quickly and may grow.

@art three-kinds
Each has different difficulties, so no one architecture suits all three. Fowler says alarm bells ring for him when someone says always do this. Much of the book is about choosing between alternatives.

@chapter Counting the illogic
@code block=1 lines=1-19 label=Java focus="4-6@government customers|7-9@northern customers|10-14@retail or online|15-17@nobody but government"
Here's a due date rule written for the lesson, with four invented agreements in it. Government customers get fifteen more days. Long standing northern customers get ten. Retail or online customers invoiced late in the month get five. And nobody but government waits past day sixty.

@math heading="Decision points" items="1 + if 5 + && 2 + || 1@one, plus;;= 9@nine in all;;plain rule: 1@the plain rule"
Count decision points: one, plus one for each if, and, and or. That's one, plus five ifs, two ands, and one or: nine in all. The not on line fifteen adds nothing, since it makes no new branch. Take every agreement out and the plain rule has just one.

@words text="8 points = 4 agreements" sub="none derived from the plain rule"
So the four agreements cost eight points between them, and none could be derived from the plain rule. That's not bad code. It's how much a reader has to learn case by case.

@chapter Patterns
@words text="The example is not the pattern"
Fowler starts from Christopher Alexander: a pattern is a recurring problem and the core of its solution, which never comes out quite the same way twice. He adds that it's advice rooted in practice, discovered rather than invented. And he insists the example is not the pattern. Patterns are half baked, and you finish them in your own project.

@chapter Where people slip
@list heading="Common slips" items="Expecting the special cases to go@The first|Thinking enterprise means big@The second|Copying the example as the pattern@And the third"
The first slip is expecting a principle to make the special cases go away. They won't. The second is thinking enterprise means big. Fowler's own list includes a small expense tracker. And the third is copying a pattern's example as if it were the pattern.

@chapter Try it
@code block=3 lines=1-17 label=Java focus="4@more than ten days|7@flagged|10@charity|13@new account"
Your turn. Here's a late fee routine from the lesson's exercise. Count its decision points by the same rule, and write the breakdown the way the lab does. Then name the agreement each if encodes: more than ten days late, over thirty or flagged, a charity, and a new account with no payments yet.

@end text="Count the agreements yourself"
You can paste a routine into the lab and watch its decision points add up, on Learn. That's learn dot get er done dot I O.
