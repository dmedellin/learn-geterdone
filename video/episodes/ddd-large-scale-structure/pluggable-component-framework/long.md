---
format: long
lesson: ddd-large-scale-structure/pluggable-component-framework
title: Pluggable Component Framework, and how restrictive a structure should be
thumb: One core, many plugs
---

@chapter A structure for a mature model
@title text="Pluggable Component Framework" sub="Domain-Driven Design, Chapter 16" art=thumb
This structure belongs to a mature model. Evans says it usually comes into play only after a few applications have been built in the same domain. Many applications, designed independently on the same abstractions, now have to work together.

@art pairwise-web
Translating between all their contexts limits integration. A Shared Kernel is impractical between teams that aren't close. And duplication raises the cost of everything.

@chapter The pattern
@art plug-hub
So make the Abstract Core's interfaces, and their interactions, the only contract. Any component that honours it can be swapped for another, and an application can work with a component without knowing which one it has. The hub is an Abstract Core inside a Shared Kernel. Behind each interface there may be a different context.

@art quilt
His example is a framework for semiconductor factories, where a vendor's new machine plugs into any application that keeps to the interfaces. And the chapter's opening image belongs here: the AIDS Memorial Quilt, tens of thousands of panels made by people working apart, held together by a few rules about each panel's purpose, size and durability.

@list heading="The downsides" items="Very hard to apply@very hard|Applications are limited@different idea|The core freezes@more or less stops"
Evans is frank about the downsides. It's very hard to apply, needing precise interfaces and a deep model. Applications with a different idea of the core find it in the way. And the core can't change without changing every component's protocol, so refactoring the core more or less stops. It should be neither the first structure a project applies, nor the second.

@chapter How restrictive?
@art loose-to-tight
Set the four structures on a line, from the loose metaphor to the restrictive framework. A tighter structure is more uniform, easier to interpret, and if it fits, pushes developers toward good designs. It also takes away flexibility they may need, especially across contexts built with different technologies.

@quote text="The most important contribution of the large-scale structure is conceptual coherence, and giving insight into the domain." cite="Evans, Domain-Driven Design, Chapter 16"
So resist the urge to build frameworks around a structure, and make every rule make development easier. The most important contribution of the large scale structure is conceptual coherence, and giving insight into the domain.

@chapter Refactoring toward a structure
@list heading="Keeping it affordable" items="Minimalism: start loose@Minimalism|Communication and self-discipline@self discipline|Restructuring yields supple design@Restructuring|Distillation lightens the load@Distillation"
A useful structure only comes from deep understanding, so it has to be refactored into the code as it's found. Minimalism: deal only with the gravest concerns, and start loose. Communication and self discipline, because no functional test depends on the structure. Restructuring yields supple design. And distillation lightens the load.

@art leather-jacket
Evans reports something he can't fully explain. A design that has had a structure is easier to restructure than one that never had one, even into a different kind. His image is a leather jacket that loosens with wear.

@chapter A museum group
@math heading="six applications" items="pairwise:  6·5/2 = 15 to build · 5 to change@Integrated pairwise;;framework:  6 to build · 1 to change@plugged into one framework;;ratios:  5/2 ≈ 2.5× · 5×@two and a half"
A museum group runs six applications: collections, exhibitions, outward loans, conservation, ticketing and the shop. All need an object, where it is, and its condition. Integrated pairwise, fifteen translators, and five to change when one application changes. Plugged into one framework, six, and one to change. Two and a half times as many to build, five times to change.

@math heading="twelve applications" items="pairwise:  66 to build · 11 to change@sixty six;;framework:  12 · 1@twelve;;ratios:  11/2 ≈ 5.5× · 11×@five and a half"
Pairwise cost grows with the square of the number of applications, the framework's in proportion to it. With twelve, it's sixty six against twelve to build, and eleven against one to change. Five and a half times, and eleven times.

@art core-change-reaches-all
What the count leaves out is Evans's main downside. A change to the core interfaces themselves reaches every component at once, twelve of twelve. That's why the core stops evolving. And it assumes a model deep enough to write the core in the first place.

@chapter Where people slip
@list heading="Common slips" items="A framework at the start@The first|A technical plug-in platform@The second|Tighter is always safer@And the third"
The first slip is reaching for a pluggable framework at the start of a project. The second is equating the pattern with a technical plug in platform. It's a way of organising responsibilities. And the third is assuming a more restrictive structure is always safer.

@chapter Try it
@words text="Nine applications, all exchanging data"
Your turn. Nine applications must all exchange data. Find the translators to build pairwise, two way and one way, and how many change when one application's model changes. Then the figures through one framework interface, and the components a change to that interface reaches.

@end text="Not the first structure, nor the second"
Set the lab to nine to check, on Learn. That's learn dot get er done dot I O.
