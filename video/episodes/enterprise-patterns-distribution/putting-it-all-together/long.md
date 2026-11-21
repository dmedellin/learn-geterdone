---
format: long
lesson: enterprise-patterns-distribution/putting-it-all-together
title: Putting it all together: Fowler's whole book in one chapter
thumb: Choose the domain logic first
---

@chapter Advice, not a recipe
@title text="Putting It All Together" sub="Patterns of Enterprise Application Architecture, Chapter 8" art=thumb
Chapter eight sweeps the whole book together. Fowler even wonders whether it was needed, since it repeats earlier advice. He keeps it to put the discussion in context, with a warning.

@quote text="Use this advice to prod your thinking, but don't use it as a replacement for your thinking." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 8"
Use this advice to prod your thinking, but don't use it as a replacement for your thinking. You know your own project far better than he can.

@words text="Not cast in stone" sub="continuous integration · test-driven development · refactoring"
And your decisions aren't cast in stone. Architectural refactoring is hard, but possible. He asks you to consider three practices: continuous integration, test driven development, and refactoring. They make it easier to change your mind, and you'll need to.

@chapter Domain first
@art domain-first
The central decision is the domain logic. The strongest force is its complexity, which nobody can yet measure. The second is how hard the connection to the database is. Every decision below is shaped by this one.

@list heading="The central decision" items="Transaction Script: simplest, duplicates@Transaction Script|Domain Model: complex logic, hard to map@Domain Model|Table Module: in between, Record Sets@Table Module"
Transaction Script is the simplest, but handles complex logic badly and invites duplication. Domain Model handles really complex logic better than anything, but is hard to learn and hard to map to tables. Table Module sits between them, and fits tools that work with Record Sets very well.

@art choice-tree
Then the data source follows. A Transaction Script takes a Row or Table Data Gateway. A Table Module takes a Table Data Gateway. A fairly simple Domain Model can use Active Record. A complex one needs Data Mapper, and then Unit of Work above all.

@words text="One process if you can" sub="if not, a Remote Facade and Data Transfer Objects"
For presentation, prefer an HTML browser where you can, with Model View Controller underneath. And then the sentence this course turns on. Run everything in one process if you can. If you can't, wrap the domain layer in a Remote Facade, and talk to the web server with Data Transfer Objects.

@chapter Dated, by Fowler
@words text="Early 2002" sub="technologies change faster than patterns"
The platform advice Fowler dates himself. He's writing in early two thousand and two, and technologies change faster than patterns. Stored procedures are an optimisation, not a principle. And web services are for integrating applications, not building one. Remember the First Law.

@chapter Price one request
@code block=1 lines=1-11 label=Java focus="4@opens a Unit of Work|5@finds the cart|6@check it out|7-8@registers|9@commits"
Here's one request through those layers. A service method opens a Unit of Work, finds the cart through a mapper, lets the domain check it out, registers the new order and the changed cart, and commits. Every one of those calls is cheap, if the layers share a process.

@art layer-calls
One request makes one call from the browser to the page, two from the page to the service, forty from the service to the domain, twenty five from the domain to the mappers, and six to the database. Seventy four in all, at two thousand microseconds a remote call, and one a local one.

@math heading="three deployments" items="web-and-database: 7 remote · 14,067 µs · ≈ 190.1×@seven remote calls;;service-split-off: 9 remote · 18,065 µs@nine;;domain-split-off: 47 remote · 94,027 µs@forty seven"
Put the browser and the database on their own nodes: seven remote calls, fourteen thousand and sixty seven microseconds, about a hundred and ninety times one node. Split off above the service: nine remote calls. Split off under the service: forty seven, and ninety four thousand and twenty seven microseconds.

@art boundary-above-service
So a boundary above the Service Layer is crossed by a few coarse calls, two more than the seven.

@art boundary-under-service
A boundary under it adds forty, because it's crossed by the domain's many fine calls. That's the arithmetic behind the advice to wrap the domain in a Remote Facade.

@chapter Other schemes
@art other-schemes
Last, Fowler maps five other layering schemes onto his three. The Brown model's extra layers he reads as Application Controller and Data Mapper. Microsoft DNA's record sets are a Record Set acting as a Data Transfer Object. To him, every mediating layer is an optional extra, added when a layer gets too complex.

@chapter Where people slip
@list heading="Common slips" items="Read it as a decision procedure@The first|The technology advice is the point@The second|Other schemes contradict the three layers@And the third"
The first slip is reading the chapter as a flowchart. The decisions remain yours. The second is taking the technology advice for the point. It's dated, and the patterns aren't. And the third is thinking the other layering schemes contradict the three layers. Fowler maps each one onto them.

@chapter Try it
@list heading="A phone app's screen" items="app→facade 3 · facade→domain 30 · domain→mapper 20 · mapper→db 4@three|only the phone is remote@phone|remote 50,000 µs · local 1 µs@fifty thousand"
Your turn. A phone app calls a facade three times. The facade calls the domain thirty times, the domain calls mappers twenty, and the mappers call the database four. Only the phone is remote, at fifty thousand microseconds a call. Find the total, the ratio to one node, and the time if one facade method served the screen.

@end text="Price a deployment yourself"
You can move layers between nodes and price one request, on Learn. That's learn dot get er done dot I O.
