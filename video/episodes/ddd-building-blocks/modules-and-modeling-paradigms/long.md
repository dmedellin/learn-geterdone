---
format: long
lesson: ddd-building-blocks/modules-and-modeling-paradigms
title: Modules in Domain-Driven Design: package by concept, not by tier
thumb: Modules are chapters
---

@chapter Why modules
@title text="Modules and Modeling Paradigms" sub="Domain-Driven Design, Chapter 5" art=thumb
Everybody uses packages. Evans's complaint is that hardly anyone treats them as part of the model.

@art two-views
The main reason for modules, he says, isn't technical. It's cognitive overload. Modules give two views of a model: the detail inside one module without the whole, or the relationships between modules without the detail.

@words text="Low coupling, high cohesion" sub="a fact about minds"
The familiar rule, loose coupling between modules and cohesion inside, is usually explained as a technical metric. Evans reads it as a fact about minds. A person can think about only so many things at once, and fragments of ideas are as hard to follow as an undivided soup.

@chapter Chapters of a story
@quote text="If your model is telling a story, the MODULES are chapters." cite="Evans, Domain-Driven Design, Chapter 5"
So here's his image. If your model is telling a story, the modules are chapters.

@art concept-modules
Let each module hold concepts that belong together. Low coupling often follows. When it doesn't, change the model so the concepts separate. And give the modules names that enter the ubiquitous language, so a conversation with an expert can start from one.

@art stale-packages
Agile modules is about change. Modules ought to evolve with the model, and seldom do, because moving them is disruptive. So module names often describe a much older model than the classes do, and early mistakes harden.

@chapter Tiers pull concepts apart
@art tiered-split
Then the pitfall. Keeping the domain in its own layer is useful. Splitting each domain object into tiers, data in one package and logic in another, is not. On one project Evans describes, every concept was split four ways. Developers hardly ever changed a module, and what shipped was an anemic model.

@words text="One concept, one module" sub="unless it really runs on different servers"
His advice: use packaging to separate the domain layer, and otherwise keep all the code for one concept in one module, unless it really is deployed to different servers.

@chapter Package a seed bank
@code block=1 lines=1-22 label=Java focus="1@package|3@imports|5-21@GerminationTest"
Here's a seed bank, with three concepts: accessions, germination testing, and distribution. This class lives in the testing package, and imports the accessions module it depends on. GerminationTest keeps its data and its behaviour together.

@math heading="seed-bank-two-ways · 9 dependencies" items="by tier: 4 inside · 5 across = 4/9@by tier;;by concept: 7 inside · 2 across = 7/9@by concept;;no cycles in either@neither"
The lab packages one model two ways at once. By tier, logic and data, four of nine dependencies stay inside modules and five cross. By concept, seven stay inside and two cross. Neither has a cycle.

@art logic-to-data
Every crossing in the tier packaging is one concept's logic reaching its own data. That's the very high coupling between the halves of a split object that Evans warns about.

@math heading="accession-knows-shipments · 10 dependencies" items="by concept: 7/10 inside, one cycle@a cycle;;by tier: 5/10 inside, no cycle@five of ten"
Add one link: an accession that knows its shipments. By concept, seven of ten stay inside, and there's now a cycle: accessions to distribution to testing and back. By tier, five of ten, with no cycle, since logic only ever uses data.

@words text="Turn the link round" sub="a shipment names its accession"
That doesn't mean the tiers were better. It means the new link tangles three concepts. The remedy is in the model: turn the link round, so a shipment names its accession, or find the concept that would hold it.

@chapter Paradigms
@art mixed-paradigms
Evans closes the chapter on paradigms. Objects predominate for good reasons, but a domain model needn't be an object model. Mixing in a rules engine is appealing and hard. The common failure is object storage beside an unconnected set of rules. His advice: exhaust the dominant paradigm first, lean on the ubiquitous language, and be sceptical of the extra tool.

@chapter Where people slip
@list heading="Common slips" items="Packages as a filing system@The first|A package per technical tier@The second|Objects must model everything@And the third"
The first slip is treating packages as a filing system for the code. The second is splitting each concept into technical tiers, a package for each. And the third is concluding that objects must model everything.

@chapter Try it
@words text="by kind · by concept" sub="a bakery's six elements, seven dependencies"
Your turn. A bakery's six elements, packaged by pattern kind and by concept. Count the dependencies inside and across modules for each, and look for a cycle. Then name one change to the model that would remove the cycle you find.

@end text="Package it two ways"
Check your counts in the lab, on Learn. That's learn dot get er done dot I O.
