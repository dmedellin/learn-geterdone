---
format: long
lesson: ddd-supple-design/angles-of-attack
title: Angles of Attack: where to start making a design supple
thumb: Carve off one clean piece
---

@chapter Choose a target
@title text="Angles of Attack" sub="Domain-Driven Design, Chapter 10" art=thumb
Chapter ten has offered a set of techniques, and Evans admits the design they aim at is difficult. Nobody can look at a large system and decide to make it supple. You have to choose targets. He gives two broad approaches.

@quote text="It is more useful to make a big impact on one area, making a part of the design really supple, than to spread your efforts thin." cite="Evans, Domain-Driven Design, Chapter 10"
And he's clear about where effort goes. It is more useful to make a big impact on one area, making a part of the design really supple, than to spread your efforts thin.

@chapter Carve off a subdomain
@art carve-module
The first approach is to carve off subdomains. Some part may be specialised mathematics, and can be separated. Rules that restrict state changes can be pulled into a small framework where they're declared. Each step leaves a clean new module, and a smaller, clearer remainder, partly written in the carved module's terms.

@chapter Draw on a formalism
@art formalism-shelf
The second is to draw on established formalisms. You can't invent a tight conceptual framework every day, but many fields have systems refined over long periods. Accounting is one. Evans's favourite is mathematics. Many domains have a little arithmetic in them somewhere, so look for it and dig it out.

@chapter Shares Math
@art shares-pie
His example returns to the syndicated loan from Chapter eight. A payment had to be divided among the lenders by their shares, and the first design calculated the division and changed the loan in one method. Evans separates the query from the command. Then he finds the missing concept: shares as parts of one whole.

@list heading="What made it supple" items="Logic in immutable values@immutable values|Simple commands with assertions@simple commands|Concepts decoupled@decoupled|A familiar formalism@familiar formalism"
That became a value object, with addition and subtraction closed under it, and a proration that takes an amount. What made it supple? Complex logic in immutable values. Simple commands, characterised by assertions. Concepts decoupled. And a familiar formalism.

@words text="Invented, or already known?"
An invented protocol for shares could have been supple too, he says. But it would have had to be invented, which is hard and uncertain, and then learnt by everyone who met it. Arithmetic is already known.

@chapter A bakery's quantities
@art flour-sacks
Now a bakery's model, written for the lesson. Quantities of flour, butter and loaves, with their units and conversions, grew up wherever they were first needed: some beside the orders, some beside production.

@code block=1 lines=1-16 focus="3-4@an amount in a unit|9-12@plus|13-15@times"
The carve moves them into a module of their own. Here's the arithmetic: an amount in a unit, with plus converting the other quantity, and times for batches.

@code block=2 lines=1-3 focus="2@times batches|3@plus the starter feed"
And the production code can now say what it means. The flour for a day's bake is the flour per batch, times batches, plus the starter feed. It reads as a definition.

@math heading="14 dependencies" items="tangled, 2 modules:  8 inside · 6 across · share 4/7 · 1 cycle@Tangled;;carved, 3 modules:  9 inside · 5 across · share 9/14 · no cycle@Carved"
The lab counts both packagings of the same fourteen dependencies. Tangled, in two modules: eight inside, six across, a share inside of four sevenths, and one cycle, orders and production, because each side holds part of the arithmetic. Carved, in three modules: nine inside, five across, a share of nine fourteenths, and no cycle.

@art tangled-cycle
That tangled cycle exists because each side holds part of the arithmetic the other uses. Put all of it in one place, and the loop has nowhere to come from.

@chapter The shape, not the share
@art dependencies-inward
Look at the five that cross. Three point into quantities, and two run from production to orders. Nothing points from quantities outward, and nothing from orders back to production. So no loop.

@words text="A cycle gone, a module that depends on nothing"
The share inside rose by only one dependency, and that's not what the carve was for. What changed is shape. A cycle gone, and a module every other one uses. Whether the bakers would recognise its rules is a question the count can't ask.

@chapter Where people slip
@list heading="Common slips" items="Making it all supple at once@The first|Inventing a protocol@The second|Measuring a carve by the share inside@And the third"
The first slip is trying to make the whole design supple at once. The second is inventing a protocol when an established formalism fits. And the third is measuring a carve by the share of dependencies inside modules. Here it barely moves, and in the exercise it falls.

@chapter Try it
@code block=3 lines=1-9 focus="1-4@dependencies|5-6@tangled|7-9@carved"
Your turn. A clinic's model, with these dependencies. Tangled, it has two modules, booking and staff. Carved, a third module, time, holds the time slot and the duration. For each packaging, give the dependencies inside modules, those across, and the module level cycles.

@end text="Carve off one clean piece"
Enter both packagings in the lab to check, on Learn. That's learn dot get er done dot I O.
