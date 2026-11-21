---
format: long
lesson: ddd-distillation/cohesive-mechanisms
title: Cohesive Mechanisms: when the how swamps the what
thumb: The model states, the mechanism solves
---

@chapter The how swamps the what
@title text="Cohesive Mechanisms" sub="Domain-Driven Design, Chapter 15" art=thumb
Hiding an algorithm behind a method with an intention revealing name is ordinary object design. It separates what is computed from how. But sometimes a computation grows so large that the methods working out an answer hide the methods that say what the problem is.

@quote text="This proliferation of procedures is a symptom of a problem in the model." cite="Evans, Domain-Driven Design, Chapter 15"
This proliferation of procedures is a symptom of a problem in the model. So Evans's first remedy isn't the pattern at all. It's to refactor toward a deeper model in which the computation becomes simple.

@chapter A framework of its own
@art extract-mechanism
Only sometimes does part of the mechanism turn out to be coherent in its own right. Then give that part a small framework of its own. Look first for a known formalism, or a textbook family of algorithms. And let the model reach it only through operations named for what they answer.

@words text="Not a catch-all calculator"
He's careful here. It won't cover all the messy computation, and he doesn't mean a catch all calculator. The domain classes say what the problem is. The framework works out the answer. And the core gets smaller and more declarative.

@chapter The organisation chart
@art org-graph
His example is an organisation chart. Questions like who in this chain of command may approve this turned out to be mostly about walking branches of a tree. A subcontractor built a small graph traversal framework, in standard graph vocabulary, and the model could simply say that people are nodes and their relationships edges.

@art muddied-model
Leaving the traversal inside the model would have cost twice. It would have tied the model to one way of solving the problem. And worse, it would have muddied the model.

@chapter Mechanism or subdomain?
@list heading="Two ways to unburden the core" items="Generic subdomain: a model of part of the domain@generic subdomain|Cohesive mechanism: solves what the models pose@cohesive mechanism"
Both patterns take weight off the core. A generic subdomain is an expressive model of part of the domain, only less central. A cohesive mechanism represents no part of the domain. It solves a hard computational problem the models pose. The line is often blurred at first.

@art proprietary-core
The exception is a proprietary algorithm that's itself part of the software's value, like the risk rating algorithms on a project of his at an investment bank. That belongs in the core. And a year after the graph framework, other developers folded it back into the entities, keeping its interface. Such circles are common, and they usually end in a deeper model.

@chapter A school timetable
@art clashing-lessons
Now a domain written for the lesson: a school timetable. Its rule is that two lessons clash if they share a teacher, a room or a class of pupils, and their times overlap.

@code block=1 lines=1-18 focus="2-6@own terms|10-16@knows nothing of schools"
That rule is stated in the timetable's own terms. And the arithmetic of time intervals sits in a small intervals package that knows nothing of schools.

@math heading="four-changes: modules touched" items="times in minutes:  tangled 3 · separated 1@in minutes;;meeting periods don't clash:  1 · 1@only meet;;five periods a day:  1 · 1@five periods;;cleaning gap:  2 · 2@cleaning gap"
The lab packages it twice. Tangled, the interval helpers live where they were first needed. Separated, they sit together. Storing times in minutes touches three modules tangled, one separated. Letting periods that only meet not clash touches one either way, and so does capping a teacher at five periods. A ten minute cleaning gap touches two either way.

@math heading="totals" items="tangled: 7 touches · 2 confined@seven;;separated: 5 touches · 3 confined@five"
So, seven module touches tangled and five separated. Two of the four changes confined to one module tangled, three separated.

@art arithmetic-confined
The change to the arithmetic is the one separation confines. Rule changes stay where the rules are. And the count is narrower than Evans's claim, which is about reading. In the separated design, clashes says what a clash is, and nobody has to read interval arithmetic to learn it.

@chapter Where people slip
@list heading="Common slips" items="A home for every computation@The first|Confusing it with a generic subdomain@The second|Mechanisms are never core, and stay apart@And the third"
The first slip is treating a mechanism as a home for every computation. The second is confusing it with a generic subdomain. And the third is assuming a mechanism must always stay out of the core, and stay separated for good.

@chapter Try it
@words text="(a) free periods of 30+ minutes · (b) inclusive interval ends"
Your turn. Two more changes. First, teachers see free periods only if a gap is at least thirty minutes, touching gaps and the teacher's can take rule. Second, interval ends become inclusive, touching overlaps, span and gaps. Find the modules each touches, tangled and separated, and the totals.

@end text="State the rule, solve elsewhere"
Replace the lab's changes with these and check, on Learn. That's learn dot get er done dot I O.
