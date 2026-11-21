---
format: long
lesson: ddd-life-cycle/refactoring-the-example-and-modules
title: Refactoring the cargo model: a query, modules and a new feature
thumb: Package by concept, not pattern
---

@chapter Three changes
@title text="Refactoring the Example, Modules and a New Feature" sub="Domain-Driven Design, Chapter 7" art=thumb
The second half of Chapter 7 changes a working design three times: once to remove contention, once to package it, and once to add a feature that depends on another system.

@chapter Pause for refactoring
@art contended-cargo
Here's the awkward transaction. Recording a handling event also updates the cargo's delivery history, so it involves the cargo's aggregate. It can fail or wait if someone else is editing that cargo. Yet logging an event is quick operational work that shouldn't contend.

@art query-not-collection
So Evans replaces the history's collection with a query on a new handling event repository. The event is added inside its own aggregate alone. The history holds nothing persistent, and can be derived when asked for. And the cycle stops being hard to maintain.

@words text="Same model, either design" sub="the change stayed inside one boundary"
He's careful about the cost. On an object database, following a collection is probably faster than a query. What he stresses is that both designs express the same model. Because the aggregates were drawn, the whole change stayed within the cargo's boundary, plus one new repository.

@chapter Modules
@art pattern-packages
Next, packaging. An imagined, enthusiastic reader of the book puts entities in one module, values in another, and services in a third. Unrelated objects are crammed together, and associations run between every pair of modules.

@quote text="The packages tell a story, but it is not the story of shipping; it is the story of what the developer was reading at the time." cite="Evans, Domain-Driven Design, Chapter 7"
Evans's verdict: the packages tell a story, but it is not the story of shipping. It is the story of what the developer was reading at the time.

@art concept-packages
His alternative groups the model by broad concepts: customers, shipping operations, and billing. Those names tell the company's story, and they join the team's language.

@chapter A new feature
@art translator
Then a new feature. The sales division keeps allocations, how much of each kind of cargo it will try to book, in its own software, and wants each booking checked. Evans won't let the booking application talk to that system directly. He writes one translating class, an anticorruption layer, named for its job: an allocation checker.

@words text="The rule moves into the checker" sub="allocated space vs. booked + new cargo"
And the rule that accepts a booking, allocated space against space already booked plus the new cargo, is domain logic. So it moves out of the booking application and into the checker, which also derives the kind of cargo. The segment rules belong with the object that knows them.

@chapter Count the box office
@list heading="By concept" items="customers@customers|venues@venues|programme@programme|sales@sales"
Now the box office's model, thirteen elements and fourteen dependencies, packaged two ways. By pattern: entities, values, repositories and services. And by concept: customers, venues, programme, and sales.

@math heading="two-packagings · 14 dependencies" items="by pattern: 5 inside · 9 across = 5/14@by pattern;;most coupled: entities–values, 4@entities and values;;by concept: 9 inside · 5 across = 9/14@by concept;;most coupled: programme–sales, 2@programme and sales"
By pattern, five of the fourteen are inside a module and nine cross. The most coupled pair is entities and values, with four. By concept, nine are inside and five cross, and the most coupled pair is programme and sales, with two. Neither has a cycle.

@math heading="quota-feature · 16 dependencies" items="by pattern: 6 inside · 10 across = 3/8@by pattern;;by concept: 10 inside · 6 across = 5/8@by concept;;programme–sales: 3@now share"
Add a ticket agency that sells part of each performance, through a QuotaChecker service and an AgencyClient behind it. By pattern, six inside and ten across, three eighths. By concept, ten inside and six across, five eighths. And programme and sales now share three.

@art story-modules
The counts show where each packaging puts related elements, not which is right. By concept, the dependencies that cross are the ones the business has: sales depending on the programme. A different reading of the domain could draw the concepts differently, as Evans says of his own.

@chapter Where people slip
@list heading="Common slips" items="Package by building-block pattern@The first|The refactor is simply better@The second|The application applies the other system's rule@And the third"
The first slip is packaging by the building block patterns because the book names them. The second is thinking the refactored design is simply better. Evans weighs it. And the third is letting the booking application apply the other system's rule.

@chapter Try it
@words text="by pattern · by concept" sub="a seed bank: 7 elements, 8 dependencies"
Your turn. A seed bank's model, seven elements and eight dependencies, packaged by pattern and by concept. For each packaging, count the dependencies inside a module and across, and give the share inside.

@end text="Package it both ways"
Check your counts in the lab, on Learn. That's learn dot get er done dot I O.
