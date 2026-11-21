---
format: long
lesson: code-complete-high-quality-code/design-heuristics-and-information-hiding
title: Information hiding: ask what each module should keep secret
thumb: What should I hide?
---

@chapter The question
@title text="Design Heuristics and Information Hiding" sub="Code Complete, chapter 5" art=thumb
If design is heuristic, the obvious next question is: which heuristics? Chapter five gives a long list, and then singles one of them out.

@quote text="Information hiding is a particularly valuable concept. Asking ‘What should I hide?’ settles many difficult design issues." cite="McConnell, Code Complete, 2nd ed., Chapter 5, p. 123"
Information hiding is a particularly valuable concept. Asking what should I hide settles many difficult design issues.

@chapter The heuristics
@list heading="Some of the heuristics" items="Form consistent abstractions@abstractions|Encapsulate implementation details@encapsulating|Hide secrets@Hide secrets|Identify areas likely to change@likely to change|Keep coupling loose@coupling loose"
Section five point three's list includes finding real world objects, forming consistent abstractions, and encapsulating implementation details. It also says hide secrets, identify areas likely to change, keep coupling loose, and look for common design patterns.

@chapter A story with people in it
@art parnas-brooks
Information hiding has a history. David Parnas introduced it in a nineteen seventy two paper on how to divide a system into modules. Fred Brooks argued against it in The Mythical Man Month. Twenty years on, in the anniversary edition, he took it back.

@quote text="Parnas was right, and I was wrong about information hiding" cite="Fred Brooks, 1995, as quoted in Code Complete, Section 5.3"
In his words, Parnas was right, and I was wrong about information hiding. The book adds that Barry Boehm found it powerful for eliminating rework, especially when requirements change.

@chapter Secrets
@art id-counter
The idea is that each module is characterised by the design decisions it hides from the others. McConnell's example is an object id made by incrementing a global counter wherever an object is created. That spreads one decision through every creation site. One routine that hands out the next id keeps it in one place.

@list heading="Two kinds of secret" items="Hiding complexity@hiding complexity|Hiding sources of change@sources of change"
Secrets come in two kinds. Hiding complexity, so you don't have to think about it. And hiding sources of change, so that a change stays local.

@art change-boundary
For areas likely to change, there are three steps. Identify the items likely to change. Separate each into its own class. And isolate it behind an interface that doesn't change with it. Business rules, hardware, input and output, and data size limits are the usual suspects.

@chapter Count who knows
@art exposed-format
The lesson's lab counts this. In the exposed design, five modules, invoice, report, export, audit and backup, each read a CSV file format themselves. And the user interface uses report.

@math heading="Change the CSV format" items="exposed: direct 5 · reached 6@five modules know;;hidden: direct 1 (store) · reached 7@one module, store;;modules to edit: 5 → 1@five to one"
Change the format, and five modules know it directly, and six are reached, counting the user interface. Now hide the format inside one module, store, which the five use. Directly, one module, store, knows it, and seven are reached. The modules you'd have to edit fell from five to one.

@art hidden-format
Notice the total went up by one, because store is new. Hiding didn't shrink the graph. What fell is the number of modules whose code knows the secret, and that's the number the chapter cares about.

@chapter Where people slip
@list heading="Common slips" items="Expecting hiding to mean fewer dependencies@The first|Skipping the hiding for speed@The second|Equating private fields with a hidden secret@the third"
The first slip is expecting information hiding to mean fewer dependencies. The second is skipping it for speed, a worry the chapter calls premature. And the third is equating private fields with a hidden secret.

@art private-leak
That last one is worth a picture. If store hands back the raw line, and every caller splits it on commas, then store's fields are private, but its secret is public. Every caller still knows the format. The question is what a module hides, not which keywords it uses.

@chapter Practice, and how much
@list heading="Design practices" items="Iterate@Iterate|Divide and conquer@divide and conquer|Top down and bottom up@top down|Prototype@prototypes|Design with others@with others|Capture it cheaply@capture"
Section five point four turns to practice. Iterate. Divide and conquer. Work top down and bottom up, which complement each other. Build experimental prototypes. Design with others. And capture the design cheaply, in comments, on a wiki, or in a photo of the whiteboard.

@words text="Wrong every time" sub="every last detail · nothing at all"
How much design is enough? A judgement call, section five point five says. But two amounts are wrong every time: designing every last detail, and designing nothing at all.

@chapter Try it
@code block=1 lines=1-21 label=Java focus="3-6@takes the date apart|10-13@Shipping|17-20@Members"
Your turn. Three routines in three classes read a date stored as text. Billing takes the date apart by character position. So does Shipping, and so does Members. Name the secret all three know, say which one routine should know it, and count the routines that would change if the format gained dashes, before and after.

@end text="Ask what to hide"
You can count who knows a secret, and who a change reaches, in the lab on Learn. That's learn dot get er done dot I O.
