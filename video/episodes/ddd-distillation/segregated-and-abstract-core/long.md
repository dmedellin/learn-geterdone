---
format: long
lesson: ddd-distillation/segregated-and-abstract-core
title: Segregated Core and Abstract Core: moving the core itself
thumb: Every arrow points in
---

@chapter Toward a declarative core
@title text="Segregated Core and Abstract Core" sub="Domain-Driven Design, Chapter 15" art=thumb
The value of distillation is seeing what you're doing. Parts of the core can be written declaratively, when the supporting design gives them a small language for stating the core's concepts and rules, while hiding how they're computed. Even then, not everything outside the core finds a good home.

@chapter Segregated Core
@art tangled-core
Start from entanglement. Elements that serve the core partly and support it partly. Core elements tightly coupled to generic ones. A core whose cohesion is weak or invisible. Factoring out generic subdomains clears some of it, but leaves the core tangled in the residue.

@quote text="What is done with the undifferentiated mass left behind is important, but not as important." cite="Evans, Domain-Driven Design, Chapter 15"
So work from the other direction. Pull the core's concepts away from everything that only helps them, and push the rest into other classes and packages. What is done with the undifferentiated mass left behind is important, but not as important.

@list heading="Roughly the steps" items="Identify a core subdomain@Identify|Collect it in a named module@new module|Cut out what isn't the concept@Cut out|Simplify its relationships@Simplify|Repeat@repeat"
Evans gives the steps. Identify a core subdomain. Collect its classes in a new module whose name says what unites them. Cut out the data and behaviour that don't express that concept, making references outward explicit. Simplify the new module's relationships, which never quite ends. Then repeat with the next.

@words text="Costs worth paying" sub="the whole team moves together"
He's plain about the costs. Segregation can break up a module that was nicely cohesive in another way, and leave links to closely coupled classes murkier. It's a lot of work across the system. And the whole team has to move together, under one definition of the core.

@chapter Abstract Core
@quote text="Consider slicing horizontally rather than vertically." cite="Evans, Domain-Driven Design, Chapter 15"
Where subdomains interact heavily, modules by subdomain leave many references crossing between them. Consider slicing horizontally rather than vertically. If most of the interaction can go through polymorphic interfaces that are fundamental concepts of the domain, factor those into a core module. The specialised modules then reference the core, and not each other.

@art meaningless-mess
This isn't mechanical. Moving every frequently referenced class into one module makes a meaningless mess. The real thing needs deep understanding, and usually considerable redesign.

@chapter Where to start refactoring
@art refactor-target
Evans rejects two answers for where a tangled system's refactoring should start. Anywhere, which works only for teams of top programmers. And wherever it hurts, which treats symptoms. His answer: when pain drives the work, check whether its root is in the core, and if so, fix that first. When you're free to choose, improve the core's factoring and segregation.

@chapter Counting the bike share
@math heading="18 dependencies" items="as history left them:  9 inside · 9 across · cycle stations, fleet, riders@As history;;segregated:  8 inside · 10 across · 7 across the core@Segregated"
Now the bike share's twelve classes and eighteen dependencies. As history left them, nine fall inside a module and nine across, and three modules lie on one cycle. Segregated, with the forecast, the plan and the move in a rebalancing module, eight fall inside and ten across. Seven cross the core's boundary.

@art cycle-through-core
The share inside went down, from a half to four ninths. That's the cost Evans names: the forecast had been comfortable in stations. And the cycles now pass through the core, since a station still depends on the forecast, which depends on a station. But the core's relationships are now in one place, explicit, and ready to work on.

@code block=1 lines=1-20 focus="2-6@Place|8-11@Demand Source|13-20@a move"
The abstract core preset is that work, and it's a redesign. Two interfaces, Place and Demand Source, carry the core's interactions. A station implements one and a trip the other. And a move carries a number of bikes between places.

@art vertical-horizontal
The lab packages that new model twice, to show what slicing horizontally means. Vertically, by subdomain, or horizontally, with the abstractions in a layer of their own.

@math heading="abstract-core, 17 dependencies" items="vertical:  10 inside · 7 across · a cycle@Sliced vertically;;horizontal:  11 inside · 6 across · no cycle@Sliced horizontally;;5 cross the core, all pointing in@all pointing in"
Sliced vertically, each interface sits with the class that implements it: ten inside, seven across, and a cycle. Sliced horizontally, both interfaces in the core: eleven inside, six across, no cycle. Five dependencies cross the core's boundary, all pointing in. The core depends on none of them.

@chapter Where people slip
@list heading="Common slips" items="Expecting every module to get more cohesive@The first|Moving the most-referenced classes@The second|Refactoring everywhere, or only where it hurts@And the third"
The first slip is expecting a Segregated Core to make every module more cohesive. The second is building an Abstract Core by moving the most referenced classes. And the third is refactoring everywhere at once, or only where it hurts.

@chapter Try it
@words text="A seed bank: when must stored seed be grown again?" sub="6 classes · 7 dependencies · packagings A and B"
Your turn. A seed bank, whose core is deciding when stored seed must be grown again. Six classes, seven dependencies, and two packagings. Find the dependencies inside and across modules in each, those across the core's boundary in packaging B, and any cycle between B's modules.

@end text="Slice horizontally"
Type both packagings into the lab, on Learn. That's learn dot get er done dot I O.
