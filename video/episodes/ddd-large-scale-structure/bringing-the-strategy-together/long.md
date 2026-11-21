---
format: long
lesson: ddd-large-scale-structure/bringing-the-strategy-together
title: Bringing the Strategy Together: contexts, distillation and structure on one project
thumb: Assess before you choose
---

@chapter Three tools, one project
@title text="Bringing the Strategy Together" sub="Domain-Driven Design, Chapter 17" art=thumb
Once a team has met all three strategic principles, the questions come. How does a structure coexist with a Context Map? Where do the building blocks fit? And what do you do first?

@art three-tools
Evans's first answer is that none of the three, context, distillation or large scale structure, is an alternative to the others. They complement one another, and interact in many ways.

@chapter Structure and contexts
@art structure-inside-context
Chapter sixteen showed responsibility layers inside a single context, which is common and keeps things simple. A structure held within one context raises how much complexity a single model can carry. But often the harder problem is how separate contexts fit together, and then the structure can organise the Context Map itself.

@art legacy-in-layers
A legacy system that ignores your layers doesn't defeat them. Say which layers its services fall in, which describes its scope and role concisely. If it's reached through a facade, design each of the facade's services to sit in one layer.

@words text="A different structure in every context?" sub="possible, and it erodes what's shared"
Since each context is its own name space, different contexts could use different structures. Evans allows it, and warns that going far down that road erodes what a structure is for: a set of concepts the whole project shares.

@chapter Structure and distillation
@art core-layering
The two help each other. A structure can show how the modules of the Core Domain relate to each other, and to the generic subdomains. And a structure can itself be part of the core. A layering into potential, operations, policy and decision support may be an insight fundamental to the business.

@chapter Assessment first
@list heading="Six questions" items="Can a consistent Context Map be drawn?@Context Map|Is there a rich Ubiquitous Language?@language|Is the core named, with a vision?@Core Domain|Does the technology help?@technology|Do the developers have the skill?@technical skill|Do they know the domain?@know the domain"
Before choosing a strategy, find out where the project stands. Draw a Context Map, and see if a consistent one can be drawn. Listen to how language is used. Ask whether the Core Domain has been named, with a vision statement. Ask whether the technology helps. Whether the developers have the technical skill. And whether they know the domain, and find it interesting.

@quote text="You know less about this project right now than you ever will in the future." cite="Evans, Domain-Driven Design, Chapter 17"
Evans expects imperfect answers. You know less about this project right now than you ever will in the future. But first answers already show what most urgently needs doing, and they're refined as insight grows.

@chapter A bakery chain's effort
@art bakery-contexts
Now the count, for the third question. A bakery chain's system has six contexts. Bake planning, turning orders and forecasts into each shop's overnight bake, is the core. Shop orders and wholesale accounts support it. Payments, the staff rota and the ledger export are generic, and the ledger export is bought.

@math heading="as-found: 74 weeks built" items="core: 20/74 = 10/37 ≈ 27.0%@Twenty are on the core;;generic built: 30/74 = 15/37 ≈ 40.5%@thirty;;strongest on core: 1 of 4@one of the four;;buying frees 30 weeks@free thirty"
Only built parts count, so that's seventy four weeks. Twenty are on the core, about twenty seven per cent. Thirty are on generic parts, about forty and a half. One of the four strongest developers is on the core, and three on generic parts. Buying the two generic parts built in house would free thirty weeks.

@math heading="after-assessment: 54 weeks built" items="core: 30/54 = 5/9 ≈ 55.6%@thirty weeks;;generic built: none@none on generic;;strongest on core: 3 of 4@three of the strongest"
One possible response buys payments and the rota. The core gets thirty weeks and three of the strongest developers, and shop orders gets the fourth. Fifty four weeks built, five ninths on the core, none on generic parts.

@art effort-shift
The counts say where effort went. Whether the bought payment system fits the chain, and whether bake planning really is what sets it apart, are questions the assessment asks people, not tables.

@chapter Where people slip
@list heading="Common slips" items="Treating the three as rivals@The first|Strategy before assessment@The second|A different structure everywhere@And the third"
The first slip is choosing between contexts, distillation and structure as if they were rival approaches. The second is designing the strategy before assessing the present. And the third is using a different structure in every context, and calling it a strategy.

@chapter Try it
@words text="A seed bank's five parts" sub="forecast · requests · labels · email · accounting (bought)"
Your turn. A seed bank's system has five parts, one of them bought. Using the rule that only built parts count, find the weeks built in house, the share on the core and on generic parts, the strongest developers on the core, and the weeks that buying the remaining generic parts would free.

@end text="Assess first"
Type the table into the lab to check, on Learn. That's learn dot get er done dot I O.
