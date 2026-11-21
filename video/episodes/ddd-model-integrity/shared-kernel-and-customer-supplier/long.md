---
format: long
lesson: ddd-model-integrity/shared-kernel-and-customer-supplier
title: Shared Kernel and Customer/Supplier: two cooperative ways to connect contexts
thumb: Share a little, by agreement
---

@chapter Patterns as targets
@title text="Shared Kernel and Customer/Supplier" sub="Domain-Driven Design, Chapter 14" art=thumb
Chapter fourteen's relationship patterns are two things at once. Targets to move a relationship toward, and vocabulary to describe one that already exists. A real relationship that comes close to one can be named after it, with its differences noted.

@list heading="What decides among them" items="Control over the other model@control|How the teams cooperate@cooperate|How deeply they must integrate@deeply"
Evans names the variables. How much control you have over the other model. How the teams cooperate. And how deeply features and data must be integrated. The patterns run from the most cooperative to the least, and this lesson reads the first two.

@chapter Shared Kernel
@art racing-apart
Sometimes Continuous Integration costs more than it returns, because the team is too big, or lacks the skill or organisation. But teams that just race ahead on closely related applications can end up paying more for translation and retrofits than integration would have cost.

@art kernel-overlap
So choose a part of the domain model, with its code and schema, that two teams hold in common by explicit agreement. It's integrated less often than each team's own code, perhaps weekly where they merge daily. And at each integration, both teams' tests have to pass.

@quote text="This explicitly shared stuff has special status, and shouldn't be changed without consultation with the other team." cite="Evans, Domain-Driven Design, Chapter 14"
This explicitly shared stuff has special status, and shouldn't be changed without consultation with the other team. The kernel aims to reduce duplication, not end it.

@chapter Customer and supplier
@art one-way-flow
A different shape: one subsystem feeds another, the downstream one gives little back, and every dependency runs one way. The danger is political. An upstream team that downstream can veto is cramped. A downstream team at the mercy of upstream priorities is helpless.

@list heading="Make it formal" items="Downstream is a customer in planning@customer|Its needs are negotiated and budgeted@negotiated|Acceptance tests run upstream@acceptance tests"
So make it formal. In planning, the downstream team plays customer to the upstream team. Its needs are negotiated and budgeted, so everyone knows what's promised and when. And the two teams write automated acceptance tests of the interface, which the upstream team runs in its own suite.

@art planning-table
Evans marks two elements as crucial. The customer's needs come first, not a poor relation's begging. And the tests exist. His example is a yield analysis team taking data from a booking system. It works because both project managers report to one person. Such teams succeed, he says, when they share management, or really are customer and supplier.

@chapter A theatre's chain
@code block=1 lines=1-3 focus="1@share a kernel|2@programming's customer|3@the cafe"
Now the count. Programming and the venue share a kernel, the calendar of performances and spaces. The box office is programming's customer. And the cafe, which forecasts its stock from ticket sales, is the box office's customer.

@math heading="who a change reaches" items="change-programming: venue, boxoffice, cafe = 3@season planners;;change-venue: programming, boxoffice, cafe = 3@venue team;;change-cafe: 0 models · 3 untouched@cafe changes"
When the season planners change their model, three must follow: venue, box office and cafe. When the venue team changes the kernel, it reaches programming, the kernel's other owner, and from there the box office and cafe. Three again. And when the cafe changes its forecasting model, nothing else changes.

@art kernel-two-way
That's the difference in direction. Neither side of a kernel is upstream of the other, so a change by either reaches both. A customer's change doesn't travel up to its supplier.

@art tests-catch
But read the counts carefully. The lab says what's connected, not what breaks. Under Customer Supplier, the box office still has to change when programming does. What the pattern adds is that the change was negotiated in planning, and the acceptance tests catch it before it reaches users.

@chapter Where people slip
@list heading="Common slips" items="Putting as much as possible in the kernel@The first|Tests that spare the downstream change@The second|Customer/Supplier between any two teams@And the third"
The first slip is putting as much as possible into the Shared Kernel. Every change to it needs consultation and both teams' tests. The second is thinking acceptance tests stop the downstream team from having to change. And the third is expecting Customer Supplier to work between any two teams.

@chapter Try it
@code block=2 lines=1-3 focus="2@also agreed to share"
Your turn. Suppose programming and the box office also agreed to share a kernel. The box office changes its model of a sale. Find the models that must change on this map, and then on the original one. And say in a sentence what the wider kernel costs the box office team.

@end text="Agree, then test both ways"
Load both maps into the lab to check, on Learn. That's learn dot get er done dot I O.
